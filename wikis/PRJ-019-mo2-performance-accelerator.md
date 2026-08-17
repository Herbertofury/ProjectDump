# MO2 Performance Accelerator Wiki

**Project Constellation ID:** `PRJ-019`  
**Status:** ACTIVE / corrected after reproduced crash; real-host qualification pending  
**Latest recovered version:** **4.0.1**

## Purpose

MO2 Performance Accelerator is a reversible, event-driven performance layer for Mod Organizer 2. Its purpose is to reduce expensive repeated work on the real mod-list hot paths without hiding data, limiting the mod list, changing ordering/filter semantics, or introducing polling/worker churn.

Performance gains are only valid when the complete MO2 user workflow remains behaviorally identical.

## Recovered version lineage

`2.0.0 -> 3.0.0 -> 4.0.0 -> 4.0.1`

The current qualification target is **4.0.1**.

## Recovered v4 design

The durable project record describes v4 as:

- event-driven only;
- no recurring workers or scans;
- drag fast path;
- lossless filter batching;
- viewport/separator preservation;
- passive reversible tuning.

The project explicitly forbids performance shortcuts that reduce list availability, visible fidelity, or correctness.

## v4.0.0 crash and v4.0.1 correction

Version 4.0.0 could discover a deleted `QTabWidget` wrapper and raise a `RuntimeError` because the wrapped C++ object no longer existed.

Version **4.0.1** corrected that failure by:

- removing the generic discovery implementation;
- binding only after `setParentWidget()`;
- targeting the exact `modList` widget;
- containing exceptions and using a circuit breaker;
- avoiding workers, recurring timers, filesystem traversal, and arbitrary view binding.

The recovered synthetic benchmark showed roughly an 8.3-8.6x improvement for the targeted proxy-recomputation pattern. That is evidence for one measured pattern, not a promise that the whole MO2 application becomes 8x faster.

## Current MO2 host baseline, checked 2026-08-17

The official [Mod Organizer 2 v2.5.2 release](https://github.com/ModOrganizer2/modorganizer/releases/tag/v2.5.2) remains the primary stable host gate. Current [MO2 master](https://github.com/ModOrganizer2/modorganizer) is active beyond that release and was observed at `efe2a02d5dc641946baaa8db1440800f38d07837` for this pass.

Current upstream source matters directly to this project:

- `ModListSortProxy` enables `setDynamicSortFilter(true)`;
- changes to filter criteria/text call `invalidateFilter()` and emit `filterInvalidated()`;
- `ModListView::invalidateFilter()` can call the proxy's broader `invalidate()` path;
- `ModListView` already uses a small 50 ms single-shot timer to coalesce bursts of marker/plugin refresh work caused by repeated expand/collapse signals.

These are concrete host hot paths to instrument. They are stronger targets than generic widget discovery.

## Current Qt evolution: proposal versus host reality

Current Qt 6.11 documentation exposes newer `QSortFilterProxyModel::beginFilterChange()` and `endFilterChange()` APIs intended for more precise custom-filter invalidation. However:

- `beginFilterChange()` was introduced in Qt 6.9;
- `endFilterChange()` was introduced in Qt 6.10;
- the current stable MO2 v2.5.2 host ships Qt 6.7.1.

### Decision

**Do not adopt the Qt 6.9/6.10 filter-change APIs in the current shipping accelerator.** Record them as a forward-compatibility optimization candidate only for a future MO2 host that actually ships a sufficient Qt version and after real before/after measurement.

The strongest current implementation path remains host-version-compatible, event-driven coalescing around existing invalidation behavior.

## Host hot-path measurement contract

Before changing a performance path, capture an exact baseline for the same complete mod list and state.

Record at minimum:

- host build and Qt/Python versions;
- mod count and separator count;
- active grouping/filter/sort mode;
- number of source/proxy invalidations;
- elapsed time for each invalidation burst;
- UI-thread long stalls;
- selection/current-index changes;
- scroll position;
- expanded/collapsed separator state;
- resulting visible/hidden row set;
- resulting mod priority/order;
- task-related warnings/exceptions.

After acceleration, the semantic result must match exactly while the measured work/time improves.

## Filter batching rule

Lossless batching means coalescing redundant invalidations from the same logical event burst, not skipping real updates.

Required properties:

1. every relevant source change is eventually represented;
2. the final filter result equals unaccelerated MO2 for the same inputs;
3. sorting/grouping/selection do not silently drift;
4. rapid text/filter changes converge to the newest state;
5. pending work is cancelled or superseded safely when profile/model identity changes;
6. restart leaves MO2 in native behavior until the plugin is correctly rebound.

## Drag fast-path rule

Drag optimization must preserve exact native drag/drop semantics. The accelerator may reduce unrelated recomputation during an active reorder, but it must not:

- modify drop acceptance;
- suppress the native insertion line;
- change final row target;
- freeze stale proxy/filter state past the drop;
- discard queued model changes;
- break the coordinated synthetic-column plugins.

Run drag tests with Image Column 1.4.12, Bethesda Plugin Info 1.5.3, Version Tracker 2.4.3, and Line Restorer 1.1.0 where available.

## Reversible binding and circuit breaker

The 4.0.1 exact-widget binding is a preservation contract.

A future build should retain:

- exact `modList` identity checking before hooks are installed;
- weak/QPointer-equivalent lifetime awareness where available;
- safe disconnect/unhook on parent/view destruction;
- idempotent setup so restart/rebind does not duplicate handlers;
- a circuit breaker that restores native behavior after unexpected errors;
- diagnostics that identify which optimization path was disabled and why.

A circuit breaker must never hide data corruption or continue partially applying a broken optimization.

## Proposed additive test improvement: host contract probes

When the canonical 4.0.1 source is recovered, add a lightweight development-only probe layer around the exact upstream host methods being optimized:

- proxy `invalidateFilter()` / `invalidate()` call counts;
- filter criteria/text change bursts;
- relevant model reset/layout/data-change signals;
- drag start/end windows;
- marker/plugin refresh bursts;
- final proxy row mapping and stable mod identities.

Use the probes to compare **accelerator off** versus **accelerator on** on the same deterministic fixture. The test should fail if work decreases but the final row mapping/state differs.

Current Qt also offers `QAbstractItemModelTester` as an additive model-consistency check in matching test environments. Use it only in the development harness if the same Qt/PyQt Test bindings are available; do not make QtTest a new shipping runtime dependency.

## Required real-host qualification matrix

Use a real Windows MO2 v2.5.2 process and a complete representative mod list. Do not cap the dataset to make results look better.

| Area | Required proof |
| --- | --- |
| Artifact identity | Loaded plugin is exactly 4.0.1, not crash-prone 4.0.0. |
| Startup | Exact `modList` binding occurs cleanly with no deleted-wrapper errors. |
| Idle | No recurring worker, scan, polling loop, or hot idle CPU regression. |
| Filter text | Rapid filter changes converge to the same final rows as native MO2. |
| Criteria filters | Category/content/update filters remain lossless and correct. |
| Sorting | Sort order and stable mod identity are unchanged. |
| Grouping/separators | Grouping, expanded/collapsed state, and separator placement are preserved. |
| Drag reorder | Native insertion target/final order remain exact; UI stays responsive. |
| Selection/scroll | Current row, selection and scroll survive accelerated refresh paths. |
| Profile switch | Old-model work cannot write into the new profile/model state. |
| Failure path | Injected/induced hook failure trips the circuit breaker and returns to native behavior. |
| Restart | No duplicate hooks; state and native fallback remain correct after full restart. |
| Full-list performance | Measured relevant invalidation/recompute work improves on the same complete dataset. |
| Logs | No task-related exceptions/warnings after sustained use. |

## Anti-degradation rules

Do not improve benchmarks by:

- viewport-only processing;
- visible-row-only filtering;
- mod-count caps;
- dropping off-screen updates;
- stale caches presented as current;
- disabling separators/grouping/sorting;
- lowering image/media quality in other plugins;
- weakening tests;
- replacing the full proxy/model stack without exact behavioral parity;
- changing current host dependencies merely to access newer Qt optimization APIs.

## Source recovery priorities

The connected project evidence does not yet expose the complete canonical 4.0.1 source tree. Recover and record:

- exact artifact/source hash relationship;
- plugin entry point and `setParentWidget()` binding path;
- exact `modList` identity check;
- filter batching/coalescing implementation;
- drag fast-path implementation;
- state snapshot/restore behavior;
- circuit-breaker thresholds and diagnostics;
- test harness and synthetic benchmark fixture;
- packaging command and archive layout.

## Exact next action

**Recover the exact MO2 Performance Accelerator 4.0.1 source/artifact bytes, instrument the current MO2 `ModListSortProxy`/`ModListView` invalidation paths as host-contract probes, then run accelerator-off versus accelerator-on comparisons in real MO2 v2.5.2 for startup, rapid filtering, sorting/grouping, drag reorder, profile switch, failure/circuit-breaker behavior, selection/scroll/separators, restart, logs, and full-list timing. Keep Qt 6.9/6.10 filter-change APIs proposal-only until the actual MO2 host ships them.**

## Evidence boundary

The 4.0.1 crash fix and targeted synthetic benchmark are preserved evidence. This page does not claim fresh real Windows MO2 v2.5.2 whole-workflow qualification or a newly recovered canonical source tree.
