# PRJ-010 - RuneLite FlipForge / Farm Material Ranker / No-Hitch / 117HD Family

**Project Constellation ID:** PRJ-010  
**Tracked state:** ACTIVE, release blocker  
**Confidence:** Medium  
**Current connected GitHub publication point:** `Herbertofury/FlipForge`  
**Current repository state:** placeholder only, not a recovered implementation source

## Purpose

PRJ-010 is the RuneLite project family that groups the user-facing **FlipForge** work with the Farm Material Ranker, a Rust dashboard/bridge track, the No-Hitch RuneLite launcher/runtime, and 117HD/RLHD integration work.

The defining release requirement is stronger than compilation or developer-mode loading: the relevant external plugins must be visible, enabled, functional, and persistent in the **actual Jagex-launched RuneLite client after restart**.

## Current source-of-truth status

### Connected GitHub repository

The connected repository `Herbertofury/FlipForge` currently contains only:

- `README.md`

The README content is only `# FlipForge`. The repository was created on 2026-08-15, reports repository size `0`, has no detected language, and its only observed commit is the initial commit `03cb2057c480929831852fed8fd866954e3ad5c0`.

This means the connected repository is presently a **project identity/publication placeholder**, not sufficient evidence for the current implementation, build system, dependency graph, plugin descriptors, Rust bridge, or release packaging.

Do not invent Gradle, Maven, Cargo, launcher, or RuneLite installation commands from this placeholder. Recover the project-owned implementation first.

## Durable recovered project lineage

Project Constellation preserves the following components for this family:

- `flipfore-osrs` historical/internal naming with **FlipForge** as the user-facing name;
- Farm Material Ranker;
- Rust dashboard/bridge;
- No-Hitch RuneLite launcher/runtime;
- 117HD / RLHD integration.

Related durable RuneLite planning/reference artifacts include:

- `RuneLite_Master_Prompt_Smart_No_BS.md`
- `RuneLite_Codex_Master_Prompt_No_Logging.md`
- `runelite_flipping_codex_master_prompt(4).md`
- `RuneLite_External_Plugins_Codex_Prompt_CLEANED(7).md`

These are continuity evidence and requirements references. They are not substitutes for the missing canonical implementation source.

## Farm Material Ranker

### Latest recovered standalone identity

The latest durable Project Constellation record identifies **Farm Material Ranker v1.1.0**.

Recovered capabilities are:

- searchable RuneLite sidebar;
- OSRS / Grand Exchange pricing;
- item icons;
- sorting;
- monster metadata;
- shortest-path routing.

Recovered artifact name:

- `farm-material-ranker.zip`

### Verification boundary

The current connected GitHub state does not contain the Farm Material Ranker source or release ZIP, and the current Drive search resolves references to the artifact through Project Constellation continuity material rather than a separately retrievable canonical release artifact.

Therefore this wiki does **not** claim a fresh build, plugin load, data refresh, pricing lookup, route calculation, or restart-persistence test for v1.1.0.

## No-Hitch RuneLite reference runtime

Project Constellation preserves an exact known-good reference identity:

| Field | Verified durable value |
| --- | --- |
| Artifact | `hitchless-runelite-main.jar` |
| SHA-256 | `80d99e72d82ad28a5fe7779d7325450b487edb2c9c1f617b2e75acfa39f61d89` |
| Size | `57,842,944` bytes |
| Main class | `com.bertsplugins.hitchless.HitchlessRuneLiteMain` |
| Embedded RuneLite | `1.12.29.1` |
| Recorded source commit | `68ff80e` |

This identity is valuable as a **latest-known-good reference artifact**, not proof that the current connected FlipForge repository can rebuild it.

### Preservation rule

Do not replace or relabel a newly found launcher/JAR as the known-good reference solely because its filename or version appears newer. Compare at minimum:

1. artifact SHA-256;
2. embedded RuneLite identity;
3. main class and launcher behavior;
4. source commit/lineage when available;
5. external-plugin loading behavior;
6. restart persistence in the real target client.

## 117HD / RLHD relationship

117HD/RLHD is preserved as part of the PRJ-010 family because the project has historically combined RuneLite launcher/runtime work with external plugins and rendering integration.

The current connected FlipForge repository does not expose enough implementation source to document:

- the exact 117HD dependency version;
- whether 117HD is bundled, dynamically discovered, or externally installed;
- compatibility patches;
- GPU/backend configuration;
- plugin descriptor or injector wiring.

Those details remain unresolved until the canonical implementation source or exact release artifact is recovered.

## Intended project architecture

The durable record supports this **family-level** architecture, but not exact current module boundaries:

```text
Jagex launcher / real RuneLite client
          |
          v
No-Hitch RuneLite runtime / launcher layer
          |
          +--> FlipForge external plugin
          |
          +--> Farm Material Ranker external plugin
          |
          +--> 117HD / RLHD integration
          |
          +--> Rust dashboard / bridge
```

The critical architecture rule is that a successful standalone build or developer-mode launch is only an intermediate check. The final release path terminates in the actual Jagex-launched client and must survive restart.

## Release qualification contract

A PRJ-010 release is not complete until the exact candidate artifact has evidence for all applicable stages below.

### 1. Identity

Record:

- repository/worktree/branch;
- source commit;
- artifact filename;
- SHA-256;
- file size;
- embedded RuneLite version where applicable;
- plugin versions;
- Rust bridge/dashboard version where applicable.

### 2. Clean build

Once the actual source is recovered, document and execute the **project-owned** build commands from its manifests or wrapper scripts. Do not infer commands from generic RuneLite conventions.

Required evidence should include:

- clean dependency resolution;
- compilation;
- unit/integration tests supplied by the project;
- generated plugin descriptors/resources;
- packaged JAR/ZIP integrity.

### 3. Developer/runtime smoke test

Use this as an intermediate diagnostic only:

- application launches;
- plugin class discovery succeeds;
- plugin UI opens;
- obvious startup exceptions are absent;
- Farm Material Ranker can render its sidebar/data surfaces;
- FlipForge can expose its actual user workflow;
- 117HD/RLHD integration does not break startup.

Passing this stage does **not** clear the release blocker.

### 4. Jagex-launched client proof

This is the project family's hard release gate.

For every external plugin being shipped:

- launch RuneLite through the real Jagex-supported path used by the user;
- verify the plugin appears in the client;
- enable it;
- exercise its primary workflow rather than only observing the settings entry;
- verify required data/network/UI behavior;
- close the client cleanly;
- relaunch through the same Jagex path;
- verify the plugin is still present;
- verify enabled/settings state persists;
- re-run a representative workflow after restart.

The durable Project Constellation record explicitly states that **JAR inspection, compilation, or developer-mode loading alone is insufficient**.

## Farm Material Ranker qualification

When the v1.1.0 source/artifact is recovered, test at minimum:

- sidebar availability;
- search behavior;
- item icon loading;
- price lookup/display;
- sorting;
- monster metadata display;
- shortest-path route generation;
- empty/offline/error states;
- repeated use without duplicate panels or stale state;
- restart persistence where the plugin stores settings/state.

Any current OSRS/GE data-source assumptions must be re-read from the actual source before documenting provider URLs, cache intervals, or API requirements.

## FlipForge qualification

The current repository name establishes the project identity but not the feature contract. Before documenting user instructions, recover either the canonical source or a verified release and inventory its visible features.

Then document and test each user-facing action end-to-end:

- promised flipping workflow;
- market/item search;
- pricing or profitability calculations;
- saved/watchlisted state if present;
- external dashboard/bridge behavior if present;
- error handling;
- persistence after restart.

Do not use the existence of a button, panel, or plugin entry as proof that the promised workflow works.

## Rust dashboard / bridge

The durable record says a Rust dashboard/bridge is part of the family, but the current GitHub repository does not contain Cargo manifests or Rust source.

Before adding build instructions, recover and inspect:

- `Cargo.toml` / workspace manifests;
- bridge protocol or IPC transport;
- bind addresses/ports if any;
- authentication/session model if any;
- RuneLite-side client code;
- persistence/schema files;
- shutdown/reconnect behavior.

Document the actual protocol rather than guessing whether it is HTTP, WebSocket, native IPC, files, or another mechanism.

## Installation

### Current truthful state

A complete installation procedure cannot yet be published from current connected source because the `Herbertofury/FlipForge` repository contains no implementation artifacts beyond the README.

The correct next recovery step is to locate the latest verified FlipForge/Farm Material Ranker/No-Hitch source or release artifacts, reconcile them against the known-good identities above, and only then publish exact installation steps.

### What not to do

Do not:

- initialize a replacement RuneLite plugin project inside the placeholder repository;
- overwrite the known-good JAR identity with an unverified newer file;
- claim Plugin Hub/Jagex-client compatibility from developer-mode success;
- assume Farm Material Ranker v1.1.0 build commands without its manifest;
- assume 117HD dependency or configuration versions;
- invent Rust bridge ports or commands.

## Troubleshooting

### FlipForge repository has no source

This is the current verified condition. Search project-owned Drive artifacts, prior release archives, local canonical worktrees, and exact artifact hashes before creating new code. The repository placeholder should not be treated as permission to restart the project.

### Plugin works in developer mode but not the normal client

The release blocker remains open. Reproduce using the exact Jagex-launched flow, record the loaded client/runtime identity, inspect external-plugin discovery, and verify that the plugin artifact is installed where that runtime actually discovers it.

### Plugin disappears after restart

Treat persistence as failed even if the first launch worked. Capture:

- plugin installation location;
- client profile/account context;
- enabled-state storage;
- launcher path;
- before/after artifact identity;
- startup logs/errors.

### Farm Material Ranker data is stale or empty

Do not change providers based on assumptions. First recover the exact v1.1.0 source, identify its pricing/data adapters, reproduce the failure, then update the provider integration and its tests together.

### 117HD changes break the client

Keep renderer/plugin changes isolated from FlipForge/Farm Material Ranker qualification. Prove the base external-plugin path first, then add the rendering integration and compare startup, frame behavior, UI, and restart persistence.

## Contribution and modification workflow

Until source recovery is complete, contribution work is primarily **continuity recovery and verification**, not implementation.

For each recovered candidate:

1. preserve the original bytes;
2. compute SHA-256 and size;
3. inspect embedded version/manifest metadata;
4. identify repository/worktree lineage when possible;
5. compare against the known-good hitchless JAR and Farm Material Ranker v1.1.0 record;
6. classify it as historical, candidate, latest-known-good, or superseding verified state;
7. only then publish source or documentation updates.

Once implementation source is restored to the canonical repository, expand this wiki with:

- exact prerequisites;
- repository layout;
- Gradle/Maven/Cargo commands actually present in the source;
- plugin descriptors and injection points;
- configuration files and schemas;
- dashboard/bridge protocol;
- test suites;
- packaging/release commands;
- real client installation paths verified by runtime testing.

## Current blockers

1. `Herbertofury/FlipForge` is currently a one-file placeholder rather than the implementation repository.
2. The Farm Material Ranker v1.1.0 ZIP is referenced in durable continuity state but was not independently recovered from current connected Drive search during this documentation pass.
3. The known-good No-Hitch JAR identity is preserved, but the corresponding buildable source is not present in the connected FlipForge repository.
4. The Rust dashboard/bridge implementation is not present in the connected repository.
5. 117HD/RLHD wiring is not present in the connected repository.
6. The real Jagex-launched external-plugin and restart-persistence release gate remains unresolved in the durable project record.

## Exact next documentation checkpoint

Recover the latest PRJ-010 implementation/release artifacts, starting with FlipForge source, `farm-material-ranker.zip`, and the source matching No-Hitch commit `68ff80e`. Reconcile hashes and manifests without overwriting the known-good reference, restore the canonical source repository, then replace the recovery-only sections of this wiki with exact build/install/configuration/API/module documentation backed by that source.
