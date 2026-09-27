# D4 Whisper Hunter 0.5.0 Executioner Guard

**Ad-free Diablo IV Whisper + DangerSense overlay for Windows, now with Executioner Guard and Smart Evade.** It marks and remembers Whispers, tracks Grim Favor progress, plans a fast route to the next cache, detects the notorious overhead Executioner sword separately from ordinary slashes, and can fire one foreground-only Evade keypress when a lethal sword/drop or configured impact is actually imminent—without reading Diablo IV process memory.

## What it does

- Detects the light-pink / rose / deep-red map markers used for **1 / 3 / 5 Grim Favor** Whispers.
- Registers the live Diablo IV world map with SIFT + RANSAC and converts icon pixels into stable world positions.
- **Learns a persistent visual atlas as you pan**, so it is not permanently limited to the old five-region base map. Overlapping views extend the atlas into Nahantu, Skovos, and later map expansions without a new hard-coded coordinate database.
- Remembers off-screen Whispers instead of forgetting them when you pan or zoom.
- Marks objectives that repeatedly disappear from a visible area as completed/rotated and ages genuinely stale observations.
- Tracks your current Favor total and beam-searches for an efficient route to the next 10-Favor turn-in.
- Projects learned Whisper markers and numbered route steps back onto the live game map at the current pan/zoom.
- Uses a transparent, top-most, **click-through** overlay and asks Windows to exclude that overlay from screen capture, preventing visual feedback loops.
- Saves a one-key diagnostic screenshot/JSON for fast tuning if Blizzard changes map colors or icon art.
- **DangerSense lethal-telegraph warnings** run at a separate fast CV cadence so combat warnings do not slow Whisper/map scanning.
- Recognizes QQT-Evade-style geometry families from rendered pixels: **explosion/circle, sword/slash rectangle, cone/slam, and moving projectile**.
- **Executioner Guard** separately detects the Executioner elite-affix sword that tracks overhead, watches for its player-centered red lock circle, and estimates an imminent downward drop even if the lock circle is hidden by spell VFX.
- Predicts whether a moving slash/projectile is actually converging on the player instead of beeping for every red effect.
- **Smart Evade** uses the useful foreground-only behavior from the MIT `griffeth-barker/Diablo-IV-Evade-Macro`, but is event-driven instead of spamming Space: one evade per qualified threat/cooldown and never `AppActivate`s or steals focus.
- Plays distinct asynchronous Windows warning sounds for **Executioner sword**, **blade/slash**, **incoming projectile**, **explosion**, and **cone/slam** threats.
- Draws high-visibility, capture-safe cyan/white warning geometry plus a top-center urgent banner; no red/orange overlay pixels are used, preventing detector feedback loops even if capture exclusion fails.
- Suppresses DangerSense automatically while the world map is registered, so red Whisper/event icons cannot trigger combat alarms.
- **No ads, no telemetry, no analytics, no account, no subscription, no browser framework.**

## Fast start

### Ready-built EXE

Use `D4WhisperHunter.exe` from the Windows release bundle when available. Open Diablo IV, open the **world map**, then run Whisper Hunter.

### From source

1. Install current Python 3.11–3.14 from the official Python site.
2. Run `install.bat` once.
3. Run `run-venv.bat`.
4. Open Diablo IV's world map and pan/zoom through the areas you want scanned.

The permitted Sanctuary image from `mxtsdev/d4-map-overlay` is now bundled inside the official Windows EXE and integrity-checked, so first-run map registration no longer depends on GitHub/network access. It is only an **anchor**, not the coverage limit. If that anchor is unavailable or does not overlap the current expansion map, open the world map and press **F9 once**: the plugin seeds its local visual atlas from the current view and grows it from overlapping pans.

You can also set `D4WH_MAP_PATH` to any map image you have permission to use. Custom maps are intentionally not forced to match the legacy asset hash.

## Hotkeys

- **F8** — hide/show overlay
- **F9** — force a fresh registration/rescan; with an empty atlas, seeds the currently open map if the old anchor cannot lock
- **Ctrl+Alt+1 / 3 / 5** — manually add that many Grim Favors
- **Ctrl+Alt+Space** — complete the current route step, remove it, and credit its Favor
- **Ctrl+Alt+R** — reset Favor counter after turn-in
- **Ctrl+Alt+Shift+C** — clear tracked Whisper markers only
- **Ctrl+Alt+Shift+A** — reset the visual atlas **and** tracked markers together; use after a major map-art/resolution migration if re-locking becomes impossible
- **Ctrl+Alt+D** — save an annotated diagnostic screenshot + JSON under `%APPDATA%\D4WhisperHunter\debug\`
- **Ctrl+Alt+W** — toggle DangerSense combat warnings on/off
- **Ctrl+Alt+S** — mute/unmute DangerSense warning sounds (visual warnings remain)
- **Ctrl+Alt+E** — toggle Smart Evade on/off immediately
- **Ctrl+Alt+Q** — exit

## Getting a complete current Whisper set

Whisper Hunter never invents objectives it has not seen. To collect the current set, open the world map at a useful zoom and pan through Sanctuary once. Every overlapping map view expands/re-localizes the atlas and adds visible Whisper markers to persistent tracking. After that, previously scanned Whispers remain available to the route planner even when they are off-screen.

This is deliberately different from pretending there is a complete public live-Whisper API when there is not. Current Diablo IV references still describe Whispers as map-visible objectives distinguished primarily by light-pink through deep-red color, with higher-value objectives using deeper red.

## How the expansion-safe atlas works

The original public overlay matched screenshots against one static Sanctuary image. That is useful as an initial anchor but eventually becomes obsolete. Version 0.2 instead stores a bounded set of high-quality SIFT descriptors paired with stable world coordinates:

1. a static anchor can establish the initial coordinate system;
2. a live screenshot localizes into that system;
3. if the view is geographically new, the plugin stores spatially diverse features from it;
4. the next overlapping pan localizes against those learned features, including terrain that never existed in the old image;
5. the learned atlas persists in `%APPDATA%\D4WhisperHunter\visual_atlas.*`.

Fixed menu/UI margins are excluded from atlas learning so the tracker learns the moving map texture instead of screen chrome. Atlas size is bounded and redundant keyframes are retired automatically.

## Classification and false-positive resistance

Detection filters for compact red/pink components rather than huge red regions, so large Helltide/zone fills are rejected. It now also rejects broad Tree-like badges and flat filled red pips/diamonds unless they have the framed/internal-detail geometry expected from Whisper objectives. Favor classification combines absolute marker color with adaptive clustering for HDR/gamma variation. Adaptive clustering is accepted only when the detected shade families are actually separated; it will not force one color family into fake 1/3/5 classes. Low-confidence marks get `?` instead of silently claiming certainty.


## DangerSense + Executioner Guard + Smart Evade

DangerSense runs independently from the world-map scanner. The capture loop can sample combat frames at up to the configured `danger_hz` while SIFT map registration and Whisper extraction keep their lower cadence. This preserves the existing map feature set and responsiveness instead of making every combat frame pay for expensive map CV.

The geometry model is adapted from the public QQT Diablo Evade API vocabulary at commit `14acd83bd3e94d6da27f0c361c9d1cbc3b06e916`: circular spells with explosion delay, rectangular/projectile spells, cone spells, and low/medium/high danger levels. D4 Whisper Hunter does **not** import QQT's loader or game-memory access. It infers warning geometry from the pixels Diablo IV already renders on your screen.

Warning and evade behavior:

- **Executioner sword:** looks in the player-overhead corridor for a long near-vertical steel/gold blade instead of assuming the mechanic is a generic red slash. A compact red player-centered lock circle boosts it to an immediate `EXECUTIONER SWORD — EVADE` event. If the circle is obscured, a sufficiently fast downward sword track gets a screen-space ETA fallback.
- **Tracking vs. committed drop:** seeing the sword overhead warns early but does **not** automatically burn an evade while it may still be following you. Smart Evade waits for the lock cue or an inferred imminent drop.
- **Explosion/circle:** warns when the blast/ring approaches or overlaps the player region; high-danger overlaps can Smart Evade.
- **Sword/slash:** detects ordinary long narrow red/orange attack telegraphs. Generic slash stays warning-only by default so false positives cannot waste your evade charges.
- **Incoming projectile:** temporally tracks moving slash/projectile geometry, estimates velocity/trajectory, and can Smart Evade only when its projected path is imminent.
- **Cone/slam:** detects triangular/conical danger telegraphs near the player. Automatic cone evade is off by default.
- **Foreground-only input:** Smart Evade sends one configured virtual key (Space by default) through Windows `SendInput` only while the foreground title is Diablo IV. It never brings Diablo IV to the foreground and never runs a key-spam timer.
- **Debouncing:** each tracked threat can trigger only once, with a global cooldown between different threats.
- High-confidence immediate threats can bypass normal multi-frame confirmation; ordinary candidates need temporal confirmation to reduce false alarms.
- Native warning audio is generated locally as tiny WAV cues under `%APPDATA%\D4WhisperHunter\sounds\`; no media framework, cloud service, ads, or telemetry are involved.

**Account/ToS note:** Smart Evade generates an input on your behalf. Game rules can treat automated input differently from passive overlays. `Ctrl+Alt+E` disables it instantly, and `auto_evade_enabled` can be set to `false` in `config.json` if you want warning-only behavior.

Default hot-path target is 24 DangerSense samples/sec. On the deterministic 1080p regression fixture, the CV detector runs substantially faster than that budget on the development runner; actual in-game performance still depends on resolution, capture path, and other system load.

## Headless screenshot test / calibration

```powershell
python -m whisper_hunter --input .\my-d4-map.png --output .\annotated.png
```

This prints registration/detection/tracking JSON and writes an annotated image. For the live overlay, **Ctrl+Alt+D** produces the same kind of evidence without leaving the game.

DangerSense can be tested independently:

```powershell
python -m whisper_hunter --danger-input .\combat-frame.png --danger-output .\danger-annotated.png
```

You can pass multiple sequential screenshots after `--danger-input` to exercise motion/trajectory prediction.

## Build a single EXE

Run `build_windows.bat`. It fetches and verifies the permitted upstream map asset at build time, installs build dependencies in an isolated `.venv-build`, compiles the source, runs the regression suite, and only then creates a self-contained `dist\D4WhisperHunter.exe` with PyInstaller.

The repository also contains `.github/workflows/build-windows.yml`, which builds on `windows-latest`, runs the full unit suite, verifies the native Executioner warning sound dispatch, creates deterministic map/combat/Executioner fixtures, and smoke-tests the **packaged EXE itself** through the Whisper, generic DangerSense, bundled-map, and Executioner Guard headless paths before uploading the Windows ZIP.

## Persistent state

Stored under `%APPDATA%\D4WhisperHunter\`:

- `config.json` — scan rate, routing weights, marker aging, etc.
- `whispers.json` — tracked Whisper positions and observed state
- `progress.json` — current Grim Favor progress
- `visual_atlas.npz` + `visual_atlas.json` — learned expansion-safe map features
- `assets\map_5_small.jpg` — optional verified legacy anchor
- `debug\` — only when you explicitly press Ctrl+Alt+D
- `sounds\` — locally generated native warning tones for DangerSense

## Accuracy boundary

The plugin can only discover map icons that are actually rendered in a captured viewport. It therefore remembers scanned areas rather than claiming unseen objectives. It also does not fabricate an exact per-objective expiration timer: a marker is retired from direct visual evidence (repeatedly missing while its area is visible) plus a conservative stale-observation fallback.

## Attribution

See `NOTICE.md` and `THIRD_PARTY_LICENSES/`. Diablo IV is a trademark of Blizzard Entertainment. This is an independent companion overlay and is not affiliated with Blizzard Entertainment.


## 0.5.0 Executioner Guard + Smart Evade

- Dedicated Executioner elite-affix detector: overhead vertical blade + compact red lock-circle fusion, with downward-motion ETA fallback when player VFX obscure the circle.
- Dedicated `executioner.wav` warning cue so the instant-kill sword cannot be confused with a generic slash.
- Event-driven Smart Evade adapted from the useful foreground-only behavior of the MIT `griffeth-barker/Diablo-IV-Evade-Macro`; no 2 ms Space spam and no focus stealing.
- Smart Evade defaults to Executioner, imminent projectiles, and high-danger explosions. Generic slash remains warning-only; cone auto-evade defaults off.
- `Ctrl+Alt+E` toggles Smart Evade immediately and persists the setting.
- New deterministic regressions cover lock detection, pre-lock tracking behavior, lock-circle-obscured downward ETA, off-center decoys, foreground gating, one-shot dispatch/debounce, cooldown, and generic-slash suppression.
- Packaged Windows CI now proves the Executioner detector path and Executioner warning sound dispatch in addition to all previous map/Whisper/DangerSense gates.

## 0.4.0 map reliability fixes

- The official EXE bundles the verified upstream Sanctuary anchor; no first-run map download is required.
- Static registration tries the original donor overlay's proven 0.5x SIFT map path first, normalized back into our existing full-resolution atlas coordinates, then falls back to our prior full-size registrar.
- Capture and overlay placement automatically follow the monitor containing the Diablo IV window, including negative virtual-desktop coordinates on left/top secondary displays.
- Existing persistent atlas, Whisper routing, and DangerSense behavior remain intact.
