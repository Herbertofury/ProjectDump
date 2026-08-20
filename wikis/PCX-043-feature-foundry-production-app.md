# Feature Foundry Production App Wiki

**Project Constellation ID:** `PCX-043`  
**Status:** ACTIVE / TRACKED  
**Current canonical product repository:** [Herbertofury/Feature-Foundry](https://github.com/Herbertofury/Feature-Foundry)  
**Current canonical released source line:** `v24.0.0`  
**Current verified repository head:** `e1ba080b5c7590f1c844a6ed13b3a471709920b9`  
**Tagged release:** [Feature Foundry v24.0.0](https://github.com/Herbertofury/Feature-Foundry/releases/tag/v24.0.0)  
**Canonical Drive release folder:** [Feature Foundry v24.0.0](https://drive.google.com/drive/folders/1eU95XQZNq-3mc9HvY08JbClSBTu7tXYY)  
**Historical runnable benchmark:** `V33 FINAL_READY`  
**Historical/parallel project-operations recovery line:** `GameSync / Feature Foundry V2-253`

## Purpose

This project tracks the actual Feature Foundry production application, distinct from design-only directives, generated starters, data-only bundles, migration packages, and Project Constellation itself.

The production acceptance contract is a real stateful living-world authoring application with professional workspaces, complete persisted state, reversible editing, complete data availability, live rendered worlds, real media/music integrations, truthful native behavior, recoverable release lineage, and verified build/runtime evidence.

## Current authority model

Feature Foundry now has a verified canonical repository and published native/web release. Older continuity evidence remains important, but authority has changed materially.

### 1. Current canonical source and released product: Feature Foundry v24.0.0

`Herbertofury/Feature-Foundry` is no longer a placeholder. Current `main` contains a complete maintainable application and the project-owned progress record identifies `v24.0.0` as published.

Current repository evidence verifies:

- package version `24.0.0`;
- TypeScript 7 + Vite 8 web application;
- Three.js/WebGL living-world renderer;
- Tauri 2 + Rust native desktop shell;
- bundled SQLite persistence;
- V24 compatibility contract preserved in source;
- V33 runtime catalog authority integrated into the current application;
- 17 approved theme packages / worlds;
- 34 rooms;
- 17 weather systems;
- 85 exact ecology objects;
- 10 current artist worlds;
- browser interaction/screenshot verification at 1536x1024;
- production web/source/native release artifacts;
- a published GitHub release and mirrored Google Drive release set.

This is the current default implementation authority for install, build, package, modification, and release work.

### 2. V33 FINAL_READY: preserved behavior/data benchmark

`V33 FINAL_READY` remains valuable as a historical high-confidence runnable benchmark. Current v24 explicitly imports the V33 theme/world authority instead of discarding it.

Use V33 when checking for regressions in the richer historical living-world behavior set, but do not treat its standalone artifact as newer source authority than the current Feature-Foundry repository.

### 3. GameSync / Feature Foundry V2-253: preserved project-operations and recovery architecture

The V2 recovery lineage remains valid continuity evidence for Project Vault, Improvement Radar, agent operations, repository/supply-chain intelligence, launch-readiness modeling, and exact recovery history.

That line is not the current canonical v24 application tree. Do not silently claim that every V2-253 Project Vault/agent subsystem ships inside the standalone v24 repository unless current source proves it.

Use the two lines deliberately:

- v24 repository/release for current application source, runtime, build, native package, media/music, world rendering, and release operations;
- V2-253 continuity for preserved project-operations architecture and recovery evidence not represented in the current v24 source tree;
- V33 for historical runnable behavior and data non-regression evidence.

## Current v24 release identity

Current project-owned repository head:

`e1ba080b5c7590f1c844a6ed13b3a471709920b9`

The release implementation was introduced by commit:

`7dced5c61b83ce2478acee135b784abdbc5b3df5` - `feat: ship Feature Foundry living-world v24`

The complete-release bundle behavior was finalized by:

`f6ee83bdea159b1409954399a4b54cb1442dc104` - `build: add complete release bundle`

The project-owned release record then published the v24 release and Drive mirror.

### Drive artifacts

| Artifact | Drive file ID | Size | SHA-256 |
| --- | --- | ---: | --- |
| `Feature-Foundry-v24.0.0-source.zip` | `1tKvfMHe4bYV_tlZy_WLe4vaDeMECTkrq` | 6,998,572 bytes | `b8701b37328277667820af9f6ea630f33d13d1c9ffaa9827b914328895fc97c2` |
| `Feature-Foundry-v24.0.0-web.zip` | `1SsDrkQxct_-DCB_qqWDrsBgA6rDsdt7y` | 328,556 bytes | `99f3714e5cae72e726711ebed0821ed09dbc1cadd7ab470afa2c3ad5f9f48726` |
| `Feature-Foundry-v24.0.0-windows-x64-setup.exe` | `1TH-uZzg6r4ef0Qos6AjR5ZFjuSn10kV7` | 2,003,721 bytes | `b4ac90edf1213f3e5a9a1a8724184ae2e97bc30da3f69f877aadfe71819dc49a` |
| `Feature-Foundry-v24.0.0-windows-x64.msi` | `1S7bOwzr3by8vAbEYiqxKE62vKy7ze5-g` | 2,633,728 bytes | `29a42693cc630d3aec72d137297063eab8f7c08ec21828cb8efd3871e025b157` |
| `Feature-Foundry-v24.0.0-complete-release.zip` | `1PvBdu6sD8bm3AYnLmCnR4Hdo_HUNCbF2` | 11,716,663 bytes | `593b3e0be60ab694ddd8fbe9e3bc48c3b2c443a542d0eb41390b09596707f54b` |
| `SHA256SUMS.txt` | `18c325aHLh9Kue8oTz0_KS4yNTtXShRxC` | 533 bytes | contains the five published artifact digests above |

The complete-release ZIP includes the release-facing artifacts plus the checksum manifest. The packaging script computes SHA-256 directly from artifact bytes and fails if the native Tauri bundles are absent.

## Product systems in v24

Current source and README describe these implemented product systems.

### Theme and world catalog

- 17 approved V33 theme packages;
- 17 theme worlds;
- 34 rooms;
- 17 weather systems;
- 85 exact ecology objects;
- 10 current artist worlds across Frawgy, Lightweaverart, Dreamrelicc, Karoline Georges, and saveroom;
- 27 total catalog worlds in current verification coverage.

The older 16-theme / 80-object recovery summary is historical and is not current runtime authority.

### Living world rendering

The premium runtime uses Three.js/WebGL for a continuously animated world with:

- water shaders;
- particles;
- time and weather response;
- reflections;
- volumetric light;
- parallax;
- music and interaction pulses;
- procedural environment geometry and decoration.

The runtime keeps the canonical V24 body/CSS/imperative behavior contract protected while layering typed premium systems around it.

### Workspaces and world controls

The current V24 interface includes the canonical living-world shell with:

- Home;
- Explorer;
- Vault;
- Rooms;
- Theme Lab;
- undo/redo;
- theme selection;
- district selection;
- weather and time controls;
- animated environment controls;
- soundtrack controls;
- world-state controls;
- focus/canvas-oriented modes;
- settings;
- left, center, and right living regions;
- activity, soundtrack, quick-action, room-routing, weather, dock, chrome-mode, and history surfaces.

A visible control remains a product promise. Do not treat a rendered button, selector, or workspace tab as complete without the real behavior behind it.

### Object ecology and mascots

Current source preserves real direct-manipulation behavior including:

- draggable and throwable objects;
- restitution/physics behavior;
- selection;
- keyboard movement;
- reactions;
- room-aware placement;
- media and music affordances;
- mascot registry;
- mascot direct manipulation;
- pinning;
- mascot physics;
- autonomy;
- UI awareness;
- speech;
- weather/music reactions;
- independent behavior controls.

### Living Screen Studio

Current v24 supports:

- local video files;
- direct HTTPS media;
- privacy-enhanced YouTube playback;
- room TV mirroring;
- an animated procedural idle channel.

The Tauri CSP allows local/app assets, blob/data media, HTTPS media, and `youtube-nocookie.com` frame content while keeping the broader application CSP explicit.

### Music Hub

Music Hub supports per-theme/per-room mapping and six provider adapters:

- Spotify;
- Apple Music;
- Deezer;
- SoundCloud;
- TIDAL;
- YouTube Music.

All six providers support search, room mapping, and external handoff without bundling user credentials.

Account-controlled behavior is provider-specific:

- Spotify uses Authorization Code with PKCE. Configure the Spotify developer application for loopback callback use and enter the Client ID in Feature Foundry settings. The native app creates a dynamic `127.0.0.1` callback port, validates OAuth state, emits the result back to the application, and manages current-session token behavior.
- Apple Music uses MusicKit v3 and expects a server-issued developer token. Keep the signing private key off the client.
- Deezer, SoundCloud, TIDAL, and YouTube Music use validated external provider URLs/handoff unless a current source revision proves deeper embedded control.

Do not advertise provider capabilities beyond the current adapter implementation.

## Native desktop architecture

The current native shell is Tauri 2.

### Application identity

- product name: `Feature Foundry`;
- package/native version: `24.0.0`;
- Tauri identifier: `com.featurefoundry.livingworld`;
- primary window: 1536x1024;
- minimum window: 1120x720;
- resizable, centered, undecorated application window;
- native bundling enabled.

### Rust/native stack

`src-tauri/Cargo.toml` currently declares:

- Rust edition 2024;
- minimum Rust `1.88`;
- Tauri `2.11.5`;
- `tauri-plugin-opener` `2.5.4`;
- `rusqlite` `0.40.2` with bundled modern SQLite;
- `serde` / `serde_json`;
- `url`.

### Native commands

The current native command layer includes:

- runtime profile reporting;
- save world snapshot;
- load world snapshot;
- dynamic Spotify loopback callback startup;
- catalog summary;
- music-route listing;
- room soundtrack assignment;
- room soundtrack lookup;
- native history recording.

World snapshots are validated as JSON and written under the application data directory as `living-world-snapshot.json`.

### SQLite ownership

The native database initializes during Tauri setup. Current project-owned documentation describes SQLite ownership for:

- verified catalog seeding;
- room soundtrack assignments;
- history;
- integrity diagnostics;
- runtime profiles/catalog status as exposed through native commands.

When changing persistent schemas, add explicit migration and restart verification. Do not silently replace or discard user state.

## Current source layout

```text
Feature-Foundry/
|-- README.md
|-- progress.md
|-- package.json
|-- package-lock.json
|-- index.html
|-- vite.config.ts
|-- tsconfig.json
|-- src/
|   |-- main.ts
|   |-- main.css
|   |-- prototype-v24.ts
|   |-- premium.ts
|   |-- data/
|   |-- world/
|   |-- music/
|   |-- media/
|   |-- styles/
|   `-- types/
|-- src-tauri/
|   |-- Cargo.toml
|   |-- Cargo.lock
|   |-- tauri.conf.json
|   |-- capabilities/
|   |-- icons/
|   `-- src/
|       |-- main.rs
|       |-- lib.rs
|       `-- database.rs
|-- tests/
|   |-- contract.test.ts
|   |-- authority.test.ts
|   |-- ui.test.ts
|   `-- actions/
|-- scripts/
|   `-- package-release.ps1
`-- reference/
```

### Source ownership guide

- `index.html`: canonical V24 body markup and module entry.
- `src/prototype-v24.ts`: protected compatibility runtime for the original V24 behavior contract.
- `src/styles/prototype-v24.css`: protected V24 style contract.
- `src/premium.ts`: typed premium application layer.
- `src/world/`: current living-world render/runtime ownership.
- `src/music/`: provider and soundtrack ownership.
- `src/media/`: Living Screen Studio/media ownership.
- `src/data/`: verified runtime and artist-world authority exports.
- `src-tauri/src/database.rs`: native SQLite ownership.
- `src-tauri/src/lib.rs`: Tauri commands, snapshots, Spotify loopback, runtime integration.
- `tests/contract.test.ts`: exact V24 source-contract guard.
- `tests/authority.test.ts`: data/catalog authority guard.
- `tests/ui.test.ts`: real browser interaction/render verification.
- `scripts/package-release.ps1`: deterministic release staging, native artifact collection, ZIP assembly, and SHA-256 manifest generation.

## Web development workflow

Prerequisites:

- Node.js/npm able to install the current lockfile;
- a browser capable of running the Vite/Three.js application.

From the repository root:

```powershell
npm install
npm run dev
```

The dev server binds to loopback.

Production web build:

```powershell
npm run build
```

Local production preview:

```powershell
npm run preview
```

## Native desktop development workflow

Additional prerequisites:

- Rust toolchain meeting the current `rust-version = 1.88` floor;
- platform prerequisites required by Tauri 2;
- npm dependencies installed.

Run the native app in development:

```powershell
npm run desktop:dev
```

Tauri runs the frontend dev server on loopback port 1420 through the configured `beforeDevCommand`/`devUrl` path.

Build native installers/bundles:

```powershell
npm run desktop:build
```

The current release folder contains verified Windows x64 MSI and NSIS-style setup artifacts.

## Verification workflow

Primary full verification command:

```powershell
npm run verify
```

Current `verify` expands to:

```text
npm run test
npm run typecheck
npm run build
cargo check --manifest-path src-tauri/Cargo.toml
npm run test:ui
```

The test scripts are:

```powershell
npm run test
npm run test:ui
npm run typecheck
```

Project-owned `progress.md` records the current release as passing:

- exact V24 source contract;
- data authority checks;
- TypeScript verification;
- Rust verification;
- optimized production build;
- 1536x1024 browser interaction/screenshot verification.

The README additionally states verification covers:

- exact V24 markup/CSS/runtime contract;
- database authority counts and IDs;
- full-width procedural rendering;
- both reference themes;
- all 27 catalog worlds;
- Music Hub provider behavior;
- the real media-surface flow.

Do not convert repository text into a fresh current-run pass if the exact current head has not actually completed the command in the environment performing the change. Preserve the project-owned release evidence and add new evidence when requalified.

## Release packaging workflow

Before packaging, create the optimized web build and native release bundles:

```powershell
npm run verify
npm run desktop:build
npm run package
```

`npm run package` invokes `scripts/package-release.ps1`.

The packaging script:

1. resolves the project and artifact roots;
2. refuses an artifact path outside the repository;
3. creates isolated web/source staging directories;
4. copies the built web output;
5. copies source, tests, scripts, reference material, native source/configuration, and root project files;
6. creates web and source ZIPs;
7. requires installable native Tauri artifacts;
8. copies native artifacts into release-facing names;
9. computes SHA-256 for all release files;
10. writes `SHA256SUMS.txt` without a BOM;
11. creates a complete release ZIP containing the release artifacts plus checksum manifest;
12. hashes that complete release ZIP and appends the digest to the checksum manifest;
13. removes the temporary stage.

A package run must fail rather than quietly create a partial release when the native Tauri bundles are missing.

## Installing the released Windows application

Use the current Drive/GitHub v24 release rather than an older prototype HTML.

Choose one verified Windows artifact:

- `Feature-Foundry-v24.0.0-windows-x64-setup.exe`;
- `Feature-Foundry-v24.0.0-windows-x64.msi`.

Before treating an artifact as canonical, compare its SHA-256 to the release manifest in this page.

After installation:

1. launch Feature Foundry;
2. confirm the application reports/behaves as the v24 native product;
3. open theme/world controls;
4. exercise at least one world/room switch;
5. exercise object/mascot interaction;
6. verify media and soundtrack surfaces appropriate to the local configuration;
7. save a world snapshot with `Ctrl+S`;
8. restart the application and confirm persisted/native state remains available;
9. inspect visible errors instead of accepting silent fallback.

The current Windows artifacts are release-optimized but are not recorded as Authenticode-signed by the project-owned progress file.

## Daily use and configuration

### Theme/world operation

Use the theme, district, weather, time, room, world, and workspace controls to move between authored world states. Preserve full content availability when changing performance/presentation behavior.

### Fullscreen and snapshot shortcuts

Current README documents:

- `F`: fullscreen toggle;
- `Ctrl+S`: persist a native world snapshot.

### Music provider setup

Spotify account-controlled behavior requires a configured provider Client ID and loopback callback support. Apple Music account-controlled behavior requires a valid developer token. Other listed providers must remain truthful to their current external-handoff behavior.

### Media surface setup

Living Screen Studio accepts supported local video files, direct HTTPS media, and privacy-enhanced YouTube sources. Keep media fidelity and user choice intact; do not replace this with lower-quality proxy content merely for performance.

## Modification map

### Change canonical V24 interface behavior

Edit `index.html`, `src/prototype-v24.ts`, and `src/styles/prototype-v24.css` only with great care. The project intentionally protects the V24 contract with exact tests. Any change to that contract must be explicit and must update the acceptance evidence rather than weakening the test.

### Change premium rendering/world behavior

Use `src/premium.ts` and `src/world/`. Preserve authored content, runtime data, input behavior, performance tiers, and world-state semantics.

### Change theme/world authority data

Use `src/data/` and the corresponding authority tests. Preserve the 17-theme V33 authority and the separate artist-world authority instead of flattening them into an unverified merged source.

### Change media behavior

Use `src/media/` plus the relevant UI/runtime tests. Verify local file, direct HTTPS, YouTube privacy mode, TV mirroring, and failure feedback where affected.

### Change music/provider behavior

Use `src/music/`, native OAuth support in `src-tauri/src/lib.rs`, and native persistence/routes in `src-tauri/src/database.rs` where applicable. Provider capability must remain truthful and provider credentials/secrets must never be bundled into release artifacts.

### Change native persistence or commands

Use `src-tauri/src/database.rs` and `src-tauri/src/lib.rs`. Add migration, restart, and corruption/error-path proof for stateful changes.

### Change packaging

Use `scripts/package-release.ps1`, Tauri configuration, and package metadata. Preserve deterministic file naming, checksum generation, complete-release assembly, and fail-closed native-bundle requirements.

## Production-app non-regression rules

- Preserve all verified theme, world, room, weather, object, artist-world, soundtrack, history, snapshot, and user-authored state unless an explicit migration proves equivalence.
- Never reintroduce the old 16-theme/80-object summary as current runtime authority.
- No viewport culling, hidden off-screen admission, artificial item/data caps, reduced result quantity, or lower-fidelity modes that remove authored content.
- Performance/presentation modes may reduce rendering cost only when authored state and functionality remain available.
- Every top-level workspace/tab must open distinct real functionality.
- Every visible control must be wired end-to-end with truthful success/error state.
- Stateful operations require persistence and restart verification.
- Provider/API/tool absence remains explicit unavailable/unsupported state, never synthetic success.
- Preserve the exact V24 contract unless a deliberate successor contract is implemented and fully reverified.
- Preserve V33 behavior/data evidence until a successor explicitly proves equal-or-better coverage.
- Preserve V2-253 recovery/project-operations history even though it is not the current canonical v24 product tree.

## Historical V33 runnable benchmark

Drive contains `Feature Foundry V33 FINAL_READY Checkpoint`, status `FINAL_READY`, built forward from the verified V25 runnable base plus V30/V31 verification lineage and V32 interaction/ecology specification without overwriting preserved base bytes.

V33 records:

- `101/101` V33 runtime assertions passed;
- `117/117` legacy runtime assertions passed;
- `22/22` V33 static assertions passed;
- 59 legacy audited controls with 0 missing handlers;
- 0 console errors and 0 page errors;
- fresh extraction pass;
- text-clipping audit at 1280x800 and 1600x1000;
- non-regression and no-artificial-caps guarantees;
- verified ZIP SHA-256 `680978a3aa8f16b47e767720ebfdc3b89fda5c148c5f3d4d3f308390b09385d9`;
- verified HTML SHA-256 `83aac630afa4e6522d28452bb6a7c0ebe183eee6812b89b6d742662876af06ec`;
- remote Drive artifact ID `1_mLbBXiS0yL7g2cKP7qQJxqyyRHP4RSY` with matching remote SHA-256.

V33 includes Theme-aware Library Ecology Lab, Ecology Director world modes, transition depth 0-5, Efficient/Balanced/High/Ultra/Cinematic presentation tiers with content parity, a causal world-signal bus, chronological/interaction/authored-world memory channels, advanced optical/spatial composition, six soundtrack/provider mappings, five host adapters, persistent state, and reduced-motion/performance equivalence.

Current v24 uses the V33 theme/world authority as an explicit source input. Keep the stronger historical interaction evidence available for regression comparison.

## Historical/parallel V2-253 continuity

The V2 recovery ledger starts from `GameSync-V2-239-contracts` and records additive checkpoints through V2-253.

Important milestones:

| Version | Verified material increment |
| --- | --- |
| V2-239 | complete recovery base for the reconstruction line |
| V2-242 | corruption-resistant Project Vault daemon, research radar, Feature Drops, agent runners, history/recovery UI |
| V2-243 | evidence-bound Feature Drop synthesis and custom local agent profiles |
| V2-244 | native ACP v1 stdio bridge with permissions, cancellation, bounded filesystem tools, and escape protection |
| V2-245 | OpenHands Agent Server bridge |
| V2-246 | ACP Registry discovery/import with provenance and fail-closed binary handling |
| V2-247 | checksum-verified agent binary install/update/rollback lifecycle and archive hardening |
| V2-248 | autonomous GitHub repository discovery with durable candidate inventory |
| V2-249 | capability-change intelligence, complete evidence retention, and removal of application-level evidence/display caps |
| V2-250 | repository health/trust intelligence |
| V2-251 | dependency inventory, OSV intelligence, CycloneDX 1.7 export |
| V2-252 | release-integrity, digest, attestation, verifier-identity, and cryptographic-verification evidence |
| V2-253 | 13-gate launch-readiness model and production smoke harnesses |

### V2-253 recovery identity

The durable ledger records:

- full local checkpoint: `278,378,882` bytes;
- full checkpoint SHA-256: `a74d90679015cb5da01777bca9e32578d639bbbf299861a6a6cecf86db6b2c07`;
- exact source fingerprint: `de24e9a03470ee397072b2ffcec0b8aee46529abbd9a3422e62cec24f404214d`;
- source tree: `6,379` files / `485,619,841` source bytes;
- V2-252 -> V2-253 incremental ZIP: `136,149` bytes;
- incremental ZIP SHA-256: `4c35d6087548378451401e9fe7748ec8ef0afb60625a5a88c800f08fe8f78efc`;
- Drive exact-byte delta document: `1vDJ4IDn2FvTS5hYH4-A_HC80VgaNe9poBmIOOo9JGyk`.

### V2-253 project-operations capabilities

That line records Project Vault atomic state, append-only SHA-bound history, version/artifact/dependency/research/Feature Drop/agent-run history, backups/recovery points, source fingerprinting, scheduler state, HTTP API, Improvement Radar, GitHub repository discovery, repository health/trust history, dependency/vulnerability intelligence, release-integrity/attestation intelligence, evidence-bound agent proposals, ACP/OpenHands integration, and machine-computed launch readiness.

### V2-253 launch-readiness result

The recorded GameSync/Feature Foundry state was `BLOCKED, 6/13 hard gates`.

Passing:

- exact dependency evidence;
- runtime integrity;
- daemon contract;
- UI contract;
- fresh checkpoint;
- remote publication.

Blocking:

- exact Node `26.7.0` unavailable in that environment;
- pnpm `11.21.0` unavailable;
- `pnpm-lock.yaml` absent;
- strict parity incomplete;
- exact full production build proof unavailable;
- production browser smoke unavailable;
- production desktop smoke unavailable.

Do not rewrite this historical blocked state as if it were the current v24 release status. The current standalone v24 repository has its own successful build, browser verification, native release, lockfile, and release artifacts.

### V2 strict parity history

V2-253 recorded:

- `433` discovered identifiers;
- `417` high-confidence candidates;
- `239` migrated request contracts;
- `178` pending candidates;
- `16` ambiguous identifiers.

Preserve this as GameSync/V2 continuity evidence if those cross-product contracts are resumed.

## Troubleshooting

### Repository still described elsewhere as a placeholder

That statement is obsolete for the current production-app source. `Herbertofury/Feature-Foundry` now contains the complete v24 source and is the canonical product repository. Older recovery/checkpoint documents may still preserve the placeholder-era history.

### Running the wrong Feature Foundry artifact

Verify the loaded source/release identity. Historical V33 HTML, GameSync/V2 recovery checkpoints, generated starter bundles, and current v24 are different evidence lanes.

For current production-app work, start from the current Feature-Foundry repository or the verified v24 source ZIP.

### `npm run verify` fails before browser UI testing

Fix the failing contract, authority, typecheck, production build, or Rust check first. Do not skip an earlier gate and count `test:ui` alone as release verification.

### Tauri build succeeds but packaging fails

`npm run package` requires native installable files under the Tauri release bundle directory. Run `npm run desktop:build`, confirm the platform prerequisites, then package again. The packager is intentionally fail-closed if no MSI/EXE/DMG/AppImage/DEB/RPM is present.

### Release hash differs from the manifest

Stop using that artifact as canonical. Re-download the expected release file, confirm exact filename/version, and compare against the SHA-256 values documented above. Do not overwrite a known-good release with an unmatched same-name file.

### World snapshot does not persist

Confirm the native Tauri build is running, the application data directory is writable, the state sent to `save_world_snapshot` is valid JSON, and restart from the same native application identity. Browser-only Vite sessions do not prove native snapshot persistence.

### Spotify callback never arrives

Confirm the native application can bind a loopback port, the provider application accepts the loopback callback form, the returned OAuth state matches the initiating state, and the callback is not being tested from a browser-only build that lacks the Tauri command.

### Apple Music playback/account control is unavailable

Confirm a valid server-issued developer token and MusicKit configuration. Keep the signing private key on the protected server; do not embed it in Feature Foundry.

### A media URL does not render

Check whether the source is a supported local file, direct HTTPS media URL, or privacy-enhanced YouTube path, and inspect the Tauri CSP/media/frame restrictions. Do not widen CSP indiscriminately just to make an unrelated URL load.

### A V33 feature appears absent in v24

Treat that as a regression candidate, not permission to delete the V33 record. Reproduce the exact V33 behavior, identify whether v24 intentionally replaced it, and require equal-or-better verified behavior before marking the old capability superseded.

### Project Vault or V2 agent features are absent from v24

That is currently an authority-lane distinction, not proof of a broken v24 release. Those capabilities live in the preserved GameSync/Feature Foundry V2 continuity line unless a later current Feature-Foundry repository revision integrates them.

## Contribution and change qualification

For a normal production-app change:

1. resolve current `main` and record the exact starting commit;
2. run the current baseline workflow before broad edits;
3. change the narrowest owning module;
4. preserve the V24 contract unless intentionally superseding it;
5. update/extend authority or UI tests for changed behavior;
6. run `npm run verify`;
7. when native behavior changed, run the real native application;
8. when stateful behavior changed, restart and verify persistence;
9. when release packaging changed, run `npm run desktop:build` and `npm run package`;
10. verify generated artifact hashes and fresh extraction/install where applicable;
11. compare affected user-facing behavior against the V33 non-regression benchmark where relevant;
12. publish only after exact-source and exact-artifact evidence agree.

## Exact next actions

The production application is no longer blocked on recovering a canonical repository. Current next work should start from `Herbertofury/Feature-Foundry` v24.0.0 and focus on evidence-backed product evolution rather than repository reconstruction.

Highest-value qualification actions are:

1. preserve v24 as the known-good release baseline and record the exact starting source commit before new work;
2. re-run `npm run verify` and native smoke on the exact current head when modifying the product;
3. keep release artifact SHA-256 and Drive/GitHub publication identity synchronized;
4. run explicit restart/state tests for snapshot, SQLite soundtrack/history, and provider configuration changes;
5. compare any world/ecology/workspace changes against the preserved V33 behavior baseline;
6. reconcile selected V2-253 Project Vault/Improvement Radar/agent-operation capabilities only through explicit product decisions and current-source implementation, never by merely claiming they are present.

## Evidence index

Current source/release:

- [Feature Foundry repository](https://github.com/Herbertofury/Feature-Foundry)
- [Feature Foundry v24.0.0 release](https://github.com/Herbertofury/Feature-Foundry/releases/tag/v24.0.0)
- current release record: repository `progress.md`
- current product/run/configuration overview: repository `README.md`
- package/version/scripts/dependency contract: repository `package.json`
- native product/window/security contract: `src-tauri/tauri.conf.json`
- native Rust/dependency contract: `src-tauri/Cargo.toml`
- native commands/snapshot/OAuth integration: `src-tauri/src/lib.rs`
- deterministic release packaging: `scripts/package-release.ps1`
- canonical Drive release folder: `1eU95XQZNq-3mc9HvY08JbClSBTu7tXYY`
- Drive checksum manifest: `18c325aHLh9Kue8oTz0_KS4yNTtXShRxC`

Historical continuity:

- Feature Foundry V2 Continuity recovery ledger: Drive document `1AES2lZ6GFfpdBFZdSX4XXy-FbGQxPKGrXFLJjM67Smg`
- V2-253 exact delta document: Drive document `1vDJ4IDn2FvTS5hYH4-A_HC80VgaNe9poBmIOOo9JGyk`
- V33 FINAL_READY remote artifact ID: `1_mLbBXiS0yL7g2cKP7qQJxqyyRHP4RSY`

## Wiki maintenance

Update this page when any of the following changes materially:

- canonical Feature-Foundry repository head/release identity;
- product version;
- V24 successor contract;
- V33 authority counts or their current-source integration;
- artist-world authority;
- runtime/render architecture;
- media or Music Hub providers;
- native commands, SQLite schema, snapshot behavior, or OAuth flow;
- Node/TypeScript/Vite/Three/Tauri/Rust floors;
- verification commands or observed release evidence;
- release artifacts, hashes, or Drive/GitHub publication location;
- Project Vault/V2 continuity becomes integrated into current Feature-Foundry source;
- a newer runnable release supersedes v24 with equal-or-stronger verified behavior.

Preserve current-source facts, V33 benchmark evidence, and V2 continuity as separate authority lanes until a later verified implementation legitimately unifies them.