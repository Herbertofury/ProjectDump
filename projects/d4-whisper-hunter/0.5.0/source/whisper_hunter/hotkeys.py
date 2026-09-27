from __future__ import annotations

import ctypes
from ctypes import wintypes
import os


class Hotkeys:
    """Tiny RegisterHotKey wrapper; no keyboard-hook dependency."""
    WM_HOTKEY = 0x0312
    MOD_ALT = 0x0001
    MOD_CONTROL = 0x0002
    MOD_SHIFT = 0x0004
    MOD_NOREPEAT = 0x4000

    def __init__(self):
        self.enabled = os.name == "nt"
        self.user32 = ctypes.windll.user32 if self.enabled else None
        self.bindings: dict[int, str] = {}
        self._next_id = 1

    def register(self, name: str, vk: int, mods: int) -> bool:
        if not self.enabled:
            return False
        ident = self._next_id
        self._next_id += 1
        ok = bool(self.user32.RegisterHotKey(None, ident, mods | self.MOD_NOREPEAT, vk))
        if ok:
            self.bindings[ident] = name
        return ok

    def poll(self) -> list[str]:
        if not self.enabled:
            return []
        out = []
        msg = wintypes.MSG()
        PM_REMOVE = 0x0001
        while self.user32.PeekMessageW(ctypes.byref(msg), None, self.WM_HOTKEY, self.WM_HOTKEY, PM_REMOVE):
            name = self.bindings.get(int(msg.wParam))
            if name:
                out.append(name)
        return out

    def close(self) -> None:
        if not self.enabled:
            return
        for ident in list(self.bindings):
            self.user32.UnregisterHotKey(None, ident)
        self.bindings.clear()
