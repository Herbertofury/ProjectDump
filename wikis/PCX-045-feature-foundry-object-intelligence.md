# Feature Foundry Object Intelligence Wiki

**Project Constellation ID:** `PCX-045`  
**Status:** ACTIVE / TRACKED  
**Strongest verified Object Atlas-specific data/runtime lineage:** `Feature Foundry V23`, Object Atlas schema `13`, build `23.0.0`  
**Later runnable product evidence:** `Feature Foundry V33 FINAL_READY`, which preserves object/ecology behavior but has not been shown to supersede the V23 Object Atlas schema contract  
**Newer maintainable production-app lineage:** `GameSync / Feature Foundry V2-253`, which must be reconciled with V23 before production ownership is promoted

## Purpose

Object Intelligence is the Feature Foundry layer that turns visual or imported assets into stable, semantically identified, behavior-capable, provenance-preserving objects. It covers object identity, families and archetypes, variants, materials, affordances, behavior profiles, rigs and anchors, support/media surfaces, colliders, interaction semantics, source lineage, reversible derivation, placement state, mascot relationships, history, search/spatial indexing, and host/export behavior.

The key architectural rule is that **one reusable object has one stable Object Atlas identity**. Themes, districts, rooms, host adapters, and packages reference that identity. They must not silently fork a second incompatible behavior definition merely because the object appears in another theme or host.

## Evidence authority and lineage

Object Intelligence currently has three evidence lanes that must not be collapsed into one claim.

### V23: strongest verified Object Atlas schema and interaction contract

The project-owned `feature-foundry-aesthetic-worlds-codex-master-directive-v23.md` identifies V23 as **Object Atlas and Theme Worlds schema 13** with context-aware actor commands. The paired `feature-foundry-v23-validation-report.md` records **142 passed, 0 failed** and exercises both the database contract and the executable Chromium interaction reference.

This is the strongest recovered evidence for the detailed Object Atlas schema, database relationship model, actor command registry, and object/sticker/mascot interaction contract.

### V33: later runnable Feature Foundry behavior evidence

`V33 FINAL_READY` remains later product-level runnable evidence. It verifies persistent authored objects, distinct press/drag/collision/recovery paths, world signaling/replay, presentation-tier behavior, and broader Feature Foundry runtime non-regression. Nothing recovered in the current documentation pass proves that V33 replaced or invalidated Object Atlas schema 13, so V23 remains the authoritative detailed Object Atlas contract until a later object-specific schema is recovered and verified.

### V2-253: newer maintainable production-app source lineage

The remotely byte-verified GameSync / Feature Foundry V2-253 recovery line is newer maintainable production-app source evidence. It must be reconciled with the V23 Object Atlas database and interaction contract before production ownership is promoted. Do not silently discard the richer V23 object model because a newer app checkpoint exists, and do not describe V23 as the newest complete production application.

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

Do not restore or migrate one database independently from a different content era without explicit reconciliation.

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
5. record stable identity, source identity, SHA-256, content/preview URI, type/dimensions, lineage, semantic metadata, revision/approval state, and usage references in SQLite;
6. commit database references only after the binary stage succeeds.

A failed conversion or database transaction must not delete the raw source or leave an approved record pointing at missing content.

## Typed repository and SQL boundary

The production desktop architecture keeps authoritative database access behind the Rust/domain repository layer. React, renderers, physics, weather, audio, mascot code, and plug-ins should not issue arbitrary SQL.

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

## Actor presentation and context-command model

Schema 13 adds explicit object/mascot presentation and command records rather than hardcoding every right-click path in UI code.

Verified database/runtime evidence includes:

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

A populated schema is not proof of finished production content. The V23 directive preserves explicit seed/status values including:

- `spec-seed`;
- `needs-production-art`;
- `needs-curation`;
- `room-template`;
- `research-only-not-installed`.

Do not hide or promote these states merely because validation succeeds. Replace them through the real import/review/publishing workflow and retain provenance/history.

## Database build and validation workflow

The recovered Feature Foundry data bundle defines deterministic database scripts:

- `scripts/build_databases.py`
- `scripts/validate_databases.py`

Use the project Python environment to invoke these exact scripts. A normal validation sequence is:

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

Before every Object Atlas or paired Theme Worlds schema migration:

1. resolve the canonical matched database pair;
2. prevent concurrent writers;
3. run integrity and foreign-key preflight;
4. checkpoint WAL state;
5. create and open-test a consistent paired backup;
6. record hashes, schema versions, active content revisions, and migration provenance;
7. apply the migration;
8. run the complete database validation suite;
9. compile/open a representative world snapshot that consumes the changed object model;
10. launch the real application/reference runtime and exercise the affected object workflow;
11. restart and prove persistence;
12. retain a last-known-good rollback target.

Recovery Mode should expose read-only logs, integrity results, backup selection, export, restore, and rollback. It must not loop a failing migration or silently initialize empty replacement databases.

## Required Object Intelligence workspaces

The production Feature Foundry UI contract includes database-backed workspaces for:

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

Every visible control in those workspaces is expected to call a real typed operation, produce truthful errors, update observable state, participate in History where appropriate, and persist when the operation is stateful.

## Host and package interoperability

GameSync, GameSync Next, Feature Foundry, and future hosts are intended to consume the same stable object IDs/data contracts through host adapters. Host limitations should produce explicit authored fallbacks rather than forked schemas or generic degraded skins.

Signed data packages may carry non-executable object metadata, recipes, verified asset bundles, district/object-pool composition, and related data. A package should declare schema version, minimum runtime, host capabilities, content hashes, dependencies, release channel, and rollback predecessor before activation.

Executable object behavior remains subject to the host runtime and plug-in capability model. Do not treat a data-pack signature as permission for arbitrary executable code.

## Troubleshooting

### Integrity or foreign-key validation fails

Stop promotion of the candidate pair. Keep the last-known-good matched databases intact, inspect the migration/source reconciliation, and fix the data or migration before trying again. Do not disable the failing check.

### Theme Worlds references an unknown Object Atlas ID

Treat this as a schema/data compatibility failure. Confirm that both databases came from the same content era and migration set. Restoring only one side from an older backup is unsafe unless an explicit reconciliation migration exists.

### Object search returns stale or missing results

Verify schema/build version, the Object Atlas FTS/index population, and whether the object record or relevant derivative was committed successfully. Rebuild/validate through the project scripts rather than creating a second ad hoc search index.

### Spatial placement or hit testing is wrong

Check `object_bounds`, placement/physics profiles, collider/semantic surface metadata, and the runtime transform state separately. Do not rewrite visual geometry to compensate for stale spatial metadata without fixing the underlying contract.

### Right-click menu moves or drags the actor

Treat this as a regression. Secondary-pointer invocation must not start ordinary drag/auto-peel behavior. Re-run the V23 context-menu interaction fixture including edge clamping, keyboard invocation, outside-click closure, and normal left-drag preservation.

### Pin/Peel or Delete loses persistence/history

Re-run exact command + Undo/Redo + reload behavior. Pinned state must survive reload, Delete must target the selected actor, and Peel must preserve the intended object/sticker history rather than silently resetting it.

### Database rows exist but the object still behaves like a static image

Check whether the actual runtime is consuming the stable Object Atlas identity, affordance/behavior profile, surfaces/collider/rig metadata, and typed command path. A seeded row or successful SQL query is not runtime proof.

### Newer Feature Foundry source conflicts with V23 schema 13

Do not pick the newer timestamp automatically. Build a reconciliation ledger:

`V23 Object Atlas entity/field/command -> newer source owner -> migration/adapter -> runtime proof -> preservation decision`

Preserve V23 evidence until the newer source proves equal or stronger behavior and data coverage.

## Preserved interoperability research

Khronos submitted `KHR_interactivity` for glTF 2.0 ratification in July 2026. The extension is relevant to Feature Foundry because it can represent portable behavior graphs with glTF assets. Related interaction/physics work remains less mature than Feature Foundry's internal object model.

Treat this as an **interchange experiment**, not a replacement for Object Atlas.

A narrow future experiment can map three representative Object Atlas behaviors to `KHR_interactivity` and back:

1. a selectable/toggle object;
2. an object with a bounded animation/state sequence;
3. an object whose behavior depends on a world signal/input.

Acceptance for that experiment should require stable identity, preserved supported affordance semantics, visible failure for unsupported nodes, unchanged source/provenance, no unrelated metadata mutation, bounded/replayable behavior, and no reduction in object quantity or quality.

## Exact next action

Recover/open the exact V23 Object Atlas + Theme Worlds pair in a maintainable workspace and create a typed Object Atlas qualification fixture that exercises:

1. exact schema/build/hash identity;
2. archetype/family/variant lookup;
3. FTS and spatial lookup;
4. one material + affordance + behavior/profile read;
5. one context-command path through History and reload;
6. matched-pair backup/restore;
7. all 170 Theme Worlds -> Object Atlas references;
8. reconciliation against the newer V2-253 maintainable production-app source.

Only promote a newer production Object Atlas owner when it preserves or explicitly migrates the V23 schema/data/interaction surface and passes real runtime verification.

## Wiki maintenance

Update this page when a newer verified Object Atlas schema/database pair appears, Object Atlas counts or fields change, a later production source supersedes V23 with migration proof, Object Studio becomes a verified production runtime, actor-command behavior changes, host adapters change, or the glTF interactivity experiment produces real round-trip evidence. Preserve the V23 hashes/counts as historical validation evidence rather than rewriting lineage.