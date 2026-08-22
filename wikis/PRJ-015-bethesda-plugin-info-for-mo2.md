# Bethesda Plugin Info for MO2 Wiki

**Project Constellation ID:** `PRJ-015`  
**Status:** VALIDATED ARTIFACT; current-host live proof pending  
**Latest recovered version:** **1.5.3** compatibility correction  
**Primary current host gate:** **Mod Organizer 2 v2.5.2**  
**Current upstream forward-compatibility heads checked:** `ModOrganizer2/modorganizer@efe2a02d5dc641946baaa8db1440800f38d07837`, `ModOrganizer2/modorganizer-plugin_python@e9d55a50a7c9f38280e72f52d910852fdcf0321e`

## Purpose

Bethesda Plugin Info adds a dedicated Mod Organizer 2 column and related metadata UX while preserving native MO2 list behavior. The plugin is not allowed to own or replace MO2 drag/drop, alter native columns, write into game Data/Overwrite, or trade compatibility for a visually working column.

The project has two distinct proof layers:

1. **artifact-level validation** proving the recovered plugin package and compatibility correction behave correctly in automated/offscreen qualification; and
2. **real-host qualification** proving the exact plugin remains correct inside a real Windows MO2 process with the coordinated synthetic-column stack, actual theme/DPI, current Python proxy, real mod-list model/proxy behavior, drag/drop, and restart persistence.

Do not collapse those layers into one `works` status.

## Recovered version lineage and proof

Recovered lineage is:

`1.0.0 -> 1.1.0 -> 1.2.0 -> 1.3.0 -> 1.4.0 -> 1.5.0 -> 1.5.1/1.5.2 patch work -> 1.5.3`

The strongest full validation remains **1.5.0**:

- 69 automated tests passed;
- release/ZIP hygiene passed;
- dedicated-column movement and resize behavior passed;
- branch restoration and selection/model preservation passed;
- rich and classic tooltip modes passed;
- warning/category behavior passed;
- 22 ICO plus 22 PNG assets were covered;
- no networking, subprocesses, per-mod sidecars, game Data writes, or Overwrite writes were recorded by that validation.

The later shared drag/drop compatibility pass produced **1.5.3**. The preserved root-cause evidence records native-column-zero drop-capability and paint-barrier corrections, with 76 tests plus four subtests retained in that compatibility pass. **1.5.3 is the current live-qualification target.**

## Current Mod Organizer 2 baseline

### Stable release gate

The official [Mod Organizer 2 releases](https://github.com/ModOrganizer2/modorganizer/releases) still identify **v2.5.2** as the latest stable release. The release requires Windows 10 1809+ or Windows 11 and Microsoft Visual C++ Redistributable 14.40.33810.0. Its dependency set includes Qt/PyQt **6.7.1** and Python **3.12.3**.

The release is directly relevant to this project because it includes third-party plugin API changes and Bethesda/Starfield Creation support changes. It therefore remains the primary release gate rather than an older beta host.

Official download/reference:

- [Mod Organizer 2 v2.5.2 release](https://github.com/ModOrganizer2/modorganizer/releases/tag/v2.5.2)
- [All Mod Organizer 2 releases](https://github.com/ModOrganizer2/modorganizer/releases)

### Current upstream development heads

Current upstream development remains ahead of v2.5.2:

- `ModOrganizer2/modorganizer` master: `efe2a02d5dc641946baaa8db1440800f38d07837`
- `ModOrganizer2/modorganizer-plugin_python` master: `e9d55a50a7c9f38280e72f52d910852fdcf0321e`

Use these only as a **separate forward-compatibility lane** after the stable v2.5.2 gate passes. Do not silently rewrite the plugin around unreleased interfaces merely because master exposes them.

## Current MO2 Python-plugin host architecture

Bethesda Plugin Info's exact 1.5.3 source tree has not yet been recovered through the connected evidence used for this page, so this section describes the **current MO2 host architecture that a recovered Python plugin must qualify against**, not a claim about exact PRJ-015 imports.

The official `modorganizer-plugin_python` repository currently implements the Python bridge with five source areas:

- `src/proxy` - the native proxy plugin loaded by MO2; its build produces `plugin_python.dll` and installs the Python runtime pieces and `mobase`;
- `src/runner` - owns Python interpreter creation and Python plugin load/unload;
- `src/pybind11-qt` - Qt/PyQt interoperability support;
- `src/pybind11-utils` - shared pybind11 utilities;
- `src/mobase` - the generated Python-facing MO2 plugin interface.

The Python/C++ boundary is implemented through **pybind11**. This matters for PRJ-015 qualification because crashes, stale wrapped Qt objects, invalid model/view lifetimes, profile API changes, or incorrect plugin unload behavior may originate at the host bridge boundary even when the plugin's own column logic is correct.

### Host-side test infrastructure

The upstream Python proxy includes:

- Python/pytest tests;
- C++/GTest runner tests that instantiate the Python runner and verify Python plugins from the C++ side;
- mock `uibase` interfaces;
- optional test builds enabled with `PLUGIN_PYTHON_TESTS`.

The official host-side test commands are:

```powershell
# after configuring a compatible MO2 Python-proxy build with PLUGIN_PYTHON_TESTS enabled
cmake --build vsbuild --config RelWithDebInfo --target "python-tests" "runner-tests"
ctest.exe --test-dir vsbuild -C RelWithDebInfo
```

MO2's Python proxy is normally built as part of the broader `mob` repository/build system. These commands are **host compatibility references**, not invented PRJ-015 build commands. Once the exact Bethesda Plugin Info source is recovered, document its own test/package commands separately.

Official host sources:

- [MO2 Python proxy](https://github.com/ModOrganizer2/modorganizer-plugin_python)
- [MO2 `mob` build system](https://github.com/ModOrganizer2/mob)

## Upstream API drift that must be included in forward compatibility

Current MO2 master history contains 2026 API/lifecycle changes that should be part of PRJ-015's forward-compatibility watchlist after stable v2.5.2 qualification. Important examples include:

- `IOrganizer::profile()` ownership changing to a shared pointer;
- new executable-list access in the plugin API;
- instance-manager exposure to plugins;
- Nexus OAuth/authentication migration work;
- stable download-ID refactoring and download/update accuracy work;
- continued Qt/Python/pybind11 host evolution.

Do **not** assume Bethesda Plugin Info uses every one of those interfaces. The rule is narrower: after source recovery, identify which host APIs the plugin actually imports or receives and pin a compatibility test to each relevant lifetime/identity contract.

## Coordinated drag/column contract

PRJ-015 is part of the coordinated [MO2 Drag/Column Compatibility Pack](PRJ-024-mo2-drag-column-compatibility-pack.md) with:

- MO2 Image Column **1.4.12**;
- Bethesda Plugin Info **1.5.3**;
- Bethesda Creations Version Tracker **2.4.3**.

The compatibility contract is stronger than `the column renders`.

Bethesda Plugin Info must preserve:

- MO2's native insertion targeting;
- native reorder drag/drop;
- completed-download-to-mod-list drag;
- selection/current index;
- scroll position;
- separators and collapsed/expanded state;
- filtering/search and sorting;
- profile state;
- theme and DPI behavior;
- MO2's base list/delegate behavior;
- restart persistence;
- its own dedicated column, tooltip, warning, category, and metadata behavior.

A synthetic column must never become a second drop-ownership system.

## Data and UI ownership contract

### Dedicated column

The dedicated column may display Bethesda Plugin Info data, but it must not mutate native column meaning or make native list behavior dependent on the column remaining visible.

Verify:

- the column appears exactly once;
- move/resize/hide/show does not corrupt model identity;
- native columns remain unchanged;
- the plugin does not replace the whole list delegate merely to paint its own cells;
- row identity survives proxy/sort/filter changes;
- state persists across full restart where intended.

### Tooltips

Rich and classic tooltip modes were part of the validated behavior. Live qualification must prove tooltip content remains attached to the **correct mod identity**, especially under:

- rapid pointer movement;
- filter changes;
- sorting;
- row reordering;
- separator expansion/collapse;
- theme/DPI changes.

An asynchronously completed tooltip must not overwrite a newer hover target.

### Warnings and categories

Warnings and categories must remain data-driven and truthful. A visual warning cannot be treated as correct merely because it appears; verify the underlying mod identity and triggering metadata.

### Writes and side effects

The strong 1.5.0 validation recorded no networking, subprocesses, per-mod sidecars, game Data writes, or Overwrite writes. Treat that as a preservation requirement unless a later explicit project decision and migration contract proves otherwise.

## Installation and recovery workflow

The exact canonical 1.5.3 archive/source layout has not yet been rediscovered through the connected evidence used for this page. Do not invent an archive structure.

Use this preservation-first workflow:

1. locate the exact 1.5.3 artifact or source bundle from durable project storage;
2. record filename, byte size, SHA-256, embedded version, package root, and source provenance;
3. preserve an immutable copy before installation or modification;
4. record the current MO2 instance/profile, installed Python proxy, theme, DPI, and coordinated plugin versions;
5. create an isolated MO2 v2.5.2 qualification instance;
6. install exactly Image Column 1.4.12, Bethesda Plugin Info 1.5.3, and Version Tracker 2.4.3 for coordinated drag/column testing;
7. prove the loaded plugin identity from the actual installed path, not a staging/archive filename alone;
8. run the acceptance matrix below;
9. only after the stable release gate passes, repeat the relevant checks against current MO2/Python-proxy master as a separate forward-compatibility lane.

## Required real-host acceptance matrix

Use a real Windows MO2 v2.5.2 process with the actual relevant theme/DPI and coordinated plugin stack.

| Area | Required proof |
| --- | --- |
| Host identity | Exact MO2 v2.5.2 build, Qt/PyQt, Python, Python-proxy/plugin bridge, theme, DPI, and profile are recorded. |
| Plugin identity | Loaded artifact is proven to be Bethesda Plugin Info 1.5.3. |
| Startup | No task-related MO2/Python/plugin errors. |
| Dedicated column | Column appears exactly once in the intended list. |
| Native columns | Native column meaning, order, render behavior, and interaction remain unchanged. |
| Column layout | Move, resize, hide/show, and layout persistence work. |
| Tooltip identity | Rich/classic tooltip follows the correct mod under rapid hover, sort, filter, reorder, and separator changes. |
| Warnings | Warning state matches the intended underlying mod metadata. |
| Categories | Category behavior remains correct and attached to the intended mod. |
| Native reorder drag | Native insertion line remains visible and final placement is exact. |
| Cross-column drag | Crossing the Bethesda Plugin Info synthetic column does not change acceptance or target row. |
| Download drag | Completed download-to-mod-list drag still works. |
| Selection/current index | Selection and current item remain correct during column/model operations. |
| Scroll/separators | Scroll position and separator state remain stable. |
| Sort/filter/search | Correct data remains bound to each mod after proxy/model changes. |
| Theme/DPI | Painting, text contrast, geometry, hit targets, and drag indicator remain correct. |
| Repeated drag/hover | No handler accumulation, stale tooltip, repaint artifact, or wrapped-object exception appears. |
| Restart | Plugin settings and intended column state survive a full MO2 restart. |
| Side-effect boundary | No new per-mod sidecars, game Data writes, Overwrite writes, subprocesses, or networking appear unless explicitly introduced and documented later. |
| Logs | No new task-related errors appear in MO2/Python/plugin logs. |

A load-only smoke test, offscreen Qt pass, or visually correct insertion line without correct final row placement does not close this gate.

## Forward-compatibility lane

After the v2.5.2 matrix passes, run a **separate** current-master lane.

Record:

- exact `modorganizer` commit;
- exact `modorganizer-plugin_python` commit;
- Python proxy/runner build identity;
- Qt/PyQt and Python versions;
- plugin artifact hash;
- which relevant host interfaces differ from v2.5.2;
- whether profile/model/view/delegate object lifetimes differ;
- whether all stable-release acceptance cases still pass.

A forward-master failure does not retroactively invalidate a working v2.5.2 release artifact, but it must remain visible as compatibility debt.

## Instrumentation and evidence capture

For a useful qualification receipt, capture at minimum:

```text
MO2 version / commit
MO2 Python proxy commit
Qt/PyQt version
Python version
Windows build
plugin artifact filename + SHA-256
coordinated plugin versions
active profile
active theme
DPI / monitor scaling
acceptance matrix result per case
MO2 log path / relevant errors
Python/plugin log path / relevant errors
restart result
```

For a failure, also capture the exact mod identity, selected row, proxy/source row when relevant, active sort/filter state, drag source/target, and whether the failure still reproduces with the other synthetic-column plugins disabled one at a time.

## Troubleshooting

### Column appears but shows wrong mod data after sorting/filtering

Treat this as an identity/proxy mapping defect. Compare the selected proxy index, source index, stable mod identity, and displayed metadata. Do not fix it by caching the visible row number.

### Tooltip shows data for the previous row

Treat this as stale asynchronous ownership or hover-target identity. Newer hover identity must supersede older work; cancellation or completion guards should be keyed to stable mod identity, not only screen position.

### Native insertion line disappears over the Bethesda Plugin Info column

Treat this as a regression of the 1.5.3 shared compatibility correction. Verify exact plugin versions, theme/DPI, synthetic-column drop capability, queued repaint behavior, and whether Image Column/Version Tracker are installed. Do not replace MO2 drag/drop.

### Drag appears correct but lands on the wrong row

Pixels are not semantic proof. Capture MO2's actual target row/action and final order. The native drop result is authoritative.

### Plugin crashes only on current MO2 master

Check the exact MO2/Python-proxy commits and relevant API/lifetime changes before changing plugin logic. Preserve the stable v2.5.2 result separately.

### Wrapped C++/Qt object errors appear

Treat deleted or stale Qt wrapper access as a lifetime bug. Stop using the stale object, re-resolve the authoritative current view/model where appropriate, and preserve exception containment. Do not hide the error with broad exception swallowing around the entire plugin.

### Theme or DPI breaks cell geometry

Verify host metrics and the active MO2 delegate before hard-coding dimensions. The plugin should compose with the host's current row/column geometry rather than assume one historical theme or scaling factor.

## Modification and contribution rules

Until the canonical source tree is recovered, do not invent module names or project-specific build commands. When source is available, preserve these requirements:

1. stable mod identity must survive sort/filter/reorder and async completion;
2. native MO2 drag/drop and insertion targeting remain host-owned;
3. base MO2 delegate/model semantics remain intact;
4. tooltips, warnings, and categories remain bound to the correct mod;
5. no viewport-only correctness shortcuts or hidden data caps;
6. no new write/network/subprocess side effects without an explicit product decision and migration/security review;
7. shared-column changes must be tested with Image Column 1.4.12 and Version Tracker 2.4.3;
8. host-API compatibility must be tested against stable v2.5.2 first and current master separately;
9. failures must be reproduced before weakening any test or safety boundary;
10. preserve prior validation reports and package hashes as lineage evidence.

## Source recovery priorities

The next source-recovery pass should locate and record:

- canonical repository/worktree/branch or exact 1.5.3 source archive;
- exact package/source SHA-256 and size;
- package/install layout and entry point;
- MO2/mobase interfaces actually imported;
- dedicated-column model/proxy/delegate implementation;
- stable mod identity and metadata cache ownership;
- tooltip ownership/cancellation path;
- warning/category data path;
- exact 1.5.3 drop-capability/repaint correction;
- settings persistence keys;
- test runner and fixtures;
- packaging/release command.

Once recovered, add exact project build/test/package commands and a source-module interaction map without discarding the behavior and host-compatibility contract already documented here.

## Exact next action

**Recover or identify the exact Bethesda Plugin Info 1.5.3 source/artifact bytes and package layout, then live-qualify that exact artifact with Image Column 1.4.12 and Version Tracker 2.4.3 in real Windows MO2 v2.5.2 across dedicated-column behavior, tooltip identity, warnings/categories, native drag/drop, download drag, proxy/sort/filter identity, theme/DPI, logs, side-effect boundaries, and full restart persistence. After the stable lane passes, repeat the relevant matrix against pinned current MO2 and Python-proxy master commits as a separate forward-compatibility gate.**

## Evidence boundary

The durable automated validation and 1.5.3 compatibility evidence are strong. This page does **not** claim fresh real Windows MO2 v2.5.2 qualification, a newly recovered canonical 1.5.3 source tree, or that every current MO2 master API listed in the watchlist is used by Bethesda Plugin Info. Those remain explicit proof tasks.
