# GameSync Capability Truth / UI QoL Wiki

**Project Constellation ID:** `PCX-051`
**Status:** ACTIVE / TRACKED
**Current source authorities:** [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync) and [Herbertofury/GameSync-Next](https://github.com/Herbertofury/GameSync-Next)
**Current GameSync Next evidence watermark:** `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`

## Purpose

GameSync Capability Truth / UI QoL exists to make every user-visible capability claim match the strongest current evidence. Its job is not to create more badges, toggles, or status text. Its job is to prevent the UI, project brain, migration work, and release surfaces from saying a capability is complete when the current shipping/Next implementation, tests, runtime, or parity evidence does not prove that claim.

The core rule is simple: **every visible capability status must be derived from executable or inspectable evidence, and the UI must never be able to promote itself to verified.**

## Current canonical evidence model

The strongest current machine-readable authority is GameSync Next's [`docs/gamesync-parity-matrix.json`](https://github.com/Herbertofury/GameSync-Next/blob/main/docs/gamesync-parity-matrix.json), validated by [`scripts/audit-gamesync-parity.mjs`](https://github.com/Herbertofury/GameSync-Next/blob/main/scripts/audit-gamesync-parity.mjs).

The current parity matrix defines **four** canonical states:

- `verified` - both implementations exist and current runtime evidence supports the parity claim;
- `implemented-unverified` - both implementations exist but equivalent end-to-end proof is incomplete;
- `gap` - a JavaScript-baseline capability is missing or materially incomplete in Next;
- `implementation-specific` - a platform-specific capability has an explicit reason not to be identical.

The fourth state is important. `implementation-specific` must not be collapsed into `verified`, `gap`, or a generic exception bucket because the canonical matrix intentionally represents legitimate platform-specific divergence separately from incomplete parity.

The audit script does substantially more than validate JSON syntax. It checks matrix semantics, requires source/evidence/test-gate fields where appropriate, rebuilds Extension V2 before inspecting generated output, and audits concrete invariants across shipping GameSync and GameSync Next. That makes it a better source of capability truth than a manually maintained checklist or UI toggle.

## Material current-main status change

GameSync Next `main` advanced from the older `9e337c720f0180cffa577f140b181c699f0a1650` watermark to merge commit `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`, **Merge universal Game Tracker, Bounty, and Animation Tracker recovery**.

That merge materially changes capability truth. The prior wiki described Bounty and Animation Tracker as explicit parity gaps. The current parity matrix now marks:

- `bounty` as `verified`;
- `animation-tracker` as `verified`;
- `universal-game-tracker` as `verified`.

These are evidence-backed status transitions, not documentation-only promotions.

### Bounty verification now represented in the canonical matrix

The current parity record points to:

- JavaScript baseline: `src/features/bounty`;
- GameSync Next implementation: `apps/extension-v2/src/features/bounty`, `apps/extension-v2/src/ui/app/bounty`, and background routing;
- runtime gate: `scripts/verify-extension-v2-opera.js`.

The matrix records a clean isolated Opera run that synchronized **107 live GamerPower records** with zero rejected rows, persisted a healthy source snapshot, rendered the calendar, and kept the React root mounted once.

### Animation Tracker verification now represented in the canonical matrix

The current parity record points to:

- JavaScript baseline: `src/animation-tracker`;
- GameSync Next implementation: `apps/extension-v2/src/features/animation-tracker`, `apps/extension-v2/src/ui/app/animation-tracker`, and the universal Game Tracker view;
- runtime gate: `scripts/verify-extension-v2-opera.js`.

The matrix records isolated Opera proof for exact HTTPS source persistence, semantic-version detection, polling, an installed-pack update, and a single React root mount.

### Universal Game Tracker is now a verified capability

The merged Game Tracker is materially broader than a simple tab replacement. Current project-owned evidence records:

- public feature entrypoint under `apps/extension-v2/src/features/game-tracker`;
- UI entrypoint under `apps/extension-v2/src/ui/app/game-tracker`;
- Dexie database `gamesync-game-tracker-v1` for workspaces, records, relationships, binary assets, activity, and preferences;
- archive/restore behavior without a permanent-delete action;
- first-class Sims 4 collections for households, Sims, missing households, worlds, lots, and CC/mod dependencies;
- universal template workspaces for animations, quests, collectibles, mods, and custom tracking;
- typed user-defined fields and collections;
- `.docx`, `.xlsx`, `.xls`, `.csv`, `.tsv`, GameSync JSON, Google Docs, and Google Sheets import paths;
- lossless GameSync JSON, multi-sheet XLSX, editable image-aware DOCX, and active-collection CSV export paths;
- native DOCX dropdown parsing with selected value, full option list, alias, and source shading preserved as tracker field schema;
- worker-owned heavy parsing, relation resolution, persistence, and document generation so large binary/document work does not become a UI-thread shortcut.

The current parity record states that clean isolated Opera runs imported both a supplied **43 MB local DOCX** and its live Google Docs source. The verified result was **181 active records** consisting of 75 households, 4 populated Sims, 67 lots, and 35 worlds, plus 75 relationships and 124 schema-bound images. Opera rendered **836 inline pills**, preserved the complete source wardrobe option set, persisted an inline `Cleaned` to `Dirty` edit, kept root mount count at one, and recorded zero extension console/page/request errors. JSON, XLSX, DOCX, and CSV downloads were retained as test artifacts and passed content-level checks.

Capability Truth must preserve these exact evidence boundaries. A future source change affecting tracker import, schema mapping, relation resolution, image ownership, export generation, or browser mounting can make the verification stale even if the visible tab still renders.

## Current examples from the parity contract

Current GameSync Next evidence marks examples such as extension identity/in-place upgrade, the main library shell, web-page overlay injection, source discovery/Found Mods, Living Room, the universal page mascot shim, Bounty, Animation Tracker, Universal Game Tracker, the command center, and the offscreen transformer runtime as `verified`.

The same matrix deliberately keeps a substantial set as `implemented-unverified`, including collections/wishlist/playing, Nexus integration, the mods organizer, mod authors, News/NewsForge, achievements, the card game, mascot runtime/core games, Shimeji Browser, GX Corner, the AI assistant, themes/effects, and storage/settings.

Explicit `gap` examples still include the complete JavaScript mascot arcade catalog and expanded Petz/ACS content. These unresolved gaps must remain visible even as other features graduate to verified.

These distinctions must remain visible. A rendered tab, a TypeScript type, a copied legacy asset, or a successful build does not transform an unverified or missing capability into a verified one.

## Capability Truth surface

The next useful product-level improvement is a read-only Capability Truth surface generated from the canonical parity matrix and audit output rather than a second independent status database.

A useful row should expose:

- capability ID/name;
- shipping GameSync baseline owner/source;
- GameSync Next implementation owner/source;
- current canonical status (`verified`, `implemented-unverified`, `gap`, or `implementation-specific`);
- evidence files;
- test/runtime gate;
- latest source commit or verification watermark when available;
- **status-transition provenance** when a capability changes class;
- stale-evidence warning when a load-bearing implementation changed after the last proof;
- exact blocker/next proof step;
- direct links to the relevant source, test, matrix entry, or runtime evidence.

### Required filters / views

The surface should support fast read-only views such as:

- gaps;
- implemented but unverified;
- verified;
- implementation-specific;
- stale evidence;
- changed since last verification;
- newly verified since a selected watermark;
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
- collapse `implementation-specific` into another state merely to simplify reporting;
- weaken audit/test gates;
- replace real runtime verification with a rendered UI badge;
- use stale generated output as evidence for current source;
- convert a `gap` into `implemented-unverified` without actual implementation evidence;
- convert `implemented-unverified` into `verified` without the required proof;
- erase the historical status transition when a capability becomes verified;
- treat one verified subworkflow as proof for a broader capability record than the matrix actually defines.

## Staleness model

Capability truth needs source-lineage awareness. A previously verified record can become stale when any load-bearing implementation, schema, manifest, host adapter, provider contract, import/export format, worker boundary, or verification fixture changes.

A practical staleness watermark should compare at least:

- shipping GameSync commit/source identity;
- GameSync Next commit/source identity;
- parity-matrix revision;
- relevant test/runtime evidence revision;
- last successful verification timestamp/receipt.

A stale verified record should remain historically verified but be visibly marked as **verification stale** until the affected gates are rerun. Do not silently demote historical evidence or silently present old evidence as current.

A repository head change is not automatically a capability change. The current `cd906ff...` head is a useful counterexample: it materially changes Bounty, Animation Tracker, and Universal Game Tracker truth, but does not automatically invalidate unrelated capabilities whose load-bearing source/evidence did not change. Staleness must therefore be dependency-aware.

## Relationship to Project Constellation

Project Constellation should mirror capability truth, not invent it. A useful Project Constellation lens can summarize per-project counts of gaps, implemented-unverified capabilities, implementation-specific capabilities, stale verifications, newly verified capabilities, and verified capabilities, with direct links into the canonical GameSync evidence.

This should remain read-only from the Project Constellation presentation layer. Editing the second-brain view must not bypass GameSync's source/test/runtime verification authority.

## Current repository baselines checked 2026-08-18

At this evolution pass:

- shipping GameSync `main` remains `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`;
- GameSync Next `main` is `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`;
- Extension V2 still declares version `0.8.0`.

The GameSync Next head change is materially relevant because it merged verified feature recovery and changed canonical parity states. These commit IDs are evidence watermarks, not permanent latest-version claims.

## Implementation experiment

Build the first Capability Truth surface as a generated/read-only view over the existing parity matrix. Do not add a second manually maintained capability database.

The first fixture should specifically preserve the current transition history for Bounty and Animation Tracker and the introduction of Universal Game Tracker as verified, so the view can demonstrate that status changes are derived from matrix/evidence revision rather than manual UI edits.

### Acceptance test

The experiment passes only if:

1. the parity audit succeeds on the exact source commits under test;
2. every rendered capability corresponds one-to-one with a canonical matrix record;
3. all four status classes are represented without lossy remapping;
4. status counts exactly match the matrix/audit result;
5. Bounty and Animation Tracker render as `verified` at the `cd906ff...` evidence watermark and retain provenance showing they were previously gaps;
6. Universal Game Tracker renders as a first-class verified capability with its actual source/evidence/test gate;
7. each nontrivial status exposes its source/evidence/test gate or explicit implementation-specific rationale;
8. the UI cannot promote a capability to verified by itself;
9. changing a matrix status/evidence source changes the generated surface without manual duplication;
10. stale-source detection flags only records whose load-bearing implementation/evidence changed after the last verification watermark;
11. filters never delete or mutate canonical records;
12. real contextual controls used from the surface land on the exact evidence/destination they promise.

## Exact current next action

Implement or prototype the read-only Capability Truth generator/view against the current `cd906ff...` parity matrix and audit output. Include all four status classes, dependency-aware stale-evidence logic, and status-transition provenance. Use Bounty, Animation Tracker, and Universal Game Tracker as the first transition fixtures, then verify exact record/status parity and exact evidence destinations in the real GameSync workflow before treating the surface itself as authoritative.

## Evidence

- Shipping GameSync repository: https://github.com/Herbertofury/Gamesync
- GameSync Next repository: https://github.com/Herbertofury/GameSync-Next
- Current parity matrix: https://github.com/Herbertofury/GameSync-Next/blob/main/docs/gamesync-parity-matrix.json
- Current recovery merge: https://github.com/Herbertofury/GameSync-Next/commit/cd906ff0831bf7fc33b41fea31b6f0c004cc1562
- Extension V2 package: https://github.com/Herbertofury/GameSync-Next/blob/main/apps/extension-v2/package.json
- Parity audit: https://github.com/Herbertofury/GameSync-Next/blob/main/scripts/audit-gamesync-parity.mjs

## Wiki maintenance

Update this page whenever the parity status vocabulary changes, a capability changes canonical state, the audit contract changes, a new host becomes part of parity, stale-evidence tracking is implemented, or the current source/runtime verification watermarks materially change. Preserve historical verification and status-transition evidence rather than rewriting old results as if they never happened.
