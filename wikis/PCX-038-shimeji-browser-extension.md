# Shimeji Browser Extension Wiki

**Project Constellation ID:** PCX-038  
**Tracked project:** Shimeji Browser Extension  
**Verified implementation evidence:** GameSync `Herbertofury/Gamesync` and GameSync Next `Herbertofury/GameSync-Next`, both on `main`  
**GameSync package version inspected:** `0.6.3`  
**GameSync commit inspected:** `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`  
**GameSync Next Extension V2 package version inspected:** `0.8.0`  
**GameSync Next current main inspected:** `9e337c720f0180cffa577f140b181c699f0a1650`  
**GameSync Next universal mascot parity commit:** `60940e8479af518f3373a79efa091902f4843842`  
**Standalone Shimeji Browser Extension repository:** unresolved in connected GitHub  
**Documentation boundary:** this page documents the strongest verified browser-Shimeji implementations currently connected through GameSync and GameSync Next. It does not claim that either containing repository is the canonical standalone Shimeji Browser Extension source repository.

## Purpose

The tracked Shimeji Browser Extension project is the browser-hosted Shimeji runtime: faithful mascot packs, page interaction, spawning/removal, persistent configuration, and browser-safe integration. The current connected source proves that GameSync contains a substantial implementation of this track rather than merely a decorative mascot overlay.

GameSync Next now also provides a verified all-site lightweight mascot path in Extension V2. That path closes the previous parity gap where the Next content runtime only covered explicit GameSync integration sites instead of ordinary web pages.

The verified implementation evidence now spans:

1. a bundled Shimeji Browser Engine distribution under GameSync `app/Shimeji Browser Engine/`;
2. a GameSync background compatibility bridge at `app/background/shimeji-browser-bridge.js`;
3. a global GameSync content-script forwarding shim at `app/content/shimeji-popup-shim.js`;
4. GameSync's modular mascot-pack runtime under `app/modules/mascot-pack/background/`;
5. ShimejiEE XML parsing and pack-resolution code in `mascot-shimeji-parse.js`;
6. the large GameSync browser/page mascot runtime in `app/Mascot_Engine.js`;
7. GameSync manifest wiring that makes the bridge, embedded UI assets, external `shimejis.xyz` install flow, and page injection available in Manifest V3;
8. GameSync Next's all-site `page-mascot.content.ts` entrypoint;
9. GameSync Next's `universalPageMascot.ts` settings/lifecycle coordinator;
10. GameSync Next's `pageMascot.ts` page-mount runtime;
11. GameSync Next's `runtimeCoordination.ts` SPA/full-runtime ownership coordinator;
12. GameSync Next's isolated Opera parity verification in `scripts/verify-extension-v2-opera.js`.

## Source map

### GameSync embedded Shimeji Browser Engine distribution

`app/Shimeji Browser Engine/` contains hashed browser-extension artifacts, including:

- `background.58565342.js`
- `content-script.430647cf.js`
- `content-script.d43d51f5.css`
- `popup.01c765a5.html`
- `popup.d6320669.js`
- extension icons and other static UI assets
- bundled fonts

These files are best treated as a compatibility/reference distribution. The GameSync integration deliberately provides the message contract expected by the real bundled popup and content script rather than rewriting their behavior.

### GameSync background bridge

`app/background/shimeji-browser-bridge.js` is the primary adapter between the embedded Shimeji Browser Extension behavior and GameSync's Manifest V3 service worker.

It provides:

- ShimejiEE XML parsing compatible with the expected configuration format;
- local-storage helpers matching the embedded popup/content script's JSON-string storage convention;
- default configuration initialization;
- active/inactive Shimeji settings;
- active-tab lookup and tab messaging;
- Shimeji context-menu creation and refresh;
- spawn/change/toggle context-menu actions;
- popup/content-script message handling;
- external install/configuration messages from `shimejis.xyz`;
- service-worker initialization and listener cleanup.

### GameSync global forwarding shim

`app/content/shimeji-popup-shim.js` runs on every normal web page from `document_start`. Its job is intentionally narrow: when the embedded popup sends direct tab messages before `Mascot_Engine.js` has been injected, the shim forwards `callAnotherShimeji` and `isConnected` to the background bridge. Removal messages remain the responsibility of the real mascot engine after it is loaded.

### GameSync modular mascot implementation

`app/modules/mascot-pack/background/` contains the maintainable GameSync-side mascot subsystem. Important files currently include:

| File | Responsibility |
| --- | --- |
| `mascot-contract.js` | Message/event contract, settings defaults, storage keys, built-in catalog data, engine identifiers, behavior limits. |
| `mascot-external-message.js` | External mascot-facing message handling. |
| `mascot-idb.js` | IndexedDB-backed mascot storage. |
| `mascot-import.js` | Pack import and conversion pipeline. |
| `mascot-memory.js` | Bounded mascot memory/history state. |
| `mascot-message-handler.js` | Main internal mascot message routing. |
| `mascot-runtime.js` | Runtime pack/session behavior. |
| `mascot-session-helpers.js` | Per-session helpers. |
| `mascot-settings-bg.js` | Background settings management. |
| `mascot-shimeji-parse.js` | ShimejiEE config discovery, XML parsing, frame resolution, schema compatibility, behavior hints. |
| `mascot-game-handler.js` | Mascot game-related message handling. |
| `native-audio.js` | Native/audio integration used by mascot features. |

## GameSync Next universal page mascot parity

GameSync Next Extension V2 `0.8.0` now has a distinct lightweight all-site mascot path. This is materially different from the older state in which Next depended on the full content runtime's explicit supported-site list.

The parity work was introduced by commit `60940e8479af518f3373a79efa091902f4843842`. The repository's parity record changed the universal-page-mascot item from `gap` to `verified` and tied verification to the isolated Opera Extension V2 workflow.

### All-site content entrypoint

`apps/extension-v2/src/entrypoints/page-mascot.content.ts` is a WXT content-script entrypoint with:

- matches: `*://*/*`;
- `document_idle` startup;
- dynamic import of `../content/universalPageMascot`;
- immediate call to `initUniversalPageMascot()` after import.

This keeps the ordinary-page mascot path separate from the much larger GameSync content runtime.

### Universal lifecycle coordinator

`apps/extension-v2/src/content/universalPageMascot.ts` owns the lightweight all-page lifecycle.

Verified behavior includes:

- starting from `GAME_SYNC_SETTINGS_DEFAULTS`;
- resolving current settings through the background `getSettings` message first;
- falling back to `chrome.storage.sync` if background messaging is unavailable;
- listening for `MASCOT_SPAWN`, `MASCOT_DISMISS`, and `SETTINGS_CHANGED` runtime messages;
- listening for `chrome.storage.onChanged` updates to the shared `settings` object;
- coalescing refreshes through `requestAnimationFrame`;
- listening for GameSync SPA route-change events plus `popstate` and `hashchange`;
- listening for the full-runtime-active event;
- disposing runtime listeners and the live mascot on `pagehide` or `beforeunload`.

The coordinator deliberately avoids owning the page when the full GameSync content runtime does. If the page is a known GameSync runtime page, or the full content runtime marks itself active, the lightweight runtime disposes its controller without falsely reporting a user dismissal.

### Shared SPA/full-runtime coordination

`apps/extension-v2/src/content/runtimeCoordination.ts` provides two explicit events:

- `gamesync:runtime-route-change`
- `gamesync:full-runtime-active`

It patches `history.pushState` and `history.replaceState` once, then dispatches a route-change event in a microtask after navigation. The full content runtime marks a global `__gamesyncV2FullContentRuntimeActive` flag and dispatches the full-runtime-active event when it takes ownership.

This prevents two mascot hosts from independently mounting on the same GameSync-owned page while still allowing the lightweight mascot to survive ordinary SPA navigation on unrelated sites.

### Page mascot mount runtime

`apps/extension-v2/src/content/features/pageMascot.ts` is the mount controller used by both lightweight and full content paths.

Current source verifies these rules:

- settings must be ready;
- mascot `enabled` must be true;
- `gameSyncSitePolicyAllowsUrl()` must allow the current URL;
- a detected game is no longer required before page mascot mounting;
- the current effective mascot settings are serialized into a mount key so unchanged settings reuse the existing live controller;
- changed settings dispose and remount the page mascot;
- `mountSurfaceMascot(..., "content")` owns the visible mascot instance;
- runtime activity is reported back through `mascotPageRuntime` messages;
- mount failures are written to the mascot timeline as `surface-mount-error` with the page URL and captured error text before inactive state is reported.

Removing the old `DetectedGame` requirement is what makes ordinary-page mascot behavior possible without pretending every arbitrary website is a detected game integration.

### Verified parity behavior

The GameSync Next parity matrix now points universal-page-mascot verification at:

- `apps/extension-v2/src/entrypoints/page-mascot.content.ts`
- `apps/extension-v2/src/content/universalPageMascot.ts`
- `apps/extension-v2/src/content/features/pageMascot.ts`
- `scripts/verify-extension-v2-opera.js`

The current verification record states that isolated Opera:

- loads the lightweight all-site mascot on an unrelated HTTP page;
- preserves one live mascot host across an SPA route change;
- restores changed settings after the check;
- verifies that the full overlay/content runtime was not loaded merely to provide the lightweight mascot.

Treat that as parity proof for the all-site host path, not proof that every historical standalone Shimeji Browser Extension feature has been reimplemented in GameSync Next.

## Manifest V3 wiring

### GameSync

The verified GameSync manifest is Manifest V3 and declares the GameSync background entry point as:

`app/background/background.js`

The background service worker imports and initializes the Shimeji bridge alongside the broader mascot-pack modules.

The manifest also exposes these relevant behaviors:

- `externally_connectable` permits `https://shimejis.xyz/*` and `https://www.shimejis.xyz/*`;
- `app/content/shimeji-popup-shim.js` is injected on `*://*/*` at `document_start`;
- context-menu, scripting, storage, tabs, activeTab, offscreen, nativeMessaging, notifications, and related extension permissions are available to the containing runtime;
- web-accessible resources include `content/mascot/*`, Shimeji pack assets, embedded Shimeji Browser Engine popup/static assets, voice packs, and other mascot resources.

Because GameSync is a large extension, these permissions are not all exclusively for Shimeji. Do not infer that every declared permission is required by the standalone Shimeji project.

### GameSync Next

GameSync Next builds Extension V2 with WXT. The verified package is `gamesync-extension-v2` version `0.8.0` using WXT `0.21.4` and TypeScript `6.0.3`.

The universal mascot content entrypoint is generated from `src/entrypoints/page-mascot.content.ts`. Its all-site match scope and lightweight dynamic import are source-level project behavior, not an inferred manifest claim.

## Configuration and storage

### Embedded GameSync bridge storage

The bridge stores the embedded Shimeji Browser Engine compatibility state in `chrome.storage.local` using JSON-encoded strings so the bundled popup/content-script helpers receive the format they expect.

Verified keys include:

- `shimejiBrowser_specs`
- `shimejiBrowser_settings`

The settings default currently used by the bridge is:

- `active: true`
- `reportErrors: false`

If no Shimeji specifications exist, the bridge installs a minimal `Blank Guy` stub so the embedded UI has a valid initial shape.

### GameSync mascot storage contract

The modular mascot layer defines separate GameSync-owned state including:

- `mascotSettings`
- `mascotMemory`
- `mascotTimeline`
- `mascotSelectionProfiles`
- IndexedDB database `gamesync_mascot`, schema version `2`

The current contract limits timeline history to 500 entries and mascot memory to 50 entries. Runtime asset concurrency is 8 and the current runtime asset ceiling is 220 assets.

This means the embedded Shimeji Browser compatibility state and the broader GameSync mascot state are related but not identical stores. Preserve both contracts when refactoring.

### GameSync Next shared settings

GameSync Next's universal mascot reads the shared resolved `GameSyncSettings` object. It reacts to background `SETTINGS_CHANGED` messages and `chrome.storage.sync` changes rather than creating a separate per-page mascot settings store.

The page mount key currently tracks at least:

- enabled state;
- agent;
- active pack ID;
- greet-on-open;
- interaction mode;
- dock side;
- speech enabled;
- quiet mode;
- snooze time;
- size;
- speed;
- site-policy mode and list.

This is an important migration boundary. The older embedded GameSync Shimeji compatibility keys and GameSync Next's typed shared settings are not interchangeable persistence formats.

## Current mascot settings relevant to Shimeji

The GameSync mascot contract currently includes these Shimeji/Webmeji-related defaults:

- mascot system enabled by default;
- roam enabled;
- interaction mode enabled;
- size and speed default to `1`;
- `wallThrowMode: "grab"`;
- `webmejiCanvasRenderer: false`;
- `webmejiEnabled: false`;
- `webmejiSpawnCount: 3`;
- `sitePolicyMode: "all"`;
- default Shimeji fixed RNG seed value `1337`, while fixed-seed mode is disabled by default;
- `shimejiTickMs: 40`;
- `shimejiSpawnCap: 12`;
- automatic spawn on import enabled;
- Webmeji pet, drag, bottom, top, left, and right allowances enabled.

These values are part of the current GameSync mascot contract, not necessarily the historical standalone extension defaults.

## ShimejiEE compatibility

The maintainable parser in `mascot-shimeji-parse.js` is explicitly based on ShimejiEE behavior and records the reference source as `Reference/shimejieesrc`.

### Config discovery

The parser supports action and behavior XML discovery in multiple traditional locations, including root `conf`, image-set-specific `conf`, and image-set-local configuration directories. It also supports multiple historical/translated aliases for `actions.xml` and `behaviors.xml`.

When multiple candidates exist, the resolver scores the likely configuration using:

- directory rank;
- detected image set;
- root prefix consistency;
- alias priority;
- deterministic path tie-breaking.

This is important when importing old Shimeji packs whose layout differs from modern standardized archives.

### Core semantics preserved

The current parser records or implements these ShimejiEE compatibility expectations:

- a 40 ms manager tick interval;
- weighted next-behavior selection using behavior frequencies;
- required non-toggleable behaviors `Fall`, `Dragged`, and `Thrown`;
- animation poses with image, anchor, velocity, and duration;
- action references and nested Sequence/Select actions;
- behavior references and conditional behavior groups;
- border and movement parameters;
- physics fields including initial velocity, resistance, gravity, and gap;
- compatibility with the historical `RegistanceX` / `RegistanceY` spelling alongside corrected resistance names;
- Japanese/alternate XML tag and attribute aliases.

Do not replace this parser with a generic sprite-sequence loader. The XML graph, physics, condition, reference, and behavior-frequency semantics are part of project correctness.

## Installing a Shimeji from shimejis.xyz

The GameSync manifest permits external messages from `shimejis.xyz`. The verified bridge accepts these external message types:

- `activateShimejiConfiguration`
- `getConfigurations`
- `callAnotherShimeji`

For `activateShimejiConfiguration`, the bridge:

1. validates the incoming configuration;
2. derives an ID from the explicit configuration ID or `metadata.shimeji`;
3. converts string-form ShimejiEE actions/behaviors XML into the expected runtime representation when needed;
4. builds the stored spec with actions, behaviors, spritesheet, sprites, and metadata;
5. replaces a requested previous configuration or updates an existing same-ID configuration;
6. persists the spec in `shimejiBrowser_specs`;
7. forces Shimeji activity on;
8. rebuilds the extension context menus.

`getConfigurations` intentionally reports an empty active-configuration list to the site, so the bridge does not enforce the site's two-Shimeji active-configuration cap.

This external install protocol is verified for the GameSync bridge. The all-site GameSync Next parity work described above does not by itself prove equivalent `shimejis.xyz` external-install compatibility in Extension V2.

## Popup and page message flow

The verified embedded GameSync compatibility contract supports these internal message types:

- `getTabId`
- `openPageAndStart`
- `isOnToolbar`
- `callAnotherShimeji`
- `removeOneShimejiForSpec`
- `removeAllShimejisForSpec`
- `isConnected`

### Spawn flow

A typical spawn from the embedded popup is:

1. popup sends `callAnotherShimeji` to the active tab;
2. if the full mascot engine is not yet present, `shimeji-popup-shim.js` forwards the request to the background;
3. the background bridge resolves the active tab and forwards the spawn request into the page runtime;
4. the broader GameSync injection/runtime layer can ensure the mascot engine is available;
5. the page runtime owns the live creature after injection.

### Open-page-and-start flow

`openPageAndStart` navigates the current active tab to the requested URL, waits briefly for navigation, then requests a spawn for each stored Shimeji specification.

### Connectivity flow

`isConnected` checks the active tab and delegates to the page runtime. Failures return a false/unsuccessful result rather than claiming the page is connected.

## Context menus

The GameSync background bridge owns a `Shimeji Browser Extension` page context-menu parent. It can add:

- one `Spawn <name>` entry per stored spec;
- `Change Character...`, which opens `shimejis.xyz`;
- `STOP Shimejis` or `START Shimejis`, depending on current activation state.

The bridge rebuilds these entries when `shimejiBrowser_specs` changes. It removes children before the parent and tolerates duplicate/nonexistent menu-ID errors during refresh.

## Bundled reference Shimejis

The current GameSync mascot contract defines at least these bundled Shimeji references:

- `Mangle`
- `Toy Bonnie`

Their configuration JSON and spritesheet paths live under `assets/mascot/shimejis/`. The contract also contains a larger built-in ACS/Office/Microsoft Agent catalog. Those ACS packs are a neighboring mascot-runtime concern, not evidence that Shimeji packs should be converted into ACS semantics.

## Build and development workflow

### GameSync

The verified containing GameSync repository is currently package version `0.6.3`.

From the repository root:

```powershell
npm ci
npm run build
```

For active development:

```powershell
npm run dev
```

The GameSync README identifies `app/` as canonical editable extension source and `dist/` as generated production output. After source changes, rebuild and load the generated `dist/` directory as the unpacked Opera GX extension.

Do not directly treat the hashed files in `app/Shimeji Browser Engine/` as the only maintainable project source. Integration changes should normally be made in the bridge, shim, modular mascot parser/runtime, manifest, or source asset pipeline unless the bundled reference itself intentionally needs replacement.

### GameSync Next Extension V2

From the GameSync Next repository root, the verified workspace commands are:

```powershell
npm ci
npm --workspace apps/extension-v2 run build
npm --workspace apps/extension-v2 run verify:opera
```

The equivalent root verification command is:

```powershell
npm run verify:extension-v2:opera
```

`apps/extension-v2/package.json` also exposes:

```powershell
npm --workspace apps/extension-v2 run dev
npm --workspace apps/extension-v2 run zip
npm --workspace apps/extension-v2 run lint
npm --workspace apps/extension-v2 run typecheck:room
```

The Extension V2 `build` script runs `wxt build` and then verifies the offscreen runtime. Do not skip the build before Opera parity verification when testing a clean checkout.

## What to test after changing Shimeji behavior

A meaningful regression pass should preserve both containing implementations where the change touches shared behavior.

### GameSync bridge/runtime checklist

1. clean `npm ci` and `npm run build`;
2. load the generated `dist/` extension in Opera GX/Chromium;
3. popup opens and communicates with the active page;
4. `isConnected` reflects real page runtime state;
5. first spawn injects/activates the mascot runtime;
6. repeated spawn works without duplicate-listener breakage;
7. remove-one and remove-all behavior works after the engine is active;
8. context-menu Spawn entries match stored packs;
9. START/STOP menu state updates after toggling;
10. installing a configuration from `shimejis.xyz` persists it;
11. imported XML actions/behaviors preserve references, conditions, poses, anchors, durations, movement, and required behaviors;
12. restart/reload preserves imported packs and activation/settings state;
13. site policy and interaction allowances still work;
14. page interaction does not break normal host-page input or navigation;
15. service-worker restart does not create duplicate context-menu/listener behavior.

### GameSync Next all-site parity checklist

1. build Extension V2 from current source;
2. run `npm run verify:extension-v2:opera` in the isolated Opera fixture;
3. confirm a mascot appears on the unrelated smoke HTTP page without loading the full overlay runtime;
4. navigate the smoke page through a client-side SPA route and confirm only one live mascot host remains;
5. change a mascot setting and confirm the page host remount/reuses according to the mount-key contract;
6. disable the mascot or deny the URL through site policy and confirm the live page mascot disposes;
7. force a mascot mount failure and confirm the timeline receives `surface-mount-error` plus the page URL while active state becomes false;
8. enter a GameSync-owned full content runtime page and confirm the lightweight host yields ownership rather than double-mounting;
9. confirm settings altered by the fixture are restored after verification;
10. reload/restart the extension and confirm shared settings still drive the all-site host.

Where fixed-seed mode is used for deterministic debugging, verify again with normal random behavior before treating the runtime as generally correct.

## Modification guide

### Adding parser compatibility in GameSync

Modify `app/modules/mascot-pack/background/mascot-shimeji-parse.js` when adding support for:

- additional XML aliases;
- layout/config discovery;
- schema compatibility;
- pose/action/behavior parsing;
- Shimeji frame resolution;
- behavior hints.

Preserve the existing reference semantics and fallback aliases.

### Changing embedded-extension compatibility in GameSync

Modify `app/background/shimeji-browser-bridge.js` for:

- popup/content-script message-contract changes;
- `shimejis.xyz` external-message compatibility;
- bridge-owned storage compatibility;
- context-menu behavior.

Modify `app/content/shimeji-popup-shim.js` only for the narrow direct-tab-before-engine-loaded forwarding problem. Avoid turning the shim into a second mascot runtime.

### Changing the GameSync real page runtime

The broader runtime spans `app/Mascot_Engine.js` plus the modular mascot-pack runtime and injection helpers imported by `background/background.js`. Preserve the separation between pack parsing/storage, background control, and page execution.

### Changing GameSync Next all-site mascot behavior

Use these ownership boundaries:

- `apps/extension-v2/src/entrypoints/page-mascot.content.ts`: all-site WXT entrypoint and load timing;
- `apps/extension-v2/src/content/universalPageMascot.ts`: all-page lifecycle, settings synchronization, SPA/lifecycle listeners, lightweight/full-runtime ownership handoff;
- `apps/extension-v2/src/content/features/pageMascot.ts`: eligibility, mount-key identity, mount/dispose behavior, activity reporting, mount-error timeline reporting;
- `apps/extension-v2/src/content/runtimeCoordination.ts`: shared SPA route events and full-runtime ownership marker;
- `apps/extension-v2/src/ui/lib/surfaceMascot`: actual visible surface mascot implementation loaded by the page runtime;
- `scripts/verify-extension-v2-opera.js`: real isolated-Opera parity proof.

Do not solve an all-site mascot defect by loading the complete GameSync overlay/content runtime onto every arbitrary page. The current architecture deliberately keeps the generic mascot host lightweight.

### Adding a bundled reference pack

Use the mascot import/storage pipeline and explicit catalog/reference entries. Preserve source identity and pack semantics. Do not flatten pack behavior into a generic animation list merely to simplify import.

## Troubleshooting

### GameSync popup says the page is not connected

Check whether `shimeji-popup-shim.js` is present in the built manifest and whether the background service worker is alive. The shim must be able to forward `isConnected` before the full page engine exists.

### GameSync spawn action does nothing

Check, in order:

1. active tab resolution;
2. bridge message handling;
3. page injection of the mascot runtime;
4. stored spec ID;
5. runtime asset availability;
6. site policy / activation state.

Do not treat a successful background response alone as proof that a visible Shimeji spawned.

### GameSync Next mascot appears only on known game sites

Confirm the built extension includes the WXT output for `page-mascot.content.ts`. The verified source matches `*://*/*`; the page mascot itself no longer requires a detected game. If the generic host is missing, inspect build output and entrypoint generation before changing site detection.

### GameSync Next shows two mascot hosts on a GameSync integration page

Inspect `runtimeCoordination.ts`, the full-runtime marker/event, and `fullContentRuntimeOwnsPage()` in `universalPageMascot.ts`. The lightweight host must dispose when the full runtime owns the page.

### GameSync Next mascot disappears after SPA navigation

Confirm `installGameSyncRouteObserver()` is installed once and that `gamesync:runtime-route-change`, `popstate`, and `hashchange` listeners remain registered. The parity fixture specifically verifies one live host survives an SPA route transition.

### GameSync Next mascot mount fails silently

Inspect mascot timeline data for a `surface-mount-error` entry. Current `pageMascot.ts` records the page URL and captured error text, then reports inactive runtime state. A missing timeline record indicates the failure occurred outside the verified page-mount error path.

### Character installs but has no meaningful behavior

Inspect the imported actions and behaviors, not just sprites. Verify that the correct XML files were selected, references resolve, animations contain poses, behavior frequencies/conditions survived parsing, and image paths resolve into the chosen image set.

### Old pack cannot find actions.xml or behaviors.xml

Use the parser's candidate-resolution model. Packs may use alternate names or place configuration under root `conf`, `conf/<imageSet>`, or `img/<imageSet>/conf`. Preserve alternate/Japanese schema aliases.

### Context-menu duplicates or stale names appear

The GameSync bridge intentionally rebuilds menus and removes children before the parent. Check whether multiple bridge initializations/listeners are being installed or whether a service-worker lifecycle change bypassed cleanup.

### State disappears after restart

Check the persistence model for the containing implementation actually under test. GameSync's `shimejiBrowser_*` compatibility keys and broader mascot IndexedDB state are separate stores; GameSync Next reads its typed shared settings through background resolution or `chrome.storage.sync`. Do not migrate or troubleshoot one as if it were the other.

## Architecture invariants

- Preserve authentic Shimeji action/behavior graph semantics.
- Preserve anchors, pose durations, velocity/physics, borders, conditions, references, and weighted behavior choice.
- Preserve required `Fall`, `Dragged`, and `Thrown` behavior expectations.
- Keep page interaction browser-safe and user-controlled.
- Keep GameSync bridge compatibility separate from the page runtime.
- Keep the GameSync forwarding shim lightweight.
- Keep the GameSync Next generic page mascot host lightweight and separate from the full overlay/content runtime.
- Preserve SPA route coordination and single-host ownership in GameSync Next.
- Treat storage migration carefully because embedded compatibility state, GameSync mascot state, and GameSync Next typed settings use different contracts.
- Never count a popup or background success response as proof that the page runtime performed the requested visible action.
- Do not claim standalone-repository completeness from either containing GameSync repository.
- Treat GameSync Next's universal-page-mascot verification as proof of all-site host parity, not proof of every historical popup, context-menu, external-install, or ShimejiEE import feature.

## Known unresolved boundary

The connected GitHub installation does not currently expose a separate repository named for Shimeji Browser Extension. GameSync proves a real, substantial integrated browser-Shimeji implementation and contains an embedded extension distribution. GameSync Next now proves a typed lightweight all-site page mascot host with isolated Opera parity evidence. Neither establishes whether a newer standalone source tree exists elsewhere.

The biggest remaining documentation/implementation reconciliation question is feature ownership across the two containing runtimes: which historical standalone behaviors are intentionally retained only in the GameSync compatibility bridge, and which should also exist in GameSync Next. In particular, the current all-site parity proof does not establish Extension V2 equivalents for the historical `shimejis.xyz` external install protocol or the embedded Shimeji Browser context-menu contract.

A future documentation pass should supersede or extend this page when the standalone canonical repository is resolved or when those compatibility surfaces move into GameSync Next.

## Maintenance triggers

Update this wiki when any of the following changes materially:

- canonical standalone repository identity;
- GameSync or GameSync Next version/integration ownership;
- universal all-site mascot parity status;
- Shimeji bridge message contract;
- `shimejis.xyz` external install protocol;
- XML schema/parser behavior;
- pack/config discovery rules;
- runtime tick/physics/behavior semantics;
- storage schema or keys;
- page injection architecture;
- SPA/full-runtime ownership coordination;
- context-menu behavior;
- build/load procedure;
- browser verification evidence;
- bundled Shimeji reference packs.