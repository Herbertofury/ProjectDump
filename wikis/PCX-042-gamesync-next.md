# GameSync Next Wiki

**Project Constellation ID:** `PCX-042`
**Status:** ACTIVE / TRACKED
**Canonical connected repository:** [Herbertofury/GameSync-Next](https://github.com/Herbertofury/GameSync-Next)
**Default branch:** `main`
**Current verified main head:** `9e337c720f0180cffa577f140b181c699f0a1650`
**Extension V2 package/manifest version:** `0.8.0`
**Current shipping parity source:** [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync) at `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`

## Purpose

GameSync Next is the typed, modular successor and migration workspace for the shipping GameSync browser product. It combines a WXT/React Manifest V3 extension, desktop and WebSocket server hosts, shared packages, native integrations, Feature Foundry surfaces, game/runtime projects, Playwright/Opera verification tooling, and an executable parity system against the shipping JavaScript GameSync implementation.

The governing rule is **migration with proof, not replacement by assumption**. Shipping GameSync remains the product-surface baseline until each relevant capability is implemented and proven through current runtime evidence.

## Current source authority

The canonical source is the private `Herbertofury/GameSync-Next` repository on `main`. The current main head is `9e337c720f0180cffa577f140b181c699f0a1650`, whose latest change repairs transient Opera extension discovery so failed probes can retry on later polling iterations while preserving de-duplication within one iteration.

The standalone shipping baseline is `Herbertofury/Gamesync` at `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928` in the current durable lead-gate evidence. Do not run a parity audit against an arbitrary older GameSync checkout and treat the result as current.

Open proposal branches and pull requests are **not current product source** until merged and reverified. In particular, the current Vite 8.2.1 stack proposal and the package-build incremental optimization remain open/draft and externally blocked from exact-head acceptance. They are documented later as pending work, not as main behavior.

## Repository layout

The current README and source tree identify these major areas:

- `apps/extension-v2` - WXT Manifest V3 Opera/Chromium extension.
- `apps/desktop` - React/Vite desktop host with a Tauri 2 shell.
- `apps/server` - authoritative WebSocket room/game server.
- `apps/feature-foundry` - portable Feature Foundry authoring surface hosted inside this monorepo.
- `apps/asset-orchestrator` - source-only asset tooling; local asset vaults are intentionally excluded from Git.
- `packages` - shared schemas, engine, core, UI, shared logic, Pixi/game packages, Pascal room engine, Petz-related packages, HyperBowl packages, and other reusable slices.
- `native-helper`, `native-host`, `playnite-bridge` - native integration sources.
- `scripts/audit-gamesync-parity.mjs` - executable shipping-JavaScript-to-Next parity audit.
- `docs/gamesync-parity-matrix.json` - machine-readable capability contract.
- `scripts/verify-extension-v2-opera.js` - maintained real Opera GX Extension V2 verifier.
- `scripts/agent-browser.mjs` and Opera launch helpers - browser automation/diagnostic surfaces.
- `scripts/hyperbowl/*` - HyperBowl extraction, indexing, audit, capture, reconstruction, and evidence tooling.

The root also preserves large project-owned references including `AGENTS.md`, `Bugs&Fixes.md`, `Feature Layout.md`, `GAMESYNC.md`, `CARDGAME.md`, `HYPERBOWL.md`, and `HYPERBOWL_ORIGINAL_RECONSTRUCTION_MASTER.md`. Treat those as project evidence, but prefer current executable source and current machine-readable contracts when prose and runtime disagree.

## Dependency installation

From a clean canonical checkout:

```text
npm ci
```

The root workspace uses npm workspaces over:

```text
apps/*
packages/*
```

Use the checked-in lockfile as the dependency-resolution authority. Do not hand-promote a newer dependency version from a proposal branch into documentation as current main behavior.

## Root workspace commands

### Shared packages and primary hosts

```text
npm run build:packages
npm run dev:desktop
npm run dev:feature-foundry
npm run dev:server
npm run build
npm run build:feature-foundry
```

The root `build:packages` command currently builds these shared workspaces in order:

```text
packages/schema
packages/shared
packages/engine
packages/core
packages/pixi-game
packages/ui
```

The root `build` then builds the server and desktop hosts after shared packages.

### GameSync parity and Opera verification

```text
npm run audit:gamesync-parity
npm run verify:extension-v2:opera
npm run opera:inventory
npm run browser:opera:start
npm run browser:agent:opera
```

### Playwright

```text
npm run pw:list
npm run pw:test
npm run pw:test:headed
npm run pw:test:ui
npm run pw:test:web
npm run pw:test:extension
npm run pw:test:opera-extension
```

### Regression suites

```text
npm run test:mo2-regression
npm run test:intel-regression
npm run test:intel-ui-smoke
npm run test:extension-regression
```

### Important current command defect

The root manifest also advertises:

```text
npm run test:e2e-opera
```

which currently resolves to:

```text
node opera-extension/app/tests/e2e.opera-gx.test.js
```

That file is **absent on current `main`**. This script is therefore not a valid current verification path. Do not report `test:e2e-opera` as runnable on main until the compatibility entrypoint is restored and merged.

The maintained real Extension V2 Opera verification path is:

```text
npm run verify:extension-v2:opera
```

which builds Extension V2 and invokes `scripts/verify-extension-v2-opera.js`.

## Extension V2 identity and build

`apps/extension-v2/package.json` currently identifies:

```text
name: gamesync-extension-v2
version: 0.8.0
module type: ESM
WXT: 0.21.4
TypeScript: ^6.0.3
React / React DOM: ^19.2.7
```

Important runtime dependencies include:

- `@gamesync/core`
- `@gamesync/pascal-room-engine`
- `@gamesync/shared`
- `@gamesync/ui`
- Dexie
- DOMPurify
- JSZip
- morphdom
- Three.js

Extension-local commands are:

```text
npm --workspace apps/extension-v2 run dev
npm --workspace apps/extension-v2 run build
npm --workspace apps/extension-v2 run typecheck:room
npm --workspace apps/extension-v2 run lint
npm --workspace apps/extension-v2 run zip
npm --workspace apps/extension-v2 run verify:opera
npm --workspace apps/extension-v2 run verify:same-id-upgrade
npm --workspace apps/extension-v2 run verify:offscreen-runtime
```

The extension `build` command runs WXT and then the offscreen-runtime verifier. A WXT compilation that skips the offscreen-runtime integrity gate is not equivalent to the declared package build.

## Extension V2 generated page surfaces

The WXT configuration maps the legacy root page names to current app entrypoints:

```text
full.html -> app-full.html
options.html -> app-options.html
panel.html -> app-panel.html
popup.html -> app-popup.html
```

The source entrypoint tree contains dedicated app surfaces for:

- `app-full`
- `app-options`
- `app-panel`
- `app-popup`
- background service worker
- general content script
- Feature Foundry bridge
- page-mascot content script
- compatibility/redirect entrypoints for full, options, panel, and popup

This structure matters when debugging stale surface behavior. Confirm which generated page is actually loaded rather than editing a compatibility redirect and assuming the React application changed.

## Extension V2 manifest behavior

The current WXT config emits a Manifest V3 extension named `GameSync V2 (MALSync-style for games)` at version `0.8.0`.

### Primary extension surfaces

- browser action popup: `app-popup.html`
- options page/UI: `app-options.html`
- Opera `sidebar_action`: `app-panel.html`
- Chromium `side_panel`: `app-panel.html`
- module service worker: `background.js`

### Keyboard commands

```text
Ctrl+Shift+K -> open-command-center
Alt+G -> toggle-overlay
```

The parity matrix records the command center as verified through a real Windows key chord in Opera. The verified flow opens/focuses the canonical full surface and renders the command palette without duplicating the React root.

### Permissions

Current declared permissions are:

```text
activeTab
alarms
contextMenus
cookies
desktopCapture
downloads
nativeMessaging
notifications
offscreen
scripting
storage
unlimitedStorage
tabCapture
tabs
```

The manifest also permits localhost/127.0.0.1 integrations, Steam/RAWG/store-provider hosts, and broad HTTPS host access. `externally_connectable` currently includes `shimejis.xyz` and `www.shimejis.xyz`.

The CSP explicitly permits packaged WASM through `wasm-unsafe-eval` and permits local/HTTPS connection and image paths needed by project runtime integrations.

## Extension V2 source architecture

The current `apps/extension-v2/src` tree is organized into explicit responsibilities:

- `assets` - source-managed extension assets.
- `background` - service-worker/background implementation.
- `content` - site detection, overlay, page integrations, and content features.
- `entrypoints` - WXT application and content/background entrypoints.
- `game-layer` - game-facing runtime layer.
- `lib` - extension utilities/domain helpers.
- `living-room` - living-room scene/runtime slice.
- `mascot-interactions` - typed mascot interaction adapters.
- `persistence` - world database, backups, and backup controls.
- `platform` - host/browser platform adapters.
- `shared` - extension-local shared code.
- `ui` - React application/options UI.
- `universal-objects` - universal object runtime/layer.
- `wasm` - packaged WASM-facing runtime assets/adapters.

This is a real layered architecture. New functionality should be placed according to ownership rather than growing `App.tsx`, background bootstrap, or content bootstrap into catch-all modules.

## User-facing React shell

The current `App.tsx` exposes three surface modes:

```text
panel
popup
full
```

The popup/panel and full shell share the same underlying application state while exposing different tab sets.

Current typed tab IDs are:

```text
games
collections
wishlist
playing
news
gx
mods
modauthors
foundmods
livingroom
shimejibrowser
mascotgames
achievements
cardgame
mascot
ai
```

The full surface includes Mascot Games, while the popup/panel list includes Shimeji Browser and otherwise uses the compact tab set defined in `App.tsx`.

The shell lazy-loads major feature views rather than placing all implementation into the root bundle, including:

- News Hub / News Inbox
- Collections
- GX Corner
- Mods
- Mod Authors
- Found Mods
- Living Room
- Mascot Games
- Shimeji Browser
- Achievements
- Card Game
- Mascot Studio / popup surfaces
- legacy AI surface
- Living Game Dock
- Universal Object Layer

### Routing and deep links

The shell uses hash routes such as:

```text
#tab/<tab-id>
#game/<game-key>
#cardgame
```

It also reads search parameters for creator, game, Mods, and selected mod context. Contextual actions should preserve those destination identifiers rather than opening a generic root surface.

### Library controls

The source includes search, tab filtering, multiple sorts, split/grid/compact views, image aspect/fit controls, contextual menus, game detail, collections editing, command palette, keyboard navigation, shortcuts overlay, status/progress UI, and persisted navigation/scroll state.

A rendered control is not parity proof. Use the parity matrix and real runtime checks for mutations, persistence, provider actions, and restart behavior.

## Persistence and backup layer

The Extension V2 source has a dedicated persistence area containing:

```text
WorldBackupControls.tsx
worldBackup.ts
worldDatabase.ts
```

The extension also depends on Dexie and uses typed settings/persistence helpers elsewhere in the shared/UI layers. When changing world or settings storage:

1. identify the owning storage adapter/schema;
2. preserve old data where migration is expected;
3. test write/read behavior;
4. reload the affected surface;
5. restart the browser/profile when persistence is part of the promise;
6. verify backup/export and restore behavior where relevant.

Do not infer migration success from TypeScript compilation or from one in-memory session.

## Shipping parity contract

`docs/gamesync-parity-matrix.json` defines four statuses:

- `verified` - both implementations exist and current runtime evidence exists.
- `implemented-unverified` - both implementations exist but equivalent end-to-end evidence is incomplete.
- `gap` - shipping JavaScript capability is missing or incomplete in Next.
- `implementation-specific` - a platform-specific difference is intentional and explicitly justified.

The matrix is intentionally stricter than a feature checklist.

### Representative verified capabilities on current main

The current matrix records verified evidence for capabilities including:

- stable extension identity and same-ID upgrade;
- games library shell, sorting, filtering, and detail surface;
- page/store detection and GameSync overlay;
- multi-source Found Mods discovery with packaged offscreen MiniLM/WASM reranking;
- Living Room scene surface;
- universal all-site page mascot shim;
- keyboard command center;
- offscreen transformer runtime.

The same-ID upgrade evidence records a fresh isolated Opera upgrade from `0.6.3` to `0.8.0` under the same public extension identity while preserving local, sync, and IndexedDB sentinels across restart.

### Implemented but not fully parity-proven

Examples currently marked `implemented-unverified` include:

- Collections / Wishlist / Playing mutation and persistence behavior;
- Nexus catalog/tracking/mod actions;
- Mods organizer versions/dependencies/status;
- Mod Authors and creator feeds;
- News / NewsForge / inbox feeds;
- achievements;
- card game;
- mascot runtime core;
- core Mascot Games modes;
- Shimeji Browser management;
- GX Corner;
- AI assistant;
- themes/effects;
- storage/settings migration coverage.

Do not rewrite those statuses as verified merely because the React views or typed modules exist.

### Current explicit gaps

The matrix currently identifies real product gaps including:

- complete JavaScript mascot arcade catalog parity, with several later page-game modes absent from Next;
- expanded Petz generations and ACS content/offscreen intelligence parity;
- Bounty tab/calendar workflow;
- Animation Tracker tab/tools.

These are documented gaps, not optional cleanup. A migration-complete claim must either close them with evidence or explicitly supersede them through a verified product decision.

## Clean-checkout parity behavior

Current main contains a repair ensuring the parity audit rebuilds Extension V2 before inspecting generated manifest output. This is required because a clean checkout should not depend on stale `.output` bytes already being present.

Expected loop:

1. `npm ci`.
2. Resolve current standalone `Gamesync` source.
3. Run `npm run audit:gamesync-parity`.
4. Allow the audit/build path to create current Extension V2 generated output.
5. Review `docs/gamesync-parity-matrix.json` and audit findings.
6. Fix real gaps rather than weakening the matrix.
7. Run target-specific tests.
8. Exercise the actual host and exact workflow.
9. verify persistence/restart behavior for stateful capabilities.

## Opera GX verification

The maintained verifier is `scripts/verify-extension-v2-opera.js`.

Its current defaults and behavior include:

- expected Extension V2 build: `apps/extension-v2/.output/chrome-mv3`;
- default Opera GX executable on Windows: `C:/Users/Owner/AppData/Local/Programs/Opera GX/opera.exe`;
- isolated/profile-aware execution;
- dedicated artifact/report/trace directories;
- optional existing extension ID/profile reuse;
- smoke manifest staging when using load-extension flags;
- CDP readiness and target inspection;
- real site target defaulting to the Steam Portal 2 page;
- optional deeper transformer/WASM validation with `GAMESYNC_VERIFY_TRANSFORMERS=1`;
- screenshot/trace/evidence capture;
- cleanup of the isolated runtime.

Relevant environment variables include:

```text
OPERA_GX_EXE
GAMESYNC_V2_TARGET_URL
GAMESYNC_V2_EXTENSION_ID
GAMESYNC_V2_OPERA_PROFILE
GAMESYNC_V2_ARTIFACT_DIR
GAMESYNC_V2_STAGED_EXTENSION_DIR
GAMESYNC_V2_REPORT
GAMESYNC_V2_TRACE
GAMESYNC_V2_OPERA_DEBUG_PORT
GAMESYNC_VERIFY_TRANSFORMERS
GAMESYNC_V2_PRESERVE_PROFILE
GAMESYNC_V2_USE_LOAD_EXTENSION_FLAGS
```

For Opera-specific work:

1. build the target first;
2. verify the exact loaded extension path/identity;
3. exercise popup/panel/full/content/background behavior relevant to the change;
4. inspect service-worker/background/content-script failures;
5. test page reload and browser restart when stateful;
6. verify same-ID upgrade behavior if migration identity is involved;
7. retain generated evidence rather than relying on a CDP handshake.

## Desktop host

`apps/desktop` is a React/Vite desktop application with a Tauri 2 shell.

Current commands:

```text
npm --workspace apps/desktop run dev
npm --workspace apps/desktop run build
npm --workspace apps/desktop run tauri:dev
npm --workspace apps/desktop run tauri:build
npm --workspace apps/desktop run preview
npm --workspace apps/desktop run lint
```

The desktop host consumes shared GameSync packages including core, engine, Pixi game, schema, shared logic, and UI, plus PlayCanvas. Treat browser-extension and desktop behavior as adapters over shared contracts where the source already shares ownership; do not fork feature semantics casually between hosts.

## Server host and WebSocket protocol

`apps/server` is a TypeScript WebSocket server using the shared schema and engine packages.

Current commands:

```text
npm --workspace apps/server run dev
npm --workspace apps/server run build
npm --workspace apps/server run start
```

The default port is `8787`, overridable through `PORT`. At startup the server reports the schema version.

The server is authoritative for room actions:

1. a connection receives a generated player ID;
2. `hello` checks the client's schema version and returns `welcome`;
3. `joinRoom` joins or creates a room and returns/broadcasts state;
4. `action` is validated against the shared client schema;
5. the server forces the action's `playerId` to the authenticated connection/session player;
6. `applyAction` from `@gamesync/engine` produces the next state;
7. the server broadcasts validated state to room sockets;
8. invalid JSON, invalid message shape, schema mismatch, invalid room state, and engine rejection return explicit errors.

Rooms keep player IDs for reconnect-friendly behavior while sockets exist; empty rooms are removed after the final socket disconnects. Any production persistence/matchmaking claim beyond this source behavior requires separate evidence.

## Feature Foundry workspace inside GameSync Next

`apps/feature-foundry` is a real monorepo workspace, but it is not automatically equivalent to the separate Project Constellation `PCX-043 Feature Foundry Production App` lineage.

Current commands:

```text
npm run dev:feature-foundry
npm run build:feature-foundry
npm --workspace apps/feature-foundry run preview
```

The app uses React, React Three Fiber/Drei, XYFlow, Three.js, shared GameSync logic, and project fonts/icons. Its dev server is explicitly bound to `127.0.0.1:5175`; preview uses `127.0.0.1:4175`.

Document cross-project integrations carefully. A working GameSync Next Feature Foundry surface does not prove the separate production-app recovery lineage complete, and the separate production artifact does not automatically prove this workspace current.

## Native integration surface

The repository includes:

```text
native-helper
native-host
playnite-bridge
```

Native integration claims must be verified through the actual host/bridge flow, including process/host discovery, message exchange, failure behavior, and restart persistence. Presence of source or a successful native build alone is insufficient.

## HyperBowl tooling boundary

The root manifest exposes a large HyperBowl toolchain for indexing proprietary formats, extracting assets/audio/geometry, building inventories and cross-references, capturing manual traces/memory evidence, parsing animations, exporting runtime assets, and auditing reconstructed-runtime parity.

Use the dedicated HyperBowl documentation before those operations. Many scripts are evidence/reconstruction tools, not normal GameSync Next application build steps.

## Current toolchain snapshot on main

The root manifest currently resolves/declares major tooling such as:

- React / React DOM 19.x
- Vite with root override `^8.1.3`
- Playwright / `@playwright/test`
- Oxc linting
- TypeScript 6 in affected workspaces
- Sharp
- Rapier 2D compatibility package
- Chrome Remote Interface
- WebSocket support

The Extension V2 workspace itself remains on WXT `0.21.4` and version `0.8.0`.

### Pending stack proposal, not current main

Open draft PR [#8](https://github.com/Herbertofury/GameSync-Next/pull/8) proposes a coherent Vite `8.1.3 -> 8.2.1` refresh while retaining WXT `0.21.4`. The proposal is based directly on current main and is not merged.

Its exact current proposal head is `ad76818499e02cb8fb3164c60d414954e1d9491c` in the connected PR record. The required exact-head private acceptance has not executed because the repository's hosted Actions jobs are currently failing before workflow steps receive a runner. Treat all prior branch test evidence as historical until the exact proposal head executes the required install/build/parity/Ferrum/Opera/security gates.

## Pending package-build optimization, not current main

Open draft PR [#7](https://github.com/Herbertofury/GameSync-Next/pull/7) adds package-local TypeScript incremental build state for six shared packages.

The latest successfully benchmarked implementation showed repeated warm `build:packages` measurements improving from about `11,170 ms` median to `6,741 ms` median, roughly `39.65%` faster, while the benchmark harness checked emitted-output hash equivalence, deleted-output recovery, and changed-source invalidation against a clean rebuild.

The current PR head is `b4f840bb01a77551382588ffe8c8dc01bcada892`. Later commits are primarily verification-workflow maintenance. The exact current head remains externally blocked from the severe acceptance surface, so this optimization is **not** documented as merged main behavior.

## Current infrastructure blocker affecting proposals

Current durable lead-gate evidence and current PR metadata agree on the following boundary:

- the private GameSync repositories' exact-head GitHub Actions jobs are failing before project workflow steps execute;
- affected runs show no executable step payload and prior investigation recorded no hosted runner allocation plus an account payment/spending-limit startup condition;
- no equivalent full-fidelity connected path currently proves exact private proposal build + Ferrum + Windows Opera acceptance;
- therefore branch-only or historical evidence must not be promoted into exact-current-head merge proof.

This is an infrastructure blocker, not evidence that current `main` is broken.

## Testing discipline

For changed GameSync Next behavior:

1. resolve current `main` and current shipping Gamesync baseline;
2. run the narrow changed-path regression first;
3. run applicable lint/type checks;
4. build the affected workspace;
5. run the parity audit whenever shipping behavior is involved;
6. exercise the actual affected host;
7. confirm the runtime loaded the new build rather than stale output/profile state;
8. inspect service-worker/content/page/server/native errors appropriate to the host;
9. reload/restart for stateful behavior;
10. run broader shared-package/host regressions when a cross-cutting package changed.

Do not weaken the parity matrix, skip a failing real-runtime lane, or treat a build as an end-to-end pass.

## Troubleshooting

### Parity audit fails on a clean checkout

Confirm the source includes the clean-checkout rebuild repair, install dependencies with `npm ci`, and allow the parity path to rebuild Extension V2 before inspecting generated manifest output. Do not commit stale generated output to satisfy the audit.

### Opera extension discovery fails transiently

Current main includes retry behavior for transient probe failures. Confirm the loaded source is `9e337c720f0180cffa577f140b181c699f0a1650` or a verified descendant before inventing a second discovery path.

### `npm run test:e2e-opera` fails because the test file is missing

That is a known current-main script/path mismatch. The declared target file `opera-extension/app/tests/e2e.opera-gx.test.js` is absent. Use the maintained `npm run verify:extension-v2:opera` path for current Extension V2 Opera verification. A compatibility-entrypoint fix must still pass its full candidate acceptance before the root script can be described as repaired on main.

### A feature is visible in Next but parity status is unclear

Open `docs/gamesync-parity-matrix.json`, find the capability ID, inspect its current status/reason/evidence, and run the listed/current host verification. Visible UI or typed implementation does not override an `implemented-unverified` or `gap` status.

### The wrong GameSync repository is used as parity source

The current standalone baseline is `Herbertofury/Gamesync`. Use the canonical sibling/source resolution supported by the audit and verify its head before comparing. Case-sensitive source-root handling has had explicit regression fixes.

### Extension surface opens but shows stale behavior

Verify the loaded extension build path, generated `app-*` page, extension ID/version, browser profile, and service-worker instance. Root compatibility pages redirect to generated app surfaces, so editing/observing the wrong page can create false conclusions.

### State disappears after reload or restart

Identify whether the feature is owned by browser storage, Dexie/IndexedDB, world database/backup logic, or host-specific persistence. Test the declared migration/restart contract rather than adding a second storage mechanism.

### Server reports schema mismatch

Client/server messages are validated against `@gamesync/schema` and the server checks `SchemaVersion` during `hello`. Build/update matching schema consumers rather than bypassing the version check.

### A shared-package change breaks only one host

Treat the host adapter/configuration as a first suspect while preserving the shared contract. Test all affected consumers before changing the shared behavior to fit a single host.

## Security and repository hygiene

The repository README explicitly keeps these out of Git:

- signing keys;
- API credentials;
- Steam secrets;
- browser profiles;
- `.env` files;
- generated native outputs;
- local asset vaults;
- backup archives.

Public extension identity material may remain in the manifest while private signing material stays external. Review `SECURITY.md` and `docs/REPOSITORY_SCOPE.md` before changing repository visibility or publication behavior.

## Contribution workflow

For a scoped contribution:

1. read root `AGENTS.md` and the nearest project instructions;
2. identify the owning app/package and current parity capability;
3. reproduce/record the baseline behavior;
4. make the narrowest complete change in the owning layer;
5. add or update a regression test/evidence path;
6. build/lint/typecheck the affected workspace;
7. run parity audit when the shipping product is involved;
8. run the real host flow, including reload/restart when stateful;
9. preserve generated evidence and exact source/build identity;
10. avoid unrelated dependency/framework churn.

When a capability spans extension, desktop, server, native host, or Feature Foundry, record the shared contract and each adapter instead of creating parallel incompatible implementations.

## Exact current next actions

1. Preserve current `main` and shipping Gamesync parity identity as the baseline.
2. Keep closing machine-readable parity gaps and `implemented-unverified` capabilities with paired real-runtime evidence.
3. Repair/promote the stale `test:e2e-opera` compatibility entrypoint only after a candidate passes current Ferrum and Windows Opera acceptance.
4. Keep PR #8's Vite 8.2.1 migration and PR #7's incremental package-build optimization separate from current-main documentation until their exact heads execute every required acceptance gate and are merged.
5. Continue verifying extension state across popup, panel, full page, content script, service worker, offscreen runtime, restart, and supported provider/site paths.

## Wiki maintenance

Update this page when any of the following changes materially:

- canonical repository/main head or shipping parity source;
- extension version/identity;
- app/package ownership;
- root or workspace commands;
- WXT manifest permissions/surfaces/commands;
- UI tab/workspace routing;
- persistence/schema ownership;
- parity status/gap set;
- Opera/Ferrum verification path;
- desktop/server/native host behavior;
- a pending proposal is merged/rejected/superseded;
- the current broken `test:e2e-opera` entrypoint is actually repaired on main.

Prefer project-owned source and machine-readable/runtime evidence over older prose. Do not mark migration complete while the parity matrix still carries unclosed gaps or unverified feature claims.
