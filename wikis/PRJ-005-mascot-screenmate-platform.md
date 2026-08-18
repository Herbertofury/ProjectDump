# PRJ-005 - Mascot / Screenmate Platform

**Project Constellation ID:** PRJ-005
**Status:** ACTIVE umbrella
**Current verified browser implementation host:** [`Herbertofury/Gamesync`](https://github.com/Herbertofury/Gamesync)
**Verified shipping baseline:** GameSync `0.6.3`
**Observed canonical commit for this documentation pass:** `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`
**Historical Project Constellation next action:** resolve which repository owns the shared mascot core.
**Current resolution:** the shipping browser-side mascot implementation is verified inside GameSync, but a single standalone repository owning the entire browser + desktop umbrella is still not proven.

## Purpose

The Mascot / Screenmate Platform is the umbrella project for GameSync's and related projects' interactive desktop/browser character systems. Its durable Project Constellation mission is broader than one engine: preserve authentic behavior from Shimeji-style packs, classic Microsoft Agent / ACS characters, screenmates, browser mascots, PF Magic Petz-style creatures, voice-capable assistants, page-aware companions, mascot mini-games, and future desktop/Feature Foundry integrations without flattening those systems into a generic sprite player.

Current project-owned source proves a substantial browser implementation in GameSync. That implementation should be treated as the strongest current evidence for browser behavior. The broader umbrella still includes desktop/runtime ownership questions that remain unresolved until a canonical shared-core or desktop repository is identified.

## Relationship map

This umbrella overlaps several separately tracked Project Constellation projects. Keep their identities separate while preserving one coherent mascot architecture.

| Project | Relationship |
| --- | --- |
| [PRJ-006 - ACS Agent Parity Runtime](PRJ-006-acs-agent-parity-runtime.md) | Classic Microsoft Agent / ACS parsing, conversion, compatibility semantics, request/state parity. |
| PRJ-007 - PF Magic Petz Runtime Integration | GameSync/Mascot Petz integration track. Detailed source ownership still needs its own current-source pass. |
| PRJ-008 - Mascot Games / Sports and Golf | Playable mascot-game layer. Keep gameplay modular from the mascot core. |
| [PCX-037 - Shimeji Desktop](PCX-037-shimeji-desktop.md) | Desktop Shimeji runtime track. |
| [PCX-038 - Shimeji Browser Extension](PCX-038-shimeji-browser-extension.md) | Browser Shimeji compatibility and extension integration. |
| [PCX-039 - Webmeji](PCX-039-webmeji.md) | Lightweight web-native Shimeji behavior. |
| [PCX-049 - GameSync Live Mascot Tavern](PCX-049-gamesync-live-mascot-tavern.md) | GameSync host surface for live mascot systems. |
| [PCX-060 - ACS Voice / Speech Runtime](PCX-060-acs-voice-speech-runtime.md) | Speech, voice, listening and classic-agent audio interaction track. |
| PCX-061 - Petz Shared Core | Shared PF Magic-compatible runtime intended to serve multiple hosts. |

## Canonical current browser source

The current shipping browser implementation lives in the GameSync extension repository.

Important verified paths:

- `app/Mascot_Engine.js` - large unified browser mascot runtime and host integration layer.
- `app/content/mascot/` - modular mascot/ACS components, compatibility helpers, host-surface logic, assistant affordances, inspectors, event reactions, talk input, page attachment and binary/animation assets.
- `app/Shimeji Browser Engine/` - bundled browser-engine distribution assets, including background, content-script and popup bundles.
- `app/Voicepacks/` - packaged voice resources.
- `app/assets/mascot/shimejis/` - bundled Shimeji assets exposed by the extension manifest.
- `app/assets/petz/` - Petz-related browser assets exposed by the extension manifest.
- `app/background/background.js` - Manifest V3 service-worker integration point for mascot-related background operations.
- `app/content/shimeji-popup-shim.js` - page-level compatibility bridge injected at `document_start` on all URLs.
- `app/manifest.json` - shipping capabilities, permissions, externally connectable sites and web-accessible mascot resources.

Do not assume a copied/generated mascot bundle elsewhere is newer than these project-owned sources. Resolve source identity against the repository before editing.

## Browser architecture

At the shipping GameSync baseline, the mascot stack can be understood as five cooperating layers.

### 1. Host/integration layer

`app/Mascot_Engine.js` is the primary integration runtime. It owns the GameSync-facing mascot contract, settings, state exchange, pack lifecycle, tab state, event handling and UI behavior.

The runtime guards against duplicate loading with `window.__gsMascotEngineLoaded`, declares a mascot contract version, distinguishes extension UI surfaces such as options/popup/panel pages, and centralizes its message and event vocabulary.

### 2. Engine/compatibility modules

`app/content/mascot/` contains project-owned modular systems rather than relying only on one monolithic animation loop. Verified directory contents include modules such as:

- `acs-ai-bridge.js`
- `acs-assistant-affordances.js`
- `acs-compat-core.js`
- `acs-event-reactions.js`
- `acs-host-surfaces.js`
- `acs-inspector.js`
- `acs-page-attach.js`
- `acs-script-recorder.js`
- `acs-talk-input.js`

The directory also contains binary and JSON animation/runtime assets. The ACS-specific behavior is documented more deeply in [PRJ-006](PRJ-006-acs-agent-parity-runtime.md) and [PCX-060](PCX-060-acs-voice-speech-runtime.md).

### 3. Shimeji compatibility layer

GameSync ships a bundled `Shimeji Browser Engine` distribution and a page shim. The shipping manifest exposes the Shimeji engine's popup, CSS, images/fonts and mascot assets to pages where the integration requires them. It also allows external connection from `https://shimejis.xyz/*` and `https://www.shimejis.xyz/*`.

The mascot runtime normalizes legacy engine identifiers. `clippy` is canonicalized to the ACS engine, while `shimeji-browser` and `shimeji-desktop` are normalized to `shimeji-browser-plus` for unified menu behavior.

### 4. Pack/runtime data layer

The mascot contract contains explicit import/export/list/delete operations for mascot packs and a separate operation to ensure bundled reference Shimejis exist. Pack state is therefore part of the runtime contract, not merely a static asset list.

Runtime asset resolution supports direct URLs and pack-relative asset lookup. The engine maintains active-pack identity and exposes active pack runtime state through its message API.

### 5. GameSync/browser integration layer

The extension manifest exposes mascot JavaScript, binary and JSON resources as web-accessible resources, alongside ClippyJS, voice packs, Shimeji assets and Petz assets. GameSync's MV3 background worker and page integration provide the host boundary around the mascot runtime.

## Verified mascot settings contract

The current `Mascot_Engine.js` defaults establish the supported configuration surface. Important fields include:

- `enabled`
- `quietMode`
- `snoozeUntil`
- `mode` with current default `corner`
- `roamEnabled`
- `interactMode`
- `size`
- `speed`
- `speechFrequency`
- `attentionBudgetPerHour`
- `voiceEnabled`
- `voiceRate`
- `voicePitch`
- `voiceVolume`
- `activePackId`
- `personality`
- `engineOverride`
- `wallThrowMode`
- `webmejiCanvasRenderer`
- `dismissMode`
- `globalCooldownMs`
- `skillCooldownMs`
- `webmejiEnabled`
- `webmejiSpawnCount`
- `sitePolicyMode`
- `sitePolicyList`
- `webmejiJumpChance`
- `webmejiWalkSpeed`
- `webmejiFallSpeed`
- `webmejiJumpSpeed`
- `webmejiGetUpMs`
- `shimejiFixedSeedEnabled`
- `shimejiFixedSeed`
- `shimejiTickMs`
- `shimejiSpawnCap`
- `baselineProfile`
- Webmeji allowances for petting, dragging and each screen edge.

The default Shimeji tick is `40 ms`; the default spawn cap is `12`. A fixed-seed mode exists for deterministic Shimeji behavior and testing.

### Attention and assistant skills

The runtime also defines assistant-oriented skills with per-skill enablement and cooldown concepts. Current built-in skill identifiers include progress narration, completion celebration, ambiguous-match handling, missing-requirement handling, patch-without-target warnings, volatility warnings, notes-found behavior, import/export prompts, quiet-mode prioritization, snooze handling, batch-action help and explainability fallback.

Treat these as behavior policy surfaces. A UI toggle or message handler is not proof that every downstream assistant behavior is fully runtime-qualified.

## Character and compatibility presets

The current browser runtime contains built-in visual/personality presets covering multiple mascot families. Verified preset identities include:

- Clippy / Clippit
- Merlin
- Genie
- Robby
- Dot
- Will
- Genius
- F1
- Links
- Rocky
- Power Pup
- Scribble
- Mother Nature
- Rover
- Earl
- Bonzi-style variants including MaxALERT, PeedyBUDDY and BlobBUDDY
- PF Magic-style Catz
- PF Magic-style Dogz
- Oddballz

These presets prove that the unified host recognizes these character identities. They do not by themselves prove complete behavioral parity with every original source engine.

## Runtime message API

`Mascot_Engine.js` defines the current browser-side message vocabulary. Important operations include:

### State and inspection

- `MASCOT_GET_STATE`
- `MASCOT_GET_TIMELINE`
- `MASCOT_GET_MEMORY`
- `MASCOT_GET_ACTIVE_PACK_RUNTIME`
- `MASCOT_GET_TAB_STATE`
- `GET_TAB_ID`

### Settings and mode

- `MASCOT_SET_SETTINGS`
- `SET_MODE`
- `MASCOT_SETTINGS_SYNC`
- `SET_MASCOT`
- `SET_INTERACT_MODE`
- `SNOOZE`

### Pack lifecycle

- `MASCOT_IMPORT_PACK`
- `MASCOT_EXPORT_PACK`
- `MASCOT_LIST_PACKS`
- `MASCOT_ENSURE_BUNDLED_REFERENCE_SHIMEJIS`
- `MASCOT_DELETE_PACK`
- `MASCOT_CLEAR_CACHED_PACKS`

### Memory, timeline and diagnostics

- `MASCOT_CLEAR_MEMORY`
- `MASCOT_APPEND_MEMORY`
- `MASCOT_LOG_TIMELINE`
- `MASCOT_DEBUG_FIRE`
- `MASCOT_CLEAR_DISMISSED`
- `MASCOT_SAVE_TAB_STATE`

### Host navigation

- `OPEN_EXTENSION_UI`
- `OPEN_SETTINGS`

When extending the mascot subsystem, preserve message compatibility unless an intentional versioned migration is implemented. A renamed message can break popup/panel/background/content coordination even when the local module still appears functional.

## Manifest and browser integration

The current GameSync `0.6.3` manifest is Manifest V3 and declares:

- background service worker `background/background.js` as an ES module;
- `storage`, `tabs`, `scripting`, `alarms`, `offscreen`, `notifications`, `contextMenus`, `nativeMessaging` and related browser permissions used by the broader host;
- a global `content/shimeji-popup-shim.js` injection at `document_start`;
- external connectivity for `shimejis.xyz` and `www.shimejis.xyz`;
- web-accessible `content/mascot/*.js`, `*.bin` and `*.json` resources;
- `third_party/clippyjs/**`;
- `Voicepacks/**`;
- `assets/mascot/shimejis/**`;
- `assets/petz/**`;
- selected bundled `Shimeji Browser Engine` assets.

Changes to mascot file locations must therefore be reflected in the manifest and verified from a production build, not only from source imports.

## Install and run the current browser host

### Prerequisites

- [Node.js](https://nodejs.org/) with npm.
- A Chromium-compatible browser for normal extension development. GameSync's established target includes [Opera GX](https://www.opera.com/gx).
- A clone of [`Herbertofury/Gamesync`](https://github.com/Herbertofury/Gamesync).

### Install dependencies

From the GameSync repository root:

```powershell
npm ci
```

### Development server

```powershell
npm run dev
```

### Production build

```powershell
npm run build
```

GameSync's project contract treats `app/` as canonical editable source and `dist/` as generated production output. After source changes, rebuild before loading the extension.

### Load the extension

Load the generated `dist/` directory as an unpacked extension in the target Chromium/Opera browser. Do not load `app/` directly as if it were the production package.

## Using the mascot platform

A complete user flow should be validated through the real GameSync UI, but the source contract shows the following core capabilities that should remain reachable through host surfaces:

1. enable/disable the mascot system;
2. choose an active mascot/pack;
3. select or override the mascot engine where supported;
4. configure size, speed, roaming, interaction and speech behavior;
5. configure voice parameters;
6. enable Webmeji behavior and allowances;
7. configure site policy and page interaction boundaries;
8. import/export/list/delete mascot packs;
9. inspect state, timeline and memory;
10. use snooze/quiet behavior without corrupting persisted state;
11. preserve per-tab state where the host uses it.

Do not describe a control as working merely because it is rendered. Each user-facing control must be exercised through its real handler, persisted state and observable mascot behavior before it is claimed as qualified.

## Adding or modifying a mascot engine

When adding engine support:

1. identify whether the engine is a true behavior runtime, a compatibility adapter, a pack format or only a visual preset;
2. keep its native semantics intact rather than translating everything into a generic frame loop;
3. define a stable engine identifier and normalize legacy aliases deliberately;
4. preserve pack asset lookup, runtime state and import/export behavior;
5. connect the engine to the unified host menu only after its lifecycle is functional;
6. expose required resources through `app/manifest.json` when page access is needed;
7. preserve settings compatibility and migrate persisted fields explicitly;
8. test drag, movement, idle/state transitions, speech/audio and page interaction relevant to that engine;
9. test engine switching without losing or corrupting another engine's state;
10. verify a production build and browser restart.

### Shimeji-specific rule

Preserve action/behavior graph semantics, timing, anchors, movement, wall/ceiling interaction and pack compatibility. Do not replace authentic Shimeji behavior with a cosmetic sprite animation substitute.

### ACS-specific rule

Preserve parser/converter/runtime semantics and classic request/state behavior. See [PRJ-006](PRJ-006-acs-agent-parity-runtime.md) for the detailed current evidence and unresolved parity boundaries.

### Petz-specific rule

Do not flatten Petz/Catz/Dogz/Oddballz behavior into an ordinary mascot skin. The umbrella explicitly expects Petz-style creature semantics to remain a distinct engine/core concern.

## Pack development and asset handling

The runtime allows a broad mascot import surface and exposes explicit pack import/export APIs. When working on packs:

- preserve original pack metadata and behavior/state definitions;
- keep asset paths stable or migrate them explicitly;
- isolate duplicate mascot identities rather than merging by display name alone;
- verify imported assets resolve through the active runtime;
- verify export can round-trip the pack without dropping behavior metadata;
- verify cached pack cleanup does not delete source-owned or unrelated user data;
- use deterministic/fixed-seed modes where available for reproducible Shimeji tests.

## Persistence and state

The browser mascot contract includes settings synchronization, memory, timeline, dismissed-state management, per-tab state and pack state. Therefore restart and navigation persistence are part of correctness.

For any stateful mascot change, qualify at least:

1. initial configuration;
2. repeated use;
3. tab navigation/reload;
4. browser/service-worker restart;
5. switching away from and back to the mascot/engine;
6. export/import when the changed state is portable;
7. failure recovery when a pack or asset cannot load.

## Testing and verification

The shipping GameSync `package.json` currently exposes general build/development commands plus Bounty-specific tests and a Wasm legacy-acceleration build. It does **not** expose a dedicated top-level mascot test command. Therefore `npm run build` proves build closure, not mascot behavioral correctness.

### Minimum static/build gate

Run:

```powershell
npm ci
npm run build
```

Then inspect the generated `dist/` manifest/resource closure to confirm mascot assets and modules are present as expected.

### Required real-browser qualification

A meaningful mascot release should exercise:

- extension startup with mascot disabled and enabled;
- active pack selection;
- at least one Shimeji-compatible pack;
- at least one ACS character path;
- Webmeji mode if changed;
- drag and page-bound movement;
- wall/edge behavior relevant to the engine;
- speech/voice path if changed;
- quiet/snooze behavior;
- site policy allow/deny behavior;
- pack import/export/delete;
- memory/timeline operations;
- per-tab behavior;
- engine switching;
- reload and browser restart persistence;
- console/service-worker error review.

### Desktop boundary

The historical umbrella includes a desktop build/runtime direction, but this documentation pass did not identify one current standalone repository that conclusively owns the entire shared browser + desktop mascot core. Do not claim desktop parity merely because the browser host exposes a `shimeji-desktop` compatibility identifier.

## Troubleshooting

### Mascot UI appears but no character is visible

Check:

1. the production `dist/` build is the extension actually loaded;
2. mascot `enabled` state;
3. active pack identity;
4. engine override/normalization;
5. site-policy mode and current hostname;
6. required web-accessible assets in the built manifest;
7. content-page and service-worker console errors.

### Shimeji pack imports but behaves incorrectly

Treat this as a behavior/compatibility issue, not an art issue. Compare action graphs, state mapping, timing, anchors, edge interaction, velocity and required behaviors against the source pack and the Shimeji compatibility runtime.

### ACS character renders but classic commands behave incorrectly

Use the ACS parity wiki. Rendering/conversion success is not equivalent to complete Microsoft Agent request/queue/Commands/recognition parity.

### Voice settings change but no audible output occurs

Verify the active engine actually has a speech/audio provider path and required audio assets. `voiceEnabled` and rate/pitch/volume settings are host configuration; they are not proof that every engine has a fully qualified speech provider.

### Engine switch loses state

Check engine identifiers, persisted pack/settings ownership and tab-state migration. Do not fix this by globally clearing storage unless a scoped migration proves the stored data is invalid.

### Pack assets are missing only after production build

Inspect `app/manifest.json`, Vite copy/build behavior and generated `dist/` resource paths. A source file existing under `app/` does not guarantee it is reachable at runtime.

## Extension points

The current architecture supports several natural extension surfaces:

- new engine adapters;
- new mascot pack formats;
- new bundled character packs;
- Shimeji behavior compatibility work;
- ACS request/command/speech parity work;
- Petz shared-core integration;
- new host surfaces and assistant affordances;
- mascot games;
- page-element attachment/reaction behavior;
- local AI/STT/TTS adapters;
- inspectors and deterministic test harnesses;
- desktop host adapters once canonical ownership is resolved.

Every extension should preserve the separation between engine semantics and host UI. The host can unify controls without erasing the behavioral model that makes each engine distinct.

## Current verified facts versus unresolved items

### Verified from current project-owned source

- GameSync `0.6.3` contains the active browser mascot implementation.
- `Mascot_Engine.js` exposes a unified settings/message/pack/state contract.
- GameSync ships modular ACS compatibility files under `app/content/mascot/`.
- GameSync bundles a Shimeji Browser Engine distribution.
- The manifest exposes mascot, ClippyJS, voice, Shimeji and Petz assets.
- `shimejis.xyz` is an explicitly externally connectable integration source.
- the runtime recognizes multiple Office/Microsoft Agent, Bonzi-style and PF Magic-style preset identities.
- deterministic Shimeji seed/tick/spawn settings exist.
- pack import/export/list/delete and state/timeline/memory operations exist in the browser message contract.
- GameSync's canonical editable browser source is `app/`; production output is generated into `dist/`.

### Not yet proven for the umbrella

- one canonical repository owns the entire shared browser + desktop mascot core;
- full Shimeji Desktop parity from the current browser host;
- complete Microsoft Agent request, Commands, speech-recognition and lip-sync parity;
- complete PF Magic Petz behavioral parity;
- every visible mascot control has been freshly requalified in Opera GX at the observed commit;
- every pack format round-trips without loss;
- desktop restart/persistence behavior across the full umbrella;
- all mascot games are fully playable and parity-qualified.

## Contribution checklist

Before publishing a mascot-related change:

1. confirm the exact source repository/branch/commit;
2. identify the affected engine, pack format and host surfaces;
3. preserve unrelated engine behavior;
4. update manifest/resource closure when required;
5. run the production build;
6. load the generated `dist/` extension;
7. exercise the changed control and observable mascot behavior;
8. test failure feedback rather than swallowing errors;
9. test reload and restart persistence for stateful changes;
10. verify at least one representative pack for each engine affected;
11. inspect page and service-worker consoles;
12. record what was actually exercised versus what remains unverified.

## Documentation maintenance rule

Update this wiki when the shared mascot-core ownership is resolved, GameSync changes its mascot contract, a separate desktop runtime becomes canonical, engine identifiers/settings change, pack formats change, Shimeji/ACS/Petz semantics change, mascot resource paths move, a real mascot test suite is added, or a new runtime qualification materially changes what can be claimed.

Do not replace this umbrella wiki with one of its subproject pages. The umbrella exists to document how the engines, host surfaces and shared state fit together, while the subproject wikis preserve deep engine-specific detail.