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

## Current evidence state

Project Constellation currently preserves exactly **63 tracked projects**, with Sports Group Hub intentionally absent. The byte-verified v0.5.0 Quick View contains the active 63-record embedded project dataset and remains a valid recovery surface.

A historical `USER-PROJECTS-DATABASE.md` is also present in Google Drive. That document is useful for lineage and detailed recovery history, especially for the original 25 project families, but Project Constellation explicitly treats it as historical evidence rather than authority over the current 63-record catalog.

### Important continuity gap found on 2026-08-17

The current Project Constellation handoff refers to a standalone `Project-Constellation-Project-Catalog.json`, and prior automation state records that such a catalog was materialized. During this pass, the standalone file was not found in the current `Herbertofury/ProjectDump/project-constellation/` tree and a Drive search for that exact file name returned no result.

That absence is a **catalog publication/availability gap**, not permission to recreate the project list from the older 25-project database or to start over. The embedded 63-record Project Constellation dataset and current source-controlled project evidence remain the recovery inputs.

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

Two current standards are especially useful for a future restored standalone machine catalog:

### JSON Schema 2020-12

JSON Schema's current published specification is Draft 2020-12. A catalog schema can use it to enforce stable required fields, extension fields, enum/status shapes, and nested artifact/evidence records without relying only on application code.

Primary source: https://json-schema.org/specification

### RFC 8785 JSON Canonicalization Scheme

RFC 8785 defines deterministic JSON canonicalization. Applying JCS before SHA-256 hashing would make catalog snapshot and per-record integrity independent of irrelevant whitespace or object-key ordering.

Primary source: https://www.rfc-editor.org/rfc/rfc8785.html

These mechanisms should improve evidence integrity, not change project semantics.

## Proposed restoration experiment

Restore the standalone machine catalog only from the newest active 63-record evidence set, then apply current project-owned overlays additively.

Suggested sequence:

1. Read the byte-verified v0.5.0 embedded 63-record Quick View dataset.
2. Read current source-controlled project wikis/evidence queues and explicit user corrections.
3. Preserve every existing `recoveryHistory` field and project ID.
4. Apply only evidence-backed field supersessions.
5. Validate against a versioned JSON Schema 2020-12 schema.
6. Canonicalize the resulting JSON with RFC 8785 and record SHA-256 for the snapshot and optionally each record.
7. Verify exactly 63 projects and Sports Group Hub absence.
8. Publish the exact bytes to both GitHub and the dedicated Project Constellation Drive folder.
9. Re-fetch/re-download the remote copies and verify the hashes before calling the standalone catalog durable.

## Optional indexed mirror

SQLite can be useful as a **derived index** for fast cross-project search, relationship lookup, artifact-hash lookup, and research freshness queries. It must not become the sole authority or silently rewrite the canonical JSON record set.

If added, the mirror should be reproducible from the canonical JSON and disposable without data loss.

## Anti-degradation rules

- Never replace the 63-record catalog with the older 25-project database.
- Never drop recovery history to simplify a schema migration.
- Never merge same-name artifacts solely because names or timestamps match.
- Never promote an artifact without content/hash/version evidence.
- Never treat a generated catalog as durable until its remote bytes are verified.
- Never let a search/index layer mutate canonical project records implicitly.

## Acceptance test

A restored standalone catalog is acceptable only when:

- exactly 63 current project IDs are present;
- Sports Group Hub is absent;
- every current record retains goal, requirements, stop point, next action, and recovery history;
- explicit user edits win;
- same-name different-content lineage is preserved;
- schema validation passes;
- deterministic canonical hashes are reproducible;
- GitHub and Drive remote bytes match the promoted hashes;
- Project Constellation can consume the catalog without dropping local user state.

## Exact current next action

Recover and republish the missing standalone 63-record machine catalog from the active Project Constellation dataset and newer project-owned evidence, with schema validation and deterministic byte/hash verification. Do **not** regenerate it from the historical 25-project database.
