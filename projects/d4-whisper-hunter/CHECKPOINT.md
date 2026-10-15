# D4 Whisper Hunter — Verified 0.2.1 Checkpoint

Status: **Windows packaged-runtime verified**
Date: 2026-09-26

## Canonical build lineage

- Branch: `build/d4-whisper-hunter-0.2.1`
- Build commit: `9a8027fa497fdb4375a6a113032dc518517f76af`
- GitHub Actions run: `36214159654`
- GitHub Actions artifact: `10896448624`
- Workflow conclusion: **success**
- Windows runner: `windows-latest`
- Python: 3.14

## Verification

The Windows workflow:
1. reconstructed the frozen source from the four committed payload parts;
2. verified the tar.xz SHA-256 before extraction;
3. installed the production/build dependencies;
4. passed the full 9-test regression suite;
5. built a one-file `D4WhisperHunter.exe`;
6. launched the packaged EXE in headless mode;
7. registered the deterministic map fixture;
8. detected 1-, 3-, and 5-Favor Whisper fixtures;
9. tracked all three objectives;
10. produced the annotated output;
11. assembled and uploaded the Windows release bundle.

## Hashes

- Frozen source TAR.XZ: `250e86dc962322e71d29efed7a6cbed1ae0b5049b71e7b50462066bbfc55e3a6`
- Source ZIP: `600f977d10e95377e21aead8dbdd292cd128c920de2ee8d7dd135234befcacda`
- GitHub Actions artifact ZIP: `73c7412181d0c753884f33b72a80e7fadd0aa427b6ba353662a8f0d096166bc0`
- Final Windows release ZIP: `fbfed3e8c31cb9f57b2264a1ebf4c205dafad6e01d7f54375bf9a37b95b8617e`
- Final EXE: `1cd5ccf22c8cc63cfc43aa82f1fcc878fe058db4e968dc9c3c8a6549303736c8`

## Google Drive persistence

Folder ID: `1KLWpnaoH2dCWWdLXvzkzgnoxFAzuMdCD`

- Source ZIP ID: `1CmNSuQP856kbor7T1kLsKouM5kR0jsXT`
  - remote byte size verified: 42,374
  - round-trip SHA-256 verified: `600f977d10e95377e21aead8dbdd292cd128c920de2ee8d7dd135234befcacda`
- Verified Windows Actions artifact ID: `1gEkWoaj14OXEyRBDrCQBjb0F6HhZZ89M`
  - remote byte size verified: 69,072,686
  - round-trip SHA-256 verified: `73c7412181d0c753884f33b72a80e7fadd0aa427b6ba353662a8f0d096166bc0`

## Product invariants

- no ads
- no telemetry/analytics
- no account/subscription
- screen-reading only; no Diablo IV process-memory hook
- persistent Whisper tracking across map pans
- Grim Favor progress + route planning
- expansion-safe learned visual atlas
- conservative handling of unseen objectives: never invent Whispers not observed on the rendered map
- preserved upstream MIT attribution for `mxtsdev/d4-map-overlay`

## Exact next action

Use the verified Windows release bundle. Real live-game tuning, if Blizzard's current map art/HDR differs from the synthetic regression fixture, should be driven from Ctrl+Alt+D diagnostic captures without weakening the detector's false-positive gates.
