# Shimeji Browser Extension Wiki

**Project Constellation ID:** PCX-038  
**Tracked project:** Shimeji Browser Extension  
**Verified current implementation evidence:** GameSync extension repository, `Herbertofury/Gamesync`, branch `main`  
**GameSync package version inspected:** `0.6.3`  
**GameSync commit inspected:** `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`  
**Standalone Shimeji Browser Extension repository:** unresolved in connected GitHub  
**Documentation boundary:** this page documents the verified browser-Shimeji implementation currently embedded/integrated in GameSync. It does not claim that this GameSync subtree is the canonical standalone Shimeji Browser Extension source repository.

## Purpose

The tracked Shimeji Browser Extension project is the browser-hosted Shimeji runtime: faithful mascot packs, page interaction, spawning/removal, persistent configuration, and browser-safe integration. The current connected source proves that GameSync contains a substantial implementation of this track rather than merely a decorative mascot overlay.

The verified implementation is split between:

1. a bundled Shimeji Browser Engine distribution under `app/Shimeji Browser Engine/`;
2. a GameSync background compatibility bridge at `app/background/shimeji-browser-bridge.js`;
3. a global content-script forwarding shim at `app/content/shimeji-popup-shim.js`;
4. GameSync's modular mascot-pack runtime under `app/modules/mascot-pack/background/`;
5. ShimejiEE XML parsing and pack-resolution code in `mascot-shimeji-parse.js`;
6. the large browser/page mascot runtime in `app/Mascot_Engine.js`;
7. manifest wiring that makes the bridge, embedded UI assets, external `shimejis.xyz` install flow, and page injection available in Manifest V3.

## Source map

### Embedded Shimeji Browser Engine distribution

`app/Shimeji Browser Engine/` contains hashed browser-extension artifacts, including:

- `background.58565342.js`
- `content-script.430647cf.js`
- `content-script.d43d51f5.css`
- `popup.01c765a5.html`
- `popup.d6320669.js`
- extension icons and other static UI assets
- bundled fonts

These files are best treated as a compatibility/reference distribution. The GameSync integration deliberately provides the message contract expected by the real bundled popup and content script rather than rewriting their behavior.

### Background bridge

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

### Global forwarding shim

`app/content/shimeji-popup-shim.js` runs on every normal web page from `document_start`. Its job is intentionally narrow: when the embedded popup sends direct tab messages before `Mascot_Engine.js` has been injected, the shim forwards `callAnotherShimeji` and `isConnected` to the background bridge. Removal messages remain the responsibility of the real mascot engine after it is loaded.

### Modular mascot implementation

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

## Manifest V3 wiring

The verified GameSync manifest is Manifest V3 and declares the GameSync background entry point as:

`app/background/background.js`

The background service worker imports and initializes the Shimeji bridge alongside the broader mascot-pack modules.

The manifest also exposes these relevant behaviors:

- `externally_connectable` permits `https://shimejis.xyz/*` and `https://www.shimejis.xyz/*`;
- `app/content/shimeji-popup-shim.js` is injected on `*://*/*` at `document_start`;
- context-menu, scripting, storage, tabs, activeTab, offscreen, nativeMessaging, notifications, and related extension permissions are available to the containing runtime;
- web-accessible resources include `content/mascot/*`, Shimeji pack assets, embedded Shimeji Browser Engine popup/static assets, voice packs, and other mascot resources.

Because GameSync is a large extension, these permissions are not all exclusively for Shimeji. Do not infer that every declared permission is required by the standalone Shimeji project.

## Configuration and storage

### Embedded bridge storage

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

The manifest permits external messages from `shimejis.xyz`. The verified bridge accepts these external message types:

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

## Popup and page message flow

The verified embedded compatibility contract supports these internal message types:

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

The background bridge owns a `Shimeji Browser Extension` page context-menu parent. It can add:

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

The verified containing repository is currently GameSync `0.6.3`.

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

## What to test after changing Shimeji behavior

The repository currently does not expose a dedicated top-level `npm` script named specifically for Shimeji. Therefore this wiki does not invent one. At minimum, a Shimeji change should be validated through the containing extension build plus real browser behavior.

A meaningful manual/runtime verification pass should cover:

1. clean `npm ci` and `npm run build`;
2. loading the generated `dist/` extension in Opera GX/Chromium;
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

Where fixed-seed mode is used for deterministic debugging, verify again with normal random behavior before treating the runtime as generally correct.

## Modification guide

### Adding parser compatibility

Modify `app/modules/mascot-pack/background/mascot-shimeji-parse.js` when adding support for:

- additional XML aliases;
- layout/config discovery;
- schema compatibility;
- pose/action/behavior parsing;
- Shimeji frame resolution;
- behavior hints.

Preserve the existing reference semantics and fallback aliases.

### Changing embedded-extension compatibility

Modify `app/background/shimeji-browser-bridge.js` for:

- popup/content-script message-contract changes;
- `shimejis.xyz` external-message compatibility;
- bridge-owned storage compatibility;
- context-menu behavior.

Modify `app/content/shimeji-popup-shim.js` only for the narrow direct-tab-before-engine-loaded forwarding problem. Avoid turning the shim into a second mascot runtime.

### Changing the real page runtime

The broader runtime spans `app/Mascot_Engine.js` plus the modular mascot-pack runtime and injection helpers imported by `background/background.js`. Preserve the separation between pack parsing/storage, background control, and page execution.

### Adding a bundled reference pack

Use the mascot import/storage pipeline and explicit catalog/reference entries. Preserve source identity and pack semantics. Do not flatten pack behavior into a generic animation list merely to simplify import.

## Troubleshooting

### Popup says the page is not connected

Check whether `shimeji-popup-shim.js` is present in the built manifest and whether the background service worker is alive. The shim must be able to forward `isConnected` before the full page engine exists.

### Spawn action does nothing

Check, in order:

1. active tab resolution;
2. bridge message handling;
3. page injection of the mascot runtime;
4. stored spec ID;
5. runtime asset availability;
6. site policy / activation state.

Do not treat a successful background response alone as proof that a visible Shimeji spawned.

### Character installs but has no meaningful behavior

Inspect the imported actions and behaviors, not just sprites. Verify that the correct XML files were selected, references resolve, animations contain poses, behavior frequencies/conditions survived parsing, and image paths resolve into the chosen image set.

### Old pack cannot find actions.xml or behaviors.xml

Use the parser's candidate-resolution model. Packs may use alternate names or place configuration under root `conf`, `conf/<imageSet>`, or `img/<imageSet>/conf`. Preserve alternate/Japanese schema aliases.

### Context-menu duplicates or stale names appear

The bridge intentionally rebuilds menus and removes children before the parent. Check whether multiple bridge initializations/listeners are being installed or whether a service-worker lifecycle change bypassed cleanup.

### State disappears after restart

Check both stores: `shimejiBrowser_*` compatibility keys and GameSync's broader mascot settings/IndexedDB state. They are not the same persistence layer.

## Architecture invariants

- Preserve authentic Shimeji action/behavior graph semantics.
- Preserve anchors, pose durations, velocity/physics, borders, conditions, references, and weighted behavior choice.
- Preserve required `Fall`, `Dragged`, and `Thrown` behavior expectations.
- Keep page interaction browser-safe and user-controlled.
- Keep bridge compatibility separate from the page runtime.
- Keep the lightweight forwarding shim lightweight.
- Treat storage migration carefully because embedded compatibility state and GameSync mascot state use different contracts.
- Never count a popup success response as proof that the page runtime performed the requested visible action.
- Do not claim standalone-repository completeness from the embedded GameSync subtree.

## Known unresolved boundary

The connected GitHub installation does not currently expose a separate repository named for Shimeji Browser Extension. GameSync proves a real, substantial integrated browser-Shimeji implementation and contains an embedded extension distribution, but this does not establish whether a newer standalone source tree exists elsewhere.

A future documentation pass should supersede or extend this page when the standalone canonical repository is resolved. Until then, this GameSync implementation is the strongest verified connected source for the tracked browser-Shimeji project.

## Maintenance triggers

Update this wiki when any of the following changes materially:

- canonical standalone repository identity;
- GameSync version or integration ownership;
- Shimeji bridge message contract;
- `shimejis.xyz` external install protocol;
- XML schema/parser behavior;
- pack/config discovery rules;
- runtime tick/physics/behavior semantics;
- storage schema or keys;
- page injection architecture;
- context-menu behavior;
- build/load procedure;
- browser verification evidence;
- bundled Shimeji reference packs.
