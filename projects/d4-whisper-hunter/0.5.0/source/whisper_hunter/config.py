from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path


@dataclass(slots=True)
class Config:
    scan_hz: float = 4.0
    register_hz: float = 2.0
    min_feature_matches: int = 28
    stale_after_minutes: int = 100
    disappear_after_scans: int = 5
    marker_merge_radius_px: float = 34.0
    route_target_favors: int = 10
    route_distance_weight: float = 1.0
    route_activity_weight: float = 28.0
    favor1_minutes: float = 2.0
    favor3_minutes: float = 4.0
    favor5_minutes: float = 6.0
    overlay_opacity: float = 0.93
    show_route_lines: bool = True
    show_history: bool = False
    debug: bool = False

    # DangerSense: passive screen-reading lethal-telegraph warnings.
    danger_enabled: bool = True
    danger_overlay_enabled: bool = True
    danger_sound_enabled: bool = True
    danger_hz: float = 24.0
    danger_max_cv_width: int = 1120
    danger_player_screen_y: float = 0.50
    danger_player_radius_px: float = 105.0
    danger_min_confidence: float = 0.56
    danger_immediate_confidence: float = 0.79
    danger_confirm_frames: int = 2
    danger_track_hold_s: float = 0.18
    danger_projectile_min_speed_px_s: float = 145.0
    danger_projectile_horizon_s: float = 2.4
    danger_max_events: int = 12
    danger_sound_volume: float = 0.62
    danger_sound_cooldown_s: float = 1.20
    danger_urgent_sound_cooldown_s: float = 0.48

    # Executioner Guard: dedicated detector for the overhead tracking sword.
    executioner_enabled: bool = True
    executioner_center_half_width_px: float = 235.0
    executioner_overhead_height_px: float = 360.0
    executioner_min_blade_aspect: float = 2.65
    executioner_lock_radius_px: float = 125.0
    executioner_lock_eta_s: float = 0.42

    # Smart Evade: event-driven foreground-only evade key dispatch. Defaults are
    # intentionally conservative; generic red slash geometry remains warning-only.
    auto_evade_enabled: bool = True
    auto_evade_foreground_only: bool = True
    auto_evade_vk: int = 0x20  # Space, Diablo IV default Evade binding.
    auto_evade_min_confidence: float = 0.72
    auto_evade_eta_s: float = 0.90
    auto_evade_cooldown_s: float = 0.72
    auto_evade_seen_ttl_s: float = 5.0
    auto_evade_executioner: bool = True
    auto_evade_explosions: bool = True
    auto_evade_projectiles: bool = True
    auto_evade_cones: bool = False


def app_dir() -> Path:
    base = os.environ.get("APPDATA")
    if base:
        p = Path(base) / "D4WhisperHunter"
    else:
        p = Path.home() / ".d4-whisper-hunter"
    p.mkdir(parents=True, exist_ok=True)
    return p


def load_config() -> Config:
    path = app_dir() / "config.json"
    if not path.exists():
        cfg = Config()
        save_config(cfg)
        return cfg
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        valid = {k: v for k, v in raw.items() if k in Config.__dataclass_fields__}
        return Config(**valid)
    except Exception:
        return Config()


def save_config(cfg: Config) -> None:
    (app_dir() / "config.json").write_text(
        json.dumps(asdict(cfg), indent=2, sort_keys=True), encoding="utf-8"
    )
