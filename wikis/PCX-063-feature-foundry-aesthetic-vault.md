# PCX-063 - Feature Foundry Aesthetic Vault

## Status

**Tracked project:** PCX-063  
**Current verified implementation name:** **Inspiration Vault**  
**Current implementation host:** `Herbertofury/GameSync-Next` on `main`  
**Primary source path:** `apps/feature-foundry/`  
**Bridge source:** `apps/extension-v2/src/entrypoints/feature-foundry-bridge/` plus `apps/extension-v2/src/background/bootstrap.ts`  
**Shared capture contract:** `packages/shared/src/featureFoundryCapture.ts`

Project Constellation originally describes this track as an Aesthetic Vault that must become a real searchable asset/aesthetic operating surface rather than an empty drawer, with persistent assets, source provenance, visual direction, capture flows, and reversible organization. Current project-owned source shows that this goal now has an implemented browser-connected Feature Foundry workspace named **Inspiration Vault**.

The separate connected repository `Herbertofury/Feature-Foundry` currently has repository size `0`. It is not the strongest implementation source for this track. The current code described below lives in the GameSync Next monorepo.

## What the Inspiration Vault does

The Inspiration Vault is Feature Foundry's browser-connected reference capture and lightweight asset-preparation workspace. It is designed to move material from the web into structured creative boards, preserve where each reference came from, and prepare selected images for downstream theme/object/sticker/world work.

The current Feature Foundry README describes the workspace as a capture studio for saving art references from the web, sorting them into boards, and running local cleanup/export passes for theme objects, sticker packs, mystery-game ideas, and broader mood worlds.

Verified current capabilities include:

- browser-extension capture of a **page**, **image**, **link**, or **selected text**;
- a dedicated Feature Foundry bridge page that transfers capture payloads from the extension into the local Feature Foundry app;
- source-provider identity and provenance fields;
- persistent local vault state;
- board-based organization;
- intent and status classification;
- pinning and tagging;
- drag/drop and manual asset use in the cleanup bench;
- local image cleanup controls;
- palette extraction;
- outline/shadow styling;
- PNG export;
- a built-in source atlas covering major visual-reference providers.

## Architecture

```text
Browser page
   |
   | right-click "Save to Feature Foundry"
   v
GameSync Extension V2 background service worker
   |
   | create FeatureFoundryBridgeCapture
   | store temporary envelope in chrome.storage.local
   v
feature-foundry-bridge extension page
   |
   | validate envelope
   | copy envelope into window.name
   | remove temporary chrome.storage.local record
   v
Feature Foundry app at http://127.0.0.1:5175/
   |
   | ?ff-workspace=inspiration-vault
   v
InspirationVaultEditor
   |
   +--> persistent vault state in localStorage
   +--> boards / tags / intent / source provenance
   +--> local cleanup bench
   +--> PNG and palette output
```

### Primary implementation files

| File | Responsibility |
| --- | --- |
| `apps/feature-foundry/README.md` | Current Feature Foundry workspace overview and verified development/build commands. |
| `apps/feature-foundry/ui/src/App.tsx` | Main Feature Foundry shell, workspace routing, and Inspiration Vault mounting. |
| `apps/feature-foundry/src/ui/editors/InspirationVaultEditor.tsx` | Vault state model, source registry, boards, capture import, cleanup bench, palette extraction, and export UI. |
| `packages/shared/src/featureFoundryCapture.ts` | Typed capture envelope, provider normalization, storage-key helpers, and workspace URL construction/parsing. |
| `apps/extension-v2/src/background/bootstrap.ts` | Context-menu registration, capture creation, temporary staging, and bridge-tab launch. |
| `apps/extension-v2/src/entrypoints/feature-foundry-bridge/main.ts` | Reads staged capture, validates it, forwards it to Feature Foundry, and cleans up temporary extension storage. |
| `apps/extension-v2/wxt.config.ts` | Extension permissions and Manifest V3 build configuration. |

## Vault data model

The current editor stores `InspirationVaultItem` records with these important fields:

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

This is important because a vault item is not just an image blob. The source URL, page URL, capture kind, provider identity, notes, tags, time, classification, and board placement are first-class state.

### Persistent storage

The current vault stores its state in browser local storage under:

```text
gamesync:feature-foundry:inspiration-vault:v1
```

The editor validates the restored object and falls back to its seed state if the stored value is missing, malformed, or does not contain an item array.

Current source proves persistence for the local Feature Foundry browser session. A separate durable database, multi-device sync service, or project-file storage layer is **not** established by the inspected implementation and should not be claimed.

## Boards

Current source defines six boards:

1. **Inbox** - fresh browser-extension and manual captures.
2. **Theme Objects** - props, interface ornaments, silhouettes, and world materials.
3. **Sticker Tray** - icons, seals, charms, badges, and cutout-ready references.
4. **Mystery Games** - unusual game references, mechanics, and unfinished-game concepts.
5. **World Thesis** - atmosphere, palette anchors, moodboards, and world-direction material.
6. **Collector Cabinet** - long-lived keeper references for later packs, apps, and extension surfaces.

The current intent taxonomy is separate from board placement and includes:

- theme object;
- sticker;
- mystery game;
- UI motif;
- palette;
- material;
- scene;
- character.

Items also carry a status of `inbox`, `processing`, `ready`, or `archive`.

## Browser capture flow

### Context menus

GameSync Extension V2 registers a root context menu named:

```text
Save to Feature Foundry
```

It exposes four concrete capture actions:

- Page into Inspiration Vault
- Image into Inspiration Vault
- Link into Inspiration Vault
- Selection into Inspiration Vault

The service worker converts the selected context into a typed `FeatureFoundryBridgeCapture` record.

### Capture contract

The shared contract supports four capture kinds:

```text
page
image
link
selection
```

Every accepted capture must include a non-empty:

- capture ID;
- title;
- page URL;
- source URL;
- capture timestamp.

The capture envelope also carries provider host/label and may include image URL, link URL, selected text, note, and tags.

The current envelope identifier is:

```text
gamesync:feature-foundry-capture:v1
```

The default Feature Foundry app URL is:

```text
http://127.0.0.1:5175/
```

and the workspace query parameter is:

```text
ff-workspace=inspiration-vault
```

### Temporary staging and handoff

The extension temporarily stages the capture envelope in `chrome.storage.local` using a key prefixed with:

```text
featureFoundryCaptureBridgeV1:
```

It then opens `feature-foundry-bridge.html?captureId=...`.

The bridge:

1. validates that a capture ID exists;
2. reads the staged envelope;
3. validates the envelope with the shared parser;
4. places the valid envelope in `window.name`;
5. removes the temporary extension-storage entry;
6. redirects to the Feature Foundry workspace URL.

The Feature Foundry shell reads `ff-workspace` during initial routing, and the Inspiration Vault editor reads and validates the capture envelope from `window.name`. The editor prevents duplicate insertion when the incoming capture ID is already present.

## Source atlas

The current Inspiration Vault source registry contains built-in guidance for these providers:

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

Each source entry records the host, category, specialties, expected capture flow, and a short use note. Categories currently include `popular`, `community`, and `gem`.

Provider labels are normalized centrally by the shared capture contract. Current special-case labels include `X`, `CARI`, and `Aesthetics Wiki`.

## Cleanup bench

The current editor includes a browser-side local cleanup bench rather than only a reference board.

Verified controls include:

- background mode:
  - none;
  - remove light;
  - remove dark;
  - remove green;
- threshold;
- brightness;
- contrast;
- saturation;
- crop transparent pixels;
- optional outline;
- outline size;
- outline color;
- shadow strength.

The editor loads images through an `HTMLImageElement` with `crossOrigin = "anonymous"` and performs pixel processing in the browser. If the host blocks pixel access, the UI explicitly tells the user to download the image and drop the local file into the bench instead.

The processed result contains:

- a generated PNG data URL;
- extracted palette values;
- output width;
- output height.

The current export action downloads the processed result as a `.png` whose filename is derived from the source label. Palette text can also be copied when clipboard access is available.

### External-tool recommendations

The editor currently names these as optional external recipes rather than built-in runtime dependencies:

- BiRefNet
- RMBG 2.0
- Segment Anything 2
- Real-ESRGAN
- SUPIR
- CLIP-style similarity
- color clustering

Do not document these as bundled Feature Foundry services unless project source later adds actual integrations.

## Running Feature Foundry

The GameSync Next monorepo uses npm workspaces.

From the repository root:

```sh
npm ci
npm run dev:feature-foundry
```

The root script builds `packages/shared` first and then starts Feature Foundry.

The verified development URL is:

```text
http://127.0.0.1:5175/
```

You can also invoke the workspace directly after dependencies/shared build requirements are satisfied:

```sh
npm --workspace apps/feature-foundry run dev
```

### Build

Preferred root command:

```sh
npm run build:feature-foundry
```

This builds the shared package and then the Feature Foundry app.

Direct workspace build:

```sh
npm --workspace apps/feature-foundry run build
```

The app's build script runs TypeScript checking followed by the Vite build.

### Preview

The app exposes:

```sh
npm --workspace apps/feature-foundry run preview
```

with a strict preview port of `4175`.

## Building the capture extension

The web-capture bridge is part of GameSync Extension V2, not the standalone Feature Foundry Vite app.

After root dependency installation, build Extension V2 with its workspace build command:

```sh
npm --workspace apps/extension-v2 run build
```

The extension manifest requests `contextMenus`, `storage`, `tabs`, and broad host access needed by the current capture path. The capture system is implemented as an MV3 service-worker flow plus an extension page, so changes must be tested in a real built extension rather than only in the Feature Foundry dev server.

## How to use the current workflow

### Capture from the browser

1. Run Feature Foundry locally on port 5175.
2. Load a current built GameSync Extension V2.
3. On a reference page, image, link, or selected text, open the browser context menu.
4. Choose **Save to Feature Foundry** and the appropriate capture subtype.
5. The extension opens its bridge page and forwards the capture into the Inspiration Vault.
6. Confirm the item appears once in the expected board and preserves source/provider fields.

### Organize a reference

Use board, intent, status, tags, notes, and pin state rather than encoding meaning into the title alone. Keep the original source URL and page URL intact so later work can trace the reference back to where it came from.

### Prepare an image

1. Load the item's image into the cleanup bench.
2. Adjust background-removal mode and threshold.
3. Tune brightness, contrast, saturation, outline, and shadow as needed.
4. Review the extracted palette.
5. Export the prepared PNG.
6. Move the result into the appropriate downstream Feature Foundry authoring flow only after verifying the resulting asset is suitable for that project.

## Modification guide

### Add a board

Update the `VaultBoardId` union and `BOARD_META` in `InspirationVaultEditor.tsx`. Then verify:

- existing stored records still load;
- the board appears in the UI;
- capture defaults remain sensible;
- moving items between boards remains reversible;
- no existing board ID is silently renamed without migration.

### Add an intent

Update the `VaultIntent` union and `INTENT_OPTIONS`. Preserve old intent values or provide a migration path before renaming them.

### Add a provider

Add a `SOURCE_REGISTRY` entry with:

- stable ID;
- display label;
- host;
- source category;
- specialties;
- expected capture flow;
- operator note.

If provider-label normalization needs a special display form, update `normalizeFeatureFoundryProviderLabel()` in `packages/shared/src/featureFoundryCapture.ts` rather than duplicating host rules inside the editor.

### Change the capture schema

The capture envelope is explicitly versioned. Schema changes must be coordinated across:

1. `packages/shared/src/featureFoundryCapture.ts`;
2. service-worker capture construction in `apps/extension-v2/src/background/bootstrap.ts`;
3. `feature-foundry-bridge/main.ts`;
4. `InspirationVaultEditor.tsx`;
5. any runtime test/fixture coverage added for the bridge.

Do not change the wire shape in only one host.

### Change the local-storage schema

The vault key is versioned as `...:v1`. A breaking stored-state change should introduce a migration or a new storage version. Do not silently discard a user's existing boards, notes, tags, pins, or provenance.

## Verification checklist

A meaningful qualification pass for this project should cover all of the following:

### Feature Foundry app

- `npm ci` completes from a clean checkout;
- `npm run build:feature-foundry` succeeds;
- the app opens at port 5175;
- `?ff-workspace=inspiration-vault` lands directly in the Inspiration Vault;
- all six boards render;
- stored items survive reload;
- board/intent/status/tag/pin changes survive reload;
- malformed stored JSON does not crash the app.

### Browser bridge

- Extension V2 builds successfully;
- **Page**, **Image**, **Link**, and **Selection** captures each create the correct capture kind;
- provider host and label are correct;
- source/page/image/link/selection fields are preserved appropriately;
- the staged extension-storage record is removed after a successful bridge handoff;
- invalid or expired captures show truthful bridge errors;
- duplicate capture IDs do not create duplicate vault items.

### Cleanup bench

- local file processing works;
- supported remote images process when CORS permits;
- blocked remote pixel access produces the documented fallback message;
- background modes materially alter pixels as intended;
- crop/brightness/contrast/saturation/outline/shadow controls change the output;
- palette extraction returns usable values;
- PNG export produces a valid image with the intended dimensions;
- repeated edits do not corrupt existing vault metadata.

## Troubleshooting

### Feature Foundry does not open

Verify the local app is running on the configured default endpoint:

```text
http://127.0.0.1:5175/
```

The current bridge contract assumes this default unless code explicitly supplies another app URL.

### The context menu is missing

Confirm you are testing a current built GameSync Extension V2 with `contextMenus` permission and that the background service worker initialized its context menus. Inspect service-worker errors rather than assuming the Feature Foundry UI is at fault.

### The bridge says "Missing capture id"

The extension page was opened without its required `captureId` query parameter. Re-run the capture through the registered context menu.

### The bridge says "Capture expired"

The staged `chrome.storage.local` envelope is absent or failed schema validation. Verify the service worker wrote the expected `featureFoundryCaptureBridgeV1:<id>` record and that producer/consumer schema versions still match.

### The vault opens but the capture is absent

Inspect:

- the `window.name` handoff;
- envelope `kind` and `version`;
- workspace ID;
- duplicate capture ID handling;
- browser console errors in Feature Foundry.

### Remote image cleanup fails

Some hosts block browser pixel access even when the image visibly loads. The current intended fallback is to download the file and use a local file/drop workflow in the cleanup bench.

### State disappears after changing storage code

Check the exact `gamesync:feature-foundry:inspiration-vault:v1` key and any migration logic. Do not solve schema issues by blindly clearing the user's vault.

## Current verification boundaries

The inspected source verifies that the Inspiration Vault, typed capture contract, context-menu producer, bridge page, local persistence, boards, provider atlas, and cleanup/export code all exist in the current GameSync Next repository.

This documentation pass does **not** claim that every context-menu capture path was freshly exercised in Opera/Chromium, that the cleanup bench was freshly pixel-compared against golden fixtures, or that vault state has a durable database/cloud/project-file backend. The Feature Foundry workspace package currently defines `lint` as a TODO echo rather than a real lint gate, and no dedicated Inspiration Vault automated test command was identified in the inspected package scripts.

Those gaps should remain explicit until runtime evidence exists.

## Highest-value next verification work

1. Run a clean `build:feature-foundry` and Extension V2 build from the same checkout.
2. Exercise all four browser capture kinds in a real Chromium/Opera runtime.
3. Verify bridge cleanup and duplicate suppression.
4. Test persistence across reload/restart with a populated multi-board vault.
5. Add automated contract tests for capture envelope parsing and bridge staging/cleanup.
6. Add focused tests for local-storage migration and duplicate IDs.
7. Add deterministic cleanup-bench image fixtures for background removal, crop, palette, outline, shadow, and export.
8. Decide whether long-term vault storage remains browser-local or moves to a project-owned durable asset database while preserving existing v1 state.

## Relationship to nearby Project Constellation tracks

- **PRJ-002 Feature Foundry** is the umbrella authoring application.
- **PCX-043 Feature Foundry Production App** covers the full production application surface.
- **PCX-045 Feature Foundry Object Intelligence** consumes or enriches object-oriented material after capture.
- **PCX-046 Feature Foundry Source Hubs** covers provider/source-adapter strategy more broadly.
- **PCX-047 Favorite Artist Worlds Database** is a structured research/database track rather than the general live capture vault.
- **PCX-059 Feature Foundry Project Brain Bridge** covers continuity/project-brain interchange, not visual-reference capture.
- **PCX-063 Feature Foundry Aesthetic Vault** is the persistent browser-connected inspiration/reference and lightweight asset-preparation workspace documented here.

Keep these ownership boundaries explicit so the Inspiration Vault does not become a duplicate of the whole Feature Foundry platform or an unstructured dumping ground.