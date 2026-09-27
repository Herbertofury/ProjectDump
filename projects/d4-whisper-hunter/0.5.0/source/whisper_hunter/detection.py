from __future__ import annotations

from dataclasses import dataclass
import math
import cv2
import numpy as np


@dataclass(slots=True)
class WhisperCandidate:
    center: tuple[float, float]
    favor: int
    confidence: float
    bbox: tuple[int, int, int, int]
    area: float
    saturation: float
    value: float
    redness: float
    shape_score: float = 1.0
    holes: int = 0
    edge_density: float = 0.0


@dataclass(slots=True)
class PlayerCandidate:
    center: tuple[float, float]
    confidence: float


def _cluster_favor(raw: list[dict]) -> None:
    """Refine favor classes from the current screen's marker-color distribution.

    Darker/more saturated Whisper markers are higher-value. If a screen contains all
    three families, 1-D k-means makes the classification insensitive to HDR/gamma.
    Heuristics remain the fallback for one/two-family screens.
    """
    if len(raw) < 3:
        return
    scores = np.array([
        (r["sat"] / 255.0) * 0.58 + (1.0 - r["val"] / 255.0) * 0.30 + (r["redness"] / 255.0) * 0.12
        for r in raw
    ], dtype=np.float32)
    unique_spread = float(scores.max() - scores.min())
    if unique_spread < 0.12:
        return
    k = min(3, len(raw))
    data = scores.reshape(-1, 1)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, 0.002)
    _compactness, labels, centers = cv2.kmeans(data, k, None, criteria, 8, cv2.KMEANS_PP_CENTERS)
    order = np.argsort(centers[:, 0])
    ordered_centers = np.array([float(centers[i, 0]) for i in order], dtype=np.float32)
    # Do not manufacture 1/3/5 classes from lighting variation inside a single
    # marker family. Only trust clustering when adjacent color families are truly
    # separated; otherwise keep the absolute per-marker classifier above.
    gaps = np.diff(ordered_centers)
    min_gap = 0.065 if k == 3 else 0.075
    if len(gaps) and float(gaps.min()) < min_gap:
        return
    rank_to_favor = {}
    if k == 3:
        vals = [1, 3, 5]
    elif k == 2:
        # Anchor using absolute score: low pair tends to 1/3, high pair tends to 3/5.
        mid = float(centers.mean())
        vals = [1, 3] if mid < 0.58 else [3, 5]
    else:
        return
    for rank, cluster_idx in enumerate(order):
        rank_to_favor[int(cluster_idx)] = vals[rank]
    for i, r in enumerate(raw):
        r["favor"] = rank_to_favor[int(labels[i, 0])]
        r["clustered"] = True


def detect_whispers(image: np.ndarray) -> list[WhisperCandidate]:
    """Detect light-pink/rose/deep-red Whisper icons from a D4 map screenshot.

    This intentionally ignores giant red Helltide/Whisper region fills and UI panels
    by operating on compact high-redness components only.
    """
    if image is None or image.size == 0:
        return []
    h, w = image.shape[:2]
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    b, g, r = cv2.split(image)
    # Red/pink pixels: allow pale pink but require red dominance and enough chroma.
    redness = r.astype(np.int16) - ((g.astype(np.int16) + b.astype(np.int16)) // 2)
    hue = hsv[:, :, 0]
    sat = hsv[:, :, 1]
    val = hsv[:, :, 2]
    hue_red = (hue <= 14) | (hue >= 158)
    mask = hue_red & (r >= 88) & (redness >= 18) & (sat >= 38) & (val >= 55)

    # Exclude map-menu chrome where red text/selection accents live.
    mask[: max(4, int(h * 0.045)), :] = False
    mask[max(0, int(h * 0.94)) :, :] = False

    u8 = (mask.astype(np.uint8) * 255)
    # Close fragmented icon borders; modest dilation joins star/ring pieces.
    u8 = cv2.morphologyEx(u8, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8), iterations=1)
    u8 = cv2.dilate(u8, np.ones((3, 3), np.uint8), iterations=1)

    num, labels, stats, centroids = cv2.connectedComponentsWithStats(u8, 8)
    raw: list[dict] = []
    scale = max(0.65, min(2.0, math.sqrt((w * h) / (1920.0 * 1080.0))))
    min_area = int(12 * scale * scale)
    max_area = int(2400 * scale * scale)
    min_dim = max(3, int(4 * scale))
    max_dim = int(78 * scale)

    for idx in range(1, num):
        x, y, ww, hh, area = [int(v) for v in stats[idx]]
        if area < min_area or area > max_area:
            continue
        if ww < min_dim or hh < min_dim or ww > max_dim or hh > max_dim:
            continue
        aspect = ww / max(1.0, float(hh))
        if not 0.35 <= aspect <= 2.8:
            continue
        # Keep marker-sized components, reject thin text strokes and broad/flat
        # map symbols (Tree icon wings, Helltide blobs, UI badges). Real Whisper
        # objectives use a compact framed glyph with internal negative space or
        # enough border/detail to produce a high binary-edge density.
        fill = area / max(1.0, ww * hh)
        if fill < 0.08 or fill > 0.84:
            continue
        if not 0.48 <= aspect <= 2.05:
            continue
        component = labels[y:y+hh, x:x+ww] == idx
        if int(component.sum()) == 0:
            continue
        component_u8 = component.astype(np.uint8) * 255
        contours, hierarchy = cv2.findContours(component_u8, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        holes = 0
        if hierarchy is not None and len(hierarchy):
            holes = sum(1 for row in hierarchy[0] if int(row[3]) >= 0)
        edge = cv2.morphologyEx(component_u8, cv2.MORPH_GRADIENT, np.ones((3, 3), np.uint8))
        edge_density = float(np.count_nonzero(edge)) / max(1.0, float(ww * hh))
        # A flat filled circle/diamond is a common red-map decoy but is not a
        # Whisper frame. Preserve ornate/outlined glyphs even when HDR changes
        # their fill ratio.
        if holes == 0 and edge_density < 0.255:
            continue
        sat_med = float(np.median(sat[y:y+hh, x:x+ww][component]))
        val_med = float(np.median(val[y:y+hh, x:x+ww][component]))
        red_med = float(np.median(redness[y:y+hh, x:x+ww][component]))
        cx, cy = [float(v) for v in centroids[idx]]

        # Absolute classification fallback. Deep red is most saturated/dark.
        score = (sat_med / 255.0) * 0.58 + (1.0 - val_med / 255.0) * 0.30 + (red_med / 255.0) * 0.12
        if score >= 0.64:
            favor = 5
        elif score >= 0.47:
            favor = 3
        else:
            favor = 1
        size_score = min(1.0, area / max(1.0, 80.0 * scale * scale))
        aspect_score = math.exp(-1.6 * abs(math.log(max(1e-6, aspect))))
        detail_score = min(1.0, edge_density / 0.34)
        hole_score = min(1.0, holes / 2.0)
        fill_score = max(0.0, 1.0 - abs(fill - 0.56) / 0.36)
        shape_score = max(0.0, min(1.0, 0.28 * aspect_score + 0.30 * detail_score + 0.24 * hole_score + 0.18 * fill_score))
        base_confidence = 0.43 + 0.28 * size_score + 0.22 * min(1.0, red_med / 90.0)
        confidence = max(0.25, min(0.98, base_confidence * (0.70 + 0.30 * shape_score)))
        raw.append({
            "center": (cx, cy), "favor": favor, "confidence": confidence,
            "bbox": (x, y, ww, hh), "area": float(area), "sat": sat_med,
            "val": val_med, "redness": red_med, "shape_score": shape_score,
            "holes": holes, "edge_density": edge_density, "clustered": False,
        })

    _cluster_favor(raw)
    return [
        WhisperCandidate(
            center=r["center"], favor=int(r["favor"]), confidence=float(r["confidence"]),
            bbox=r["bbox"], area=r["area"], saturation=r["sat"], value=r["val"], redness=r["redness"],
            shape_score=r["shape_score"], holes=r["holes"], edge_density=r["edge_density"]
        )
        for r in raw
    ]


def detect_player_marker(image: np.ndarray) -> PlayerCandidate | None:
    """Best-effort blue player-arrow/diamond detection; returns None if ambiguous."""
    if image is None or image.size == 0:
        return None
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Player marker is generally blue/cyan. Waypoints are cyan too, so shape/ranking is conservative.
    mask = cv2.inRange(hsv, np.array([88, 80, 90], np.uint8), np.array([118, 255, 255], np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8), iterations=1)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    candidates = []
    h, w = image.shape[:2]
    scale = max(0.65, min(2.0, math.sqrt((w * h) / (1920.0 * 1080.0))))
    for c in contours:
        area = cv2.contourArea(c)
        if not (18 * scale * scale <= area <= 900 * scale * scale):
            continue
        x, y, ww, hh = cv2.boundingRect(c)
        if not (0.55 <= ww / max(1.0, hh) <= 1.8):
            continue
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.08 * peri, True)
        # Diamond/arrow-ish shapes score above circular waypoint rings.
        poly_score = 1.0 if 3 <= len(approx) <= 6 else 0.4
        center_bias = 1.0 - min(1.0, math.hypot((x+ww/2)-w/2, (y+hh/2)-h/2) / math.hypot(w/2, h/2))
        score = 0.65 * poly_score + 0.35 * center_bias
        candidates.append((score, (x + ww/2.0, y + hh/2.0)))
    if not candidates:
        return None
    candidates.sort(reverse=True, key=lambda z: z[0])
    if len(candidates) > 1 and candidates[0][0] - candidates[1][0] < 0.08:
        return None
    return PlayerCandidate(candidates[0][1], min(0.95, 0.45 + candidates[0][0] * 0.5))
