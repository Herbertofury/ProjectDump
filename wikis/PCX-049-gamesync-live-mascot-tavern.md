# GameSync Live Mascot Tavern Wiki

**Project Constellation ID:** `PCX-049`  
**Status:** ACTIVE / TRACKED  
**Goal:** Run live mascot engines inside GameSync as real interactive systems.  
**Historical shipping authority:** GameSync `0.25.9` **Live Mascot Tavern - Native Engines** / Moonwake Rest House.  
**Current typed descendant authority:** `Herbertofury/GameSync-Next` `main` at `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`.  
**Current staged Petz correctness repair:** draft PR #10, exact observed head `2612396804b44399b7b23b4f32f21217325da79c`; open, mergeable, unmerged, and not current-product authority.

## Purpose and authority model

GameSync Live Mascot Tavern is the room-capability and social-space layer around GameSync's real mascot engines. The project must preserve the identity and behavior of each underlying engine rather than replacing ACS, Shimeji, WebMeji, Petz, or future mascot families with a generic room-local sprite simulator.

There are currently three evidence lanes that must remain distinct:

1. **GameSync 0.25.9 / Moonwake Rest House** is the strongest durable shipping/recovery proof for the completed native-engine tavern experience.
2. **GameSync Next current `main`** is the strongest current source authority for the typed Petz engine/bridge descendant and the surrounding next-generation mascot host.
3. **GameSync Next PR #10** is a staged Petz persistence repair proposal. Its code is useful implementation evidence, but it is not current-main behavior and must not be described as shipped until exact-head verification passes and the proposal is merged.

A newer proposal timestamp or branch head does not supersede either shipping or current-main authority by itself.

## Moonwake Rest House shipping baseline

The durable 0.25.9 verification records that the Mascot Room became **Moonwake Rest House**, a living mascot resting tavern connected to GameSync's real mascot registry and global swarm.

Recorded real engine families include:

- Clippy / ACS;
- Shimeji;
- WebMeji;
- Petz;
- future global-swarm engines through the same room-capability bridge model.

The verified design preserves engine-native behavior while adding room-aware roles, furnishing anchors, resting/social behaviors, and entry/exit integration. The fake mascot simulation and decorative stand-ins were removed rather than being retained as a compatibility fallback.

### Native behavior contract

The durable baseline explicitly preserves:

- animation lists and engine-native behavior graphs;
- native `moveTo` / `setPosition`-style movement paths where supported;
- speech and balloons;
- drag/context-menu behavior;
- spawn selection;
- persistence;
- global-swarm controls;
- room entry/exit without replacing the engine's own state machine.

A room feature is additive. It must never become a reason to flatten a mascot engine into a generic animation interface.

## Shipping archive identity

The durable 0.25.9 record identifies:

- archive: `GameSync-0.25.9-Live-Mascot-Tavern-Native-Engines-FULL.zip`;
- size: `247,583,122` bytes;
- SHA-256: `87c4380af9e5bf405dca67c07160086a79cb2e9e3f1381cc23120ffaac7678f4`.

The multipart release contains three parts with individually recorded hashes. Reassembly scripts exist for Windows and Unix-like systems and print the expected full archive SHA-256.

### Recorded validation

The durable shipping/recovery evidence records:

- ZIP CRC: pass;
- duplicate ZIP entries: zero;
- manifest entries: one;
- local reassembly byte match: true;
- real mascot-engine bridge: true;
- native `moveTo` preference: true;
- fake mascot simulation removed: true;
- no-cap contract: pass;
- entry controls: 264/264;
- static actions: 213/213;
- workspaces: 18/18;
- workspace actions: 54.

The managed Chromium extension-navigation gate was blocked by environment policy and is not counted as passed.

### Historical performance evidence

The same durable record reports:

- previous bundle: `4,926,116` bytes;
- current bundle: `4,214,259` bytes;
- bytes removed: `711,857`;
- reduction: `14.45%`.

That reduction came from separating duplicate/stale bundle work. It is not evidence for reducing mascot features, suspending hidden mascots, or culling room content.

## Current GameSync Next Petz descendant

Current `Herbertofury/GameSync-Next` `main` at `cd906ff0831bf7fc33b41fea31b6f0c004cc1562` contains the typed Petz stack:

```text
packages/petz-engine
packages/petz-compat
packages/petz-formats
packages/petz-bridge
```

`packages/petz-bridge/src/mascot-bridge.ts` explicitly identifies itself as the bridge between `PetzEngine` and the GameSync mascot system. The source states that this bridge is consumed by both the Opera-extension v1 path and Extension V2.

The current bridge maps real pet state into the mascot display contract and forwards native interactions such as:

- drag start/update/end;
- throw velocity;
- petting start/stop;
- engine-native event/sound handling;
- current sprite frame/state projection.

This is current project-owned source evidence, not an inferred architectural plan.

## Current-main Petz correctness defects

Current `main` still contains source-proven defects that prevent the Petz descendant from being treated as a fully qualified Moonwake Rest House successor.

### Restore path is not wired on `main`

Current-main `spawnPet()` loads saved data by `breedId`, detects an object, and then reaches a `TODO: restore from save` branch before spawning a fresh pet. The saved object is therefore not hydrated through the bridge on current `main`.

### Save/load identity does not match on `main`

Current-main reads using `breedId` but `destroy()` writes using the generated runtime `pet.id`. It also serializes the entire engine once per pet and saves that whole-engine snapshot under each runtime ID.

This creates two separate ownership problems:

1. the key used to write is not necessarily the key used to read;
2. a whole-engine snapshot is ambiguously duplicated under multiple per-pet runtime keys.

### Teardown does not await persistence on `main`

Current-main `destroy()` fires asynchronous `savePetData()` calls and only attaches `.catch(() => {})`. It returns without waiting for the host persistence operations to settle, so a browser/service-worker teardown can race durable storage.

### Fixed four-pet ceiling remains on `main`

`PetzMascotBridge` constructs `PetzEngine` with:

```text
maxPets: 4
```

The engine default also uses four pets and `spawnPet()` refuses another pet once the configured maximum is reached.

That is an architectural count ceiling unless explicitly converted into a user-configurable safety preference with a non-destructive complete path. It conflicts with the Live Mascot Tavern no-artificial-cap contract as currently implemented.

## Staged persistence repair: GameSync Next PR #10

Current draft PR #10 is **Fix Petz bridge persistence identity and restore path**.

Observed state:

- base: `main`;
- base SHA: `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`;
- branch: `automation/petz-bridge-persistence-20260818`;
- exact observed head: `2612396804b44399b7b23b4f32f21217325da79c`;
- state: open;
- draft: true;
- mergeable: true;
- merged: false.

This proposal must not be presented as current product behavior.

### What PR #10 materially fixes in source

The staged bridge adds a host-owned stable `persistenceId` and uses the same identity for load and save. It retains a legacy breed-key read fallback for historical data.

The staged engine/bridge also adds or uses:

- single-pet `serializePet(petId)`;
- additive `restorePet(save)` without clearing unrelated live pets;
- one runtime-pet-to-persistence-ID mapping per live pet;
- direct one-pet save compatibility;
- historical whole-engine `{ pets: [...] }` read compatibility when a matching breed record exists;
- corrupt/invalid-save diagnostics through optional host callbacks;
- fresh-spawn fallback when restore fails;
- mapping cleanup on pet removal;
- awaited asynchronous per-pet saves in `destroy()` through `Promise.all()`.

The staged source therefore directly addresses the current-main persistence-key mismatch, restore TODO, whole-engine-per-pet ownership problem, and teardown race.

### Exact staged behavior observed in source

The staged `spawnPet()`:

1. tries the host-owned stable `persistenceId`;
2. falls back to the historical `breedId` key when needed;
3. extracts a matching saved pet;
4. calls `restorePet()` when valid;
5. reports a host-visible persistence error when the payload is invalid or restoration fails;
6. falls back to fresh `spawnPet()`;
7. binds the live runtime `pet.id` to the host persistence identity.

The staged `destroy()`:

1. stops the simulation;
2. serializes each pet independently;
3. resolves that pet's stable persistence identity;
4. saves each pet independently;
5. reports individual save failures;
6. awaits all saves before returning.

### What PR #10 does **not** solve

The exact staged bridge still constructs `PetzEngine` with `maxPets: 4`.

Therefore PR #10 must not be described as closing the Live Mascot Tavern no-cap parity gap. Persistence correctness and mascot-count policy are separate acceptance items.

## PR #10 acceptance evidence and external blocker

The proposal contains an exact-source regression script, `scripts/petz/persistence-regression.mjs`, designed to transpile and exercise the actual staged engine/bridge source. The PR's maintained acceptance description covers:

- two same-breed stable persistence slots;
- exact identities;
- position/physics/action/motive restoration;
- additive second-pet restore;
- interaction after restore;
- historical whole-engine save compatibility;
- corrupt-save fallback;
- deliberately delayed asynchronous host save proving teardown remains pending until durable persistence completes;
- Petz engine/bridge typecheck and build;
- Extension V2 build;
- current GameSync parity regression/audit;
- exact-build Ferrum browser recovery/restart checks;
- integrity and secret scanning.

However, the current exact head has **not executed those full gates successfully**.

The PR records exact-head private checks that failed before executable verification steps were allocated, with `steps: null`. Those failures are infrastructure non-execution, not Petz product failures and not passes.

The public Ferrum recovery path can receive runners but currently stops at the explicit private GameSync read-token preflight before private candidate checkout. No historical test result should be promoted to exact-head acceptance.

## Building and checking the current typed descendant

The repository is an npm workspaces monorepo with a checked-in lockfile (`lockfileVersion: 3`). For a clean current-main checkout, preserve the lockfile and use a frozen install when qualifying a candidate:

```bash
npm ci
```

The Petz packages expose direct TypeScript gates:

```bash
npm --workspace packages/petz-engine run typecheck
npm --workspace packages/petz-engine run build
npm --workspace packages/petz-bridge run typecheck
npm --workspace packages/petz-bridge run build
```

The repository also exposes the current GameSync parity audit:

```bash
npm run audit:gamesync-parity
```

and an Opera Extension V2 verification path:

```bash
npm run verify:extension-v2:opera
```

Do not convert a source inspection, successful TypeScript build, or old Ferrum run into full Live Mascot Tavern acceptance. The exact loaded browser build and persistence/restart behavior still need to match the candidate being qualified.

## Cross-engine room architecture

Moonwake Rest House should remain a **room-capability adapter over native mascot engines**, not a replacement mascot engine.

A useful cross-engine capability contract should express at least:

- engine identity and version;
- idle/active state;
- native locomotion and target positioning;
- room bounds;
- native speech/balloon output where supported;
- drag/throw behavior;
- context actions;
- furnishing interaction hooks;
- persistence owner/key contract;
- spawn/despawn lifecycle;
- engine-specific serialization;
- cancellation/interruption;
- swarm participation;
- declared unsupported capabilities.

Each adapter should declare what it genuinely supports. Missing capability must remain a visible gap rather than being faked through a generic animation path.

## Deterministic cross-engine fixture

One representative instance from every available engine should execute the same room-level sequence while remaining on its native implementation:

1. spawn;
2. enter Moonwake Rest House;
3. move to a furnishing anchor;
4. perform an engine-native idle or furnishing interaction;
5. speak or expose the nearest genuinely supported interaction;
6. drag/move/throw when supported;
7. leave and re-enter;
8. persist;
9. terminate the browser/host fully;
10. restart;
11. restore exact engine-owned state;
12. rejoin the global swarm without duplication or state loss.

The fixture should record outcomes per capability instead of forcing every engine to implement the same internals.

### Petz-specific fixture requirements

For the current Petz descendant, include:

- two independent same-breed pets with stable host identities;
- save/load under the exact same persistence keys;
- position, physics, action, motives, personality/genetics/wardrobe, ancestry/generation, and lifecycle state restoration as supported by the current save model;
- legacy save compatibility;
- corrupt-save fallback with diagnostics;
- delayed persistence proving teardown awaits completion;
- full browser restart;
- no duplicate restored pets;
- no state bleed between same-breed pets;
- explicit count-policy test proving the room is not silently constrained by a hard architectural ceiling.

## Anti-regression rules

- Do not flatten ACS, Shimeji, WebMeji, and Petz into one generic sprite/animation engine.
- Do not replace native movement, speech, context-menu, persistence, or behavior graphs with room-local approximations.
- Do not restore the fake mascot simulator.
- Do not introduce viewport admission, hidden off-screen suspension, arbitrary mascot caps, or quality reduction as a performance shortcut.
- Preserve room and global-swarm ownership boundaries.
- Bundle-size improvements must preserve the same engine and interaction capability set.
- Persistence must have one explicit owner/key contract and must restore the exact promised engine state after a full restart.
- A configurable safety preference may exist, but it must not be confused with a hard architectural maximum or silently remove otherwise available mascots.
- Draft proposal behavior must remain labeled as staged until merged and exact-head acceptance passes.

## Troubleshooting

### A Petz pet always respawns fresh after restart

On current `main`, this is expected from the source defect: saved data is loaded but not restored through the bridge. Do not diagnose this as a content-pack problem before checking the bridge version.

For a PR #10 candidate, verify the host passes a stable `persistenceId`, the stored payload contains the expected breed, and host persistence diagnostics show no load/restore error.

### Two pets of the same breed overwrite each other

Current-main breed-key loading plus runtime-ID writing is not a safe same-breed multi-pet identity model. A qualified candidate needs separate host-owned persistence IDs and a restart test proving both pets survive independently.

### Pet state disappears during browser/service-worker shutdown

Current-main `destroy()` does not await asynchronous saves. On a candidate containing PR #10's staged repair, verify `destroy()` is awaited by the host and use a deliberately delayed persistence fixture to prove teardown does not complete early.

### A fifth pet cannot spawn

Current-main and the current PR #10 staged source both still construct the engine with `maxPets: 4`. This is a known unresolved policy/architecture gap, not evidence that four is a native Petz engine limit.

### Room behavior works but swarm state duplicates after restart

Treat room membership, engine persistence identity, and global-swarm registration as separate owners. The restart fixture must prove exactly one restored mascot instance per persistent identity and no duplicate registration.

## Acceptance test

A Live Mascot Tavern successor is qualified only when:

- every representative mascot is a real native engine instance;
- native animation/behavior/state APIs remain active;
- unsupported features report a truthful capability gap;
- room interactions do not corrupt global-swarm state;
- state survives a full GameSync/browser restart where persistence is promised;
- Petz bridge save/load identity matches exactly and restored data is actually applied;
- asynchronous persistence is durably complete before teardown finishes;
- two same-breed pets remain independently persistent;
- no hard artificial mascot-count ceiling removes otherwise supported mascots;
- no fake placeholder mascot path is invoked;
- full mascot availability remains intact;
- console/background/content-script errors are checked in the real extension runtime;
- the loaded build/archive identity matches the exact candidate under test;
- draft/branch-only behavior is not mislabeled as shipped.

## Exact next action

Keep PR #10 fail-closed until exact head `2612396804b44399b7b23b4f32f21217325da79c` actually executes and passes its Petz package, persistence-regression, host-build, parity, browser-restart, integrity, and security gates. Separately create a scoped follow-up for the still-unresolved `maxPets: 4` architectural ceiling, then qualify both fixes through the cross-engine Moonwake Rest House restart fixture before promoting the GameSync Next descendant as full Live Mascot Tavern parity.

## Evidence

- GameSync Next current main: https://github.com/Herbertofury/GameSync-Next
- Petz bridge on current main: https://github.com/Herbertofury/GameSync-Next/blob/main/packages/petz-bridge/src/mascot-bridge.ts
- Petz engine: https://github.com/Herbertofury/GameSync-Next/tree/main/packages/petz-engine
- Draft persistence repair PR #10: https://github.com/Herbertofury/GameSync-Next/pull/10
- Live Mascot Tavern Drive folder: https://drive.google.com/drive/folders/1OP7dZJbrGD4H0MdRzi7gjuI25KW0fqP-
- Historical verification: https://drive.google.com/file/d/1Y3kpuwq5kwqqSFQAdG9MRZhhCEN_DFEp/view
- Historical status manifest: https://drive.google.com/file/d/1eU9lIq1MYBu03Ify8uqqzoRXkS1ziqFM/view

## Wiki maintenance

Update this page when a mascot engine, room capability, bridge API, persistence identity, count-policy contract, PR #10 head/state, archive identity, performance figure, or real runtime verification changes. Preserve engine-specific behavior as first-class evidence and keep draft proposal state visibly separate from current-main/shipping authority.