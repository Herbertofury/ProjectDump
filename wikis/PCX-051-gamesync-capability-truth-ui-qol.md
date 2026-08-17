# GameSync Capability Truth / UI QoL Wiki

**Project Constellation ID:** `PCX-051`  
**Status:** ACTIVE / TRACKED  
**Current source authorities:** [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync) and [Herbertofury/GameSync-Next](https://github.com/Herbertofury/GameSync-Next)

## Purpose

GameSync Capability Truth / UI QoL exists to make every user-visible capability claim match the strongest current evidence. Its job is not to create more badges, toggles, or status text. Its job is to prevent the UI, project brain, migration work, and release surfaces from saying a capability is complete when the current shipping/Next implementation, tests, runtime, or parity evidence does not prove that claim.

The core rule is simple: **every visible capability status must be derived from executable or inspectable evidence, and the UI must never be able to promote itself to verified.**

## Current canonical evidence model

The strongest current machine-readable authority is GameSync Next's [`docs/gamesync-parity-matrix.json`](https://github.com/Herbertofury/GameSync-Next/blob/main/docs/gamesync-parity-matrix.json), validated by [`scripts/audit-gamesync-parity.mjs`](https://github.com/Herbertofury/GameSync-Next/blob/main/scripts/audit-gamesync-parity.mjs).

The parity matrix already distinguishes three important states:

- `verified` - implementation plus evidence/test gates support the parity claim;
- `implemented-unverified` - implementation exists but the verification contract is not complete;
- `gap` - required behavior is still absent or materially incomplete.

The audit script does substantially more than validate JSON syntax. It checks matrix semantics, requires source/evidence/test-gate fields where appropriate, rebuilds Extension V2 before inspecting generated output, and audits concrete invariants across shipping GameSync and GameSync Next. That makes it a better source of capability truth than a manually maintained checklist or UI toggle.

## Current examples from the parity contract

Current GameSync Next evidence marks several areas as verified, including settings/shared-storage parity, the Mods release-table/Updates path, AutoNotes, and source-discovery/storage-durability work. The same matrix explicitly records **Bounty & Twitch reward runtime** as a `gap` in Extension V2 because the production entitlement/reward integration has not been reproduced there.

That distinction must remain visible. A page rendering a Bounty button, a TypeScript type existing, or a local build passing does not transform a parity gap into a verified capability.

## Capability Truth surface

The next useful product-level improvement is a read-only Capability Truth surface generated from the canonical parity matrix and audit output rather than a second independent status database.

A useful row should expose:

- capability ID/name;
- shipping GameSync baseline owner/source;
- GameSync Next implementation owner/source;
- current status (`verified`, `implemented-unverified`, or `gap`);
- evidence files;
- test/runtime gate;
- latest source commit or verification watermark when available;
- stale-evidence warning when the implementation changed after the last proof;
- exact blocker/next proof step;
- direct links to the relevant source, test, matrix entry, or runtime evidence.

### Required filters / views

The surface should support fast read-only views such as:

- gaps;
- implemented but unverified;
- verified;
- stale evidence;
- changed since last verification;
- shipping-only;
- Next-only;
- cross-host parity work.

Filtering must never hide records from the underlying truth set or alter their canonical status.

## Verification authority and write path

The Capability Truth UI must not contain an ordinary `Mark verified` control. A capability can become verified only when the canonical evidence contract is updated and the audit/test/runtime gates pass.

The safe write path is:

1. implement or repair the real feature;
2. add/update source evidence and test gates;
3. run the parity audit and affected runtime verification;
4. update the canonical parity record when the evidence is genuinely sufficient;
5. regenerate/reload the read-only Capability Truth surface from that canonical state.

If a human override is ever required, it should be recorded as an explicit review note with provenance, not as a silent replacement for executable evidence.

## UI QoL contract

GameSync UI quality is part of capability truth. A technically present feature is still misleading if the control is dead, opens the wrong destination, shows success before work succeeds, hides an error, loses state after restart, or implies support that the backend/provider does not actually provide.

Every affected user-visible control should therefore preserve this end-to-end chain:

`control -> validation -> real implementation/service -> observable result -> truthful error state -> persistence/reload/restart behavior where applicable`

### Contextual destination rule

Actions such as Open, View source, Guide me, Show location, Download, Launch, Update, or Configure must land on the exact promised entity/state. A generic homepage, broad search result, empty panel, or unrelated route is not a successful implementation of a contextual control.

## Anti-degradation requirements

Capability-truth work must never improve a score by shrinking the product. In particular, do not:

- mark a feature verified by deleting an unsupported branch or adapter;
- remove a failing control instead of fixing the promised workflow unless the product requirement itself is explicitly retired;
- reduce supported sites/providers/hosts to make parity easier;
- hide unverified capabilities from the data model;
- weaken audit/test gates;
- replace real runtime verification with a rendered UI badge;
- use stale generated output as evidence for current source;
- convert a `gap` into `implemented-unverified` without actual implementation evidence;
- convert `implemented-unverified` into `verified` without the required proof.

## Staleness model

Capability truth needs source-lineage awareness. A previously verified record can become stale when any load-bearing implementation, schema, manifest, host adapter, provider contract, or verification fixture changes.

A practical staleness watermark should compare at least:

- shipping GameSync commit/source identity;
- GameSync Next commit/source identity;
- parity-matrix revision;
- relevant test/runtime evidence revision;
- last successful verification timestamp/receipt.

A stale verified record should remain historically verified but be visually marked as **verification stale** until the affected gates are rerun. Do not silently demote historical evidence or silently present old evidence as current.

## Relationship to Project Constellation

Project Constellation should mirror capability truth, not invent it. A useful Project Constellation lens can summarize per-project counts of gaps, implemented-unverified capabilities, stale verifications, and verified capabilities, with direct links into the canonical GameSync evidence.

This should remain read-only from the Project Constellation presentation layer. Editing the second-brain view must not bypass GameSync's source/test/runtime verification authority.

## Current repository baselines checked 2026-08-17

At this evolution pass:

- shipping GameSync `main` resolved to `d84c2389b9e01dc47b7ba094c2d23a7b4cbbf9f4`;
- GameSync Next `main` resolved to `9e337c720f0180cffa577f140b181c699f0a1650`.

Treat these as this pass's evidence watermarks, not permanent latest-version claims.

## Implementation experiment

Build the first Capability Truth surface as a generated/read-only view over the existing parity matrix. Do not add a second manually maintained capability database.

### Acceptance test

The experiment passes only if:

1. the parity audit succeeds on the exact source commits under test;
2. every rendered capability corresponds one-to-one with a canonical matrix record;
3. status counts exactly match the matrix/audit result;
4. each nontrivial status exposes its source/evidence/test gate;
5. the UI cannot promote a capability to verified by itself;
6. changing a matrix status/evidence source changes the generated surface without manual duplication;
7. stale-source detection flags changed implementation after the last verification watermark;
8. filters never delete or mutate canonical records;
9. real contextual controls used from the surface land on the exact evidence/destination they promise.

## Exact current next action

Implement or prototype the read-only Capability Truth generator/view against the current parity matrix and audit output, then verify exact record/status parity. Keep the feature advisory until its own stale-evidence and exact-destination tests pass in the real GameSync workflow.

## Wiki maintenance

Update this page whenever the parity status vocabulary changes, the audit contract changes, a new host becomes part of parity, stale-evidence tracking is implemented, or the current source/runtime verification watermarks materially change. Preserve historical verification evidence rather than rewriting old results as if they never happened.
