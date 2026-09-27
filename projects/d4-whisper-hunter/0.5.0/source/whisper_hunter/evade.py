from __future__ import annotations

import ctypes
import os
import time
from typing import Callable

from .config import Config
from .danger import DANGER_HIGH, DangerEvent


# Input behavior is intentionally tiny and transparent. The MIT
# griffeth-barker/Diablo-IV-Evade-Macro proved the useful product rule we retain:
# send the evade key only while Diablo IV is the foreground window. Unlike that
# archived macro, this controller never spams Space on a timer and never activates
# or steals focus from the game. DangerSense decides *when* one evade is warranted.


def diablo_is_foreground() -> bool:
    if os.name != "nt":
        return False
    try:
        user32 = ctypes.windll.user32
        hwnd = user32.GetForegroundWindow()
        if not hwnd:
            return False
        length = int(user32.GetWindowTextLengthW(hwnd))
        if length <= 0:
            return False
        buf = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buf, length + 1)
        title = buf.value.strip().lower()
        return title == "diablo iv" or title.startswith("diablo iv ")
    except Exception:
        return False


def _modifiers_clear() -> bool:
    """Avoid turning our synthetic Evade into one of the app's Ctrl/Alt hotkeys."""
    if os.name != "nt":
        return True
    try:
        user32 = ctypes.windll.user32
        for vk in (0x10, 0x11, 0x12, 0x5B, 0x5C):  # Shift, Ctrl, Alt, Win L/R
            if int(user32.GetAsyncKeyState(vk)) & 0x8000:
                return False
        return True
    except Exception:
        return False


def _send_virtual_key(vk: int) -> bool:
    """Send one key-down/key-up pair through Win32 SendInput."""
    if os.name != "nt":
        return False
    try:
        from ctypes import wintypes

        INPUT_KEYBOARD = 1
        KEYEVENTF_KEYUP = 0x0002
        ULONG_PTR = wintypes.WPARAM

        class KEYBDINPUT(ctypes.Structure):
            _fields_ = [
                ("wVk", wintypes.WORD),
                ("wScan", wintypes.WORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", ULONG_PTR),
            ]

        class _INPUTUNION(ctypes.Union):
            _fields_ = [("ki", KEYBDINPUT)]

        class INPUT(ctypes.Structure):
            _anonymous_ = ("u",)
            _fields_ = [("type", wintypes.DWORD), ("u", _INPUTUNION)]

        key_down = INPUT(type=INPUT_KEYBOARD, ki=KEYBDINPUT(vk, 0, 0, 0, 0))
        key_up = INPUT(type=INPUT_KEYBOARD, ki=KEYBDINPUT(vk, 0, KEYEVENTF_KEYUP, 0, 0))
        inputs = (INPUT * 2)(key_down, key_up)
        sent = int(ctypes.windll.user32.SendInput(2, ctypes.byref(inputs), ctypes.sizeof(INPUT)))
        return sent == 2
    except Exception:
        return False


class EvadeController:
    """Event-driven foreground-only Diablo IV evade dispatcher.

    It consumes passive DangerSense events and emits at most one configured evade
    keypress per threat/cooldown window. It does not read game memory, hook input,
    keep a key-spam loop, or bring Diablo IV to the foreground.
    """

    def __init__(
        self,
        cfg: Config,
        *,
        sender: Callable[[int], bool] | None = None,
        foreground_check: Callable[[], bool] | None = None,
        input_guard: Callable[[], bool] | None = None,
    ):
        self.cfg = cfg
        self.enabled = bool(cfg.auto_evade_enabled)
        self._sender = sender or _send_virtual_key
        self._foreground_check = foreground_check or diablo_is_foreground
        self._input_guard = input_guard or _modifiers_clear
        self._last_evade_at = float("-inf")
        self._seen: dict[int, float] = {}
        self._last_reason = ""

    @property
    def last_reason(self) -> str:
        return self._last_reason

    def set_enabled(self, enabled: bool) -> None:
        self.enabled = bool(enabled)
        if not self.enabled:
            self._seen.clear()
            self._last_reason = ""

    def _eligible(self, event: DangerEvent) -> bool:
        if event.confidence < float(self.cfg.auto_evade_min_confidence):
            return False

        # The Executioner is the primary reason for Smart Evade. An explicit lock
        # cue is decisive; a high-confidence high-danger drop/impact is also enough
        # because current D4 versions can shorten the visible tracking phase.
        if event.kind == "executioner":
            if not self.cfg.auto_evade_executioner:
                return False
            if event.locked:
                return True
            if event.eta_seconds is not None:
                return event.eta_seconds <= float(self.cfg.auto_evade_eta_s)
            # Do not burn an evade merely because the sword is visibly tracking:
            # current and older Executioner variants can follow the player before
            # committing. Auto-evade only after lock or an inferred imminent drop.
            return False

        if event.kind == "explosion":
            if not self.cfg.auto_evade_explosions:
                return False
            return event.level >= DANGER_HIGH and (
                event.eta_seconds is None
                or event.eta_seconds <= float(self.cfg.auto_evade_eta_s)
            )

        if event.kind == "projectile":
            if not self.cfg.auto_evade_projectiles:
                return False
            return (
                event.level >= DANGER_HIGH
                and event.eta_seconds is not None
                and event.eta_seconds <= float(self.cfg.auto_evade_eta_s)
            )

        if event.kind == "cone":
            if not self.cfg.auto_evade_cones:
                return False
            return event.level >= DANGER_HIGH and (
                event.eta_seconds is None
                or event.eta_seconds <= float(self.cfg.auto_evade_eta_s)
            )

        # Generic slash geometry is deliberately warning-only. Auto-evading every
        # red line would waste charges; the dedicated Executioner path handles the
        # notorious overhead sword specifically.
        return False

    def maybe_evade(self, events: list[DangerEvent], now: float | None = None) -> DangerEvent | None:
        if not self.enabled:
            return None
        if now is None:
            now = time.time()

        prune_before = now - max(2.0, float(self.cfg.auto_evade_seen_ttl_s))
        self._seen = {tid: t for tid, t in self._seen.items() if t >= prune_before}

        if now - self._last_evade_at < max(0.10, float(self.cfg.auto_evade_cooldown_s)):
            return None
        if self.cfg.auto_evade_foreground_only and not self._foreground_check():
            return None
        if not self._input_guard():
            return None

        # Priority is already danger-sorted, but explicitly bias Executioner so a
        # sword lock wins over a coincident generic explosion contour.
        ordered = sorted(
            events,
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
        for event in ordered:
            if event.id in self._seen or not self._eligible(event):
                continue
            if not self._sender(int(self.cfg.auto_evade_vk)):
                return None
            self._seen[event.id] = now
            self._last_evade_at = now
            self._last_reason = event.label
            return event
        return None
