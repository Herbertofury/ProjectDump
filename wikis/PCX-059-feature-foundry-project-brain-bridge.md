# Feature Foundry Project Brain Bridge Wiki

**Project Constellation ID:** `PCX-059`
**Status:** ACTIVE / TRACKED
**Goal:** Keep Feature Foundry second-brain import/export portable, additive, provenance-aware, and truthful about integration status.

## Purpose

The Project Brain Bridge is the continuity boundary between Project Constellation/project-owned memory and Feature Foundry. Its job is to move **project state and intent**, not to make Project Constellation or an export bundle pretend to be Feature Foundry's native runtime.

The bridge should preserve enough information for Feature Foundry or another compatible host to resume a project without losing identity, progress, blockers, decisions, provenance, or exact next actions.

## Current evidence state

Historical cross-chat project evidence references a `Feature-Foundry-Project-Brain.zip` handoff artifact and a portable project-brain workflow. Project Constellation also preserves a host-neutral `feature-foundry.project-brain/1` schema concept in its continuity rules.

During this 2026-08-17 pass, searches of the connected ProjectDump repository and Google Drive did **not** locate a current standalone `Feature-Foundry-Project-Brain.zip` object or a current `feature-foundry.project-brain/1` file that could be promoted as the active bridge artifact.

That means the **bridge contract is preserved, but current native integration and current portable package bytes are not proven here**. Do not recreate a missing artifact from a filename reference and call it canonical.

## Minimum portable state

A bridge snapshot should be additive and host-neutral. At minimum it should preserve:

- stable project ID and aliases;
- project name and canonical source pointers;
- current goal / northpoints;
- requirements and guardrails;
- exact last verified stop point;
- one exact next action and why it is next;
- blockers and smallest unblock step;
- notes/tasks/session breadcrumbs when present;
- latest verified artifact/version separately from WIP lineage;
- artifact paths, hashes, provenance, and verification state;
- research decisions and checked dates;
- source snapshot/checkpoint identity;
- schema version and bridge version;
- import history and supersession lineage.

A receiving host may add its own state, but it must not erase unknown fields merely because it does not understand them.

## Merge rules

Import should be additive and conflict-aware:

1. Explicit user edits win.
2. Newer canonical repository/runtime evidence beats an older bridge export.
3. Project-owned durable memory beats presentation-layer summaries.
4. Unknown extension fields are preserved.
5. Same-name different-content artifacts remain distinct until reconciled.
6. Import never silently changes the tracked-project list.
7. Imported completion claims remain evidence-scoped; they do not become runtime proof merely because Feature Foundry rendered them.

## Integrity research

### JSON Schema 2020-12

A portable bridge envelope can use JSON Schema 2020-12 to define required identity, provenance, checkpoint, artifact, and extension fields while still allowing forward-compatible namespaces.

Primary source: https://json-schema.org/specification

### RFC 8785 JSON Canonicalization Scheme

RFC 8785 provides deterministic canonical JSON suitable for reproducible snapshot fingerprints. A bridge export can record a canonical SHA-256 without making formatting differences look like project changes.

Primary source: https://www.rfc-editor.org/rfc/rfc8785.html

### MCP 2026-07-28 as an optional transport boundary

The 2026-07-28 Model Context Protocol specification introduces a stateless core, stronger discovery, deterministic/cacheable list semantics, routing headers, formal extensions, and authorization hardening. If Feature Foundry eventually exposes project-brain operations over MCP, those capabilities can inform a transport adapter.

MCP must **not** redefine the canonical project-brain schema, and MCP discovery/handshake success must not be reported as proof that Feature Foundry actually imported, persisted, rendered, and resumed the project state.

Primary source: https://modelcontextprotocol.io/specification/2026-07-28

## Proposed portable-envelope experiment

Build one read/write fixture around an existing project without changing the production Feature Foundry runtime.

The fixture should:

1. export project identity, stop point, next action, blockers, notes, artifact hashes, and intent references;
2. validate against a versioned JSON Schema;
3. canonicalize and SHA-256 hash the snapshot;
4. import into an isolated bridge test harness;
5. add one host-owned extension field;
6. export again;
7. prove all original fields and unknown extension fields survive;
8. simulate an older conflicting export and prove it cannot overwrite a newer user/canonical record;
9. preserve a supersession/import ledger.

Only after a real Feature Foundry runtime is resolved should the same fixture be exercised through the actual application's import/export controls.

## Anti-degradation rules

- Never claim native Feature Foundry integration from a portable ZIP or schema alone.
- Never discard unknown fields during import/export.
- Never overwrite newer user edits with an older snapshot.
- Never flatten verified/WIP/spec states into one version.
- Never turn transport authentication into project-state verification.
- Never store secrets or provider credentials in project-brain exports.
- Never require Feature Foundry to be available in order for the Project Constellation record to remain recoverable.

## Acceptance test for native integration

Native Feature Foundry integration is proven only when the canonical application can:

- import the exact bridge snapshot;
- show the correct project identity and progress;
- preserve exact stop point, next action, blockers, notes, and provenance;
- save the imported state durably;
- restart and reopen with the same state;
- export a snapshot that round-trips all required and unknown fields;
- reject or safely merge stale/conflicting snapshots;
- expose truthful errors instead of silently dropping unsupported data.

## Exact current next action

Locate the newest real Project Brain export or canonical Feature Foundry runtime. Until then, preserve the bridge as a host-neutral schema/merge contract and prototype a schema-validated, RFC-8785-hashable round-trip fixture without claiming native integration.
