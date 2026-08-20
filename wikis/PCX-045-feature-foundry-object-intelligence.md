# Feature Foundry Object Intelligence Wiki

**Project Constellation ID:** `PCX-045`  
**Status:** ACTIVE / TRACKED  
**Current production application authority:** `Feature Foundry v24.0.0`, repository `Herbertofury/Feature-Foundry`, `main` head `e1ba080b5c7590f1c844a6ed13b3a471709920b9`  
**Strongest verified detailed Object Atlas schema lineage:** `Feature Foundry V23`, Object Atlas schema `13`, build `23.0.0`  
**Historical runnable interaction/non-regression evidence:** `Feature Foundry V33 FINAL_READY`  
**Preserved maintainable-app recovery lineage:** `GameSync / Feature Foundry V2-253`; useful continuity evidence, but superseded by the released v24 repository for current production ownership

## Purpose

Object Intelligence is the Feature Foundry layer that turns visual or imported assets into stable, semantically identified, behavior-capable, provenance-preserving objects. It covers object identity, families and archetypes, variants, materials, affordances, behavior profiles, rigs and anchors, support/media surfaces, colliders, interaction semantics, source lineage, reversible derivation, placement state, mascot relationships, history, search/spatial indexing, and host/export behavior.

The key architectural rule is that **one reusable object has one stable Object Atlas identity**. Themes, districts, rooms, host adapters, and packages reference that identity. They must not silently fork a second incompatible behavior definition merely because the object appears in another theme or host.

## Evidence authority and lineage

Object Intelligence now has four evidence lanes that must not be collapsed into one claim.

### v24.0.0: current production runtime authority

`Herbertofury/Feature-Foundry` is now a complete released production repository rather than a placeholder or recovery-only checkpoint. Its package declares version `24.0.0`, and the project README describes the maintained application as TypeScript 7 + Vite 8 + Three.js/WebGL + Tauri 2 + Rust + bundled SQLite.

Current v24 production source directly owns a typed object/ecology lane:

- `src/world/themeCatalog.ts` defines `WorldObjectRecord` with stable object ID, theme ID, name, semantic role, lane preference, material, shape, affordances, damage/residue/restitution behavior, and socket profile;
- `src/data/theme-world-packages.json` is imported as verified runtime package authority;
- `src/world/ObjectEcologyLayer.ts` materializes those records as real interactive actors in the left/right living-world regions;
- `src/prototype-v24.ts` preserves the canonical V24 compatibility runtime and still contains the richer Object Atlas, object transform, pin/peel, room extraction, object interaction, History, and scrapbook behavior that the released app protects through source-contract tests;
- `src-tauri/` owns the native desktop shell and persistent native systems used by the production application;
- `tests/` and `npm run verify` protect the exact V24 source contract, authority data, TypeScript build, Rust compilation, and browser interaction path.

The production README reports **17 approved V33 theme packages and 85 exact ecology objects**. Those 85 production objects are the current runtime ecology set. They are not evidence that the richer historical V23 Object Atlas database has been reduced to 85 rows or that its 178-object schema contract has been deleted.

### V23: strongest verified detailed Object Atlas schema and interaction contract

The project-owned `feature-foundry-aesthetic-worlds-codex-master-directive-v23.md` identifies V23 as **Object Atlas and Theme Worlds schema 13** with context-aware actor commands. The paired `feature-foundry-v23-validation-report.md` records **142 passed, 0 failed** and exercises both the database contract and the executable Chromium interaction reference.

This remains the strongest recovered evidence for the detailed Object Atlas database schema, database relationship model, actor command registry, search/spatial indexes, provenance model, and object/sticker/mascot interaction contract. Current v24 source does not yet prove a one-for-one production migration of every V23 table and record.

### V33: historical runnable Feature Foundry behavior evidence

`V33 FINAL_READY` remains deeper historical product-level runnable evidence. It verifies persistent authored objects, distinct press/drag/collision/recovery paths, world signaling/replay, presentation-tier behavior, and broader Feature Foundry runtime non-regression. v24 now supersedes V33 as the current production application, but V33 remains a valuable behavior ceiling and regression fixture where v24 has not yet produced stronger equivalent evidence.

### V2-253: preserved production-app recovery lineage

The remotely byte-verified GameSync / Feature Foundry V2-253 recovery line remains useful maintainable-app continuity evidence, especially for Project Vault and project-operations history. It is no longer the current production owner because the dedicated `Herbertofury/Feature-Foundry` v24 repository is released and source-complete.

Do not silently discard V23/V33 detail merely because v24 is newer. Instead, use v24 as the production source authority and preserve V23/V33 as explicit qualification and migration baselines until equivalent current production proof exists.

## Current v24 production object model

`src/world/themeCatalog.ts` defines the current typed production object record as:

- `id`;
- `themeId`;
- `name`;
- `role`;
- `lanePreference`;
- `material`;
- `shape`;
- `affordances[]`;
- `behavior.damage`;
- `behavior.residue`;
- `behavior.restitution`;
- `socketProfile[]`.

The same module combines the durable V33-derived package catalog with artist-world data into `THEME_CATALOG`. Its diagnostics report durable theme, room, and object counts plus artist-world counts and database authority. The released README records the current durable production counts as **17 themes, 34 rooms, and 85 exact ecology objects**.

### Typed ecology runtime

`src/world/ObjectEcologyLayer.ts` turns each `WorldObjectRecord` into a real interactive button actor. Verified source behavior includes:

- loading the active theme's complete object set rather than only visible/near-visible objects;
- left/right lane routing from `lanePreference` with deterministic fallback;
- object identity, shape, and material exposed as actor data attributes;
- affordances exposed in accessible labels and titles;
- pointer selection, drag, and throw behavior;
- velocity derived from pointer movement;
- gravity, damping, edge collision, and restitution from the object record;
- keyboard activation and arrow-key movement, with Shift for the larger movement step;
- activation routing to the real media surface when an affordance references screen/video;
- activation routing to Music Hub when an affordance references music/note;
- general object-ecology events for other actions;
- theme-change reload through the `ff:premium-theme-change` event;
- diagnostics for theme, actor count, selected actor, and moving actor count.

This production layer is intentionally narrower than the full historical Object Atlas schema. It is the current typed ecology runtime, not proof that every V23 database concern has already moved into this class.

### Protected V24 compatibility runtime

The released project also preserves the original V24 imperative runtime byte-for-byte inside `src/prototype-v24.ts` and protects it with an exact source-contract test. That compatibility runtime contains richer object tooling including:

- Object Atlas selection and metadata presentation;
- object duplication, delete, repair, layer movement, lock/unlock, transform, visibility, filters, and blend behavior;
- scrapbook persistence;
- pinning and peeling;
- gravity-after-peel behavior;
- media-object behavior;
- room semantic analysis;
- extraction of detachable room actors into Object Atlas with room lineage;
- room/object affordance testing;
- context-command behavior such as Open in Object Atlas and Reveal in Layers;
- History integration for multiple object and room operations.

The production architecture therefore has two current object-related lanes: the typed premium ecology layer and the protected V24 compatibility runtime. Documentation and future refactors must keep their ownership clear until they are deliberately converged.

## v24 build, verification, and package workflow

From the canonical `Herbertofury/Feature-Foundry` repository:

```powershell
npm install
npm run verify
npm run desktop:build
npm run package
```

The package scripts define:

- `npm run test`: source-contract + authority tests;
- `npm run typecheck`: TypeScript compile check without emit;
- `npm run build`: optimized Vite production build;
- `cargo check --manifest-path src-tauri/Cargo.toml`: native Rust compile validation inside `verify`;
- `npm run test:ui`: browser interaction verification;
- `npm run desktop:build`: Tauri desktop build;
- `npm run package`: deterministic release packaging through `scripts/package-release.ps1`.

For development:

```powershell
npm run dev
npm run desktop:dev
```

Do not treat a successful TypeScript build or historical database validation as sufficient Object Intelligence qualification. Exercise the real object workflow in the built application and verify that the loaded build is the intended v24 source.

## Current v24 versus historical V23 qualification boundary

The current production repository does **not** justify rewriting the V23 schema 13 record as obsolete. Instead, maintain an explicit coverage ledger:

`V23 entity/capability -> v24 owner/representation -> migration or adapter -> current runtime proof -> preserved gap`

High-value reconciliation areas include:

- 178 historical Object Atlas archetypes/families/variants versus the 85 exact production ecology objects;
- historical material and behavior-profile depth versus the current typed `WorldObjectRecord` fields;
- historical FTS/spatial indexes versus current runtime catalog/selection behavior;
- historical provenance/derivative chains versus current production asset/package ownership;
- historical context-command registry versus current compatibility-runtime and typed-ecology command ownership;
- historical matched Object Atlas + Theme Worlds database pair versus current JSON package authority plus native SQLite systems;
- historical room-actor extraction and stable atlas identity versus current production room and ecology ownership;
- historical host/package interoperability contracts versus current v24 release/package behavior.

A difference is not automatically a regression. It becomes a regression when required behavior or data disappears without an explicit migration, replacement, or intentionally narrower production contract.

## V23 validation identity

The V23 validation report records:

- result: **PASS**;
- passed checks: **142**;
- failed checks: **0**;
- Python SQLite build: `3.46.1`;
- Object Atlas database size: `2,318,336` bytes;
- Theme Worlds database size: `1,351,680` bytes;
- Object Atlas schema version: `13`;
- Object Atlas metadata schema version: `13`;
- Object Atlas build version: `23.0.0`;
- Object Atlas recorded migrations: `13`;
- Object Atlas STRICT tables: `37`;
- Theme Worlds schema version: `13`;
- Theme Worlds build version: `23.0.0`;
- Theme Worlds recorded migrations: `13`;
- Theme Worlds STRICT tables: `42`.

Verified V23 artifact hashes:

| Artifact | SHA-256 |
| --- | --- |
| Object Atlas database | `dcf8e7000b6a32f3a0960e85d2b662d1d0d860e7f228975a35042f785bb56765` |
| Theme Worlds database | `ed4a3f97b71e5927e7a191dfc0f6dfc7f67fbc07e012bdbb4b54c8122940c468` |
| V23 prototype | `07b529aec512e0572630c802c431d3dd84b15f75a34746773ea726c1c506759d` |
| V23 master directive | `5dbe307e8bd5a1e62d9968ce43f369b6223f0483993a6a2c82d0dd298da2dc5f` |

The HTML/prototype is a verified executable interaction and composition reference. It is **not** the final Feature Foundry application or final authored-art ceiling. Production must preserve the verified interaction/data contracts while replacing demonstration art with final production assets.

## Object Atlas schema 13 verified population

The V23 database validation records these Object Atlas populations:

| Domain | Verified rows |
| --- | ---: |
| `object_archetypes` | 178 |
| `object_families` | 178 |
| `materials` | 52 |
| `behavior_profiles` | 178 |
| `object_variants` | 178 |
| `object_affordances` | 831 |
| `room_actors` | 8 |
| `object_search` | 178 |
| `object_bounds` | 178 |
| `selection_interaction_profiles` | 1 |
| `placement_physics_profiles` | 1 |
| `mascot_actor_control_profiles` | 1 |
| `mascot_actor_capabilities` | 14 |
| `actor_presentation_profiles` | 2 |
| `actor_context_menu_profiles` | 1 |
| `actor_context_menu_commands` | 20 |

Object Atlas integrity and foreign-key checks passed. FTS queries passed. The spatial index returned all `178` expected object-bound candidates.

### Cross-database relationship proof

Theme Worlds and Object Atlas are a coordinated database pair. The V23 report records **170 resolved Theme Worlds -> Object Atlas references and zero unresolved references**.

Theme Worlds schema 13 also preserves the surrounding authored context required by intelligent objects, including 17 themes, 72 districts, 17 room presets, 85 semantic surfaces, 17 mascot profiles, 14 mascot capabilities, 238 theme/mascot capability relationships, 136 mascot behavior events, 17 mascot instance presets, and five cinematic quality profiles per theme.

Do not restore or migrate one historical database independently from a different content era without explicit reconciliation.

## Canonical Object Atlas ownership boundary

The V23 directive preserves the Object Atlas database as the owner of reusable semantic identity and behavior, including:

- immutable source provenance;
- content-addressed asset records;
- derivative chains;
- tags and collections;
- material and failure profiles;
- object families, archetypes, and visual variants;
- behavior states and transitions;
- UI, object, damage, repair, and rare-event sound profiles;
- sockets;
- support surfaces;
- media surfaces;
- colliders;
- rigs and animation clips;
- user affordances;
- mascot affordances;
- theme and district compatibility;
- full-text indexes;
- spatial indexes;
- imported-room sources and semantic room actors;
- optional embeddings behind feature-gated vector search.

Theme Worlds owns authored composition and routing. It can reference an Object Atlas ID, but it must not silently redefine the object.

For current production work, treat this historical ownership model as a migration/coverage requirement, not as evidence that v24 still uses the exact same SQLite tables internally.

## Intelligent object contract

An intelligent object should preserve at least:

- stable Object Atlas identity;
- family/archetype and semantic role;
- visual variant identity;
- immutable original/source provenance;
- content hash and derivative lineage;
- material/visual DNA metadata;
- authored affordances and interaction capabilities;
- behavior/profile/state-machine identity;
- sockets, support surfaces, media surfaces, anchors/hotspots where applicable;
- collider/physics profile;
- rig/animation metadata where applicable;
- placement state separate from asset identity;
- mascot-facing capabilities where applicable;
- source and failure/repair metadata;
- theme/district/room compatibility;
- host/export compatibility;
- validation and schema/version evidence.

Do not collapse these fields into a display name, image URL, or per-theme copied behavior object.

## Content-addressed binary policy

Large images, video, audio, texture sets, Blender files, GLB files, generated atlases, and other heavy binaries do not belong as giant SQLite blobs.

The production contract is:

1. preserve the imported original unchanged;
2. stage and validate the binary;
3. hash it cryptographically;
4. write it to a content-addressed binary store;
5. record stable identity, source identity, SHA-256, content/preview URI, type/dimensions, lineage, semantic metadata, revision/approval state, and usage references in the authoritative data layer;
6. commit database/catalog references only after the binary stage succeeds.

A failed conversion or database transaction must not delete the raw source or leave an approved record pointing at missing content.

## Typed repository and SQL boundary

The historical production desktop architecture keeps authoritative database access behind the Rust/domain repository layer. React, renderers, physics, weather, audio, mascot code, and plug-ins should not issue arbitrary SQL.

The V23 directive names repository boundaries including:

- `ObjectAtlasRepository`;
- `ThemeWorldRepository`;
- `AssetImportRepository`;
- `RoomRepository`;
- `PlaylistRepository`;
- `HistoryRepository`;
- `RegistryRepository`;
- `BackupRepository`.

The purpose of this boundary is not stylistic. It keeps schema migrations, validation, history, permissions, recovery, and host behavior from leaking into ad hoc UI queries.

Current v24 uses typed TypeScript modules for the premium runtime and Rust/Tauri for native ownership. When the historical database functions move into current production, preserve the same separation of concerns even if repository/interface names change.

## Actor presentation and context-command model

Schema 13 adds explicit object/mascot presentation and command records rather than hardcoding every right-click path in UI code.

Verified historical database/runtime evidence includes:

- two presentation contracts, `mascot` and `object`;
- one shared actor context profile;
- one context-menu profile;
- **20 context-menu commands**;
- theme-native context-menu material contracts for all 17 themes;
- context menus using shared behavior without continuous background work;
- context command registry containing destructive delete and nonblocking peel paths.

### Verified executable command behavior

The V23 Chromium runtime report passed **28/28** checks. Relevant object-intelligence behavior includes:

- right-click opens the actor menu without moving or dragging the actor;
- the menu is clamped inside the viewport;
- accessible menu semantics are present;
- ordinary objects expose the expected context commands;
- **Duplicate** creates and selects a real actor;
- **Lock** changes real actor state and blocks direct manipulation;
- **Unlock** restores direct manipulation;
- **Bring to front** changes actual layer ordering;
- **Reveal in Layers** opens the exact selected layer;
- **Delete** removes the exact actor;
- Undo restores the deletion;
- Redo reapplies it;
- **Pin** converts an actor into a real sticker;
- the pinned sticker menu contextually replaces Pin with **Peel**;
- pinned state survives reload;
- sticker gravity controls gravity-after-peel rather than silently moving pinned content;
- **Peel** releases the sticker into the whole-UI actor system;
- `Shift+F10` and arrow-key menu navigation work;
- Escape closes the menu and restores focus to the actor;
- mascot menus use the mascot-specific command registry and remain edge-clamped;
- outside click closes the menu;
- normal left-button object dragging remains functional;
- no runtime page or console errors were recorded.

This interaction proof matters because Object Intelligence is not complete when only database rows exist. Commands must execute against real object state, History, persistence, layers, and selection.

## Mascot/object interaction boundary

Object Atlas schema 13 records 14 mascot actor capabilities. V23 verifies that mascot resizing is opt-in and disabled by default while rotation remains independent and enabled by default. All 17 theme mascot profiles inherit those defaults.

The presentation contract also limits automatic theme-companion clutter:

- `automaticThemeCompanions: 1`;
- `defaultSpeechBubbles: 0`;
- `maximumConcurrentSpeech: 1`;
- theme-linked companion deduplication enabled;
- user-added mascots preserved.

These constraints protect the professional workspace without deleting user-owned mascots or flattening mascot/object semantics.

## Seed-status truthfulness

A populated historical schema is not proof of finished production content. The V23 directive preserves explicit seed/status values including:

- `spec-seed`;
- `needs-production-art`;
- `needs-curation`;
- `room-template`;
- `research-only-not-installed`.

Do not hide or promote these states merely because historical validation succeeds. Current production content should replace them through the real import/review/publishing workflow while retaining provenance/history.

## Historical database build and validation workflow

The recovered V23 data bundle defines deterministic database scripts:

- `scripts/build_databases.py`
- `scripts/validate_databases.py`

Use those commands only against the matched historical data bundle that contains them. Do not imply that the current v24 repository uses those Python scripts as its primary production build.

A normal historical validation sequence is:

1. identify the matched Object Atlas + Theme Worlds source pair;
2. preserve/checkpoint the current pair;
3. run the database builder from a clean fixture/source state when rebuilding is intended;
4. run the validator;
5. require integrity and foreign-key checks for both databases;
6. require expected schema/build/migration versions;
7. require FTS and spatial-index checks;
8. require all Theme Worlds -> Object Atlas references to resolve;
9. inspect the produced database hashes and bundle manifest;
10. run the affected executable/runtime workflow rather than treating database validation as product completion.

Do not invent command-line switches that are not present in the recovered scripts.

## Migration and recovery procedure

Before every Object Atlas or paired Theme Worlds migration into current production:

1. resolve the canonical current v24 source and the exact historical matched database pair;
2. prevent concurrent writers;
3. run integrity and foreign-key preflight on the historical pair;
4. checkpoint current production source/data state;
5. create and open-test consistent backups of the data being migrated;
6. record hashes, schema versions, active content revisions, and migration provenance;
7. apply the migration or adapter change without overwriting unrelated v24 data;
8. run the complete historical database validation where applicable;
9. run `npm run verify` in the current production repository;
10. compile/open a representative world that consumes the changed object model;
11. launch the real desktop/browser runtime and exercise the affected object workflow;
12. restart and prove persistence where the operation is stateful;
13. retain a last-known-good rollback target.

Recovery must expose enough evidence to distinguish source-data failure, migration failure, current runtime failure, and packaging failure. It must not silently initialize empty replacement data or erase the released v24 authority.

## Required Object Intelligence workspaces

The long-term Feature Foundry UI contract includes database-backed workspaces for:

- Object Atlas browser;
- source/provenance inspector;
- derivative graph;
- semantic search;
- similarity search;
- material editor;
- behavior graph editor;
- socket and support-surface editor;
- collider editor;
- rig/animation editor;
- **Play With Object** sandbox;
- room-source and room-actor inspector;
- object-pool composer;
- mascot-affordance inspector;
- History integration;
- pack diff/validation;
- backup/restore/rollback tools.

The released v24 repository proves real current object/ecology behavior, but this list must not be read as a claim that every historical V23 studio workspace has already been reimplemented as a separate v24 screen. Every visible production control must call a real operation, produce truthful errors, update observable state, and persist when the operation is stateful.

## Host and package interoperability

GameSync, GameSync Next, Feature Foundry, and future hosts are intended to consume stable object IDs/data contracts through host adapters. Host limitations should produce explicit authored fallbacks rather than forked schemas or generic degraded skins.

Signed data packages may carry non-executable object metadata, recipes, verified asset bundles, district/object-pool composition, and related data. A package should declare schema version, minimum runtime, host capabilities, content hashes, dependencies, release channel, and rollback predecessor before activation.

Executable object behavior remains subject to the host runtime and plug-in capability model. Do not treat a data-pack signature as permission for arbitrary executable code.

## Troubleshooting

### Current v24 object does not appear

Confirm that the object exists in `src/data/theme-world-packages.json`, that `src/world/themeCatalog.ts` includes the package in `DURABLE_THEME_CATALOG`, and that the active premium theme is the intended one. `ObjectEcologyLayer` reloads the complete theme object set on `ff:premium-theme-change`.

### Current v24 object cannot be dragged or activated

Check `document.body.dataset.world` and the current mode. The typed ecology layer intentionally ignores direct pointer manipulation unless the world is interactive and the mode is `living` or `stage`. Also verify that another layer is not intercepting pointer input.

### Media/music affordance opens the wrong system

Inspect the object's `affordances[]`. Screen/video affordances route to `ff:open-media-surface`; music/note affordances route to `ff:open-music-hub`; other actions emit `ff:object-ecology-action`. Fix the semantic affordance record rather than adding a UI-only special case.

### Throw or collision behavior feels wrong

Verify the current `behavior.restitution` value and the typed ecology physics path before changing visual transforms. Current production physics derives velocity from pointer movement, applies gravity/damping, clamps to the whole actor lane, and uses the object record's restitution on floor/wall collision.

### Historical integrity or foreign-key validation fails

Stop promotion of the candidate historical pair. Keep the last-known-good matched databases intact, inspect the migration/source reconciliation, and fix the data or migration before trying again. Do not disable the failing check.

### Historical Theme Worlds references an unknown Object Atlas ID

Treat this as a schema/data compatibility failure. Confirm that both databases came from the same content era and migration set. Restoring only one side from an older backup is unsafe unless an explicit reconciliation migration exists.

### Object search returns stale or missing historical results

Verify schema/build version, the Object Atlas FTS/index population, and whether the object record or relevant derivative was committed successfully. Rebuild/validate through the historical project scripts rather than creating a second ad hoc search index.

### Spatial placement or hit testing is wrong

Separate historical `object_bounds`/collider metadata from current v24 lane placement and transform state. Do not rewrite visual geometry to compensate for stale spatial metadata without fixing the owning contract.

### Right-click menu moves or drags the compatibility-runtime actor

Treat this as a regression. Secondary-pointer invocation must not start ordinary drag/auto-peel behavior. Re-run the historical/V24 compatibility context-menu interaction fixture including edge clamping, keyboard invocation, outside-click closure, and normal left-drag preservation.

### Pin/Peel or Delete loses persistence/history

Re-run exact command + Undo/Redo + reload behavior in the compatibility runtime. Pinned state must survive reload, Delete must target the selected actor, and Peel must preserve the intended object/sticker history rather than silently resetting it.

### Database rows exist but the production object behaves like a static image

Check whether current v24 is consuming the intended `WorldObjectRecord` and whether the corresponding affordance route is wired. A historical seeded row or successful SQL query is not current runtime proof.

### Current v24 source conflicts with V23 schema 13

Do not pick the newer timestamp automatically and do not revert v24 to the historical app. Build the coverage ledger:

`V23 Object Atlas entity/field/command -> v24 owner/representation -> migration/adapter -> runtime proof -> preservation decision`

Preserve V23 evidence until current production proves equal behavior, a deliberate migration, or an explicit narrower contract.

## Preserved interoperability research

Khronos submitted `KHR_interactivity` for glTF 2.0 ratification in July 2026. The extension is relevant to Feature Foundry because it can represent portable behavior graphs with glTF assets. Related interaction/physics work remains less mature than Feature Foundry's internal object model.

Treat this as an **interchange experiment**, not a replacement for Object Atlas.

A narrow future experiment can map three representative Object Atlas behaviors to `KHR_interactivity` and back:

1. a selectable/toggle object;
2. an object with a bounded animation/state sequence;
3. an object whose behavior depends on a world signal/input.

Acceptance for that experiment should require stable identity, preserved supported affordance semantics, visible failure for unsupported nodes, unchanged source/provenance, no unrelated metadata mutation, bounded/replayable behavior, and no reduction in object quantity or quality.

## Exact next action

Build a **V23 -> v24 Object Intelligence coverage ledger** against the released `Herbertofury/Feature-Foundry` repository. Start with representative records that exercise:

1. stable object identity and theme linkage;
2. material/shape/semantic role;
3. affordance routing into media, music, and general ecology actions;
4. drag, keyboard movement, throw, restitution, and selection in `ObjectEcologyLayer`;
5. one compatibility-runtime context command through History and reload;
6. room-actor extraction into Object Atlas with lineage;
7. one provenance/derivative-chain case;
8. historical FTS/spatial lookup versus current production search/selection ownership;
9. matched-pair backup/restore evidence where V23 data is imported;
10. preservation or explicit migration of the historical 170 Theme Worlds -> Object Atlas references.

Run `npm run verify`, build the desktop application, exercise the representative workflows in the real loaded v24 product, restart for stateful cases, and record each V23 capability as **preserved**, **migrated**, **replaced by a stronger current contract**, or **still open**. Do not infer completeness from version number or row counts alone.

## Evidence

- current production repository: https://github.com/Herbertofury/Feature-Foundry
- current production head: `e1ba080b5c7590f1c844a6ed13b3a471709920b9`
- current production Object Ecology layer: `src/world/ObjectEcologyLayer.ts`
- current production catalog: `src/world/themeCatalog.ts`
- protected V24 compatibility runtime: `src/prototype-v24.ts`

## Wiki maintenance

Update this page when the released Feature Foundry object/ecology runtime changes, current production object counts or record fields change, a newer verified Object Atlas database/schema pair is migrated into production, current search/provenance/derivative ownership becomes explicit, actor-command behavior changes, host adapters change, or the glTF interactivity experiment produces real round-trip evidence. Preserve the V23 hashes/counts as historical validation evidence rather than rewriting lineage.