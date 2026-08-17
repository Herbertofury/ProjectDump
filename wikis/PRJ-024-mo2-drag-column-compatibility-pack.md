# MO2 Drag/Column Compatibility Pack Wiki

**Project Constellation ID:** `PRJ-024`  
**Status:** VALIDATED COMPATIBILITY WORK; current-host live stack proof pending

## Coordinated versions

The compatibility pack is a coordinated set rather than three unrelated plugins:

- MO2 Image Column **1.4.12**
- Bethesda Plugin Info **1.5.3**
- Bethesda Creations Version Tracker **2.4.3**

The preserved compatibility work corrected synthetic-column drag/drop behavior while retaining the Image Column's own delegate/rendering path and the other plugins' dedicated-column behavior.

## Preserved root-cause evidence

The durable compatibility reports identify two shared problems:

1. synthetic/dedicated columns inherited drop capability from an inappropriate native-column baseline;
2. queued repaint/update behavior could obscure the native insertion line or produce compatibility problems during drag/drop.

The corrected coordinated versions preserve dedicated columns while restoring native insertion-target behavior rather than replacing MO2 drag/drop with plugin-owned drag logic.

## Hard compatibility contract

The pack must preserve all of the following together:

- native MO2 drag/drop semantics;
- native insertion target/line behavior;
- dedicated plugin columns;
- Image Column thumbnail identity and rendering;
- Bethesda Plugin Info tooltips/warnings/categories;
- Version Tracker metadata/migration/conflict behavior;
- selection, scroll, separators, filter/search, and profile state;
- active theme and DPI rendering;
- restart persistence;
- download-to-mod-list drag behavior;
- no plugin intercept that accepts/rejects/reroutes drops on MO2's behalf.

## Current host baseline, checked 2026-08-17

The official Mod Organizer 2 release page lists **v2.5.2** as the latest release. That line includes Qt/PyQt 6.7.1, Python 3.12.3, Starfield Creation changes, and additional third-party plugin interface capabilities.

Project Constellation previously carried an older MO2 2.5.3 beta 12 live-test target from historical development work. Preserve that as useful regression history when needed, but the primary current release gate is now MO2 v2.5.2.

## Exact live verification matrix

Use an isolated current MO2 v2.5.2 instance with the exact coordinated plugin versions and the user's actual relevant theme/DPI settings.

Verify:

1. all three plugins load without startup errors;
2. dedicated columns appear in the intended locations;
3. native columns remain unchanged;
4. column movement/resizing works;
5. native insertion line is visible during mod-list reorder drag;
6. dropping before/after rows lands at the exact intended target;
7. download-to-mod-list drag still works;
8. Image Column thumbnails/tooltips map to the correct mods, including duplicates;
9. Bethesda Plugin Info warnings/tooltips/categories remain correct;
10. Version Tracker migration/metadata/version/source/conflict behavior remains correct;
11. selection, scroll, separators, filters, searches, and profile state remain stable;
12. theme/DPI changes do not break painting or target geometry;
13. repeated drags do not accumulate duplicate handlers or repaint artifacts;
14. restart preserves settings/state;
15. MO2/Python/plugin logs contain no new task-related errors.

## Verification discipline

Automated/offscreen compatibility tests are valuable but do not close the release gate. Final proof requires the real Windows MO2 process and actual drag/drop interaction.

A technically rendered insertion line is not enough if the final insertion target is wrong. A plugin is not compatible merely because it loads.

## Anti-degradation requirements

Do not solve compatibility by:

- disabling a dedicated column;
- replacing Image Column's rendering with a generic delegate;
- hiding the insertion line;
- disabling native drag/drop;
- lowering thumbnail fidelity;
- reducing mod-list availability;
- changing row density unless explicitly requested;
- swallowing drag failures;
- disabling other validated plugin behavior.

## Exact current next action

**Live-test Image Column 1.4.12, Bethesda Plugin Info 1.5.3, and Version Tracker 2.4.3 together on current MO2 v2.5.2 with the full relevant plugin stack, theme/DPI, drag/drop paths, and restart persistence.** Keep older beta-target evidence as regression history rather than the only current gate.

## Wiki maintenance

Update this page when any coordinated plugin version changes, MO2/Python/Qt host behavior changes, the live stack test is completed, drag/drop root cause changes, or a new plugin joins the compatibility pack.