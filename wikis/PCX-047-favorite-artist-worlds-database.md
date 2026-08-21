# Favorite Artist Worlds Database Wiki

**Project Constellation ID:** `PCX-047`  
**Status:** ACTIVE / TRACKED  
**Goal:** Preserve and operationalize favorite-artist worldbuilding data for Feature Foundry.  
**Current durable curation lineage:** `feature-foundry-favorite-artist-worlds-v4.0.1` / `feature-foundry-favorite-artist-worlds-CURRENT.xlsx`.  
**Current production consumer:** `Herbertofury/Feature-Foundry` v24.0.0 at verified head `e1ba080b5c7590f1c844a6ed13b3a471709920b9`.

## Authority model

PCX-047 now has two complementary authority layers that must not be collapsed into one version number.

1. **Favorite Artist Worlds v4.0.1** is the current durable curation/database authority. It owns artist identity, stable world/district IDs, provenance, weather, interaction, discovery, music-route, and reference data.
2. **Feature Foundry v24.0.0** is the current production application consumer. It embeds the verified v4.0.1 JSON authority into the shipped typed application and native SQLite catalog.

A Feature Foundry application release does not silently create a new Favorite Artist Worlds database version. A new workbook or JSON timestamp likewise does not automatically supersede v4.0.1 without integrity and lineage proof.

## Verified v4.0.1 curation authority

The embedded production source identifies its authority as:

```text
title: Feature Foundry Favorite Artist Worlds
lineage: feature-foundry-favorite-artist-worlds-v4.0.1
sourceDriveFileId: 1BLxXdbNN0hJggKDJ16fBFv86OOep1Q40
sourceFile: feature-foundry-favorite-artist-worlds-CURRENT.xlsx
workbookSha256: fbed5880cc3440e983ad7d418b36258c824808454a8109c52470238ec393b60e
canonicalJsonSha256: 9865ef491c5baeec39702a0a6724df1bf9c9a29ed062a30e6bb6af270dd6b00a
canonicalSqliteSha256: a825ad348280342a92b713146375999ab18d3e8067dcac531d177c7636deac78
status: CURATION_AUTHORITY
```

The current embedded authority was extracted into the production repository on 2026-08-19.

### Promotion rule

The production data preserves this explicit curation rule:

> `CANDIDATE` and `SEARCH_ROUTE` music entries require Bert's explicit listening approval before `APPROVED`.

Do not convert research inclusion into shipping approval merely because the record is present in a production repository.

## Included artists

The current verified artist set remains:

1. Frawgy
2. Lightweaverart
3. Dreamrelicc
4. Karoline Georges
5. saveroom

The production authority test asserts this exact ordered unique artist-name set.

## Verified database totals

The v4.0.1 authority records:

- 5 artists
- 10 world variants
- 20 districts
- 25 aesthetic-DNA records
- 20 weather systems
- 20 timeflow records
- 25 interaction rules
- 21 music routes
- 75 discovery links
- 50 provenance records
- 9 glossary records

These counts are now also enforced in the Feature Foundry v24 production authority test for the entity classes that the current application consumes directly.

## Stable correction: Azure Save Coast

The canonical corrected district name is **Azure Save Coast** for the stable ID:

```text
district.saveroom.paradise-zero-lagoon
```

The v4.0.1 correction changed the human-readable name while preserving the stable ID. Production `tests/authority.test.ts` explicitly asserts that this ID resolves to `Azure Save Coast`.

Stable IDs are integration contracts. Naming, presentation, and curation corrections must not silently break IDs referenced by:

- Feature Foundry runtime data;
- native SQLite rows;
- full-text search;
- weather triggers;
- saved worlds;
- source-hub music routes;
- host adapters;
- user-created mappings.

## Feature Foundry v24 production integration

### Embedded source

Current production source:

```text
src/data/artist-worlds-v4.0.1.json
```

contains the curation authority, counts, artists, worlds, districts, weather, timeflow, interactions, music routes, discovery links, provenance, glossary, and stable IDs used by the application.

The current repository blob for that file is:

```text
aeb91447df265ae816b82a37ea1ea31bf3b76997
```

### Production authority test

`tests/authority.test.ts` reads the embedded JSON and asserts:

- 5 artists;
- 10 worlds;
- 20 districts;
- 20 weather records;
- 25 interactions;
- 21 music routes;
- 75 discovery links;
- 50 provenance rows;
- the Azure Save Coast stable-ID correction;
- the exact five-artist set;
- the current music-route approval-status vocabulary.

It also verifies that the native database source contains the expected catalog/music commands and the canonical artist-world JSON hash.

Current authority-test blob:

```text
7e53258e065239fc5351d6d0d842eac6940eb95b
```

### Native SQLite seeding

`src-tauri/src/database.rs` embeds the JSON with:

```rust
const ARTIST_WORLDS: &str = include_str!("../../src/data/artist-worlds-v4.0.1.json");
```

The native database seeds and updates dedicated tables including:

```text
artist_worlds
artist_districts
artist_weather
music_routes
room_soundtracks
history
```

The database records the canonical artist-world JSON SHA-256 in metadata:

```text
9865ef491c5baeec39702a0a6724df1bf9c9a29ed062a30e6bb6af270dd6b00a
```

This gives the production runtime a durable source fingerprint rather than relying on filenames or workbook timestamps alone.

### Native database behavior

The current Tauri database:

- enables foreign keys;
- uses WAL journaling;
- uses `synchronous=NORMAL`;
- exposes `catalog_summary`;
- exposes `list_music_routes`;
- stores room soundtrack mappings separately from source curation records;
- records native history events.

`catalog_summary` returns the SQLite runtime version plus current durable artist/world counts and `PRAGMA integrity_check` result. That makes the actual SQLite engine identity observable from the production runtime rather than inferred from a documentation page.

### Production world count

Feature Foundry v24 documents:

- 17 approved durable theme packages;
- 10 current favorite-artist worlds.

The browser UI acceptance test expects the Theme Atlas to expose **27 catalog worlds**, preserving both authority families in the production application.

Do not merge the 10 artist worlds into the 17 approved durable theme packages simply to obtain one smaller theme schema. They have different provenance and promotion rules.

## Music-route state

The current production authority test preserves these music-route approval states:

```text
CANDIDATE
SEARCH_ROUTE
GENERATIVE_CANDIDATE
OFFICIAL_SOURCE
OFFICIAL_SOUNDTRACK
```

These states are meaningful data, not UI labels to normalize away.

A music route can be useful to the Music Hub without being approved as a shipping soundtrack. Source Hubs must preserve the route's curation status and must not silently convert search/candidate material into approved playback mappings.

## Data contract

An artist world is a structured authored system, not merely a palette, wallpaper, or style tag.

The durable database models interconnected concepts such as:

- artist identity;
- world variant;
- district;
- aesthetic DNA;
- weather;
- timeflow;
- interactions;
- discovery;
- music routing;
- provenance;
- references;
- curation/promotion state.

The production app may derive runtime-friendly records, but it must preserve the source relationships and provenance necessary to reconstruct why a world or route exists.

## Provenance boundary

Artist/source/profile/music/reference links are curation provenance. They must remain attached to relevant records and must not be silently collapsed into unsourced generated content.

Preserve at least:

- artist identity;
- source URL;
- source type;
- captured/reference asset identity;
- SHA-256 when available;
- world/district relationship;
- music route;
- verification date;
- interpretation/notes;
- promotion state.

The v4.0.1 authority still carries a per-artist rights/release boundary for reference/curation material. Production inclusion does not erase that evidence boundary.

## Current SQLite runtime research

SQLite's current official release is **3.53.4**, released **July 24, 2026**. The official release record identifies source ID:

```text
2026-07-24 19:02:57 bf7c7f30031888f4e796e429ab3978879485813aaca6f641c7b33e4e09459bcc
```

The 3.53 line includes a WAL-reset corruption fix and multiple query/planner and self-healing-index changes. The 3.53.4 patch itself is a maintenance release containing fixes for issues introduced or found across the 3.53 line.

Primary sources:

- https://sqlite.org/
- https://www.sqlite.org/releaselog/3_53_4.html
- https://sqlite.org/changes.html

### Important production distinction

Feature Foundry v24 uses:

```toml
rusqlite = { version = "0.40.2", features = ["bundled", "modern_sqlite"] }
```

The application therefore carries its SQLite through the bundled rusqlite build rather than simply using whichever system SQLite happens to be installed.

Do not claim that the production app is running SQLite 3.53.4 merely because 3.53.4 is the latest upstream release. Read the actual `catalog_summary.sqliteVersion` from the built application or inspect the resolved bundled dependency first.

## Build and verification workflow

From the canonical Feature Foundry v24 repository:

```powershell
npm install
npm run verify
```

The current `verify` command runs:

```text
npm run test
npm run typecheck
npm run build
cargo check --manifest-path src-tauri/Cargo.toml
npm run test:ui
```

For the native application:

```powershell
npm run desktop:dev
npm run desktop:build
```

For release packaging:

```powershell
npm run package
```

The database must remain valid in both browser-facing authority tests and the native Tauri/SQLite path.

## End-to-end validation ledger

A database update should be treated as complete only after the following chain is proven for the same data identity:

```text
workbook
-> canonical JSON
-> canonical SQLite/reference validation
-> Feature Foundry embedded JSON
-> authority tests
-> native SQLite seed
-> catalog_summary/integrity check
-> Theme Atlas / source-hub runtime behavior
-> restart persistence where state is user-owned
```

Record the hash or stable identity at each transition where available.

## Current validation requirements

For a v4.0.1 or successor validation pass, record at least:

- workbook SHA-256;
- canonical JSON SHA-256;
- canonical SQLite SHA-256;
- embedded production JSON blob/hash;
- resolved bundled SQLite runtime version/source identity;
- `PRAGMA integrity_check` result;
- foreign-key violations;
- stable-ID uniqueness;
- row counts for every entity class;
- FTS result parity when validating the canonical curation database;
- representative artist -> world -> district -> weather -> interaction joins;
- music-route status preservation;
- Azure Save Coast stable-ID/name parity;
- Theme Atlas count and artist-world visibility;
- native restart/persistence behavior for user mappings without mutating the source curation rows.

## Anti-regression rules

- Never regenerate stable IDs for cosmetic naming corrections.
- Never drop provenance/reference rows merely to reduce file size.
- Never deduplicate a meaningful reference occurrence solely because another occurrence has the same bytes.
- Never flatten all artist worlds into one generic theme schema that loses artist-specific districts, weather, interactions, music routes, or provenance.
- Never treat a newer workbook timestamp alone as stronger evidence than the verified v4.0.1 lineage.
- Preserve JSON, SQLite, workbook, FTS, archive, and production-embedding validation together when the database changes.
- Keep curation approval state separate from application availability.
- Do not promote `CANDIDATE` or `SEARCH_ROUTE` music entries to approved soundtrack state without explicit curator approval.
- Do not rewrite the curation database merely because Feature Foundry releases a new application version.
- Do not infer the native SQLite engine version from the latest upstream SQLite website; verify the bundled runtime.
- Keep production user mappings such as room soundtrack assignments separate from immutable/recoverable curation source rows.

## Troubleshooting

### A favorite-artist world is missing from Theme Atlas

Check, in order:

1. `src/data/artist-worlds-v4.0.1.json` contains the stable world ID;
2. `tests/authority.test.ts` still passes the 10-world count;
3. the production bundle includes the current JSON;
4. the UI still reports 27 total catalog worlds;
5. no presentation filter is silently treating artist worlds as unapproved durable themes.

Do not fix the symptom by copying the world into the 17-theme package list.

### Azure Save Coast reverted to the older name

Search by stable ID `district.saveroom.paradise-zero-lagoon`, not display text. Reconcile workbook, canonical JSON, canonical SQLite/FTS, production embedded JSON, and native seed output. The stable ID must remain unchanged.

### Native catalog counts differ from authority tests

Inspect the Tauri SQLite seed transaction and `catalog_summary`. Confirm the embedded JSON hash in metadata matches the expected canonical JSON hash. Do not patch counts directly in SQLite.

### A music route appears usable but is not approved

Read `approval_status`. Availability in a search result, source hub, or Music Hub route is not equivalent to soundtrack approval.

### A source/reference URL changed

Preserve the prior provenance record and add verified supersession metadata rather than replacing history without traceability.

### SQLite behavior changed after a dependency update

Record the actual runtime `sqlite_version()` value from `catalog_summary`, run integrity/foreign-key/query parity tests, compare query plans for important paths, and keep the prior known-good build available until the new runtime is proven.

## Exact next action

Run one **v4.0.1 production round-trip qualification** against Feature Foundry v24:

1. verify the workbook, canonical JSON, and canonical SQLite hashes;
2. verify the embedded `src/data/artist-worlds-v4.0.1.json` hash and authority counts;
3. launch the native app and record `catalog_summary.sqliteVersion`, integrity result, and all artist-world counts;
4. verify all 10 artist worlds and the Azure Save Coast correction in the real Theme Atlas;
5. verify music-route approval states survive native seeding and Music Hub use;
6. restart and confirm user-created room mappings persist without modifying curation source rows;
7. compare the resolved bundled SQLite runtime with current SQLite 3.53.4 and adopt any engine change only after correctness parity and a material benefit or needed bug fix are proven.

## Evidence

### Current curation authority

- Current workbook: https://docs.google.com/spreadsheets/d/1BLxXdbNN0hJggKDJ16fBFv86OOep1Q40/edit
- v4.0.1 workbook: https://docs.google.com/spreadsheets/d/1X1NySI08HjVAlcjJEfXQzNrjc7ELEsB4/edit
- v4.0.1 README: https://drive.google.com/file/d/1UulWpSH2wvIq4Zj08SPdlqKtxpalPuAM/view

### Current production source

- Repository: https://github.com/Herbertofury/Feature-Foundry
- Verified production head: `e1ba080b5c7590f1c844a6ed13b3a471709920b9`
- Embedded artist authority: `src/data/artist-worlds-v4.0.1.json`
- Native catalog: `src-tauri/src/database.rs`
- Authority test: `tests/authority.test.ts`
- Native dependencies: `src-tauri/Cargo.toml`

## Wiki maintenance

Update this page when artist/world counts, stable IDs, provenance records, curation schema/version, production embedding, source hashes, promotion rules, native SQLite schema/runtime identity, integrity evidence, search/index behavior, or Feature Foundry promotion status changes. Preserve prior validated lineage and historical corrections rather than rewriting history.