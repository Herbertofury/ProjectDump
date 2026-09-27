from __future__ import annotations

from dataclasses import dataclass
import cv2
import numpy as np


@dataclass(slots=True)
class Registration:
    query_to_map: np.ndarray
    map_to_query: np.ndarray
    inliers: int
    good_matches: int
    viewport_map_polygon: np.ndarray


class MapRegistrar:
    """Feature-register an in-game world-map screenshot to the canonical Sanctuary map."""

    def __init__(self, map_image: np.ndarray, max_features: int = 5200, max_query_width: int = 1600, world_scale: float = 1.0):
        if map_image is None or map_image.size == 0:
            raise ValueError("map_image is empty")
        self.map_image = map_image
        self.max_query_width = max_query_width
        self.world_scale = float(world_scale)
        if not np.isfinite(self.world_scale) or self.world_scale <= 0:
            raise ValueError("world_scale must be finite and > 0")
        self.gray_map = cv2.cvtColor(map_image, cv2.COLOR_BGR2GRAY)
        self.sift = cv2.SIFT_create(nfeatures=max_features)
        self.kp_map, self.des_map = self.sift.detectAndCompute(self.gray_map, None)
        if self.des_map is None or len(self.kp_map) < 20:
            raise RuntimeError("Canonical map has too few features for registration")
        index_params = dict(algorithm=1, trees=5)  # FLANN KD-tree
        search_params = dict(checks=64)
        self.flann = cv2.FlannBasedMatcher(index_params, search_params)

    def register(self, screenshot: np.ndarray, min_matches: int = 28) -> Registration | None:
        if screenshot is None or screenshot.size == 0:
            return None
        gray_full = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        scale = 1.0
        if self.max_query_width and gray_full.shape[1] > self.max_query_width:
            scale = self.max_query_width / float(gray_full.shape[1])
            gray = cv2.resize(gray_full, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        else:
            gray = gray_full
        kp_q, des_q = self.sift.detectAndCompute(gray, None)
        if des_q is None or len(kp_q) < min_matches:
            return None
        try:
            raw = self.flann.knnMatch(des_q, self.des_map, k=2)
        except cv2.error:
            return None
        good = []
        for pair in raw:
            if len(pair) != 2:
                continue
            m, n = pair
            if m.distance < 0.70 * n.distance:
                good.append(m)
        if len(good) < min_matches:
            return None

        src = np.float32([kp_q[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst = np.float32([self.kp_map[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        H_small, mask = cv2.findHomography(src, dst, cv2.RANSAC, 4.0)
        if H_small is None or mask is None:
            return None
        # src points were extracted from the scaled query image. Convert the
        # homography so callers can use original full-resolution screenshot pixels.
        if scale != 1.0:
            S = np.array([[scale, 0.0, 0.0], [0.0, scale, 0.0], [0.0, 0.0, 1.0]], dtype=np.float64)
            H = H_small @ S
        else:
            H = H_small
        # Some proven donor paths (including the original mxtsdev overlay) run the
        # static map at 0.5x for robust/faster SIFT. Normalize those coordinates
        # back into the canonical full-resolution map space so old tracks, atlas
        # keyframes and fallback registrars all share one world-coordinate lineage.
        if self.world_scale != 1.0:
            W = np.array(
                [[self.world_scale, 0.0, 0.0], [0.0, self.world_scale, 0.0], [0.0, 0.0, 1.0]],
                dtype=np.float64,
            )
            H = W @ H
        inliers = int(mask.ravel().sum())
        if inliers < max(12, min_matches // 2):
            return None
        try:
            inv = np.linalg.inv(H)
        except np.linalg.LinAlgError:
            return None

        h, w = screenshot.shape[:2]
        corners = np.float32([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]]).reshape(-1, 1, 2)
        poly = cv2.perspectiveTransform(corners, H).reshape(-1, 2)
        return Registration(H, inv, inliers, len(good), poly)

    @staticmethod
    def query_points_to_map(points: list[tuple[float, float]], reg: Registration) -> np.ndarray:
        if not points:
            return np.empty((0, 2), dtype=np.float32)
        arr = np.float32(points).reshape(-1, 1, 2)
        return cv2.perspectiveTransform(arr, reg.query_to_map).reshape(-1, 2)

    @staticmethod
    def map_points_to_query(points: list[tuple[float, float]], reg: Registration) -> np.ndarray:
        if not points:
            return np.empty((0, 2), dtype=np.float32)
        arr = np.float32(points).reshape(-1, 1, 2)
        return cv2.perspectiveTransform(arr, reg.map_to_query).reshape(-1, 2)

    @staticmethod
    def point_in_viewport(point: tuple[float, float], reg: Registration) -> bool:
        contour = reg.viewport_map_polygon.astype(np.float32).reshape(-1, 1, 2)
        return cv2.pointPolygonTest(contour, (float(point[0]), float(point[1])), False) >= 0
