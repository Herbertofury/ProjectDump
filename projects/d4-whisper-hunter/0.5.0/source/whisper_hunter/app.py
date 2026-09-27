from __future__ import annotations

import argparse
import json
import os
import queue
import threading
import time
from pathlib import Path

import cv2
import numpy as np

from .assets import ensure_map_asset, resolve_map_asset, verify_map
from .atlas import FeatureAtlas
from .capture import ScreenCapture
from .config import app_dir, load_config, save_config
from .detection import detect_player_marker, detect_whispers
from .danger import DANGER_MEDIUM, DangerDetector, DangerEvent
from .audio import DangerSoundEngine
from .evade import EvadeController
from .homography import MapRegistrar, Registration
from .hotkeys import Hotkeys
from .overlay import OverlayState, OverlayWindow
from .routing import plan_route
from .tracker import WhisperTracker


def _annotate(image: np.ndarray, candidates, reg: Registration | None, tracker: WhisperTracker) -> np.ndarray:
    out = image.copy()
    for c in candidates:
        x, y, w, h = c.bbox
        color = {1: (201, 188, 247), 3: (114, 88, 216), 5: (47, 23, 157)}.get(c.favor, (114, 88, 216))
        cv2.rectangle(out, (x, y), (x + w, y + h), color, 2)
        cv2.putText(
            out,
            f"{c.favor}F {c.confidence:.2f}",
            (x, max(12, y - 4)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.42,
            color,
            1,
            cv2.LINE_AA,
        )
    cv2.putText(
        out,
        f"tracked={len(tracker.active())} registered={reg is not None}",
        (18, 28),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )
    return out


def scan_image(image: np.ndarray, registrar: MapRegistrar, tracker: WhisperTracker, min_matches: int):
    reg = registrar.register(image, min_matches=min_matches)
    candidates = detect_whispers(image)
    if reg:
        qpts = [c.center for c in candidates]
        mpts = MapRegistrar.query_points_to_map(qpts, reg)
        observations = [((float(p[0]), float(p[1])), c.favor, c.confidence) for p, c in zip(mpts, candidates)]
        tracker.update(observations, reg)
    return reg, candidates


def run_headless_image(path: Path, output: Path | None = None) -> dict:
    cfg = load_config()
    map_path = ensure_map_asset(print)
    canonical = cv2.imread(str(map_path), cv2.IMREAD_COLOR)
    registrar = MapRegistrar(canonical)
    state = app_dir() / "headless-whispers.json"
    state.unlink(missing_ok=True)
    tracker = WhisperTracker(cfg, state)
    image = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if image is None:
        raise SystemExit(f"Could not read image: {path}")
    reg, candidates = scan_image(image, registrar, tracker, cfg.min_feature_matches)
    if output:
        cv2.imwrite(str(output), _annotate(image, candidates, reg, tracker))
    payload = {
        "registered": reg is not None,
        "matches": reg.good_matches if reg else 0,
        "inliers": reg.inliers if reg else 0,
        "candidates": [
            {"x": c.center[0], "y": c.center[1], "favor": c.favor, "confidence": c.confidence}
            for c in candidates
        ],
        "tracked": [
            {"id": x.id, "map_x": x.map_x, "map_y": x.map_y, "favor": x.favor, "confidence": x.confidence}
            for x in tracker.active()
        ],
    }
    print(json.dumps(payload, indent=2))
    return payload


def run_headless_danger(paths: list[Path], output: Path | None = None) -> dict:
    cfg = load_config()
    detector = DangerDetector(cfg)
    events: list[DangerEvent] = []
    image: np.ndarray | None = None
    now = 1000.0
    # Repeat a single still once so the default two-frame confirmation path can be
    # tested deterministically without weakening production confirmation settings.
    seq = paths if len(paths) > 1 else [paths[0], paths[0]]
    for i, path in enumerate(seq):
        image = cv2.imread(str(path), cv2.IMREAD_COLOR)
        if image is None:
            raise SystemExit(f"Could not read danger image: {path}")
        events = detector.update(image, now + i / max(1.0, cfg.danger_hz))
    if image is None:
        raise SystemExit("No danger image supplied")
    if output:
        annotated = image.copy()
        for e in events:
            pts = np.array(e.polygon, np.int32)
            if len(pts) >= 3:
                cv2.polylines(annotated, [pts], True, (255, 255, 255), 3, cv2.LINE_AA)
            x, y, w, h = e.bbox
            cv2.putText(annotated, e.label, (x, max(24, y-8)), cv2.FONT_HERSHEY_SIMPLEX, .55, (255,255,255), 2, cv2.LINE_AA)
        cv2.imwrite(str(output), annotated)
    payload = {
        "danger_events": [
            {
                "id": e.id,
                "kind": e.kind,
                "level": e.level,
                "confidence": e.confidence,
                "center": list(e.center),
                "eta_seconds": e.eta_seconds,
                "urgent": e.urgent,
                "locked": e.locked,
                "label": e.label,
            }
            for e in events
        ]
    }
    print(json.dumps(payload, indent=2))
    return payload


class LiveApp:
    def __init__(self):
        self.cfg = load_config()

        # The old public map is now only an optional anchor. The persistent visual
        # atlas extends beyond it into Nahantu/Skovos/future regions by chaining
        # overlapping in-game map views, so startup never blocks on a network fetch.
        self.static_registrars: list[tuple[str, MapRegistrar]] = []
        self.anchor_loading = True
        self.anchor_error = ""
        self.anchor_source = ""
        self.anchor_thread = threading.Thread(target=self._prepare_static_anchor, name="whisper-anchor", daemon=True)
        self.atlas = FeatureAtlas()
        self.atlas_lock = threading.RLock()
        self.data_lock = threading.RLock()

        # Follow the monitor that actually contains the Diablo IV window instead
        # of assuming monitor 1. This also places the click-through overlay at the
        # correct virtual-desktop origin for left/top/secondary monitors.
        probe_capture = ScreenCapture(None)
        self.capture_monitor_index = probe_capture.monitor_index
        self.screen_size = probe_capture.size
        self.screen_origin = probe_capture.origin
        probe_capture.close()
        self.tracker = WhisperTracker(self.cfg)
        self.danger_detector = DangerDetector(self.cfg)
        self.danger_sound = DangerSoundEngine(self.cfg)
        self.evade = EvadeController(self.cfg)
        self.q: queue.Queue = queue.Queue(maxsize=2)
        self.stop = threading.Event()
        self.force_scan = threading.Event()
        self.save_debug = threading.Event()
        self.progress_path = app_dir() / "progress.json"
        self.current_favors = 0
        try:
            payload = json.loads(self.progress_path.read_text(encoding="utf-8"))
            self.current_favors = max(0, min(10, int(payload.get("favors", 0))))
        except Exception:
            pass

        self.last_route = None
        self.last_reg: Registration | None = None
        self.last_reg_mode = ""
        self.last_reg_at = 0.0
        self.last_screen: np.ndarray | None = None
        self.last_player_map: tuple[float, float] | None = None
        self.last_debug_path: Path | None = None

        self.hotkeys = Hotkeys()
        mod = Hotkeys.MOD_CONTROL | Hotkeys.MOD_ALT
        self.hotkeys.register("toggle", 0x77, 0)  # F8
        self.hotkeys.register("rescan", 0x78, 0)  # F9
        self.hotkeys.register("plus1", ord("1"), mod)
        self.hotkeys.register("plus3", ord("3"), mod)
        self.hotkeys.register("plus5", ord("5"), mod)
        self.hotkeys.register("reset", ord("R"), mod)
        self.hotkeys.register("clear", ord("C"), mod | Hotkeys.MOD_SHIFT)
        self.hotkeys.register("reset_atlas", ord("A"), mod | Hotkeys.MOD_SHIFT)
        self.hotkeys.register("debug", ord("D"), mod)
        self.hotkeys.register("danger_toggle", ord("W"), mod)
        self.hotkeys.register("sound_toggle", ord("S"), mod)
        self.hotkeys.register("evade_toggle", ord("E"), mod)
        self.hotkeys.register("complete", 0x20, mod)  # Ctrl+Alt+Space
        self.hotkeys.register("quit", ord("Q"), mod)

        self.window = OverlayWindow(
            *self.screen_size, self.q, opacity=self.cfg.overlay_opacity,
            left=self.screen_origin[0], top=self.screen_origin[1]
        )
        self.thread = threading.Thread(target=self._worker, name="whisper-cv", daemon=True)

    def _prepare_static_anchor(self) -> None:
        try:
            asset = resolve_map_asset()
            canonical = cv2.imread(str(asset.path), cv2.IMREAD_COLOR)
            if canonical is None:
                raise RuntimeError(f"Could not open Sanctuary anchor: {asset.path}")

            # The donor overlay's proven path downsizes map_5_small.jpg to 0.5x
            # before SIFT. Keep that path first, but normalize its homography back
            # to our canonical full-resolution world coordinates. Our previous
            # full-size registrar remains as a zero-loss fallback.
            half = cv2.resize(canonical, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            registrars: list[tuple[str, MapRegistrar]] = [
                ("static-upstream-0.5x", MapRegistrar(half, world_scale=2.0)),
                ("static-full", MapRegistrar(canonical)),
            ]
            self.static_registrars = registrars
            self.anchor_source = asset.source
        except Exception as exc:
            self.anchor_error = f"{type(exc).__name__}: {exc}"
        finally:
            self.anchor_loading = False

    def _publish(self, state: OverlayState) -> None:
        try:
            while True:
                self.q.get_nowait()
        except queue.Empty:
            pass
        try:
            self.q.put_nowait(state)
        except queue.Full:
            pass

    def _save_progress(self) -> None:
        try:
            self.progress_path.write_text(json.dumps({"favors": self.current_favors}, indent=2), encoding="utf-8")
        except Exception:
            pass

    def _reset_atlas_and_tracks(self) -> None:
        # Tracker coordinates live in atlas world-space. Clearing one without the
        # other would leave apparently valid markers in an incompatible space.
        with self.atlas_lock:
            self.atlas.clear()
        with self.data_lock:
            self.tracker.clear()
            self.last_route = None
            self.last_player_map = None
            self.last_reg = None
            self.last_reg_mode = ""
        self.force_scan.set()

    def _hotkey_pump(self) -> None:
        for action in self.hotkeys.poll():
            if action == "toggle":
                self.window.toggle()
            elif action == "rescan":
                self.force_scan.set()
            elif action in {"plus1", "plus3", "plus5"}:
                add = {"plus1": 1, "plus3": 3, "plus5": 5}[action]
                with self.data_lock:
                    self.current_favors = min(10, self.current_favors + add)
                    self._save_progress()
            elif action == "reset":
                with self.data_lock:
                    self.current_favors = 0
                    self._save_progress()
            elif action == "complete":
                with self.data_lock:
                    if self.last_route and self.last_route.items:
                        item = self.last_route.items[0]
                        if self.tracker.mark_gone(item.id):
                            self.current_favors = min(10, self.current_favors + item.favor)
                            self._save_progress()
                            self.force_scan.set()
            elif action == "clear":
                with self.data_lock:
                    self.tracker.clear()
                    self.last_route = None
                self.force_scan.set()
            elif action == "reset_atlas":
                self._reset_atlas_and_tracks()
            elif action == "debug":
                self.save_debug.set()
                self.force_scan.set()
            elif action == "danger_toggle":
                self.cfg.danger_enabled = not self.cfg.danger_enabled
                self.danger_detector.clear()
                save_config(self.cfg)
            elif action == "sound_toggle":
                self.cfg.danger_sound_enabled = not self.cfg.danger_sound_enabled
                self.danger_sound.set_enabled(self.cfg.danger_sound_enabled)
                save_config(self.cfg)
            elif action == "evade_toggle":
                self.cfg.auto_evade_enabled = not self.cfg.auto_evade_enabled
                self.evade.set_enabled(self.cfg.auto_evade_enabled)
                save_config(self.cfg)
            elif action == "quit":
                self.stop.set()
                try:
                    self.window.root.destroy()
                except Exception:
                    pass
                return
        if not self.stop.is_set():
            self.window.root.after(35, self._hotkey_pump)

    def _register_frame(self, image: np.ndarray, *, forced: bool) -> tuple[Registration | None, str]:
        """Resolve the current map view into a persistent world coordinate space."""
        reg: Registration | None = None
        mode = ""

        # Learned atlas first: once seeded, this is the fastest route and it also
        # supports regions absent from the legacy static anchor.
        with self.atlas_lock:
            if self.atlas.ready:
                reg = self.atlas.localize(image, self.cfg.min_feature_matches)
                if reg is not None:
                    mode = "atlas"
                    self.atlas.add_keyframe(image, reg.query_to_map, source=self.atlas.world_source)

        # Static anchor is used only in the same coordinate lineage. Never mix it
        # into a free-seeded atlas, which would corrupt every stored track.
        if reg is None and self.static_registrars:
            with self.atlas_lock:
                can_use_static = self.atlas.world_source != "free"
            if can_use_static:
                for static_mode, registrar in self.static_registrars:
                    static_reg = registrar.register(image, self.cfg.min_feature_matches)
                    if static_reg is None:
                        continue
                    reg = static_reg
                    mode = static_mode
                    with self.atlas_lock:
                        self.atlas.add_keyframe(
                            image,
                            reg.query_to_map,
                            source="static",
                            force=not self.atlas.ready,
                        )
                    break

        # If there is no usable static anchor, one intentional F9 press while the
        # D4 world map is visible seeds an expansion-safe coordinate system from
        # the user's own pixels. Overlapping pans then grow it automatically.
        if reg is None and forced:
            with self.atlas_lock:
                if not self.atlas.ready:
                    seeded = self.atlas.seed_free(image)
                    if seeded is not None:
                        reg = seeded
                        mode = "free-seed"

        return reg, mode

    def _status_for(self, reg: Registration | None, mode: str, seen: int = 0) -> str:
        with self.atlas_lock:
            atlas_ready = self.atlas.ready
            atlas_count = self.atlas.keyframe_count
        if reg is not None:
            anchor = f" · anchor {self.anchor_source}" if self.anchor_source and mode.startswith('static') else ""
            return f"{mode or 'map'} lock{anchor} · {seen} Whispers this view · atlas {atlas_count} · pan to learn more"
        if atlas_ready:
            return f"Map searching · atlas {atlas_count} · pan back through a learned overlap · F9 retry"
        if self.anchor_loading:
            return "Preparing base anchor in background · open world map · F9 can seed this view now"
        if self.anchor_error:
            return "Base anchor unavailable · open world map and press F9 once to seed local atlas"
        return "Open the D4 world map · press F9 once if automatic lock does not start"

    def _save_debug_capture(self, image: np.ndarray, candidates, reg: Registration | None, mode: str, hazards: list[DangerEvent] | None = None) -> None:
        folder = app_dir() / "debug"
        folder.mkdir(parents=True, exist_ok=True)
        stamp = time.strftime("%Y%m%d-%H%M%S")
        png = folder / f"whisper-scan-{stamp}.png"
        meta = folder / f"whisper-scan-{stamp}.json"
        with self.data_lock:
            annotated = _annotate(image, candidates, reg, self.tracker)
            tracks = [
                {
                    "id": x.id,
                    "map_x": x.map_x,
                    "map_y": x.map_y,
                    "favor": x.favor,
                    "confidence": x.confidence,
                    "state": x.state,
                }
                for x in self.tracker.items
            ]
        cv2.imwrite(str(png), annotated)
        with self.atlas_lock:
            atlas_info = {
                "world_source": self.atlas.world_source,
                "keyframes": self.atlas.keyframe_count,
            }
        payload = {
            "created_at": time.time(),
            "registration_mode": mode,
            "registered": reg is not None,
            "matches": reg.good_matches if reg else 0,
            "inliers": reg.inliers if reg else 0,
            "atlas": atlas_info,
            "candidates": [
                {
                    "center": list(c.center),
                    "favor": c.favor,
                    "confidence": c.confidence,
                    "bbox": list(c.bbox),
                    "saturation": c.saturation,
                    "value": c.value,
                    "redness": c.redness,
                    "shape_score": c.shape_score,
                    "holes": c.holes,
                    "edge_density": c.edge_density,
                }
                for c in candidates
            ],
            "tracks": tracks,
            "danger_events": [
                {
                    "id": e.id,
                    "kind": e.kind,
                    "level": e.level,
                    "confidence": e.confidence,
                    "center": list(e.center),
                    "bbox": list(e.bbox),
                    "polygon": [list(p) for p in e.polygon],
                    "distance_to_player": e.distance_to_player,
                    "eta_seconds": e.eta_seconds,
                    "locked": e.locked,
                    "velocity": list(e.velocity),
                    "age_frames": e.age_frames,
                }
                for e in (hazards or [])
            ],
        }
        meta.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        self.last_debug_path = png

    def _worker(self) -> None:
        capture: ScreenCapture | None = None
        try:
            capture = ScreenCapture(self.capture_monitor_index)
            # Capture at DangerSense speed while keeping expensive map/Whisper CV at
            # its existing cadence. This adds reaction speed without slowing or
            # reducing the map feature set.
            capture_hz = max(float(self.cfg.danger_hz), float(self.cfg.scan_hz), 8.0)
            capture_interval = 1.0 / capture_hz
            map_scan_interval = 1.0 / max(0.5, self.cfg.scan_hz)
            reg_interval = 1.0 / max(0.25, self.cfg.register_hz)
            last_map_scan_at = 0.0
            last_candidates = []

            while not self.stop.is_set():
                t0 = time.time()
                try:
                    image = capture.grab()
                    self.last_screen = image
                    now = time.time()
                    forced = self.force_scan.is_set()
                    need_reg = forced or self.last_reg is None or now - self.last_reg_at >= reg_interval
                    if need_reg:
                        self.last_reg, self.last_reg_mode = self._register_frame(image, forced=forced)
                        self.last_reg_at = now
                        self.force_scan.clear()

                    reg = self.last_reg
                    mode = self.last_reg_mode
                    screen_points = []
                    route_points = []
                    matches = inliers = 0
                    candidates = last_candidates if reg else []

                    # World-map frames contain red Whisper/event icons, so DangerSense
                    # is suppressed whenever the map registrar is locked.
                    hazards: list[DangerEvent] = self.danger_detector.update(
                        image, now, suppress=(reg is not None)
                    )
                    if self.cfg.danger_sound_enabled:
                        for event in hazards:
                            if event.level >= DANGER_MEDIUM:
                                if self.danger_sound.alert(event, now):
                                    break
                    evaded = self.evade.maybe_evade(hazards, now) if hazards else None
                    if evaded is not None:
                        danger_alert = f"AUTO EVADE · {evaded.label}"
                    else:
                        danger_alert = hazards[0].label if hazards else ""

                    if reg:
                        matches, inliers = reg.good_matches, reg.inliers
                        if forced or now - last_map_scan_at >= map_scan_interval:
                            candidates = detect_whispers(image)
                            last_candidates = candidates
                            last_map_scan_at = now
                            map_pts = MapRegistrar.query_points_to_map([c.center for c in candidates], reg)
                            obs = [
                                ((float(p[0]), float(p[1])), c.favor, c.confidence)
                                for p, c in zip(map_pts, candidates)
                            ]
                            with self.data_lock:
                                self.tracker.update(obs, reg, now)

                            player = detect_player_marker(image)
                            if player:
                                pmap = MapRegistrar.query_points_to_map([player.center], reg)
                                if len(pmap):
                                    self.last_player_map = (float(pmap[0, 0]), float(pmap[0, 1]))

                        with self.data_lock:
                            active_visible = self.tracker.visible_items()
                            active_all = self.tracker.active()
                            favors = self.current_favors
                        qpts = MapRegistrar.map_points_to_query([x.point for x in active_visible], reg)
                        screen_points = [(item, float(p[0]), float(p[1])) for item, p in zip(active_visible, qpts)]

                        start = self.last_player_map
                        if start is None:
                            center_q = [(image.shape[1] / 2.0, image.shape[0] / 2.0)]
                            center_m = MapRegistrar.query_points_to_map(center_q, reg)
                            if len(center_m):
                                start = (float(center_m[0, 0]), float(center_m[0, 1]))
                        route = plan_route(active_all, start, favors, self.cfg)
                        with self.data_lock:
                            self.last_route = route
                        route_q = MapRegistrar.map_points_to_query([x.point for x in route.items], reg)
                        route_points = [(item, float(p[0]), float(p[1])) for item, p in zip(route.items, route_q)]
                    else:
                        last_candidates = []
                        with self.data_lock:
                            route = plan_route(self.tracker.active(), self.last_player_map, self.current_favors, self.cfg)
                            self.last_route = route
                            favors = self.current_favors
                            active_all = self.tracker.active()

                    if self.save_debug.is_set():
                        self.save_debug.clear()
                        self._save_debug_capture(image, candidates, reg, mode, hazards)

                    with self.atlas_lock:
                        atlas_keyframes = self.atlas.keyframe_count
                        atlas_source = self.atlas.world_source
                    state = OverlayState(
                        screen_points=screen_points,
                        route_points=route_points,
                        route=route,
                        current_favors=favors,
                        tracked_total=len(active_all),
                        registered=reg is not None,
                        matches=matches,
                        inliers=inliers,
                        status=self._status_for(reg, mode, len(candidates)),
                        scan_age=max(0.0, time.time() - self.last_reg_at),
                        atlas_keyframes=atlas_keyframes,
                        map_mode=mode or atlas_source,
                        hazards=hazards if self.cfg.danger_overlay_enabled else [],
                        danger_enabled=self.cfg.danger_enabled,
                        danger_sound_enabled=self.cfg.danger_sound_enabled,
                        auto_evade_enabled=self.cfg.auto_evade_enabled,
                        danger_alert=danger_alert,
                    )
                    self._publish(state)
                except Exception as exc:
                    with self.data_lock:
                        route = plan_route(self.tracker.active(), self.last_player_map, self.current_favors, self.cfg)
                        favors = self.current_favors
                        tracked = len(self.tracker.active())
                    with self.atlas_lock:
                        atlas_keyframes = self.atlas.keyframe_count
                    self._publish(
                        OverlayState(
                            screen_points=[],
                            route_points=[],
                            route=route,
                            current_favors=favors,
                            tracked_total=tracked,
                            registered=False,
                            matches=0,
                            inliers=0,
                            status=f"Scan error: {type(exc).__name__}: {exc}",
                            scan_age=0.0,
                            atlas_keyframes=atlas_keyframes,
                            map_mode="error",
                            hazards=[],
                            danger_enabled=self.cfg.danger_enabled,
                            danger_sound_enabled=self.cfg.danger_sound_enabled,
                            auto_evade_enabled=self.cfg.auto_evade_enabled,
                        )
                    )
                delay = capture_interval - (time.time() - t0)
                if delay > 0:
                    self.stop.wait(delay)
        finally:
            if capture is not None:
                capture.close()

    def run(self) -> None:
        self.anchor_thread.start()
        self.thread.start()
        self.window.root.after(50, self._hotkey_pump)
        try:
            self.window.run()
        finally:
            self.stop.set()
            self.hotkeys.close()
            self.thread.join(timeout=2.0)


def main(argv=None):
    p = argparse.ArgumentParser(description="Ad-free Diablo IV Whisper Hunter overlay")
    p.add_argument("--input", type=Path, help="Headless: scan one D4 map screenshot")
    p.add_argument("--output", type=Path, help="Headless: save annotated map screenshot")
    p.add_argument("--danger-input", type=Path, nargs="+", help="Headless: scan one or more combat screenshots for lethal telegraphs")
    p.add_argument("--danger-output", type=Path, help="Headless: save annotated danger screenshot")
    p.add_argument("--asset-check", action="store_true", help="Verify the self-contained Sanctuary anchor and exit")
    args = p.parse_args(argv)
    if args.asset_check:
        asset = resolve_map_asset(print)
        payload = {"path": str(asset.path), "source": asset.source, "verified": bool(asset.verified or verify_map(asset.path))}
        print(json.dumps(payload, indent=2))
        return 0
    if args.danger_input:
        run_headless_danger(args.danger_input, args.danger_output)
        return 0
    if args.input:
        run_headless_image(args.input, args.output)
        return 0
    if os.name != "nt":
        raise SystemExit("Live overlay mode requires Windows. Use --input for headless fixture/image testing.")
    LiveApp().run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
