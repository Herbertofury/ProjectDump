# PCX-063 - Feature Foundry Aesthetic Vault

## Status and authority

**Tracked project:** `PCX-063`  
**Project goal:** operate a real searchable asset/aesthetic vault rather than an empty drawer, with persistent assets, source provenance, visual DNA, hot-drop/capture flows, and reversible organization.

This project currently has **two verified implementation lanes** that solve different parts of that goal and must not be collapsed into one fictional system.

### Current production asset/runtime authority

- **Repository:** `Herbertofury/Feature-Foundry`
- **Branch:** `main`
- **Verified head:** `e1ba080b5c7590f1c844a6ed13b3a471709920b9`
- **Release/package version:** `24.0.0`
- **Current product surface:** **Asset Vault**, including the floating Object Atlas/Scrapbook/Layers/History/Environment/Room Intelligence window
- **Primary implementation:** `index.html`, `src/prototype-v24.ts`, `src/premium.ts`, `src/world/`, `src-tauri/`

Feature Foundry v24 is now the real released production application and supersedes the older claim that the standalone `Feature-Foundry` repository was empty. Its Asset Vault is the current production surface for importing, searching, inspecting, placing, pinning, transforming, and operating assets inside living worlds and the professional UI.

### Browser capture and provenance authority

- **Repository:** `Herbertofury/GameSync-Next`
- **Branch:** `main`
- **Verified head:** `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`
- **Implementation name:** **Inspiration Vault**
- **Primary app path:** `apps/feature-foundry/`
- **Bridge source:** `apps/extension-v2/src/entrypoints/feature-foundry-bridge/` and `apps/extension-v2/src/background/bootstrap.ts`
- **Shared capture contract:** `packages/shared/src/featureFoundryCapture.ts`

The GameSync Next implementation remains the strongest verified browser-to-vault capture/provenance workflow: it captures pages, images, links, and selections, preserves source/provider metadata, organizes references into boards, and includes a browser-local cleanup/export bench.

### Important boundary

Do **not** claim that Feature Foundry v24 and GameSync Next Inspiration Vault are already one unified persistence system. The production v24 Asset Vault does not currently consume the GameSync Next capture envelope, and GameSync Next's browser-local reference database is not the same storage layer as the v24 runtime's Asset Vault, scrapbook state, browser snapshot, Tauri snapshot, or SQLite database.

The correct architectural direction is additive reconciliation: preserve both proven lanes, define a versioned bridge between them, then migrate data only after round-trip and restart tests prove no loss of source metadata, imported bytes, transforms, or board state.

---

## What Feature Foundry v24 Asset Vault provides

The v24 application exposes **Asset Vault** as a first-class workspace beside Living Dashboard, Aesthetic Explorer, Room Studio, and Theme Lab.

The current UI explicitly supports:

- asset search across asset names and affordances;
- import of images, Blender files, GLB/GLTF, OBJ, FBX, and audio;
- a drag/drop import zone;
- an Asset Intelligence inspector;
- placement into the left or right living world;
- placement as a whole-UI actor;
- pinning as a scrapbook sticker to the exact UI surface under the pointer;
- floating the Vault into its own movable/resizable window;
- direct drag/drop from the floating Vault into worlds, cards, or scrapbook zones.

The normal Asset Vault workspace exposes:

```text
Asset Vault
- Search assets and affordances
- Float Vault
- Import asset
- Drop image/model/audio
- Asset grid
- Asset Intelligence inspector
- Add left
- Add right
- Place in UI
- Pin sticker
```

The floating Vault adds these tabs:

```text
Object Atlas
Mascots
Scrapbook
Layers
History
Environment
Room Intelligence
```

This makes the production surface broader than a passive asset browser: it is also a live object-placement, transformation, scrapbook, history, environment, and room-intelligence tool.

---

## Feature Foundry v24 Asset Vault architecture

```text
Feature Foundry v24
|
+-- Asset Vault workspace
|   +-- searchable asset grid
|   +-- Asset Intelligence inspector
|   +-- file/drop import
|   +-- left/right/UI/sticker placement
|
+-- Floating Asset Vault
|   +-- Object Atlas
|   +-- Mascots
|   +-- Scrapbook
|   +-- Layers
|   +-- History
|   +-- Environment
|   +-- Room Intelligence
|
+-- objectState runtime
|   +-- world objects
|   +-- UI actors
|   +-- pinned stickers
|   +-- transform/physics state
|
+-- browser persistence
|   +-- ff-floating-vault
|   +-- ff-scrapbook-layout
|   +-- ff.browser-snapshot.v1
|
+-- Tauri desktop persistence
    +-- living-world-snapshot.json
    +-- feature-foundry.sqlite3 for catalog/music/history systems
```

### Primary source ownership

| Source | Responsibility |
| --- | --- |
| `index.html` | Asset Vault workspace, floating Vault markup, tabs, drop/import surfaces, and live controls. |
| `src/prototype-v24.ts` | Asset catalog/runtime, file import, placement, drag/drop, sticker pinning, transforms, floating Vault state, scrapbook persistence, Room Intelligence extraction, self-tests. |
| `src/premium.ts` | Production diagnostics, browser snapshot, native snapshot dispatch, typed premium runtime and Tauri integration. |
| `src/world/ObjectEcologyLayer.ts` | Premium runtime object-ecology behavior separate from the V24 compatibility asset layer. |
| `src-tauri/src/lib.rs` | Native world snapshot storage under the app-data directory and Tauri runtime commands. |
| `tests/ui.test.ts` | Browser-level production verification for major Feature Foundry workspaces and runtime health. |

---

## Asset identity and runtime behavior

The v24 compatibility runtime maintains an in-memory asset catalog and lookup map used by the Asset Vault and Object Atlas. Built-in assets carry project-owned metadata such as:

- stable asset ID;
- theme/world ownership;
- display name;
- rendered art;
- semantic type;
- physics description;
- affordances;
- mascot behavior hints;
- optional media kind;
- sticker capability;
- breakability and other runtime flags.

Selected assets are surfaced through Asset Intelligence rather than treated as opaque blobs. The inspector exposes at least type, physics, affordances, and mascot behavior.

### Placement modes

The floating Vault supports three materially different placement contracts.

#### World restricted

Assets stay within a living side world and use world-coordinate placement and world collision/physics rules.

#### Whole UI

Assets live in the global UI actor layer. They can remain positioned at rest or participate in UI-aware gravity/collision behavior.

#### Scrapbook sticker

Assets pin to the exact target panel/card/UI surface under the pointer. Pinned stickers store a target key plus normalized pin coordinates and intentionally ignore ordinary gravity until peeled or changed.

The global drop handler preserves these distinctions instead of silently converting every import into one generic actor type.

---

## Scrapbook persistence

Feature Foundry v24 persists non-world actor placement under:

```text
ff-scrapbook-layout
```

The saved record includes important runtime state such as:

- `assetId`
- `scope`
- `gravity`
- `gravityAfterPeel`
- `x`, `y`
- `rotation`
- `scaleX`, `scaleY`
- `opacity`
- `blendMode`
- `locked`
- `zIndex`
- `skewX`, `skewY`
- `brightness`
- `contrast`
- `saturation`
- `hue`
- `blur`
- visibility and anchor state
- pinned-target identity and normalized pin coordinates

`restoreScrapbookState()` recreates saved actors only when their `assetId` exists in the current runtime asset catalog.

### Current imported-asset persistence gap

This is an important production limitation and should remain explicit.

Current `handleFile()` creates imported assets in memory with IDs such as:

```text
user-<timestamp>
```

Image imports are read as data URLs and inserted into the in-memory `assets`/`assetById` catalog. Non-image files are represented as an imported 3D/media placeholder with a semantic-rig-pending status.

However, the current scrapbook persistence stores **only the imported asset ID**, not the imported asset definition or file bytes. On reload, `restoreScrapbookState()` skips records whose asset ID is absent from the rebuilt catalog.

Therefore:

- built-in asset placement persistence is source-backed;
- imported asset bytes/catalog definitions are **not yet proven durable across a full reload/restart**;
- a pinned or placed user import may have a scrapbook placement record but still fail to restore because the imported asset definition was memory-only.

Do not call imported-asset persistence complete until the asset definition/blob itself is stored durably and a clean-restart test proves restoration.

---

## Floating Vault window persistence

The floating Vault window persists its geometry and minimized state separately under:

```text
ff-floating-vault
```

Stored properties include position, dimensions, and minimized state. The window can be dragged, minimized, centered, resized, and restored on reload.

This is UI-window persistence only. It must not be confused with persistence of user-imported asset bytes.

---

## Browser and native world snapshots

Feature Foundry v24 adds another persistence lane through `src/premium.ts`.

### Browser mode

`Ctrl+S` stores the current textual production state under:

```text
ff.browser-snapshot.v1
```

The snapshot includes runtime diagnostics such as mode, view, theme, world state/layout, visual quality, current object snapshots, selected state, mascots, floating-Vault-open state, catalog diagnostics, Theme Director, Music Hub, media surface, and runtime metadata.

### Tauri desktop mode

The same save action invokes:

```text
save_world_snapshot
```

The native command validates that the submitted state is valid JSON and writes:

```text
living-world-snapshot.json
```

under the platform-specific Feature Foundry application-data directory.

`load_world_snapshot` can read the file back.

### Snapshot boundary

The production snapshot serializes the **current runtime state**. It is not evidence that source files, browser-captured reference objects, imported binary asset bytes, or GameSync Inspiration Vault boards have been copied into the native database.

A real Aesthetic Vault durability layer still needs explicit asset/blob identity and provenance storage rather than relying only on scene snapshots.

---

## Room Intelligence and Object Atlas handoff

The floating Vault is integrated with Room Intelligence. Current source allows a detected room mesh to be inspected and then **added to the Object Atlas**. The produced asset is inserted into the runtime asset catalog with its source-room identity.

The room workflow also supports:

- selecting detected room meshes;
- assigning semantic roles;
- assigning physics behavior;
- testing primary actions;
- sending mascots to semantic anchors;
- placing a selected Atlas asset onto a room surface;
- showing/hiding and locking mesh mappings.

This establishes a source-backed room-to-Atlas workflow, but the same persistence rule applies: a runtime-generated asset is not automatically a durable project asset merely because it appears in the in-memory Atlas.

---

## Import behavior in Feature Foundry v24

### Accepted file classes

The main Asset Vault currently advertises:

```text
image/*
.blend
.glb
.gltf
.obj
.fbx
audio/*
```

The wider floating/mascot import path also includes additional types such as JSON, ZIP, PNG, WebP, and audio.

### Image import

Image files are read with `FileReader` and represented as borderless image actors with a data-URL visual.

Current source assigns semantic defaults equivalent to:

- imported image actor;
- 2.5D dynamic behavior;
- place / throw / resize affordances;
- mascot inspect/carry behavior.

### 3D/media import

Current generic non-image import creates an imported 3D/media runtime record whose semantic rig is still pending. That is a staging representation, not proof that arbitrary Blender/FBX/GLTF geometry is already fully parsed, rigged, persisted, and restored by the Asset Vault.

Room Intelligence has a deeper Blender/3D semantic pipeline; do not transfer those claims automatically to every generic Asset Vault import path unless the same file is actually routed through and verified by that subsystem.

---

## Production verification in Feature Foundry v24

The released package defines:

```powershell
npm install
npm run dev
npm run desktop:dev
npm run test
npm run typecheck
npm run build
npm run test:ui
npm run verify
npm run desktop:build
npm run package
```

`npm run verify` currently chains:

1. contract tests;
2. authority tests;
3. TypeScript checking;
4. optimized Vite production build;
5. `cargo check` for the Tauri application;
6. Playwright browser UI verification.

The current Playwright suite verifies major production health including the living-world layout, Frutiger and Frawgy runtime changes, Theme Atlas, Music Hub, media surface, runtime diagnostics, and zero page errors.

The V24 compatibility runtime also contains a large internal self-test. Asset/Vault-related assertions include the existence and opening of the floating Vault, whole-UI actor creation, sticker pinning, transform tools, drag assets, Room Intelligence, Object Atlas extraction, and other studio behavior.

### Missing dedicated imported-asset durability gate

The current production verification does **not** establish a dedicated clean-restart test that imports a new local asset, places or pins it, fully reloads/restarts the application, and proves both asset bytes/definition and placement return unchanged.

That should be treated as the most important current PCX-063 production gap.

---

# GameSync Next Inspiration Vault

The GameSync Next implementation remains valuable because it solves the capture/provenance half of the PCX-063 goal more explicitly than Feature Foundry v24 currently does.

## What the Inspiration Vault does

The Inspiration Vault is a browser-connected reference capture and lightweight asset-preparation workspace. Verified capabilities include:

- browser-extension capture of a page, image, link, or selected text;
- source-provider identity and provenance fields;
- a dedicated bridge page;
- persistent local reference state;
- board-based organization;
- intent/status classification;
- pinning and tagging;
- a browser-side cleanup bench;
- palette extraction;
- outline/shadow styling;
- PNG export;
- a built-in reference-provider atlas.

## Capture architecture

```text
Browser page
 |
 | right-click "Save to Feature Foundry"
 v
GameSync Extension V2 service worker
 |
 | create FeatureFoundryBridgeCapture
 | stage envelope in chrome.storage.local
 v
feature-foundry-bridge extension page
 |
 | validate envelope
 | copy envelope into window.name
 | remove staged storage record
 v
GameSync Next Feature Foundry app
 |
 | ?ff-workspace=inspiration-vault
 v
InspirationVaultEditor
 |
 +-- boards / tags / intent / provenance
 +-- local cleanup bench
 +-- palette + PNG output
```

## Capture contract

The shared contract at `packages/shared/src/featureFoundryCapture.ts` defines:

```text
workspace: inspiration-vault
query parameter: ff-workspace
window envelope kind: gamesync:feature-foundry-capture:v1
storage prefix: featureFoundryCaptureBridgeV1:
default app URL: http://127.0.0.1:5175/
```

Supported capture kinds are:

```text
page
image
link
selection
```

Every accepted capture requires:

- capture ID;
- title;
- page URL;
- source URL;
- capture timestamp.

Optional fields include image URL, link URL, selection text, note, and tags. Provider host and display label are also first-class fields.

## Inspiration Vault data model

The current `InspirationVaultItem` record includes:

- `id`
- `title`
- `boardId`
- `intent`
- `status`
- `sourceKind`
- `providerHost`
- `providerLabel`
- `sourceUrl`
- `pageUrl`
- optional `imageUrl`
- optional `linkUrl`
- optional `selectionText`
- `note`
- `tags`
- `pinned`
- `capturedAt`

This is the strongest currently verified provenance model for PCX-063. A future v24 bridge should preserve this data rather than reducing a captured reference to an image file and title.

## Inspiration Vault persistence

The GameSync Next vault persists its state under:

```text
gamesync:feature-foundry:inspiration-vault:v1
```

The editor validates restored data and falls back to seed state if the stored object is malformed.

This proves browser-local reference persistence. It does not prove native SQLite, cloud, or project-file durability.

## Boards and intent taxonomy

Current boards:

1. Inbox
2. Theme Objects
3. Sticker Tray
4. Mystery Games
5. World Thesis
6. Collector Cabinet

Current intent taxonomy:

- theme object;
- sticker;
- mystery game;
- UI motif;
- palette;
- material;
- scene;
- character.

Statuses are `inbox`, `processing`, `ready`, or `archive`.

## Source atlas

The Inspiration Vault includes built-in guidance for:

- Pinterest
- ArtStation
- Behance
- Dribbble
- DeviantArt
- Tumblr
- X
- Instagram
- Cara
- Are.na
- Savee
- CARI
- Aesthetics Wiki
- Flickr
- Cosmos

Provider records include host, category, specialties, expected capture flow, and operator notes.

## Cleanup bench

Verified controls include:

- background mode: none / remove light / remove dark / remove green;
- threshold;
- brightness;
- contrast;
- saturation;
- transparent-pixel crop;
- outline enable/size/color;
- shadow strength;
- palette extraction;
- PNG export.

Remote images are processed with browser canvas access when CORS allows it. The intended fallback for blocked pixel access is to download the image and use a local file/drop workflow.

---

## Running the two current implementation lanes

### Feature Foundry v24 production app

From `Herbertofury/Feature-Foundry`:

```powershell
npm install
npm run dev
```

Native desktop development:

```powershell
npm run desktop:dev
```

Verification and packaging:

```powershell
npm run verify
npm run desktop:build
npm run package
```

### GameSync Next Inspiration Vault

From `Herbertofury/GameSync-Next`:

```sh
npm ci
npm run dev:feature-foundry
```

Direct workspace development:

```sh
npm --workspace apps/feature-foundry run dev
```

Build:

```sh
npm run build:feature-foundry
npm --workspace apps/extension-v2 run build
```

The old GameSync Next Feature Foundry app still uses strict port `5175`; its preview uses `4175`.

---

## Recommended operator workflow today

Until the two lanes are formally bridged, use them according to their verified strengths.

### For web research and source provenance

Use GameSync Next Inspiration Vault:

1. run the GameSync Next Feature Foundry app;
2. load a current Extension V2 build;
3. use **Save to Feature Foundry** on a page/image/link/selection;
4. verify the captured provider/source fields;
5. organize into boards, intents, statuses, tags, and notes;
6. use the cleanup bench when useful;
7. export prepared PNGs when moving references toward production authoring.

### For current production world/object authoring

Use Feature Foundry v24:

1. open **Asset Vault**;
2. search or select a built-in project asset;
3. inspect its type, physics, affordances, and mascot behavior;
4. choose world, whole-UI, or scrapbook placement;
5. use the floating Vault for layers/history/environment/Room Intelligence;
6. save browser/native snapshots when appropriate;
7. treat newly imported user assets as session-scoped until imported-asset durability is fixed and restart-proven.

---

## Required bridge architecture

The safest way to converge the two implementations is a versioned additive import contract, not a destructive rewrite.

A future production bridge should preserve at least:

```text
capture identity
source URL
page URL
provider host/label
capture kind
capture timestamp
notes
user tags
board / intent / status
pinned state
original asset bytes or durable content address
processed derivative bytes
palette / visual DNA metadata
Feature Foundry production asset ID
lineage from source capture -> derivative -> production asset
```

Recommended high-level flow:

```text
GameSync capture envelope
      |
      v
validated PCX-063 import envelope
      |
      +--> immutable source/provenance record
      +--> durable binary/blob identity
      +--> optional processed derivative
      |
      v
Feature Foundry v24 Asset Vault / Object Atlas
      |
      +--> production asset identity
      +--> placement/transforms
      +--> room/world/sticker usage
```

Unknown fields should be preserved in a namespaced extension area rather than discarded during migration.

---

## Modification guide

### Change Feature Foundry v24 Asset Vault UI

Start with:

- `index.html`
- `src/prototype-v24.ts`
- corresponding CSS under `src/styles/`

Preserve the existing workspace routing, floating-window behavior, object placement modes, and V24 exact-source contract tests.

### Change v24 asset import behavior

The current import entry is `handleFile()` in `src/prototype-v24.ts`.

Any durability fix should separate:

1. immutable original file identity;
2. decoded/display representation;
3. derived/editable runtime asset metadata;
4. project placement state.

Do not solve restart persistence by embedding unbounded binary data into every scene snapshot or by silently discarding originals.

### Change scrapbook persistence

A breaking change to `ff-scrapbook-layout` requires migration. Preserve existing actor IDs when possible and do not clear a user's layout merely because a new field was added.

### Change GameSync capture schema

Coordinate changes across:

1. `packages/shared/src/featureFoundryCapture.ts`;
2. Extension V2 service-worker capture construction;
3. `feature-foundry-bridge/main.ts`;
4. `InspirationVaultEditor.tsx`;
5. bridge/capture tests.

The envelope is versioned. Do not modify only one producer or consumer.

### Add an Inspiration Vault provider

Update the source registry with stable identity, label, host, category, specialties, expected flow, and operator note. Keep provider-label normalization centralized in the shared capture package.

---

## Verification matrix

A release-worthy PCX-063 pass should eventually prove both lanes and the bridge between them.

### Feature Foundry v24 production Asset Vault

- clean `npm install`;
- `npm run verify` succeeds;
- Asset Vault is directly reachable from rail/tab/dock;
- search filters assets and affordances;
- built-in assets can be added left/right/UI/sticker;
- floating Vault can open, move, resize, minimize, center, and restore geometry;
- object transforms and pinning survive reload for built-in assets;
- Room Intelligence can extract a selected mesh into Object Atlas;
- browser snapshot and native snapshot paths remain functional;
- no console/page errors in the changed workflow.

### Imported-asset durability gate

This is currently the highest-priority missing acceptance test:

1. import one local image and one representative 3D/media file;
2. place each in at least two scopes;
3. modify transform/appearance metadata;
4. pin at least one imported asset as a sticker;
5. save state;
6. fully reload/restart the application;
7. prove the imported asset definitions and source bytes still resolve;
8. prove placements/transforms/pins remain intact;
9. prove no unknown asset IDs are silently skipped;
10. prove deleting a derived placement does not delete the immutable source asset unless the user explicitly requests that deletion.

### GameSync Inspiration Vault

- clean monorepo install/build;
- Feature Foundry app builds;
- Extension V2 builds;
- Page/Image/Link/Selection capture all work in a real Chromium/Opera extension runtime;
- staged capture storage is removed after successful handoff;
- provider/source fields survive;
- duplicate capture IDs do not duplicate records;
- multi-board state survives reload/restart;
- cleanup-bench output passes deterministic image fixtures.

### Cross-lane bridge

- every provenance field round-trips;
- original bytes retain content identity;
- processed derivatives link to originals;
- repeated import is idempotent;
- duplicate source capture does not silently fork asset identity;
- existing GameSync browser-local state is migrated without destructive overwrite;
- existing v24 placements survive the bridge upgrade;
- project export/import reproduces the same asset/provenance graph after restart.

---

## Troubleshooting

### Feature Foundry v24 Asset Vault does not show

Verify you are running the released `Herbertofury/Feature-Foundry` repository rather than the GameSync Next Feature Foundry sub-app. The production app has Asset Vault as a top-level rail/tab/dock workspace.

### Imported image appears now but disappears after restart

This matches the current source-backed durability gap. The import created an in-memory `user-<timestamp>` asset, while the scrapbook record retained only its asset ID. Do not clear unrelated storage. Preserve the source file and treat the issue as missing imported-asset catalog/blob persistence.

### Built-in sticker does not restore

Inspect `ff-scrapbook-layout`, its `assetId`, pin target key, and stored transform fields. Confirm the built-in asset still exists in the runtime catalog and the target UI surface still resolves.

### Floating Vault geometry is wrong

Inspect `ff-floating-vault`. Geometry is clamped against the current viewport during restoration. A radically smaller viewport can legitimately move or shrink the window.

### Native snapshot fails

Verify the Tauri app-data directory is writable and that the submitted snapshot is valid JSON. `save_world_snapshot` rejects malformed JSON before writing.

### Browser capture context menu is missing

This belongs to the GameSync Next bridge lane. Confirm a current Extension V2 build is loaded, `contextMenus` permission is present, and the MV3 service worker initialized successfully.

### GameSync bridge reports an expired capture

Inspect the expected `featureFoundryCaptureBridgeV1:<id>` staging record and confirm producer/consumer envelope versions still match.

### Cleanup bench cannot read remote pixels

Use the documented local-file fallback. A visible remote image is not automatically canvas-readable because CORS rules still apply.

---

## Current verified boundaries

Verified now:

- Feature Foundry v24 is a real released production repository at version `24.0.0`.
- v24 contains a first-class Asset Vault and floating Object Atlas/Scrapbook/Layers/History/Environment/Room Intelligence surface.
- built-in assets have rich runtime metadata and multiple placement modes.
- built-in non-world placement/transform/pin state has a browser-local persistence path.
- the floating Vault window has its own persisted geometry state.
- browser and Tauri world snapshots exist.
- GameSync Next still contains the typed browser-capture/provenance Inspiration Vault path at current main.

Not yet claimed:

- durable restart-safe storage of arbitrary user-imported asset definitions/bytes in Feature Foundry v24;
- automatic migration of GameSync Inspiration Vault records into Feature Foundry v24;
- a unified native database for browser-captured reference provenance and production Asset Vault bytes;
- cloud/multi-device synchronization;
- complete arbitrary Blender/FBX/GLTF semantic ingestion through the generic Asset Vault import button;
- complete current-run cross-browser qualification of all GameSync capture kinds.

These are real acceptance gaps, not reasons to discard the working systems that already exist.

---

## Highest-value next work

1. Add content-addressed durable storage for Feature Foundry v24 imported asset originals and metadata.
2. Migrate `ff-scrapbook-layout` from asset-ID-only references to durable asset identities without losing existing built-in placements.
3. Add a clean-restart imported-asset durability test to the v24 release gate.
4. Define a versioned PCX-063 bridge envelope that can ingest the existing GameSync `FeatureFoundryCaptureEnvelope` without losing provenance.
5. Preserve browser-captured source records as immutable lineage while allowing derived production assets and edits.
6. Add idempotent capture-to-production import with duplicate/source collision handling.
7. Add deterministic project export/import that includes asset graph, hashes, provenance, derivatives, placements, and visual-DNA metadata.
8. Only after those gates pass, consider retiring or merging the older GameSync Next Feature Foundry sub-app; do not remove it merely because v24 now owns the production authoring surface.

## Wiki maintenance

Update this page when Feature Foundry production Asset Vault behavior, import persistence, Object Atlas/Room Intelligence ownership, GameSync capture schema, browser bridge behavior, storage keys, native snapshot/database behavior, project export/import, build commands, or verified acceptance evidence changes. Prefer current project-owned source/runtime evidence over Project Constellation's older generic continuity summary, and preserve historical implementation lanes when they still contain capabilities not yet migrated into the current production application.
