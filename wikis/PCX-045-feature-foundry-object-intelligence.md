# Feature Foundry Object Intelligence Wiki

**Project Constellation ID:** `PCX-045`
**Status:** ACTIVE / TRACKED

## Purpose

Object Intelligence is the Feature Foundry layer that turns visual assets into semantically identified, behavior-capable, provenance-preserving objects. It covers object identity, archetypes/families, materials, affordances, behavior graphs/profiles, rigs/anchors, interaction semantics, source lineage, reversible derivation, placement state, and export/host behavior.

## Current durable evidence

Feature Foundry's preserved V11 data lineage established an Object Atlas direction with validated object archetypes/families, materials, behavior profiles, affordances, cross-database references, search/indexing support, and manifest hashes. Later Feature Foundry production recovery promoted authored theme/world data into production-owned runtime boundaries rather than depending on migration-only packages.

The current V33 verified ecology artifact demonstrates the runtime side of intelligent objects: authored world objects remain present across presentation tiers, participate in distinct press/drag/collision/recovery paths, preserve persistent state, and feed a causal world-signal/replay model. V33's checkpoint records complete runtime/static/legacy verification with zero missing legacy handlers and no artificial caps.

## Object contract

An intelligent object should preserve at least:

- stable object identity;
- archetype/family and semantic role;
- source/provenance and immutable original reference;
- material/visual DNA metadata;
- authored affordances and interaction capabilities;
- behavior/profile/graph identity;
- rig/anchor/hotspot or spatial interaction metadata where needed;
- placement/state independent from asset identity;
- reversible derivation lineage for generated/transformed assets;
- host/export compatibility metadata;
- validation/version evidence.

Do not collapse these fields into a single display name or image URL.

## Current standards research

Khronos submitted `KHR_interactivity` for glTF 2.0 ratification in July 2026. It embeds portable behavior graphs directly in glTF assets and is accompanied by emerging node interaction extensions. Khronos also maintains an experimental React-based authoring tool for creating and previewing these behavior graphs. This is highly relevant to Feature Foundry's object-intelligence goals because it offers a standards-oriented interchange layer between object identity, authored behavior, and host runtimes.

However, `KHR_interactivity` is still a Release Candidate in the Khronos extension registry, while related physics/collision extensions remain earlier-stage. Treat it as an **interchange experiment**, not a replacement for Feature Foundry's internal object model yet.

## Proposed interoperability experiment

Build a narrow adapter that maps a small verified subset of Feature Foundry object affordances/behavior nodes to `KHR_interactivity` and back without changing the internal canonical model.

Start with three representative objects:

1. a selectable/toggle object;
2. an object with a bounded animation/state sequence;
3. an object whose behavior depends on a world signal/input.

For each object, export glTF + behavior graph, load it in an independent Khronos-compatible test path, re-import the supported graph, and compare the resulting semantic contract to the original.

## Acceptance test

- stable Feature Foundry object ID survives round trip through explicit metadata or a mapped identity field;
- supported affordance semantics are preserved;
- unsupported nodes fail visibly and do not silently degrade;
- original object source/provenance remains intact;
- round trip does not mutate unrelated object metadata;
- behavior remains bounded and replayable;
- internal Object Atlas remains authoritative until the external standard reaches sufficient maturity and parity;
- no object count/quality reduction is introduced.

## Current technology caution

Do not bind object semantics directly to an archived or unstable runtime library. The dedicated `rapier.js` repository was archived in July 2026 even though Rapier's Rust core continues. Keep physics behind an adapter so an object can retain the same affordance/behavior model if the physics implementation changes.

## Exact next action

Resolve the newest canonical Object Atlas/production object-schema source from the Feature Foundry recovery lineage, record the exact current fields and validation counts, then prototype the three-object `KHR_interactivity` interoperability fixture without changing canonical object storage.

## Wiki maintenance

Update this page when the Object Atlas schema is re-resolved, object counts/fields change, a verified Object Studio runtime appears, the glTF interactivity extensions reach a new maturity level, or the interchange experiment produces real round-trip evidence.