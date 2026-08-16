# GameSync Next Wiki

**Project Constellation ID:** `PCX-042`  
**Status:** ACTIVE / TRACKED  
**Canonical connected repository:** [Herbertofury/GameSync-Next](https://github.com/Herbertofury/GameSync-Next)  
**Default branch:** `main`

## Purpose

GameSync Next is the typed, modular successor/migration workspace for the shipping GameSync Opera extension. It combines a WXT/React extension, desktop and server hosts, shared packages, native integrations, source/tooling for parity auditing, Feature Foundry surfaces, and game/runtime projects.

The governing rule is **migration with proof**, not replacement by assumption. The shipping JavaScript extension in [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync) remains the user-facing parity baseline until the relevant behavior is proven equivalent in the new host.

## Verified repository layout

The current README identifies these major areas:

- `apps/extension-v2` - WXT Manifest V3 Opera/Chromium extension
- `apps/desktop` - desktop host
- `apps/server` - server host
- `apps/feature-foundry` - portable feature-authoring surface
- `apps/asset-orchestrator` - source-only asset tooling; local vaults excluded
- `packages` - shared engines, schemas, UI, themes, games, and portable feature slices
- `native-helper`
- `native-host`
- `playnite-bridge`
- `scripts/audit-gamesync-parity.mjs` - executable parity audit
- `docs/gamesync-parity-matrix.json` - machine-readable parity contract

The repository root also contains substantial project documentation including `AGENTS.md`, `Bugs&Fixes.md`, `Feature Layout.md`, `GAMESYNC.md`, HyperBowl reconstruction documents, and other project-specific references.

## Install / dependency setup

From a clean checkout:

```text
npm ci
```

The repository uses npm workspaces under `apps/*` and `packages/*`.

## Core verification commands

The current README specifies this verification path:

```text
npm ci
npm run audit:gamesync-parity
npm --workspace apps/extension-v2 run build
npm --workspace apps/extension-v2 run lint
npm --workspace apps/extension-v2 run typecheck:room
npm --workspace apps/extension-v2 run verify:same-id-upgrade
node scripts/verify-extension-v2-opera.js
```

Set `GAMESYNC_VERIFY_TRANSFORMERS=1` for the deeper isolated-Opera transformer/WASM smoke test.

## Root workspace commands

The current package manifest exposes a broad toolchain. Important categories include:

### Shared packages and hosts

```text
npm run build:packages
npm run dev:desktop
npm run dev:feature-foundry
npm run dev:server
npm run build
npm run build:feature-foundry
```

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
npm run test:e2e-opera
npm run test:extension-regression
```

### HyperBowl

The package manifest contains many explicit HyperBowl indexing, extraction, audit, capture, parsing, export, and game-build commands. These are project tooling, not generic build steps. Use the relevant HyperBowl project documentation before running destructive or extraction-heavy operations.

## Current toolchain snapshot

The root manifest currently includes React 19, React DOM 19, Playwright, Vite 8, Oxc linting, Sharp, Rapier 2D compatibility packages, Chrome Remote Interface, WebSocket support, and other build/runtime tooling. Always use the checked-in manifest/lockfile as the current version source.

## Shipping GameSync parity contract

The parity system exists because the shipping JavaScript extension and GameSync Next can diverge. The expected development loop is:

1. Resolve the current shipping `Gamesync` checkout.
2. Build the relevant Next target.
3. Run the parity audit.
4. Review `docs/gamesync-parity-matrix.json` and audit output.
5. Fix real parity gaps rather than weakening the matrix.
6. Run target-specific tests.
7. Load the actual extension/host and exercise the workflow.
8. Verify persistence/restart behavior when stateful.

A rendered control or passing TypeScript build is not sufficient evidence of parity.

## Recent verified repository activity

The current connected history includes a **2026-08-15** fix for transient Opera extension discovery. The latest observed commit is `9e337c720f0180cffa577f140b181c699f0a1650`, which resets extension-probe de-duplication per polling iteration so transient Opera probe failures can recover while retaining intra-iteration de-duplication and regression coverage.

The preceding work added tests and the implementation fix, indicating the failure was treated as a reproduced behavior with regression coverage rather than a documentation-only change.

## Clean-checkout parity behavior

Recent repository history also includes work to make the parity audit rebuild Extension V2 before inspecting generated manifest output, with regression coverage around clean-checkout behavior, Windows command selection, source-root casing, and explicit source-path precedence.

This is important for wiki instructions: do not assume generated extension output exists in a fresh checkout before parity auditing.

## Opera verification

For Opera-specific extension work:

- build the target first;
- use the repository's isolated Opera launcher/agent flow where appropriate;
- verify the exact loaded extension path and identity;
- test the real user flow, not only a CDP handshake;
- inspect runtime/background/content-script errors;
- verify same-ID upgrade behavior when migration identity matters.

## Shared architecture rule

GameSync Next is a monorepo because shared behavior should not be separately reimplemented in extension, desktop, server, Feature Foundry, and game hosts. Prefer shared packages and explicit adapters where the repository already establishes that structure.

When adding a feature, record:

- source package/module;
- host adapters;
- shipping GameSync equivalent;
- data/schema contract;
- persistence/storage owner;
- verification commands;
- runtime proof;
- known parity gap.

## Feature Foundry relationship

`apps/feature-foundry` and shared packages provide a bridge toward portable feature-authoring behavior. Do not confuse this with proof that the separate Feature Foundry production application is complete. Keep project identity and acceptance criteria separate.

## Native integration surface

The repository includes `native-helper`, `native-host`, and `playnite-bridge`. Native integration claims should be verified through the actual host/bridge workflow, including discovery, communication, errors, and restart behavior.

## Testing discipline

At minimum for changed GameSync Next behavior:

1. Run the narrow changed-path test or regression suite.
2. Run applicable lint/type checks.
3. Build the affected workspace.
4. Run parity audit if shipping GameSync behavior is involved.
5. Exercise the actual affected host.
6. Confirm the runtime loaded the new output rather than a stale build.
7. Check persistence after reload/restart when stateful.
8. Run broader regression suites when cross-cutting shared packages changed.

## Troubleshooting

### Parity audit fails on a clean checkout

Confirm current source includes the clean-checkout rebuild behavior, run dependency installation, and allow the audit to build Extension V2 before generated-manifest inspection. Do not satisfy the audit by committing stale generated output.

### Opera extension discovery fails transiently

Current repository history includes a retry fix. Confirm the loaded source contains the current probe behavior and regression tests before inventing an alternate discovery mechanism.

### Next feature appears implemented but shipping parity is unclear

Run the parity audit and inspect the matrix. Record the gap explicitly rather than declaring migration complete.

### A shared-package change breaks only one host

Treat host-specific adapters/configuration as first suspects while preserving the shared contract. Test every affected host before changing shared behavior to fit one consumer.

## Security / repository hygiene

The current README states that signing keys, API credentials, Steam secrets, browser profiles, `.env` files, generated native outputs, local asset vaults, and backup archives must stay out of Git. Public extension identity material may remain in the manifest while private signing material stays external.

## Exact current next action

Keep advancing the typed implementation while maintaining a verified parity ledger against current shipping GameSync. Every migration claim should identify the feature, shipping behavior, Next implementation, host coverage, tests, and real-runtime evidence.

## Wiki maintenance

Update this wiki when the monorepo layout, parity contract, host ownership, major workspace commands, extension verification flow, or shipping-baseline relationship changes. Link detailed subsystem wikis rather than duplicating them when a track becomes independently maintained.