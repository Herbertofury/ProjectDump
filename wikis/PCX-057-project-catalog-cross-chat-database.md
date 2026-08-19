# Project Catalog / Cross-Chat Database Wiki

**Project Constellation ID:** `PCX-057`  
**Status:** ACTIVE / TRACKED, current catalog publication debt  
**Current authority:** the valid 63-record Google Drive catalog plus current project-owned repository/runtime evidence  
**Goal:** Maintain the durable cross-project locator, version lineage, artifact hashes, and exact next actions without promoting stale copies by filename or timestamp alone.

## Purpose

The Project Catalog is the machine-facing cross-project continuity layer behind Project Constellation. It exists to answer four questions reliably:

1. Which project is this artifact, repository, or checkpoint associated with?
2. Which version or artifact is actually the newest verified state?
3. What evidence proves that state?
4. Where did work stop and what exact action happens next?

The catalog must preserve same-name different-content artifacts, predecessor/successor relationships, source provenance, validation state, user corrections, exact stop points, and next actions. It must never flatten project history into a filename or modified-time guess.

## Current verified catalog state

Project Constellation still has a valid **63-record catalog**, but the two durable catalog copies are **not currently byte-identical**. The current machine-readable integrity receipt records a split state that supersedes the older wiki claim that GitHub and Drive contain the exact same bytes.

### Google Drive: current complete catalog authority

The current Drive object is:

- file: `Project-Constellation-Project-Catalog.json`
- Drive file ID: `1-ks_2aRKgKQ-O7Y9LHte7w_Xk5t16egq`
- size: **116,737 bytes**
- SHA-256: `79c43dde274c7e4420a27d35ff58fdea4b7bdfc4c5cc412ad527c995eb8977ab`
- JSON parse: **pass**
- `projectCount`: **63**
- project array length: **63**
- unique project IDs: **63 / 63**
- every project has a non-empty `goal`: **pass**
- every project has a non-empty `requirements` array: **pass**
- every project has `recoveryHistory`: **pass**

The current Drive catalog ends with `PCX-059`, `PCX-060`, `PCX-061`, `PCX-062`, and `PCX-063`, which is consistent with a complete 63-record set rather than a partial export.

### GitHub: current malformed/truncated mirror

The current repository path is:

- path: `project-constellation/Project-Constellation-Project-Catalog.json`
- current Git blob SHA: `297284ad1417e5b8b9dd8f6d16fbb3a28906e6ed`
- size recorded by the current integrity receipt: **48,132 bytes**
- SHA-256 recorded by the current integrity receipt: `e222fc0aadf0c653c1f87af2d790994235d9f30fb350b77a51274a7ad6ab5a45`
- current receipt parse status: `pre-existing malformed catalog preserved; retired references removed`

A direct repository read confirms the GitHub file ends in the middle of the `PRJ-019` record, inside the USVFS research text, and does not contain the remainder of the 63-project document or closing JSON structure. Therefore the current GitHub copy must **not** be treated as the complete catalog authority even though its top-level header still says `projectCount: 63`.

This is a real publication-integrity defect. A header count is not proof that the complete record set is present.

## Catalog publication history and the current split

The standalone catalog was previously restored to GitHub from a verified Drive copy at commit:

`eb99a193c08b9f2ca370dbcf85c75c2f997eafa6`

An initial machine-readable integrity receipt was added at:

`ab071e23eecb9c658ad6b50f62c9c2b73b3a4c68`

The catalog documentation was then expanded at:

`fe70193796934db22f31dffd4ccc5fbacc139974`

Later cleanup work at commit:

`057aa34c9b691b7898a0596a7fde0093da81a966`

removed retired-project references across ProjectDump. The current integrity receipt deliberately records that the malformed GitHub catalog was **pre-existing and preserved** by that cleanup rather than claiming the cleanup produced a new valid catalog.

The current integrity receipt was checked at `2026-08-18T16:20:00Z` and now records different Drive and GitHub byte identities. That receipt is stronger evidence than the older wiki text, so the wiki must reflect the divergence rather than repeat the earlier exact-match claim.

## Machine-readable catalog integrity receipt

The current receipt is:

`project-constellation/Project-Constellation-Catalog-Integrity.json`

Schema:

```text
project-constellation.catalog-integrity/1
```

Current recorded identities:

```text
Drive file ID: 1-ks_2aRKgKQ-O7Y9LHte7w_Xk5t16egq
Drive bytes: 116737
Drive SHA-256: 79c43dde274c7e4420a27d35ff58fdea4b7bdfc4c5cc412ad527c995eb8977ab

GitHub blob: 297284ad1417e5b8b9dd8f6d16fbb3a28906e6ed
GitHub bytes: 48132
GitHub SHA-256: e222fc0aadf0c653c1f87af2d790994235d9f30fb350b77a51274a7ad6ab5a45
GitHub JSON parse: pre-existing malformed catalog preserved; retired references removed
```

Current semantic invariants recorded by the receipt are:

- `projectCount: 63`
- unique project IDs
- every project has a goal
- every project has requirements
- every project has recovery history

Those semantic invariants describe the recovered 63-record continuity state and the complete Drive catalog. They do **not** make the current truncated GitHub file a valid 63-record JSON document.

### Important interpretation of publication status fields

The receipt currently says:

```text
github: RESTORED_AND_FETCH_VERIFIED
googleDrive: SOURCE_REDOWNLOADED_AND_SHA256_VERIFIED
```

These labels mean the individual remote objects were fetched and identified. They do **not** mean the two remote objects currently match each other. The recorded byte counts and SHA-256 values prove that they do not.

For PCX-057, a healthy dual-publication state requires one promoted catalog byte identity on both destinations, not two independently fetchable but different files.

## Safe catalog recovery procedure

The current defect is recoverable without reconstructing the project list or discarding continuity history.

### 1. Freeze authority correctly

Until the GitHub mirror is repaired, treat the verified Drive catalog as the complete standalone catalog authority. Project-specific repositories and project-owned memory can still supersede individual stale record fields when verified, but the malformed GitHub catalog must not supersede the complete Drive record set.

### 2. Re-download and verify the Drive source

Before any repair, verify all of the following against Drive file `1-ks_2aRKgKQ-O7Y9LHte7w_Xk5t16egq`:

- exact byte size `116737`;
- SHA-256 `79c43dde274c7e4420a27d35ff58fdea4b7bdfc4c5cc412ad527c995eb8977ab`;
- JSON parses;
- `projectCount == 63`;
- exactly 63 project objects;
- 63 unique project IDs;
- every record retains goal, requirements, recovery history, next action, and stop point.

If any of those fail, stop promotion and resolve the stronger source before writing either destination.

### 3. Capture the broken GitHub identity before replacement

Record the current GitHub blob, byte count, and hash before repair so the malformed state remains traceable:

```text
blob: 297284ad1417e5b8b9dd8f6d16fbb3a28906e6ed
bytes: 48132
sha256: e222fc0aadf0c653c1f87af2d790994235d9f30fb350b77a51274a7ad6ab5a45
```

Do not try to merge the truncated tail into the valid Drive JSON line by line. Preserve the malformed blob in Git history and promote one verified complete catalog.

### 4. Replace the GitHub catalog only with verified complete bytes

The safe repair is a scoped replacement of `project-constellation/Project-Constellation-Project-Catalog.json` using the verified complete catalog bytes, after confirming there is no newer valid catalog checkpoint that supersedes the Drive object.

Do not regenerate from `USER-PROJECTS-DATABASE.md`, the Quick View HTML, filenames, timestamps, or partial GitHub records. Those are supporting continuity evidence, not substitutes for the verified complete catalog.

### 5. Verify the repaired GitHub copy independently

After replacement, fetch the repository file again and require:

- byte size equal to Drive;
- raw SHA-256 equal to Drive;
- JSON parse pass;
- 63 project objects;
- 63 unique IDs;
- required continuity fields intact;
- no accidental truncation, encoding damage, or dropped history.

### 6. Refresh the integrity receipt only after convergence

`Project-Constellation-Catalog-Integrity.json` should then be rewritten with one shared promoted catalog identity and a new `checkedAt` value. The receipt should distinguish:

- exact-byte equality across GitHub and Drive;
- JSON parse result for each destination;
- semantic invariant results;
- the commit/blob identity that published the GitHub copy;
- the Drive file ID and re-download verification result.

A receipt must not label publication healthy merely because both destinations are separately readable.

## Authority and conflict resolution

Use this order when catalog records conflict:

1. Current explicit user correction.
2. Current canonical project repository/runtime evidence.
3. Current project-owned memory / Project Compass evidence.
4. The complete current Project Constellation catalog authority.
5. Older handoffs, exports, File Library artifacts, and historical cross-chat database copies.

A newer timestamp alone is never enough to win a conflict.

The historical `USER-PROJECTS-DATABASE.md` remains valuable for lineage and detailed recovery history, especially for the original 25 project families, but it is historical evidence rather than authority over the current 63-record catalog.

## Required catalog record fields

A durable project record should preserve at least:

- stable project ID;
- canonical project name and aliases;
- canonical repository/worktree/branch when verified;
- status and confidence;
- goal / northpoint;
- requirements and guardrails;
- latest verified version or artifact;
- latest WIP/spec lineage separately;
- exact last verified stop point;
- one exact next action;
- blockers and smallest unblock step;
- artifact filenames, paths, sizes, hashes, and source locations;
- predecessor/successor or supersession relationships;
- build/test/runtime/restart verification state separately;
- research decisions with source and checked date;
- last checkpoint and evidence watermark.

Do not collapse `discovered`, `build passed`, `packaged`, `installed`, `real workflow passed`, and `restart persistence passed` into one `done` flag.

## Integrity layers

### Exact byte identity

Raw SHA-256 plus exact byte size is the primary publication identity when verifying that GitHub and Drive carry the same promoted catalog bytes.

### JSON parsing and semantic invariants

Exact bytes are not sufficient if the promoted object is malformed. Both remote copies should parse independently and satisfy the 63-project invariant set.

### Optional schema validation

A formal JSON Schema can be added as an extra contract for field types, required properties, enums, and nested structures. Schema validation is additive and must not discard existing continuity detail simply to make validation easier.

### Optional canonical semantic digest

A canonicalized JSON digest can be useful to detect semantic equality across harmless formatting differences. It is additive evidence only. It must not replace raw-byte equality when the publication requirement is exact remote-byte identity.

## Publication-integrity contract

Treat any of these conditions as publication debt:

- the GitHub catalog path is missing;
- either remote copy is truncated or malformed;
- GitHub and Drive byte size or SHA-256 differ when exact mirror publication is expected;
- project count is not 63;
- the project array does not contain 63 records;
- project IDs are not unique;
- required continuity fields disappear;
- a historical 25-project database is promoted over stronger current evidence;
- the integrity receipt describes an older catalog rather than the promoted catalog;
- the receipt reports both destinations as individually fetched but does not surface that their bytes diverge.

The minimal integrity receipt for a healthy checkpoint should record both remote destinations, exact byte size, raw SHA-256, parse result, Git blob or commit identity, project count, unique-ID result, required-field coverage, and the checkpoint at which the comparison was performed.

## Optional indexed mirror

SQLite can be useful as a **derived index** for fast cross-project search, relationship lookup, artifact-hash lookup, and research-freshness queries. It must not become the sole authority or silently rewrite canonical project records.

If added, the mirror should be reproducible from the canonical JSON and disposable without data loss.

## Anti-degradation rules

- Never replace the 63-record catalog with the older 25-project database.
- Never repair a truncated catalog by inventing missing records.
- Never drop recovery history to simplify a schema migration.
- Never merge same-name artifacts solely because names or timestamps match.
- Never promote an artifact without content/hash/version evidence.
- Never treat a generated catalog as durable until both remote destinations are verified.
- Never treat an old integrity receipt as proof of a newer catalog checkpoint.
- Never let a search/index layer mutate canonical project records implicitly.
- Never substitute a semantic canonicalization digest for the exact-byte digest required by publication verification.
- Never treat a `projectCount` header as proof that all project objects are physically present.

## Acceptance test

The standalone catalog is durable only when:

- exactly 63 current project objects are present;
- all 63 project IDs are unique;
- every current record retains goal, requirements, stop point, next action, and recovery history;
- explicit user edits win;
- same-name different-content lineage is preserved;
- both GitHub and Drive copies parse independently;
- GitHub and Drive remote identities match the promoted catalog bytes;
- the machine integrity receipt matches those promoted bytes and invariants;
- Project Constellation can consume the catalog without dropping local user state.

## Exact current next action

Restore `project-constellation/Project-Constellation-Project-Catalog.json` from the verified complete Drive catalog only after confirming that no newer valid catalog checkpoint supersedes it. Then re-fetch both destinations, require exact byte/hash equality plus independent JSON/63-record validation, and refresh `Project-Constellation-Catalog-Integrity.json` so it records one converged catalog identity. Schema validation and semantic canonicalization should wait until the publication debt is closed.