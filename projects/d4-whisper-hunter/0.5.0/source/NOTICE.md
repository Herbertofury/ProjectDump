# Third-party attribution

D4 Whisper Hunter uses the map-registration concept and permitted legacy Sanctuary base-map asset from:

- `mxtsdev/d4-map-overlay` — https://github.com/mxtsdev/d4-map-overlay
- Original project license: MIT
- Base map asset: `map_images/map_5_small.jpg`
- Upstream Git blob: `4394f963aff1545d928bcf160809fbd05a5a4bfd`
- Exact upstream license text: `THIRD_PARTY_LICENSES/mxtsdev-d4-map-overlay-MIT.txt`

The default anchor is downloaded directly from that repository and verified against the upstream Git blob hash. It is only used as an optional registration anchor; D4 Whisper Hunter's local visual atlas grows from the user's own rendered world-map pixels and is not limited to the old image's geographic coverage.

DangerSense uses the geometry vocabulary documented by the public QQT Diablo Evade API:

- `qqtnn/qqt_diablo` — https://github.com/qqtnn/qqt_diablo
- Evade API path: `scripts/#api/evade.lua`
- Reference commit: `14acd83bd3e94d6da27f0c361c9d1cbc3b06e916` (2026-05-18)
- Concepts adapted: circular/explosion, rectangular/projectile, cone, and low/medium/high danger-level modeling.

D4 Whisper Hunter does not copy the QQT loader, does not invoke QQT process-memory APIs, and does not require that loader at runtime. The user provided authorization to integrate the relevant warning/evade concepts for this project; the implementation here remains screen-reading computer vision.

Smart Evade adapts the useful foreground-window input behavior from:

- `griffeth-barker/Diablo-IV-Evade-Macro` — https://github.com/griffeth-barker/Diablo-IV-Evade-Macro
- Original project license: MIT
- Reference commit: `0fc150f92c4f4189c907ad3f9c987d2b5f8cf9b5` (2025-07-13)
- Source reference: `src/sendSpace.ps1`
- Exact upstream license text: `THIRD_PARTY_LICENSES/griffeth-barker-diablo-iv-evade-macro-MIT.txt`

D4 Whisper Hunter does not retain the archived macro's 2 ms key-spam timer, external icon download, GUI, or `AppActivate` focus-stealing behavior. The production implementation is a native Python/Win32 event-driven dispatcher: only a qualified DangerSense event can request one configured Evade keypress, and foreground-only mode verifies Diablo IV is already active before input is sent.

D4 Whisper Hunter contains no advertising SDK, analytics SDK, telemetry client, account service, or subscription system.

Diablo IV is a trademark of Blizzard Entertainment. This project is an independent companion overlay and is not affiliated with Blizzard Entertainment.
