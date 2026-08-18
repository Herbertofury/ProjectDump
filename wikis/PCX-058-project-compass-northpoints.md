# Project Compass Northpoints Wiki

**Project Constellation ID:** `PCX-058`
**Status:** ACTIVE / TRACKED
**Goal:** Preserve durable product intent, goals, guardrails, wants, feature pillars, publication targets, and measurable acceptance signals without silently rewriting foundational intent.

## What Project Compass is

Project Compass is the intent layer for ongoing projects. It records **why a project exists and what must remain true** while implementation details, versions, branches, and artifacts change underneath it.

Project Constellation answers where work stopped and what happens next. Project Compass complements that with durable northpoints, goals, principles, guardrails, and proof signals so an apparently successful technical change cannot quietly move the product away from the user's intended outcome.

## Direct durable evidence resolved this pass

Google Drive contains a real `PROJECT-COMPASS.md` artifact for project `prj-9e0f6a6885ba4cf5`, revision **16**, updated 2026-08-09. The artifact demonstrates the current Compass model in practice rather than only as a design idea.

It contains stable IDs and evidence fields for:

- Northpoints;
- Goals;
- Feature Pillars;
- Principles;
- Wants;
- Guardrails;
- Acceptance Signals;
- Publication Targets.

Each substantive entry carries status, priority, source, prose intent, and an explicit proof condition. Examples in the recovered artifact include `NP-FAST`, `G-LAYOUT`, `GR-NOCULL`, `GR-DRIVE-ALWAYS`, and `AS-PERF-SATURATION`.

The artifact is currently Markdown. A Drive search during this pass did not locate a standalone `COMPASS.json`, so a machine-readable Compass mirror should not be claimed as presently available there.

## Why stable IDs matter

A Compass entry should be addressable independently of its prose wording. Stable IDs allow later revisions to say that a northpoint was refined, superseded, split, or retired without pretending the previous intent never existed.

For example:

- an implementation can satisfy a new goal while still violating `GR-NOCULL`;
- a later wording refinement can supersede a goal without destroying the prior text;
- an acceptance signal can remain stable while the implementation technology changes completely.

## Supersession contract

Foundational intent should be **superseded**, not overwritten silently.

A meaningful change should preserve:

- entry ID;
- old revision/value;
- new revision/value;
- source of the change;
- timestamp/checkpoint;
- reason for supersession;
- affected acceptance signals;
- whether the old entry is historical, replaced, or still concurrently active.

User corrections always outrank derived or automated interpretations.

## Current integrity research

### JSON Schema 2020-12

If a machine mirror is created, JSON Schema 2020-12 is suitable for enforcing the structure of Compass entries, revisions, stable IDs, proof conditions, and extension fields.

Primary source: https://json-schema.org/specification

### RFC 8785 canonical JSON

RFC 8785 can provide deterministic canonical JSON for reproducible hashes. That enables a revision ledger to record exact content fingerprints without making whitespace or property order significant.

Primary source: https://www.rfc-editor.org/rfc/rfc8785.html

These are integrity mechanisms, not replacements for the human-readable Compass.

## Proposed machine-mirror experiment

Create a **derived, additive** machine mirror for one existing Compass without changing the canonical Markdown artifact.

The experiment should:

1. parse every active section and stable ID;
2. preserve status, priority, source, prose intent, and proof condition exactly;
3. validate the mirror with a versioned JSON Schema;
4. canonicalize it with RFC 8785;
5. record snapshot SHA-256 plus the source Markdown hash;
6. export the machine mirror back to a human-readable comparison report;
7. prove no entry was lost, renamed, or semantically changed;
8. record future supersession as append-only revision events.

## Anti-degradation rules

- Never regenerate user-authored intent from project code and overwrite the original.
- Never mark a guardrail satisfied because a build passes.
- Never infer that a newer implementation invalidates an older northpoint.
- Never drop proof conditions during serialization.
- Never mutate Compass entries merely because Project Constellation filtering or research changes.
- Never let a machine mirror become authoritative unless the user explicitly promotes it.

## Acceptance test

A machine Compass mirror is acceptable only when:

- every stable ID in the source Compass exists exactly once;
- all active/inactive/superseded states survive;
- source/provenance survives;
- proof conditions are byte- or semantically equivalent by a documented rule;
- round-trip comparison reports zero unintended loss;
- canonical hashes are reproducible;
- a user correction creates a traceable supersession event rather than rewriting history;
- Project Constellation can link to the latest active intent without becoming the intent authority.

## Exact current next action

Preserve the recovered revision-16 Project Compass as durable intent evidence, then prototype a schema-validated, hashable **derived** mirror and append-only supersession ledger without changing the human-authored Compass or claiming a current `COMPASS.json` already exists.
