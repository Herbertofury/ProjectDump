# MO2 Drag-and-Drop Line Restorer Wiki

**Project Constellation ID:** `PRJ-018`
**Status:** VALIDATED ARTIFACT; real-host visual/target proof pending
**Latest recovered version:** **1.1.0**
**Recovered SHA-256:** `615b3b05e081ce6c529b4e9e117dbdc207f30e0dca5c858c31739a0981da7b56`

## Purpose

MO2 Drag-and-Drop Line Restorer is a **visual-only overlay** for the Mod Organizer 2 mod list. It restores an always-visible, configurable drop indicator while leaving acceptance, rejection, rerouting, ordering, and execution of drag/drop entirely with MO2.

That boundary is the project's core safety property. A visually correct line with the wrong final insertion target is a failure.

## Recovered 1.1.0 feature set

The recovered artifact adds:

- exact MO2 native renderer mode;
- Enhanced v1 mode;
- Fully Custom mode;
- live preview;
- presets;
- target tests;
- native indicator positioning.

The current qualification target is the exact 1.1.0 artifact identified above.

## Current MO2 host baseline, checked 2026-08-17

The official [Mod Organizer 2 v2.5.2 release](https://github.com/ModOrganizer2/modorganizer/releases/tag/v2.5.2) remains the primary stable host gate. Current [MO2 master](https://github.com/ModOrganizer2/modorganizer) is active beyond the release and was observed at `efe2a02d5dc641946baaa8db1440800f38d07837` for this pass.

Current upstream source makes the ownership boundary explicit:

- `ModListView::dragMoveEvent()` performs MO2-specific timer/state handling and then delegates the drag move to `QAbstractItemView::dragMoveEvent()`;
- current `ModList::flags()` only enables `Qt::ItemIsDropEnabled` for the host-defined valid cases rather than on every cell;
- MO2's drop path uses its own model/view logic to resolve the final target.

This is direct current-host evidence that Line Restorer must paint from host state without manufacturing independent drop acceptance rules.

## Qt drop-indicator contract

Qt's current `QAbstractItemView` contract exposes `DropIndicatorPosition` values for `OnItem`, `AboveItem`, `BelowItem`, and `OnViewport`, and the view/model together determine whether a drag/drop position is valid.

Line Restorer may observe/translate this state for painting, but it must not turn an invalid target into a valid one, change the event's accepted state, change the proposed/drop action, or mutate model item flags simply to keep the overlay visible.

## Host-contract invariants

Before and after enabling the plugin, a deterministic drag fixture should prove that these values remain identical except for pixels painted by the overlay:

- event acceptance / ignored state;
- proposed action and final drop action;
- target index and row;
- model `ItemIsDropEnabled` flags;
- moved mod identity and final priority/order;
- selection and current index;
- auto-scroll behavior;
- collapsed/expanded separator state;
- filter/sort/grouping state.

If any of these change because Line Restorer is enabled, the plugin has crossed its visual-only boundary.

## Native renderer mode

Exact native renderer mode should derive its geometry and style from the current view/theme/DPI rather than hard-coded coordinates from an older beta.

Qualification must cover:

- above-row and below-row targets;
- top/bottom edge targets;
- separators and collapsible groups;
- first/last mod rows;
- horizontal movement across every native and synthetic column;
- filtered and grouped views;
- different row heights where the host permits them;
- transparent/dark/light themes;
- 100%, 125%, 150%, 175%, 200% and mixed-monitor DPI scenarios where practical.

## Enhanced and custom modes

Enhanced v1 and Fully Custom modes may change the line's visual treatment, but not its semantic position.

Preserve:

- one source of truth for target geometry;
- live preview that matches actual renderer geometry;
- preset round-trip without precision loss that affects target alignment;
- user settings across full MO2 restart;
- a safe reset to exact native mode;
- no animation/effect that obscures the real target at the moment of drop.

## Coordinated plugin-stack requirement

The visual overlay must be tested with the current synthetic-column compatibility stack:

- [[MO2 Image Column / MO2R Image Automation|PRJ-017-mo2-image-column-mo2r-image-automation]] **1.4.12**;
- [[Bethesda Plugin Info for MO2|PRJ-015-bethesda-plugin-info-for-mo2]] **1.5.3**;
- [[Bethesda Creations Version Tracker for MO2|PRJ-016-bethesda-creations-version-tracker-for-mo2]] **2.4.3**.

Crossing any dedicated/synthetic column must not move the semantic drop target, suppress native acceptance, or create a second competing drag/drop handler.

## Required real-host acceptance matrix

Use an isolated real Windows MO2 v2.5.2 instance with the user's relevant theme/DPI and the coordinated plugin stack.

| Area | Required proof |
| --- | --- |
| Artifact identity | Loaded Line Restorer is exactly 1.1.0 and hash evidence is recorded. |
| Startup | No task-related plugin/MO2/Python errors. |
| Visual-only boundary | Enabling the plugin changes pixels only, not event/model/drop semantics. |
| Above/below target | Line is displayed at the exact target and the mod lands there. |
| Separator target | Group/separator boundaries preserve MO2's native allowed/blocked behavior. |
| Cross-column drag | Moving horizontally across all columns does not change the target. |
| Download-to-mod-list drag | Existing external/download drag remains functional. |
| Auto-scroll | Edge scrolling remains native and the overlay follows the actual target. |
| Theme/DPI | Native, enhanced and custom modes align correctly under relevant themes/scales. |
| Presets | Save/load/reset reproduces the intended visual style without semantic drift. |
| Repeated drag | No duplicate event filters, flicker accumulation, stale lines, or ghost targets. |
| Cancel/leave | Line clears immediately and native state is unchanged. |
| Restart | Mode/preset/settings persist and native mode can be restored exactly. |
| Logs | No new task-related errors after repeated drag cycles. |

## Test-harness improvement proposal

Add a **Host Drag Contract Recorder** to the development test harness when canonical source is recovered. For each deterministic drag case, capture before/after:

`accepted -> proposedAction -> dropAction -> dropIndicatorPosition -> target model index -> item flags -> final mod order`

Run each fixture once with Line Restorer disabled and once enabled. Acceptance requires identical semantic traces and only the expected overlay-paint evidence to differ.

This is a stronger regression gate than screenshot comparison alone because it proves the visual feature did not take ownership of the drop operation.

## Anti-degradation rules

Do not make the line reliable by:

- accepting drag events that MO2 rejected;
- adding `ItemIsDropEnabled` to synthetic/native cells indiscriminately;
- rerouting drop events;
- replacing MO2's drag/drop handler;
- disabling auto-scroll or grouping;
- forcing a fixed row height or DPI assumption;
- hiding target errors behind a visually plausible line;
- disabling other MO2R/MO2 plugins.

## Source recovery priorities

The connected project evidence does not yet expose the complete canonical 1.1.0 source tree. Recover and record:

- exact artifact/source hash relationship;
- plugin entry point and event filters/hooks;
- geometry calculation path;
- native/enhanced/custom renderer implementation;
- settings/preset schema;
- cleanup on drag leave/drop/cancel;
- target test fixtures;
- packaging command and release layout.

## Exact next action

**Recover the exact 1.1.0 source/artifact lineage, add a semantic Host Drag Contract Recorder around the existing target tests, then run native/enhanced/custom modes in real Windows MO2 v2.5.2 with the full synthetic-column stack, proving the overlay changes only rendering while exact insertion target, event acceptance, item flags, final mod order, auto-scroll, theme/DPI, cancellation, logs, and restart behavior remain native.**

## Evidence boundary

The artifact and automated target evidence are preserved, but this page does not claim fresh real Windows MO2 v2.5.2 visual/semantic proof. That remains the final release gate.
