# D4 Whisper Hunter 0.4.0 — Map Reliability Checkpoint

Status: **VERIFIED WINDOWS BUILD**
Date: 2026-09-26 America/Denver / 2026-09-27 UTC

## Canonical lineage

- Repository: `Herbertofury/ProjectDump`
- Branch: `build/d4-whisper-hunter-0.4.0-map-reliability`
- Validated source/workflow head: `9de1cf8f51a6d81c505251b0d1fdd8428ecdaebc`
- Post-validation cleanup head before this checkpoint: `6ac32fe4266552f1642949065d1f0443e1968ab9`
- Final Windows Actions run: `36286025912`
- Final Windows job: `108526851859`
- Final Actions artifact: `10920582762`
- Donor map project: `mxtsdev/d4-map-overlay`
- Donor map Git blob SHA-1: `4394f963aff1545d928bcf160809fbd05a5a4bfd`

## User-visible repair

0.4.0 keeps the full 0.3.0 Whisper Hunter + DangerSense feature set and fixes the map reliability problems that could make the shipped app appear nonfunctional on a real PC:

1. **Self-contained map anchor** — the permitted `map_5_small.jpg` donor asset is fetched and integrity-verified at build time and bundled inside the one-file Windows EXE. First-run map registration no longer depends on GitHub/network access.
2. **Proven donor registration path** — static registration tries the original donor overlay's proven 0.5x SIFT map path first, while normalizing coordinates back to our existing full-resolution world/atlas coordinate lineage. Our previous full-size registrar remains as a fallback.
3. **Correct monitor targeting** — capture automatically selects the physical monitor overlapping the visible Diablo IV window instead of blindly assuming monitor 1.
4. **Correct virtual-desktop overlay placement** — the click-through overlay uses the selected monitor's real left/top origin, including negative coordinates for monitors positioned left/above the primary display.
5. **No regression to our improvements** — learned expansion-safe atlas, persistent Whisper tracking, 1/3/5 Favor classification, routing, timers, DangerSense visual warnings, sword/slash/projectile/explosion/cone detection, and sound cues remain intact.
6. **Still ad-free** — no ads, telemetry, analytics, account, or subscription path was added.

## Frozen source identity

- Complete 0.4.0 source ZIP: `D4WhisperHunter-0.4.0-source.zip`
- Source ZIP size: `60,274` bytes
- Source ZIP SHA-256: `83aa1b379ac3bf11391ae70a8ad2b15e675b10632f68e71c3dbd295ab97e1cec`
- Canonical 0.3 -> 0.4 upgrade patch SHA-256: `05ca0cfd6af084b5a4f20bdbb0a1575b367dd691e9fe83002923b1f611d8907e`
- Canonical 0.3 base TAR.XZ SHA-256: `5bbf54473aaf35b2eb645eb37ac298b1c73000c85fd6e6dd070df36e0560c32d`

The GitHub build reconstructs the exact verified 0.3 base, decodes the exact 0.4 patch, verifies both hashes, and requires `git apply --check` before building.

## Windows proof — run 36286025912

The following gates passed in one Windows run:

1. canonical 0.3 source reconstruction and SHA gate — PASS
2. canonical 0.4 patch decode, SHA gate, and apply — PASS
3. Python 3.14 + production/build dependencies — PASS
4. complete 0.4 regression suite — PASS (17 tests in the frozen source suite)
5. donor `map_5_small.jpg` build-time fetch + exact integrity check — PASS
6. Windows DangerSense sound dispatch preservation — PASS (`slash.wav`, `explosion.wav`)
7. one-file Windows EXE build with donor map bundled — PASS
8. **packaged EXE bundled-map proof with `D4WH_MAP_PATH` removed and isolated empty APPDATA** — PASS
   - `source = bundled`
   - `verified = true`
9. packaged Whisper smoke — PASS
   - map registration true
   - 1 / 3 / 5 Favor detections
   - tracked Whispers = 3
10. packaged DangerSense smoke — PASS
    - kind `explosion`
    - level `3`
    - confidence `0.99`
    - ETA `0.0`
    - urgent `true`
    - label `EXPLOSION — MOVE`
11. verified Windows release assembly — PASS
12. GitHub Actions artifact upload — PASS

## Final Windows artifact identity

GitHub Actions wrapper:
- size: `73,492,700` bytes
- SHA-256: `f591d9d5c65b6077026a5fb5377c34edd2e571329c1f4693aefad71e6ddf421c`

Direct runnable release ZIP inside the Actions wrapper:
- file: `D4WhisperHunter-0.4.0-Windows-x64.zip`
- size: `73,470,514` bytes
- SHA-256: `bf2df84630d0979ab541e8bd49eb76a835a6a0a8347e631520acab512abf3e47`

Windows executable:
- file: `D4WhisperHunter.exe`
- size: `73,889,974` bytes
- SHA-256: `3863c640c37c8fed31412c5b0d13777ae272dc3b395e07591a2f1e5bfeeb56c2`

Embedded runtime receipts:
- `PACKAGED-BUNDLED-MAP-CHECK.json` SHA-256 `26c1d0cdc9df433a67536b71f618bd643853236366eb1e653e52ecd46f3743a9`
- `PACKAGED-WHISPER-SMOKE.json` SHA-256 `a9c929901e613605205d9aa60a034bd9433c1602d8689b432debe0c23c0ae60a`
- `PACKAGED-DANGERSENSE-SMOKE.json` SHA-256 `76b6b9021b7e0d31d818c2212f9fa48c32f0f6d5815a4875d5bb94a8d9d82ed0`

## Google Drive persistence

Project folder: `1KLWpnaoH2dCWWdLXvzkzgnoxFAzuMdCD`

Source:
- Drive ID: `1Yt2vtXj35V8xECl13z5TayVcyXZv7usm`
- name: `D4WhisperHunter-0.4.0-source.zip`
- remote size: `60,274` bytes
- full round-trip SHA-256: `83aa1b379ac3bf11391ae70a8ad2b15e675b10632f68e71c3dbd295ab97e1cec`

Verified Windows Actions artifact:
- Drive ID: `1o8Wqto5983JnjrTxuL2unUc5MZMyXBZS`
- name: `D4WhisperHunter-0.4.0-Windows-x64-verified-actions.zip`
- remote size: `73,492,700` bytes
- full round-trip SHA-256: `f591d9d5c65b6077026a5fb5377c34edd2e571329c1f4693aefad71e6ddf421c`
- contains the direct runnable Windows ZIP plus its checksum

## Recovered incidents — do not repeat

### 1. Release relied on first-run map download
Signature: packaged app can launch but map registration may never become useful when GitHub/network fetch fails or is blocked.
Cause: donor map asset was not part of the PyInstaller one-file payload.
Recovery: fetch + integrity-check the permitted donor map during build; package it with PyInstaller `--add-data`; prefer the bundled verified map before any network fallback.
Regression protection: packaged `--asset-check` runs with no `D4WH_MAP_PATH` and isolated empty APPDATA and must report `source=bundled`, `verified=true`.

### 2. Hardcoded monitor 1 / origin 0,0
Signature: no useful detection/overlay when Diablo IV is on another monitor or monitor coordinates are negative.
Cause: capture and overlay assumed primary/monitor-1 geometry.
Recovery: enumerate visible windows, find Diablo IV, select the physical monitor with maximum overlap, capture that monitor, and position the overlay at its real virtual-desktop origin.
Regression protection: monitor-overlap tests include a left-side monitor with negative X coordinates.

### 3. Donor's proven 0.5x SIFT path was not preserved
Signature: synthetic registration passes but current real-world map matching can be less robust than the donor overlay that inspired it.
Cause: only our full-resolution static registrar was used.
Recovery: keep donor-compatible 0.5x registration first and normalize its homography to our full-resolution coordinate lineage; retain full-size registrar and learned atlas as fallbacks.
Regression protection: scaled registrar test proves mapped coordinates stay in the full world-coordinate space.

### 4. 0.4 patch initially targeted a convenience 0.3 ZIP rather than canonical GitHub 0.3 bytes
Signature: hash gate passes for the patch payload, but `git apply --check` rejects every touched file against the canonical base.
Cause: two legitimate 0.3 packaging snapshots differed.
Recovery: export the canonical GitHub base once, regenerate the delta from those exact bytes, verify a fresh local apply and byte-for-byte comparison, then encode the patch as base64 chunks and pin the decoded patch SHA.
Regression protection: CI now verifies canonical base SHA + decoded patch SHA + `git apply --check` before dependency install or build.

## Product invariants

- no ads
- no telemetry/analytics
- no account/subscription
- no Diablo IV process-memory hooks
- no QQT loader dependency
- existing Whisper/map functionality preserved and hardened
- learned expansion-safe atlas preserved
- DangerSense preserved
- upstream donor attribution/license preserved

## Evidence boundary / next action

The actual 0.4.0 packaged Windows executable was exercised on Windows CI through the repaired map-asset resolution path, Whisper path, and DangerSense path. A live Diablo IV client session is not available in this execution environment, so arbitrary live-current-game map rendering has not been independently replayed. If a live capture still fails to register, use the existing diagnostic capture path as the next reproducer; do not remove or weaken any 0.4 safeguards or features.
