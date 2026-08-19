# MO2 Drag-and-Drop Line Restorer Wiki

**Project Constellation ID:** `PRJ-018`  
**Status:** VALIDATED ARTIFACT; real-host visual/target proof pending  
**Latest recovered version:** **1.1.0**  
**Recovered package SHA-256:** `615b3b05e081ce6c529b4e9e117dbdc207f30e0dca5c858c31739a0981da7b56`

## Purpose

MO2 Drag-and-Drop Line Restorer is a **visual-only overlay** for the Mod Organizer 2 mod list. It restores an always-visible, configurable drop indicator while leaving acceptance, rejection, rerouting, ordering, installation, and execution of drag/drop entirely with MO2.

That boundary is the project's core safety property. A visually correct line with the wrong final insertion target is a failure.

The project is intentionally independent of Image Column, Bethesda Plugin Info, Bethesda Creations Version Tracker, and other synthetic-column plugins. It finds MO2's real mod-list `QTreeView` and paints a mouse-transparent child overlay over that view's viewport rather than replacing MO2's model, delegate, or drag/drop implementation.

## Artifact identity and evidence

The current qualification artifact is **MO2 Drag-and-Drop Line Restorer 1.1.0**.

Recovered package hash:

```text
615b3b05e081ce6c529b4e9e117dbdc207f30e0dca5c858c31739a0981da7b56  MO2-Drag-Drop-Line-Restorer-v1.1.0.zip
```

Project-owned evidence includes:

- `MO2-Drag-Drop-Line-Restorer-v1.1.0-README.md`;
- `MO2-Drag-Drop-Line-Restorer-v1.1.0-TEST-REPORT.md`;
- `MO2-Drag-Drop-Line-Restorer-v1.1.0.sha256`;
- the earlier v1.0.0 README/test report for lineage;
- `MO2-Drag-Drop-Audit-and-Fix-Report.md` and `MO2-Drag-Drop-Root-Cause-and-Fix-Report.md` for the coordinated synthetic-column drag/drop failure class.

## Current MO2 host baseline, checked 2026-08-19

The official [Mod Organizer 2 releases](https://github.com/ModOrganizer2/modorganizer/releases) still identify **v2.5.2** as the current stable release. That release ships Qt/PyQt 6.7.1 and Python 3.12.3 and remains the primary current stable host gate for this project.

Version 1.1.0 itself was rebuilt and source-checked against the user-supplied **MO2 2.5.3 beta 12 source**. Keep those two facts separate:

- **implementation/native-renderer reference:** MO2 2.5.3 beta 12 source used by the 1.1.0 development pass;
- **current stable live qualification target:** MO2 v2.5.2 unless a newer stable release supersedes it.

A successful test against one does not silently prove the other.

## Verified native indicator implementation

The 1.1.0 validation pass inspected the supplied MO2 source rather than approximating the indicator from screenshots.

Verified source locations:

```text
modorganizer/src/moapplication.cpp
modorganizer/src/modlistview.cpp
modorganizer/src/modlistview.h
```

Verified Qt style primitive:

```text
QStyle::PE_IndicatorItemViewItemDrop
```

The source-backed native appearance includes:

- full-width adjustment from the tree indentation;
- `WindowText` palette color;
- two-pixel line;
- five-pixel left triangle;
- antialiasing;
- alpha-50 fill;
- a five-pixel rounded rectangle when MO2 reports an on-item target.

The controller performs a queued reconciliation after MO2 processes each drag event and follows MO2's own `dropIndicatorPosition()` whenever available. The validated position states include Above Item, Below Item, On Item, and On Viewport.

This means the default mode is not a visual imitation. It asks the active MO2 style to paint the same drop-indicator primitive used by the host and follows the host's current target decision.

## Renderer modes

### MO2 Native

This is the **default** and recommended baseline.

It calls MO2's active style engine for `PE_IndicatorItemViewItemDrop`, inherits the live theme, and follows the current native drop-indicator position.

Use this mode first when qualifying a new MO2 release, theme, DPI configuration, or plugin stack.

### Enhanced v1 Overlay

This preserves the original Line Restorer presentation while keeping the same visual-only safety boundary.

Verified presentation features include:

- selection-accent color;
- glow;
- contrast edge;
- arrows on both ends;
- three-pixel center line.

### Fully Custom

Open **Tools > Drag-and-Drop Line Restorer** for the live visual editor.

The recovered 1.1.0 README verifies controls for:

- theme `WindowText`, selection-accent, or custom color;
- 1 to 16 pixel thickness;
- opacity;
- solid, dashed, dotted, or dash-dot line style;
- square or round caps;
- full-width or tree-indented start;
- no markers, MO2 left triangle, or arrows on both ends;
- adjustable marker size;
- optional glow with width and opacity;
- optional automatic high-contrast outline;
- on-item fill opacity;
- rounded-corner radius;
- antialiasing;
- native-position following;
- 4 to 33 ms cursor-follow interval.

Built-in presets are:

- MO2 Native;
- Enhanced v1;
- Clean Accent;
- Neon Glow;
- High Contrast;
- Minimal.

Custom presentation must never create its own semantic drop target. All renderer modes consume the same host-derived target geometry.

## Live preview and tool actions

The customizer includes a themed mini mod list so appearance changes can be previewed without starting a real reorder.

Verified tool actions include:

- **Apply** - apply the current editor values to the live overlay for the current session;
- **Save and Apply** - persist settings through `IOrganizer.setPluginSetting()` and apply them immediately;
- **Test in MO2** - draw a temporary insertion line in the real mod list;
- **Test on-item box** - preview the rounded on-item target state;
- **Reset to MO2 Native** - return to the source-backed default mode.

Existing 1.0.0 settings are harmless. Version 1.1.0 still defaults to `mo2_native` even when older enhanced-only keys remain in MO2's configuration.

## Installation

### Install or replace the plugin

1. Close MO2 completely.
2. Preserve a recoverable copy of the currently installed plugin folder and relevant MO2 plugin settings if replacing an older build.
3. Extract `MO2-Drag-Drop-Line-Restorer-v1.1.0.zip` into MO2's `plugins` directory.
4. Confirm the entry point exists:

```text
MO2/
└─ plugins/
   └─ mo2-drag-drop-line-restorer/
      └─ __init__.py
```

5. Start MO2.
6. Open **Tools > Drag-and-Drop Line Restorer**.
7. Leave **MO2 Native** selected for the first qualification run.
8. Click **Test in MO2** and confirm the overlay attaches to the actual mod list rather than a downloads-pane or other tree-view decoy.
9. Drag an installed mod and then a completed download across the real mod list.
10. Complete the semantic/visual acceptance matrix before treating the installation as qualified.

The plugin should not require cache deletion, mod/profile data migration, or changes to Data/Overwrite because it does not own mod content or load-order state.

## Architecture and ownership boundaries

### View discovery

The validated implementation selects the real `modList` view and rejects a downloads-pane decoy. Discovery correctness is important because painting an overlay over the wrong tree can look superficially functional while providing useless guidance.

### Transparent overlay

The overlay is a child of the real mod-list viewport and remains mouse-transparent. Validation confirms that it does not accept drops.

### Event filter

The drag event filter returns `False`. The plugin observes drag state for painting but does not consume DragEnter, DragMove, DragLeave, or Drop events.

### Position resolution

The plugin follows native `dropIndicatorPosition()` where available. For synthetic or moved columns, the validated implementation can recover a valid row through native-column probes so the overlay remains aligned with host semantics instead of treating a synthetic column as a separate drop universe.

### Rendering

The renderer owns pixels only. Native mode delegates to the active style primitive. Enhanced/custom modes draw alternate presentation using the host-derived target.

### Persistence

Custom settings persist through MO2's plugin-setting API. Persistence of visual settings does not imply ownership of any mod, profile, load-order, or archive state.

## Visual-only safety contract

The plugin must never:

- accept or reject a drag event;
- call `dropMimeData()`;
- move mods;
- install downloads;
- rewrite priorities;
- change `acceptDrops`;
- change drag enablement;
- change drag/drop mode;
- change accepted/proposed/final drop actions;
- change auto-scroll behavior;
- replace the model;
- replace the item delegate;
- change selection;
- turn an invalid target into a valid one;
- add `ItemIsDropEnabled` flags merely so the line remains visible.

The overlay itself must remain mouse-transparent and non-drop-accepting.

## Host-contract invariants

Before and after enabling the plugin, deterministic drag fixtures should prove these values remain identical except for pixels painted by the overlay:

- event accepted/ignored state;
- proposed action;
- final drop action;
- target model index and row;
- model `ItemIsDropEnabled` flags;
- moved mod identity;
- final priority/order;
- selection and current index;
- auto-scroll behavior;
- collapsed/expanded separator state;
- filter/sort/grouping state.

If any of these change because Line Restorer is enabled, the visual-only boundary has been violated.

## Verified automated validation

The v1.1.0 project-owned test report records a complete offscreen pass.

Verified checks include:

1. Python compilation of `plugin.py` and `__init__.py`.
2. Default mode is `mo2_native`.
3. Native mode calls `PE_IndicatorItemViewItemDrop` through the attached view's active style.
4. Exact-source fallback rendering works when style dispatch fails.
5. Native, Enhanced v1, and Fully Custom modes all produce visible output.
6. Custom on-item rounded rectangle renders correctly.
7. Mod-list discovery selects `modList` and rejects a downloads-pane decoy.
8. Synthetic/moved-column cursor positions recover a valid row through native-column probes.
9. Above/below boundary geometry remains stable.
10. The live customizer constructs successfully.
11. Neon and other preset data applies without errors.
12. Custom settings persist through `IOrganizer.setPluginSetting()` and reload correctly.
13. The overlay remains mouse-transparent and does not accept drops.
14. Drag event filtering always returns `False`.
15. No drag event is accepted, rejected, rerouted, or executed by the plugin.

### Performance check

The project-owned v1.1.0 test used a 1,000-row offscreen tree for 100,000 indicator-position calculations:

```text
total:   0.331753 seconds
average: 3.318 microseconds per calculation
```

The cursor-follow timer runs only while a drag is active. The validated drag path performs no filesystem, network, metadata, image-decoding, or model-mutation work.

### Package checks

The validation report also records:

- ZIP layout verified;
- required entry point present;
- extracted package compiled successfully;
- SHA-256 generated after final packaging.

These are strong automated checks, but they do not replace the real Windows host test described below.

## Native renderer qualification

Exact native mode should derive geometry and style from the current view/theme/DPI rather than from hard-coded coordinates copied from an older beta.

Live qualification should cover:

- Above Item;
- Below Item;
- On Item;
- On Viewport when reachable through normal host behavior;
- top/bottom edge targets;
- first/last mod rows;
- separators and collapsible groups;
- horizontal movement across native and synthetic columns;
- filtered, sorted, and grouped views;
- alternate row heights where the host permits them;
- transparent, dark, and light themes;
- 100%, 125%, 150%, 175%, and 200% DPI where practical;
- mixed-monitor DPI transitions where practical.

Theme or DPI changes may alter pixels, but they must not alter semantic target ownership.

## Enhanced/custom qualification

Enhanced v1 and Fully Custom modes may change appearance but not semantic position.

Preserve:

- one source of truth for target geometry;
- live preview consistent with the real renderer;
- preset round-trip without precision loss that changes alignment;
- user settings across full MO2 restart;
- safe reset to exact native mode;
- no animation/effect that obscures the real target at drop time.

## Coordinated plugin-stack requirement

The overlay must be tested with the current synthetic-column compatibility stack:

- [[MO2 Image Column / MO2R Image Automation|PRJ-017-mo2-image-column-mo2r-image-automation]] **1.4.12**;
- [[Bethesda Plugin Info for MO2|PRJ-015-bethesda-plugin-info-for-mo2]] **1.5.3**;
- [[Bethesda Creations Version Tracker for MO2|PRJ-016-bethesda-creations-version-tracker-for-mo2]] **2.4.3**.

The shared root-cause evidence for those synthetic-column plugins found two relevant failure classes:

1. synthetic cells inheriting drop flags from the wrong native column;
2. queued plugin repaint work erasing or destabilizing native drag feedback.

Line Restorer is deliberately separate from those fixes. It should visualize the current host target, not compensate for a broken model/drop contract by manufacturing a different one.

Crossing any dedicated/synthetic column must not move the semantic drop target, suppress native acceptance, or create a second competing drag/drop handler.

## Required real-host acceptance matrix

Use an isolated real Windows MO2 v2.5.2 instance first, with the user's relevant theme/DPI and the coordinated plugin stack. A separate 2.5.3 beta 12 regression lane may be retained because 1.1.0 was built against that supplied source.

| Area | Required proof |
| --- | --- |
| Artifact identity | Loaded Line Restorer is exactly 1.1.0 and SHA-256 evidence is recorded. |
| Host identity | Exact MO2 build, Qt/Python versions, theme, DPI and plugin stack are recorded. |
| Startup | No task-related plugin/MO2/Python errors. |
| View discovery | Overlay attaches to the real `modList`, not another tree view. |
| Visual-only boundary | Enabling the plugin changes pixels only, not event/model/drop semantics. |
| Native mode | Active style paints the indicator and follows the live theme. |
| Above/below target | Line is displayed at the exact target and the mod lands there. |
| On-item target | Rounded target state matches the host decision where the host allows it. |
| Separator target | Group/separator boundaries preserve MO2's native allowed/blocked behavior. |
| Cross-column drag | Moving horizontally across every native/synthetic column does not change the target. |
| Download-to-mod-list drag | Existing external/download drag remains functional. |
| Auto-scroll | Edge scrolling remains native and the overlay follows the actual target. |
| Theme/DPI | Native, enhanced and custom modes align correctly under relevant themes/scales. |
| Presets | Save/load/reset reproduces the intended visual style without semantic drift. |
| Live Apply | Apply and Save and Apply update the live overlay without restart. |
| Repeated drag | No duplicate event filters, flicker accumulation, stale lines, or ghost targets. |
| Cancel/leave | Line clears immediately and native state is unchanged. |
| Restart | Mode/preset/settings persist and native mode can be restored exactly. |
| Logs | No new task-related errors after repeated drag cycles. |

A load-only smoke test, offscreen Qt pass, or visually correct line with the wrong final row placement does not close the gate.

## Development test improvement: Host Drag Contract Recorder

When the canonical 1.1.0 source tree is recovered, add a development-only **Host Drag Contract Recorder** around deterministic drag cases.

Capture:

```text
accepted
proposedAction
dropAction
dropIndicatorPosition
target model index
item flags
final mod order
```

Run each fixture once with Line Restorer disabled and once enabled.

Acceptance requires identical semantic traces. Only expected overlay paint evidence may differ.

This is stronger than screenshot comparison because it proves the visual feature did not take ownership of the operation.

## Troubleshooting

### Tool opens but Test in MO2 paints in the wrong pane

Treat this as view-discovery failure. Confirm the plugin selected the real `modList` tree and rejected downloads or other decoy views. Do not hard-code screen coordinates around the wrong widget.

### Native mode is visible but does not match the active theme

Verify the loaded mode is `mo2_native`, then confirm the active view's style is receiving `PE_IndicatorItemViewItemDrop`. Native mode is expected to inherit the live MO2 style. If style dispatch fails, compare the exact-source fallback rather than approximating a new indicator from screenshots.

### Line looks correct but the mod lands elsewhere

Treat this as a semantic failure. Capture the host `dropIndicatorPosition`, target index, item flags, event actions, and final mod order. Do not move the overlay to the visually expected row if the host reports a different valid target. Fix target observation or the underlying host/plugin compatibility issue.

### Indicator disappears over Image Column or another synthetic column

Run with Line Restorer disabled first. If the host target itself disappears or becomes invalid, the problem is likely in the synthetic-column model/drop contract and should be diagnosed there. Line Restorer must not make the invalid target valid merely to keep drawing.

### Overlay blocks clicks or drag events

The overlay must be mouse-transparent and non-drop-accepting. This is a hard regression. Verify the child overlay attributes and event-filter return path immediately.

### Drag performance degrades

The validated 1.1.0 drag path has no disk/network/media/model work and calculated 100,000 positions at about 3.318 microseconds each in the offscreen harness. Look for duplicate filters/timers, expensive custom painting, or unrelated plugin work before increasing the cursor-follow interval.

### Custom settings do not survive restart

Verify **Save and Apply** was used and inspect the MO2 plugin-setting persistence path. Custom settings were validated through `IOrganizer.setPluginSetting()` and reload. Do not invent a sidecar settings file unless project-owned source later proves one exists.

### Old v1.0 settings are still present

They are expected to be harmless. Version 1.1.0 defaults to native mode. Use **Reset to MO2 Native** if the visible configuration is uncertain.

## Anti-degradation rules

Do not make the line reliable by:

- accepting drag events that MO2 rejected;
- adding `ItemIsDropEnabled` to synthetic/native cells indiscriminately;
- rerouting drop events;
- replacing MO2's drag/drop handler;
- replacing the model or delegate;
- disabling auto-scroll or grouping;
- forcing a fixed row height or DPI assumption;
- hiding target errors behind a visually plausible line;
- disabling other MO2R/MO2 plugins;
- using viewport-only/capped behavior as a correctness shortcut.

## Source recovery priorities

The connected project evidence exposes the current README, test report, hash, behavior, installation layout, and acceptance facts, but not the complete canonical 1.1.0 source tree as a connected repository.

Recover and record:

- exact source/artifact hash relationship;
- canonical repository/worktree/branch if one exists;
- `plugin.py` and `__init__.py` ownership boundaries;
- plugin entry point and event filters/hooks;
- view-discovery implementation;
- native-position reconciliation path;
- geometry calculation path;
- native/enhanced/custom renderer implementation;
- settings/preset schema and persistence keys;
- cleanup on drag leave/drop/cancel;
- target test fixtures;
- packaging command and release layout.

Preserve the detailed operational and safety contract on this page when the source tree is found.

## Exact next action

**Recover the complete 1.1.0 source lineage, add a semantic Host Drag Contract Recorder around the existing target tests, then run MO2 Native, Enhanced v1 and Fully Custom modes in real Windows MO2 v2.5.2 with the full synthetic-column stack. Prove the overlay changes only rendering while exact insertion target, event acceptance, item flags, final mod order, download drag, auto-scroll, theme/DPI, presets, live Apply, cancellation, logs, and full restart persistence remain native. Keep a separate 2.5.3 beta 12 regression lane because that source was used by the 1.1.0 development pass.**

## Evidence boundary

The 1.1.0 package hash, source-backed native renderer behavior, installation layout, renderer modes, settings surface, offscreen automated suite, persistence checks, safety checks, ZIP validation, and performance sample are all verified project-owned evidence.

This page does **not** claim fresh real Windows MO2 v2.5.2 visual/semantic proof, full coordinated-stack qualification, or a newly resolved canonical source repository. Those remain the final promotion gates.
