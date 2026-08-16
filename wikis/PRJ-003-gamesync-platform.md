# GameSync Platform Wiki

**Project Constellation ID:** `PRJ-003`  
**Status:** ACTIVE, multiple hosts  
**Primary current repository:** [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync)  
**Typed successor / migration repository:** [Herbertofury/GameSync-Next](https://github.com/Herbertofury/GameSync-Next)

## Purpose

GameSync is a multi-host platform centered on the shipping Opera/Chromium extension plus a typed modular successor, desktop/server hosts, shared game/theme/mascot systems, source discovery, mod intelligence, automation, and related runtime projects. Project Constellation tracks the platform as one project family because the hosts and shared feature contracts can drift if maintained independently.

The durable Project Constellation goal is to continue GameSync without losing host parity, source identity, completed work, or the relationship between the shipping extension and the newer typed implementation.

## Current verified shipping-extension repository

The connected `Herbertofury/Gamesync` repository currently identifies itself as `gamesync-extension` version **0.6.3** in `package.json`.

### Repository layout

The repository README defines the source/build contract:

- `app/` is the canonical editable extension source.
- `dist/` is generated production output and is the only directory intended to be loaded unpacked in Opera GX.
- `vite.config.ts`, `package.json`, and `node_modules/` provide build/dependency tooling.
- `scripts/`, `dev/`, `rust/`, `docs/`, and `reference/` are development-support areas.
- Root documentation currently includes `PERF_AUDIT_REPORT.md`, `RESUME_OPTIMIZATION_SUMMARY.md`, `SECURITY.md`, and `checklist.md`.

Do not edit `dist/` as the canonical source. Rebuild it from `app/`.

## Install and development setup

From a clean checkout of [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync):

1. Install a current Node.js/npm environment compatible with the checked-in lockfile and Vite configuration.
2. Run `npm ci` from the repository root.
3. Develop against `app/` and the repository-level Vite tooling.
4. Build production output with `npm run build`.
5. Load the generated `dist/` folder as the unpacked extension in Opera GX.

### Verified package scripts

```text
npm run dev
npm run build
npm run test:bounty
npm run benchmark:bounty
npm run build:wasm:legacy-accel
npm run preview
```

The current package manifest maps these to:

- `dev` -> `vite`
- `build` -> `vite build`
- `test:bounty` -> Node's test runner over `app/test/bounty/*.test.js`
- `benchmark:bounty` -> `app/test/bounty/benchmark.js`
- `build:wasm:legacy-accel` -> `wasm-pack` build of `rust/gs-legacy-accel`
- `preview` -> `vite preview`

## Current dependency surface

The current shipping repository uses Vite and includes browser/runtime dependencies for SQLite WASM, Comlink, DOM delegation, scheduling, search/indexing, IndexedDB helpers, image formats, DOM morphing, LRU caching, NLP, and web-vitals collection. The current manifest includes:

- `@sqlite.org/sqlite-wasm`
- `comlink`
- `delegate-it`
- `fastdom`
- `flexsearch`
- `idb`
- `idb-keyval`
- `libheif-js`
- `morphdom`
- `quick-lru`
- `utif`
- `web-vitals`
- `wink-eng-lite-web-model`
- `wink-nlp`

Treat the checked-in `package.json` and lockfile as the version source rather than copying dependency versions from this wiki indefinitely.

## Major platform tracks

### Shipping Opera/Chromium extension

This is the current user-facing baseline. Project Constellation records major areas including theme runtime, source discovery, mod/title identity, AutoNotes, FolderMonitor, ModAuthors, mascot systems, bounty/rewards behavior, and other extension subsystems.

### GameSync Next

`Herbertofury/GameSync-Next` is the typed modular successor and parity-migration workspace. It is not evidence that the shipping extension can be discarded. Migration work must be checked against the real shipping repository and runtime.

### Desktop and server hosts

The Next repository contains desktop/server host work. Project Constellation's preservation rule is to avoid three divergent reimplementations of shared behavior. Shared engines and schemas should remain shared where the repository architecture supports that.

### Feature Foundry relationship

GameSync theme/world behavior overlaps Feature Foundry authoring and exports. Do not assume a checked GameSync theme feature automatically proves parity with the newest Feature Foundry contract. Record source contract, host implementation, and runtime proof separately.

### HyperBowl and game/runtime subprojects

Project Constellation tracks HyperBowl reconstruction and other game/runtime work as related subprojects. Original source assets and reconstruction evidence must remain distinct from generated or Unity-derived material when authenticity matters.

### Mascot and Petz systems

Mascot, ACS, Shimeji, and PF Magic Petz work intersects GameSync. Preserve engine-specific semantics and shared-core ownership rather than flattening them into generic animation features.

## Performance and architecture evidence

The repository contains a performance audit that identifies concrete hot paths in the extension, including message-router dispatch, storage migration, content injection, mascot state reads, and settings/broadcast paths. It should be treated as optimization evidence and a backlog, not proof that every suggested optimization has already been implemented.

When modifying hot paths:

1. Reproduce the current behavior first.
2. Preserve all returned data and ordering semantics.
3. Measure before and after with the same workload.
4. Run relevant regression tests.
5. Exercise the actual extension in Opera GX.
6. Do not trade correctness, full-library availability, or feature quantity for viewport culling or hidden off-screen processing.

## Credentials and local state

The shipping repository README states that Steam, Nexus Mods, Twitch, and other user-provided credentials are read at runtime from browser-managed extension storage rather than being bundled in source/build output. Local environment files, private keys, credential exports, package-registry authentication, and generated build trees are excluded from source control.

The manifest's public extension identity key is not a private signing key. Preserve stable extension identity while keeping signing material outside the repository.

## How to modify GameSync safely

### Before editing

- Resolve whether the requested change belongs to shipping `Gamesync`, `GameSync-Next`, a shared package, a desktop/server host, or a related project.
- Record the current branch/commit and loaded extension identity.
- Establish a baseline in the real user-facing host.
- Check project instructions and relevant subsystem documentation.

### For shipping extension changes

- Edit `app/`, not generated `dist/`.
- Run the narrow regression tests for the changed subsystem.
- Run `npm run build`.
- Load the rebuilt `dist/` in Opera GX.
- Exercise the actual control/feature flow.
- Inspect extension/background/content-script errors as appropriate.
- Verify persistence after reload/restart for stateful features.

### For GameSync Next changes

Use the dedicated GameSync Next wiki. Its parity tooling is a required source of evidence when claiming a migration or replacement is equivalent to shipping GameSync.

## Host/parity ledger

Project Constellation's exact next action for this project is to preserve the host roots and maintain a ledger like:

`feature/version -> shipping Opera extension -> extension-v2 -> desktop -> Feature Foundry source -> evidence -> parity gap`

A feature should not be marked complete across the platform merely because one host renders a control or passes a local build.

## Troubleshooting

### Source change does not appear in Opera GX

Confirm that `npm run build` regenerated `dist/`, then confirm Opera GX is loading that exact `dist/` path rather than an older copy or another checkout.

### Extension ID changes unexpectedly

Check the public identity material in the manifest and confirm the correct build is loaded. Do not replace stable identity material casually.

### A feature works in Next but not shipping GameSync

Treat that as a parity gap, not as proof the shipping path is obsolete. Record it in the host/parity ledger.

### Performance fix reduces card/item availability

Treat that as a regression. Full data/card availability is part of the product contract; optimization must not hide, cap, or defer the actual collection simply because it is off-screen.

### An old checklist says a feature is done

Use the checklist as implementation history. Re-verify the current source and real runtime before using it as present-tense proof.

## Exact current next action

Preserve the known host roots and maintain one evidence-backed host/version/parity ledger so shipping GameSync, GameSync Next, desktop/server hosts, and Feature Foundry contracts cannot silently drift.

## Wiki maintenance

Update this page when the shipping extension version, source/build layout, host ownership, parity contract, major subsystem architecture, real-runtime verification process, or exact next action changes. Preserve prior validated behavior and version lineage.