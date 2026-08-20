# Project Catalog / Cross-Chat Database Wiki

**Project Constellation ID:** `PCX-057`  
**Status:** ACTIVE / TRACKED, dual-publication catalog integrity verified  
**Current authority:** the converged 63-record catalog in GitHub and Google Drive plus newer project-owned repository/runtime evidence where verified  
**Goal:** Maintain the durable cross-project locator, version lineage, artifact hashes, and exact next actions without promoting stale copies by filename or timestamp alone.

## Purpose

The Project Catalog is the machine-facing cross-project continuity layer behind Project Constellation. It exists to answer four questions reliably:

1. Which project is this artifact, repository, or checkpoint associated with?
2. Which version or artifact is actually the newest verified state?
3. What evidence proves that state?
4. Where did work stop and what exact action happens next?

The catalog must preserve same-name different-content artifacts, predecessor/successor relationships, source provenance, validation state, user corrections, exact stop points, and next actions. It must never flatten project history into a filename or modified-time guess.

## Current verified catalog state

The standalone Project Constellation catalog is again in a healthy dual-publication state.

The current verified catalog identity is:

```text
Path: project-constellation/Project-Constellation-Project-Catalog.json
Drive file ID: 1-ks_2aRKgKQ-O7Y9LHte7w_Xk5t16egq
Bytes: 116737
SHA-256: 79c43dde274c7e4420a27d35ff58fdea4b7bdfc4c5cc412ad527c995eb8977ab
Git blob SHA: 0cbd23ef565c5ea61c26c978142d2b1f434c6bbf
JSON parse: pass
Project count: 63
Project array length: 63
Unique project IDs: 63 / 63
```

The Google Drive catalog was re-downloaded during the current verification pass. Its raw SHA-256 is `79c43dde274c7e4420a27d35ff58fdea4b7bdfc4c5cc412ad527c995eb8977ab` and its exact byte size is 116,737 bytes.

The same re-downloaded Drive bytes produce Git blob SHA `0cbd23ef565c5ea61c26c978142d2b1f434c6bbf` when passed through `git hash-object`. That equals the blob currently stored at the GitHub catalog path, so the GitHub and Drive objects are not merely semantically similar: they are the same promoted catalog bytes.

The catalog parses successfully and preserves all 63 tracked project objects. The last five IDs are `PCX-059`, `PCX-060`, `PCX-061`, `PCX-062`, and `PCX-063`, which confirms the file reaches the complete tail of the tracked-project set rather than stopping inside an earlier record.

Required continuity-field checks currently pass for every project:

- non-empty `goal`;
- non-empty `requirements`;
- `recoveryHistory`;
- `nextAction`;
- `stopPoint`.

## Machine-readable integrity receipt

The durable integrity receipt is:

`project-constellation/Project-Constellation-Catalog-Integrity.json`

Schema:

```text
project-constellation.catalog-integrity/1
```

The current receipt was refreshed at `2026-08-20T03:50:00Z` and records:

```text
Drive bytes: 116737
Drive SHA-256: 79c43dde274c7e4420a27d35ff58fdea4b7bdfc4c5cc412ad527c995eb8977ab
Drive JSON parse: pass

GitHub blob: 0cbd23ef565c5ea61c26c978142d2b1f434c6bbf
GitHub bytes: 116737
GitHub SHA-256: 79c43dde274c7e4420a27d35ff58fdea4b7bdfc4c5cc412ad527c995eb8977ab
GitHub JSON parse: pass
Git blob matches re-downloaded Drive bytes: true
Exact byte match: true

Project count: 63
Project array length: 63
Unique IDs: true
Goal coverage: pass
Requirements coverage: pass
Recovery-history coverage: pass
Next-action coverage: pass
Stop-point coverage: pass
Dual publication: PASS
```

The receipt was committed as a new evidence checkpoint at ProjectDump commit `7e9791beeb4546a2230c8029724b3fe08e899ca0`.

## Historical publication-integrity incident

PCX-057 previously had a real split-publication defect and that history remains important.

The complete Drive catalog stayed valid at 116,737 bytes and SHA-256 `79c43dde274c7e4420a27d35ff58fdea4b7bdfc4c5cc412ad527c995eb8977ab`, while the GitHub mirror temporarily regressed to:

```text
Git blob: 297284ad1417e5b8b9dd8f6d16fbb3a28906e6ed
Bytes: 48132
SHA-256: e222fc0aadf0c653c1f87af2d790994235d9f30fb350b77a51274a7ad6ab5a45
Condition: malformed/truncated inside PRJ-019
```

The truncated file retained a top-level `projectCount: 63` header but did not physically contain the complete 63-record document. That incident proved why a header count alone is insufficient integrity evidence.

The incident is now **resolved**, not erased. The previous malformed blob remains preserved in Git history and in the integrity receipt's `historicalDivergence` section. Current GitHub and Drive catalog bytes converge on the complete 116,737-byte object.

## Authority and conflict resolution

Use this order when catalog records conflict:

1. Current explicit user correction.
2. Current canonical project repository/runtime evidence.
3. Current project-owned memory / Project Compass evidence.
4. The complete current Project Constellation catalog.
5. Older handoffs, exports, File Library artifacts, and historical cross-chat database copies.

A newer timestamp alone is never enough to win a conflict.

The historical `USER-PROJECTS-DATABASE.md` remains valuable for lineage and detailed recovery history, especially for the original project families, but it is historical evidence rather than authority over the current 63-record catalog.

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

## Version and artifact trust order

When several copies claim to be current, resolve them in this order:

1. explicit user correction;
2. canonical repository and real runtime evidence;
3. embedded version/changelog tied to exact bytes;
4. content hash and verified predecessor/successor lineage;
5. validation report tied to the same artifact identity;
6. durable catalog/checkpoint metadata;
7. upload or filesystem timestamp;
8. filename alone.

A numerically higher filename or newer modification time does not automatically supersede a known-good artifact.

## Safe catalog update workflow

### 1. Resolve the current promoted source

Before modifying the catalog, identify the strongest verified current catalog object. Do not regenerate from the Quick View HTML, Wiki pages, filenames, or historical 25-project database when a complete stronger catalog already exists.

### 2. Preserve the previous identity

Before replacement, record:

```text
remote/source identity
byte size
SHA-256
Git blob or Drive file ID
project count
checkpoint/revision
```

This keeps rollback and same-name-different-content history recoverable.

### 3. Apply only verified record changes

Project-owned evidence may refine a project name, repository, version, latest state, requirements, blocker, next action, or stop point. Preserve unaffected fields and recovery history. Do not regenerate all records just because one project changed.

### 4. Validate the candidate locally

Require:

- JSON parse pass;
- `projectCount == 63`;
- exactly 63 project objects;
- exactly 63 unique project IDs;
- non-empty goal/requirements/recovery-history/next-action/stop-point coverage;
- no retired/removed target accidentally reintroduced;
- no unexpected truncation or encoding damage.

### 5. Publish to both durable destinations

The current catalog contract requires publication to:

- `Herbertofury/ProjectDump` at `project-constellation/Project-Constellation-Project-Catalog.json`;
- the canonical Project Constellation Google Drive location.

An acknowledgement from one destination is insufficient.

### 6. Re-read both remote objects independently

After publication:

- re-fetch GitHub and identify the current blob;
- re-download Drive;
- compare raw byte size;
- compare SHA-256;
- parse both copies;
- rerun the 63-record semantic invariants.

For GitHub/Drive exact-mirror verification, computing `git hash-object` on the re-downloaded Drive bytes is a useful independent cross-check against the GitHub content blob SHA.

### 7. Refresh the integrity receipt last

The receipt is the result of verification, not a prediction. Update it only after both remote copies are confirmed.

The receipt should record:

- checked time;
- GitHub commit/blob;
- Drive file ID;
- exact byte size and SHA-256 for both;
- parse result for both;
- exact-byte equality;
- project count and unique-ID result;
- required-field coverage;
- any historical divergence being closed or newly opened.

## Integrity layers

### Raw byte identity

Exact byte size plus SHA-256 is the primary publication identity when GitHub and Drive are intended to mirror one promoted catalog file.

### Git blob identity

Git's blob SHA is content-derived. Comparing the repository blob with `git hash-object` of the independently re-downloaded Drive file adds a useful provider-independent equality check.

### JSON parsing

A byte-complete object that does not parse is not a healthy catalog.

### Semantic invariants

The catalog must still contain 63 records, unique IDs, and required continuity fields after every update. Exact bytes alone do not prove the document remains meaningful.

### Optional schema validation

A formal JSON Schema can add field-type and enum validation. It is additive. It must not delete valid continuity detail simply to simplify the schema.

### Optional canonical semantic digest

A canonicalized JSON digest can help compare meaning across harmless formatting changes. It is additive evidence only and does not replace raw-byte equality where exact publication identity is required.

## Publication-debt conditions

Treat any of these as catalog publication debt:

- the GitHub catalog path is missing;
- the Drive catalog is missing;
- either copy is truncated or malformed;
- GitHub and Drive differ in byte size or SHA-256 when they are expected to mirror one promoted object;
- project count is not 63;
- the project array does not physically contain 63 records;
- project IDs are not unique;
- required continuity fields disappear;
- a historical 25-project database is promoted over stronger current evidence;
- an integrity receipt describes older bytes than the currently promoted catalog;
- a receipt claims success while one destination is only partially verified.

## Recovery procedure for future divergence

If the catalog diverges again:

1. freeze writes until the strongest complete authority is identified;
2. re-download every plausible candidate and compare bytes, hashes, parse state, record count, and project IDs;
3. preserve every divergent blob/file identity before replacing anything;
4. choose the complete verified candidate using the authority order above;
5. replace only the stale/broken destination;
6. re-read both remote destinations independently;
7. require exact-byte equality plus JSON and semantic-invariant passes;
8. refresh the integrity receipt only after convergence.

Do not merge a truncated tail into a complete catalog line-by-line and do not invent missing records.

## Optional indexed mirror

SQLite can be useful as a derived index for fast cross-project search, relationship lookup, artifact-hash lookup, and research-freshness queries. It must remain disposable and reproducible from canonical JSON. It must not become the sole authority or silently rewrite canonical project records.

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

Keep the converged 116,737-byte catalog and its integrity receipt synchronized whenever a future verified project-record change is promoted. On every catalog publication, re-read both GitHub and Drive, require exact size/SHA-256 equality plus independent JSON and 63-record validation, then refresh the integrity receipt last. If any destination diverges, reopen publication debt immediately and repair the stale side without reconstructing or flattening the catalog history.
