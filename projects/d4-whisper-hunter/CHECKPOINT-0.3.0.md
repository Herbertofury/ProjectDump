# D4 Whisper Hunter 0.3.0 — DangerSense Verified Checkpoint

Status: **Windows build + packaged Whisper/DangerSense + Windows sound dispatch verified**
Date: 2026-09-26

## Canonical lineage

- Repository: `Herbertofury/ProjectDump`
- Branch: `build/d4-whisper-hunter-0.3.0-dangersense`
- Final validation head: `c8e761fe23f4cf55678f2bd3498e17703be98dff`
- Final GitHub Actions run: `36218522937`
- Final job: `108339222941`
- Final artifact: `10898029631`
- Workflow conclusion: **success**
- Windows runner: `windows-latest`
- Python: 3.14
- Danger geometry reference: `qqtnn/qqt_diablo` commit `14acd83bd3e94d6da27f0c361c9d1cbc3b06e916`

## Product behavior added

DangerSense is integrated into the existing ad-free D4 Whisper Hunter without removing or reducing Whisper/map behavior.

- passive rendered-screen detection only; no Diablo IV process-memory hook or QQT loader dependency
- circles / explosions
- sword and slash rectangles
- fast moving incoming slash/projectile prediction
- cone / slam geometry
- low / medium / high danger levels
- ETA/urgency scoring
- persistent visual danger overlay and urgent top-center warning
- separate fast DangerSense cadence from slower map/Whisper CV
- map-mode suppression to prevent Whisper/map-red false alarms
- temporal confirmation and cooldown/debounce
- distinct local Windows WAV cues for slash, projectile, explosion, cone and fallback danger
- Ctrl+Alt+W DangerSense toggle
- Ctrl+Alt+S sound mute toggle
- no ads, telemetry, account or subscription

## Frozen source identity

- Source ZIP SHA-256: `4476344215c9c912a319a7b7db21b5e797d130184b3071d980c805cc02d74463`
- Source ZIP size: `53,105` bytes
- Source TAR.XZ SHA-256: `5bbf54473aaf35b2eb645eb37ac298b1c73000c85fd6e6dd070df36e0560c32d`
- Four GitHub payload chunks were blob-verified against the frozen local source.

## Final Windows proof

Final run `36218522937` passed all gates in one run:

1. exact source reconstruction and SHA-256 gate
2. dependency install
3. full regression suite — 14 tests
4. Windows DangerSense sound cue generation + dispatch gate
   - all five WAV cues created and validated as mono 16-bit 22,050 Hz PCM
   - slash danger dispatched `slash.wav`
   - explosion danger dispatched `explosion.wav`
5. one-file Windows EXE build
6. packaged Whisper smoke
   - map registration true
   - 1 / 3 / 5 Favor detections
   - 3 persistent tracked Whispers
7. packaged DangerSense smoke
   - event kind: `explosion`
   - danger level: `3`
   - confidence: `0.99`
   - ETA: `0.0`
   - urgent: `true`
   - label: `EXPLOSION — MOVE`
8. release ZIP assembly
9. GitHub Actions artifact upload

Sound gate log evidence:
`DangerSense sound cue generation + Windows dispatch wiring PASS: [('slash.wav', 131075), ('explosion.wav', 131075)]`

## Final artifact hashes

- GitHub Actions artifact ZIP: `3e38ef7742b6463f038d794b091764b15941ad958fc341bb5c30d00c8ceef9b0`
- Runnable Windows release ZIP: `c695400567c96c24b286e5d1023f5d3b505aef586859d807e3f5c4955617db02`
- Runnable Windows release ZIP size: `69,139,874` bytes
- `D4WhisperHunter.exe` SHA-256: `13464d66aa8926c7ba31a45b9d1e9af2e46bc94e5d93ae9123b6f404f213ca60`
- `D4WhisperHunter.exe` size: `69,560,283` bytes

## Google Drive persistence

Project folder: `1KLWpnaoH2dCWWdLXvzkzgnoxFAzuMdCD`

Source:
- Drive ID: `1557Hv8W4ucZPOMlmI0i99_EplhN5MRSs`
- name: `D4WhisperHunter-0.3.0-DangerSense-source.zip`
- remote size: `53,105` bytes
- full re-download SHA-256: `4476344215c9c912a319a7b7db21b5e797d130184b3071d980c805cc02d74463`

Runnable Windows release:
- Drive ID: `144cr-pscE2cijf4062E_P1zF_qcha_Zf`
- name: `D4WhisperHunter-0.3.0-DangerSense-Windows-x64.zip`
- remote size: `69,139,874` bytes
- full re-download SHA-256: `c695400567c96c24b286e5d1023f5d3b505aef586859d807e3f5c4955617db02`

## Recovered CI incidents — do not repeat

### Incident: source extraction root mismatch

Signature: exact source SHA gate passed, then `Source extraction failed`.

Cause: the 0.3.0 tar stores project files at archive root while the first workflow assumed a nested `D4WhisperHunter/` directory.

Failed path: `buildsrc/D4WhisperHunter/pyproject.toml`

Verified recovery:
- require `buildsrc/pyproject.toml`
- use `working-directory: buildsrc`

Regression protection: final workflow run reconstructs and builds successfully from the flat archive layout.

### Incident: artifact upload used stale nested path

Signature: product build + both packaged smoke tests passed, then `actions/upload-artifact` reported no files.

Cause: upload paths still referenced the obsolete nested extraction directory.

Failed paths:
- `buildsrc/D4WhisperHunter/D4WhisperHunter-0.3.0-DangerSense-Windows-x64.zip`
- matching SHA file path

Verified recovery:
- upload from `buildsrc/D4WhisperHunter-0.3.0-DangerSense-Windows-x64.zip`
- upload matching `.sha256` from the same root

Regression protection: final run uploaded artifact ID `10898029631` successfully.

## Evidence boundary

The actual Windows executable and warning/audio code paths are verified using deterministic packaged-runtime fixtures on GitHub's Windows runner. This environment does not provide a live Diablo IV client session, so arbitrary current in-game combat encounters have not been independently replayed here. Live screenshots/captures can be used for further tuning without weakening the conservative false-positive gates.
