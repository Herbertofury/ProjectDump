# PRJ-012 - Sims 4 Native DX11 Overlay Mod

**Project Constellation ID:** `PRJ-012`  
**Status:** SPEC / relationship unresolved  
**Recovered architecture:** native Windows C++ / DirectX 11 / Dear ImGui overlay concept  
**Current source boundary:** no canonical repository or runnable DLL has been resolved in connected GitHub/Drive state.

## Purpose

Provide a native DirectX 11 telemetry/control overlay for The Sims 4, most plausibly as an instrumentation module inside the Sims 4 Accelerator rather than as an independent product. The relationship remains unresolved until original source or explicit user direction proves otherwise.

The first legitimate milestone is a read-only, fail-closed diagnostic surface whose numbers can be cross-checked against an independent external collector. Optimization controls come later.

## Current graphics baseline

DirectX 11 is now the default Sims 4 renderer for NVIDIA, AMD, and Intel GPUs according to Electronic Arts' September 2024 and August 2025 updates. This makes DX11 the primary overlay compatibility target for mainstream Windows systems in 2026.

Primary sources:

- https://www.ea.com/en/games/the-sims/the-sims-4/news/update-9-18-2024
- https://www.ea.com/en/games/the-sims/the-sims-4/news/update-8-19-2025

The overlay must still detect the actual renderer at runtime and fail closed if the expected DX11 swap-chain path is not present.

## Current library research

### Dear ImGui

Current stable release rechecked on 2026-08-21: **v1.92.9**, released July 25, 2026.

Source:

- https://github.com/ocornut/imgui/releases

Dear ImGui remains a strong fit for a diagnostic overlay because it emits vertex/index data and draw-call batches while leaving graphics API integration to the host/backend. It is a UI layer, not a hooking or telemetry solution.

### External comparison authority: PresentMon 2.5.1

Current GameTechDev release rechecked on 2026-08-21: **v2.5.1**.

Source:

- https://github.com/GameTechDev/PresentMon/releases

This supersedes the old v2.4.1 note on this page.

Use PresentMon as an external ground-truth comparison so the in-process overlay cannot validate itself with only its own timing path.

#### Why the 2.5 line matters

PresentMon 2.5.0 changed metric behavior in ways directly relevant to an overlay-validation fixture:

- corrected CPU busy/wait frame calculations;
- corrected percentile calculation behavior, including a historical case where a requested 99% percentile could effectively behave like MAX;
- tightened query validation;
- improved ETW session/provider lifecycle handling;
- changed the device association used by CPU metrics.

PresentMon 2.5.1 then fixed FPS percentile ordering and a backward-compatibility regression in its API.

Therefore any overlay acceptance report must record the exact PresentMon version. Do not compare a v2.4.x percentile summary directly with a v2.5.x summary and attribute the difference to the overlay without preserving/recomputing the raw evidence.

#### Raw-evidence rule

For every validation run preserve:

- exact PresentMon version;
- raw CSV/ETL or equivalent capture;
- capture command/configuration;
- process ID/executable identity;
- selected metrics and units;
- HAGS state;
- overlay build identity;
- game build and renderer;
- scenario and run ID.

If old measurements matter, recompute from raw frame data with one analysis method when possible.

PresentMon also warns that several GPU execution metrics are less accurate under Hardware-Accelerated GPU Scheduling. The overlay must not claim sub-millisecond GPU-timing parity against fields whose external authority is itself known to shift with HAGS.

### DirectX Tool Kit for DirectX 11

Current Microsoft release rechecked on 2026-08-21: **May 7, 2026 / NuGet 2026.5.8**.

Source:

- https://github.com/microsoft/DirectXTK/releases

DirectXTK is an optional helper for DX11 resource/device utilities. It should not be introduced merely because it is current; adopt only if the recovered overlay source needs functionality that would otherwise be reimplemented.

### Hooking alternatives

Current research candidates:

- MinHook current release line: `v1.3.4`, https://github.com/TsudaKageyu/minhook/releases
- Microsoft Detours current tagged release: `v4.0.1`, https://github.com/microsoft/Detours/releases

Do not choose a hook library before recovering the existing architecture. If the historical source already has a working hook path, first baseline it with hooks disabled and enabled, then compare a migration only if there is a measurable correctness, compatibility, security, or maintainability gain.

## Anti-regression contract

The overlay must never become a prerequisite for the game to launch. Required failure behavior:

- if injection/load fails, the unmodified game remains launchable;
- if DX11 device/swap-chain discovery fails, overlay rendering disables itself without corrupting game state;
- hook-disable mode must be genuinely pass-through;
- no overlay control may imply an optimization succeeded until external telemetry confirms it;
- overlay initialization and shutdown must be repeatable across full game restarts;
- input capture must not steal gameplay input when the overlay is closed;
- window/fullscreen/borderless/resolution changes must not orphan resources or crash the game;
- a device-loss/recreation path must not double-install hooks or leak overlay resources;
- stale overlay DLLs must never be confused with the build under test.

## Read-only diagnostic milestone

After source recovery, implement or recover one narrow diagnostic overlay before optimization controls.

### Minimum panel

Display only source-backed state such as:

- overlay build/commit identity;
- detected renderer;
- D3D11 device/context/swap-chain status;
- window mode and back-buffer dimensions;
- overlay hook enabled/disabled state;
- frame timing derived from the overlay path;
- PresentMon comparison run ID or evidence link when a synchronized external capture is active.

Do not surface controls that claim to tune the game until their actual effect is implemented and independently measurable.

## Exact diagnostic acceptance matrix

1. launch the exact game build with the overlay disabled and record control behavior;
2. attach/load the candidate overlay build;
3. prove the loaded DLL/build identity;
4. identify the actual D3D11 device/context/swap chain;
5. render the read-only panel;
6. run a simultaneous PresentMon 2.5.1-or-later capture;
7. compare frame boundaries/timing under one documented method;
8. toggle the panel open/closed repeatedly;
9. verify keyboard/mouse input is unchanged while closed;
10. change resolution and window/fullscreen/borderless mode;
11. load a fixed save and transition to a fixed zone;
12. exercise pause/menu/gameplay transitions;
13. restart the game and repeat;
14. inspect logs for leaked resources, double-hooking, device-reset failures, stale handles, and input-capture errors;
15. rerun with the overlay or hooks disabled to prove the pass-through lane remains valid.

A single screenshot of the panel is not acceptance evidence.

## Timing comparison rules

The overlay and PresentMon observe different layers of the frame pipeline. Do not require numerically identical values unless the metric definitions are proven equivalent.

For each displayed overlay metric document:

- start and end event used;
- clock/timestamp source;
- units;
- whether the value is CPU, GPU, presentation, or application timing;
- expected relationship to the chosen PresentMon metric;
- HAGS sensitivity if relevant.

A useful test proves consistent semantics and trends rather than forcing unlike metrics to match.

## Device and swap-chain lifecycle

A robust DX11 overlay must treat swap-chain/device state as lifecycle-managed resources rather than one-time globals.

After source recovery, explicitly verify:

- first discovery/attachment;
- repeated Present calls;
- resize-buffer handling;
- fullscreen/borderless/windowed transitions;
- target-window changes if the game creates/replaces windows;
- shutdown before DLL unload;
- process exit;
- full game restart;
- no duplicate hook registration after recovery from a transient failure.

If the exact source uses a different architecture, preserve its working lifecycle and map these acceptance requirements onto the actual implementation instead of rewriting for style.

## Input ownership

When the overlay is closed, game input must behave exactly as without the overlay.

When the overlay is open:

- consume only the input required by the visible panel;
- make capture state visible in diagnostics;
- release capture immediately on close/focus loss;
- never trap the user in an overlay-only input mode after an exception;
- verify text input, mouse buttons, wheel, and keyboard shortcuts used by the game.

## Logging and evidence

Logs should be bounded and diagnostic rather than a per-frame performance regression.

Useful events include:

- exact overlay build identity;
- injection/load success or reason for failure;
- renderer/device/swap-chain identity;
- hook installation/removal;
- resize/device lifecycle events;
- panel open/close state;
- capture run ID;
- clean shutdown or contained failure.

Do not log every frame by default.

## Relationship to PRJ-011

Until stronger evidence appears, treat this project as a **module candidate inside PRJ-011 Sims 4 Accelerator**. Keep PRJ-012 as a tracked continuity record because the Project Constellation catalog preserves its identity, but avoid a second independent hook stack.

PRJ-011 now defines PresentMon 2.5.1-or-later as the external frame-time baseline and uses an evidence ladder that puts external telemetry before invasive hooks. PRJ-012 should inherit that benchmark authority rather than invent a separate performance ledger.

Promote PRJ-012 to a separate product only if recovered project-owned evidence shows separate scope, lifecycle, packaging, or explicit user intent.

## Recovery checklist

Before editing any recovered overlay source, record:

- repository/path/worktree;
- exact commit/version;
- build system and compiler/Windows SDK;
- current hook library/version;
- Dear ImGui integration and backend files;
- DLL/injector ownership;
- target process discovery logic;
- D3D11 discovery and lifecycle logic;
- input-hook ownership;
- logging path;
- prior binaries and hashes;
- any existing runtime verification evidence.

Do not initialize a replacement project because the current source is missing.

## Packaging and install boundary

No canonical DLL or injector is currently recovered, so no installation command is claimed here.

Once source is resolved, a release package should make these identities explicit:

- overlay DLL filename/version/hash;
- loader/injector filename/version/hash when separate;
- supported game/renderer baseline;
- hook-disable or safe-mode method;
- uninstall/remove procedure;
- logs/evidence location;
- exact build source commit.

The game must remain launchable after removing the overlay package.

## Troubleshooting

### Game fails before the panel appears

Disable/remove the overlay candidate and prove the unmodified game still launches. Treat early process failure as an overlay/load blocker, not as a reason to weaken the game's launch path.

### Panel appears but FPS/timing disagrees with PresentMon

Check metric semantics, PresentMon version, HAGS, process identity, frame-selection window, and whether the two values measure different points in the frame pipeline. Preserve raw capture before changing code.

### Overlay stops rendering after a resolution change

Inspect ResizeBuffers/device/swap-chain lifecycle handling and stale render-target resources. Do not force a game restart as the only supported recovery unless source/runtime evidence proves the game itself requires it.

### Mouse/keyboard feels captured after closing the panel

Treat that as a release-blocking input-ownership regression. Verify the close/focus-loss path releases every capture flag/hook state.

### Repeated restarts become unstable

Check duplicate hook installation, leaked global state, loader lifetime, and shutdown ordering. A first-launch pass does not close restart acceptance.

## Exact next action

Locate the original overlay prompt/source and determine whether its hooks already live inside the Sims 4 Accelerator scaffold. Then qualify one read-only DX11 diagnostic overlay against **PresentMon 2.5.1 or later**, preserving raw evidence and exact collector/build identity, before exposing any optimization control or choosing a new hook library.

## Wiki maintenance

Update when source identity is resolved, library versions are actually adopted, renderer-hook behavior is runtime-proven, the relationship to PRJ-011 changes, PresentMon changes benchmark semantics again, or a packaged overlay passes the complete launch/input/device-lifecycle/restart matrix.
