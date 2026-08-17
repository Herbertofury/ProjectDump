# PRJ-012 - Sims 4 Native DX11 Overlay Mod

**Project Constellation ID:** `PRJ-012`  
**Status:** SPEC / relationship unresolved  
**Recovered architecture:** native Windows C++ / DirectX 11 / Dear ImGui overlay concept  
**Current source boundary:** no canonical repository or runnable DLL has been resolved in connected GitHub/Drive state.

## Purpose

Provide a native DirectX 11 telemetry/control overlay for The Sims 4, most plausibly as an instrumentation module inside the Sims 4 Accelerator rather than as an independent product. The relationship remains unresolved until original source or explicit user direction proves otherwise.

## Current graphics baseline

DirectX 11 is now the default Sims 4 renderer for NVIDIA, AMD, and Intel GPUs according to Electronic Arts' September 2024 and August 2025 updates. This makes DX11 the primary overlay compatibility target for mainstream Windows systems in 2026.

Primary sources:

- https://www.ea.com/en/games/the-sims/the-sims-4/news/update-9-18-2024
- https://www.ea.com/en/games/the-sims/the-sims-4/news/update-8-19-2025

The overlay must still detect the actual renderer at runtime and fail closed if the expected DX11 swap-chain path is not present.

## Current library research, checked 2026-08-17

### Dear ImGui

Current stable release observed: **v1.92.9**, released July 25, 2026.

Source:

- https://github.com/ocornut/imgui/releases

Dear ImGui remains a strong fit for a diagnostic overlay because it emits vertex/index data and draw-call batches while leaving graphics API integration to the host/backend. It is a UI layer, not a hooking or telemetry solution.

### PresentMon

Current release observed: **v2.4.1**.

Source:

- https://github.com/GameTechDev/PresentMon/releases

Use PresentMon as an external ground-truth comparison so the in-process overlay cannot validate itself with its own timing path.

### DirectX Tool Kit for DirectX 11

Current Microsoft release observed: **May 7, 2026 / NuGet 2026.5.8**.

Source:

- https://github.com/microsoft/DirectXTK/releases

DirectXTK is an optional helper for DX11 resource/device utilities. It should not be introduced merely because it is current; adopt only if the recovered overlay source needs functionality that would otherwise be reimplemented.

### Hooking alternatives

Current research candidates:

- MinHook current release line: `v1.3.4`, https://github.com/TsudaKageyu/minhook/releases
- Microsoft Detours current tagged release: `v4.0.1`, https://github.com/microsoft/Detours/releases

Do not choose a hook library before recovering the existing architecture. If the historical source already has a working hook path, first baseline it with hooks disabled and enabled, then compare a migration only if there is a measurable correctness, compatibility, or maintainability gain.

## Anti-regression contract

The overlay must never become a prerequisite for the game to launch. Required failure behavior:

- if injection/load fails, the unmodified game remains launchable;
- if DX11 device/swap-chain discovery fails, overlay rendering disables itself without corrupting game state;
- hook disable mode must be genuinely pass-through;
- no overlay control may imply an optimization succeeded until external telemetry confirms it;
- overlay initialization and shutdown must be repeatable across full game restarts;
- input capture must not steal gameplay input when the overlay is closed;
- window/fullscreen/borderless/resolution changes must not orphan resources or crash the game.

## Minimal architecture experiment

After source recovery, test one narrow diagnostic overlay before optimization controls:

1. attach to the exact game build;
2. identify the real D3D11 device/context/swap chain;
3. render a read-only panel with build identity, renderer, frame timing, and hook status;
4. compare displayed timing to a simultaneous PresentMon capture;
5. toggle the panel open/closed repeatedly;
6. change resolution/window mode;
7. load a fixed save and zone;
8. restart the game and repeat;
9. inspect logs for leaked resources, double-hooking, device-reset failures, and input capture errors.

## Relationship decision gate

Until stronger evidence appears, treat this project as a **module candidate inside PRJ-011 Sims 4 Accelerator**. Keep PRJ-012 as a tracked continuity record because the 63-project catalog is fixed, but avoid a second independent hook stack.

Promote it to a separate product only if recovered project-owned evidence shows separate scope, lifecycle, packaging, or user intent.

## Exact next action

Locate the original overlay prompt/source and determine whether its hooks already live inside the Sims 4 Accelerator scaffold. Then establish a read-only DX11 telemetry overlay and compare it against PresentMon before exposing any optimization control.

## Wiki maintenance

Update when source identity is resolved, library versions are actually adopted, renderer-hook behavior is runtime-proven, or the relationship to PRJ-011 changes.