from __future__ import annotations

import json
import math
import os
from pathlib import Path
import time

import cv2
import numpy as np

from .config import app_dir
from .homography import Registration


class FeatureAtlas:
    """Persistent self-learning visual map atlas.

    Each learned keyframe contributes SIFT descriptors paired with *world-space*
    coordinates. A later screenshot can therefore be localized directly into the
    same world coordinate system even when the original static reference map does
    not contain an expansion region.

    The atlas never needs game memory or a remote service; it learns only from map
    pixels already rendered on the user's screen.
    """

    FORMAT_VERSION = 1

    def __init__(
        self,
        path: Path | None = None,
        *,
        max_query_width: int = 1500,
        max_features: int = 4200,
        sample_per_keyframe: int = 750,
        max_keyframes: int = 160,
        keyframe_spacing: float = 240.0,
    ):
        self.path = path or (app_dir() / "visual_atlas.npz")
        self.meta_path = self.path.with_suffix(".json")
        self.max_query_width = max_query_width
        self.sample_per_keyframe = sample_per_keyframe
        self.max_keyframes = max_keyframes
        self.keyframe_spacing = keyframe_spacing
        self.sift = cv2.SIFT_create(nfeatures=max_features)
        self.descriptors = np.empty((0, 128), np.float32)
        self.world_points = np.empty((0, 2), np.float32)
        self.keyframe_ids = np.empty((0,), np.int32)
        self.centers: dict[int, tuple[float, float]] = {}
        self.next_id = 1
        self.world_source = "unknown"  # static | free | unknown
        self.created_at = time.time()
        self.updated_at = self.created_at
        self.load()

    @property
    def ready(self) -> bool:
        return len(self.descriptors) >= 24

    @property
    def keyframe_count(self) -> int:
        return len(self.centers)

    def _resize_gray(self, image: np.ndarray) -> tuple[np.ndarray, float]:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        scale = 1.0
        if self.max_query_width and gray.shape[1] > self.max_query_width:
            scale = self.max_query_width / float(gray.shape[1])
            gray = cv2.resize(gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        return gray, scale

    def _features(self, image: np.ndarray):
        gray, scale = self._resize_gray(image)
        kp, des = self.sift.detectAndCompute(gray, None)
        if des is None or not kp:
            return gray, scale, [], None
        return gray, scale, kp, des.astype(np.float32, copy=False)

    @staticmethod
    def _transform_points(points: np.ndarray, H: np.ndarray) -> np.ndarray:
        if len(points) == 0:
            return np.empty((0, 2), np.float32)
        return cv2.perspectiveTransform(np.float32(points).reshape(-1,1,2), H).reshape(-1,2)

    def _center_world(self, image: np.ndarray, H_full_to_world: np.ndarray) -> tuple[float, float]:
        h,w = image.shape[:2]
        p = self._transform_points(np.array([[w/2.0,h/2.0]],np.float32), H_full_to_world)[0]
        return float(p[0]), float(p[1])

    def should_add(self, image: np.ndarray, H_full_to_world: np.ndarray) -> bool:
        center = self._center_world(image, H_full_to_world)
        if not self.centers:
            return True
        d = min(math.hypot(center[0]-c[0], center[1]-c[1]) for c in self.centers.values())
        return d >= self.keyframe_spacing

    def add_keyframe(
        self,
        image: np.ndarray,
        H_full_to_world: np.ndarray,
        *,
        source: str | None = None,
        force: bool = False,
    ) -> bool:
        if image is None or image.size == 0:
            return False
        if not force and not self.should_add(image, H_full_to_world):
            return False
        _gray, scale, kp, des = self._features(image)
        if des is None or len(kp) < 24:
            return False

        # Keep strongest, spatially diverse features. Sort by response, then apply
        # a light grid quota so one text-heavy corner cannot dominate the atlas.
        order = sorted(range(len(kp)), key=lambda i: kp[i].response, reverse=True)
        h,w = image.shape[:2]
        small_w = max(1, int(round(w*scale))); small_h = max(1, int(round(h*scale)))
        grid_counts: dict[tuple[int,int], int] = {}
        selected = []
        cell_cap = max(12, self.sample_per_keyframe // 24)
        for i in order:
            x,y = kp[i].pt
            # Avoid persistent menu chrome/buttons. A free-seeded atlas must learn
            # the moving map texture, not fixed screen UI that would falsely match
            # at the same pixels after the user pans.
            if x < small_w * 0.055 or x > small_w * 0.945 or y < small_h * 0.070 or y > small_h * 0.930:
                continue
            cell = (min(5,int(x/max(1,small_w)*6)), min(3,int(y/max(1,small_h)*4)))
            if grid_counts.get(cell,0) >= cell_cap:
                continue
            grid_counts[cell] = grid_counts.get(cell,0)+1
            selected.append(i)
            if len(selected) >= self.sample_per_keyframe:
                break
        if len(selected) < 24:
            return False

        pts_small = np.float32([kp[i].pt for i in selected])
        S_inv = np.array([[1.0/scale,0,0],[0,1.0/scale,0],[0,0,1]],np.float64)
        H_small_to_world = np.asarray(H_full_to_world,dtype=np.float64) @ S_inv
        world = self._transform_points(pts_small, H_small_to_world)
        finite = np.isfinite(world).all(axis=1)
        if int(finite.sum()) < 24:
            return False
        selected_np = np.asarray(selected,dtype=np.int32)[finite]
        world = world[finite].astype(np.float32)
        new_des = des[selected_np].astype(np.float32)

        kid = self.next_id
        self.next_id += 1
        center = self._center_world(image, H_full_to_world)
        self.centers[kid] = center
        ids = np.full((len(new_des),), kid, np.int32)
        self.descriptors = np.vstack([self.descriptors,new_des])
        self.world_points = np.vstack([self.world_points,world])
        self.keyframe_ids = np.concatenate([self.keyframe_ids,ids])
        if source and self.world_source in {"unknown", source}:
            self.world_source = source
        elif source and self.world_source == "unknown":
            self.world_source = source

        # Bound disk/RAM while preserving broad geographic coverage: when over the
        # cap, remove the most redundant keyframe (closest-center pair, older id).
        while len(self.centers) > self.max_keyframes:
            ids_list = sorted(self.centers)
            drop = ids_list[0]
            best = float("inf")
            for i,a in enumerate(ids_list):
                for b in ids_list[i+1:]:
                    ca,cb=self.centers[a],self.centers[b]
                    d=math.hypot(ca[0]-cb[0],ca[1]-cb[1])
                    if d < best:
                        best=d; drop=min(a,b)
            keep = self.keyframe_ids != drop
            self.descriptors = self.descriptors[keep]
            self.world_points = self.world_points[keep]
            self.keyframe_ids = self.keyframe_ids[keep]
            self.centers.pop(drop,None)
        self.updated_at = time.time()
        self.save()
        return True

    def seed_free(self, image: np.ndarray) -> Registration | None:
        """Start a new atlas coordinate space from the currently visible map."""
        H = np.eye(3,dtype=np.float64)
        if not self.add_keyframe(image,H,source="free",force=True):
            return None
        h,w=image.shape[:2]
        poly=np.float32([[0,0],[w-1,0],[w-1,h-1],[0,h-1]])
        return Registration(H,H.copy(),999,999,poly)

    def localize(self, image: np.ndarray, min_matches: int = 28) -> Registration | None:
        if not self.ready or image is None or image.size == 0:
            return None
        _gray, scale, kp, des = self._features(image)
        if des is None or len(kp) < min_matches:
            return None
        index_params = dict(algorithm=1, trees=5)
        search_params = dict(checks=64)
        matcher = cv2.FlannBasedMatcher(index_params,search_params)
        try:
            raw = matcher.knnMatch(des,self.descriptors,k=2)
        except cv2.error:
            return None
        good=[]
        used_train=set()
        for pair in raw:
            if len(pair)!=2:
                continue
            m,n=pair
            if m.distance < 0.68*n.distance and m.trainIdx not in used_train:
                good.append(m); used_train.add(m.trainIdx)
        if len(good) < min_matches:
            return None
        src=np.float32([kp[m.queryIdx].pt for m in good]).reshape(-1,1,2)
        dst=np.float32([self.world_points[m.trainIdx] for m in good]).reshape(-1,1,2)
        H_small,mask=cv2.findHomography(src,dst,cv2.RANSAC,6.0)
        if H_small is None or mask is None:
            return None
        inliers=int(mask.ravel().sum())
        if inliers < max(14,min_matches//2):
            return None
        # Reject geometrically implausible homographies that can arise from repeated
        # map textures/text. We only need positive, finite local scale.
        A=H_small[:2,:2]
        det=float(np.linalg.det(A))
        if not math.isfinite(det) or abs(det) < 0.02 or abs(det) > 80:
            return None
        S=np.array([[scale,0,0],[0,scale,0],[0,0,1]],np.float64)
        H=H_small@S
        try:
            inv=np.linalg.inv(H)
        except np.linalg.LinAlgError:
            return None
        h,w=image.shape[:2]
        corners=np.float32([[0,0],[w-1,0],[w-1,h-1],[0,h-1]]).reshape(-1,1,2)
        poly=cv2.perspectiveTransform(corners,H).reshape(-1,2)
        return Registration(H,inv,inliers,len(good),poly)

    def save(self) -> None:
        self.path.parent.mkdir(parents=True,exist_ok=True)
        tmp=self.path.with_suffix(".tmp")
        with tmp.open("wb") as f:
            np.savez_compressed(
                f,
                version=np.array([self.FORMAT_VERSION],np.int32),
                descriptors=self.descriptors,
                world_points=self.world_points,
                keyframe_ids=self.keyframe_ids,
            )
        os.replace(tmp,self.path)
        meta={
            "version":self.FORMAT_VERSION,
            "world_source":self.world_source,
            "next_id":self.next_id,
            "created_at":self.created_at,
            "updated_at":self.updated_at,
            "centers":{str(k):[v[0],v[1]] for k,v in self.centers.items()},
        }
        self.meta_path.write_text(json.dumps(meta,indent=2,sort_keys=True),encoding="utf-8")

    def load(self) -> None:
        if not self.path.exists() or not self.meta_path.exists():
            return
        try:
            with np.load(self.path,allow_pickle=False) as z:
                version=int(z["version"][0])
                if version != self.FORMAT_VERSION:
                    return
                des=z["descriptors"].astype(np.float32)
                pts=z["world_points"].astype(np.float32)
                ids=z["keyframe_ids"].astype(np.int32)
            if des.ndim != 2 or des.shape[1] != 128 or len(des)!=len(pts) or len(des)!=len(ids):
                return
            meta=json.loads(self.meta_path.read_text(encoding="utf-8"))
            self.descriptors=des; self.world_points=pts; self.keyframe_ids=ids
            self.centers={int(k):(float(v[0]),float(v[1])) for k,v in meta.get("centers",{}).items()}
            self.next_id=max(int(meta.get("next_id",1)),max(self.centers,default=0)+1)
            self.world_source=str(meta.get("world_source","unknown"))
            self.created_at=float(meta.get("created_at",time.time()))
            self.updated_at=float(meta.get("updated_at",self.created_at))
        except Exception:
            # Corruption never blocks the overlay; caller can learn a fresh atlas.
            self.descriptors=np.empty((0,128),np.float32)
            self.world_points=np.empty((0,2),np.float32)
            self.keyframe_ids=np.empty((0,),np.int32)
            self.centers={}; self.next_id=1; self.world_source="unknown"

    def clear(self) -> None:
        self.descriptors=np.empty((0,128),np.float32)
        self.world_points=np.empty((0,2),np.float32)
        self.keyframe_ids=np.empty((0,),np.int32)
        self.centers={}; self.next_id=1; self.world_source="unknown"
        self.path.unlink(missing_ok=True); self.meta_path.unlink(missing_ok=True)
