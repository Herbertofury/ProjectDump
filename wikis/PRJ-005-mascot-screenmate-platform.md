# PRJ-005 - Mascot / Screenmate Platform

**Project Constellation ID:** PRJ-005
**Status:** ACTIVE umbrella
**Verified shipping browser host:** [`Herbertofury/Gamesync`](https://github.com/Herbertofury/Gamesync) `0.6.3`
**Verified next-generation browser host:** [`Herbertofury/GameSync-Next`](https://github.com/Herbertofury/GameSync-Next) Extension V2 `0.8.0`
**GameSync Next current head observed:** `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`
**Universal mascot parity implementation commit:** `60940e8479af518f3373a79efa091902f4843842`
**Standalone desktop-core ownership:** unresolved in connected user-owned GitHub
**Historical Project Constellation next action:** resolve which repository owns the shared mascot core.
**Current resolution:** the umbrella now has two verified browser implementation hosts and separately tracked desktop compatibility/architecture benchmarks, but one user-owned repository that canonically owns the complete browser + desktop mascot core is still not proven.

## Purpose

The Mascot / Screenmate Platform is the umbrella project for GameSync's and related projects' interactive desktop/browser character systems. Its durable Project Constellation mission is broader than one engine: preserve authentic behavior from Shimeji-style packs, classic Microsoft Agent / ACS characters, screenmates, browser mascots, PF Magic Petz-style creatures, voice-capable assistants, page-aware companions, mascot mini-games, and future desktop/Feature Foundry integrations without flattening those systems into a generic sprite player.

Current project-owned evidence now proves two substantial browser implementations:

1. GameSync `0.6.3`, which remains the verified shipping JavaScript host and contains the broadest legacy unified mascot contract.
2. GameSync Next Extension V2 `0.8.0`, which has a typed WXT/React implementation and has verified universal all-site mascot parity on arbitrary pages through its Opera verification path.

Neither result proves that a single standalone repository owns the full browser + desktop umbrella. The separately tracked desktop project therefore remains the authority for desktop compatibility research and future desktop-source resolution.

## Relationship map

This umbrella overlaps several separately tracked Project Constellation projects. Keep their identities separate while preserving one coherent mascot architecture.

| Project | Relationship |
| --- | --- |
| [PRJ-006 - ACS Agent Parity Runtime](PRJ-006-acs-agent-parity-runtime.md) | Classic Microsoft Agent / ACS parsing, conversion, compatibility semantics, request/state parity. |
| [PRJ-007 - PF Magic Petz Runtime Integration](PRJ-007-pf-magic-petz-runtime-integration.md) | Typed Petz core and GameSync integration track. Preserve Petz-specific behavior and persistence semantics. |
| PRJ-008 - Mascot Games / Sports and Golf | Playable mascot-game layer. Keep gameplay modular from the mascot core. |
| [PCX-037 - Shimeji Desktop](PCX-037-shimeji-desktop.md) | Desktop Shimeji runtime track, including current Java compatibility and Rust/Flutter architecture benchmarks. |
| [PCX-038 - Shimeji Browser Extension](PCX-038-shimeji-browser-extension.md) | Browser Shimeji compatibility, GameSync Next universal page mascot parity, and extension integration. |
| [PCX-039 - Webmeji](PCX-039-webmeji.md) | Lightweight web-native Shimeji behavior. |
| [PCX-049 - GameSync Live Mascot Tavern](PCX-049-gamesync-live-mascot-tavern.md) | GameSync host surface for live mascot systems. |
| [PCX-060 - ACS Voice / Speech Runtime](PCX-060-acs-voice-speech-runtime.md) | Speech, voice, listening and classic-agent audio interaction track. |
| PCX-061 - Petz Shared Core | Shared PF Magic-compatible runtime intended to serve multiple hosts. |

## Source authority model

The umbrella should not be reduced to one repository simply because one host currently has more code. Use this source hierarchy instead.

### Shipping browser authority

[`Herbertofury/Gamesync`](https://github.com/Herbertofury/Gamesync) `0.6.3` remains the strongest verified shipping browser baseline. Its legacy JavaScript runtime contains the large unified mascot contract, broad settings surface, pack lifecycle, ACS/Shimeji/Webmeji/Petz assets, voice resources, message APIs, and existing user-facing behavior.

### Next-generation browser authority

[`Herbertofury/GameSync-Next`](https://github.com/Herbertofury/GameSync-Next) Extension V2 `0.8.0` is the strongest verified typed next-generation browser implementation. Its universal mascot parity work was introduced in commit `60940e8479af518f3373a79efa091902f4843842`, while the current repository head inspected for this pass is `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`.

The later `cd906...` head merged the verified Universal Game Tracker, Bounty, and Animation Tracker recovery into `main`; it did not replace the mascot implementation origin. Direct inspection at `cd906...` still shows the all-site `page-mascot.content.ts` entrypoint matching `*://*/*`, the shared settings/site-policy flow, SPA route resynchronization, and lightweight/full-runtime ownership handoff introduced by the mascot parity work. Treat `cd906...` as the current repository authority and `60940e...` as the source lineage for the universal mascot implementation.

The current parity implementation is source-backed by:

- `apps/extension-v2/src/entrypoints/page-mascot.content.ts`
- `apps/extension-v2/src/content/universalPageMascot.ts`
- `apps/extension-v2/src/content/features/pageMascot.ts`
- `apps/extension-v2/src/content/runtimeCoordination.ts`
- `apps/extension-v2/src/ui/lib/surfaceMascot.ts`
- `apps/extension-v2/src/content/mascot/sharedCommands.ts`
- `apps/extension-v2/src/background/bootstrap.ts`
- `apps/extension-v2/wxt.config.ts`
- `scripts/verify-extension-v2-opera.js`

The GameSync Next parity audit marks `universal-page-mascot-shim` as **verified**, with its implementation and Opera verification files recorded directly in the audit evidence.

### Desktop authority boundary

A user-owned standalone desktop mascot repository is still unresolved. [PCX-037 - Shimeji Desktop](PCX-037-shimeji-desktop.md) currently tracks compatibility and architecture benchmarks rather than pretending an upstream public repository is the user's canonical source. Its present comparison set includes the Java-compatible DalekCraft2 Shimeji Desktop line and the newer NeurolingsCE Rust + Flutter architecture benchmark.

Do not infer desktop parity from browser identifiers such as `shimeji-desktop`. Resolve the user's actual desktop source before transplanting or replacing implementation.

## Canonical shipping browser source

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

## Shipping GameSync browser architecture

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

## GameSync Next universal mascot architecture

GameSync Next adds a distinct lightweight all-site runtime rather than requiring the full store/site integration runtime on every page.

### Universal WXT entrypoint

`src/entrypoints/page-mascot.content.ts` is a WXT content entrypoint with:

```text
matches: *://*/*
runAt: document_idle
```

It lazy-loads `src/content/universalPageMascot.ts` and initializes the universal mascot runtime on arbitrary HTTP(S) pages.

This is materially different from the earlier GameSync Next state in which the full content runtime was limited to explicit supported-site detection. The mascot no longer requires a detected GameSync game page merely to mount.

### Shared settings and site policy

`universalPageMascot.ts` resolves settings through the background `getSettings` message and falls back to `chrome.storage.sync`. It listens for both runtime `SETTINGS_CHANGED` messages and `chrome.storage.onChanged` updates.

`src/content/features/pageMascot.ts` now gates mounting on:

1. settings being ready;
2. mascot enabled state;
3. `gameSyncSitePolicyAllowsUrl(...)` for the current URL.

It no longer requires a detected game object. This is the key source-level reason universal arbitrary-page mascot behavior is possible.

### SPA route continuity

`src/content/runtimeCoordination.ts` installs one shared History API route observer for `pushState` and `replaceState`, emitting `gamesync:runtime-route-change`. The universal mascot also listens for `popstate` and `hashchange`.

This means a mascot surface can survive and resynchronize across single-page-app navigation without relying only on a full page reload.

### Lightweight-versus-full runtime ownership

The universal runtime deliberately avoids double-owning a page. GameSync Next uses a shared full-runtime marker/event. When the full content runtime activates, the lightweight mascot runtime disposes its surface rather than leaving two competing mascot hosts mounted.

This ownership handoff is important for performance and correctness. Do not create another global content script that bypasses this coordination.

### Surface mounting and failure reporting

The universal runtime dynamically imports `src/ui/lib/surfaceMascot.ts` and `src/content/mascot/sharedCommands.ts` only when needed. `mountSurfaceMascot(...)` marks its host with `data-gs-surface-mascot`, cleans the host if agent initialization fails, and returns one controller responsible for disposal.

A failed page mount is recorded through the mascot timeline using the `surface-mount-error` event with the current URL and failure message. Mount failure is therefore observable rather than silently swallowed.

### Clippy compatibility initialization repair

The same `60940e...` parity commit corrected Clippy-compatible agent initialization ordering. Queue construction and `_setupEvents()` are now performed only after the prototype methods required by those operations have been installed. This prevents early construction from calling incomplete instance behavior.

That repair matters to the umbrella because ACS/Clippy-style agents are one of the shared mascot families, not a separate decorative feature.

## GameSync Next manifest and resource closure

`apps/extension-v2/wxt.config.ts` declares Extension V2 `0.8.0`, Manifest V3, and the next-generation resource boundary.

Verified mascot-related facts include:

- `https://*/*` host permission and the universal content entrypoint;
- externally connectable `shimejis.xyz` and `www.shimejis.xyz` origins;
- web-accessible `content/mascot/*.js` resources;
- `third_party/clippyjs/**`;
- `Voicepacks/**`;
- `assets/mascot/shimejis/**`;
- selected `Shimeji Browser Engine` assets;
- popup, full, options and panel surfaces;
- both Opera `sidebar_action` and Chromium `side_panel` surfaces;
- the `open-command-center` and `toggle-overlay` commands.

The manifest therefore proves that mascot parity in Extension V2 is part of the packaged extension contract, not only an unreferenced source module.

## Verified mascot settings contract

The current shipping `Mascot_Engine.js` defaults establish the broadest verified configuration surface. Important fields include:

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

GameSync Next uses the typed shared `GameSyncSettings` contract and `mergeGameSyncSettings(...)` rather than inventing a separate universal-page mascot settings store. When evolving settings, maintain deliberate migration/parity between the shipping and next-generation hosts.

### Attention and assistant skills

The shipping runtime also defines assistant-oriented skills with per-skill enablement and cooldown concepts. Current built-in skill identifiers include progress narration, completion celebration, ambiguous-match handling, missing-requirement handling, patch-without-target warnings, volatility warnings, notes-found behavior, import/export prompts, quiet-mode prioritization, snooze handling, batch-action help and explainability fallback.

Treat these as behavior policy surfaces. A UI toggle or message handler is not proof that every downstream assistant behavior is fully runtime-qualified.

## Character and compatibility presets

The shipping browser runtime contains built-in visual/personality presets covering multiple mascot families. Verified preset identities include:

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

## Shipping GameSync runtime message API

`Mascot_Engine.js` defines the current shipping browser-side message vocabulary. Important operations include:

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

## Shipping GameSync manifest and browser integration

The GameSync `0.6.3` manifest is Manifest V3 and declares:

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

## Install and run the shipping GameSync host

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

## Install, build, and verify GameSync Next Extension V2

### Prerequisites

- [Node.js](https://nodejs.org/) with npm.
- [`Herbertofury/GameSync-Next`](https://github.com/Herbertofury/GameSync-Next).
- A Chromium-family browser for normal WXT development.
- [Opera GX](https://www.opera.com/gx) for the maintained isolated parity verification path.

### Install

From the GameSync Next repository root:

```powershell
npm ci
```

### Build Extension V2

```powershell
npm --workspace apps/extension-v2 run build
```

The Extension V2 package also exposes:

```powershell
npm --workspace apps/extension-v2 run dev
npm --workspace apps/extension-v2 run zip
npm --workspace apps/extension-v2 run verify:opera
npm --workspace apps/extension-v2 run verify:same-id-upgrade
npm --workspace apps/extension-v2 run verify:offscreen-runtime
```

The workspace-level Opera path is:

```powershell
npm run verify:extension-v2:opera
```

### What the Opera verifier proves for the universal mascot

The parity audit records that the isolated Opera verifier:

- loads the lightweight mascot on an unrelated local HTTP page;
- keeps one live host through a single-page-app route change;
- restores settings after the smoke path;
- verifies the full overlay runtime was not loaded merely to show the mascot.

This is stronger evidence than only seeing source files or a successful WXT build.

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
11. preserve per-tab state where the host uses it;
12. in GameSync Next, keep the lightweight all-site mascot synchronized with shared settings and SPA route changes without unnecessarily loading the full site runtime.

Do not describe a control as working merely because it is rendered. Each user-facing control must be exercised through its real handler, persisted state and observable mascot behavior before it is claimed as qualified.

## Adding or modifying a mascot engine

When adding engine support:

1. identify whether the engine is a true behavior runtime, a compatibility adapter, a pack format or only a visual preset;
2. keep its native semantics intact rather than translating everything into a generic frame loop;
3. define a stable engine identifier and normalize legacy aliases deliberately;
4. preserve pack asset lookup, runtime state and import/export behavior;
5. connect the engine to the unified host menu only after its lifecycle is functional;
6. expose required resources through the host manifest/WXT config when page access is needed;
7. preserve settings compatibility and migrate persisted fields explicitly;
8. test drag, movement, idle/state transitions, speech/audio and page interaction relevant to that engine;
9. test engine switching without losing or corrupting another engine's state;
10. verify a production build and browser restart;
11. where both GameSync and GameSync Next implement the behavior, run a cross-host parity comparison instead of assuming a port is equivalent.

### Shimeji-specific rule

Preserve action/behavior graph semantics, timing, anchors, movement, wall/ceiling interaction and pack compatibility. Do not replace authentic Shimeji behavior with a cosmetic sprite animation substitute.

### ACS-specific rule

Preserve parser/converter/runtime semantics and classic request/state behavior. See [PRJ-006](PRJ-006-acs-agent-parity-runtime.md) for the detailed current evidence and unresolved parity boundaries.

### Petz-specific rule

Do not flatten Petz/Catz/Dogz/Oddballz behavior into an ordinary mascot skin. The umbrella explicitly expects Petz-style creature semantics to remain a distinct engine/core concern. See [PRJ-007](PRJ-007-pf-magic-petz-runtime-integration.md) for the typed shared-core and persistence boundary.

## Pack development and asset handling

The shipping runtime allows a broad mascot import surface and exposes explicit pack import/export APIs. When working on packs:

- preserve original pack metadata and behavior/state definitions;
- keep asset paths stable or migrate them explicitly;
- isolate duplicate mascot identities rather than merging by display name alone;
- verify imported assets resolve through the active runtime;
- verify export can round-trip the pack without dropping behavior metadata;
- verify cached pack cleanup does not delete source-owned or unrelated user data;
- use deterministic/fixed-seed modes where available for reproducible Shimeji tests.

GameSync Next should not silently narrow this contract merely because its lightweight universal-page runtime currently exercises a smaller visible surface. Port pack lifecycle and engine semantics deliberately, with parity evidence.

## Persistence and state

The shipping browser mascot contract includes settings synchronization, memory, timeline, dismissed-state management, per-tab state and pack state. GameSync Next additionally proves storage-change synchronization for its universal mascot surface. Therefore restart and navigation persistence are part of correctness.

For any stateful mascot change, qualify at least:

1. initial configuration;
2. repeated use;
3. tab navigation/reload;
4. SPA route change where applicable;
5. browser/service-worker restart;
6. switching away from and back to the mascot/engine;
7. export/import when the changed state is portable;
8. failure recovery when a pack or asset cannot load;
9. cross-host compatibility if both GameSync and GameSync Next consume the same setting or pack data.

## Testing and verification

The shipping GameSync `package.json` does not expose one top-level all-mascot behavioral test command. Therefore `npm run build` proves build closure, not mascot behavioral correctness.

GameSync Next has a stronger maintained browser verification path for the universal page mascot through `scripts/verify-extension-v2-opera.js`, but this still does not prove every legacy mascot engine and pack capability.

### Minimum shipping build gate

```powershell
npm ci
npm run build
```

Then inspect the generated `dist/` manifest/resource closure to confirm mascot assets and modules are present as expected.

### Minimum GameSync Next build/parity gate

```powershell
npm ci
npm --workspace apps/extension-v2 run build
npm run verify:extension-v2:opera
```

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
- pack import/export/delete when that host exposes them;
- memory/timeline operations;
- per-tab behavior;
- engine switching;
- reload and browser restart persistence;
- SPA navigation for GameSync Next's universal runtime;
- lightweight/full-runtime ownership handoff for GameSync Next;
- console/service-worker error review.

### Cross-host parity matrix

When a feature exists in both browser hosts, qualify it explicitly instead of marking the whole umbrella complete from one host.

| Behavior | GameSync 0.6.3 | GameSync Next 0.8.0 | Required proof |
| --- | --- | --- | --- |
| All-site mascot bootstrap | shipping global shim | verified WXT universal page entrypoint | arbitrary non-game page runtime |
| Settings/site policy | broad unified settings | typed shared settings + URL policy | persisted setting change affects real mascot |
| SPA navigation | host-dependent legacy behavior | shared route observer | one host persists/resyncs without duplicate mount |
| Clippy/ACS surface | legacy unified engine | typed surface mascot compatibility | agent mounts and commands without initialization errors |
| Pack lifecycle | broad import/export/list/delete contract | partial parity must remain evidence-driven | round-trip exact pack metadata/assets |
| Shimeji engine semantics | shipping bundled engine | next-generation integration/asset parity | behavior graph and movement parity |
| Petz semantics | shipping assets/integration | typed Petz core/bridge track | non-destructive state/persistence parity |
| Desktop behavior | not proven by browser host | not proven by browser host | separate desktop runtime source and real desktop tests |

## Desktop boundary and architecture target

The umbrella includes a desktop build/runtime direction, but connected GitHub still does not expose one user-owned repository that conclusively owns the entire shared browser + desktop mascot core.

The separate [PCX-037](PCX-037-shimeji-desktop.md) page currently records two useful external benchmarks:

- DalekCraft2/Shimeji-Desktop for active Java/Shimeji-ee compatibility modernization;
- qingchenyouforcc/NeurolingsCE for a newer Rust engine/runtime + Flutter manager architecture, native transparent-window backends, pack validation, CLI/HTTP/IPC control and deterministic smoke/package workflows.

These are benchmarks, not permission to replace unresolved user-owned desktop source. The umbrella's long-term architecture should seek a shared semantic core only after actual user-owned desktop identity is recovered and differential tests prove compatibility.

## Troubleshooting

### Mascot UI appears but no character is visible

Check:

1. the production build is the extension actually loaded;
2. mascot `enabled` state;
3. active pack identity;
4. engine override/normalization;
5. site-policy mode and current hostname;
6. required web-accessible assets in the built manifest/WXT output;
7. content-page and service-worker console errors.

For GameSync Next, also inspect the mascot timeline for `surface-mount-error` and confirm the lightweight universal runtime has not handed ownership to the full content runtime.

### GameSync Next mascot appears on supported sites but not arbitrary pages

Verify the loaded 0.8.0 build contains the `page-mascot.content` WXT entrypoint with `*://*/*` matching. Confirm settings are ready, the mascot is enabled, and the site policy allows the current URL. Do not reintroduce a detected-game requirement into `pageMascot.ts`.

### GameSync Next mascot duplicates after SPA navigation

Inspect `runtimeCoordination.ts`, the full-runtime marker/event, and the universal runtime's disposal path. There should be one shared History observer and one active mascot host. Do not solve this by disabling SPA synchronization globally.

### Shimeji pack imports but behaves incorrectly

Treat this as a behavior/compatibility issue, not an art issue. Compare action graphs, state mapping, timing, anchors, edge interaction, velocity and required behaviors against the source pack and the Shimeji compatibility runtime.

### ACS character renders but classic commands behave incorrectly

Use the ACS parity wiki. Rendering/conversion success is not equivalent to complete Microsoft Agent request/queue/Commands/recognition parity.

### GameSync Next Clippy-compatible agent fails during initialization

Confirm the loaded source includes the `60940e...` ordering repair: prototype behavior must be installed before creating the agent queue and calling `_setupEvents()`. An older build can fail before the corrected lifecycle is available.

### Voice settings change but no audible output occurs

Verify the active engine actually has a speech/audio provider path and required audio assets. `voiceEnabled` and rate/pitch/volume settings are host configuration; they are not proof that every engine has a fully qualified speech provider. GameSync Next's visible Clippy balloon speech is not by itself proof of audible TTS; see PCX-060.

### Engine switch loses state

Check engine identifiers, persisted pack/settings ownership and tab-state migration. Do not fix this by globally clearing storage unless a scoped migration proves the stored data is invalid.

### Pack assets are missing only after production build

For GameSync inspect `app/manifest.json`, Vite copy/build behavior and generated `dist/` resource paths. For GameSync Next inspect `wxt.config.ts`, Extension V2 asset closure and the generated WXT output. A source file existing in the repository does not guarantee it is reachable at runtime.

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
- GameSync-to-GameSync-Next parity adapters;
- desktop host adapters once canonical ownership is resolved.

Every extension should preserve the separation between engine semantics and host UI. The host can unify controls without erasing the behavioral model that makes each engine distinct.

## Current verified facts versus unresolved items

### Verified from current project-owned source

- GameSync `0.6.3` contains the verified shipping browser mascot implementation.
- `Mascot_Engine.js` exposes a unified settings/message/pack/state contract.
- GameSync ships modular ACS compatibility files under `app/content/mascot/`.
- GameSync bundles a Shimeji Browser Engine distribution.
- the shipping manifest exposes mascot, ClippyJS, voice, Shimeji and Petz assets.
- `shimejis.xyz` is an explicitly externally connectable integration source.
- the shipping runtime recognizes multiple Office/Microsoft Agent, Bonzi-style and PF Magic-style preset identities.
- deterministic Shimeji seed/tick/spawn settings exist in the shipping host.
- shipping GameSync exposes pack import/export/list/delete and state/timeline/memory operations in the browser message contract.
- GameSync's canonical editable browser source is `app/`; production output is generated into `dist/`.
- GameSync Next Extension V2 is version `0.8.0` and contains a verified universal all-site mascot entrypoint.
- the GameSync Next universal mascot no longer requires detected-game state to mount; it requires resolved settings, enabled state, and site-policy permission.
- GameSync Next shares route-change coordination and lightweight/full-runtime ownership to avoid duplicate mascot hosts.
- GameSync Next reports page mascot mount errors to the mascot timeline rather than silently dropping them.
- commit `60940e...` repairs Clippy-compatible initialization ordering and marks universal page mascot parity verified.
- the GameSync Next Opera verifier exercises the mascot on an unrelated HTTP page and through an SPA route without loading the full overlay runtime.

### Not yet proven for the umbrella

- one canonical user-owned repository owns the entire shared browser + desktop mascot core;
- full Shimeji Desktop parity from either browser host;
- complete Microsoft Agent request, Commands, speech-recognition and lip-sync parity;
- complete PF Magic Petz behavioral/persistence parity across all hosts;
- every visible mascot control has been freshly requalified in both browser hosts;
- every pack format round-trips without loss across both hosts;
- desktop restart/persistence behavior across the full umbrella;
- all mascot games are fully playable and parity-qualified;
- GameSync Next has complete parity for every broad legacy shipping pack/message/assistant capability merely because universal mascot mounting is verified.

## Contribution checklist

Before publishing a mascot-related change:

1. confirm the exact source repository/branch/commit and whether the target is GameSync, GameSync Next, or a future desktop host;
2. identify the affected engine, pack format and host surfaces;
3. preserve unrelated engine behavior;
4. update manifest/WXT resource closure when required;
5. run the host's production build;
6. load the generated production extension rather than source files;
7. exercise the changed control and observable mascot behavior;
8. test failure feedback rather than swallowing errors;
9. test reload, SPA navigation and restart persistence where applicable;
10. verify at least one representative pack for each engine affected;
11. when behavior exists in both browser hosts, run a cross-host parity comparison;
12. inspect page and service-worker consoles/timeline diagnostics;
13. prove the runtime loaded the new build rather than a stale extension;
14. record what was actually exercised versus what remains unverified.

## Documentation maintenance rule

Update this wiki when shared mascot-core ownership is resolved, either browser host changes its mascot contract, a separate desktop runtime becomes canonical, engine identifiers/settings change, pack formats change, Shimeji/ACS/Petz semantics change, mascot resource paths move, a new runtime qualification materially changes what can be claimed, or GameSync Next gains/losses parity against the shipping host.

Do not replace this umbrella wiki with one of its subproject pages. The umbrella exists to document how the engines, browser hosts, desktop track, host surfaces and shared state fit together, while the subproject wikis preserve deep engine-specific detail.