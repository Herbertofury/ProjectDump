# Bethesda Creations Version Tracker for MO2 Wiki

**Project Constellation ID:** `PRJ-016`  
**Status:** VALIDATED ARTIFACT; current-host live proof pending  
**Latest recovered version:** **2.4.3** shared drag/drop compatibility correction

## Purpose

Bethesda Creations Version Tracker is a Mod Organizer 2 plugin for tracking Bethesda Creation metadata, versions, sources, and conflicts while presenting the data through an MO2-integrated column workflow. The plugin must preserve native MO2 list behavior and user metadata while avoiding per-mod marker-file sprawl or false conflict state.

## Recovered version lineage

Durable Project Constellation continuity preserves this line:

`2.0.0 -> 2.1.0 -> 2.2.0 -> 2.3.0 -> 2.3.1 -> 2.4.0 -> 2.4.1 -> 2.4.2 patch -> 2.4.3 compatibility correction`

The current qualification target is **2.4.3**.

## Important migration history

Version **2.3.1** is a major data-ownership checkpoint. The recovered project record states that it stopped creating `.bethesda-creation-sorter.json` inside every Creation mod, moved ownership into MO2 metadata / central plugin data, quarantined corrupt legacy marker data, and preserved user metadata.

That migration must remain intact in all successors. A future build must not silently reintroduce per-mod sidecars or overwrite user-owned metadata simply to simplify implementation.

## Latest 2.4.3 compatibility correction

The shared MO2 drag/column root-cause report records **2.4.3** with the same dedicated-column drop-capability and repaint corrections used by the coordinated synthetic-column plugin stack.

The preserved failure class had two parts:

1. a synthetic/dedicated column inherited inappropriate drop capability from a native-column baseline;
2. queued repaint/update work could obscure MO2's native insertion line or interfere with drag/drop painting.

The corrected line preserves the dedicated Version Tracker column while leaving reorder/drop ownership with MO2 itself. A plugin-owned drag/drop replacement is outside the accepted architecture.

## Current MO2 host baseline, checked 2026-08-17

The official [Mod Organizer 2 release page](https://github.com/ModOrganizer2/modorganizer/releases/tag/v2.5.2) identifies **v2.5.2** as the current stable release.

That release is directly relevant to this project because it includes Bethesda Creation handling such as ContentCatalog parsing, Creation names/file lists, updated Starfield Creation behavior, and newer plugin-list support. Use MO2 v2.5.2 as the primary current release gate. Preserve older MO2 2.5.3 beta 12 evidence only as regression history when reproducing prior development behavior.

## Coordinated compatibility stack

PRJ-016 belongs to the validated [[MO2 Drag / Column Compatibility Pack|PRJ-024-mo2-drag-column-compatibility-pack]] together with:

- MO2 Image Column **1.4.12**;
- Bethesda Plugin Info **1.5.3**;
- Bethesda Creations Version Tracker **2.4.3**.

Related pages:

- [[Bethesda Plugin Info for MO2|PRJ-015-bethesda-plugin-info-for-mo2]]
- [[MO2 Drag / Column Compatibility Pack|PRJ-024-mo2-drag-column-compatibility-pack]]
- [[MO2R|PCX-035-mo2r]]

The stack is only compatible when all three plugins preserve native insertion targeting, list state, theme/DPI behavior, restart persistence, and their own project-specific data behavior at the same time.

## Functional contract

### Creation metadata

The plugin must surface the intended Bethesda Creation metadata without replacing or corrupting MO2-owned metadata. The recovered continuity specifically calls out version and source data as live-test requirements.

### Version tracking

Version information must remain associated with the correct Creation/mod identity through sorting, filtering, profile changes, and restart. A visually populated column is not sufficient if the values attach to the wrong row or become stale after model changes.

### Source tracking

Source data must remain stable through migration and ordinary MO2 operations. Any future source-recovery pass should document the exact storage keys and precedence rules from the current artifact/source rather than inferring them from old releases.

### Conflict behavior

The current acceptance contract explicitly requires **no false conflicts**. Conflict state must be based on the intended metadata/version rules and must not be triggered merely by stale legacy marker files, reordered rows, or another plugin's column rendering.

### Dedicated column

The Version Tracker column must remain a normal MO2 participant. It can display plugin-owned data, but it must not take ownership of MO2 reorder semantics, selection, scrolling, separators, filters, or native insertion targeting.

## Data ownership and migration contract

The 2.3.1 migration defines a durable rule for successors:

- do not recreate `.bethesda-creation-sorter.json` in every Creation mod;
- use MO2 metadata / central plugin data for plugin-owned state;
- preserve user metadata during migration;
- quarantine corrupt legacy marker data rather than silently treating it as authoritative;
- make migration idempotent so reopening/restarting does not repeat destructive work;
- keep legacy cleanup distinguishable from current active state.

A migration is not verified by reaching startup. It must be tested against representative clean, legacy, corrupt, and partially migrated fixtures.

## Installation and qualification

The complete current 2.4.3 archive layout and canonical source repository are not exposed through the connected project evidence used for this page, so this wiki does not invent a package path or build command.

Use this release qualification sequence:

1. obtain the preserved 2.4.3 artifact from the project's durable archive/continuity source;
2. inspect embedded version/package metadata before installation;
3. preserve a recoverable copy of the current MO2 plugin/configuration state;
4. use an isolated MO2 v2.5.2 Windows instance for first qualification;
5. install the exact coordinated versions when testing shared column behavior: Image Column 1.4.12, Bethesda Plugin Info 1.5.3, Version Tracker 2.4.3;
6. launch MO2 and verify clean plugin startup;
7. exercise migration, metadata, conflicts, column behavior, drag/drop, and restart using the matrix below.

## Required real-host acceptance matrix

| Area | Required proof |
| --- | --- |
| Host identity | Exact MO2 v2.5.2 build is recorded. |
| Plugin identity | Loaded artifact is proven to be Version Tracker 2.4.3. |
| Startup | No task-related MO2/Python/plugin errors. |
| Legacy migration | Representative legacy `.bethesda-creation-sorter.json` state migrates once and is not recreated per mod. |
| Corrupt marker handling | Corrupt legacy data is quarantined and does not overwrite valid user/current metadata. |
| Metadata preservation | Existing user metadata survives migration and restart. |
| Version data | Correct version data appears on the correct Creation/mod rows. |
| Source data | Correct source data remains stable under sort/filter/profile changes. |
| Conflicts | Known fixtures produce intended conflicts and clean fixtures do not produce false conflicts. |
| Dedicated column | Column appears once, moves/resizes safely, and native columns remain unchanged. |
| Native drag/drop | Native insertion indicator remains visible and the final drop lands at the exact intended target. |
| Cross-column drag | Crossing the Version Tracker column does not change MO2 drop semantics. |
| Coordinated stack | Image Column 1.4.12 and Bethesda Plugin Info 1.5.3 still behave correctly. |
| Theme/DPI | Geometry, text, painting, and insertion targeting remain correct. |
| Restart | Plugin data, column state, and migration completion persist after a full MO2 restart. |
| Logs | No new task-related errors appear in MO2/Python/plugin logs. |

A load-only smoke test, synthetic widget test, or visually correct insertion line without correct final row placement does not close the gate.

## Troubleshooting

### Legacy marker files reappear

Treat this as a migration regression. Confirm the loaded version is 2.4.3, inspect whether the active code is writing `.bethesda-creation-sorter.json`, and verify that central/MO2 metadata storage is writable and being selected. Do not accept sidecar recreation as a fallback.

### Migration loses user metadata

Stop promotion of the build. Compare pre-migration metadata, quarantined legacy content, and post-migration central state. The preserved 2.3.1 contract requires user metadata preservation.

### False conflicts appear

Record the exact Creation identity, stored version/source metadata, expected conflict state, and actual conflict state. Check for stale legacy data and duplicate identity before changing conflict logic. Do not suppress all conflicts to hide a bad rule.

### Version/source data changes after sorting or filtering

Verify whether row identity or model mapping is wrong rather than the underlying data. The dedicated column must track the correct mod/Creation through proxy/model changes.

### Native insertion line disappears over the Version Tracker column

Treat this as a regression of the 2.4.3 shared compatibility correction. Verify theme/DPI, coordinated plugin versions, and repaint/drop-capability behavior. Do not replace MO2 native drag/drop.

### Restart repeats migration

Migration should be idempotent. Capture pre-close state, fully exit MO2, reopen the same instance/profile, and confirm that already migrated data is recognized without duplicate writes or re-quarantine.

## Modification and contribution rules

Until the canonical source tree is recovered, do not invent module names or build commands. When source is available, preserve these verified requirements:

1. keep migration idempotent and user-metadata-preserving;
2. keep active plugin state in MO2 metadata / central plugin data rather than per-mod marker files;
3. quarantine corrupt legacy data instead of treating it as current truth;
4. preserve version/source identity through model/proxy changes;
5. preserve accurate conflict behavior and explicitly test clean fixtures against false positives;
6. preserve native MO2 drag/drop ownership and insertion targeting;
7. test with Image Column 1.4.12 and Bethesda Plugin Info 1.5.3 when shared column/paint/drop behavior changes;
8. verify the intended theme/DPI configuration and full restart persistence;
9. preserve useful historical migration evidence rather than deleting it from documentation.

## Source recovery priorities

The next source-recovery pass should locate and record:

- canonical repository or preserved 2.4.3 source archive;
- exact artifact/source hashes;
- plugin entry point and MO2 interfaces used;
- central metadata/settings persistence implementation;
- migration detector and legacy quarantine path;
- Creation identity and version/source resolution logic;
- conflict calculation path and fixtures;
- dedicated-column model/delegate/proxy implementation;
- exact 2.4.3 drop-capability/repaint correction;
- test runner, fixtures, packaging command, and release archive layout.

Once recovered, add exact install/build/test/package instructions and a module interaction diagram without discarding the behavioral and migration contract already captured here.

## Verification boundary

This page currently does **not** claim that 2.4.3 has completed fresh real Windows MO2 v2.5.2 qualification. It also does not claim that the complete 2.4.3 source tree or exact packaging commands are available in a connected GitHub repository.

Those are explicit remaining proof tasks.

## Exact next action

**Recover or identify the exact Bethesda Creations Version Tracker 2.4.3 artifact/source bytes, record their hash and package layout, then install 2.4.3 with Image Column 1.4.12 and Bethesda Plugin Info 1.5.3 in an isolated MO2 v2.5.2 Windows instance. Verify legacy migration, metadata preservation, version/source data, no false conflicts, dedicated-column behavior, native drag/drop, theme/DPI, logs, and full restart persistence before promoting the stack as live-qualified.**
