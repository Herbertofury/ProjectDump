from __future__ import annotations

import ctypes
import os
import queue
import tkinter as tk
from dataclasses import dataclass, field

from .danger import DANGER_HIGH, DangerEvent
from .routing import RoutePlan
from .tracker import TrackedWhisper


@dataclass(slots=True)
class OverlayState:
    screen_points: list[tuple[TrackedWhisper, float, float]]
    route_points: list[tuple[TrackedWhisper, float, float]]
    route: RoutePlan
    current_favors: int
    tracked_total: int
    registered: bool
    matches: int
    inliers: int
    status: str
    scan_age: float
    atlas_keyframes: int = 0
    map_mode: str = ""
    hazards: list[DangerEvent] = field(default_factory=list)
    danger_enabled: bool = True
    danger_sound_enabled: bool = True
    auto_evade_enabled: bool = True
    danger_alert: str = ""


class OverlayWindow:
    TRANSPARENT = "#ff0080"

    def __init__(self, width: int, height: int, state_queue: queue.Queue, opacity: float = 0.93, left: int = 0, top: int = 0):
        self.width = width
        self.height = height
        self.left = int(left)
        self.top = int(top)
        self.state_queue = state_queue
        self.root = tk.Tk()
        self.root.title("D4 Whisper Hunter")
        self.root.geometry(f"{width}x{height}{self.left:+d}{self.top:+d}")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", opacity)
        self.root.configure(bg=self.TRANSPARENT)
        if os.name == "nt":
            try:
                self.root.wm_attributes("-transparentcolor", self.TRANSPARENT)
            except tk.TclError:
                pass
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg=self.TRANSPARENT, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.visible = True
        self.last_state: OverlayState | None = None
        self._make_clickthrough()
        self.root.after(33, self._pump)

    def _make_clickthrough(self) -> None:
        if os.name != "nt":
            return
        self.root.update_idletasks()
        hwnd = int(self.root.winfo_id())
        user32 = ctypes.windll.user32
        GWL_EXSTYLE = -20
        WS_EX_LAYERED = 0x00080000
        WS_EX_TRANSPARENT = 0x00000020
        WS_EX_TOOLWINDOW = 0x00000080
        style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_LAYERED | WS_EX_TRANSPARENT | WS_EX_TOOLWINDOW)
        # Windows 10 2004+: keep our own overlay out of screen-capture APIs.
        try:
            WDA_EXCLUDEFROMCAPTURE = 0x00000011
            user32.SetWindowDisplayAffinity(hwnd, WDA_EXCLUDEFROMCAPTURE)
        except Exception:
            pass

    def toggle(self) -> None:
        self.visible = not self.visible
        if self.visible:
            self.root.deiconify()
        else:
            self.root.withdraw()

    def _pump(self) -> None:
        try:
            while True:
                self.last_state = self.state_queue.get_nowait()
        except queue.Empty:
            pass
        if self.visible and self.last_state:
            self._draw(self.last_state)
        self.root.after(33, self._pump)

    def _draw_marker(self, x: float, y: float, favor: int, route_idx: int | None, confidence: float) -> None:
        # Deliberately non-red overlay colors so the CV detector cannot learn its own output.
        fill = {1: "#55b9d6", 3: "#d5aa45", 5: "#f2eee2"}.get(favor, "#d5aa45")
        outline = "#86f7a8" if route_idx is not None else "#22252a"
        radius = 14 if route_idx is not None else 10
        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=fill, outline=outline, width=3)
        label = str(route_idx) if route_idx is not None else str(favor)
        label_color = "#101216" if favor == 5 else "#ffffff"
        self.canvas.create_text(x, y, text=label, fill=label_color, font=("Segoe UI", 9, "bold"))
        if confidence < 0.55:
            self.canvas.create_text(x+12, y-12, text="?", fill="#ffe08a", font=("Segoe UI", 8, "bold"))

    def _draw_hazard(self, event: DangerEvent) -> None:
        # Cyan/green/white are intentional: danger CV watches red/orange, so even a
        # broken capture-exclusion driver cannot create a warning feedback loop.
        urgent = event.urgent
        outline = "#f7fbff" if urgent else "#00e5ff"
        accent = "#fff59b" if event.kind == "executioner" else ("#7fffd4" if event.kind in {"slash", "projectile"} else "#9fe9ff")
        width = 5 if urgent else 3
        pts = [coord for p in event.polygon for coord in p]
        if len(pts) >= 6:
            self.canvas.create_polygon(*pts, outline=outline, fill="", width=width)
        x, y, w, h = event.bbox
        if event.kind == "explosion":
            self.canvas.create_oval(x, y, x+w, y+h, outline=outline, width=width, dash=(7, 4) if not urgent else None)
        elif event.kind in {"slash", "projectile", "executioner"}:
            vx, vy = event.velocity
            cx, cy = event.center
            if abs(vx) + abs(vy) > 1:
                scale = 0.18
                self.canvas.create_line(cx, cy, cx + vx * scale, cy + vy * scale, fill=accent, width=3, arrow=tk.LAST)
        label = event.label
        if event.eta_seconds is not None:
            label += f"  {max(0.0, event.eta_seconds):.1f}s"
        self.canvas.create_text(
            event.center[0],
            max(34, y - 18),
            text=label,
            fill=outline,
            font=("Segoe UI", 10 if urgent else 9, "bold"),
        )

    def _draw(self, s: OverlayState) -> None:
        self.canvas.delete("all")

        if s.danger_enabled:
            for event in s.hazards:
                self._draw_hazard(event)
            top = s.hazards[0] if s.hazards else None
            if top and top.level >= DANGER_HIGH:
                # Strong peripheral flash without obscuring gameplay.
                self.canvas.create_rectangle(8, 8, self.width-8, self.height-8, outline="#e8ffff", width=6)
                banner = top.label
                if top.eta_seconds is not None:
                    banner += f" · {max(0.0, top.eta_seconds):.1f}s"
                self.canvas.create_rectangle(self.width/2-235, 34, self.width/2+235, 82, fill="#111820", outline="#e8ffff", width=2)
                self.canvas.create_text(self.width/2, 58, text=banner, fill="#ffffff", font=("Segoe UI", 18, "bold"))

        route_index = {item.id: i+1 for i, (item, _x, _y) in enumerate(s.route_points)}
        if s.route_points and len(s.route_points) > 1:
            coords = []
            for _item, x, y in s.route_points:
                coords += [x, y]
            self.canvas.create_line(*coords, fill="#ffd36a", width=3, dash=(7, 5))
        for item, x, y in s.screen_points:
            if -30 <= x <= self.width+30 and -30 <= y <= self.height+30:
                self._draw_marker(x, y, item.favor, route_index.get(item.id), item.confidence)

        # Compact unobtrusive panel in the upper-right.
        panel_w = 316
        panel_h = 158 + min(5, len(s.route.items)) * 22
        x0 = self.width - panel_w - 18
        y0 = 92
        self.canvas.create_rectangle(x0, y0, x0+panel_w, y0+panel_h, fill="#151318", outline="#6c5a46", width=1)
        mode = f" {s.map_mode}" if s.map_mode else ""
        reg = f"Map {'LOCK' if s.registered else 'searching'}{mode} · {s.inliers}/{s.matches} inliers · atlas {s.atlas_keyframes}"
        self.canvas.create_text(x0+14, y0+14, anchor="nw", text="WHISPER HUNTER + DANGERSENSE", fill="#f0dcc1", font=("Segoe UI", 11, "bold"))
        self.canvas.create_text(x0+14, y0+38, anchor="nw", text=reg, fill="#aaa2a1", font=("Segoe UI", 8))
        self.canvas.create_text(x0+14, y0+58, anchor="nw", text=f"Favors {s.current_favors}/10  ·  tracked {s.tracked_total}", fill="#ffffff", font=("Segoe UI", 9, "bold"))
        danger_state = "ON" if s.danger_enabled else "OFF"
        sound_state = "ON" if s.danger_sound_enabled else "MUTED"
        hazard_count = len(s.hazards)
        self.canvas.create_text(x0+14, y0+80, anchor="nw", text=f"DangerSense {danger_state} · sound {sound_state} · threats {hazard_count}", fill="#8defff", font=("Segoe UI", 9, "bold"))
        evade_state = "ON" if s.auto_evade_enabled else "OFF"
        self.canvas.create_text(x0+14, y0+100, anchor="nw", text=f"Executioner Guard · Smart Evade {evade_state}", fill="#fff59b", font=("Segoe UI", 9, "bold"))
        route_line = f"Route +{s.route.favor}F · ~{s.route.estimated_minutes:.0f}m" if s.route.items else "Route waiting for markers"
        self.canvas.create_text(x0+14, y0+122, anchor="nw", text=route_line, fill="#ffd36a", font=("Segoe UI", 9, "bold"))
        status = s.danger_alert or s.status
        self.canvas.create_text(x0+14, y0+142, anchor="nw", text=status[:48], fill="#aaa2a1", font=("Segoe UI", 8))
        yy = y0 + 162
        for i, item in enumerate(s.route.items[:5], 1):
            self.canvas.create_text(x0+16, yy, anchor="nw", text=f"{i}. {item.favor} Favor  ·  conf {item.confidence:.0%}", fill="#f2e8df", font=("Segoe UI", 8))
            yy += 22

    def run(self) -> None:
        self.root.mainloop()
