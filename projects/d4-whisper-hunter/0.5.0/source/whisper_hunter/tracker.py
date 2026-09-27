from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import math
import time
from pathlib import Path
from typing import Iterable

from .config import Config, app_dir
from .homography import Registration, MapRegistrar


@dataclass(slots=True)
class TrackedWhisper:
    id: int
    map_x: float
    map_y: float
    favor: int
    confidence: float
    first_seen: float
    last_seen: float
    seen_count: int = 1
    missed_visible_scans: int = 0
    state: str = "active"  # active | gone | stale

    @property
    def point(self) -> tuple[float, float]:
        return (self.map_x, self.map_y)


class WhisperTracker:
    def __init__(self, cfg: Config, state_path: Path | None = None):
        self.cfg = cfg
        self.state_path = state_path or (app_dir() / "whispers.json")
        self.items: list[TrackedWhisper] = []
        self.next_id = 1
        self.load()

    def load(self) -> None:
        if not self.state_path.exists():
            return
        try:
            raw = json.loads(self.state_path.read_text(encoding="utf-8"))
            self.items = [TrackedWhisper(**x) for x in raw.get("items", [])]
            self.next_id = max([x.id for x in self.items], default=0) + 1
            self.expire()
        except Exception:
            self.items = []
            self.next_id = 1

    def save(self) -> None:
        payload = {"items": [asdict(x) for x in self.items], "saved_at": time.time()}
        self.state_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def _nearest(self, point: tuple[float, float], radius: float) -> TrackedWhisper | None:
        best = None
        best_d = radius
        for item in self.items:
            d = math.hypot(item.map_x - point[0], item.map_y - point[1])
            if d <= best_d:
                best, best_d = item, d
        return best

    def update(
        self,
        observations: Iterable[tuple[tuple[float, float], int, float]],
        registration: Registration,
        now: float | None = None,
    ) -> None:
        now = now or time.time()
        observed_ids: set[int] = set()
        alpha = 0.32
        for point, favor, confidence in observations:
            item = self._nearest(point, self.cfg.marker_merge_radius_px)
            if item is None:
                item = TrackedWhisper(
                    id=self.next_id, map_x=float(point[0]), map_y=float(point[1]),
                    favor=int(favor), confidence=float(confidence), first_seen=now, last_seen=now,
                )
                self.next_id += 1
                self.items.append(item)
            else:
                item.map_x = item.map_x * (1-alpha) + float(point[0]) * alpha
                item.map_y = item.map_y * (1-alpha) + float(point[1]) * alpha
                # Favor promotion/demotion needs repeated evidence; confidence-weighted consensus by recency.
                if favor != item.favor:
                    if confidence >= item.confidence + 0.08 or item.seen_count < 3:
                        item.favor = int(favor)
                item.confidence = min(0.99, item.confidence * 0.70 + float(confidence) * 0.30)
                item.last_seen = now
                item.seen_count += 1
                item.missed_visible_scans = 0
                item.state = "active"
            observed_ids.add(item.id)

        # If a tracked point is inside the current registered viewport and repeatedly
        # vanishes, mark it gone. This lets completed/rotated Whispers disappear naturally.
        for item in self.items:
            if item.id in observed_ids or item.state == "stale":
                continue
            if MapRegistrar.point_in_viewport(item.point, registration):
                item.missed_visible_scans += 1
                if item.missed_visible_scans >= self.cfg.disappear_after_scans:
                    item.state = "gone"
        self.expire(now)
        self.save()

    def expire(self, now: float | None = None) -> None:
        now = now or time.time()
        stale_s = max(5, self.cfg.stale_after_minutes) * 60
        for item in self.items:
            if now - item.last_seen > stale_s:
                item.state = "stale"
        # Keep a bounded history for useful debugging without infinite growth.
        hard_cut = now - max(stale_s * 4, 24 * 3600)
        self.items = [x for x in self.items if x.last_seen >= hard_cut]

    def active(self) -> list[TrackedWhisper]:
        return [x for x in self.items if x.state == "active"]

    def visible_items(self) -> list[TrackedWhisper]:
        if self.cfg.show_history:
            return list(self.items)
        return self.active()

    def mark_gone(self, item_id: int) -> bool:
        for item in self.items:
            if item.id == item_id and item.state == "active":
                item.state = "gone"
                item.missed_visible_scans = self.cfg.disappear_after_scans
                self.save()
                return True
        return False

    def clear(self) -> None:
        self.items.clear()
        self.next_id = 1
        self.save()
