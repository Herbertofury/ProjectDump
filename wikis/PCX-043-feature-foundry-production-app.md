# Feature Foundry Production App Wiki

**Project Constellation ID:** `PCX-043`  
**Status:** ACTIVE / TRACKED  
**Current strongest verified runnable lineage:** `V33 FINAL_READY`  
**Connected placeholder repository:** [Herbertofury/Feature-Foundry](https://github.com/Herbertofury/Feature-Foundry)

## Purpose

This project tracks the actual Feature Foundry production application as distinct from historical directives, data-only bundles, generated starters, and project-family design documents. Its acceptance contract is a real stateful authoring application with professional workspaces, persistent project state, complete controls, recoverability, and verified host/export behavior.

## Current source-authority boundary

The connected GitHub repository currently exposes only a minimal README and is not enough to serve as the production source tree. The strongest durable application evidence is in the Feature Foundry Drive lineage and recovery checkpoints.

The recovery ledger records a verified V2 production reconstruction sequence that restored `apps/feature-foundry`, production-owned theme data, persistence, undo/redo, import/export, saved layouts, docking, density/motion settings, living/focus/performance modes, theme/world rendering, draggable authored objects, runtime evidence, and regression gates.

## Current strongest verified runnable artifact

Drive contains a `Feature Foundry V33 FINAL_READY Checkpoint` with status `FINAL_READY`, created 2026-08-12, built forward from the verified V25 runnable base plus V30/V31 verification lineage and V32 interaction/ecology specification without overwriting preserved base bytes.

V33 records:

- `101/101` V33 runtime assertions passed;
- `117/117` legacy runtime assertions passed;
- `22/22` V33 static assertions passed;
- 59 legacy audited controls with 0 missing handlers;
- 0 console errors and 0 page errors;
- fresh extraction pass;
- text-clipping audit at 1280x800 and 1600x1000;
- non-regression and no-artificial-caps guarantees;
- verified ZIP SHA-256 `680978a3aa8f16b47e767720ebfdc3b89fda5c148c5f3d4d3f308390b09385d9`;
- verified HTML SHA-256 `83aac630afa4e6522d28452bb6a7c0ebe183eee6812b89b6d742662876af06ec`;
- remote Drive artifact ID `1_mLbBXiS0yL7g2cKP7qQJxqyyRHP4RSY` with matching remote SHA-256.

## V33 production capabilities recorded by the checkpoint

The verified artifact includes:

- Theme-aware Library Ecology Lab;
- Ecology Director world modes and transition depth 0-5;
- Efficient/Balanced/High/Ultra/Cinematic presentation tiers with content parity;
- causal world-signal bus and replay history;
- chronological, interaction, and authored-world memory channels;
- advanced optical/spatial depth composition;
- soundtrack/provider mapping hub with six provider mappings;
- five host adapters;
- persistent state and reduced-motion/performance equivalence.

## Production-app rules

- The standalone HTML/artifact is valid verified runtime evidence, but the canonical maintainable source/worktree still needs to be resolved before broad implementation work.
- Preserve every verified theme/world/object record and every completed control.
- Never introduce viewport culling, hidden caps, reduced off-screen availability, or lower-fidelity presentation tiers that change content semantics.
- Every top-level tab/workspace must open distinct real functionality, not only change selection state.
- Every visible control remains subject to the no-dead-UI rule.
- State-changing operations need persistence and recovery behavior appropriate to the feature.
- Maintain source/data lineage so generated/exported content can be traced to its project-owned origin.

## Current technology observations

Feature Foundry's current browser-side ecology/rendering direction should treat PixiJS `8.18.1` as the current stable PixiJS line when Pixi integration is evaluated. Existing Rapier JavaScript packages remain at `0.19.3`, but the dedicated `dimforge/rapier.js` repository was archived in July 2026 while the Rust `dimforge/rapier` core continues actively. That makes any new direct JS-binding dependency a migration-risk item requiring an explicit maintenance strategy rather than a silent upgrade.

## Exact next action

Resolve the maintainable canonical V33-equivalent source/worktree from the durable recovery lineage, verify its source manifest against the known verified runnable artifact, then run the real build and full workspace/runtime matrix before accepting any new framework or physics-stack migration.

## Wiki maintenance

Update this page when a newer remotely byte-verified runnable Feature Foundry checkpoint appears, the canonical production repository/source tree is recovered, host adapters change, or the runtime verification matrix materially advances.