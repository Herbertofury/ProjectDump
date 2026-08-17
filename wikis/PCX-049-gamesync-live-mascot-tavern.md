# GameSync Live Mascot Tavern Wiki

**Project Constellation ID:** `PCX-049`  
**Status:** ACTIVE / TRACKED  
**Goal:** Run live mascot engines inside GameSync as real interactive systems.  
**Current verified line:** GameSync 0.25.9 Live Mascot Tavern - Native Engines.

## Verified current state

The durable 0.25.9 verification records that the Mascot Room became **Moonwake Rest House**, a living mascot resting tavern connected to GameSync's real mascot registry and global swarm.

The implementation uses real engine instances rather than a generic mascot simulator. Recorded engine families include:

- Clippy / ACS
- Shimeji
- WebMeji
- Petz
- future global-swarm engines through the same bridge contract

The implementation preserves engine-native behavior while adding room-aware roles and furnishing interactions.

## Native behavior contract

The durable status record explicitly preserves:

- animation lists;
- behaviors;
- native `moveTo` / `setPosition` movement paths;
- speech and balloons;
- drag/context-menu behavior;
- spawn picker;
- persistence;
- swarm controls.

The fake mascot simulation and decorative mascot stand-ins were removed. Generated image stand-ins were not used as substitutes for the native engines.

## Performance evidence

The durable status record reports:

- previous bundle: 4,926,116 bytes
- current bundle: 4,214,259 bytes
- bytes removed: 711,857
- reduction: 14.45%

This came from separating duplicate/stale vendor/app bundle work, not from reducing mascot features or culling mascot content.

## Validation evidence

Recorded validation includes:

- ZIP CRC: pass
- duplicate ZIP entries: zero
- manifest entries: one
- local reassembly byte match: true
- real mascot-engine bridge: true
- native `moveTo` preference: true
- fake mascot simulation removed: true
- no-cap contract: pass
- entry controls: 264/264
- static actions: 213/213
- workspaces: 18/18
- workspace actions: 54

The managed Chromium extension-navigation gate was blocked by environment policy and is explicitly not counted as passed.

## Archive identity

The durable status record identifies:

- archive: `GameSync-0.25.9-Live-Mascot-Tavern-Native-Engines-FULL.zip`
- size: 247,583,122 bytes
- SHA-256: `87c4380af9e5bf405dca67c07160086a79cb2e9e3f1381cc23120ffaac7678f4`

The multipart release contains three parts with individually recorded hashes. Reassembly scripts exist for Windows and Unix-like systems and print the expected full archive SHA-256.

## Architecture rule

Moonwake Rest House should be a **room-capability adapter** over native mascot engines, not a replacement mascot engine.

A useful cross-engine contract should describe capabilities such as:

- idle/active state;
- locomotion and target positioning;
- room bounds;
- speech/balloon output;
- drag/throw behavior;
- context actions;
- furnishing interaction hooks;
- persistence ownership;
- spawn/despawn lifecycle;
- engine-specific state serialization;
- cancellation/interruption;
- swarm participation;
- capability gaps.

Each adapter should declare what it genuinely supports. Missing capabilities must degrade visibly rather than being faked through a generic animation path.

## Anti-regression rules

- Do not flatten ACS, Shimeji, WebMeji, and Petz into one generic sprite/animation engine.
- Do not replace native movement, speech, context-menu, persistence, or behavior graphs with room-local approximations.
- Do not restore the fake mascot simulator.
- Do not introduce viewport admission, mascot count caps, hidden off-screen suspension, or quality reduction as a performance shortcut.
- Preserve room and global-swarm ownership boundaries.
- A bundle-size improvement must preserve the same engine and interaction capability set.

## Proposed next verification layer

Add a deterministic **cross-engine room-interaction fixture**. One representative instance from each available engine should execute the same room-level sequence while using its native implementation:

1. spawn;
2. enter Moonwake Rest House;
3. move to a furnishing anchor;
4. perform an engine-native idle/interaction;
5. speak or expose its equivalent supported interaction;
6. drag/move when supported;
7. leave/re-enter;
8. persist/restart;
9. restore exact engine-owned state.

The fixture should record capability-by-capability outcomes rather than forcing all engines to pretend they implement the same internals.

## Acceptance test

- every representative engine is the real native engine instance;
- native animation/behavior/state APIs remain active;
- unsupported features report a truthful capability gap;
- room interactions do not corrupt global-swarm state;
- state survives full GameSync/browser restart where persistence is promised;
- no fake placeholder mascot path is invoked;
- full mascot availability is preserved;
- console/background/content-script errors are checked in the real extension runtime;
- loaded build/archive identity matches the verified candidate.

## Exact next action

Resolve the current source/runtime descendant of the 0.25.9 native-engine checkpoint, then run the cross-engine room-interaction fixture in the real GameSync browser runtime before changing the mascot bridge architecture.

## Evidence

- Live Mascot Tavern folder: https://drive.google.com/drive/folders/1OP7dZJbrGD4H0MdRzi7gjuI25KW0fqP-
- Verification: https://drive.google.com/file/d/1Y3kpuwq5kwqqSFQAdG9MRZhhCEN_DFEp/view
- Status manifest: https://drive.google.com/file/d/1eU9lIq1MYBu03Ify8uqqzoRXkS1ziqFM/view

## Wiki maintenance

Update this page when a mascot engine, room capability, bridge API, archive identity, performance figure, persistence contract, or real runtime verification changes. Preserve engine-specific behavior as first-class evidence.