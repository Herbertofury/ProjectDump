# D4 Whisper Hunter 0.5.0 — Executioner Guard + Smart Evade

Status: **VERIFIED WINDOWS BUILD**

## Canonical state

- Branch: `build/d4-whisper-hunter-0.5.0-executioner-guard`
- Verified source publication commit: `d0df180278ff1acc3cca262943093a2a6a5c233b`
- One-time bootstrap removed at: `6071cbd144f79ace0fefd752ff075fe4ae59b296`
- Windows run: `36291087485`
- Windows job: `108541188360`
- Actions artifact: `10922038664`

## What changed

0.5.0 preserves all 0.4.0 map reliability, persistent atlas, Whisper 1/3/5 Favor tracking/routing, and generic DangerSense behavior, and adds:

- dedicated `executioner` detection for the elite-affix sword that tracks overhead and drops on the player;
- player-centered overhead ROI detection for vertical steel/white or warm/gold sword geometry;
- red/orange lock-circle recognition plus downward-motion/ETA fallback when VFX obscure the lock cue;
- explicit `EXECUTIONER SWORD — READY` and `EXECUTIONER SWORD — EVADE` states;
- dedicated `executioner.wav` warning;
- event-driven Smart Evade with `Ctrl+Alt+E` enable/disable;
- one configured Win32 `SendInput` evade per qualified threat/cooldown;
- foreground-only gating and modifier-key guard;
- locked/imminent Executioner, high imminent explosion, and high imminent projectile auto-evade eligibility;
- generic slash remains warning-only so Evade charges are not wasted.

## GitHub dodge donor

Smart Evade adapts the useful foreground-only input behavior from:

- `griffeth-barker/Diablo-IV-Evade-Macro`
- reference commit `0fc150f92c4f4189c907ad3f9c987d2b5f8cf9b5`
- source path `src/sendSpace.ps1`
- MIT license included verbatim in `THIRD_PARTY_LICENSES/griffeth-barker-diablo-iv-evade-macro-MIT.txt`

The donor's 2 ms Space-spam loop, GUI, external icon fetch, `AppActivate`, and focus stealing are intentionally not retained.

QQT Diablo remains geometry/concept-only. No QQT loader or process-memory dependency was introduced.

## Performance

The first Executioner implementation was rejected at about 18.6 ms/frame versus ~6 ms/frame for 0.4. The promoted implementation reuses the existing resized HSV/red mask and restricts new CV to the player-overhead ROI.

Representative local 1080p fixture:
- 0.4: ~5.9–6.2 ms/frame
- 0.5: ~6.46 ms/frame (~155 detector FPS)
- existing combat capture budget: 24 Hz / 41.67 ms

## Verification — Windows run 36291087485

Passed:
- exact 0.5 source ZIP SHA gate;
- compile + complete 25-test suite;
- Smart Evade one-shot request exactly `[32]` (Space);
- foreground-negative test produced no request;
- donor map integrity;
- `executioner.wav` Windows dispatch;
- one-file EXE build;
- packaged bundled-map check: `source=bundled`, `verified=true`;
- packaged Whisper smoke: map registered, Favor 1/3/5, tracked=3;
- packaged generic DangerSense smoke: urgent level-3 explosion;
- packaged Executioner smoke:
  - kind `executioner`
  - level `3`
  - confidence `0.995`
  - ETA `0.42`
  - urgent `true`
  - locked `true`
  - label `EXECUTIONER SWORD — EVADE`;
- clean 36-file source snapshot committed to this branch;
- Windows release ZIP assembled and uploaded.

## Artifact identities

Source ZIP:
- `D4WhisperHunter-0.5.0-source.zip`
- 66,758 bytes
- SHA-256 `1bd3403b77b2c5f437514c28da1620cc84e534afab7af02065ab77faf7fb0655`

Actions wrapper:
- 73,508,249 bytes
- SHA-256 `1f9726a198e33438cc8a337b3bc4fdcb2707c83c82a67ce61295ccd4c98f3c5b`

Runnable Windows ZIP:
- `D4WhisperHunter-0.5.0-Windows-x64.zip`
- 73,486,178 bytes
- SHA-256 `8ba18dac05f33f603011f397e76fea9e7b86a981cb24e05724f6b82dacdbb215`

EXE:
- 73,902,286 bytes
- SHA-256 `1f83399ee34aba4df121b4c39e86356bd0ce47dcd712b20a9608aa760f3e4df5`

## Google Drive

- Source ID: `1ALKnzeWl249L9sobExiBB7bAVYAa7I6X` — round-trip hash matches source SHA above.
- Runnable build ID: `1cJiAJhzlzflN-9OrDbjRNL8MM42CIf8N` — round-trip hash matches runnable ZIP SHA above.
- Full checkpoint ID: `1zGg7JuwY3cMy4sm16Erg8NNYd88lzY2v` — 9,946 bytes, SHA-256 `ea56f1803f68f595fd6419e479b6c244f91af26861c88512d4994de2961d3e9c`.

## Invariants

- no ads;
- no telemetry/analytics;
- no account/subscription;
- no Diablo IV process-memory hooks;
- no QQT loader;
- no focus stealing;
- no timed Space spam;
- all 0.4 map/Whisper/DangerSense functionality preserved.

## Evidence boundary

The packaged Windows EXE was exercised through map, Whisper, generic DangerSense, and Executioner detection fixtures. Smart Evade's production decision/gating pipeline was exercised on Windows with an injected sender. There is no live Diablo IV client in CI, so no claim is made that a real Space key was injected into a live game or that every future/current Executioner animation will be avoided perfectly. Use a live missed/late-warning capture as the next regression fixture if needed.
