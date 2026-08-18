# Project Catalog / Cross-Chat Database Wiki

**Project Constellation ID:** `PCX-057`  
**Status:** ACTIVE / TRACKED  
**Current authority:** Project Constellation 63-record continuity state plus current project-owned evidence  
**Goal:** Maintain the durable cross-project locator, version lineage, artifact hashes, and exact next actions without promoting stale copies by timestamp alone.

## Purpose

The Project Catalog is the machine-facing cross-project continuity layer behind Project Constellation. It exists to answer four questions reliably:

1. Which project is this artifact, repository, or checkpoint associated with?
2. Which version or artifact is actually the newest verified state?
3. What evidence proves that state?
4. Where did work stop and what exact action happens next?

This catalog must preserve same-name different-content artifacts, predecessor/successor relationships, source provenance, validation state, and user corrections. It must never flatten project history into a single filename or modified-time guess.

## Current verified catalog state

Project Constellation currently preserves exactly **63 tracked projects**, with Sports Group Hub intentionally absent. The byte-verified v0.5.0 Quick View remains a valid recovery surface, and the standalone machine catalog has now been independently resolved rather than reconstructed from historical data.

The canonical Drive object is:

- file: `Project-Constellation-Project-Catalog.json`
- Drive file ID: `1-ks_2aRKgKQ-O7Y9LHte7w_Xk5t16egq`
- size: **116,771 bytes**
- SHA-256: `79c8dd524b866ab1fe2dc011820f010d7ab5c8f4b0f42d31ad3e6ca8db82e8be`

The exact same catalog bytes were restored to the canonical GitHub tree at:

- path: `project-constellation/Project-Constellation-Project-Catalog.json`
- restoration commit: `eb99a193c08b9f2ca370dbcf85c75c2f997eafa6`
- Git blob SHA: `d417e516449f7c2d4ec9a16accdedfebc5cb590f`

The restored JSON was validated as a 63-record catalog with 63 unique project IDs, `sportsGroupHubExcluded: true`, no Sports Group Hub record, and complete `goal`, `requirements`, and `recoveryHistory` coverage across every project.

A historical `USER-PROJECTS-DATABASE.md` is also present in Google Drive. That document remains useful for lineage and detailed recovery history, especially for the original 25 project families, but Project Constellation explicitly treats it as historical evidence rather than authority over the current 63-record catalog.

### Publication-gap correction

An earlier 2026-08-17 documentation pass incorrectly concluded that the standalone catalog was absent from both GitHub and Drive. The stronger current evidence proves a narrower failure: the exact canonical catalog remained present and byte-verifiable in Drive, while the GitHub mirror had disappeared from `project-constellation/`.

The repair deliberately reused the existing verified Drive bytes. It did **not** regenerate the catalog, reconstruct the project list, rewrite recovery history, or promote the older 25-project database. This preserves the current catalog lineage while repairing redundant publication.

## Machine-readable catalog integrity receipt

The previously documented next step to create a catalog-integrity receipt has now been completed.

`project-constellation/Project-Constellation-Catalog-Integrity.json` was added at commit `ab071e23eecb9c658ad6b50f62c9c2b73b3a4c68` with schema:

```text
project-constellation.catalog-integrity/1
```

The receipt records the exact promoted catalog identity:

```text
path: project-constellation/Project-Constellation-Project-Catalog.json
driveFileId: 1-ks_2aRKgKQ-O7Y9LHte7w_Xk5t16egq
bytes: 116771
sha256: 79c8dd524b866ab1fe2dc011820f010d7ab5c8f4b0f42d31ad3e6ca8db82e8be
githubBlobSha: d417e516449f7c2d4ec9a16accdedfebc5cb590f
githubRestoreCommit: eb99a193c08b9f2ca370dbcf85c75c2f997eafa6
```

It also records these verified invariants:

- `projectCount: 63`
- unique project IDs
- Sports Group Hub excluded
- Sports Group Hub record absent
- every project has a goal
- every project has requirements
- every project has recovery history

The publication status is explicitly recorded as:

```text
github: RESTORED_AND_FETCH_VERIFIED
googleDrive: SOURCE_REDOWNLOADED_AND_SHA256_VERIFIED
```

The receipt preserves the stronger publication rule already used by Project Constellation: a missing, stale, partial, or unverifiable GitHub or Drive copy is publication debt. Raw byte SHA-256 remains the exact publication identity. Any semantic/canonicalized digest is additive evidence only.

### What the receipt does and does not prove

The receipt is a durable snapshot of one verified catalog checkpoint. It proves the recorded catalog identity and invariants for that checkpoint.

It does **not** yet prove that every future catalog checkpoint automatically regenerates and verifies the receipt. A later catalog mutation can still create drift unless the normal checkpoint path compares the live GitHub and Drive copies, recomputes the receipt, and rejects or flags divergence.

That distinction matters because a stale integrity receipt is evidence about an older checkpoint, not evidence that the current catalog is still synchronized.

## Authority and conflict resolution

Use this order when catalog records conflict:

1. Current explicit user correction.
2. Current canonical repository/runtime evidence.
3. Current project-owned memory / Project Compass evidence.
4. Current Project Constellation record.
5. Older handoffs, exports, File Library artifacts, and historical cross-chat database copies.

A newer timestamp alone is never enough to win a conflict.

## Required catalog record fields

A durable record should preserve at least:

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

## Canonicalization and integrity research

### JSON Schema published dialect and active forward track

The JSON Schema specification site still identifies Draft 2020-12 as the latest published meta-schema. An active IETF draft updated in 2026 is developing the next specification line and introduces a `v1/2026` naming model in work-in-progress source material.

For Project Constellation, the correct near-term choice is therefore conservative in format but current in awareness: keep Draft 2020-12 as the validation dialect for a production catalog schema until the next specification line is actually published and supported by the selected validator. Track the 2026 draft as a migration candidate rather than silently changing the durable catalog format.

Primary sources:

- https://json-schema.org/specification
- https://datatracker.ietf.org/doc/draft-ietf-jsonschema-json-schema/

### RFC 8785 JSON Canonicalization Scheme

RFC 8785 defines deterministic JSON canonicalization. Applying JCS before a semantic SHA-256 can make a derived integrity fingerprint independent of irrelevant whitespace or object-key ordering.

Project Constellation must continue to keep the **raw byte SHA-256** as the publication identity when exact remote-byte equality matters. A JCS-derived semantic digest can be additive, not a replacement for the byte hash.

Primary source:

- https://www.rfc-editor.org/rfc/rfc8785.html

## Publication-integrity contract

The catalog is now a dual-published continuity artifact. A future run should treat either of these conditions as publication debt:

- the GitHub path is missing or does not resolve to the expected catalog lineage;
- the Drive object is missing or has unexpected bytes;
- project count is not 63;
- project IDs are not unique;
- Sports Group Hub reappears;
- required continuity fields disappear;
- a catalog is promoted from the historical 25-project database without stronger evidence;
- `Project-Constellation-Catalog-Integrity.json` no longer describes the promoted catalog bytes.

The minimal integrity receipt for a catalog checkpoint should record both remote destinations, exact byte size, raw SHA-256, Git blob or commit identity, project count, exclusion invariant, required-field coverage, and the checkpoint at which the comparison was performed.

## Optional indexed mirror

SQLite can be useful as a **derived index** for fast cross-project search, relationship lookup, artifact-hash lookup, and research freshness queries. It must not become the sole authority or silently rewrite the canonical JSON record set.

If added, the mirror should be reproducible from the canonical JSON and disposable without data loss.

## Anti-degradation rules

- Never replace the 63-record catalog with the older 25-project database.
- Never drop recovery history to simplify a schema migration.
- Never merge same-name artifacts solely because names or timestamps match.
- Never promote an artifact without content/hash/version evidence.
- Never treat a generated catalog as durable until both remote destinations are verified.
- Never treat an old integrity receipt as proof of a newer catalog checkpoint.
- Never let a search/index layer mutate canonical project records implicitly.
- Never substitute a semantic canonicalization digest for the exact-byte digest required by publication verification.

## Acceptance test

The standalone catalog is durable only when:

- exactly 63 current project IDs are present;
- Sports Group Hub is absent;
- every current record retains goal, requirements, stop point, next action, and recovery history;
- explicit user edits win;
- same-name different-content lineage is preserved;
- schema validation passes when a formal schema is present;
- GitHub and Drive remote identities match the promoted catalog bytes;
- the machine integrity receipt matches those promoted bytes and invariants;
- Project Constellation can consume the catalog without dropping local user state.

## Exact current next action

Wire `Project-Constellation-Catalog-Integrity.json` into the normal catalog/checkpoint workflow so every material catalog mutation automatically revalidates the 63-project invariants, rechecks both GitHub and Drive identities, and refreshes the receipt only after both copies agree. Then prototype Draft 2020-12 schema validation and optional RFC-8785 semantic hashing as additive verification layers without changing catalog semantics.
