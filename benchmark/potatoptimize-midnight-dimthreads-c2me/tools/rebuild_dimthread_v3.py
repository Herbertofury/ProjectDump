#!/usr/bin/env python3
import hashlib
import os
import sys
import zipfile
from pathlib import Path

EXPECTED = {
    "me/srrapero720/dimthread/DimThread.class": "ae64d947f64d0cfe0e7780a9c8431472a8483146d85e71ff90d61a784da99dae",
    "me/srrapero720/dimthread/NoxviolaThreadSwap.class": "e5fa5134270becff61b3d3cf31892f1e48cd4954eed350c07d4a0ee0379c4dd5",
    "me/srrapero720/dimthread/NoxviolaThreadSwap$LockEntry.class": "41c56ce6a5db39e2339ed5e10df8dbccd554fd36d704be3cae81e8c9b2b638f9",
    "META-INF/noxviola-dimthread-async-interop.txt": "5e763b3aa145ac483d1763d8e8885b8641e50f0a5b98b7d82b83c93387e4586a",
}

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("usage: rebuild_dimthread_v3.py <official-1.2.1.jar> <fixture-dir> <output.jar>")
    src = Path(sys.argv[1])
    fixture = Path(sys.argv[2])
    out = Path(sys.argv[3])
    replacements = {
        "me/srrapero720/dimthread/DimThread.class": fixture / "DimThread.class",
        "me/srrapero720/dimthread/NoxviolaThreadSwap.class": fixture / "NoxviolaThreadSwap.class",
        "me/srrapero720/dimthread/NoxviolaThreadSwap$LockEntry.class": fixture / "NoxviolaThreadSwap$LockEntry.class",
        "META-INF/noxviola-dimthread-async-interop.txt": fixture / "noxviola-dimthread-async-interop.txt",
    }
    payload = {}
    mismatches = []
    for name, path in replacements.items():
        data = path.read_bytes()
        got = sha(data)
        if got != EXPECTED[name]:
            mismatches.append(f"fixture hash mismatch for {name}: {got} != {EXPECTED[name]}")
        payload[name] = data
    if mismatches:
        raise SystemExit("\n".join(mismatches))

    with zipfile.ZipFile(src, "r") as zin:
        names = set(zin.namelist())
        for n in names:
            u = n.upper()
            if u.startswith("META-INF/") and u.endswith((".SF", ".RSA", ".DSA", ".EC")):
                raise SystemExit(f"refusing signed upstream jar: {n}")
        if "META-INF/mods.toml" not in names:
            raise SystemExit("upstream DimThread mods.toml missing")
        base_mods = zin.read("META-INF/mods.toml")
        out.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(out, "w") as zout:
            for info in zin.infolist():
                name = info.filename
                data = payload.get(name, zin.read(name))
                zout.writestr(info, data)
            for name in (
                "me/srrapero720/dimthread/NoxviolaThreadSwap.class",
                "me/srrapero720/dimthread/NoxviolaThreadSwap$LockEntry.class",
                "META-INF/noxviola-dimthread-async-interop.txt",
            ):
                if name in names:
                    continue
                zi = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                zi.compress_type = zipfile.ZIP_DEFLATED
                zi.external_attr = 0o100644 << 16
                zout.writestr(zi, payload[name])

    with zipfile.ZipFile(out, "r") as z:
        if z.read("META-INF/mods.toml") != base_mods:
            raise SystemExit("DimThread metadata changed unexpectedly")
        for name, expected in EXPECTED.items():
            got = sha(z.read(name))
            if got != expected:
                raise SystemExit(f"output entry mismatch {name}: {got}")
        if b'modId="dimthread"' not in z.read("META-INF/mods.toml") or b'version="1.2.1"' not in z.read("META-INF/mods.toml"):
            raise SystemExit("DimThread identity/version gate failed")
    print(f"DIMTHREAD_V3_CONTENT_OK output_sha256={sha(out.read_bytes())}")

if __name__ == "__main__":
    main()
