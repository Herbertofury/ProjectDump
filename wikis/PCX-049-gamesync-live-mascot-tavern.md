# GameSync Live Mascot Tavern Wiki

**Project Constellation ID:** `PCX-049`  
**Status:** ACTIVE / TRACKED  
**Goal:** Run live mascot engines inside GameSync as real interactive systems.  
**Current verified line:** GameSync 0.25.9 Live Mascot Tavern - Native Engines, with a newer GameSync Next Petz bridge descendant requiring parity repair.

## Verified current state

The durable 0.25.9 verification records that the Mascot Room became **Moonwake Rest House**, a living mascot resting tavern connected to GameSync's real mascot registry and global swarm.

The implementation uses real engine instances rather than a generic mascot simulator. Recorded engine families include:

- Clippy / ACS
- Shimeji
- WebMeji
- Petz
- future global-swarm engines through the same bridge contract

The implementation preserves engine-native behavior while adding room-aware roles and furnishing interactions.

## Current GameSync Next descendant

Current `Herbertofury/GameSync-Next` `main` at `9e337c720f0180cffa577f140b181c699f0a1650` contains a real typed Petz integration path:

- `packages/petz-engine`
- `packages/petz-compat`
- `packages/petz-formats`
- `packages/petz-bridge`

`packages/petz-bridge/src/mascot-bridge.ts` explicitly states that it bridges `PetzEngine` into the GameSync mascot system and is consumed by both the Opera extension v1 path and Extension V2. It maps real pet state into the mascot display contract and forwards native drag, throw, and petting interactions into the engine.

This is stronger current source evidence than treating the 0.25.9 archive as the only implementation line. It also exposes concrete parity gaps that prevent the current descendant from being promoted as a fully verified successor yet.

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

## Current descendant parity gaps

The current Petz bridge contains three material source-backed gaps against the durable Moonwake Rest House contract.

### Artificial simultaneous-pet cap

`PetzMascotBridge` currently constructs `PetzEngine` with `maxPets: 4`. The engine's own `DEFAULT_ENGINE_CONFIG` also sets `maxPets: 4`, and `spawnPet()` refuses to create another pet when `pets.size >= maxPets`.

That is an explicit count cap and conflicts with this project's no-artificial-cap rule unless a real external/runtime limit is measured and documented. A fixed default may be useful as a user-configured policy, but it must not silently become the architectural maximum for the complete mascot system.

### Restore path is unfinished

`spawnPet()` currently calls `loadPetData(breedId)`, detects an object, and then leaves a `TODO: restore from save` branch before spawning a fresh pet. The underlying `PetzEngine` already exposes `restore(data)` and can rebuild pets from serialized state when the needed breed packs are loaded.

Therefore current source proves that persistence restoration is available in the engine but not wired end to end through this bridge path.

### Save/load identity mismatch

The bridge loads saved data using `breedId`, but `destroy()` saves by each runtime `pet.id`. It also serializes the entire engine for every pet and writes that same whole-engine snapshot repeatedly under different pet IDs.

This creates an identity/ownership mismatch: the next `spawnPet(name, breedId)` lookup is not guaranteed to find the data written during destruction, and one whole-engine snapshot should not be ambiguously owned by several pet IDs.

These are source-level findings. They are not proof that every other mascot engine shares the same defects, and they are not a reason to replace the native-engine architecture.

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
- Persistence must have one explicit owner/key contract and must restore the exact promised engine state after a full restart.
- A configurable safety preference may exist, but it must not be confused with a hard architectural maximum or silently remove already-available mascots.

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

For the current Petz descendant, add targeted bridge tests before the broader fixture:

1. define one stable persistence identity and ownership model;
2. prove a serialized engine/pet state is actually consumed by `restore()` after restart;
3. prove save and load use the same key contract;
4. remove the fixed four-pet architectural ceiling or convert it to an explicitly user-configurable/non-destructive policy with an uncapped/default-complete path;
5. prove both extension v1 and Extension V2 consume the corrected bridge without state loss.

## Acceptance test

- every representative engine is the real native engine instance;
- native animation/behavior/state APIs remain active;
- unsupported features report a truthful capability gap;
- room interactions do not corrupt global-swarm state;
- state survives full GameSync/browser restart where persistence is promised;
- Petz bridge save/load identity matches exactly and restored data is actually applied;
- no fixed artificial mascot-count ceiling removes otherwise supported mascots;
- no fake placeholder mascot path is invoked;
- full mascot availability is preserved;
- console/background/content-script errors are checked in the real extension runtime;
- loaded build/archive identity matches the verified candidate.

## Exact next action

Create a scoped current-main Petz bridge repair proposal that removes the fixed architectural `maxPets: 4` ceiling, defines one persistence identity/owner, and wires the existing engine `restore()` path through the mascot bridge. Add narrow unit/state tests first, then run the cross-engine room-interaction and full browser-restart fixture against both GameSync extension generations before merge.

## Evidence

- Current GameSync Next main: https://github.com/Herbertofury/GameSync-Next
- Current Petz mascot bridge: https://github.com/Herbertofury/GameSync-Next/blob/main/packages/petz-bridge/src/mascot-bridge.ts
- Current Petz engine: https://github.com/Herbertofury/GameSync-Next/blob/main/packages/petz-engine/src/engine.ts
- Current Petz engine config: https://github.com/Herbertofury/GameSync-Next/blob/main/packages/petz-engine/src/types.ts
- Live Mascot Tavern folder: https://drive.google.com/drive/folders/1OP7dZJbrGD4H0MdRzi7gjuI25KW0fqP-
- Verification: https://drive.google.com/file/d/1Y3kpuwq5kwqqSFQAdG9MRZhhCEN_DFEp/view
- Status manifest: https://drive.google.com/file/d/1eU9lIq1MYBu03Ify8uqqzoRXkS1ziqFM/view

## Wiki maintenance

Update this page when a mascot engine, room capability, bridge API, persistence identity, count-policy contract, archive identity, performance figure, or real runtime verification changes. Preserve engine-specific behavior as first-class evidence.