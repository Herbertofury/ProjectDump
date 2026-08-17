# GameSync Theme Foundry Wiki

**Project Constellation ID:** `PCX-048`  
**Status:** ACTIVE / TRACKED  
**Goal:** Author and package GameSync themes without drifting from Feature Foundry source contracts.  
**Current durable implementation evidence:** GameSync 0.25.9 progress checkpoint plus Feature Foundry North Star UI validation evidence.

## Verified current state

The durable GameSync **0.25.9 Progress Checkpoint** preserves the verified 0.25.8 baseline plus the implemented 0.25.9 agent-enforcer, 54-action workspace pass, complete-control excellence layer, and **Feature Foundry theme/workspace adoption**.

That checkpoint explicitly states that full runtime and release validation was still in progress. Treat it as a real resumable source checkpoint, not a release-complete claim.

The later **Feature Foundry North Star UI Pass 2** verification records state-driven behavior across Full, Panel, Popup, and Options surfaces while preserving existing themes and complete-data guarantees.

## Verified North Star behavior

The pass records:

- procedural ambient response to pointer position, application work, success, failure, search, and modal state;
- determinate progress where the provider actually exposes progress and indeterminate motion only where progress is unknown;
- selected-tab continuity without replacing theme styling;
- selected-item-to-detail continuity;
- accessible activity capsule/deck state;
- semantic control intent states;
- reduced-motion and effects-off fallbacks preserving hierarchy and identity.

## Anti-degradation evidence

The current verification explicitly prohibits:

- IntersectionObserver admission;
- `content-visibility` admission;
- lazy media admission;
- first-N slicing;
- item limits;
- hidden pagination;
- requestIdleCallback admission;
- viewport culling;
- quality reduction.

All cards, records, media, and controls remain immediately available.

### Recorded validation counts

- North Star tests: 9 passed
- JavaScript syntax: 568 files, zero errors
- JSON syntax: 179 files, zero errors
- HTML resources: 689 references, zero missing
- Manifest resources: 78 references, zero missing
- No-cap contract: 615 runtime files, zero violations
- Entry controls: 264/264 wired
- Static actions: 213/213 wired
- Workspaces: 18/18
- Workspace actions: 54/54 distinct actions
- UI completion regressions: passed
- Usability accelerator: passed
- Agent enforcer: passed

The managed headless Chromium visual/runtime attempt did not complete, so browser-runtime proof remains a separate gate.

## Theme Foundry ownership model

Theme Foundry should not become a second independent theme schema. The durable Project Constellation requirement is one source-of-truth theme contract with explicit host adapters and migration/parity evidence.

A theme package should distinguish:

- stable theme identity/version;
- source Feature Foundry contract version;
- semantic design tokens;
- assets and provenance;
- object/world/ecology data;
- sound/provider metadata;
- motion/accessibility variants;
- GameSync host overrides;
- extension/desktop host capabilities;
- migration version;
- validation evidence.

Host-specific fields must not silently redefine source semantics.

## Current interoperability research

The **Design Tokens Format Module 2025.10** is the first stable Design Tokens Community Group format and is intended for cross-tool design-token interoperability. It supports modern color representations and cross-platform exchange.

Primary sources:

- https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/
- https://www.designtokens.org/TR/2025.10/format/

CSS Color Module Level 4 is currently a W3C Candidate Recommendation Draft dated May 2, 2026. It provides the modern color-space basis for features such as Oklab/OKLCH and wide-gamut color.

Primary source:

- https://www.w3.org/TR/css-color-4/

These are interoperability inputs, not reasons to rewrite the working theme system.

## Proposed Theme Foundry interchange adapter

Add an export/import adapter capable of representing the semantic theme-token subset in Design Tokens 2025.10-compatible form. Preserve GameSync/Feature Foundry-specific information under explicit namespaced extension data instead of forcing non-token world/runtime semantics into generic token fields.

Use modern color spaces such as OKLCH only with deterministic fallbacks and fixture-based visual/semantic equivalence. Existing theme values remain canonical until migration is proven.

## Smallest useful experiment

Select one existing GameSync/Feature Foundry theme and produce:

1. canonical existing package;
2. Design Tokens 2025.10 interchange export;
3. reimported package;
4. host-adapter output for shipping GameSync and GameSync Next.

Compare stable IDs, token semantics, asset references, color output, accessibility variants, and runtime behavior.

### Acceptance test

- no theme/object/provider/world data is lost;
- all existing complete-data/no-cap guarantees remain intact;
- reimport preserves stable theme identity;
- current colors remain visually and semantically equivalent within declared tolerances;
- reduced-motion/effects-off variants remain equivalent;
- shipping GameSync and GameSync Next host adapters produce the same intended theme contract;
- current build/tests remain clean;
- real browser host verification is performed before interchange support is promoted as complete.

## Exact next action

Build a one-theme Design Tokens 2025.10 round-trip fixture as an adapter-only experiment, then run the existing North Star, no-cap, host-parity, and real-runtime gates before changing the canonical theme package format.

## Evidence

- GameSync 0.25.9 progress folder: https://drive.google.com/drive/folders/1UrjjvuaH5EJQO_-XgoOLGW-5GLN1DRom
- GameSync 0.25.9 progress checkpoint: https://drive.google.com/file/d/1urgN5SucgvyPeLSmMNGsk27v8C7D-gpD/view
- Feature Foundry North Star UI Pass 2 verification: https://drive.google.com/file/d/1GXjj44gdetrXvAjmIpctnrY7Qwd5ePzr/view

## Wiki maintenance

Update this page when the canonical theme schema, Feature Foundry source contract, host adapters, token interchange format, theme counts, validation gates, or real runtime evidence changes. Never replace strong no-cap and complete-data guarantees with rendering shortcuts.