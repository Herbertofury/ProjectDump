# MO2 Image Column / MO2R Image Automation Wiki

**Project Constellation ID:** `PRJ-017`
**Status:** ACTIVE corrected build; current-host live stack proof pending
**Latest recovered version:** **Image Column 1.4.12**

## Purpose

MO2 Image Column adds compact visual media to the Mod Organizer 2 mod list while preserving exact mod identity, native MO2 list behavior, complete off-screen availability, compact row density, drag/drop, sorting/filtering, separators, profile state, and restart persistence.

The image system is not a decorative thumbnail-only feature. Its contract includes resolving the correct image for the correct mod from the available local and remote source evidence, caching it safely, and keeping the rest of MO2's list semantics intact.

## Recovered version lineage

Durable Project Constellation continuity preserves this compatibility line:

- restored **1.4.10** base;
- rejected/avoided the **1.4.11 delegate-substitution** path as the final compatibility direction;
- **1.4.12** shared drag/drop correction.

The current qualification target is **1.4.12**.

## Preserved image/source contract

The broader MO2R Image Column design keeps multi-source media support instead of collapsing to one provider. Where project-owned adapters/evidence are available, preserve support for:

- Nexus Mods;
- Bethesda Creations / Creation Club;
- Patreon;
- Dwemer Mods;
- Mod DB;
- CurseForge;
- GitHub and GitLab;
- Modding Guild;
- local mod media;
- generic source pages using standards-based metadata and gallery fallbacks.

Nexus resolution should retain authenticated/API paths plus standards-based page metadata fallbacks when appropriate. Source expansion must not weaken stable mod identity, provenance, or duplicate-title handling.

## Current MO2 host baseline, checked 2026-08-17

The official [Mod Organizer 2 v2.5.2 release](https://github.com/ModOrganizer2/modorganizer/releases/tag/v2.5.2) remains the primary stable host gate. It ships Qt/PyQt 6.7.1 and Python 3.12.3.

Current [MO2 master](https://github.com/ModOrganizer2/modorganizer) is active beyond that release. The observed head for this pass is `efe2a02d5dc641946baaa8db1440800f38d07837`.

The current upstream `ModListView` installs its own `ModListStyledItemDelegate`. That delegate does more than generic cell painting: it preserves collapsible-separator indentation behavior, restores background brushes, computes marker/background colors, and selects readable text colors. This is strong current-host evidence for **not replacing MO2's whole list delegate merely to render the image column**.

Upstream MO2 also has explicit theme-related rendering history, including fixes for transparent stylesheet backgrounds, and its Qt 6 path no longer depends on the obsolete `AA_EnableHighDpiScaling` application attribute. Theme transparency and DPI therefore remain real qualification dimensions, not cosmetic test cases.

## Rendering integration rule

Image Column 1.4.12 must preserve MO2's base delegate behavior. The preferred architecture is a narrow column-specific render/paint path that composes with the host rather than substituting the entire mod-list delegate.

A future source recovery/implementation pass should prove:

1. the active MO2 base delegate remains installed or equivalently preserved;
2. Image Column rendering is restricted to its intended synthetic/dedicated column;
3. separator indentation, background color, text contrast, marker painting, selection, focus, and theme behavior remain unchanged in native columns;
4. row height remains compact by default;
5. image decode/scale/cache work does not run synchronously on scroll/hover when it can be prepared safely off the UI hot path.

## Identity and cache contract

Every image must bind to stable mod identity and source provenance, never only the visible row index or display title.

Required behaviors include:

- duplicate/similar mod names do not cross-wire thumbnails;
- sorting/filtering/reordering does not change image ownership;
- asynchronous completion for an older request cannot overwrite a newer row/mod identity;
- cached media records its source and invalidation evidence;
- missing/failed media resolves to a truthful fallback state rather than stale media from another mod;
- full list availability is preserved with no viewport-only source discovery or artificial mod-count cap;
- compact row height remains the default even when larger preview surfaces are available elsewhere.

## Current Qt testing opportunity

Current Qt 6 provides `QAbstractItemModelTester` in the Qt Test module for continuous, non-destructive model-consistency checks. This is useful as an **additive test-harness candidate**, not a runtime dependency requirement. If the recovered Image Column test environment exposes a matching QtTest/PyQt QtTest binding, attach model-consistency checks to the synthetic-column/proxy model during CI and regression testing.

Do not add a QtTest binary/runtime dependency to the shipping plugin merely for this test. The test harness must match the host Qt version being qualified.

## Coordinated drag/column contract

PRJ-017 is part of the validated [[MO2 Drag / Column Compatibility Pack|PRJ-024-mo2-drag-column-compatibility-pack]] with:

- Image Column **1.4.12**;
- Bethesda Plugin Info **1.5.3**;
- Bethesda Creations Version Tracker **2.4.3**.

The recovered root-cause work corrected synthetic-column drop capability and repaint behavior while retaining Image Column's own rendering path.

The combined stack must preserve:

- native MO2 insertion targeting and final drop position;
- download-to-mod-list drag;
- image identity and thumbnails;
- tooltips;
- selection and scroll;
- separators;
- sorting/filter/search;
- profile state;
- theme/DPI rendering;
- restart persistence.

## Required real-host acceptance matrix

Use an isolated real Windows MO2 v2.5.2 instance and the exact coordinated plugin versions.

| Area | Required proof |
| --- | --- |
| Host identity | Exact MO2 v2.5.2 build and loaded plugin artifact are recorded. |
| Plugin identity | Image Column is proven to be 1.4.12, not a stale 1.4.10/1.4.11 copy. |
| Dedicated column | Appears once, moves/resizes safely, and native columns remain unchanged. |
| Base delegate | Native separator/background/text/selection behavior remains correct. |
| Thumbnail identity | Correct image remains attached to the exact mod through sort/filter/reorder. |
| Duplicate names | Duplicate/similar names do not cross-wire cached media. |
| Source fallback | Local/remote/generic-source fallback resolves truthfully without stale wrong-mod media. |
| Drag reorder | Native insertion line remains visible and final row placement is exact. |
| Download drag | Download-to-mod-list drag still installs/targets normally. |
| Scrolling | Rapid full-list scrolling stays responsive and preserves complete off-screen availability. |
| Separators | Separator rows and collapsible/grouped layouts remain correct. |
| Theme/DPI | Transparent themes, alternate backgrounds, and DPI changes do not corrupt painting/geometry. |
| Async safety | Rapid hover/scroll/filter changes do not show an older mod's image. |
| Restart | Column layout, cache identity, and settings persist after full MO2 restart. |
| Logs | No new task-related MO2/Python/plugin errors. |

## Anti-degradation rules

Do not solve image performance or compatibility by:

- viewport-only discovery or rendering caps;
- limiting the number of mods with media;
- lowering media quality globally;
- disabling remote providers already supported by the project;
- replacing MO2's full list delegate with a generic substitute;
- increasing row height by default;
- disabling native drag/drop or the insertion indicator;
- hiding stale-identity bugs with a generic placeholder;
- dropping provenance/source metadata.

## Source recovery priorities

The connected Project Constellation evidence does not yet expose the complete canonical 1.4.12 source tree. The next source-recovery pass should record:

- canonical repository/worktree/branch and artifact hash;
- plugin entry point and MO2 interfaces used;
- image-source adapter registry and precedence rules;
- stable mod identity key and duplicate-resolution logic;
- cache schema, invalidation policy, and asynchronous request ownership;
- column model/proxy/delegate integration;
- exact 1.4.12 drop-capability/repaint correction;
- test runner, fixtures, packaging command, and archive layout.

## Exact next action

**Recover or identify the exact Image Column 1.4.12 source/artifact bytes, prove the host delegate integration against current MO2 master behavior, then live-test 1.4.12 together with Bethesda Plugin Info 1.5.3 and Version Tracker 2.4.3 in MO2 v2.5.2 across identity, thumbnails, duplicate names, source fallbacks, insertion targeting, download drag, scrolling, separators, transparent themes/DPI, logs, and full restart persistence.**

## Evidence boundary

Automated compatibility evidence and the recovered 1.4.12 lineage are strong, but this page does not claim fresh real Windows MO2 v2.5.2 qualification or a newly recovered canonical source tree. Those remain explicit proof gates.
