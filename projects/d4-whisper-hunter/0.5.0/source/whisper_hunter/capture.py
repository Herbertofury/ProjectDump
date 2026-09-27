from __future__ import annotations

import ctypes
import os
from typing import Iterable

import cv2
import numpy as np


def _intersection_area(a: tuple[int, int, int, int], b: dict) -> int:
    ax1, ay1, ax2, ay2 = a
    bx1 = int(b.get("left", 0))
    by1 = int(b.get("top", 0))
    bx2 = bx1 + int(b.get("width", 0))
    by2 = by1 + int(b.get("height", 0))
    w = max(0, min(ax2, bx2) - max(ax1, bx1))
    h = max(0, min(ay2, by2) - max(ay1, by1))
    return w * h


def select_monitor_index(monitors: Iterable[dict], window_rect: tuple[int, int, int, int] | None) -> int:
    monitors = list(monitors)
    # mss index 0 is the virtual desktop; physical monitors start at 1.
    if len(monitors) <= 1:
        return 0
    if window_rect:
        scored = [(_intersection_area(window_rect, monitors[i]), i) for i in range(1, len(monitors))]
        scored.sort(reverse=True)
        if scored and scored[0][0] > 0:
            return scored[0][1]
    return 1


def _find_diablo_window_rect() -> tuple[int, int, int, int] | None:
    if os.name != "nt":
        return None
    user32 = ctypes.windll.user32
    matches: list[tuple[int, tuple[int, int, int, int]]] = []

    WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)

    @WNDENUMPROC
    def callback(hwnd, _lparam):
        try:
            if not user32.IsWindowVisible(hwnd):
                return True
            length = user32.GetWindowTextLengthW(hwnd)
            if length <= 0:
                return True
            buf = ctypes.create_unicode_buffer(length + 1)
            user32.GetWindowTextW(hwnd, buf, length + 1)
            title = buf.value.strip().lower()
            if "diablo iv" not in title:
                return True
            rect = ctypes.wintypes.RECT()
            if not user32.GetWindowRect(hwnd, ctypes.byref(rect)):
                return True
            candidate = (int(rect.left), int(rect.top), int(rect.right), int(rect.bottom))
            area = max(0, candidate[2] - candidate[0]) * max(0, candidate[3] - candidate[1])
            if area > 0:
                matches.append((area, candidate))
        except Exception:
            pass
        return True

    try:
        # wintypes is lazily exposed by ctypes on Windows.
        import ctypes.wintypes  # noqa: F401
        user32.EnumWindows(callback, 0)
    except Exception:
        return None
    if not matches:
        return None
    matches.sort(reverse=True, key=lambda item: item[0])
    return matches[0][1]


class ScreenCapture:
    def __init__(self, monitor_index: int | None = None):
        try:
            from mss import mss
        except ImportError as exc:
            raise RuntimeError("Missing dependency 'mss'. Run install.bat or pip install -r requirements.txt") from exc
        self._ctx = mss()
        requested = monitor_index
        if requested is None:
            requested = select_monitor_index(self._ctx.monitors, _find_diablo_window_rect())
        if requested < 0 or requested >= len(self._ctx.monitors):
            requested = 1 if len(self._ctx.monitors) > 1 else 0
        self.monitor_index = int(requested)
        self.monitor = dict(self._ctx.monitors[self.monitor_index])

    @property
    def size(self) -> tuple[int, int]:
        return int(self.monitor["width"]), int(self.monitor["height"])

    @property
    def origin(self) -> tuple[int, int]:
        return int(self.monitor.get("left", 0)), int(self.monitor.get("top", 0))

    def grab(self) -> np.ndarray:
        arr = np.array(self._ctx.grab(self.monitor), dtype=np.uint8)
        return cv2.cvtColor(arr, cv2.COLOR_BGRA2BGR)

    def close(self) -> None:
        try:
            self._ctx.close()
        except Exception:
            pass
