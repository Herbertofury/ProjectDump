from __future__ import annotations

import json
import math
from pathlib import Path
import tempfile

import cv2
import numpy as np

from whisper_hunter.config import Config
from whisper_hunter.detection import detect_whispers
from whisper_hunter.homography import MapRegistrar, Registration
from whisper_hunter.routing import plan_route
from whisper_hunter.tracker import TrackedWhisper, WhisperTracker


def _make_textured_map(width=1200, height=900):
    rng = np.random.default_rng(42)
    img = np.full((height, width, 3), 74, np.uint8)
    noise = rng.integers(-18, 19, size=(height, width, 1), dtype=np.int16)
    img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    for i in range(320):
        x = int(rng.integers(20, width-20))
        y = int(rng.integers(20, height-20))
        rad = int(rng.integers(2, 13))
        c = int(rng.integers(35, 160))
        cv2.circle(img, (x,y), rad, (c, c+5 if c<250 else c, c), 1)
    for i in range(55):
        x1 = int(rng.integers(0,width)); y1=int(rng.integers(0,height))
        x2 = int(rng.integers(0,width)); y2=int(rng.integers(0,height))
        cv2.line(img,(x1,y1),(x2,y2),(110,102,95),1)
    for i in range(25):
        cv2.putText(img, f"Z{i:02d}", (25+(i*43)%1050, 40+(i*71)%800), cv2.FONT_HERSHEY_SIMPLEX, .55, (150,140,130), 1, cv2.LINE_AA)
    return img


def test_detector_classifies_1_3_5():
    img = np.full((1080, 1920, 3), (70, 68, 65), np.uint8)
    # BGR colors deliberately span light pink -> rose -> deep red.
    samples = [
        ((350, 400), (180, 170, 245)),
        ((850, 500), (90, 70, 215)),
        ((1350, 600), (30, 20, 150)),
    ]
    for (x,y), color in samples:
        cv2.circle(img, (x,y), 12, color, 4)
        cv2.line(img, (x-14,y), (x+14,y), color, 3)
        cv2.line(img, (x,y-14), (x,y+14), color, 3)
    found = detect_whispers(img)
    favors = sorted(c.favor for c in found)
    assert favors == [1, 3, 5], [(c.favor, c.saturation, c.value, c.redness, c.bbox) for c in found]


def test_sift_registration_maps_query_back_to_canonical():
    base = _make_textured_map()
    registrar = MapRegistrar(base, max_features=5000)
    # Crop a real subsection and apply a slight perspective warp to mimic D4 map display.
    crop = base[120:760, 180:1060].copy()
    h,w = crop.shape[:2]
    src = np.float32([[0,0],[w-1,0],[w-1,h-1],[0,h-1]])
    dst = np.float32([[22,15],[w-25,5],[w-6,h-20],[8,h-2]])
    P = cv2.getPerspectiveTransform(src,dst)
    query = cv2.warpPerspective(crop, P, (w,h), borderMode=cv2.BORDER_REFLECT)
    reg = registrar.register(query, min_matches=24)
    assert reg is not None
    assert reg.inliers >= 12
    # Query center should land near the corresponding map crop center.
    mapped = registrar.query_points_to_map([(w/2,h/2)], reg)[0]
    expected = np.array([180+w/2, 120+h/2])
    assert np.linalg.norm(mapped-expected) < 18.0, (mapped, expected, reg.inliers, reg.good_matches)


def test_tracker_accumulates_and_marks_gone_after_repeated_visible_misses(tmp_path: Path):
    cfg = Config(disappear_after_scans=3, marker_merge_radius_px=20)
    tracker = WhisperTracker(cfg, tmp_path/'state.json')
    I = np.eye(3, dtype=np.float64)
    poly = np.array([[0,0],[1000,0],[1000,1000],[0,1000]], np.float32)
    reg = Registration(I,I,50,60,poly)
    tracker.update([((100.0,100.0),5,0.9)], reg, now=1000.0)
    assert len(tracker.active()) == 1
    tracker.update([], reg, now=1001.0)
    tracker.update([], reg, now=1002.0)
    assert len(tracker.active()) == 1
    tracker.update([], reg, now=1003.0)
    assert len(tracker.active()) == 0
    assert tracker.items[0].state == 'gone'


def test_route_reaches_next_cache_without_using_every_marker():
    cfg = Config(route_target_favors=10, route_distance_weight=1.0, route_activity_weight=20.0)
    now = 1000.0
    vals = [
        TrackedWhisper(1, 10, 0, 5, .95, now, now),
        TrackedWhisper(2, 20, 0, 5, .95, now, now),
        TrackedWhisper(3, 500, 500, 3, .95, now, now),
        TrackedWhisper(4, 600, 600, 1, .95, now, now),
    ]
    plan = plan_route(vals, (0,0), current_favors=0, cfg=cfg)
    assert plan.favor >= 10
    assert [x.id for x in plan.items] == [1,2]
    plan2 = plan_route(vals, (0,0), current_favors=5, cfg=cfg)
    assert plan2.favor >= 5
    assert plan2.items[0].id == 1


def test_detector_rejects_flat_red_decoys_and_tree_like_wide_icons():
    img = np.full((1080, 1920, 3), (70, 68, 65), np.uint8)
    whisper = (90, 70, 215)
    # One framed/detail-rich Whisper-like glyph should survive.
    x, y = 360, 520
    cv2.circle(img, (x, y), 12, whisper, 4)
    cv2.line(img, (x - 14, y), (x + 14, y), whisper, 3)
    cv2.line(img, (x, y - 14), (x, y + 14), whisper, 3)
    # Common red-map decoy shapes: flat event/boss pips and a wide Tree-like badge.
    cv2.circle(img, (760, 520), 14, whisper, -1)
    diamond = np.array([[1110, 503], [1127, 520], [1110, 537], [1093, 520]], np.int32)
    cv2.fillPoly(img, [diamond], whisper)
    cv2.ellipse(img, (1450, 520), (31, 10), 0, 0, 360, whisper, -1)

    found = detect_whispers(img)
    assert len(found) == 1, [(c.center, c.bbox, c.shape_score, c.holes, c.edge_density) for c in found]
    assert math.hypot(found[0].center[0] - 360, found[0].center[1] - 520) < 4
    assert found[0].shape_score > 0.55


def test_detector_rejects_huge_red_regions_and_thin_ui_stripes():
    img = np.full((1080, 1920, 3), (70, 68, 65), np.uint8)
    red = (40, 30, 180)
    cv2.rectangle(img, (250, 220), (1050, 900), red, -1)
    cv2.rectangle(img, (1200, 450), (1750, 456), red, -1)
    assert detect_whispers(img) == []

from whisper_hunter.atlas import FeatureAtlas


def test_visual_atlas_localizes_overlapping_expansion_frames(tmp_path: Path):
    base = _make_textured_map(1800, 1000)
    atlas = FeatureAtlas(tmp_path/'atlas.npz', max_query_width=1000, sample_per_keyframe=500, keyframe_spacing=120)
    # First viewport: world translation is known (as if anchored by the static map).
    f1 = base[120:720, 100:1000].copy()
    H1 = np.array([[1,0,100],[0,1,120],[0,0,1]], np.float64)
    assert atlas.add_keyframe(f1, H1, source='static', force=True)
    # Second viewport overlaps but extends into previously unseen territory.
    f2 = base[160:760, 520:1420].copy()
    reg2 = atlas.localize(f2, min_matches=24)
    assert reg2 is not None
    center = atlas._transform_points(np.array([[450,300]],np.float32), reg2.query_to_map)[0]
    expected = np.array([520+450,160+300],np.float32)
    assert np.linalg.norm(center-expected) < 18, (center, expected, reg2.inliers, reg2.good_matches)
    assert atlas.add_keyframe(f2, reg2.query_to_map, force=True)
    # Third frame has little/no overlap with frame 1 but overlaps frame 2: proves chaining.
    f3 = base[200:800, 900:1800].copy()
    reg3 = atlas.localize(f3, min_matches=24)
    assert reg3 is not None
    center3 = atlas._transform_points(np.array([[450,300]],np.float32), reg3.query_to_map)[0]
    expected3 = np.array([900+450,200+300],np.float32)
    assert np.linalg.norm(center3-expected3) < 24, (center3, expected3, reg3.inliers, reg3.good_matches)
    # Persistence keeps the learned expansion descriptors.
    atlas2 = FeatureAtlas(tmp_path/'atlas.npz', max_query_width=1000)
    assert atlas2.ready and atlas2.keyframe_count == 2
    reg3b = atlas2.localize(f3, min_matches=24)
    assert reg3b is not None


def test_detector_does_not_force_three_favor_classes_from_same_color_family():
    img = np.full((1080, 1920, 3), (70, 68, 65), np.uint8)
    colors = [(96, 74, 218), (91, 69, 214), (87, 66, 210), (99, 76, 220)]
    for i, color in enumerate(colors):
        x, y = 360 + i * 330, 520 + (i % 2) * 28
        cv2.circle(img, (x, y), 12, color, 4)
        cv2.line(img, (x - 14, y), (x + 14, y), color, 3)
        cv2.line(img, (x, y - 14), (x, y + 14), color, 3)
    found = detect_whispers(img)
    assert len(found) == 4
    assert len({c.favor for c in found}) == 1, [(c.favor, c.saturation, c.value, c.redness) for c in found]


def test_visual_atlas_free_seed_is_immediately_localizable(tmp_path: Path):
    base = _make_textured_map(1200, 800)
    atlas = FeatureAtlas(tmp_path / 'free-atlas.npz', max_query_width=1000, sample_per_keyframe=450)
    reg = atlas.seed_free(base)
    assert reg is not None
    assert atlas.ready and atlas.world_source == 'free' and atlas.keyframe_count == 1
    relock = atlas.localize(base.copy(), min_matches=24)
    assert relock is not None
    p = atlas._transform_points(np.array([[600, 400]], np.float32), relock.query_to_map)[0]
    assert np.linalg.norm(p - np.array([600, 400], np.float32)) < 12

from whisper_hunter.danger import (
    DANGER_HIGH,
    DangerAlertGate,
    DangerDetector,
    DangerEvent,
)


def _danger_frame(kind: str, x: int = 960, y: int = 520) -> np.ndarray:
    img = np.full((1080, 1920, 3), (28, 28, 31), np.uint8)
    red = (32, 72, 238)
    if kind == "explosion":
        cv2.circle(img, (x, y), 130, red, 18)
        cv2.circle(img, (x, y), 80, (20, 45, 180), 8)
    elif kind == "slash":
        box = cv2.boxPoints(((x, y), (420, 34), -18)).astype(np.int32)
        cv2.fillConvexPoly(img, box, red)
    elif kind == "cone":
        pts = np.array([[x-300, y-130], [x+50, y], [x-300, y+130]], np.int32)
        cv2.fillConvexPoly(img, pts, red)
    return img


def test_dangersense_detects_near_player_explosion_after_confirmation():
    cfg = Config(danger_confirm_frames=2, danger_min_confidence=0.50, danger_immediate_confidence=0.995)
    det = DangerDetector(cfg)
    frame = _danger_frame("explosion")
    assert det.update(frame, 1000.0) == []
    events = det.update(frame, 1000.05)
    assert events
    top = events[0]
    assert top.kind == "explosion"
    assert top.level == DANGER_HIGH
    assert top.distance_to_player <= 1.0
    assert top.eta_seconds == 0.0


def test_dangersense_detects_sword_slash_geometry_and_ignores_hud_red():
    cfg = Config(danger_confirm_frames=1, danger_min_confidence=0.50)
    det = DangerDetector(cfg)
    frame = _danger_frame("slash")
    # Bottom HUD-like red blocks must not become alerts.
    cv2.rectangle(frame, (50, 960), (420, 1075), (20, 30, 230), -1)
    cv2.rectangle(frame, (1500, 940), (1900, 1070), (20, 30, 230), -1)
    events = det.update(frame, 2000.0)
    assert events
    assert events[0].kind == "slash"
    assert events[0].level >= 2
    assert all(e.center[1] < 0.90 * 1080 for e in events)


def test_dangersense_reclassifies_fast_incoming_slash_as_projectile():
    cfg = Config(
        danger_confirm_frames=1,
        danger_min_confidence=0.50,
        danger_projectile_min_speed_px_s=100.0,
        danger_projectile_horizon_s=3.0,
    )
    det = DangerDetector(cfg)
    # Horizontal narrow warning moves toward the player's center from the left.
    f1 = _danger_frame("slash", x=430, y=540)
    f2 = _danger_frame("slash", x=560, y=540)
    det.update(f1, 3000.0)
    events = det.update(f2, 3000.10)
    assert events
    top = events[0]
    assert top.kind == "projectile", [(e.kind, e.velocity, e.eta_seconds, e.level) for e in events]
    assert top.level == DANGER_HIGH
    assert top.eta_seconds is not None and 0.0 < top.eta_seconds < 1.0


def test_dangersense_suppresses_all_warnings_while_world_map_is_open():
    cfg = Config(danger_confirm_frames=1, danger_min_confidence=0.50)
    det = DangerDetector(cfg)
    frame = _danger_frame("explosion")
    assert det.update(frame, 4000.0, suppress=True) == []
    assert det.update(frame, 4000.05, suppress=True) == []


def test_danger_alert_gate_debounces_but_allows_urgent_escalation():
    gate = DangerAlertGate(normal_cooldown=1.0, urgent_cooldown=0.3)
    base = DangerEvent(1, "slash", 2, .8, (0,0), (0,0,10,10), ((0,0),(1,0),(1,1)), 10.0)
    urgent = DangerEvent(1, "slash", 3, .9, (0,0), (0,0,10,10), ((0,0),(1,0),(1,1)), 0.0, eta_seconds=.3)
    assert gate.should_alert(base, 10.0)
    assert not gate.should_alert(base, 10.2)
    assert gate.should_alert(urgent, 10.21)
    assert not gate.should_alert(urgent, 10.35)
    assert gate.should_alert(urgent, 10.55)


def test_scaled_map_registrar_preserves_full_world_coordinates():
    base = _make_textured_map(2200, 1600)
    half = cv2.resize(base, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    registrar = MapRegistrar(half, max_features=5000, world_scale=2.0)
    # Mimic the donor overlay path: query/map pixels live at the 0.5x anchor scale,
    # while returned world coordinates must remain in our full-resolution lineage.
    x, y, w0, h0 = 80, 40, 980, 720
    crop = half[y:y+h0, x:x+w0].copy()
    h, w = crop.shape[:2]
    reg = registrar.register(crop, min_matches=18)
    assert reg is not None
    mapped = registrar.query_points_to_map([(w/2, h/2)], reg)[0]
    expected = np.array([(x+w/2)*2.0, (y+h/2)*2.0])
    assert np.linalg.norm(mapped-expected) < 30.0, (mapped, expected, reg.inliers, reg.good_matches)


def test_capture_monitor_selection_prefers_diablo_window_overlap():
    from whisper_hunter.capture import select_monitor_index
    monitors = [
        {"left": -1920, "top": 0, "width": 3840, "height": 1080},
        {"left": 0, "top": 0, "width": 1920, "height": 1080},
        {"left": -1920, "top": 0, "width": 1920, "height": 1080},
    ]
    assert select_monitor_index(monitors, (-1800, 100, -100, 1000)) == 2
    assert select_monitor_index(monitors, (100, 100, 1800, 1000)) == 1
    assert select_monitor_index(monitors, None) == 1


def test_bundled_map_candidate_precedes_network(monkeypatch, tmp_path: Path):
    from whisper_hunter import assets
    root = tmp_path / 'bundle'
    p = root / 'assets' / assets.MAP_NAME
    p.parent.mkdir(parents=True)
    p.write_bytes(b'x' * 2048)
    monkeypatch.setenv('D4WH_BUNDLE_ROOT', str(root))
    monkeypatch.delenv('D4WH_MAP_PATH', raising=False)
    monkeypatch.setattr(assets, 'verify_map', lambda q: Path(q) == p)
    asset = assets.resolve_map_asset()
    assert asset.source == 'bundled'
    assert asset.path == p

from whisper_hunter.evade import EvadeController


def _executioner_frame(*, center_x: int = 960, tip_y: int = 535, locked: bool = True) -> np.ndarray:
    """Synthetic screen fixture for the overhead Executioner sword + lock circle."""
    img = np.full((1080, 1920, 3), (28, 28, 31), np.uint8)
    blade_top = max(150, tip_y - 220)
    blade = np.array(
        [
            [center_x - 12, blade_top],
            [center_x + 12, blade_top],
            [center_x + 10, tip_y - 30],
            [center_x, tip_y],
            [center_x - 10, tip_y - 30],
        ],
        np.int32,
    )
    cv2.fillConvexPoly(img, blade, (205, 215, 225))
    cv2.rectangle(img, (center_x - 35, tip_y - 50), (center_x + 35, tip_y - 35), (45, 170, 225), -1)
    if locked:
        cv2.circle(img, (960, 540), 58, (32, 72, 238), 9)
    return img


def test_executioner_guard_detects_locked_overhead_sword_as_top_priority():
    cfg = Config(danger_confirm_frames=1, danger_min_confidence=0.50)
    det = DangerDetector(cfg)
    events = det.update(_executioner_frame(), 5000.0)
    assert events
    top = events[0]
    assert top.kind == "executioner", [(e.kind, e.level, e.confidence, e.locked) for e in events]
    assert top.level == DANGER_HIGH
    assert top.locked is True
    assert top.eta_seconds is not None and 0.0 < top.eta_seconds <= cfg.auto_evade_eta_s
    assert top.label == "EXECUTIONER SWORD — EVADE"


def test_executioner_guard_warns_while_tracking_without_wasting_evade():
    cfg = Config(danger_confirm_frames=1, danger_min_confidence=0.50, auto_evade_enabled=True)
    det = DangerDetector(cfg)
    events = det.update(_executioner_frame(tip_y=475, locked=False), 5100.0)
    executioners = [e for e in events if e.kind == "executioner"]
    assert executioners
    sword = executioners[0]
    assert sword.locked is False
    assert sword.eta_seconds is None

    sends: list[int] = []
    evade = EvadeController(cfg, sender=lambda vk: sends.append(vk) or True, foreground_check=lambda: True)
    assert evade.maybe_evade([sword], 5100.0) is None
    assert sends == []


def test_executioner_guard_infers_imminent_downward_drop_when_lock_circle_is_obscured():
    cfg = Config(danger_confirm_frames=1, danger_min_confidence=0.50, danger_immediate_confidence=0.995)
    det = DangerDetector(cfg)
    det.update(_executioner_frame(tip_y=410, locked=False), 5200.0)
    events = det.update(_executioner_frame(tip_y=500, locked=False), 5200.10)
    executioners = [e for e in events if e.kind == "executioner"]
    assert executioners
    sword = executioners[0]
    assert sword.velocity[1] > 70.0
    assert sword.eta_seconds is not None and sword.eta_seconds <= cfg.auto_evade_eta_s
    assert sword.level == DANGER_HIGH


def test_executioner_guard_rejects_vertical_weapon_effect_far_from_player():
    cfg = Config(danger_confirm_frames=1, danger_min_confidence=0.50)
    det = DangerDetector(cfg)
    events = det.update(_executioner_frame(center_x=420, locked=False), 5300.0)
    assert all(e.kind != "executioner" for e in events)


def test_smart_evade_dispatches_one_foreground_space_for_locked_executioner():
    cfg = Config(danger_confirm_frames=1, danger_min_confidence=0.50, auto_evade_enabled=True)
    sword = DangerDetector(cfg).update(_executioner_frame(), 5400.0)[0]
    sends: list[int] = []
    evade = EvadeController(cfg, sender=lambda vk: sends.append(vk) or True, foreground_check=lambda: True)

    fired = evade.maybe_evade([sword], 5400.0)
    assert fired is sword
    assert sends == [0x20]
    # Same threat never causes the old macro's key-spam behavior.
    assert evade.maybe_evade([sword], 5401.0) is None
    assert sends == [0x20]


def test_smart_evade_respects_foreground_and_global_cooldown():
    cfg = Config(auto_evade_enabled=True, auto_evade_cooldown_s=0.72)
    first = DangerEvent(
        91, "executioner", DANGER_HIGH, .98, (960, 430), (940, 300, 40, 230),
        ((940,300),(980,300),(980,530),(940,530)), 5.0, eta_seconds=.35, locked=True,
    )
    second = DangerEvent(
        92, "explosion", DANGER_HIGH, .99, (960, 540), (830,410,260,260),
        ((830,410),(1090,410),(1090,670),(830,670)), 0.0, eta_seconds=0.0,
    )
    sends: list[int] = []
    active = [False]
    evade = EvadeController(cfg, sender=lambda vk: sends.append(vk) or True, foreground_check=lambda: active[0])
    assert evade.maybe_evade([first], 5500.0) is None
    assert sends == []

    active[0] = True
    assert evade.maybe_evade([first], 5500.1) is first
    assert evade.maybe_evade([second], 5500.2) is None
    assert sends == [0x20]
    assert evade.maybe_evade([second], 5500.9) is second
    assert sends == [0x20, 0x20]


def test_smart_evade_keeps_generic_slash_warning_only():
    cfg = Config(auto_evade_enabled=True)
    slash = DangerEvent(
        99, "slash", DANGER_HIGH, .99, (960, 540), (700,520,520,40),
        ((700,520),(1220,520),(1220,560),(700,560)), 0.0, eta_seconds=.2,
    )
    sends: list[int] = []
    evade = EvadeController(cfg, sender=lambda vk: sends.append(vk) or True, foreground_check=lambda: True)
    assert evade.maybe_evade([slash], 5600.0) is None
    assert sends == []


def test_smart_evade_defers_while_ctrl_alt_or_other_modifier_guard_is_active():
    cfg = Config(auto_evade_enabled=True)
    event = DangerEvent(
        101, "executioner", DANGER_HIGH, .99, (960,430), (940,300,40,230),
        ((940,300),(980,300),(980,530),(940,530)), 4.0, eta_seconds=.30, locked=True,
    )
    sends: list[int] = []
    evade = EvadeController(
        cfg,
        sender=lambda vk: sends.append(vk) or True,
        foreground_check=lambda: True,
        input_guard=lambda: False,
    )
    assert evade.maybe_evade([event], 5700.0) is None
    assert sends == []
