# Favorite Artist Worlds Database Wiki

**Project Constellation ID:** `PCX-047`
**Status:** ACTIVE / TRACKED
**Goal:** Preserve and operationalize favorite-artist worldbuilding data for Feature Foundry.
**Current verified lineage:** `feature-foundry-favorite-artist-worlds-v4.0.1` / `feature-foundry-favorite-artist-worlds-CURRENT.xlsx`.

## Verified current state

The current durable database line is **v4.0.1**. Its README identifies v4.0.1 as a focused saveroom naming correction built from the verified v4.0.0 database without removing or replacing prior artists, worlds, source records, or reference assets.

The canonical corrected district name is **Azure Save Coast** for the stable ID `district.saveroom.paradise-zero-lagoon`. The name is recorded as synchronized across JSON, SQLite, full-text search, the editable workbook, and the Sunshower Bloom weather trigger while the stable ID remains unchanged.

### Included artists

1. Frawgy
2. Lightweaverart
3. Dreamrelicc
4. Karoline Georges
5. saveroom

### Verified database totals

- 5 artists
- 10 world variants
- 20 districts
- 20 weather systems
- 25 interaction rules
- 21 Spotify/music routes
- 75 discovery links
- 50 provenance records

### Verified integrity evidence

The v4.0.1 README records:

- JSON relational and unique-ID checks passing;
- SQLite integrity checks passing;
- SQLite foreign-key checks passing;
- SQLite full-text-search checks passing;
- workbook structural checks passing;
- all 31 supplied references remaining embedded;
- ZIP reopened and tested after creation;
- fresh extraction checked against SHA-256 sums.

The workbook `feature-foundry-favorite-artist-worlds-CURRENT.xlsx` exposes the same v4.0.1 curator line and summary counts.

## Data contract

An artist theme is a complete world package, not merely a palette or wallpaper. The durable workbook explicitly models artist worlds as structured systems with provenance, weather, interactions, discovery, and music routes.

Stable IDs are integration contracts. Human-readable corrections such as Azure Save Coast must not break IDs used by Feature Foundry, search indexes, weather triggers, saved worlds, or host adapters.

## Provenance boundary

Artist/source/profile/music/reference links are curation provenance. They must remain attached to the relevant records and must not be silently collapsed into unsourced generated content.

Keep separate fields for:

- artist identity;
- source URL;
- source type;
- captured/reference asset identity;
- SHA-256 when available;
- world/district relationship;
- music route;
- verification date;
- notes/interpretation;
- shipping/promoted state.

Research inclusion does not automatically promote a world or asset into a shipping Feature Foundry theme.

## Current SQLite research

The current SQLite release is **3.53.4**, released July 24, 2026. The 3.53 line includes query-planner changes such as improved large star-schema join ordering, broader EXISTS-to-JOIN optimization, omit-noop-join improvements, and sort-and-merge handling for compound queries.

Primary sources:

- https://sqlite.org/
- https://www2.sqlite.org/releaselog/3_53_4.html
- https://www2.sqlite.org/changes.html

These changes could improve discovery and relationship queries, but a database-engine update is not automatically an application improvement. The current v4.0.1 data and integrity behavior must remain the baseline.

## Proposed database-engine verification lane

Add the exact SQLite engine/source ID to validation output, then run the existing v4.0.1 fixture suite against SQLite 3.53.4 before changing the durable database line.

Measure at least:

- integrity check result;
- foreign-key violations;
- FTS result parity;
- stable-ID count and uniqueness;
- row counts for every entity class;
- representative artist -> world -> district -> weather -> interaction joins;
- discovery-search latency;
- query plans for the largest join/search paths;
- export/import byte or semantic equivalence where applicable.

Only adopt a new SQLite runtime after correctness parity and a measurable benefit or a needed bug fix are proven.

## Anti-regression rules

- Never regenerate stable IDs for cosmetic naming corrections.
- Never drop provenance/reference records to reduce file size.
- Never replace a duplicate reference occurrence merely because its bytes match another occurrence if the occurrence itself is meaningful provenance.
- Never flatten all artist worlds into one generic theme schema that loses artist-specific districts, weather, interactions, or music routes.
- Never treat a newer workbook timestamp alone as stronger evidence than the v4.0.1 verified lineage.
- Preserve JSON, SQLite, workbook, FTS, and archive validation together when the database changes.

## Exact next action

Run the v4.0.1 validation suite against the current SQLite 3.53.4 engine, record the engine/source identity and query-plan deltas, and keep the database content unchanged unless the test proves a safe material improvement.

## Evidence

- Current workbook: https://docs.google.com/spreadsheets/d/1BLxXdbNN0hJggKDJ16fBFv86OOep1Q40/edit
- v4.0.1 workbook: https://docs.google.com/spreadsheets/d/1X1NySI08HjVAlcjJEfXQzNrjc7ELEsB4/edit
- v4.0.1 README: https://drive.google.com/file/d/1UulWpSH2wvIq4Zj08SPdlqKtxpalPuAM/view

## Wiki maintenance

Update this page when artist/world counts, stable IDs, provenance records, schema versions, search/index behavior, database engine identity, integrity evidence, or Feature Foundry promotion status changes. Preserve all prior validated lineage.