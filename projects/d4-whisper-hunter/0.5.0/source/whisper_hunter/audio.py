from __future__ import annotations

import math
import os
from pathlib import Path
import struct
import wave

from .config import Config, app_dir
from .danger import DangerAlertGate, DangerEvent


def _write_tone_pattern(path: Path, pattern: list[tuple[float, int]], volume: float) -> None:
    rate = 22050
    amp = int(32767 * max(0.05, min(1.0, volume)))
    frames = bytearray()
    phase = 0.0
    for duration, hz in pattern:
        count = max(1, int(rate * duration))
        if hz <= 0:
            frames.extend(b"\x00\x00" * count)
            continue
        step = 2.0 * math.pi * hz / rate
        for i in range(count):
            # Small attack/release envelope avoids hard clicks while staying urgent.
            edge = min(i / max(1, int(rate * 0.008)), (count - i - 1) / max(1, int(rate * 0.010)), 1.0)
            sample = int(amp * max(0.0, edge) * math.sin(phase))
            frames.extend(struct.pack("<h", sample))
            phase += step
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(frames)


class DangerSoundEngine:
    """Native Windows asynchronous warning sounds; no media/audio dependency."""

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.enabled = bool(cfg.danger_sound_enabled)
        self.gate = DangerAlertGate(cfg.danger_sound_cooldown_s, cfg.danger_urgent_sound_cooldown_s)
        self._paths: dict[str, Path] = {}
        if os.name == "nt":
            self._prepare()

    def _prepare(self) -> None:
        folder = app_dir() / "sounds"
        volume = float(self.cfg.danger_sound_volume)
        patterns = {
            # Executioner gets its own unmistakable alarm: three fast descending
            # strikes followed by a piercing high confirmation tone.
            "executioner": [(0.060, 2050), (0.018, 0), (0.060, 1680), (0.018, 0), (0.070, 1320), (0.018, 0), (0.110, 2280)],
            # Sharp rising double chirp = ordinary blade/slash.
            "slash": [(0.075, 1120), (0.028, 0), (0.095, 1760)],
            # Faster version used for a moving attack entering the player trajectory.
            "projectile": [(0.055, 1320), (0.020, 0), (0.055, 1760), (0.020, 0), (0.075, 2090)],
            # Lower triple pulse is hard to confuse with the blade cue.
            "explosion": [(0.095, 520), (0.030, 0), (0.095, 700), (0.030, 0), (0.120, 920)],
            "cone": [(0.090, 780), (0.030, 0), (0.105, 1260)],
            "danger": [(0.090, 950), (0.030, 0), (0.110, 1450)],
        }
        for key, pat in patterns.items():
            p = folder / f"{key}.wav"
            try:
                _write_tone_pattern(p, pat, volume)
                self._paths[key] = p
            except Exception:
                pass

    def set_enabled(self, enabled: bool) -> None:
        self.enabled = bool(enabled)
        if not self.enabled:
            self.gate.reset()

    def alert(self, event: DangerEvent, now: float) -> bool:
        if not self.enabled or not self.gate.should_alert(event, now):
            return False
        if os.name != "nt":
            return False
        try:
            import winsound

            path = self._paths.get(event.kind) or self._paths.get("danger")
            if path and path.exists():
                flags = winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT
                winsound.PlaySound(str(path), flags)
                return True
        except Exception:
            pass
        return False
