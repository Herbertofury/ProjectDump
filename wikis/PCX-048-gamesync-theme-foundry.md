# GameSync Theme Foundry Wiki

**Project Constellation ID:** `PCX-048`  
**Status:** ACTIVE / TRACKED  
**Goal:** Author and package GameSync themes without drifting from Feature Foundry source contracts.  
**Current production authoring authority:** Feature Foundry `v24.0.0`, repository `Herbertofury/Feature-Foundry`, current verified head `e1ba080b5c7590f1c844a6ed13b3a471709920b9`.  
**Current GameSync host/interchange authority:** GameSync Next `main` at `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`.  
**Historical shipping/recovery authority:** GameSync `0.25.9` Theme Foundry / Feature Foundry adoption checkpoints and later durable verification material.

## Purpose

GameSync Theme Foundry is the compatibility and packaging layer between Feature Foundry-authored living worlds and the GameSync host family. Its job is not to invent a second theme system. It must preserve the semantic identity, world data, object ecology, media/sound intent, accessibility behavior, performance behavior, stable IDs, and version lineage of the source package while translating that package into explicit host capabilities and runtime adapters.

The practical contract is:

`Feature Foundry source package -> versioned interchange/adapter -> GameSync host package -> exact-host verification`

A successful export must remain round-trippable and traceable to its source. Host-specific fields may extend the package, but they must not silently redefine the source theme.

## Current authority model

There are now three distinct evidence lanes that must not be collapsed into one vague "latest theme" claim.

### 1. Feature Foundry v24.0.0 is the current production authoring/runtime authority

The released `Herbertofury/Feature-Foundry` application is now the strongest current source for the authoring-side theme/world contract.

The repository build record verifies:

- 17 approved V33 theme packages;
- 17 durable theme worlds;
- 34 rooms;
- 17 weather systems;
- 85 exact ecology objects;
- 10 current artist worlds kept as a separate authority lane;
- a typed TypeScript 7 + Vite 8 + Three.js premium runtime;
- a Tauri 2 + Rust + bundled SQLite desktop application;
- exact V24 compatibility-contract preservation;
- browser interaction/screenshot verification at 1536 x 1024;
- released source, web, Windows MSI, Windows NSIS, complete bundle, and SHA-256 artifacts.

Current Feature Foundry `src/data/theme-world-packages.json` is a real production data artifact, not only a planning document. It contains schema-versioned living-world packages and is loaded as part of the v24 authority set.

The first package, Frutiger Aero, demonstrates the current shape. It contains:

- `schemaVersion: 3`;
- stable theme ID/name;
- `packageVersion`;
- material language, world, motif, and motion identity;
- capabilities;
- visual and UI language;
- worlds and districts;
- rooms;
- weather;
- time/lighting states;
- sound intent;
- transitions;
- interactions;
- performance rules;
- accessibility rules;
- workspace presets.

This is substantially richer than a flat color-token pack and must not be reduced to one.

### 2. GameSync Next is the current host/interchange architecture authority

Current `Herbertofury/GameSync-Next` `main` at `cd906ff0831bf7fc33b41fea31b6f0c004cc1562` preserves the modular theme package family:

- `packages/theme-core`
- `packages/theme-schema`
- `packages/theme-audio`
- `packages/theme-collectibles`
- `packages/theme-devtools`
- `packages/theme-elements`
- `packages/theme-extension-bridge`
- `packages/theme-object-ecology`
- `packages/theme-react`
- `packages/theme-registry`
- `packages/theme-runtime`
- `packages/theme-scene`
- `packages/theme-sfx`
- `packages/theme-storage`
- `packages/theme-wxt`

`@gamesync/theme-core` remains explicitly host-agnostic and defines the central host-facing primitives:

- `ThemeManifest`;
- `DistrictManifestEntry`;
- settings fields and sections;
- `HostCapabilityMap`;
- `SurfaceMap`;
- `AssetManifest`;
- `SoundtrackManifest`;
- `ObjectEcologyManifest`;
- theme events;
- version helpers;
- `negotiateCapabilities()`;
- `FeatureHostBridge`.

The host capability contract currently includes Three scenes, canvas objects, soundtracks, Spotify, district variation, object ecology, side lanes, backdrop filters, view transitions, persistent audio, overlays, mascots, and voice packs.

This is the correct target for GameSync-side compatibility work. It is not yet proof that released Feature Foundry v24 directly consumes these packages.

### 3. Historical GameSync 0.25.9 evidence remains continuity evidence

The durable GameSync 0.25.9 checkpoint remains useful because it records the original Theme Foundry / Feature Foundry workspace adoption, complete-control work, and no-cap validation. Preserve it for lineage and regression comparison, but do not treat it as the current authoring implementation now that Feature Foundry v24 has a released canonical repository.

## Feature Foundry v24 production theme contract

The v24 production application is intentionally a living-world system rather than a skin switcher.

### Theme/world authority

`src/data/theme-world-packages.json` preserves the verified V33 theme-world authority inside the released product. The repository build record identifies the V33 runtime catalog SHA-256 as:

`83aac630afa4e6522d28452bb6a7c0ebe183eee6812b89b6d742662876af06ec`

The file in the canonical repository is Git blob:

`da43ce2483302d9d7b0760747eef0f1cf2fa3356`

The data must be treated as ordered, versioned product authority rather than reconstructed from visible UI labels.

### Theme package semantic layers

A complete package can carry all of the following:

1. **Identity** - stable theme ID, display name, package/schema version, aliases.
2. **Visual language** - colors, pattern, cursor, loader, celebration, ambient motifs.
3. **UI language** - material/chrome/menu/pointer/reduced-motion semantics.
4. **World topology** - worlds, districts, rooms, protected center behavior, side lanes.
5. **Environmental behavior** - weather, time, lighting, reaction inputs.
6. **Sound intent** - soundtrack mode, ambience, theme/room music behavior.
7. **Interaction language** - hover, click, drag, damage, recovery behavior.
8. **Performance contract** - scheduler, runtime destruction, motion-on-demand, physics-loop constraints.
9. **Accessibility contract** - reduced motion, keyboard objects, high contrast, focus and screen-reader status.
10. **Workspace behavior** - saved layouts, task workspaces, widths, density, inspector placement.
11. **Asset/object/editor capabilities** - Asset Vault, Object Atlas, Room Studio, full-resolution assets, ecology.

An interchange adapter must preserve these layers or explicitly mark an unsupported capability. Silently dropping one is a migration failure.

### Separate artist-world authority

Feature Foundry v24 also embeds `src/data/artist-worlds-v4.0.1.json`. These 10 artist worlds are a separate curation/database authority and must not be silently merged into the 17 durable V33 theme packages. A GameSync Theme Foundry export should therefore record the source authority lane explicitly, for example:

- `durable-theme`
- `artist-world`

A host may present both in one picker, but storage/export identity must remain distinct.

## Current Feature Foundry source layout relevant to Theme Foundry

```text
Feature-Foundry/
  package.json
  progress.md
  src/
    prototype-v24.ts
    premium.ts
    data/
      theme-world-packages.json
      artist-worlds-v4.0.1.json
    world/
    music/
    media/
    types/
  src-tauri/
  tests/
  scripts/
```

The protected V24 compatibility runtime and the newer typed premium runtime coexist. Theme Foundry integration must not bypass the exact V24 contract tests or rewrite the source data merely to match a host schema.

## Building and verifying Feature Foundry v24

From a clean checkout of `Herbertofury/Feature-Foundry`:

```powershell
npm install
npm run verify
```

The verified `verify` chain is:

```text
contract tests
-> authority tests
-> TypeScript no-emit check
-> optimized Vite build
-> cargo check for src-tauri
-> browser UI test
```

Useful development commands:

```powershell
npm run dev
npm run desktop:dev
npm run build
npm run desktop:build
npm run package
```

`npm run package` invokes the repository's deterministic PowerShell release packaging script. Do not substitute an ad-hoc ZIP and call it equivalent to the released package.

## GameSync Next host contract

### `ThemeManifest`

The current GameSync Next host manifest provides:

- stable theme ID/name/version;
- district entries;
- `hostCompatibility`;
- optional settings, assets, soundtrack, and object-ecology manifest references.

### `DistrictManifestEntry`

Districts expose:

- stable ID/name;
- soundtrack linkage;
- object tags;
- CSS hook;
- color overrides.

### Host capability negotiation

`HostCapabilityMap` makes host degradation explicit. Theme Foundry exporters should use capability negotiation rather than branching on product names or silently removing unsupported systems.

If a host lacks a required feature, the adapter should return a truthful unsupported/degraded state and an explicit fallback where one is defined.

### `FeatureHostBridge`

The bridge contract provides the host boundary for:

- mounting/unmounting feature surfaces;
- current theme state;
- soundtrack state;
- object ecology state;
- user media state;
- event delivery;
- asynchronous storage.

A Feature Foundry -> GameSync adapter should terminate at this boundary rather than reaching into host DOM internals.

## Verified current schema drift in GameSync Next

The internal GameSync Next theme package family still contains a source-backed contract defect and must not be treated as production-clean simply because the files exist.

### Field type mismatch

`packages/theme-core/src/index.ts` defines:

```text
boolean | number | string | select | color | range
```

while `packages/theme-schema/src/index.ts` validates:

```text
toggle | slider | color | select | text | number
```

The validator also refers in comments to `keybind` and `file`.

That mismatch is still present at current `main` `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`.

### Select-option mismatch

`theme-core` defines select options as:

```ts
{ label: string; value: string }[]
```

but `theme-schema` currently performs:

```ts
field.options.includes(String(value))
```

That compares a string against an array of objects instead of checking an option's `value`.

### Why this matters

Theme Foundry must not build a new interchange layer on top of an internally inconsistent host schema. Fix and verify this narrow contract first.

The package-local build paths are explicit:

```powershell
npm --prefix packages/theme-core run build
npm --prefix packages/theme-schema run build
```

`theme-core` uses `tsc -p tsconfig.json`; `theme-schema` uses `tsc -b`.

Run them from a clean GameSync Next checkout and treat compilation failures as real evidence. Do not weaken types or skip the package simply to make a root build green.

## Current integration boundary

Released Feature Foundry v24 does **not** currently declare a dependency on `@gamesync/theme-core`, `@gamesync/theme-schema`, or the other GameSync theme packages. Its production `package.json` is a standalone application dependency set centered on Tauri, Three.js, TypeScript, Vite, and the Feature Foundry runtime.

Therefore:

- Feature Foundry v24 is the current authoring/runtime authority;
- GameSync Next is the current host/interchange architecture authority;
- direct v24 -> GameSync Next package consumption is **not yet verified**;
- the adapter/migration layer is the real open integration task.

Do not claim current production parity until the adapter is implemented and exercised in both hosts.

## Recommended interchange architecture

Use a narrow adapter rather than merging schemas.

```text
Feature Foundry v24 theme-world package
        |
        v
FF v24 parser + authority validator
        |
        +--> Design-token subset export
        |
        v
Theme Foundry normalized interchange record
        |
        +--> GameSync host capability negotiation
        |
        v
GameSync Next ThemeManifest + linked manifests
        |
        v
Host runtime verification
```

The normalized record should preserve at minimum:

- source authority lane;
- source repository/head;
- source schema/package version;
- stable IDs and aliases;
- worlds/districts/rooms;
- visual/UI semantics;
- object/ecology references;
- soundtrack/media intent;
- interaction semantics;
- accessibility variants;
- performance variants;
- workspace metadata where host-relevant;
- provenance/hashes;
- unsupported-capability ledger;
- migration version.

## Design Tokens interoperability

The Design Tokens Community Group **2025.10** format remains the latest stable technical report as of August 2026. It is suitable for the design-token subset of a Feature Foundry theme: colors, dimensions, typography-style values, and other design decisions that map naturally to token semantics.

Primary source:

- https://www.designtokens.org/TR/2025.10/format/

The DTCG also publishes active preview drafts. Do not implement preview-draft changes merely because they are newer than the stable report.

CSS Color Module Level 4 remains the appropriate modern color-space reference for interoperable colors such as Oklab/OKLCH and wide-gamut output:

- https://www.w3.org/TR/css-color-4/

Design Tokens are only an interchange **subset**. Do not force rooms, weather, object ecology, mascots, soundtracks, world topology, or runtime interaction rules into generic token fields. Preserve those under explicit Feature Foundry/GameSync extension data.

## No-cap and fidelity contract

Theme Foundry must preserve the existing product-wide complete-data rules.

Forbidden shortcuts include:

- viewport admission/culling;
- first-N slicing;
- hidden pagination used as a correctness workaround;
- `content-visibility` or IntersectionObserver admission that makes off-screen content unavailable;
- lazy admission of theme/world records;
- reduced image/media quality as a performance shortcut;
- silently dropping districts, rooms, objects, provider routes, or artist worlds;
- replacing living-world runtime semantics with static wallpaper or token-only skins.

Performance work must optimize processing while preserving the full logical data set and full-fidelity output.

## Installation / operating workflow for contributors

### Feature Foundry side

1. Clone `Herbertofury/Feature-Foundry`.
2. Check out the intended source commit/tag.
3. Run `npm install`.
4. Run `npm run verify` before changing theme authority data.
5. Make a scoped source/data change.
6. Re-run `npm run verify`.
7. If desktop/runtime behavior changed, run the real Tauri desktop workflow.
8. Package only through the repository packaging path when producing release artifacts.

### GameSync Next side

1. Clone `Herbertofury/GameSync-Next`.
2. Resolve current `main` and preserve the exact head in evidence.
3. Build `theme-core` and `theme-schema` independently.
4. Repair the verified field-type and select-option contract mismatch on a scoped branch.
5. Add deterministic fixtures for all supported settings types and select values.
6. Identify and verify the actual host consumer.
7. Add the v24 adapter only after the host packages are internally consistent.
8. Run the real extension/desktop host qualification path before promotion.

## Minimum adapter regression corpus

The adapter should include fixtures covering at least:

1. Frutiger Aero durable theme package;
2. one darker/high-contrast durable theme;
3. one theme with richer object ecology;
4. one artist world from the separate v4.0.1 authority lane;
5. reduced-motion mode;
6. performance mode;
7. an unsupported-host capability case;
8. an invalid settings value;
9. a valid and invalid select value;
10. round-trip export/import with stable IDs and hashes recorded.

The corpus must compare semantic records, not only screenshots.

## Acceptance contract for production Theme Foundry integration

Before claiming the v24 -> GameSync interchange complete:

- Feature Foundry v24 `npm run verify` passes from a clean checkout;
- all 17 durable theme packages are accounted for;
- all 10 artist worlds remain separately identifiable;
- GameSync `theme-core` and `theme-schema` compile cleanly and agree on field types;
- select validation checks option values correctly;
- a versioned adapter maps v24 package data without silent field loss;
- unsupported capabilities are explicit;
- stable theme/world/district/room IDs survive the round trip;
- object ecology, sound, interaction, accessibility, performance, and workspace semantics are either preserved or explicitly marked unsupported;
- Design Tokens export/reimport preserves the token subset without pretending non-token world data is standardized;
- shipping GameSync and GameSync Next consume the intended output through explicit host adapters;
- complete-data/no-cap guarantees still pass;
- browser and desktop runtime verification use the changed build, not cached prior output;
- restart persistence is verified where theme state is persisted;
- release/package hashes are recorded for promoted artifacts.

## Troubleshooting

### Feature Foundry theme appears different after export

Compare the source `theme-world-packages.json` record against the normalized interchange record before inspecting CSS. Check stable IDs, visual/UI language, world topology, weather, sound, interaction, accessibility, and performance fields. A missing semantic field is an adapter defect.

### GameSync rejects or misreads a settings field

Check the current `theme-core` / `theme-schema` type mismatch first. Do not rename source fields opportunistically until the host contract is repaired and fixture-covered.

### Select setting rejects a valid option

Inspect `theme-schema` select validation. Current main still compares the string value against the object array rather than each option's `.value`.

### Feature Foundry build passes but GameSync package build fails

These are independent authorities and build graphs. Run package-local GameSync builds and fix the host package contract rather than changing the Feature Foundry production data to fit a broken consumer.

### Theme works in one GameSync host but not another

Compare `HostCapabilityMap`, adapter output, bridge events, storage, and host version evidence. Host-specific fallback must be explicit and must not overwrite the canonical source package.

### An artist world was treated as a durable theme

Restore the authority-lane distinction. Artist worlds come from `artist-worlds-v4.0.1.json`; durable themes come from the 17-package V33 authority embedded in v24.

### Performance optimization hides theme records or objects

Treat that as a regression. Optimize processing, batching, caching, parsing, or rendering cost without reducing the complete logical data set.

## Exact next action

1. On a scoped GameSync Next proposal branch, make `theme-core` and `theme-schema` internally consistent and add direct settings-validation fixtures.
2. Prove both packages build independently from a clean checkout at current main lineage.
3. Implement a read-only Feature Foundry v24 schema-3 adapter that consumes one durable theme package without changing the source bytes.
4. Round-trip that package through the normalized Theme Foundry record and GameSync manifest family.
5. Verify stable IDs, all semantic layers, unsupported-capability reporting, and no-cap behavior.
6. Only after that fixture is green, expand the corpus across all 17 durable themes plus a representative artist world and add the Design Tokens 2025.10 subset export.

## Evidence

### Current Feature Foundry production authority

- Repository: https://github.com/Herbertofury/Feature-Foundry
- Release: https://github.com/Herbertofury/Feature-Foundry/releases/tag/v24.0.0
- Build record: https://github.com/Herbertofury/Feature-Foundry/blob/main/progress.md
- Theme authority: https://github.com/Herbertofury/Feature-Foundry/blob/main/src/data/theme-world-packages.json
- Artist-world authority: https://github.com/Herbertofury/Feature-Foundry/blob/main/src/data/artist-worlds-v4.0.1.json

### Current GameSync Next host architecture

- Repository: https://github.com/Herbertofury/GameSync-Next
- Theme core: https://github.com/Herbertofury/GameSync-Next/blob/main/packages/theme-core/src/index.ts
- Theme schema: https://github.com/Herbertofury/GameSync-Next/blob/main/packages/theme-schema/src/index.ts

### Historical continuity

- GameSync 0.25.9 progress folder: https://drive.google.com/drive/folders/1UrjjvuaH5EJQO_-XgoOLGW-5GLN1DRom
- GameSync 0.25.9 progress checkpoint: https://drive.google.com/file/d/1urgN5SucgvyPeLSmMNGsk27v8C7D-gpD/view
- Feature Foundry North Star UI Pass 2 verification: https://drive.google.com/file/d/1GXjj44gdetrXvAjmIpctnrY7Qwd5ePzr/view

## Wiki maintenance

Update this page when any of the following changes materially:

- Feature Foundry production release/head;
- durable theme schema/package version;
- approved theme or artist-world authority counts;
- GameSync theme package contracts;
- host capability or bridge semantics;
- Feature Foundry -> GameSync adapter implementation;
- Design Tokens stable report;
- browser/desktop runtime proof;
- release hashes or packaging flow;
- complete-data/no-cap acceptance gates.

Preserve old version lineage and source-backed historical evidence when newer production authority supersedes it.