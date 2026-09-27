from __future__ import annotations

from dataclasses import dataclass
import hashlib
import os
from pathlib import Path
import shutil
import sys
import urllib.request

from .config import app_dir

# Reused with permission from the MIT-licensed mxtsdev/d4-map-overlay project.
# Git object hash/size are from the upstream repository's map_5_small.jpg blob.
MAP_URL = "https://raw.githubusercontent.com/mxtsdev/d4-map-overlay/main/map_images/map_5_small.jpg"
MAP_GIT_BLOB_SHA1 = "4394f963aff1545d928bcf160809fbd05a5a4bfd"
MAP_SIZE = 4_424_290
MAP_NAME = "map_5_small.jpg"


@dataclass(frozen=True, slots=True)
class MapAsset:
    path: Path
    source: str  # override | cache | bundled | downloaded
    verified: bool


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def canonical_map_path() -> Path:
    override = os.environ.get("D4WH_MAP_PATH")
    if override:
        return Path(override).expanduser().resolve()
    p = app_dir() / "assets" / MAP_NAME
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def bundled_map_path() -> Path | None:
    """Return the read-only map shipped inside the release, if present.

    PyInstaller one-file builds expose bundled data under ``sys._MEIPASS``. Source
    checkouts use ``<repo>/assets``. ``D4WH_BUNDLE_ROOT`` is intentionally supported
    for deterministic regression tests and local portable builds.
    """
    roots: list[Path] = []
    override_root = os.environ.get("D4WH_BUNDLE_ROOT")
    if override_root:
        roots.append(Path(override_root).expanduser())
    mei = getattr(sys, "_MEIPASS", None)
    if mei:
        roots.append(Path(mei))
    roots.append(Path(__file__).resolve().parents[1])
    for root in roots:
        candidate = root / "assets" / MAP_NAME
        if candidate.exists() and candidate.is_file():
            return candidate
    return None


def verify_map(path: Path) -> bool:
    if not path.exists() or path.stat().st_size != MAP_SIZE:
        return False
    try:
        data = path.read_bytes()
    except OSError:
        return False
    return git_blob_sha1(data) == MAP_GIT_BLOB_SHA1


def resolve_map_asset(progress=None) -> MapAsset:
    override = os.environ.get("D4WH_MAP_PATH")
    if override:
        path = Path(override).expanduser().resolve()
        if path.exists() and path.is_file() and path.stat().st_size > 1024:
            return MapAsset(path, "override", False)
        raise RuntimeError(f"D4WH_MAP_PATH is missing or empty: {path}")

    cache = canonical_map_path()
    if verify_map(cache):
        return MapAsset(cache, "cache", True)

    # Release builds are self-contained: prefer the exact upstream asset bundled in
    # the EXE, avoiding a first-run network dependency. Copy it into APPDATA when
    # possible so future source/portable runs can reuse the same verified bytes.
    bundled = bundled_map_path()
    if bundled and verify_map(bundled):
        try:
            cache.parent.mkdir(parents=True, exist_ok=True)
            tmp = cache.with_suffix(".bundled-copy")
            shutil.copyfile(bundled, tmp)
            if verify_map(tmp):
                os.replace(tmp, cache)
                return MapAsset(cache, "bundled", True)
            tmp.unlink(missing_ok=True)
        except OSError:
            pass
        return MapAsset(bundled, "bundled", True)

    # Developer/source fallback only. Official release builds should never need it.
    tmp = cache.with_suffix(".download")
    if progress:
        progress("Bundled map unavailable; downloading permitted Sanctuary anchor (~4.4 MB)...")
    req = urllib.request.Request(MAP_URL, headers={"User-Agent": "D4WhisperHunter/0.4"})
    try:
        with urllib.request.urlopen(req, timeout=30) as response, tmp.open("wb") as f:
            while True:
                block = response.read(1024 * 256)
                if not block:
                    break
                f.write(block)
    except Exception as exc:
        tmp.unlink(missing_ok=True)
        raise RuntimeError(
            "Could not resolve the Sanctuary base map. Use the official self-contained release, "
            f"put {MAP_NAME} in the app assets folder, or set D4WH_MAP_PATH."
        ) from exc

    if not verify_map(tmp):
        tmp.unlink(missing_ok=True)
        raise RuntimeError("Downloaded base map failed the upstream Git blob integrity check.")
    tmp.replace(cache)
    return MapAsset(cache, "downloaded", True)


def ensure_map_asset(progress=None) -> Path:
    return resolve_map_asset(progress).path
