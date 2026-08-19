# GameSync Next Wiki

**Project Constellation ID:** `PCX-042`
**Status:** ACTIVE / TRACKED
**Canonical connected repository:** [Herbertofury/GameSync-Next](https://github.com/Herbertofury/GameSync-Next)
**Default branch:** `main`
**Current verified main head:** `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`
**Extension V2 package/manifest version:** `0.8.0`
**Current shipping parity source:** [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync) at `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`

## Purpose

GameSync Next is the typed, modular successor and migration workspace for the shipping GameSync browser product. It combines a WXT/React Manifest V3 extension, desktop and WebSocket server hosts, shared packages, native integrations, Feature Foundry surfaces, game/runtime projects, Playwright/Opera verification tooling, and an executable parity system against the shipping JavaScript GameSync implementation.

The governing rule is **migration with proof, not replacement by assumption**. Shipping GameSync remains the product-surface baseline until each relevant capability is implemented and proven through current runtime evidence.

## Current source authority

The canonical source is the private `Herbertofury/GameSync-Next` repository on `main`. The current verified main head is `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`, which merged a verified recovery slice for the **Universal Game Tracker**, **Bounty**, and **Animation Tracker** while preserving the previously verified Opera discovery and parity fixes.

The current head materially supersedes the prior documentation baseline `9e337c720f0180cffa577f140b181c699f0a1650`. Bounty and Animation Tracker are no longer parity gaps on current main, and the universal Game Tracker is now a separately verified parity capability.

The standalone shipping baseline is `Herbertofury/Gamesync` at `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928` in the current durable lead-gate evidence. Do not run a parity audit against an arbitrary older GameSync checkout and treat the result as current.

Open proposal branches and pull requests are **not current product source** until merged and reverified. Current connected PR evidence now includes separate draft lanes for package-build performance, Vite, Petz persistence, the test toolchain, the React/Three UI runtime, TypeScript 7, the PlayCanvas/Tauri desktop runtime, and the broken Opera compatibility entrypoint. These are documented later as proposals and repairs, not as current-main behavior.

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

Draft PR [#15](https://github.com/Herbertofury/GameSync-Next/pull/15), current head `3046883c2575be72c320ff25364a71a46f328629`, stages a narrow compatibility entrypoint plus a regression test. It remains unmerged and cannot be described as current behavior until its exact head passes the required compatibility, parity, Ferrum, Opera GX, restart, and security acceptance surface.

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
- `docx`
- DOMPurify
- JSZip
- `linkedom`
- `mammoth`
- morphdom
- Three.js
- SheetJS `xlsx`

The document-oriented dependencies are current source requirements for the Universal Game Tracker import/export pipeline. Do not remove them as unused browser dependencies without proving the worker-backed DOCX/XLSX import/export paths still function.

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
- `features` - typed product vertical slices, now including Bounty, Animation Tracker, and Universal Game Tracker.
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

The background bootstrap now routes `BOUNTY_*`, `ANIMATION_*`, and `TRACKER_*` messages into their owning services and installs Bounty reminder plus Animation Tracker polling alarm handling. This keeps feature state and browser lifecycle behavior inside dedicated feature modules instead of embedding those contracts in the root shell.

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
bounty
tracker
ai
```

`bounty` and `tracker` are now real current-main routes. The popup/panel surface includes both Bounty and Game Tracker; the full surface also includes both while retaining Mascot Games. Animation Tracker is exposed as a specialized subview within the universal Game Tracker rather than a second top-level shell tab.

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
- Bounty
- Universal Game Tracker
- Animation Tracker through the Game Tracker workspace
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

Current examples now include:

```text
#tab/bounty
#tab/tracker
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

The Universal Game Tracker additionally owns the Dexie database `gamesync-game-tracker-v1`. Its verified model includes workspaces, records, relationships, binary assets, activity, and preferences. Tracker records use reversible archive/restore instead of a permanent-delete action in the current verified slice.

Bounty and Animation Tracker maintain their own feature-owned persisted state and alarm-driven lifecycle behavior. Do not merge those stores into generic shell state merely to simplify UI plumbing.

Do not infer migration success from TypeScript compilation or from one in-memory session.

## Universal Game Tracker

Current main includes a verified Universal Game Tracker vertical slice with public entrypoint:

```text
apps/extension-v2/src/features/game-tracker/index.ts
```

and UI entrypoint:

```text
apps/extension-v2/src/ui/app/game-tracker/index.ts
```

The background message contract currently handles:

```text
TRACKER_GET_SNAPSHOT
TRACKER_SET_PREFERENCES
TRACKER_CREATE_WORKSPACE
TRACKER_SAVE_WORKSPACE
TRACKER_UPSERT_RECORD
TRACKER_ARCHIVE_RECORD
TRACKER_RESTORE_RECORD
TRACKER_EXPORT_BUNDLE
```

### Data model

The verified tracker is not a Sims-only hardcoded database. It supports template workspaces for:

- The Sims 4
- animations
- quests
- collectibles
- mods
- custom tracking

The Sims 4 baseline includes households, individual Sims, missing households, worlds, lots, and CC/mod dependencies. Users can add typed fields and collections without changing source. Unknown spreadsheet or JSON columns are preserved through custom collections rather than being silently discarded or forced into an unrelated schema.

### Import/export

Current verified import formats include:

- `.docx`
- `.xlsx`
- `.xls`
- `.csv`
- `.tsv`
- GameSync JSON
- exact Google Docs links through the official DOCX export endpoint
- exact Google Sheets links through the official XLSX export endpoint

Current export formats include:

- lossless GameSync JSON
- multi-sheet XLSX
- editable image-aware DOCX
- active-collection CSV

DOCX import reads native Word `w:sdt` dropdown controls from `word/document.xml` alongside the visual/table parser. Selected values, complete option lists, control aliases, and source shading are preserved as tracker field schema. Single-select, multi-select, relation, and boolean values render as accessible inline pill editors.

### Worker and binary-data contract

DOCX parsing, spreadsheet parsing, relationship resolution/persistence, and document generation run in a dedicated worker. Word images remain binary `Blob` values rather than being converted to base64 across the UI boundary. Large exports remain worker-owned behind a temporary Blob URL until Opera reports the download complete.

### Merge rules

Imports merge by collection and primary identity, resolve relation names after all records exist, preserve unresolved names with warnings, and reuse identical record/field assets on repeated imports. These rules are part of the current lossless-import contract.

### Current exact Opera evidence

Separate clean isolated Opera runs imported both the supplied 43 MB local DOCX and its supplied live Google Docs URL. The verified snapshot contained:

- 181 active records
- 75 households
- 4 populated Sims
- 67 lots
- 35 worlds
- 75 relationships
- 124 schema-bound images
- 836 rendered pills

The source wardrobe options `Dirty`, `Cleaned`, `Corrupt`, `Missing CC`, and `Need Names` remained available. A `Cleaned -> Dirty` inline edit persisted. JSON, XLSX, DOCX, and CSV downloads completed and passed content checks. The React root mount count remained `1`, with zero extension console/page/request errors recorded in the acceptance run.

## Bounty in GameSync Next

Current main now contains a typed Bounty vertical slice at:

```text
apps/extension-v2/src/features/bounty/
apps/extension-v2/src/ui/app/bounty/
```

The public background contract includes:

```text
BOUNTY_GET_SNAPSHOT
BOUNTY_SYNC
BOUNTY_SET_PREFERENCES
BOUNTY_SET_CLAIM
BOUNTY_EXPORT_ICS
```

The background bootstrap routes Bounty messages and owns the Bounty reminder alarm. The verified current-main acceptance synced **107 live GamerPower records** with zero rejected rows, persisted a healthy source state, rendered the calendar, and kept the React root mounted exactly once.

This does not erase the richer shipping `Gamesync` Bounty implementation or its provider-specific history. It closes the prior GameSync Next parity gap for the Bounty tab/calendar vertical slice with current runtime evidence. Provider-by-provider equivalence beyond the verified Next slice still requires paired evidence when migration completeness is claimed.

## Animation Tracker in GameSync Next

Current main includes a typed Animation Tracker feature at:

```text
apps/extension-v2/src/features/animation-tracker/
apps/extension-v2/src/ui/app/animation-tracker/
```

The specialized creator/version/update workflow is embedded inside the Universal Game Tracker workspace.

Current message handling includes:

```text
ANIMATION_GET_SNAPSHOT
ANIMATION_GET_STATS
ANIMATION_GET_CREATORS
ANIMATION_GET_PACKS
ANIMATION_ADD_CREATOR
ANIMATION_FOLLOW_CREATOR
ANIMATION_UNFOLLOW_CREATOR
ANIMATION_ADD_PACK
ANIMATION_UPDATE_PACK
ANIMATION_START_POLL
ANIMATION_DETECT_VERSION
ANIMATION_COMPARE_VERSIONS
ANIMATION_GET_PREFS
ANIMATION_SET_PREF
ANIMATION_SET_PREFS
ANIMATION_EXPORT_DATA
ANIMATION_IMPORT_DATA
ANIMATION_INIT_DB
```

Source URLs are required to be complete HTTPS URLs. The current initialization path deliberately installs **no fabricated URL seed**. Users or imports supply verified source URLs.

The feature owns creators, packs, poll history, and preferences including auto-check interval, notifications, view mode, sorting, and tier filtering. Version detection accepts common release/version patterns and normalized semantic-like versions.

A clean isolated Opera run verified an exact HTTPS source, detected a semantic version, persisted creator/source state, polled the source, rendered an installed-pack update, and retained a single React root mount.

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
- Bounty tab and calendar workflow;
- Animation Tracker source/version/update workflow;
- Universal Game Tracker, Sims 4 baseline, relationship persistence, editable field schema, and document/spreadsheet import/export;
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

The current matrix still identifies real product gaps including:

- complete JavaScript mascot arcade catalog parity, with several later page-game modes absent from Next;
- expanded Petz generations and ACS content/offscreen intelligence parity.

Bounty and Animation Tracker are **not** current gaps on `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`; both are verified. The Universal Game Tracker is also a verified capability.

These remaining gaps are documented gaps, not optional cleanup. A migration-complete claim must either close them with evidence or explicitly supersede them through a verified product decision.

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

For Bounty, Game Tracker, or Animation Tracker changes, the maintained verifier must exercise the exact corresponding tab/subview and persistence/export/polling path rather than merely proving that the extension loaded.

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

The Extension V2 workspace itself remains on WXT `0.21.4` and version `0.8.0`. Its current tracker document pipeline also uses Dexie, `docx`, `mammoth`, `linkedom`, JSZip, and SheetJS `xlsx`.

## Current open proposal matrix, not current main

The connected repository currently has multiple independent draft proposals. They are intentionally isolated so version migrations, performance work, correctness repairs, and runtime changes can be tested and rolled back independently. All remain unmerged as of the current documentation pass.

| PR | Current head | Scope | Current proposed versions / behavior | Publication status |
| --- | --- | --- | --- | --- |
| [#7](https://github.com/Herbertofury/GameSync-Next/pull/7) | `0fdb0dbec3729d0d96c18395cf25b469b1d09a36` | shared-package build performance | package-local TypeScript incremental state for six shared packages; historical same-workload warm median improvement about 39.65% with output-equivalence and invalidation checks | draft / unmerged / exact-current-head severe proof still blocked |
| [#8](https://github.com/Herbertofury/GameSync-Next/pull/8) | `485c84fda1821aebd1cb4246d5d68987d9f5ac2f` | Vite stack | Vite `8.2.1`, `@vitejs/plugin-react` `6.0.5`, WXT retained at `0.21.4` | draft / unmerged / authoritative lock and severe proof pending |
| [#10](https://github.com/Herbertofury/GameSync-Next/pull/10) | `1b8ad1abb3c01065e03a6780d67db9e74ef11e71` | Petz persistence correctness | stable host-owned persistence identity, additive one-pet restore, legacy-save compatibility, corrupt-save fallback, awaited async teardown persistence | draft / unmerged / full exact-head Petz, host, restart, Ferrum, Opera, parity and security proof pending |
| [#11](https://github.com/Herbertofury/GameSync-Next/pull/11) | `249b03ac043970a4132dcad2d81f38ff0671d4fa` | test toolchain | Playwright family `1.63.0-alpha-2026-08-19`, Oxlint `1.79.0`, direct `ws` `8.21.3` | draft / unmerged / authoritative lock regeneration and severe proof pending |
| [#12](https://github.com/Herbertofury/GameSync-Next/pull/12) | `52afab343550c6c56a41b893ee327b42ea1514d7` | UI runtime | React / React DOM `19.2.8`, Three `0.185.1`, React Three Fiber `9.7.0`, Drei `10.7.8` | draft / unmerged / authoritative UI graph and complete host proof pending |
| [#13](https://github.com/Herbertofury/GameSync-Next/pull/13) | `b8b22d33614cc29e64b115ddd487dafc05b1341c` | TypeScript compiler | TypeScript `7.0.2` native compiler; removes the Extension V2 TypeScript 6 deprecation-suppression escape hatch | draft / unmerged / native TypeScript 7 lock graph and severe proof pending |
| [#14](https://github.com/Herbertofury/GameSync-Next/pull/14) | `088666e2d40a3bc747c8b1fd4e11e5627734fd46` | desktop runtime | PlayCanvas `2.21.4`, `@tauri-apps/cli` `2.11.4` | draft / unmerged / native Linux and Windows build/package/runtime plus Ferrum proof pending |
| [#15](https://github.com/Herbertofury/GameSync-Next/pull/15) | `3046883c2575be72c320ff25364a71a46f328629` | broken root Opera compatibility command | restores `opera-extension/app/tests/e2e.opera-gx.test.js` as a compatibility delegate to `npm run verify:extension-v2:opera` plus a focused regression | draft / unmerged / current main remains broken at `test:e2e-opera` |

Do not infer a combined future stack from these proposal branches. Each branch has its own lockfile, build, platform, browser, restart, parity, security, and stale-main acceptance requirements. When more than one proposal is eventually eligible, rebase or recreate it from then-current `main` and rerun the combined affected matrix rather than assuming individually safe branches compose automatically.

### Pending package-build optimization evidence

PR #7's implementation still has the strongest recorded same-workload package-build benchmark for the unchanged six-package idea:

- warm median: about `11,170 ms -> 6,741 ms`;
- warm p95: about `11,262 ms -> 6,798 ms`;
- cold build: about `1.71%` faster;
- emitted-output SHA-256 equivalence was checked;
- deleted-output recovery and changed-source incremental invalidation were checked against forced full rebuild behavior.

Those measurements remain historical implementation evidence. GameSync Next `main` and the proposal verification environment have changed since the benchmark, so a fresh exact-current-head run is still required before the optimization can be promoted.

### Current-main compatibility repair staging

PR #15 is a narrow repair for the missing root `test:e2e-opera` entrypoint. It does not replace the maintained Opera verifier. The intended compatibility behavior is:

```text
npm run test:e2e-opera
  -> node opera-extension/app/tests/e2e.opera-gx.test.js
  -> npm run verify:extension-v2:opera
  -> current Extension V2 build + scripts/verify-extension-v2-opera.js
```

The repair is not current until merged. On `main`, use `npm run verify:extension-v2:opera` directly.

## Current infrastructure blocker affecting proposals

Current connected PR evidence and durable lead-gate evidence agree on the following boundary:

- the private GameSync repositories' exact-head GitHub Actions jobs are still failing before project workflow steps execute on affected proposal heads;
- proposal records report no executable workflow-step payload for those failed private runs, so they are not product/test failures;
- public runner/npm execution has been demonstrated elsewhere, but cross-repository recovery cannot read the private GameSync repositories without an authorized read token such as the repository-specific recovery secret described in the proposal evidence;
- authoritative lockfile regeneration remains required for the stack migrations and must not be replaced with synthetic lock metadata;
- no equivalent full-fidelity connected path currently proves exact private proposal build + Ferrum + Windows Opera acceptance;
- therefore branch-only or historical evidence must not be promoted into exact-current-head merge proof.

This is an infrastructure blocker for affected proposal acceptance, not evidence that current `main` is broken. The `cd906ff` tracker/Bounty/Animation recovery has explicit project-owned isolated Opera evidence and remains the current-main behavior baseline.

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

For Universal Game Tracker changes, add import/export fixtures that preserve field schema, relationships, binary assets, unresolved-name warnings, repeated-import identity, and visible labels. For Bounty changes, preserve complete record admission and calendar/claim/source state. For Animation Tracker changes, prove source identity, version detection, polling, update state, import/export, and alarm behavior.

Do not weaken the parity matrix, skip a failing real-runtime lane, or treat a build as an end-to-end pass.

## Troubleshooting

### Parity audit fails on a clean checkout

Confirm the source includes the clean-checkout rebuild repair, install dependencies with `npm ci`, and allow the parity path to rebuild Extension V2 before inspecting generated manifest output. Do not commit stale generated output to satisfy the audit.

### Opera extension discovery fails transiently

Current main includes retry behavior for transient probe failures. Confirm the loaded source is `cd906ff0831bf7fc33b41fea31b6f0c004cc1562` or a verified descendant before inventing a second discovery path.

### `npm run test:e2e-opera` fails because the test file is missing

That is a known current-main script/path mismatch. The declared target file `opera-extension/app/tests/e2e.opera-gx.test.js` is absent on `main`. Use the maintained `npm run verify:extension-v2:opera` path for current Extension V2 Opera verification. Draft PR #15 stages a compatibility delegate at current proposal head `3046883c2575be72c320ff25364a71a46f328629`, but the root command is not repaired in current-main documentation until that repair is merged and reverified.

### A feature is visible in Next but parity status is unclear

Open `docs/gamesync-parity-matrix.json`, find the capability ID, inspect its current status/reason/evidence, and run the listed/current host verification. Visible UI or typed implementation does not override an `implemented-unverified` or `gap` status.

### Bounty or Tracker tab is missing

Confirm the loaded source is `cd906ff0831bf7fc33b41fea31b6f0c004cc1562` or a verified descendant, rebuild Extension V2, and verify that `App.tsx` contains `bounty` and `tracker` in the current tab union and route parser. A profile loading an older `0.8.0` build can show the same package version while missing the newer source behavior, so prove the loaded build identity rather than relying on the version string alone.

### Universal Game Tracker imports lose fields or relationships

Check the worker import path, collection/primary identity merge rule, deferred relation resolution, and unresolved-name warnings. Unknown spreadsheet/JSON columns must remain representable through custom schema/collections. Repeated imports must reuse identical record/field assets rather than multiplying them.

### DOCX dropdowns do not match the source document

Verify the native `w:sdt` control parser ran against `word/document.xml` and that visual/table parsing did not overwrite the selected value, option list, alias, or source shading. JSON should retain canonical values/schema while Office/CSV exports use visible labels.

### Animation Tracker reports the wrong version

Verify the exact HTTPS source URL, the persisted creator record, the current poll result, and the normalization/comparison result. Do not seed fabricated source URLs or infer a version from a different creator/page.

### The wrong GameSync repository is used as parity source

The current standalone baseline is `Herbertofury/Gamesync`. Use the canonical sibling/source resolution supported by the audit and verify its head before comparing. Case-sensitive source-root handling has had explicit regression fixes.

### Extension surface opens but shows stale behavior

Verify the loaded extension build path, generated `app-*` page, extension ID/version, browser profile, source commit, and service-worker instance. Root compatibility pages redirect to generated app surfaces, so editing/observing the wrong page can create false conclusions.

### State disappears after reload or restart

Identify whether the feature is owned by browser storage, Dexie/IndexedDB, the Game Tracker database, a Bounty/Animation feature store, world database/backup logic, or host-specific persistence. Test the declared migration/restart contract rather than adding a second storage mechanism.

### Server reports schema mismatch

Client/server messages are validated against `@gamesync/schema` and the server checks `SchemaVersion` during `hello`. Build/update matching schema consumers rather than bypassing the version check.

### A shared-package change breaks only one host

Treat the host adapter/configuration as a first suspect while preserving the shared contract. Test all affected consumers before changing the shared behavior to fit a single host.

### A proposal branch appears to contain a newer dependency than main

Confirm the PR number, exact head SHA, base SHA, draft/merge state, authoritative lockfile state, and required severe gates. A proposal version is not a current product dependency until the proposal is merged and the resulting mainline product passes the required build/runtime verification.

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

For tracker-related changes, preserve the dedicated feature/service/import-export boundaries and worker ownership instead of pushing document parsing, export generation, Bounty state, or Animation polling into the React shell.

For stack proposals, keep one concern per branch where practical, regenerate the real lock graph with the actual package manager, prove clean install and affected builds, then exercise every affected runtime target. Do not merge independently verified branches together without rerunning the combined acceptance surface.

## Exact current next actions

1. Preserve current `main` at `cd906ff0831bf7fc33b41fea31b6f0c004cc1562` and shipping Gamesync parity identity as the baseline.
2. Keep the newly verified Bounty, Animation Tracker, and Universal Game Tracker capability rows current while continuing to close the remaining machine-readable parity gaps.
3. Expand paired provider/runtime evidence where GameSync Next's Bounty slice is narrower than shipping GameSync's provider set.
4. Keep Universal Game Tracker import/export fixtures lossless across large DOCX/Google Docs/XLSX inputs, custom schema, relationships, assets, archive/restore, and all declared export formats.
5. Keep the broken root `test:e2e-opera` command documented as a current-main defect until PR #15 or a verified successor is merged and proves the compatibility route end-to-end.
6. Track PRs #7, #8, and #10 through #15 as proposal-only state. Update their exact heads rather than freezing stale branch SHAs in operational instructions.
7. For PRs #11 through #14, require authoritative lock regeneration plus the full affected build/runtime matrix before any dependency version becomes a current-main wiki fact.
8. Continue verifying extension state across popup, panel, full page, content script, service worker, offscreen runtime, restart, and supported provider/site paths.
9. Re-run combined acceptance if multiple proposal lanes are eventually merged or rebased together; independently successful branches do not prove the composed stack.

## Wiki maintenance

Update this page when any of the following changes materially:

- canonical repository/main head or shipping parity source;
- extension version/identity;
- app/package ownership;
- root or workspace commands;
- WXT manifest permissions/surfaces/commands;
- UI tab/workspace routing;
- Universal Game Tracker schema/import/export/worker behavior;
- Bounty or Animation Tracker service/message/alarm behavior;
- persistence/schema ownership;
- parity status/gap set;
- Opera/Ferrum verification path;
- desktop/server/native host behavior;
- a pending proposal is merged/rejected/superseded or materially changes head/scope;
- the current broken `test:e2e-opera` entrypoint is actually repaired on main.

Prefer project-owned source and machine-readable/runtime evidence over older prose. Do not mark migration complete while the parity matrix still carries unclosed gaps or unverified feature claims.
