# GameSync Platform Wiki

**Project Constellation ID:** `PRJ-003`
**Status:** ACTIVE, multiple hosts
**Primary shipping repository:** [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync)
**Typed successor / migration repository:** [Herbertofury/GameSync-Next](https://github.com/Herbertofury/GameSync-Next)

## Purpose

GameSync is a multi-host platform centered on the shipping Opera/Chromium extension plus a typed modular successor, desktop/server hosts, shared game/theme/mascot systems, source discovery, mod intelligence, automation, and related runtime projects. Project Constellation tracks the platform as one project family because the hosts and shared feature contracts can drift if maintained independently.

The durable Project Constellation goal is to continue GameSync without losing host parity, source identity, completed work, or the relationship between the shipping extension and the newer typed implementation.

## Current verified source identities

The platform currently has two distinct source authorities that must not be conflated.

### Shipping JavaScript extension

- Repository: `Herbertofury/Gamesync`
- Verified main head during this documentation pass: `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`
- Package name: `gamesync-extension`
- Package version: `0.6.3`
- Canonical editable source: `app/`
- Generated loadable extension: `dist/`

The latest shipping-repository commits are publication/security hardening rather than a product-version bump. They include required runtime/WASM artifact preservation, dependency updates, Gitleaks-based publication guardrails, and the pull-request permission correction needed by the secret-scan path. The product version remains 0.6.3.

### GameSync Next

- Repository: `Herbertofury/GameSync-Next`
- Verified main head during this documentation pass: `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`
- Monorepo package: `gamesync-monorepo`
- Extension V2 package: `gamesync-extension-v2`
- Extension V2 version: `0.8.0`
- Extension source: `apps/extension-v2/`

The current Next head is materially newer than the previous PRJ-003 wiki checkpoint. On 2026-08-18 it merged the verified recovery of the **Universal Game Tracker**, **Bounty**, **Animation Tracker**, universal mascot work, and keyboard command-center work. This is a real umbrella-level platform change and is why this page was refreshed.

## Current verified shipping-extension repository

The connected `Herbertofury/Gamesync` repository identifies itself as `gamesync-extension` version **0.6.3** in `package.json`.

### Repository layout

The repository README defines the source/build contract:

- `app/` is the canonical editable extension source.
- `dist/` is generated production output and is the only directory intended to be loaded unpacked in Opera GX.
- `vite.config.ts`, `package.json`, and `node_modules/` provide build/dependency tooling.
- `scripts/`, `dev/`, `rust/`, `docs/`, and `reference/` are development-support areas.
- Root documentation currently includes `PERF_AUDIT_REPORT.md`, `RESUME_OPTIMIZATION_SUMMARY.md`, `SECURITY.md`, and `checklist.md`.

Do not edit `dist/` as canonical source. Rebuild it from `app/`.

## Install and development setup

From a clean checkout of [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync):

1. Install a current Node.js/npm environment compatible with the checked-in lockfile and Vite configuration.
2. Run `npm ci` from the repository root.
3. Develop against `app/` and the repository-level Vite tooling.
4. Build production output with `npm run build`.
5. Load the generated `dist/` folder as the unpacked extension in Opera GX.

### Verified shipping package scripts

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

The shipping repository uses Vite and includes browser/runtime dependencies for SQLite WASM, Comlink, DOM delegation, scheduling, search/indexing, IndexedDB helpers, image formats, DOM morphing, LRU caching, NLP, and web-vitals collection. The current manifest includes:

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

## GameSync Next platform recovery now on main

The current Next main head `cd906ff0831bf7fc33b41fea31b6f0c004cc1562` merged a previously interrupted but separately exercised feature recovery. The merge commit explicitly preserves the current-main verification fixes while restoring the following slices.

### Universal Game Tracker

The typed tracker is no longer merely a planned parity item. Current source exposes it from `apps/extension-v2/src/features/game-tracker/` and routes the existing Tracker surface to the React `GameTrackerView`.

Verified design and runtime evidence recorded in the merge includes:

- Dexie database `gamesync-game-tracker-v1` for workspaces, records, relationships, binary assets, activity, and preferences;
- reversible archive/restore behavior rather than permanent-delete-first design;
- first-class Sims 4 collections for households, Sims, worlds, lots, dependencies, relationships, media, wardrobe/lot progress, placement, upload state, dates, and notes;
- universal workspace templates for animations, quests, collectibles, mods, and custom tracking;
- user-defined typed fields and collections;
- import of `.docx`, `.xlsx`, `.xls`, `.csv`, `.tsv`, GameSync JSON, and direct Google Docs/Sheets export URLs;
- preservation of native Word dropdown choices, aliases, selected values, and shading in the imported tracker schema;
- worker-owned document/spreadsheet parsing and document generation so large binary work does not have to cross the React UI boundary as base64;
- additive merge behavior keyed by collection plus primary identity;
- relationship-name resolution after record creation, with unresolved names preserved as warnings;
- repeated-import asset reuse rather than duplicate binary creation.

The exact merge evidence reports clean isolated Opera runs against both the supplied 43 MB local DOCX and its live Google Docs source. Each produced **181 active records**, including 75 households, 4 populated Sims, 67 lots, and 35 worlds; 75 relationships; 124 schema-bound images; and 836 rendered pills. A Cleaned-to-Dirty inline edit persisted, the React root remained mounted once, and JSON/XLSX/DOCX/CSV exports completed with content-level checks.

These are controlled verification results for the tested data and build, not a universal guarantee for every document shape.

### Bounty

The current Next main now owns a typed Bounty slice under:

```text
apps/extension-v2/src/features/bounty/
apps/extension-v2/src/ui/app/bounty/
```

Background routing handles `BOUNTY_*` messages and reminder alarms. The current isolated Opera evidence recorded in the merge synced **107 live GamerPower records**, retained a healthy source state, rendered the calendar, and preserved a single React root mount.

The shipping GameSync Bounty runtime remains broader in provider scope. Do not treat the typed Next slice as evidence that every shipping Bounty provider and Twitch/Steam/Battle.net behavior has been migrated. Use the dedicated Bounty wiki for the provider-by-provider boundary.

### Animation Tracker

The typed Animation Tracker is now present under:

```text
apps/extension-v2/src/features/animation-tracker/
apps/extension-v2/src/ui/app/animation-tracker/
```

The source defines creators, packs, polling history, preferences, version detection/comparison, HTTPS-only source validation, follow/unfollow operations, installed-version tracking, update-available state, and periodic polling.

The current merge evidence records an isolated Opera run that polled an exact HTTPS source, detected a semantic version, and rendered an available installed-pack update without remounting the React root.

### Universal page mascot and command center

The current parity matrix records the universal page mascot bootstrap as verified in Next on an unrelated HTTP page, including SPA route continuity, settings restoration, and proof that the full overlay runtime was not loaded for the lightweight mascot path.

The keyboard command center is also recorded as verified: the configured `Ctrl+Shift+K` command opens or focuses the canonical full surface and the tested Opera run rendered 23 commands while preserving one root mount.

## Executable cross-repository parity contract

GameSync platform parity is now enforced by a real repository-owned audit rather than only by a prose checklist.

Run from the GameSync Next monorepo root:

```text
npm run audit:gamesync-parity
```

The audit script performs these steps:

1. rebuilds Extension V2 before inspecting generated manifest output;
2. resolves the shipping JavaScript GameSync source, preferring an explicit `GAMESYNC_JS_APP_PATH` and then known sibling/recovered source locations;
3. loads `docs/gamesync-parity-matrix.json`;
4. verifies every declared implementation-reference path exists;
5. compares shipping and Next extension identity keys;
6. extracts popup/full-page tab IDs from shipping HTML and Next React source;
7. compares manifest commands;
8. distinguishes declared parity gaps from undeclared tab/command gaps;
9. writes `output/parity/gamesync-parity-report.json`.

The report has two different success concepts:

- `ok` means the audit's structural/identity/reference checks pass and no undeclared tab or command gaps were found.
- `parityComplete` becomes true only when there are **zero** `gap` and **zero** `implemented-unverified` capabilities.

This distinction matters. A clean structural audit does not mean the typed successor can replace shipping GameSync. The current parity matrix still intentionally contains verified, implemented-unverified, gap, and implementation-specific entries.

### Relevant Next verification commands

The monorepo exposes these verified routes for platform work:

```text
npm run build
npm run verify:extension-v2:opera
npm run audit:gamesync-parity
npm run pw:test:opera-extension
npm run test:extension-regression
```

For direct Extension V2 work, the package itself exposes:

```text
npm --workspace apps/extension-v2 run build
npm --workspace apps/extension-v2 run verify:opera
npm --workspace apps/extension-v2 run verify:same-id-upgrade
npm --workspace apps/extension-v2 run verify:offscreen-runtime
```

The 0.8.0 Extension V2 build uses WXT and React and currently includes Dexie, DOMPurify, JSZip, LinkeDOM, Mammoth, Morphdom, Three.js, `docx`, and SheetJS/XLSX support relevant to the recovered tracker/import/export surface.

## Major platform tracks

### Shipping Opera/Chromium extension

This remains the shipping user-facing baseline. Project Constellation records major areas including theme runtime, source discovery, mod/title identity, AutoNotes, FolderMonitor, ModAuthors, mascot systems, bounty/rewards behavior, and other extension subsystems.

### GameSync Next

`Herbertofury/GameSync-Next` is the typed modular successor and parity-migration workspace. It now has materially verified feature recovery on current main, but it is still **not** evidence that shipping GameSync can be discarded. Migration decisions must be checked against the real shipping repository, current parity matrix, and paired runtime evidence.

### Desktop and server hosts

The Next repository contains desktop/server host work and shared packages. Project Constellation's preservation rule is to avoid divergent reimplementations of shared behavior. Shared engines, schemas, and contracts should remain shared where the repository architecture supports that.

### Feature Foundry relationship

GameSync theme/world behavior overlaps Feature Foundry authoring and exports. Do not assume a checked GameSync theme feature automatically proves parity with the newest Feature Foundry contract. Record source contract, host implementation, and runtime proof separately.

### HyperBowl and game/runtime subprojects

Project Constellation tracks HyperBowl reconstruction and other game/runtime work as related subprojects. Original source assets and reconstruction evidence must remain distinct from generated or Unity-derived material when authenticity matters. The Next monorepo exposes a substantial family of `hyperbowl:*` audit/index/extract/capture/runtime-parity commands; use the dedicated project documentation for those workflows rather than treating their existence as proof of completed reconstruction.

### Mascot and Petz systems

Mascot, ACS, Shimeji, and PF Magic Petz work intersects GameSync. Preserve engine-specific semantics and shared-core ownership rather than flattening them into generic animation features. Current Next Petz persistence still has separately tracked repair work and must not be promoted to platform-wide parity merely because a package exists.

## Performance and architecture evidence

The shipping repository contains a performance audit that identifies concrete hot paths in the extension, including message-router dispatch, storage migration, content injection, mascot state reads, and settings/broadcast paths. Treat it as optimization evidence and a backlog, not proof that every suggested optimization has already been implemented.

When modifying hot paths:

1. Reproduce current behavior first.
2. Preserve all returned data and ordering semantics.
3. Measure before and after with the same workload.
4. Run relevant regression tests.
5. Exercise the actual extension in Opera GX.
6. Do not trade correctness, full-library availability, or feature quantity for viewport culling or hidden off-screen processing.

## Credentials, identity, and publication safety

The shipping repository README states that Steam, Nexus Mods, Twitch, and other user-provided credentials are read at runtime from browser-managed extension storage rather than bundled in source/build output. Local environment files, private keys, credential exports, package-registry authentication, and generated build trees are excluded from source control.

The manifest's public extension identity key is not a private signing key. Preserve stable extension identity while keeping signing material outside the repository.

The shipping repository now explicitly requires a complete-tree secret scan before publication. Recent repository changes added Gitleaks-based publication guardrails and corrected pull-request read permission for that scan path. Treat those CI changes as release-safety infrastructure, not as a new product version.

## How to modify GameSync safely

### Before editing

- Resolve whether the requested change belongs to shipping `Gamesync`, `GameSync-Next`, a shared package, a desktop/server host, or a related project.
- Record the current branch/commit and loaded extension identity.
- Establish a baseline in the real user-facing host.
- Check project instructions and relevant subsystem documentation.
- If the change claims parity, identify the exact capability entry in `docs/gamesync-parity-matrix.json` and its current status.

### For shipping extension changes

- Edit `app/`, not generated `dist/`.
- Run the narrow regression tests for the changed subsystem.
- Run `npm run build`.
- Load the rebuilt `dist/` in Opera GX.
- Exercise the actual control/feature flow.
- Inspect extension/background/content-script errors as appropriate.
- Verify persistence after reload/restart for stateful features.

### For GameSync Next changes

- Edit the owning `apps/*` or `packages/*` source rather than generated build output.
- Run the narrow package build/type/lint/test path.
- Rebuild Extension V2 before parity auditing generated manifest behavior.
- Run `npm run audit:gamesync-parity` when the change touches parity-bearing extension behavior.
- Run `npm run verify:extension-v2:opera` or the exact isolated Opera lane for user-facing extension changes.
- For same-ID migration behavior, run the dedicated `verify:same-id-upgrade` path.
- Preserve the current shipping capability until paired evidence justifies changing its matrix status.

## Host/parity ledger

Project Constellation's exact platform requirement remains an evidence-backed ledger like:

`feature/version -> shipping Opera extension -> extension-v2 -> desktop/server -> Feature Foundry source -> evidence -> parity gap`

The repository-owned parity matrix is now the machine-readable extension layer of that ledger, but it does not replace product-family reasoning for desktop/server or Feature Foundry ownership.

A feature must not be marked complete across the platform merely because one host renders a control, one build succeeds, or the parity audit has `ok: true`.

## Troubleshooting

### Source change does not appear in Opera GX

For shipping GameSync, confirm `npm run build` regenerated `dist/`, then confirm Opera GX is loading that exact `dist/` path rather than an older copy or another checkout.

For Next, verify the exact WXT output/build under test and use the repository's isolated Opera verification path rather than a stale unpacked installation.

### Parity audit cannot find shipping GameSync

Set `GAMESYNC_JS_APP_PATH` to the canonical shipping `app/` directory. The audit also checks sibling `../Gamesync/app`, sibling `../GameSync/app`, the recovered `opera-extension/app`, and `../GameSync/opera-extension/app` locations.

### Parity audit is structurally clean but migration still is not complete

Inspect `parityComplete` and the capability statuses. `ok: true` only proves identity/reference/tab/command consistency and absence of undeclared gaps. Any `gap` or `implemented-unverified` capability still blocks full parity.

### Extension ID changes unexpectedly

Check the public identity material in the shipping manifest and the Next WXT build. The parity audit explicitly checks that the identity keys match. Do not replace stable identity material casually.

### A feature works in Next but not shipping GameSync

Treat that as a parity difference, not as proof the shipping path is obsolete. Record the exact capability, source owner, tested build, and missing paired evidence.

### A tracker import works but data is missing after export

Use the dedicated Tracker project/component evidence first. The current verified slice supports JSON, XLSX, DOCX, and active-collection CSV, but source-specific import/export regressions must be tested against the exact document shape and retained output artifact.

### Performance fix reduces card/item availability

Treat that as a regression. Full data/card availability is part of the product contract; optimization must not hide, cap, virtualize, or defer the actual collection simply because it is off-screen.

### An old checklist says a feature is done

Use the checklist as implementation history. Re-verify the current source and real runtime before using it as present-tense proof.

## Exact current next action

Maintain the repository-owned parity matrix as the extension-level source of truth for shipping-to-Next migration, then continue pairing every `implemented-unverified` and `gap` capability with exact runtime evidence. Keep desktop/server and Feature Foundry ownership in the broader host ledger. Do not retire shipping GameSync until `parityComplete` is actually true and the relevant real-host migration/restart workflows pass.

## Wiki maintenance

Update this page when either repository head materially changes platform ownership, the shipping or Next extension version changes, the parity matrix changes capability status, the executable parity-audit contract changes, a major feature slice moves onto current Next main, the real Opera verification path changes, or the platform's exact next action changes. Preserve validated shipping behavior and version lineage rather than rewriting the platform around whichever repository changed most recently.
