# GameSync Real Library Performance Wiki

**Project Constellation ID:** `PCX-050`
**Status:** ACTIVE / TRACKED
**Goal:** Optimize GameSync against the complete real library without culling or hiding off-screen cards.
**Current verified line:** GameSync 0.25.9 Real Library Performance Pass 1.
**Current storage package baseline:** shipping GameSync depends on `@sqlite.org/sqlite-wasm` `^3.53.0-build1`; the currently published npm/GitHub wrapper release is `3.53.0-build1`, while SQLite core itself is at `3.53.4`.

## Verified current state

The durable `0.25.9-real-library-performance-pass-1` evidence records a targeted performance pass over the Steam library path.

Implemented work includes:

- an O(n)-indexed Steam title merge path for large real libraries;
- initial Steam cover selection changed to portrait `library_600x900_2x` to avoid landscape-first replacement churn;
- per-real-sync telemetry for wall time, throughput, completeness, no-cap state, and quality;
- preservation of complete-library behavior;
- preservation of the no-virtualization and no-viewport-admission contract;
- preservation of media quality.

The live Steam network/account test was attempted but blocked by the environment. The durable evidence does not claim a successful live-account fetch.

## Recorded validation

The pass records:

- agent enforcer passed;
- final static validation passed;
- no-cap contract passed;
- JavaScript syntax passed.

The exact next live checkpoint in the durable evidence is to run `RESYNC_STEAM` in the user's real browser. The runtime writes `gsLastSteamSyncPerformance` for the next optimization pass.

## Current shipping dependency evidence

Current `Herbertofury/Gamesync` `package.json` identifies:

- GameSync extension version `0.6.3`;
- Vite `^8.1.3`;
- `@sqlite.org/sqlite-wasm` `^3.53.0-build1`;
- `idb` `^8.0.3`;
- `idb-keyval` `^6.2.6`;
- `flexsearch` `^0.8.212`;
- related worker/cache/runtime libraries.

The checked-in manifest is the version source. Do not infer the loaded browser bundle uses a different database line without proving the actual build identity.

## Current SQLite/WASM research

SQLite **3.53.4**, released July 24, 2026, remains the current stable SQLite core release as of this documentation pass. The 3.53 line added the `opfs-wl` Web Locks VFS and includes query-planner improvements.

SQLite's official WASM persistence guidance currently distinguishes:

### `opfs-sahpool`

- highest documented OPFS performance among the canonical options;
- no COOP/COEP requirement;
- strong for batch operations;
- does not transparently support multiple simultaneous connections to the same pool.

### `opfs`

- broader established compatibility;
- supports concurrency through SQLite's bespoke locking approach;
- may require COOP/COEP depending on usage.

### `opfs-wl`

- added in SQLite 3.53.0;
- uses browser Web Locks;
- requires `Atomics.waitAsync()`;
- performance is documented as broadly on par with `opfs`;
- provides fairer FIFO lock request handling;
- suitable when multi-context concurrency matters and required browser primitives are available.

Primary sources:

- https://sqlite.org/
- https://www2.sqlite.org/releaselog/3_53_4.html
- https://sqlite.org/wasm/doc/tip/persistence.md
- https://www.npmjs.com/package/@sqlite.org/sqlite-wasm
- https://github.com/sqlite/sqlite-wasm/releases

## Important wrapper/package boundary

Do not treat SQLite core and the npm-distributed WASM wrapper as the same version stream.

Current verified external package state on **2026-08-22** is:

- SQLite core latest stable: **3.53.4**;
- `@sqlite.org/sqlite-wasm` npm `latest`: **3.53.0-build1**;
- `sqlite/sqlite-wasm` latest published GitHub release: **3.53.0-build1**;
- GameSync's declared dependency range starts at that same `3.53.0-build1` wrapper.

This means a "SQLite 3.53.4" browser benchmark cannot be produced by merely changing GameSync's npm version today because there is no published `@sqlite.org/sqlite-wasm` 3.53.4 wrapper release to select. A 3.53.4 WASM candidate must be either:

1. a future official `@sqlite.org/sqlite-wasm` release that actually wraps 3.53.4; or
2. a locally reproducible build of the official `sqlite/sqlite-wasm` project pinned to SQLite 3.53.4, with the wrapper source revision, upstream SQLite source identity, build command, produced WASM/JS hashes, and browser artifact identity recorded.

Never label a GameSync artifact "SQLite 3.53.4" merely because the SQLite website reports 3.53.4 as current core. Record **both** the SQLite core identity and the wrapper/package identity.

### Worker/Promiser API deprecation watch

The current `@sqlite.org/sqlite-wasm` documentation states that Worker1 and Promiser1 APIs have been deprecated since **2026-04-15** and are actively discouraged for non-toy software. This wiki does not assume GameSync currently uses either API; the exact loaded storage code must be inspected first.

Before any storage refactor or VFS benchmark:

1. identify the exact SQLite WASM API entrypoint used by the shipping build;
2. record whether it uses Worker1/Promiser1 or the current recommended API path;
3. if a deprecated API is present, benchmark and qualify its replacement as a separate migration rather than combining API migration, SQLite-core upgrade, VFS change, and performance tuning into one untraceable change;
4. preserve database contents, schema, complete-library counts, restart behavior, and error recovery throughout the migration.

## Performance decision rule

A faster persistence backend is useful only if it preserves the entire library and the existing behavioral contract. Storage/VFS changes must not be used to justify:

- viewport-only loading;
- hidden item caps;
- reduced records;
- stale synchronization;
- lower cover/media quality;
- deferred off-screen availability;
- lost multi-tab or restart behavior;
- weaker source identity.

## Proposed VFS benchmark lane

After the real `RESYNC_STEAM` baseline is captured, benchmark the current storage path against a controlled SQLite/WASM VFS matrix.

Candidate lanes:

1. current production GameSync path using the exact resolved `@sqlite.org/sqlite-wasm` package and current VFS/API configuration;
2. the same exact wrapper bytes with only the VFS/API configuration changed, so VFS effects can be measured without a simultaneous SQLite upgrade;
3. `opfs-sahpool` when a single active database owner is safe;
4. `opfs-wl` when multi-context fairness/concurrency is required and supported;
5. existing `opfs` when it remains the better compatibility fit;
6. a future official or reproducibly locally built SQLite 3.53.4 WASM wrapper, tested as a **separate version-upgrade lane** after the VFS-only baseline is understood.

The experiment must use the same complete library snapshot and the same product workflow. Do not collapse package-version, API, and VFS changes into a single comparison if the goal is to know which change actually helped.

## Required measurements

Record at least:

- full library item count;
- duplicates/identity collisions;
- source/ownership fields;
- cover identity and quality;
- sync wall time;
- items/second;
- database open/close time;
- index-build/update time;
- search latency;
- memory growth;
- storage size;
- reload behavior;
- multi-tab/worker behavior if relevant;
- errors and recovery behavior;
- `gsLastSteamSyncPerformance` output;
- exact GameSync commit/build identity;
- exact `@sqlite.org/sqlite-wasm` package version and resolved package integrity;
- exact SQLite core source/version embedded in the candidate;
- exact VFS and API entrypoint under test.

Use repeated runs and compare medians/percentiles so one noisy run is not promoted as a performance win.

## Anti-regression rules

- The complete real library must remain available at all times after synchronization.
- No viewport virtualization or culling may be introduced as a correctness shortcut.
- Do not lower media quality to improve synthetic metrics.
- Do not skip identity/provenance fields to reduce database work.
- Do not adopt `opfs-sahpool` if the actual GameSync architecture needs simultaneous database owners and cannot safely coordinate them.
- Do not claim SQLite 3.53.4 browser use when only the 3.53.0-build1 npm wrapper is present.
- Do not adopt a locally rebuilt wrapper unless its source revisions, commands, generated bytes, and rollback path are recorded.
- Do not combine a deprecated Worker/Promiser migration, core SQLite upgrade, and VFS change into one benchmark whose causal improvement cannot be attributed.
- Keep rollback to the current storage path available until the candidate survives real-browser restart and persistence tests.

## Acceptance test

A candidate storage/performance path qualifies only when:

- the complete library count is identical;
- identity/provenance and cover data are equivalent;
- no-cap and quality gates pass;
- repeated real-library measurements show a material improvement beyond normal noise;
- no important latency, memory, restart, concurrency, or error-recovery path worsens materially;
- the exact GameSync build identity is recorded;
- the exact wrapper/package, embedded SQLite core identity, VFS, and API entrypoint are recorded separately;
- real browser `RESYNC_STEAM` succeeds;
- restart persistence and follow-up sync are exercised.

## Exact next action

Capture the real `RESYNC_STEAM` baseline and `gsLastSteamSyncPerformance` in the current shipping GameSync build. In that same loaded build, record the resolved `@sqlite.org/sqlite-wasm` package, embedded SQLite core identity, VFS, and API entrypoint. Then run a VFS-only A/B using identical wrapper bytes before evaluating a separately reproducible SQLite 3.53.4 WASM build. If the current code path uses deprecated Worker1/Promiser1 APIs, qualify their replacement independently rather than bundling that migration into the VFS benchmark.

## Evidence

- Real Library Performance folder: https://drive.google.com/drive/folders/1QOdZrk_y6lsewmr--pj7VTHdgPqPlxF6
- Durable performance state: https://drive.google.com/file/d/1KflWhKa4Bz1Bteom5yN9NgBvdiyMRY0T/view
- Current shipping GameSync repository: https://github.com/Herbertofury/Gamesync
- SQLite core release history: https://sqlite.org/changes.html
- SQLite WASM npm package: https://www.npmjs.com/package/@sqlite.org/sqlite-wasm
- SQLite WASM wrapper releases: https://github.com/sqlite/sqlite-wasm/releases

## Wiki maintenance

Update this page when real-library metrics, Steam sync behavior, storage/VFS choices, sqlite-wasm wrapper releases, SQLite core versions, API entrypoints, cover strategy, no-cap guarantees, or real browser verification changes. Preserve every before/after baseline needed to detect regression and keep wrapper-versus-core version identities explicit.
