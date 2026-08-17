# Bethesda Creations Version Tracker for MO2 Wiki

**Project Constellation ID:** `PRJ-016`  
**Status:** VALIDATED ARTIFACT; current-host live proof pending  
**Latest recovered version:** **2.4.3** compatibility correction

## Purpose

Bethesda Creations Version Tracker tracks Bethesda Creation metadata, version/source state, migration history, and conflict-relevant information inside Mod Organizer 2 while preserving MO2's native list, drag/drop, profile, and persistence behavior.

## Recovered version lineage

Recovered lineage is `2.0.0 -> 2.1.0 -> 2.2.0 -> 2.3.0 -> 2.3.1 -> 2.4.0 -> 2.4.1 -> 2.4.2 -> 2.4.3`.

The most important migration boundary is **2.3.1**: it stopped writing `.bethesda-creation-sorter.json` into every Creation mod, moved owned state into MO2 metadata/central plugin data, quarantined corrupt legacy marker data, and preserved user metadata.

The later shared drag/drop root-cause work produced **2.4.3**, carrying the dedicated-column drop-flag and repaint corrections used by the coordinated MO2 compatibility pack.

## Current MO2 host baseline, checked 2026-08-17

The official [Mod Organizer 2 release](https://github.com/ModOrganizer2/modorganizer/releases/tag/v2.5.2) remains **v2.5.2**. It includes Qt/PyQt 6.7.1, Python 3.12.3, Starfield Creation support changes, and additional third-party plugin capabilities.

The upstream [MO2 master](https://github.com/ModOrganizer2/modorganizer) remains active beyond that release, observed in this pass at `efe2a02d5dc641946baaa8db1440800f38d07837`. The [MO2 Python plugin](https://github.com/ModOrganizer2/modorganizer-plugin_python) is also active, observed at `e9d55a50a7c9f38280e72f52d910852fdcf0321e`, with 2026 additions around instance/profile and executable-list APIs.

### Compatibility decision

Use **MO2 v2.5.2 as the primary live release gate**. Only after that exact path passes should current upstream master be used as a separate forward-compatibility lane. Preserve the existing plugin data model unless a verified host/API change requires migration.

## Migration and data-integrity contract

The tracker must preserve all Creation state across upgrade and restart. In particular:

- legacy marker data is migrated once rather than recreated per mod;
- corrupt legacy marker data is quarantined, not silently discarded;
- user metadata survives migration;
- version/source metadata stays bound to stable mod identity rather than transient row position;
- false conflicts remain zero in the deterministic fixture set;
- no plugin-owned drag/drop behavior is introduced;
- no game Data or Overwrite writes are added as a shortcut.

## Current Creation-specific qualification

MO2 v2.5.2 changed Starfield Creation handling, including ContentCatalog-based Creation parsing and other Starfield load-order/plugin updates. The Version Tracker therefore needs current fixtures that cover at minimum:

1. legacy marker migration;
2. clean current metadata;
3. corrupt marker quarantine;
4. Starfield Creation metadata sourced from current MO2 behavior;
5. mods with incomplete or conflicting display metadata;
6. restart persistence after migration;
7. profile switch with the same Creation installed under different profile state.

Never infer authoritative version identity from display text alone when stronger source metadata exists.

## Coordinated drag/column contract

PRJ-016 participates in the [MO2 Drag/Column Compatibility Pack](PRJ-024-mo2-drag-column-compatibility-pack.md) with Image Column 1.4.12 and Bethesda Plugin Info 1.5.3. The three plugins must be qualified together.

Required live behavior includes:

- Version Tracker's dedicated column remains correct, movable, resizable and persistent;
- native columns remain unchanged;
- native insertion target/line remains visible and lands exactly where expected;
- download-to-mod-list drag remains intact;
- selection, scroll, separators, sorting, filtering, search and profile state remain stable;
- theme/DPI changes do not corrupt target geometry or cell painting;
- repeated drag/drop does not accumulate handlers or stale repaint state;
- metadata/conflict state remains correct after restart.

## Exact next action

**Install Version Tracker 2.4.3 with Image Column 1.4.12 and Bethesda Plugin Info 1.5.3 in real Windows MO2 v2.5.2. Run deterministic migration/Creation fixtures plus the full drag/column/restart matrix, then use current upstream master only as a separate forward-compatibility lane.**

## Evidence boundary

Recovered artifact and compatibility evidence is strong, but current Windows MO2 v2.5.2 runtime success has not yet been established in this pass. Do not promote the project beyond that boundary until exact live evidence exists.
