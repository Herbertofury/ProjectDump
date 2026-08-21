# PRJ-011 - The Sims 4 Accelerator

**Project Constellation ID:** `PRJ-011`  
**Status:** SPEC / SCAFFOLD  
**Recovered authority:** `TS4_ACCELERATOR_AGENT_PLAN.md` plus starter workspace README  
**Current source boundary:** no canonical runnable repository or current build has been resolved in the connected GitHub/Drive state.

## Goal

Build a Windows-only Sims 4 performance project focused on large Mods/Overrides startup cost, zone-load hitching and asset warmup, and DX11 frame pacing/render-thread overhead while preserving the real Mods library and proving gains against the exact user's game state.

This is an evidence-first accelerator project. It is not permission to delete, hide, disable, downsample, virtualize away, or silently rewrite user content to manufacture benchmark wins.

## Historical acceptance contract

The recovered project record requires:

- measure before internal patching;
- preserve the real Mods folder;
- start with pass-through projection and externalized bottlenecks;
- benchmark graphics/runtime modes rather than assuming one is faster;
- stop if projection is slower, content compatibility breaks, or a native component crashes even with hooks disabled.

These constraints remain stronger than any new optimization idea.

## Current implementation boundary

No canonical TS4 Accelerator repository, current executable, injected DLL, or exact starter-workspace source tree is currently resolved through the connected GitHub/Drive evidence. The durable plan is therefore **architecture and recovery evidence**, not proof that ProjFS, WinFsp, ETW capture, package indexing, native hooks, or renderer acceleration are implemented.

Until source identity is recovered, do not:

- initialize a replacement repository under the same project identity;
- claim a launcher/provider/DLL exists;
- choose a hook library merely because it is newer;
- mutate the real Mods folder;
- publish performance claims without exact workload and tool versions.

## Current Sims 4 graphics baseline

Electronic Arts moved NVIDIA and AMD players to DirectX 11 by default in September 2024 and moved Intel GPU players to DirectX 11 by default in the August 19, 2025 update. The 2025 update also included rendering and responsiveness work, and EA's 2026 Quality of Life program continues to prioritize stability and performance.

Primary sources:

- https://www.ea.com/en/games/the-sims/the-sims-4/news/update-9-18-2024
- https://www.ea.com/en/games/the-sims/the-sims-4/news/update-8-19-2025
- https://www.ea.com/en/games/the-sims/the-sims-4/news/the-sims-4-quality-of-life-roadmap-2026

### Benchmark implication

The old plan's DX9-versus-DX11 comparison must no longer assume DX9 is the normal baseline on NVIDIA, AMD, or Intel systems. The harness must detect and record the renderer actually loaded for every run. DX9 is a compatibility comparison only where the installed game and hardware still expose it.

## External frame-time authority: PresentMon 2.5.1

The current GameTechDev PresentMon release line observed on 2026-08-21 is **v2.5.1**:

- https://github.com/GameTechDev/PresentMon/releases

This supersedes the older v2.4.1 measurement note on this page.

PresentMon remains the preferred first external frame-pacing baseline because it observes presentation timing without requiring a Sims 4 code hook. That independence matters: an in-process accelerator or overlay must not validate itself with only its own timing path.

### Why the 2.5 line matters to this project

PresentMon 2.5.0 changed enough metric behavior that the exact collector version is part of the benchmark identity. Its release notes include:

- corrected frame metric calculations for CPU busy/wait times;
- corrected percentile calculations, including a historical case where a requested 99% percentile could effectively report MAX rather than the intended percentile;
- stricter query-registration validation;
- improved ETW session/provider lifecycle handling;
- device-model changes for CPU metrics.

PresentMon 2.5.1 then fixed percentile ordering for FPS and a backward-compatibility regression in the PresentMon API.

### Comparability rule

Do **not** merge old v2.4.x percentile summaries and new v2.5.x summaries into one performance trend as if the collector were unchanged.

For every measurement run preserve:

- PresentMon version and executable hash when practical;
- the raw CSV/ETL or equivalent raw capture used to derive summaries;
- exact metric names and units;
- the command/config used to collect them;
- benchmark scenario and run ID.

If a historical result matters to a release decision, prefer recomputing percentiles from preserved raw frame data under one analysis method. If raw data is unavailable, retain the result as historical evidence and label the collector version rather than silently normalizing it.

### HAGS boundary

PresentMon's documentation still warns that several GPU execution metrics are less accurate with Hardware-Accelerated GPU Scheduling enabled. Record HAGS state for every run and do not treat `msUntilRenderStart`, `msUntilRenderComplete`, `msGPUActive`, or `msGPUVideoActive` as identical-quality evidence across HAGS states.

## Baseline experiment before hooks

Create one reproducible matrix from an unchanged game install and unchanged real Mods folder:

1. cold launch to main menu;
2. main menu to a fixed save;
3. fixed save to a fixed lot/zone;
4. repeat the same zone transition;
5. representative gameplay frame-pacing capture;
6. repeat after a clean game restart;
7. repeat the whole matrix with the accelerator disabled once implementation exists.

For each run record at minimum:

- game build and renderer;
- expansion/pack selection;
- Mods file count and total bytes;
- Overrides file count and total bytes;
- a stable inventory hash of the tested mod profile;
- shader/cache state;
- GPU/driver and Windows build;
- HAGS state;
- Memory Boost or related game performance options;
- PresentMon version;
- raw capture identity;
- median/p95/p99 frame times calculated by the chosen analysis method;
- launch/load durations;
- zone-transition markers;
- crashes/errors;
- benchmark configuration hash.

### Cold versus warm runs

A cold launch and a warm repeat are different workloads. Keep them separate. Do not average them into one number that hides cache effects.

When changing cache/prewarming behavior, preserve the pre-run cache state explicitly so an accelerator is not credited for operating on a warmer machine state than the control.

## Startup and I/O measurement ladder

Use the least invasive evidence that can answer the question.

### Level 1 - filesystem inventory

Before adding a projection provider, create an immutable manifest of the exact tested Mods/Overrides tree:

- normalized relative path;
- byte size;
- modification timestamp as descriptive metadata only;
- content hash for identity-critical comparisons;
- extension/type;
- archive/package classification where known.

Do not infer identity from timestamp alone.

### Level 2 - external process and frame timing

Use PresentMon plus launch/zone markers to identify whether the dominant user-visible problem is startup time, zone transition, steady-state frame pacing, or a combination.

### Level 3 - Windows I/O/ETW evidence

Use ETW/WPA or equivalent Windows tracing when file-open volume, read amplification, path churn, or decompression appears to dominate. Preserve trace configuration and exact process identity.

### Level 4 - projection experiment

Only after the baseline proves startup I/O is a material bottleneck should the project compare an immutable projected Mods tree against native access.

### Level 5 - native hooks

Internal function/render hooks are the last resort, not the starting point. Require evidence that externalized approaches cannot address the measured bottleneck.

## ProjFS projection lane

The recovered architecture prefers **Windows Projected File System (ProjFS)** before the WinFsp fallback.

Microsoft's current ProjFS documentation describes a user-mode provider projecting hierarchical data from a backing store into a filesystem namespace. Microsoft also states that ProjFS is designed around a **high-speed backing data store** and is not intended to provide slow-remote-storage recall progress semantics.

Primary documentation:

- https://learn.microsoft.com/en-us/windows/win32/projfs/projected-file-system
- https://learn.microsoft.com/en-us/windows/win32/projfs/projfs-programming-guide
- https://learn.microsoft.com/en-us/windows/win32/projfs/enabling-windows-projected-file-system

### Enablement

ProjFS ships as an optional Windows component. Microsoft documents this elevated PowerShell enablement command:

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Client-ProjFS -NoRestart
```

Reboot only if Windows reports that a restart is required.

This is an environment prerequisite, not an installer action the project should perform silently.

### Sims 4 projection safety contract

The first provider prototype must be **pass-through and immutable**:

- the backing Mods tree remains the user's authority;
- the provider must never rewrite or delete original mod bytes;
- projected paths must resolve deterministically to the same content as native paths;
- unsupported writes must fail visibly or be redirected only through an explicitly designed writable layer;
- provider crash/stop must leave the original Mods library untouched;
- startup with the provider disabled must remain available as the control lane.

### Required projection acceptance

Before calling ProjFS a win, compare projected and native runs using the same mod inventory and benchmark state. Require:

- identical visible mod/content availability;
- identical inventory identity at the game-facing namespace;
- no missing package/script content;
- no duplicate path exposure;
- no new load errors;
- startup and zone-load measurements that beat noise by a repeatable margin;
- clean provider shutdown and restart;
- original Mods bytes unchanged after the entire run.

If projection is slower or compatibility changes, keep the result as rejected evidence and return to the native path.

## WinFsp fallback lane

The historical plan names WinFsp as a fallback when ProjFS is unsuitable.

Current WinFsp release research on 2026-08-21 shows:

- **WinFsp 2025** as the latest stable-labelled release on GitHub;
- **WinFsp 2026 Beta4 / v2.2B4** as the newest pre-release observed, released August 3, 2026.

Source:

- https://github.com/winfsp/winfsp/releases

The 2026 beta line includes fixes for issues the project must not ignore when evaluating a filesystem fallback, including fixes identified as CVE-2026-3006 and CVE-2026-7162 in the beta series plus cached-write/notification deadlock fixes in that line.

### WinFsp decision rule

Do not freeze a fallback implementation onto an old WinFsp package merely because it was used in an earlier scaffold. Also do not promote a pre-release build straight into production because it is newer.

Use two lanes:

1. **production candidate:** supported stable WinFsp build after security review;
2. **forward/security qualification:** current 2.2 beta only in an isolated test environment until compatibility, performance, upgrade/uninstall, and restart gates pass.

Record installer version and SHA-256 for every qualified runtime. Never download or update a filesystem driver silently as part of a Sims 4 benchmark.

## Projection comparison matrix

If source recovery reaches the projection phase, compare:

| Lane | Purpose | Required evidence |
| --- | --- | --- |
| Native Mods | control | unchanged real filesystem baseline |
| ProjFS pass-through | preferred projection | exact content parity + measured startup/load effect |
| WinFsp fallback | compatibility alternative | exact content parity + driver/runtime identity + measured effect |
| Staged/hardlink fallback | simplest non-provider fallback | exact file mapping + update/rebuild cost + measured effect |

Do not call a lane better merely because initial enumeration is faster. Measure the complete user path through launch, save load, zone transition, gameplay, shutdown, and restart.

## Performance direction

Prefer optimizations that externalize or amortize known work before patching internal game functions. Candidate categories include:

- deterministic mod/package inventory and duplicate/conflict scanning outside the game;
- cache/warmup evidence rather than blind cache deletion;
- startup I/O profiling;
- immutable Mods projection experiments that preserve original bytes;
- DBPF or script-package indexing only after access-pattern evidence supports it;
- asset/cache precomputation only when the observed workload proves a benefit;
- frame-pacing diagnosis using external telemetry before native render hooks.

Do not reduce content, hide mods, lower media quality, disable required packs, or use a smaller test library to manufacture a speedup.

## Relationship to PRJ-012

`PRJ-012 Sims 4 Native DX11 Overlay Mod` remains a relationship-unresolved C++/DX11 telemetry/control concept. Treat it as an optional measurement/control module inside this project unless recovered source or explicit user direction proves it is a separate product.

Do not duplicate render hooks across two repositories before identity is resolved.

## Recovery checklist

When the canonical workspace is found, record before editing:

- repository/worktree/path;
- Git remote, branch, and exact commit if applicable;
- starter README and plan hashes;
- launcher/provider/DLL project layout;
- package manifests and toolchain versions;
- existing projection backend and version;
- existing logging/benchmark outputs;
- prior release archives and hashes;
- any existing AGENTS/project-memory/checkpoint files.

If multiple copies exist, remain read-only until content identity and latest-good lineage are reconciled.

## First implementation milestone after recovery

The smallest complete milestone should be a **baseline harness**, not an injected optimization:

1. hash/inventory the unchanged test profile;
2. capture environment and renderer identity;
3. run the cold/warm startup and zone matrix;
4. capture raw PresentMon 2.5.1-or-later data;
5. preserve outputs with configuration hashes;
6. produce a machine-readable comparison report;
7. rerun after restart;
8. only then select the first measured bottleneck to attack.

### Baseline-harness acceptance

- no game/mod files changed;
- results are repeatable across at least three comparable runs per lane when practical;
- raw evidence is preserved, not only screenshots or summary averages;
- the report can distinguish environmental noise from a claimed improvement;
- every later optimization can be compared against this exact control state.

## Exact next action

Recover the canonical TS4 Accelerator workspace/source. Before implementing or migrating any hook or filesystem provider, run the unchanged-game baseline with **PresentMon 2.5.1 or later**, preserve raw captures and exact collector identity, then qualify ProjFS as a pass-through projection only if I/O evidence justifies it. Treat WinFsp as a separately versioned fallback lane with explicit security and driver qualification.

## Wiki maintenance

Update when canonical source is resolved, the benchmark matrix is executed, the Sims 4 renderer/performance baseline changes, PresentMon changes benchmark semantics again, a projection backend is adopted, a native hook is implemented, or a measured optimization passes full mod-compatibility and restart regression tests.
