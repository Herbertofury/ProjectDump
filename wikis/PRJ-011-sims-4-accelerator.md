# PRJ-011 - The Sims 4 Accelerator

**Project Constellation ID:** `PRJ-011`  
**Status:** SPEC / SCAFFOLD  
**Recovered authority:** `TS4_ACCELERATOR_AGENT_PLAN.md` plus starter workspace README  
**Source boundary:** no canonical runnable repository or current build has been resolved in the connected GitHub/Drive state.

## Goal

Build a Windows-only Sims 4 performance project focused on large Mods/Overrides startup cost, zone-load hitching and asset warmup, and DX11 frame pacing/render-thread overhead while preserving the real Mods library and proving gains against the exact user's game state.

## Historical acceptance contract

The recovered project record requires:

- measure before internal patching;
- preserve the real Mods folder;
- start with pass-through projection and externalized bottlenecks;
- benchmark graphics/runtime modes rather than assuming one is faster;
- stop if projection is slower, content compatibility breaks, or a native component crashes even with hooks disabled.

These constraints remain stronger than any new optimization idea.

## Current Sims 4 graphics baseline, checked 2026-08-17

Electronic Arts moved NVIDIA and AMD players to DirectX 11 by default in September 2024 and moved Intel GPU players to DirectX 11 by default in the August 19, 2025 update. The 2025 update also included additional rendering and responsiveness optimizations. EA's 2026 Quality of Life program continues to prioritize stability and performance.

Implication: the old plan's DX9-versus-DX11 comparison should no longer assume DX9 is the normal baseline on NVIDIA, AMD, or Intel systems. The benchmark harness should detect and record the actual loaded renderer/runtime for every run. DX9 remains a compatibility comparison only where the installed game/hardware still exposes it.

Primary sources:

- https://www.ea.com/en/games/the-sims/the-sims-4/news/update-9-18-2024
- https://www.ea.com/en/games/the-sims/the-sims-4/news/update-8-19-2025
- https://www.ea.com/en/games/the-sims/the-sims-4/news/the-sims-4-quality-of-life-roadmap-2026

## Current measurement candidate

Intel/GameTechDev PresentMon is a strong external frame-pacing baseline because it records presentation timing without requiring a Sims 4 code hook. Current release observed in this pass: **PresentMon v2.4.1**.

Source:

- https://github.com/GameTechDev/PresentMon/releases

Use PresentMon before invasive changes to capture at minimum:

- presented FPS and frame-time distributions;
- CPU/GPU timing fields that are reliable on the current HAGS state;
- process identity;
- test scenario name;
- cold/warm startup distinction;
- renderer identity;
- pack/mod profile identity;
- zone/load transition markers.

PresentMon's own documentation warns that some GPU execution metrics are less accurate with Hardware-Accelerated GPU Scheduling enabled, so the benchmark ledger must record HAGS state rather than treating all GPU timing columns as equally authoritative.

## Baseline experiment before hooks

Create one reproducible matrix from an unchanged game install and unchanged real Mods folder:

1. cold launch to main menu;
2. main menu to a fixed save;
3. fixed save to a fixed lot/zone;
4. repeat zone transition;
5. representative gameplay frame-pacing capture;
6. repeat after a clean restart.

For each run record game build, expansion/pack selection, mod count/bytes, Overrides count/bytes, shader/cache state, GPU/driver, Windows build, HAGS, renderer, Memory Boost/related game performance options, PresentMon version, median/p95/p99 frame times, launch/load durations, crashes/errors, and a hash of the benchmark configuration.

## Performance direction

Prefer optimizations that externalize or amortize known work before patching internal game functions. Candidate categories include:

- deterministic mod/package inventory and duplicate/conflict scanning outside the game;
- cache/warmup evidence rather than blind cache deletion;
- startup I/O profiling;
- immutable Mods projection experiments that preserve original bytes;
- asset/cache precomputation only when the game's observed access pattern proves a benefit;
- frame-pacing diagnosis using external telemetry before native render hooks.

Do not reduce content, hide mods, lower media quality, disable required packs, or use a smaller test library to manufacture a speedup.

## Relationship to PRJ-012

`PRJ-012 Sims 4 native DX11 overlay mod` is currently a relationship-unresolved C++/DX11 telemetry/control concept. Treat it as an optional measurement/control module for this project unless recovered source or explicit user direction proves it is a separate product.

Do not duplicate render hooks across two repositories before identity is resolved.

## Current implementation boundary

This pass found no canonical TS4 Accelerator repository and no current executable artifact. Therefore no code migration or hook-library upgrade is being applied. The next useful improvement is a baseline harness and exact source recovery, not speculative DLL work.

## Exact next action

Recover the canonical TS4 Accelerator workspace/source, then run the full unchanged-game baseline matrix above before adding or changing native hooks. Preserve the real Mods folder read-only during benchmark setup and record exact source/build identity before any implementation change.

## Wiki maintenance

Update when canonical source is resolved, the benchmark matrix is executed, the Sims 4 renderer/performance baseline changes, a native hook is implemented, or a measured optimization passes full mod-compatibility and restart regression tests.