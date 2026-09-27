from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable

import cv2
import numpy as np

from .config import Config


# Geometry vocabulary intentionally mirrors the useful public QQT Evade API model:
# circle/explosion, rectangle/slash/projectile, cone and danger levels. Detection
# itself remains passive computer vision; it never reads Diablo IV process memory.
DANGER_LOW = 1
DANGER_MEDIUM = 2
DANGER_HIGH = 3


@dataclass(slots=True)
class DangerEvent:
    id: int
    kind: str
    level: int
    confidence: float
    center: tuple[float, float]
    bbox: tuple[int, int, int, int]
    polygon: tuple[tuple[float, float], ...]
    distance_to_player: float
    eta_seconds: float | None = None
    velocity: tuple[float, float] = (0.0, 0.0)
    age_frames: int = 1
    locked: bool = False

    @property
    def urgent(self) -> bool:
        return self.level >= DANGER_HIGH or (self.eta_seconds is not None and self.eta_seconds <= 0.85)

    @property
    def label(self) -> str:
        if self.kind == "executioner":
            return "EXECUTIONER SWORD — EVADE" if self.locked or self.urgent else "EXECUTIONER SWORD — READY"
        if self.kind == "explosion":
            return "EXPLOSION — MOVE"
        if self.kind == "projectile":
            return "INCOMING — DODGE"
        if self.kind == "slash":
            return "SWORD / SLASH — DODGE"
        if self.kind == "cone":
            return "CONE / SLAM — MOVE"
        return "DANGER — MOVE"


@dataclass(slots=True)
class _Candidate:
    kind: str
    level: int
    confidence: float
    center: np.ndarray
    bbox: tuple[int, int, int, int]
    polygon: np.ndarray
    distance_to_player: float
    radius: float
    major: float
    minor: float
    eta_seconds: float | None = None
    locked: bool = False


@dataclass(slots=True)
class _Track:
    id: int
    kind: str
    center: np.ndarray
    bbox: tuple[int, int, int, int]
    polygon: np.ndarray
    radius: float
    level: int
    confidence: float
    distance_to_player: float
    last_seen: float
    age_frames: int = 1
    velocity: np.ndarray | None = None
    eta_seconds: float | None = None
    locked: bool = False


class DangerAlertGate:
    """Rate-limit audio without suppressing a more urgent escalation."""

    def __init__(self, normal_cooldown: float = 1.35, urgent_cooldown: float = 0.55):
        self.normal_cooldown = max(0.05, float(normal_cooldown))
        self.urgent_cooldown = max(0.05, float(urgent_cooldown))
        self._last: dict[str, tuple[float, bool]] = {}

    def should_alert(self, event: DangerEvent, now: float) -> bool:
        key = event.kind
        urgent = event.urgent
        last = self._last.get(key)
        if last is None:
            self._last[key] = (now, urgent)
            return True
        last_time, last_urgent = last
        cooldown = self.urgent_cooldown if urgent else self.normal_cooldown
        # An escalation from ordinary -> urgent bypasses the ordinary cooldown.
        if urgent and not last_urgent:
            self._last[key] = (now, True)
            return True
        if now - last_time >= cooldown:
            self._last[key] = (now, urgent)
            return True
        return False

    def reset(self) -> None:
        self._last.clear()


def _point_segment_distance(p: np.ndarray, a: np.ndarray, b: np.ndarray) -> float:
    ab = b - a
    denom = float(np.dot(ab, ab))
    if denom <= 1e-6:
        return float(np.linalg.norm(p - a))
    t = float(np.dot(p - a, ab) / denom)
    t = max(0.0, min(1.0, t))
    q = a + t * ab
    return float(np.linalg.norm(p - q))


def _major_axis(rect: tuple, scale_back: float) -> tuple[np.ndarray, np.ndarray, float, float]:
    (cx, cy), (rw, rh), angle = rect
    if rw >= rh:
        major, minor, theta = rw, rh, math.radians(angle)
    else:
        major, minor, theta = rh, rw, math.radians(angle + 90.0)
    d = np.array([math.cos(theta), math.sin(theta)], dtype=np.float32) * (major / 2.0)
    c = np.array([cx, cy], dtype=np.float32)
    return (c - d) * scale_back, (c + d) * scale_back, major * scale_back, minor * scale_back


class DangerDetector:
    """Low-latency passive CV detector for lethal Diablo IV telegraphs.

    The detector is intentionally screen-only. It uses the same geometry families as
    QQT Evade but infers them from rendered red/orange warning shapes and temporal
    motion rather than internal game object/spell names.
    """

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self._tracks: dict[int, _Track] = {}
        self._next_id = 1
        self._last_shape = (0, 0)

    def clear(self) -> None:
        self._tracks.clear()

    def _danger_mask(self, image: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
        h, w = image.shape[:2]
        max_w = max(480, int(self.cfg.danger_max_cv_width))
        scale = min(1.0, max_w / float(w))
        if scale < 0.999:
            small = cv2.resize(image, (int(round(w * scale)), int(round(h * scale))), interpolation=cv2.INTER_AREA)
        else:
            small = image
        hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)

        # D4 lethal telegraphs are commonly red -> orange. Keep this intentionally
        # conservative; white/yellow player effects are much more common noise.
        m_red1 = cv2.inRange(hsv, (0, 105, 105), (14, 255, 255))
        m_orange = cv2.inRange(hsv, (15, 135, 135), (32, 255, 255))
        m_red2 = cv2.inRange(hsv, (168, 95, 100), (179, 255, 255))
        mask = cv2.bitwise_or(cv2.bitwise_or(m_red1, m_orange), m_red2)

        sh, sw = mask.shape[:2]
        # Hard HUD masks: warning geometry under the character remains visible, but
        # health/resource globes and bottom skill-bar coloration never become alerts.
        cv2.rectangle(mask, (0, int(sh * 0.90)), (sw, sh), 0, -1)
        cv2.rectangle(mask, (0, int(sh * 0.72)), (int(sw * 0.16), sh), 0, -1)
        cv2.rectangle(mask, (int(sw * 0.84), int(sh * 0.72)), (sw, sh), 0, -1)
        cv2.rectangle(mask, (0, 0), (sw, int(sh * 0.035)), 0, -1)

        k = max(3, int(round(5 * scale)))
        if k % 2 == 0:
            k += 1
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
        mask = cv2.dilate(mask, kernel, iterations=1)
        return mask, hsv, 1.0 / scale

    def _executioner_candidates(self, image: np.ndarray, hsv_full: np.ndarray, danger_mask_full: np.ndarray, back: float) -> list[_Candidate]:
        """Detect the Executioner elite-affix sword in the player-overhead corridor.

        The full-frame resize/HSV conversion is shared with the ordinary DangerSense
        detector. Executioner Guard only thresholds a small crop of that prepared HSV
        image, avoiding a second expensive frame conversion on every capture.
        """
        if not self.cfg.executioner_enabled:
            return []

        h, w = image.shape[:2]
        scale = 1.0 / max(1e-6, float(back))
        player = np.array([w * 0.5, h * self.cfg.danger_player_screen_y], dtype=np.float32)
        player_r = float(self.cfg.danger_player_radius_px) * (w / 1920.0)
        half_w = float(self.cfg.executioner_center_half_width_px) * (w / 1920.0)
        overhead_h = float(self.cfg.executioner_overhead_height_px) * (h / 1080.0)

        sh, sw = hsv_full.shape[:2]
        sx1 = max(0, int((player[0] - half_w) * scale))
        sx2 = min(sw, int((player[0] + half_w) * scale) + 1)
        sy1 = max(0, int((player[1] - overhead_h) * scale))
        sy2 = min(sh, int((player[1] + player_r * 1.20) * scale) + 1)
        hsv = hsv_full[sy1:sy2, sx1:sx2]
        if hsv.size == 0:
            return []

        offset = np.array([sx1 * back, sy1 * back], dtype=np.float32)
        player_local_s = player * scale - np.array([sx1, sy1], dtype=np.float32)

        # Steel/white and warm/gold parts of the blade. Geometry—not raw color—is
        # the strong discriminator: long, narrow, near-vertical, player-overhead.
        steel = cv2.inRange(hsv, (0, 0, 118), (179, 118, 255))
        warm = cv2.inRange(hsv, (8, 42, 95), (48, 255, 255))
        blade_mask = cv2.bitwise_or(steel, warm)
        vk = max(5, int(round(11 * scale)))
        blade_mask = cv2.morphologyEx(
            blade_mask,
            cv2.MORPH_CLOSE,
            cv2.getStructuringElement(cv2.MORPH_RECT, (3, vk)),
            iterations=2,
        )

        # Reuse the already-computed full-frame red/orange DangerSense mask for the
        # lock cue instead of thresholding HSV three more times. Broad AoEs remain
        # owned by the ordinary explosion detector.
        lock_mask = danger_mask_full[sy1:sy2, sx1:sx2].copy()
        lock_roi = np.zeros_like(lock_mask)
        lr = float(self.cfg.executioner_lock_radius_px) * (w / 1920.0)
        cv2.circle(
            lock_roi,
            (int(player_local_s[0]), int(player_local_s[1])),
            max(8, int(lr * scale)),
            255,
            -1,
        )
        lock_mask = cv2.bitwise_and(lock_mask, lock_roi)
        lock_mask = cv2.morphologyEx(
            lock_mask,
            cv2.MORPH_CLOSE,
            cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)),
            iterations=1,
        )
        lock_found = False
        lock_center = player.copy()
        lock_radius = 0.0
        lock_contours, _ = cv2.findContours(lock_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for lc in lock_contours:
            if len(lc) < 5:
                continue
            area_s = abs(float(cv2.contourArea(lc)))
            if area_s < 24.0:
                continue
            (cx_s, cy_s), r_s = cv2.minEnclosingCircle(lc.astype(np.float32))
            radius = float(r_s) * back
            if radius < max(10.0, player_r * 0.14) or radius > player_r * 1.05:
                continue
            center = np.array([cx_s * back, cy_s * back], np.float32) + offset
            if float(np.linalg.norm(center - player)) > player_r * 0.58:
                continue
            perimeter = max(1.0, float(cv2.arcLength(lc, True)))
            circularity = min(1.0, 4.0 * math.pi * area_s / (perimeter * perimeter))
            bx, by, bw, bh = cv2.boundingRect(lc)
            aspect = max(bw, bh) / max(1.0, min(bw, bh))
            if circularity < 0.16 or aspect > 1.9:
                continue
            lock_found = True
            lock_center = center
            lock_radius = max(lock_radius, radius)

        contours, _ = cv2.findContours(blade_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        out: list[_Candidate] = []
        min_aspect = float(self.cfg.executioner_min_blade_aspect)
        for cs in contours:
            if len(cs) < 3:
                continue
            contour = cs.astype(np.float32) * back + offset
            area = abs(float(cv2.contourArea(contour)))
            if area < max(75.0, w * h * 0.000025) or area > w * h * 0.025:
                continue
            rect = cv2.minAreaRect(contour.astype(np.float32))
            a, b, major, minor = _major_axis(rect, 1.0)
            aspect = major / max(1.0, minor)
            if aspect < min_aspect or major < max(42.0, h * 0.038) or major > h * 0.42:
                continue
            axis = b - a
            verticality = abs(float(axis[1])) / max(1.0, float(np.linalg.norm(axis)))
            if verticality < 0.70:
                continue
            center = (a + b) * 0.5
            if abs(float(center[0] - player[0])) > half_w:
                continue

            tip = a if abs(float(a[1] - player[1])) <= abs(float(b[1] - player[1])) else b
            vertical_gap = max(0.0, float(player[1] - tip[1]))
            x_gap = abs(float(tip[0] - player[0]))
            threat_dist = math.hypot(x_gap * 0.70, vertical_gap)
            alignment = max(0.0, 1.0 - abs(float(center[0] - player[0])) / max(1.0, half_w))
            proximity = max(0.0, 1.0 - threat_dist / max(1.0, overhead_h))
            shape = min(1.0, 0.42 + (aspect - min_aspect) * 0.08 + verticality * 0.30)
            confidence = min(0.99, 0.43 + shape * 0.28 + alignment * 0.16 + proximity * 0.13)

            locked = lock_found and float(np.linalg.norm(lock_center - player)) <= player_r * 0.58
            eta: float | None = None
            level = DANGER_MEDIUM
            if threat_dist <= player_r * 0.70:
                level = DANGER_HIGH
                confidence = min(0.99, confidence + 0.08)
            if locked:
                level = DANGER_HIGH
                confidence = min(0.995, confidence + 0.20)
                eta = float(self.cfg.executioner_lock_eta_s)

            if confidence < min(float(self.cfg.danger_min_confidence), 0.62):
                continue
            x, y, bw, bh = cv2.boundingRect(contour.astype(np.int32))
            poly = cv2.boxPoints(rect).astype(np.float32)
            out.append(
                _Candidate(
                    kind="executioner",
                    level=level,
                    confidence=confidence,
                    center=center.astype(np.float32),
                    bbox=(x, y, bw, bh),
                    polygon=poly,
                    distance_to_player=threat_dist,
                    radius=max(lock_radius, minor * 0.5),
                    major=major,
                    minor=minor,
                    eta_seconds=eta,
                    locked=locked,
                )
            )

        out.sort(key=lambda c: (c.locked, c.level, c.confidence, -c.distance_to_player), reverse=True)
        return out[:2]

    def _candidates(self, image: np.ndarray) -> list[_Candidate]:
        h, w = image.shape[:2]
        mask, hsv_full, back = self._danger_mask(image)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        player = np.array([w * 0.5, h * self.cfg.danger_player_screen_y], dtype=np.float32)
        player_r = float(self.cfg.danger_player_radius_px) * (w / 1920.0)
        frame_area = float(w * h)
        out: list[_Candidate] = []

        for contour_small in contours:
            if len(contour_small) < 3:
                continue
            contour = contour_small.astype(np.float32) * back
            area = abs(float(cv2.contourArea(contour)))
            if area < max(70.0, frame_area * 0.000045) or area > frame_area * 0.34:
                continue
            x, y, bw, bh = cv2.boundingRect(contour.astype(np.int32))
            if bw < 7 or bh < 7:
                continue
            # Ignore narrow screen-edge UI streaks unless they geometrically point at
            # the player. This preserves incoming diagonal projectile warnings.
            center = np.array([x + bw / 2.0, y + bh / 2.0], dtype=np.float32)
            rect = cv2.minAreaRect(contour.astype(np.float32))
            a, b, major, minor = _major_axis(rect, 1.0)
            aspect = major / max(1.0, minor)
            perimeter = max(1.0, float(cv2.arcLength(contour.astype(np.float32), True)))
            circularity = min(1.0, 4.0 * math.pi * area / (perimeter * perimeter))
            hull = cv2.convexHull(contour.astype(np.float32))
            hull_area = max(1.0, abs(float(cv2.contourArea(hull))))
            solidity = min(1.0, area / hull_area)
            approx = cv2.approxPolyDP(contour.astype(np.float32), 0.045 * perimeter, True)
            vertices = len(approx)
            dist_center = float(np.linalg.norm(center - player))
            line_dist = _point_segment_distance(player, a, b)
            radius = max(major, minor) * 0.5

            kind = "explosion"
            geom_dist = max(0.0, dist_center - radius)
            if aspect >= 2.45 and major >= 42:
                kind = "slash"
                geom_dist = max(0.0, line_dist - minor * 0.55)
            elif 3 <= vertices <= 5 and solidity >= 0.62 and 1.15 <= aspect <= 2.8 and circularity < 0.58:
                kind = "cone"
                inside = cv2.pointPolygonTest(contour.astype(np.float32), (float(player[0]), float(player[1])), True)
                geom_dist = 0.0 if inside >= 0 else abs(float(inside))

            # Only alert geometry that can plausibly threaten the character soon.
            near = geom_dist <= player_r * 2.4
            central = (w * 0.14) <= center[0] <= (w * 0.86) and (h * 0.08) <= center[1] <= (h * 0.84)
            if not near and not central:
                continue
            if kind == "explosion" and circularity < 0.12 and solidity < 0.42:
                continue

            level = DANGER_LOW
            if geom_dist <= player_r * 0.55:
                level = DANGER_HIGH
            elif geom_dist <= player_r * 1.45:
                level = DANGER_MEDIUM

            # Shape confidence intentionally rewards telegraph geometry and proximity,
            # not just red pixels, which suppresses spell/UI false positives.
            shape_score = 0.0
            if kind == "slash":
                shape_score = min(1.0, (aspect - 1.8) / 3.0 + 0.30)
            elif kind == "cone":
                shape_score = min(1.0, 0.45 + solidity * 0.35 + (0.15 if vertices <= 4 else 0.0))
            else:
                shape_score = min(1.0, 0.25 + circularity * 0.55 + solidity * 0.25)
            proximity_score = max(0.0, 1.0 - geom_dist / max(1.0, player_r * 3.0))
            confidence = min(0.99, 0.38 + shape_score * 0.38 + proximity_score * 0.24)
            if confidence < float(self.cfg.danger_min_confidence):
                continue

            poly = cv2.boxPoints(rect).astype(np.float32) if kind == "slash" else approx.reshape(-1, 2).astype(np.float32)
            out.append(
                _Candidate(
                    kind=kind,
                    level=level,
                    confidence=confidence,
                    center=center,
                    bbox=(x, y, bw, bh),
                    polygon=poly,
                    distance_to_player=geom_dist,
                    radius=radius,
                    major=major,
                    minor=minor,
                )
            )

        # Dedicated Executioner detection runs outside the red-only mask. Remove
        # overlapping generic slash/explosion contours so one sword produces one
        # authoritative warning and one possible Smart Evade decision.
        executioners = self._executioner_candidates(image, hsv_full, mask, back)
        if executioners:
            filtered: list[_Candidate] = []
            for c in out:
                duplicate = False
                for ex in executioners:
                    if float(np.linalg.norm(c.center - ex.center)) <= max(70.0, ex.major * 0.72):
                        if c.kind in {"slash", "projectile"} or (ex.locked and c.kind == "explosion"):
                            duplicate = True
                            break
                if not duplicate:
                    filtered.append(c)
            out = executioners + filtered

        # Highest threat first and cap pathological particle storms without hiding the
        # most important threats. Executioner lock wins ties.
        out.sort(key=lambda c: (c.locked, c.level, c.confidence, -c.distance_to_player), reverse=True)
        return out[: int(self.cfg.danger_max_events)]

    def _match_track(self, cand: _Candidate, used: set[int]) -> _Track | None:
        best: _Track | None = None
        best_d = float("inf")
        max_d = max(48.0, cand.major * 0.8)
        for tr in self._tracks.values():
            if tr.id in used:
                continue
            if cand.kind in {"slash", "projectile"}:
                if tr.kind not in {"slash", "projectile"}:
                    continue
            elif tr.kind != cand.kind:
                continue
            d = float(np.linalg.norm(cand.center - tr.center))
            if d < max_d and d < best_d:
                best = tr
                best_d = d
        return best

    def update(self, image: np.ndarray, now: float, *, suppress: bool = False) -> list[DangerEvent]:
        self._last_shape = image.shape[:2]
        if suppress or not self.cfg.danger_enabled:
            self.clear()
            return []

        player = np.array([image.shape[1] * 0.5, image.shape[0] * self.cfg.danger_player_screen_y], dtype=np.float32)
        candidates = self._candidates(image)
        used: set[int] = set()
        new_tracks: dict[int, _Track] = {}

        for cand in candidates:
            tr = self._match_track(cand, used)
            if tr is None:
                tr = _Track(
                    id=self._next_id,
                    kind=cand.kind,
                    center=cand.center.copy(),
                    bbox=cand.bbox,
                    polygon=cand.polygon.copy(),
                    radius=cand.radius,
                    level=cand.level,
                    confidence=cand.confidence,
                    distance_to_player=cand.distance_to_player,
                    last_seen=now,
                    eta_seconds=cand.eta_seconds,
                    locked=cand.locked,
                )
                self._next_id += 1
            else:
                dt = max(1e-3, now - tr.last_seen)
                velocity = (cand.center - tr.center) / dt
                tr.velocity = velocity if tr.velocity is None else tr.velocity * 0.35 + velocity * 0.65
                tr.age_frames += 1
                tr.center = cand.center.copy()
                tr.bbox = cand.bbox
                tr.polygon = cand.polygon.copy()
                tr.radius = cand.radius
                tr.level = max(cand.level, tr.level - 1)
                tr.confidence = max(cand.confidence, min(0.99, tr.confidence * 0.72 + cand.confidence * 0.38))
                tr.distance_to_player = cand.distance_to_player
                tr.last_seen = now
                tr.locked = cand.locked
                if cand.eta_seconds is not None:
                    tr.eta_seconds = cand.eta_seconds

            # Executioner ETA: lock-circle is authoritative. Before lock, a downward
            # moving overhead blade gets a conservative tip-to-player ETA so the
            # warning can escalate even when the circle is obscured by spell VFX.
            if cand.kind == "executioner":
                tr.kind = "executioner"
                tr.locked = cand.locked
                player_r = float(self.cfg.danger_player_radius_px) * (image.shape[1] / 1920.0)
                if cand.locked:
                    tr.eta_seconds = float(self.cfg.executioner_lock_eta_s)
                    tr.level = DANGER_HIGH
                    tr.confidence = min(0.995, tr.confidence + 0.08)
                elif tr.velocity is not None and float(tr.velocity[1]) > 70.0:
                    tip_y = float(tr.center[1] + cand.major * 0.5)
                    gap = max(0.0, float(player[1] - tip_y))
                    eta = gap / max(1.0, float(tr.velocity[1]))
                    if 0.0 <= eta <= 1.8:
                        tr.eta_seconds = eta
                        tr.level = DANGER_HIGH if eta <= 0.9 else max(tr.level, DANGER_MEDIUM)
                elif cand.distance_to_player <= player_r * 0.50:
                    tr.eta_seconds = min(0.65, float(self.cfg.executioner_lock_eta_s) + 0.14)
                    tr.level = DANGER_HIGH

            # Dynamic elongated shapes become projectiles only when motion predicts a
            # near-future pass through the player. This makes "sword coming" warnings
            # directional rather than alarming on every red line on screen.
            if tr.velocity is not None and cand.kind == "slash":
                speed = float(np.linalg.norm(tr.velocity))
                if speed >= float(self.cfg.danger_projectile_min_speed_px_s):
                    rel = player - tr.center
                    v2 = float(np.dot(tr.velocity, tr.velocity))
                    eta = float(np.dot(rel, tr.velocity) / v2) if v2 > 1e-6 else -1.0
                    if 0.0 < eta <= float(self.cfg.danger_projectile_horizon_s):
                        closest = tr.center + tr.velocity * eta
                        miss = float(np.linalg.norm(closest - player))
                        player_r = float(self.cfg.danger_player_radius_px) * (image.shape[1] / 1920.0)
                        if miss <= player_r * 1.45:
                            tr.kind = "projectile"
                            tr.eta_seconds = eta
                            tr.level = DANGER_HIGH if eta <= 1.0 else max(tr.level, DANGER_MEDIUM)
                            tr.confidence = min(0.99, tr.confidence + 0.10)

            # If an explosion ring already reaches the character, impact is now.
            if tr.kind == "explosion" and tr.distance_to_player <= 1.0:
                tr.eta_seconds = 0.0
                tr.level = DANGER_HIGH

            used.add(tr.id)
            new_tracks[tr.id] = tr

        # Short temporal hold smooths contour flicker but never keeps stale warnings.
        hold = max(0.05, float(self.cfg.danger_track_hold_s))
        for tid, tr in self._tracks.items():
            if tid in new_tracks:
                continue
            if now - tr.last_seen <= hold:
                new_tracks[tid] = tr
        self._tracks = new_tracks

        events: list[DangerEvent] = []
        for tr in self._tracks.values():
            stable = tr.age_frames >= int(self.cfg.danger_confirm_frames)
            immediate = tr.level >= DANGER_HIGH and tr.confidence >= float(self.cfg.danger_immediate_confidence)
            if not stable and not immediate:
                continue
            poly = tuple((float(p[0]), float(p[1])) for p in tr.polygon)
            vel = tr.velocity if tr.velocity is not None else np.zeros(2, np.float32)
            events.append(
                DangerEvent(
                    id=tr.id,
                    kind=tr.kind,
                    level=tr.level,
                    confidence=tr.confidence,
                    center=(float(tr.center[0]), float(tr.center[1])),
                    bbox=tr.bbox,
                    polygon=poly,
                    distance_to_player=tr.distance_to_player,
                    eta_seconds=tr.eta_seconds,
                    velocity=(float(vel[0]), float(vel[1])),
                    age_frames=tr.age_frames,
                    locked=tr.locked,
                )
            )
        events.sort(
            key=lambda e: (
                e.kind == "executioner",
                e.locked,
                e.level,
                e.urgent,
                e.confidence,
                -(e.eta_seconds if e.eta_seconds is not None else 99.0),
            ),
            reverse=True,
        )
        return events[: int(self.cfg.danger_max_events)]
