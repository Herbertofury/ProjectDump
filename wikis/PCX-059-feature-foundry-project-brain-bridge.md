# Feature Foundry Project Brain Bridge Wiki

**Project Constellation ID:** `PCX-059`  
**Status:** ACTIVE / TRACKED  
**Goal:** Keep Feature Foundry second-brain import/export portable, additive, provenance-aware, and truthful about integration status.  
**Current production host authority:** `Herbertofury/Feature-Foundry` v24.0.0, `main` at `e1ba080b5c7590f1c844a6ed13b3a471709920b9`.

## Purpose

The Project Brain Bridge is the continuity boundary between Project Constellation/project-owned memory and Feature Foundry. Its job is to move **project identity, intent, progress, evidence, and resume state** without making Project Constellation, a portable export, or Feature Foundry's ordinary living-world snapshot pretend to be something it is not.

Project Constellation remains the cross-project catalog/control plane. Project-owned durable memory remains the project authority. Feature Foundry is now a real released receiving application, but a current native **project-brain import/export workflow is not yet implemented or verified** in Feature Foundry v24.0.0.

This distinction matters because v24 now has real browser and native persistence surfaces. They provide a concrete integration host for the bridge, but they currently persist **living-world/runtime state**, not the full Project Brain contract.

## Current verified production host

The old documentation boundary said the canonical Feature Foundry runtime still needed to be found. That is no longer true.

The current production repository is:

- repository: `Herbertofury/Feature-Foundry`;
- branch: `main`;
- verified head: `e1ba080b5c7590f1c844a6ed13b3a471709920b9`;
- product version: `24.0.0`;
- browser application: Vite + TypeScript;
- native application: Tauri 2 + Rust + SQLite;
- primary production compatibility runtime: `src/prototype-v24.ts`;
- premium/native integration layer: `src/premium.ts`;
- native commands: `src-tauri/src/lib.rs`;
- native database ownership: `src-tauri/src/database.rs`.

The v24 package exposes these verified commands:

```bash
npm run dev
npm run build
npm run typecheck
npm run test
npm run test:ui
npm run verify
npm run desktop:dev
npm run desktop:build
npm run package
```

`npm run verify` currently chains contract tests, authority tests, TypeScript typechecking, Vite production build, `cargo check` for the Tauri crate, and the UI test.

## Current persistence surfaces in Feature Foundry v24

Feature Foundry now has multiple real state/persistence mechanisms. They are important bridge integration points, but **none of them currently satisfies the full Project Brain contract**.

### Browser living-world snapshot

`src/premium.ts` provides `saveNativeSnapshot()`.

When Feature Foundry is running without Tauri, the save path writes the rendered production state to browser storage under:

```text
ff.browser-snapshot.v1
```

The user-facing save shortcut is `Ctrl+S` / `Cmd+S`.

The snapshot is built from the current product/runtime state and includes fields such as:

- coordinate-system description;
- current mode and view;
- current premium theme and base theme;
- lineage marker;
- world state and world layout;
- visual-quality state;
- object snapshots;
- object-ecology diagnostics;
- selected-object snapshot;
- mascot state;
- floating-vault state;
- runtime diagnostics;
- catalog diagnostics;
- Theme Director diagnostics;
- Music Hub diagnostics;
- Media Surface diagnostics;
- pointer and last-interaction state;
- native profile/catalog diagnostics when available;
- snapshot status.

This is useful production state, but it does **not** currently preserve Project Brain fields such as stable project ID, exact stop point, next action, blockers, project artifacts and hashes, research decisions, Compass/northpoint references, or import/supersession history.

### Native living-world snapshot

`src-tauri/src/lib.rs` implements real Tauri commands:

```text
save_world_snapshot
load_world_snapshot
```

`save_world_snapshot` first verifies that the supplied state is valid JSON, resolves the application's platform-specific app-data directory, and writes:

```text
living-world-snapshot.json
```

`load_world_snapshot` reads that same file when it exists.

This is a legitimate durable native persistence surface. It must **not** be silently repurposed as the Project Brain store because its name, payload, lifecycle, and compatibility expectations belong to the living-world application state.

### Native SQLite database

`src-tauri/src/database.rs` owns:

```text
feature-foundry.sqlite3
```

The database enables foreign keys, WAL journaling, and `synchronous=NORMAL` and currently stores production data including:

- metadata;
- theme packages;
- rooms;
- ecology objects;
- artist worlds;
- artist districts;
- artist weather;
- music routes;
- room soundtrack assignments;
- a generic native `history` table.

The exposed `record_native_history` command validates the JSON payload before appending an event type, payload, and timestamp to the history table.

That generic history facility is useful precedent for provenance-aware project-brain events, but the current schema has **no verified project-brain tables, import ledger, or Project Compass records**. Do not describe the `history` table as a native Project Brain implementation.

## Historical bridge evidence

Historical durable project evidence references:

- a `Feature-Foundry-Project-Brain.zip` handoff artifact;
- a portable Project Brain workflow;
- a host-neutral `feature-foundry.project-brain/1` schema concept.

Connected Drive and repository searches performed during earlier continuity passes did not recover current canonical bytes for that old ZIP or a current standalone `feature-foundry.project-brain/1` file.

The important change in the current state is that **the receiving production application is now resolved**. The missing work is no longer "find Feature Foundry"; it is "build and prove a bridge into the released v24 host without corrupting its existing state ownership."

Do not recreate an old ZIP merely from its filename and call the result canonical.

## Minimum portable Project Brain state

A bridge snapshot should be additive and host-neutral. At minimum it should preserve:

- stable project ID and aliases;
- project name;
- canonical repository/worktree/branch/source pointers;
- current goal and northpoints;
- requirements and guardrails;
- exact last verified stop point;
- one exact next action and why it is next;
- blockers and smallest unblock step;
- notes/tasks/session breadcrumbs when present;
- latest verified artifact/version separately from WIP lineage;
- artifact paths, hashes, provenance, and verification state;
- research decisions, sources, checked dates, and review dates;
- source checkpoint identity;
- schema version and bridge version;
- import history;
- supersession lineage;
- unknown extension fields from other compatible hosts.

A receiving host may add its own namespaced state, but it must not erase fields it does not understand.

## What the v24 living-world snapshot still lacks

A production state snapshot can tell Feature Foundry what its world currently looks like. A Project Brain snapshot must additionally explain **what project this is, why it exists, what work is verified, what remains blocked, and exactly how to resume it**.

The current v24 snapshot therefore must not be treated as Project Brain parity merely because it is JSON and survives native storage.

At minimum, the bridge still needs dedicated handling for:

| Project Brain concern | Current v24 living-world state | Bridge requirement |
| --- | --- | --- |
| Stable project identity | Not verified | Required |
| Canonical source/repository | Not verified | Required |
| Goal / northpoints | Not verified | Required |
| Requirements / guardrails | Not verified | Required |
| Exact stop point | Not verified | Required |
| Exact next action | Not verified | Required |
| Blockers | Not verified | Required |
| Artifact hashes/provenance | Not verified | Required |
| Research memory | Not verified | Required |
| Import/supersession ledger | Not verified | Required |
| Unknown field round-trip | Not verified | Required |
| Living-world visual/runtime state | Verified production snapshot surface | Preserve separately, optionally reference |

## Recommended v24 integration architecture

The safest bridge architecture is **parallel and additive**, not a mutation of the current living-world snapshot format.

### 1. Separate project-brain envelope

Keep the portable envelope versioned independently from `living-world-snapshot.json` and the browser `ff.browser-snapshot.v1` key.

The envelope should have a clear schema identifier and carry project-brain data only. If a bridge record references a Feature Foundry living-world snapshot, store that as an explicit linked artifact with its own hash and provenance instead of flattening the two payloads together.

### 2. Validate before persistence

The existing Tauri `save_world_snapshot` command already demonstrates the correct pattern: reject invalid JSON before writing durable state.

A project-brain import should additionally validate:

- supported schema identifier/version;
- required identity fields;
- stable-ID uniqueness;
- artifact hash shape;
- project/source provenance;
- checkpoint ordering;
- extension namespace shape;
- forbidden secret fields.

### 3. Use dedicated persistence ownership

Do not overload the existing world snapshot file.

A future native implementation can use either a dedicated app-data file or dedicated SQLite tables. If SQLite is used, keep Project Brain data namespaced from theme, ecology, music, and generic history data, and migrate it through an explicit schema version.

The existing `history` table can inspire an append-only event ledger, but current rows are generic Feature Foundry history and must not be reinterpreted retroactively as Project Brain events.

### 4. Preserve user and canonical authority

Imports must be conflict-aware rather than last-writer-wins.

Recommended precedence:

1. explicit user correction;
2. current canonical repository/runtime evidence;
3. current project-owned durable memory;
4. newer verified Project Brain checkpoint;
5. older bridge export;
6. presentation-layer summary.

A stale bridge must never overwrite newer project work simply because it was imported later.

### 5. Keep runtime state and project continuity distinct

The bridge may reference a living-world snapshot, layout, selected theme, or active Feature Foundry package as contextual state, but it should never require those fields to exist for non-Feature-Foundry projects.

That preserves portability across other hosts and prevents Feature Foundry implementation details from becoming the cross-project schema.

## Merge and supersession rules

A verified import should follow these rules:

1. Explicit user edits win.
2. Newer canonical repository/runtime evidence beats an older bridge export.
3. Project-owned durable memory beats presentation-layer summaries.
4. Unknown extension fields are preserved.
5. Same-name, different-content artifacts remain distinct until reconciled.
6. Import never silently changes the tracked-project list.
7. Completion claims remain evidence-scoped; rendering a claim in Feature Foundry does not make it runtime proof.
8. Superseded values retain lineage instead of disappearing.
9. Project Brain and living-world snapshots retain independent version and hash identities.
10. Secrets, tokens, cookies, provider credentials, and raw private account data are rejected from portable exports.

## Integrity model

### JSON Schema 2020-12

A portable bridge envelope can use JSON Schema 2020-12 to define required identity, provenance, checkpoint, artifact, and extension fields while allowing forward-compatible namespaces.

Primary source: https://json-schema.org/specification

### RFC 8785 JSON Canonicalization Scheme

RFC 8785 provides deterministic canonical JSON suitable for reproducible snapshot fingerprints. A bridge export can record a canonical SHA-256 without making whitespace or object-property ordering look like a project change.

Primary source: https://www.rfc-editor.org/rfc/rfc8785.html

### Hash-linked external artifacts

Large or host-specific data should not be duplicated into the Project Brain envelope when a durable referenced artifact is safer.

For example, a Feature Foundry living-world snapshot can be referenced by:

- artifact type;
- filename/storage identity;
- SHA-256;
- size;
- source host;
- verification state;
- creation/checkpoint ID.

The bridge should still remain useful if that optional host artifact is unavailable.

## MCP transport boundary

MCP can be an optional transport for future project-brain operations, but it is not the Project Brain schema.

If Feature Foundry eventually exposes bridge operations over MCP:

- capability discovery must not be treated as successful import;
- authorization must not be stored inside the portable project-brain payload;
- tool success must still be followed by durable reread/round-trip verification;
- the same bridge envelope should remain usable without MCP.

Transport and state authority remain separate concerns.

## Build and verify the receiving Feature Foundry host

Before testing native Project Brain integration, verify the current receiving application itself.

From a clean checkout of `Herbertofury/Feature-Foundry`:

```bash
npm install
npm run verify
```

For browser development:

```bash
npm run dev
```

For the native Tauri host:

```bash
npm run desktop:dev
```

For production artifacts:

```bash
npm run build
npm run desktop:build
npm run package
```

Do not test a bridge against an old prototype and then claim parity with the released v24 host.

## First production-aligned bridge experiment

The next useful experiment should run against the released v24 codebase while remaining isolated from current living-world persistence.

### Fixture A: portable envelope

Create one deterministic fixture containing:

- project ID and alias;
- canonical repository pointer;
- one northpoint;
- one guardrail;
- one exact stop point;
- one next action;
- one blocker;
- one verified artifact with SHA-256;
- one research decision;
- one unknown namespaced extension field.

Validate it, canonicalize it, and record the canonical SHA-256.

### Fixture B: stale conflicting envelope

Create an older snapshot that conflicts with at least:

- next action;
- blocker state;
- artifact version/hash;
- one goal or guardrail.

The import layer must not let this stale fixture silently overwrite newer canonical/user state.

### Fixture C: host-owned extension

After importing Fixture A into the isolated v24 bridge harness, add a Feature Foundry-owned extension field, export again, and prove:

- all original fields survive;
- the host-owned extension survives;
- unknown fields survive;
- the exported canonical hash is reproducible;
- living-world snapshot storage is unchanged.

## Native integration acceptance test

A native Feature Foundry Project Brain integration is proven only when the released application can:

- import the exact bridge fixture;
- show the correct stable project identity;
- show the correct goal/northpoint and guardrail;
- show the exact stop point, next action, and blocker;
- preserve artifact identity, hash, provenance, and verification state;
- save the imported state durably in a dedicated bridge persistence surface;
- restart Feature Foundry and reopen the same project-brain state;
- export a new snapshot that round-trips every required and unknown field;
- reject or safely merge the stale conflicting fixture;
- preserve a traceable import/supersession ledger;
- leave `living-world-snapshot.json` and browser `ff.browser-snapshot.v1` compatibility intact;
- expose truthful validation/merge errors instead of silently dropping data.

## Modification map

When the bridge becomes implementation work, keep responsibilities explicit.

### Portable schema and fixtures

Own versioned schema, canonicalization, fixture generation, and cross-host merge tests outside the living-world runtime payload.

### Browser Feature Foundry adapter

The browser adapter should not overload `ff.browser-snapshot.v1`. It should use dedicated bridge persistence or operate through a host-neutral import/export file path.

### Native Tauri adapter

Native commands belong near `src-tauri/src/lib.rs`; durable structured storage belongs near `src-tauri/src/database.rs` or a dedicated bridge module/table set.

### Feature Foundry UI

The UI should expose real import/export, validation, conflicts, provenance, and restart state. A decorative "Project Brain connected" badge is not integration proof.

### Project Constellation synchronization

Project Constellation should consume the resulting verified checkpoint as a control-plane mirror. It must not become a hidden runtime dependency of Feature Foundry.

## Troubleshooting

### Project Brain import appears to overwrite my current Feature Foundry world

That is an architectural regression. Project Brain state and living-world state must be separate. Disable the bridge path and inspect whether it reused `living-world-snapshot.json` or `ff.browser-snapshot.v1`.

### Import succeeds but stop point / next action are missing

Treat the import as failed. Check schema validation, field mapping, and whether the UI only rendered a subset of the envelope.

### Import succeeds but unknown fields disappear after export

The bridge is not forward-compatible. Preserve unknown namespaced fields verbatim unless an explicit migration rule supersedes them.

### Old project state overwrites newer work

Check checkpoint identity and merge precedence. Import time is not authority. Explicit user changes and newer canonical evidence must beat stale exports.

### Browser bridge works but native restart loses state

Check dedicated native persistence and reread after restart. Do not substitute in-memory React/DOM state or the ordinary living-world snapshot as proof.

### Native bridge breaks existing world snapshots

Roll back the bridge persistence integration. Project Brain is additive; existing `save_world_snapshot` / `load_world_snapshot` behavior and `living-world-snapshot.json` compatibility are non-regression requirements.

### Project Brain package contains credentials

Reject it. Portable continuity artifacts must never contain secrets, OAuth tokens, cookies, provider credentials, or raw private account data.

## Anti-degradation rules

- Never claim native Feature Foundry Project Brain integration merely because Feature Foundry v24 has snapshot persistence.
- Never repurpose `living-world-snapshot.json` as the Project Brain store without an explicit migration and compatibility contract.
- Never repurpose `ff.browser-snapshot.v1` as the Project Brain store.
- Never discard unknown bridge fields during import/export.
- Never overwrite newer user edits with an older snapshot.
- Never flatten verified, WIP, historical, and speculative states into one version.
- Never turn transport authentication or tool discovery into state-verification proof.
- Never store secrets or provider credentials in Project Brain exports.
- Never require Feature Foundry to be available for Project Constellation/project memory to remain recoverable.
- Never present the generic native `history` table as a completed Project Brain ledger until the bridge owns and verifies explicit project-brain events.

## Current documentation boundary

Verified now:

- the current Feature Foundry production repository and exact v24.0.0 head;
- real browser snapshot persistence under `ff.browser-snapshot.v1`;
- real native Tauri `save_world_snapshot` / `load_world_snapshot` commands;
- native `living-world-snapshot.json` ownership;
- native SQLite database ownership and generic history event append capability;
- current Feature Foundry build/verify/package commands;
- historical Project Brain contract and portable-artifact references.

Not yet verified:

- a current canonical `Feature-Foundry-Project-Brain.zip`;
- a current standalone `feature-foundry.project-brain/1` artifact;
- native v24 project-brain schema/tables;
- native v24 project-brain import/export UI;
- Project Brain restart/round-trip/conflict qualification inside v24.

## Exact current next action

Use released Feature Foundry v24 as the receiving host and build an **isolated, schema-validated Project Brain round-trip fixture and adapter** that does not modify `living-world-snapshot.json`, `ff.browser-snapshot.v1`, or the existing Feature Foundry SQLite schema until the fixture proves identity, provenance, unknown-field preservation, stale-conflict safety, canonical hashing, and restart semantics. Only then promote the adapter into native Feature Foundry persistence/UI and exercise the full acceptance test.