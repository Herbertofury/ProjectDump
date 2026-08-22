# MO2 Drag/Column Compatibility Pack Wiki

**Project Constellation ID:** `PRJ-024`  
**Status:** VALIDATED COMPATIBILITY WORK; current-host live stack proof pending  
**Primary stable host gate:** Mod Organizer 2 **v2.5.2**  
**Current upstream MO2 head checked:** `efe2a02d5dc641946baaa8db1440800f38d07837`

## Purpose

PRJ-024 is the coordinated compatibility contract for three MO2 plugins that all extend the mod-list surface and therefore can interact with the same drag/drop, painting, model, separator, selection, and persistence paths:

- MO2 Image Column **1.4.12**
- Bethesda Plugin Info **1.5.3**
- Bethesda Creations Version Tracker **2.4.3**

Treat the pack as one compatibility qualification surface rather than three independent plugins. A plugin is not compatible merely because it loads in isolation.

## Coordinated versions

The preserved corrected set is:

| Component | Coordinated version | Primary responsibility |
| --- | --- | --- |
| MO2 Image Column | **1.4.12** | thumbnail/media column and image automation |
| Bethesda Plugin Info | **1.5.3** | plugin-information column, warnings, categories, tooltips |
| Bethesda Creations Version Tracker | **2.4.3** | Creation/version/source metadata and migration |

The preserved compatibility work corrected synthetic-column drag/drop behavior while retaining Image Column's own delegate/rendering path and the other plugins' dedicated-column behavior.

## Preserved root-cause evidence

The durable compatibility reports identify two shared plugin-side problems:

1. synthetic/dedicated columns inherited drop capability from an inappropriate native-column baseline;
2. queued repaint/update behavior could obscure the native insertion line or add compatibility work during drag/drop.

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
- no plugin intercept that accepts, rejects, reroutes, or executes drops on MO2's behalf;
- no plugin workaround that silently changes MO2's underlying model/separator ordering to make the UI appear stable.

## Current host baseline, checked 2026-08-22

The official Mod Organizer 2 release page still identifies **v2.5.2** as the latest stable release. That release line includes Qt/PyQt 6.7.1, Python 3.12.3, Starfield Creation support changes, and additional third-party plugin interface capabilities.

Current upstream `ModOrganizer2/modorganizer` master inspected for this pass is:

`efe2a02d5dc641946baaa8db1440800f38d07837`

The historical MO2 2.5.3 beta 12 development target remains useful regression evidence when reproducing old behavior, but it is not the primary stable qualification target.

## Current upstream separator-refresh regression

MO2 upstream issue **#2420** is currently open against v2.5.2: **Top separators lose anchor and collapsible state after F5 refresh (Creation Club mods)**.

The reported reproduction is directly relevant to PRJ-024 because the compatibility pack promises to preserve separators and model/view state while adding synthetic columns and drag/drop-adjacent painting:

1. use Skyrim SE/AE with Creation Club mods present;
2. place a separator at the very top of the mod list above the Creation Club mods;
3. enable collapsible separators;
4. collapse the separator;
5. press **F5** to refresh the mod list;
6. observe whether the separator stays anchored, stays collapsed, and retains its exact relationship to the first Creation Club mod below it.

The upstream report says the separator may move, lose its anchor, or fail to remain collapsed after refresh.

### Why this matters to the compatibility pack

This host defect is **not the same thing** as the original PRJ-024 insertion-line/drag-paint defect. Treat them separately:

- insertion-line correctness is primarily a drag/drop capability and painting contract;
- issue #2420 is a refresh/model/separator-state contract;
- a plugin repaint must not hide or cosmetically mask an underlying separator movement;
- a plugin must not become the accidental owner of separator ordering simply to compensate for an MO2 host bug;
- plugin-on and plugin-off runs must therefore be compared using stable item/separator identity rather than row numbers alone.

If v2.5.2 reproduces issue #2420 with all three plugins disabled, record it as a host baseline. The coordinated plugin stack then passes this regression lane only if it does not worsen the movement, introduce a new failure, preserve stale UI state that hides the host change, or make a previously stable path unstable.

## Exact current-host differential regression lane

Use an isolated Windows MO2 v2.5.2 instance with Skyrim SE/AE, the Creation Club set required to reproduce issue #2420, the user's relevant theme/DPI, and a deterministic mod-list fixture.

### A. Baseline with PRJ-024 plugins disabled

Record before and after F5:

- separator name and stable logical identity;
- first mod immediately below the separator;
- Creation Club mod identities;
- collapsed/expanded state;
- visible priority/order;
- selection and current item;
- vertical scroll position or top visible logical item;
- active filter/search text;
- profile name;
- relevant MO2 log lines.

Repeat enough times to determine whether the host defect is deterministic, intermittent, or absent in the fixture.

### B. Coordinated stack enabled

Install exactly:

- Image Column 1.4.12;
- Bethesda Plugin Info 1.5.3;
- Bethesda Creations Version Tracker 2.4.3.

Repeat the same F5 sequence with no other changes.

Acceptance requires:

- no new separator movement attributable to the plugins;
- no new collapsed-state loss attributable to the plugins;
- no stale synthetic-column repaint that visually hides a changed underlying model;
- no duplicate or missing rows after refresh;
- no thumbnail/metadata identity crossover after the model refresh;
- selection, scroll, filter/search, and profile state remain truthful;
- no new plugin exceptions or warnings in MO2/Python logs.

### C. Drag/drop after refresh

Immediately after the F5 lane, verify native reordering to ensure model refresh did not poison the original compatibility contract:

1. drag an installed mod above and below neighboring mods;
2. move a separator;
3. drag a download into the mod list where supported;
4. verify top/bottom auto-scroll during drag;
5. verify the native insertion line remains visible;
6. verify the actual drop result matches the intended logical target;
7. repeat with each synthetic column under the pointer path.

The row highlighted during drag and the final model order must agree.

## Full live verification matrix

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
14. F5 refresh is tested against the issue #2420 top-separator/Creation Club fixture with plugins disabled and enabled;
15. restart preserves settings/state;
16. MO2/Python/plugin logs contain no new task-related errors.

## Qualification receipt

Do not close the current-host gate with a screenshot alone. Preserve a small machine-readable or Markdown receipt containing at least:

```text
mo2Version
mo2CommitOrRelease
pythonVersion
qtVersion
profile
activeTheme
windowsScaleFactor
pluginVersions
pluginArtifactHashes
fixtureIdentity
issue2420BaselineResult
issue2420PackEnabledResult
dragDropResult
downloadDropResult
separatorResult
selectionScrollResult
restartResult
logResult
testedAt
```

For failures, retain the before/after logical identities and the exact MO2/plugin log excerpt needed to reproduce the problem.

## Verification discipline

Automated/offscreen compatibility tests are valuable but do not close the release gate. Final proof requires the real Windows MO2 process and actual drag/drop interaction.

A technically rendered insertion line is not enough if the final insertion target is wrong. Likewise, a stable-looking UI after F5 is not enough if the underlying separator/model identity moved and a plugin merely failed to repaint truthfully.

## Troubleshooting

### Insertion line disappears only when the pointer crosses a synthetic column

Recheck item flags and delegate/update behavior for that exact column. Do not add plugin-owned drop acceptance as a shortcut.

### The insertion line looks correct but the mod lands in the wrong place

Treat this as a model/targeting failure, not a paint-only issue. Capture logical item identity before the drop and verify the model result afterward.

### F5 moves the top separator above Creation Club mods

First reproduce with all PRJ-024 plugins disabled. If the same movement occurs, record the host baseline under MO2 issue #2420. Then enable the coordinated stack and prove the stack does not worsen, conceal, or add a second state-corruption path.

### Thumbnail or metadata rows become mismatched after F5

Treat it as an identity/rebinding regression. Synthetic-column caches must key against stable mod identity, not stale row indexes that changed during model refresh.

### Repeated drags become slower or paint multiple insertion lines

Inspect queued updates, event filters, delegates, and any drag-path signal connections for duplicate registration or delayed repaint accumulation.

### A fix disables one of the synthetic columns

Reject it. Compatibility means the coordinated features coexist; removing a feature is not a compatibility repair.

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
- suppressing a real MO2 refresh defect with stale plugin UI state;
- silently reordering separators/mods to compensate for host behavior;
- disabling other validated plugin behavior.

## Current evidence boundary

The coordinated corrected versions and their historical compatibility fixes are durable evidence. Full current-host live proof remains pending.

The open issue #2420 is an upstream MO2 report, not proof that PRJ-024 causes the separator defect. Its value is as a current deterministic host-regression fixture that can reveal whether the coordinated plugin stack preserves model/view truth during refresh.

## Exact current next action

**Live-test Image Column 1.4.12, Bethesda Plugin Info 1.5.3, and Version Tracker 2.4.3 together on MO2 v2.5.2. Run the issue #2420 Creation Club/top-separator F5 fixture first with the pack disabled and then enabled, preserve stable logical identities and logs, then run the full drag/drop/download/restart matrix.**

Keep older beta-target evidence as regression history rather than the only current gate.

## Wiki maintenance

Update this page when any coordinated plugin version changes, MO2/Python/Qt host behavior changes, issue #2420 is fixed or superseded upstream, the live stack test is completed, drag/drop root cause changes, or a new plugin joins the compatibility pack.