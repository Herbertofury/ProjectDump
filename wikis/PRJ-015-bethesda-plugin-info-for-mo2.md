# Bethesda Plugin Info for MO2 Wiki

**Project Constellation ID:** `PRJ-015`
**Status:** VALIDATED ARTIFACT; current-host live proof pending
**Latest recovered version:** **1.5.3** compatibility correction

## Purpose

Bethesda Plugin Info adds a dedicated Mod Organizer 2 column and related metadata UX while preserving native MO2 list behavior. The plugin is not allowed to own or replace MO2 drag/drop, alter native columns, write into game Data/Overwrite, or trade compatibility for a visually working column.

## Recovered version lineage and proof

Recovered lineage is `1.0.0 -> 1.1.0 -> 1.2.0 -> 1.3.0 -> 1.4.0 -> 1.5.0 -> 1.5.1/1.5.2 patch work -> 1.5.3`.

The strongest full validation remains **1.5.0**: 69 automated tests passed; release/ZIP hygiene passed; dedicated-column movement and resize behavior, branch restoration, selection/model preservation, rich/classic tooltip modes, warning/category behavior, and 22 ICO plus 22 PNG assets were covered. That validation also recorded no networking, subprocesses, per-mod sidecars, game Data writes, or Overwrite writes.

The later shared drag/drop compatibility pass produced **1.5.3**. The preserved root-cause evidence records native-column-zero drop-capability and paint-barrier corrections, with 76 tests plus four subtests retained in that compatibility pass. This is the version to qualify live, not an older patch.

## Current MO2 host baseline, checked 2026-08-17

The official [Mod Organizer 2 release](https://github.com/ModOrganizer2/modorganizer/releases/tag/v2.5.2) remains **v2.5.2**. Its shipped stack includes Qt/PyQt 6.7.1 and Python 3.12.3 and it contains relevant third-party plugin and Starfield Creation changes.

The upstream [MO2 master repository](https://github.com/ModOrganizer2/modorganizer) is also active beyond that stable release. The current observed master head for this pass is `efe2a02d5dc641946baaa8db1440800f38d07837` (2026-07-08). The [MO2 Python plugin](https://github.com/ModOrganizer2/modorganizer-plugin_python) is likewise active, observed at `e9d55a50a7c9f38280e72f52d910852fdcf0321e`, with 2026 interface additions such as instance/profile and executable-list APIs.

### Compatibility decision

Use **MO2 v2.5.2 as the primary release gate**. After that exact real-runtime gate passes, use current MO2/Python-plugin master as a separate forward-compatibility lane. Do not silently change the plugin to unreleased interfaces merely because master exposes them.

## Coordinated drag/column contract

PRJ-015 is part of the coordinated [MO2 Drag/Column Compatibility Pack](PRJ-024-mo2-drag-column-compatibility-pack.md) with:

- MO2 Image Column 1.4.12;
- Bethesda Plugin Info 1.5.3;
- Bethesda Creations Version Tracker 2.4.3.

The compatibility contract is stronger than “the column renders.” Bethesda Plugin Info must preserve native MO2 insertion targeting, native drag/drop, download-to-mod-list drag, selection, scroll, separators, filters/search, profile state, theme/DPI behavior, and restart persistence while its own dedicated column, tooltips, warnings, and categories remain correct.

## Required real-host acceptance

On an isolated Windows MO2 v2.5.2 instance with the actual relevant theme/DPI and the coordinated plugin stack, verify all of the following in the real process:

1. plugin startup has no task-related MO2/Python errors;
2. the dedicated Bethesda Plugin Info column appears in the intended location;
3. native columns remain unchanged;
4. column move, resize, hide/show and layout persistence work;
5. tooltip modes show the correct mod's data and remain correct under rapid pointer movement;
6. warnings and categories match the intended metadata state;
7. native reorder drag shows the insertion line and lands at the exact target;
8. download-to-mod-list drag still works;
9. separators, filtering, sorting, selection and scrolling remain stable;
10. theme/DPI changes do not break geometry or painting;
11. repeated drags do not accumulate handlers or repaint artifacts;
12. a full restart preserves plugin and column state.

A load-only smoke test or offscreen Qt test does not close this gate.

## Preservation rules

Do not fix compatibility by disabling the dedicated column, intercepting drops, replacing MO2 drag semantics, hiding the native insertion indicator, swallowing errors, reducing row/data availability, changing compact-row behavior, or removing validated tooltip/warning/category functionality.

## Exact next action

**Install Bethesda Plugin Info 1.5.3 together with Image Column 1.4.12 and Version Tracker 2.4.3 in real Windows MO2 v2.5.2, run the coordinated drag/column/restart matrix, then repeat the relevant matrix against current upstream MO2/Python-plugin master only as a forward-compatibility lane.**

## Evidence boundary

The durable validation and compatibility reports prove substantial automated behavior, but current real Windows MO2 v2.5.2 runtime success has not yet been established in this Project Constellation pass. Keep that distinction visible until exact live evidence exists.
