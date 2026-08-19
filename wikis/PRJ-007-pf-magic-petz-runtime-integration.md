# PRJ-007 - PF Magic Petz Runtime Integration

**Project Constellation ID:** PRJ-007    
**Status:** ACTIVE GameSync / Mascot integration track    
**Goal:** keep one PF Magic Petz behavior/runtime core and integrate it through GameSync hosts without flattening Petz into ordinary mascot animation.    
**Historical rollout intent:** GameSync shipping extension -> GameSync Next Extension V2 -> desktop host.    
**Current strongest source evidence:** `Herbertofury/GameSync-Next` contains a typed, platform-agnostic Petz core plus compatibility, format and mascot-bridge packages; `Herbertofury/Gamesync` remains the current shipping JavaScript extension and parity baseline.    
**Current integration blocker:** [GameSync Next issue #9](https://github.com/Herbertofury/GameSync-Next/issues/9) remains present on current `main` `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`. Draft [PR #10](https://github.com/Herbertofury/GameSync-Next/pull/10) now stages a concrete stable-identity/additive-restore repair on branch `automation/petz-bridge-persistence-20260818`, but the PR is still open, draft and unmerged. GitHub currently reports head `1b8ad1abb3c01065e03a6780d67db9e74ef11e71`; exact-head Petz and Secret Scan jobs still fail before any workflow steps execute, so cross-restart persistence is not yet accepted on `main`.    
**Important boundary:** source now proves a real cross-host Petz architecture exists in GameSync Next, but this documentation pass does not claim complete original PF Magic behavioral parity or a freshly exercised end-to-end Petz flow in every host.

## 1. What this project owns

PRJ-007 is the **integration and rollout project** for PF Magic Petz across GameSync. It is related to, but not the same as, `PCX-061 - Petz Shared Core`.

- **PCX-061** owns the reusable Petz domain/runtime boundary.  
- **PRJ-007** owns getting that core into the actual GameSync hosts with preserved behavior, assets, persistence, interaction and compatibility.  
- **PRJ-005** is the larger Mascot / Screenmate umbrella that hosts Petz alongside ACS, Shimeji and other mascot engines.  
- **PCX-042** is the typed GameSync Next platform that now contains the strongest shared-core implementation evidence.

The architectural rule remains: **one Petz core, host adapters around it**. A browser-only engine, a second unrelated desktop implementation, or a generic mascot sprite loop is not a valid substitute for cross-host Petz integration.

## 2. Current source resolution

### GameSync Next

`Herbertofury/GameSync-Next` is the strongest current source for the reusable Petz architecture. The monorepo explicitly combines Extension V2, desktop/server hosts and shared packages, while retaining the current JavaScript GameSync extension as its parity baseline.

The current `packages/` tree includes four dedicated Petz packages:

| Package | Role |  
| --- | --- |  
| `packages/petz-engine` | Platform-agnostic simulation/domain core. |  
| `packages/petz-compat` | Per-game compatibility packs and merged Mega mode. |  
| `packages/petz-formats` | Readers/parsers/scanners for Petz source and mod content formats. |  
| `packages/petz-bridge` | Adapter between `PetzEngine` and the GameSync mascot contract. |

All four are private TypeScript workspace packages at version `0.1.0` with explicit `build` and `typecheck` scripts.

### Shipping GameSync

`Herbertofury/Gamesync` remains the current JavaScript extension parity baseline. Its canonical editable source is `app/`, and its generated production extension is `dist/`. The shipping mascot host already recognizes PF Magic presets such as classic Catz, Dogz and Oddballz and contains a substantial browser-side Petz implementation and packaged resource tree.

### Historical PF Magic source

Project continuity records preserve the historical local source location:

`C:\\Users\\Owner\\Desktop\\GameSync\\PF Magic`

That path is important provenance, but it is not directly readable through the connected GitHub/Drive evidence used for this pass. Do not claim byte-for-byte identity between that local tree and the current GitHub packages until the local source is reconciled and hashed.

## 3. Current architecture

```mermaid  
flowchart LR  
    A[PF Magic originals / extracted source / mods] --> B[petz-formats]  
    B --> C[Normalized breeds / pets / toys / clothing / scenes]  
    D[petz-compat] --> E[Per-family physics / AI / features]  
    C --> F[petz-engine]  
    E --> F  
    F --> G[petz-bridge]  
    G --> H[GameSync mascot contract]  
    H --> I[Shipping GameSync browser host]  
    H --> J[GameSync Next Extension V2]  
    H --> K[GameSync Next desktop host]  
```

The most important separation is that parsing/compatibility/domain behavior is not supposed to live inside one UI host. Rendering, browser APIs, storage and host lifecycle belong at adapter boundaries.

## 4. `@gamesync/petz-engine`

`packages/petz-engine` is the typed shared runtime. Its public API exports:

- Petz family and compatibility types;  
- motives and personality models;  
- action, physics, animation and breed types;  
- toys, clothing and environments;  
- save data and custom-content bundle types;  
- default motives, personality, physics and engine configuration;  
- the pure pet state machine;  
- drag and petting interaction functions;  
- serialize/restore helpers;  
- the `PetzEngine` controller.

### Supported family identifiers

The current type system explicitly supports:

- `dogz1`  
- `catz1`  
- `oddballz`  
- `petz2`  
- `petz3`  
- `petz4`  
- `babyz`  
- `petz5`

A `mega` compatibility mode is also defined for merged behavior.

### Motives

The typed engine currently models six 0-100 motives:

- hunger  
- happiness  
- energy  
- social  
- fun  
- comfort

The pure state machine decays these motives over time and applies action-specific recovery. Examples currently implemented include eating restoring hunger, sleeping restoring energy, play/toy interaction restoring fun, petting restoring happiness/social, and grooming restoring comfort.

### Personality

The current model contains 22 PF Magic-style personality traits rather than a single generic personality flag. The traits include liveliness, playfulness, independence, confidence, naughtiness, acrobaticness, patience, kindness, nurturing, finickiness, intelligence, messiness, quirkiness, insanity, constitution, metabolism, dogginess, love destiny, fertility, love loyalty, libido and offspring-sex tendency.

The package also records the seven traits that the community-standard unibreed personality fix resets to 50.

### Action model

The typed action union covers core locomotion and interaction plus species/family behavior, including:

`idle`, `walk`, `run`, `sit`, `sleep`, `eat`, `play`, `petting`, `pickup`, `thrown`, `fall`, `land`, `drag`, `toy_interact`, `groom`, `meow`, `bark`, `hiss`, `growl`, `purr`, `wag_tail`, `scratch`, `roll`, `jump`, `climb`, `arrive`, `leave`, `breed`, `nurse`, `bounce`, `zap`, `morph`, and `custom`.

This semantic action surface should remain stable across hosts. Host code may map it to different renderers, but it should not erase the meaning of the action.

## 5. Pet state machine

`packages/petz-engine/src/pet-state.ts` is intentionally pure logic: no DOM, no renderer and no platform-specific storage.

A pet instance owns:

- stable instance/name/breed/compat identity;  
- current action, elapsed time and action duration;  
- animation/frame state;  
- physics and facing;  
- six motives;  
- the 22-trait personality record;  
- age and interaction timestamps;  
- wardrobe;  
- genetics;  
- dragging, paused and asleep flags.

### Tick order

The current tick path performs, in order:

1. age advancement;  
2. motive decay when not dragging;  
3. physics when not dragging;  
4. action-timer transition;  
5. animation-frame advancement and per-frame velocity updates.

The action selector is motive- and personality-aware. For example, low energy increases sit/sleep weighting, low fun increases play weighting, species controls cat/dog vocal actions, and low comfort increases grooming weight.

### Physics

The shared state machine applies gravity, velocity, ground collision, wall collision/bounce and ground friction. Physics is part of domain behavior, not merely a CSS/display concern.

## 6. `PetzEngine` controller

`packages/petz-engine/src/engine.ts` coordinates pets and content packs without depending on a specific UI host.

Verified responsibilities include:

- loading/unloading content packs;  
- registering breeds, toys, clothing and environments;  
- spawning/removing/querying pets;  
- enforcing `maxPets`;  
- advancing all pets through `tick()`;  
- forwarding drag and petting interactions;  
- serializing engine/pet state;  
- restoring pet state after required breed packs are loaded;  
- exposing and updating engine configuration;  
- loading/unloading custom content bundles.

### Custom content

The engine has explicit conversion paths for custom breeds, toys, clothing and scenes. Custom content is gated by `moddingEnabled` and registered into the same engine maps rather than a separate fake-preview path.

## 7. `@gamesync/petz-compat`

`petz-compat` captures per-game behavioral differences so one engine can run family-specific modes instead of hard-coding a single Petz release.

Each compatibility pack records:

- physics constants;  
- AI timing;  
- motive decay multipliers;  
- available species;  
- base frame timing;  
- breeding and clothing support;  
- save-format identity;  
- playscene/toy-closet/hexing/genexing flags;  
- LNZ format generation;  
- data-folder convention;  
- breed-file extension;  
- Add Clothing / Flat Clothing support;  
- unibreed compatibility;  
- official breed IDs.

Current registered packs cover Dogz 1, Catz 1, Oddballz, Petz 2, Petz 3, Petz 4, Babyz and Petz 5.

### Mega mode

`buildMegaCompat()` creates a merged `Mega Petz (All Games)` profile using Petz 5 as the technical base, averaged physics/AI timing and the combined breed list. Treat Mega mode as a deliberate cross-version mode, not evidence that every original title behaves identically.

## 8. `@gamesync/petz-formats`

The format package is the input/recovery layer for authentic Petz content. Its current source tree contains dedicated modules for:

- `breed-reader.ts`  
- `lnz-parser.ts`  
- `pet-file-parser.ts`  
- `toy-parser.ts`  
- `clothing-parser.ts`  
- `scene-parser.ts`  
- `content-scanner.ts`

This separation matters. Parsing original or modded content should normalize into typed Petz data before the engine or UI consumes it. Do not bury format parsing inside a browser component.

### Modification rule

When extending a format parser:

1. preserve the original bytes/source artifact as evidence;  
2. parse into a typed intermediate structure;  
3. distinguish unknown/unsupported fields from zero/default values;  
4. add deterministic fixtures for each format family;  
5. keep parser failures actionable and non-destructive;  
6. do not silently coerce one Petz generation into another compatibility mode.

## 9. `@gamesync/petz-bridge`

`packages/petz-bridge/src/mascot-bridge.ts` is the cross-host integration boundary. Its own source states that it is consumed by both the shipping Opera extension and Extension V2.

The bridge:

- constructs `PetzEngine` using the pack family;  
- loads the content pack;  
- resolves asset keys through host callbacks;  
- maps Petz events to host audio;  
- starts/stops a `requestAnimationFrame` simulation loop;  
- caps a frame delta at 100 ms to reduce spiral-of-death behavior;  
- exposes mascot-compatible state for every pet;  
- forwards drag and petting interactions;  
- exposes the underlying engine and compatibility pack.

### Host callback contract

A host must provide:

- `resolveAssetUrl(assetKey)`  
- `playSound(soundUrl)`  
- `savePetData(petId, data)`  
- `loadPetData(petId)`

The mascot-facing state includes instance ID/name, pack identity, sprite URL, x/y, facing, action, drag state, scale and horizontal flip.

### Current main persistence limitation

Current GameSync Next `main` still calls `loadPetData()` when spawning while leaving the restore branch unfinished, and its shutdown path writes under generated runtime pet identity rather than the same stable identity used for loading. Therefore **save plumbing exists on main, but bridge-level cross-restart persistence is still incomplete**. Do not treat the draft repair branch as shipping behavior until it is fully executed, accepted and merged.

### Source-proven persistence identity defect

The current source contains a second persistence problem beyond the unfinished restore branch. `spawnPet()` calls `loadPetData(breedId)`, while `destroy()` iterates the current pets and calls `savePetData(pet.id, data)`. Those are different identities: a breed identifier is used for the read path and a generated pet instance identifier is used for the write path.

The same shutdown loop calls `this.engine.serialize()` for every pet before saving, so the data handed to each per-pet key is currently the whole engine snapshot rather than an explicitly scoped single-pet snapshot.

This is tracked in [GameSync Next issue #9](https://github.com/Herbertofury/GameSync-Next/issues/9). The source-proven defects are:

1. a later spawn cannot discover a save written under a generated `pet.id` by reading under `breedId`;  
2. even when `loadPetData()` returns an object, that returned state is ignored because the restore branch is still a TODO;  
3. the current API shape does not by itself provide a stable persistence identity for two pets of the same breed across restarts.

The preservation-first repair contract is to introduce an explicit stable persistence identity at the bridge/host boundary and add a non-destructive single-pet restore path to `PetzEngine`. Whole-engine restore for each spawn would be unsafe because restoring one pet must not clear or replace already-running pets.

Minimum acceptance for the repair:

- spawn a pet, mutate motives/position/action, save/destroy, construct a new bridge, and restore the same state;  
- persist two pets of the same breed independently;  
- restoring a second pet does not clear the first;  
- missing or corrupt saves fall back to a fresh spawn with a visible/traceable host error path where appropriate;  
- drag, petting and simulation continue after restore;  
- Extension V2 and every shipping host consuming the bridge perform restart proof against the changed build;  
- `petz-engine`, `petz-bridge`, and affected host build/typecheck gates pass;  
- the runtime proves the loaded artifact is the changed build rather than stale output.

Do not add a second host-only persistence system as a workaround. The shared bridge contract should become internally consistent so every consuming host receives the same persistence semantics.

### Staged persistence repair on draft PR #10

Draft [GameSync Next PR #10](https://github.com/Herbertofury/GameSync-Next/pull/10) is the current concrete repair lane. It is **staging evidence, not merged product behavior**. GitHub reports the PR as open, draft, mergeable, based on `main` `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`, with current head `1b8ad1abb3c01065e03a6780d67db9e74ef11e71` and nine changed files.

The current proposal source verifies these repair mechanics:

- `PetzEngine.serializePet(petId)` persists exactly one pet without mutating engine state;
- `PetzEngine.restorePet(save)` restores one pet additively and preserves unrelated live pets;
- `PetzMascotBridge.spawnPet()` accepts a host-owned stable `persistenceId`, defaulting to the historical breed key for compatibility;
- reads and writes use the same stable persistence identity, with a legacy breed-key fallback;
- direct one-pet saves and historical whole-engine `{ pets: [...] }` saves remain readable when a matching breed exists;
- restored runtime state includes position, velocity, facing, action/timers, animation/frame state, drag/paused/asleep flags, ancestry, generation and offset identity in addition to motives/personality/genetics/wardrobe/lifecycle fields;
- invalid or mismatched saves report through optional host persistence diagnostics and fall back to a fresh spawn;
- live `pet.id -> persistenceId` mappings are removed when pets are removed;
- `destroy()` is asynchronous and awaits every per-pet `savePetData()` operation before it resolves, preventing teardown from outrunning durable persistence.

The current PR also contains `scripts/petz/persistence-regression.mjs`, which transpiles and exercises the actual proposal engine/bridge sources rather than a mock implementation. Its coverage includes two same-breed stable slots, exact saved IDs, x/y/physics/action/motive restore, additive second-pet restore, post-restore drag/petting, legacy saves, corrupt-save fallback, and a deliberately gated asynchronous host save proving `destroy()` remains pending until persistence settles.

#### Exact-head acceptance wiring

The branch's Petz verification workflow requires:

1. current-main ancestry;
2. clean `npm ci` installation;
3. Petz engine and bridge typecheck/build;
4. the exact-source persistence regression;
5. Extension V2 build;
6. current parity regression, current-Gamesync snapshot and parity audit;
7. patch-integrity checks;
8. exact-build Ferrum extension-host worker recovery, restart, identity and diagnostic proof;
9. Secret Scan.

The branch has also accumulated explicit Ferrum acceptance workflows for fixed verified checkpoints plus a `petz-ferrum-latest-current.yml` lane that resolves the newest **durably verified** Ferrum product from Ferrum's `.agents-memory` state, checks its exact product/tree/workflow identity, installs it with `npm ci`, runs Ferrum's own tests, then exercises the freshly built GameSync Next extension with service-worker termination/recovery and full restart proof.

Ferrum evolution run 39 is the newest verified checkpoint that this current lane was updated to recognize before the PR head above. Run 39 merged deterministic `package-lock.json` plus frozen `npm ci` installs as Ferrum product `5ebbf1ffaee53dfe7ef0c8bb36f8526c8e1b7a95`, with tested proposal `28cc49d4c21bed28e8a002c24b82230c1bfff34d`, tree `122a312792f621ac14031f2c25c9edf3b20e89b9`, and all seven recorded verification workflows successful, including Ferrum CI `32217425220`. The later Ferrum `main` commit `94e58b90956fc48eef2ba5692f7832b9151c5a5d` pins CI to exact Node `24.19.0`; treat a newer Ferrum product as accepted by the Petz lane only when Ferrum's durable state records it as verified.

#### Current execution boundary

For current PR head `1b8ad1abb3c01065e03a6780d67db9e74ef11e71`, Petz persistence run [32223490382](https://github.com/Herbertofury/GameSync-Next/actions/runs/32223490382) and Secret Scan run [32223490469](https://github.com/Herbertofury/GameSync-Next/actions/runs/32223490469) both ended in failure with no workflow-step payload. The Petz job reports no steps and its Ferrum follow-up was skipped; the Gitleaks job likewise reports no steps. This is evidence that the private hosted-runner allocation blocker remains active, not evidence that the Petz code or regression failed after execution.

Keep PR #10 draft and unmerged until an exact current head actually executes the full Petz, parity, Ferrum, security and integrity surface. After that proof, follow the repository's stated promotion rule rather than merging solely from source inspection.

### Current environment limitation

The bridge currently constructs tick-environment cursor fields with `cursorX = 0`, `cursorY = 0`, `cursorNear = false`, and `nearbyToyId = null`. Host integration for live cursor proximity and nearby-toy detection therefore needs verification before those AI behaviors can be considered fully connected through this bridge.

## 10. Relationship to the shipping JavaScript Petz runtime

Shipping GameSync already has Petz-aware mascot presets and a browser implementation. GameSync Next is not supposed to replace that behavior by assumption. Its own repository defines the current JavaScript extension as the user-facing parity baseline and provides a parity-audit workflow.

Migration should therefore be treated as a ledger:

| Behavior | Shipping GameSync | Typed Petz packages | Host proof required |  
| --- | --- | --- | --- |  
| family/breed identity | implemented source exists | typed | compare exact IDs and mappings |  
| motives | Petz-specific runtime | typed six-motive model | long-running behavior comparison |  
| AI/actions | Petz-specific runtime | typed action/state machine | representative Catz/Dogz/Oddballz traces |  
| physics | browser runtime | platform-agnostic physics | drag/throw/fall/edge parity |  
| formats | preserved resources/packs | dedicated parser package | fixture corpus |  
| persistence | browser mascot infrastructure | main still has identity mismatch/ignored restore; draft PR #10 stages stable identity, additive restore and awaited teardown saves | exact-head multi-pet restart proof before merge |  
| rendering | sprite/GIF and Ballz paths | renderer-neutral state | host renderer parity |  
| audio | packaged resources | event/callback contract | actual host playback |  
| custom content | pack/resource paths | typed custom bundle support | import and reload proof |

## 11. Build and typecheck commands

### Prerequisites

Use the canonical `Herbertofury/GameSync-Next` checkout with Node/npm and the repository lockfile.

```powershell  
npm ci  
```

### Build the Petz packages explicitly

The current root `build:packages` script builds schema/shared/engine/core/pixi-game/ui and does **not** list the Petz workspaces. Until that is deliberately changed and verified, build/typecheck the Petz packages explicitly:

```powershell  
npm --workspace packages/petz-engine run build  
npm --workspace packages/petz-engine run typecheck

npm --workspace packages/petz-compat run build  
npm --workspace packages/petz-compat run typecheck

npm --workspace packages/petz-formats run build  
npm --workspace packages/petz-formats run typecheck

npm --workspace packages/petz-bridge run build  
npm --workspace packages/petz-bridge run typecheck  
```

Recommended dependency order for build diagnosis is engine -> compat -> formats -> bridge. `petz-compat` depends on `petz-engine`; `petz-bridge` depends on both `petz-engine` and `petz-compat`.

### Whole-platform verification

The GameSync Next repository also defines the broader parity and Extension V2 verification path:

```powershell  
npm run audit:gamesync-parity  
npm --workspace apps/extension-v2 run build  
npm --workspace apps/extension-v2 run lint  
npm --workspace apps/extension-v2 run typecheck:room  
npm --workspace apps/extension-v2 run verify:same-id-upgrade  
node scripts/verify-extension-v2-opera.js  
```

These checks are useful platform gates, but none is a substitute for a Petz-specific runtime test unless the Petz scenario is actually exercised.

### Draft PR #10 exact-source verification

For the current persistence-repair branch, the repository-owned acceptance sequence includes the actual Petz regression in addition to package and platform gates:

```powershell
npm ci
npm --workspace packages/petz-engine run typecheck
npm --workspace packages/petz-engine run build
npm --workspace packages/petz-bridge run typecheck
npm --workspace packages/petz-bridge run build
node --test scripts/petz/persistence-regression.mjs
npm --workspace apps/extension-v2 run build
node --test scripts/audit-gamesync-parity.test.mjs
node scripts/prepare-gamesync-parity-snapshot.mjs
npm run audit:gamesync-parity
```

The workflow supplies the exact current Gamesync snapshot path to `audit:gamesync-parity`; use the repository workflow as the command authority when reproducing that lane. A local green regression is necessary evidence, but the branch still requires its changed-build Ferrum restart/identity/diagnostic proof and security/integrity gates before promotion.

## 12. How to extend the integration

### Add a new Petz family/version

1. Add or extend the family type only when the compatibility boundary truly differs.  
2. Create the compatibility pack with verified physics/AI/format/features.  
3. Extend format parsing only where the source format requires it.  
4. Add breeds/content as typed pack data.  
5. Run engine/compat/formats/bridge build and typecheck.  
6. Add host adapter coverage.  
7. Compare behavior against the shipping/reference implementation or original-game evidence.

### Add a breed

1. Preserve stable family and breed identity.  
2. Parse or author the breed into `PetzBreed` without host-only fields.  
3. Keep animations/sounds referenced by asset keys.  
4. Verify the content pack registers it.  
5. Spawn through `PetzEngine` directly.  
6. Spawn through `PetzMascotBridge`.  
7. Verify the actual host renderer and audio path.  
8. Verify persistence after the bridge restore path is complete.

### Add a host

A new host adapter must provide real asset resolution, sound playback, persistence and a frame/tick lifecycle. It should map Petz state into the host without duplicating Petz domain logic.

Minimum proof for a new host:

- create a pet from a real pack;  
- render at least one cat, dog and Oddballz creature;  
- pet, drag and throw;  
- observe motive-driven autonomous action changes;  
- play mapped audio;  
- save, restart/reload and restore;  
- preserve family/breed/instance identity;  
- exercise at least one parsed/custom content fixture;  
- record errors for missing assets/formats instead of silently substituting unrelated content.

## 13. Testing strategy

Current `main` Petz workspace package manifests expose `build` and `typecheck` rather than a package-local Petz test script. Draft PR #10 adds a repository-level exact-source regression at `scripts/petz/persistence-regression.mjs` and wires it into dedicated Actions acceptance. Until that work is merged, treat it as staging proof and continue to reject compilation-only acceptance.

A serious Petz regression suite should cover:

### Pure engine tests

- motive decay bounds and action recovery;  
- AI weighting for low energy/fun/social/comfort;  
- species-specific vocal behavior;  
- action priority and interruption;  
- physics edge/ground behavior;  
- drag/throw/petting transitions;  
- serialize/restore round trip;  
- max-pet enforcement;  
- pack load/unload;  
- custom bundle load/unload.

### Compatibility tests

- every family resolves to the intended compatibility pack;  
- breed IDs and feature flags remain stable;  
- Mega mode combines without mutating source packs;  
- format/feature differences do not leak between families.

### Format fixtures

- representative LNZ files;  
- breed files;  
- `.pet` saves;  
- toys;  
- clothing;  
- scenes;  
- intentionally malformed/truncated inputs;  
- community/modded samples with known expected output.

### Bridge/runtime tests

- RAF start/stop and delta cap;  
- asset resolution;  
- sound event forwarding;  
- state mapping to the mascot contract;  
- drag and pet forwarding;  
- stable-key save/restore round trip through the bridge;  
- two same-breed pets persisting independently;  
- non-destructive restoration that does not clear already-running pets;  
- missing/corrupt save fallback behavior;  
- live cursor/toy environment integration once wired;  
- Extension V2 and desktop host parity.

## 14. Troubleshooting

### Petz package compiles alone but disappears in the app

Check whether the host actually imports `@gamesync/petz-bridge` or another Petz package. Workspace presence does not prove runtime wiring. Then verify the host build includes the package and that no old browser-only runtime is being exercised instead.

### `petz-bridge` build fails after an engine change

Build/typecheck `petz-engine` first, then `petz-compat`, then the bridge. Confirm exported type names and action/state contracts still match.

### Pet appears but never reacts to cursor/toys

The current typed bridge uses placeholder cursor/toy environment values. Confirm the host is supplying live environment data before debugging AI as if the domain state machine were receiving those signals.

### Pet is saved but not restored after restart

First prove which build is actually loaded. On current `main`, inspect the persistence key and restore implementation: the source-proven issue #9 path reads by breed identity, writes by generated runtime identity, and does not hydrate the returned save. On draft PR #10, verify the host supplies or deliberately accepts the stable `persistenceId`, inspect host-visible persistence diagnostics, and confirm teardown awaits `destroy()`. Do not add a second persistence layer around either path.

### Two same-breed pets overwrite, disappear, or restore incorrectly

Do not key persistence only by breed. Each persistent pet needs a stable identity that survives restart and remains distinct from another pet of the same breed. Regression-test two same-breed pets and verify restoring the second does not clear the first.

### Correct breed exists but wrong game behavior is used

Inspect the pack family and `getCompatPack(pack.family)`. Do not fall back to a generic or Mega profile when exact per-version behavior is expected.

### A source/mod file is present but cannot load

Start in `petz-formats`: determine whether the file is recognized, parsed and normalized. Do not patch the UI to read a format directly as a workaround.

### Whole `npm run build` passes but Petz changes are broken

The root `build:packages` script currently omits the Petz packages. Run their explicit workspace build/typecheck commands and then run host-specific Petz scenarios.

## 15. Verified behavior versus unresolved work

### Verified from current source

- a typed platform-agnostic Petz engine exists;  
- the engine models multiple pets, packs, motives, 22 personality traits, actions, physics, save data and custom content;  
- per-game compatibility packs exist for Dogz 1, Catz 1, Oddballz, Petz 2, Petz 3, Petz 4, Babyz and Petz 5;  
- a Mega compatibility profile exists;  
- dedicated Petz format readers/parsers/scanners exist;  
- a typed mascot bridge exists and states it is consumed by shipping Opera GameSync and Extension V2;  
- GameSync Next contains Extension V2 and desktop hosts in the same monorepo;  
- the shipping JavaScript extension remains the parity baseline;  
- current GameSync Next `main` still has the source-proven persistence failure: load and save identities differ, and returned loaded state is ignored;  
- draft PR #10 contains a source-inspected repair with stable host-owned persistence IDs, additive single-pet restore, legacy-save compatibility, persistence diagnostics, per-pet serialization and awaited asynchronous teardown saves;  
- the PR's exact-source persistence regression and Ferrum acceptance workflows are present, but the private Actions runner has not executed the current head's acceptance steps.

### Still unresolved or incomplete

- complete original PF Magic behavioral parity across every supported game;  
- byte-level reconciliation against the historical local `PF Magic` source tree;  
- dedicated automated Petz test suites in the current Petz package manifests;  
- automatic inclusion of Petz workspaces in the current root `build:packages` command;  
- [GameSync Next issue #9](https://github.com/Herbertofury/GameSync-Next/issues/9) remains unresolved on `main`; draft [PR #10](https://github.com/Herbertofury/GameSync-Next/pull/10) stages the repair but is unmerged and unaccepted;  
- live cursor/toy environment data in the inspected bridge implementation;  
- fresh real-browser qualification of the typed bridge;  
- fresh desktop runtime qualification;  
- proof that every preserved original/mod resource is represented by a working interaction.

## 16. Current next checkpoint

The highest-value next engineering/documentation checkpoint is to turn the typed Petz packages into a **provable cross-host parity lane**, starting with the source-proven persistence blocker:

1. execute draft PR #10's exact current head through Petz package typecheck/build and the exact-source persistence regression;  
2. execute changed-build Ferrum worker-recovery/restart/identity/diagnostic proof plus Secret Scan and patch-integrity gates;  
3. only after those gates pass, promote the coherent stable-identity/additive-restore repair through the repository's required fresh-branch/current-main workflow;  
4. prove two same-breed pets persist independently and restoring one never clears the other in real host storage across restart;  
5. extend the dedicated regression beyond persistence into engine/compat/formats coverage;  
6. feed real cursor/toy environment data through the bridge;  
7. make the intended root build/test pipeline include the Petz packages or add a documented Petz aggregate command;  
8. run representative Catz, Dogz and Oddballz scenarios in shipping GameSync, Extension V2 and desktop and record a behavior/parity ledger with exact build identities;  
9. reconcile the historical `PF Magic` source tree when it becomes accessible and preserve hashes/provenance.

Do not declare the rollout complete until the same stable Petz identities, core state and user interactions survive real host use and restart rather than merely compiling.

## Recovery checkpoint - Petz persistence repair

> Historical staging checkpoint. The exact head and workflow evidence in this subsection are superseded by the current PR #10 state recorded below.

The previously source-proven persistence defect is now under an active concrete repair rather than remaining only documented. GitHub canonical source is draft GameSync-Next PR #10, branch `automation/petz-bridge-persistence-20260818`, exact head `98f826b0e88340ef0d91264f726491ae02a2c192`, directly based on `main` `9e337c720f0180cffa577f140b181c699f0a1650` and 6 commits ahead / 0 behind.

Current repair scope is exactly five files: `.github/workflows/petz-persistence-verify.yml`, `packages/petz-engine/src/engine.ts`, `packages/petz-engine/src/pet-state.ts`, `packages/petz-bridge/src/mascot-bridge.ts`, and `scripts/petz/persistence-regression.mjs`.

The repair now provides host-owned stable persistence IDs, legacy breed-key fallback, direct one-pet saves, additive single-pet restore that does not clear unrelated live pets, same-breed independent slots, host-visible persistence error reporting, and runtime-state persistence for physics/position/velocity, facing, action timers, animation state, drag/paused/asleep flags, ancestry, generation and offset identity in addition to the existing motives/personality/genetics/wardrobe/lifecycle data.

A dedicated exact-source regression transpiles and exercises the actual proposal engine and bridge sources and requires: two same-breed independent slots, exact saved pet IDs, runtime x/y/action/physics restore, second restore preserving the first pet, drag/petting after restore, historical whole-engine save compatibility, and corrupt-save fallback with a visible restore diagnostic. The dedicated workflow also requires clean install, Petz engine and bridge typecheck/build, Extension V2 build, and patch integrity.

Exact-head execution remains externally blocked before code execution. Petz persistence verify run `32157288265`, job `95777443369`, and Secret scan run `32157288283`, job `95777443304`, both completed with no workflow step payload. These zero-step results are infrastructure evidence only and are not counted as product failures or passes. The established private GitHub Actions account payment/spending-limit condition remains the full-fidelity execution blocker, so blind reruns are not used as acceptance evidence.

Issue #9 and PR #10 remain open. Merge/recovery completion still requires the exact head to execute package build/typecheck, the runtime regression, affected Extension V2 build, real restart persistence with changed-build identity, applicable Ferrum exact-build runtime acceptance, Secret Scan, and patch integrity.

## Recovery checkpoint - Ferrum run 37 acceptance refresh

> Historical acceptance checkpoint. Ferrum run 37 remains valid provenance, but the Petz branch now resolves newer durably verified Ferrum state and has advanced beyond this exact head.

The stale Petz acceptance dependency on Ferrum run 36 has been repaired forward without changing or weakening the Petz persistence implementation. Canonical staging remains GameSync-Next PR #10 on branch `automation/petz-bridge-persistence-20260818`; exact recovery head is now `72669096280904eb0f210d49d3a3e3163f42b106`, based on current GameSync-Next `main` `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`.

The new `.github/workflows/petz-ferrum-run37-current.yml` preserves clean install, Petz engine/bridge typecheck and build, the exact-source persistence regression, Extension V2 build, parity regression/current-Gamesync snapshot audit, patch integrity, exact-build Ferrum service-worker termination/recovery, full browser restart, stable extension identity, console/service-worker diagnostics, and evidence upload. The obsolete run-36 acceptance workflow was removed after the run-37 workflow was committed.

Current verified Ferrum provenance is run 37: product `17b5260d6f18710e45f6b4e154ca77da5c2bbb82`, exact tested proposal `2e4ec3e0f867189dc2495c0fdb0b2d56be17d562`, exact tested/product tree `3561dfc8b8b3392ef3ec75f3a6de0d30802e34b2`, full Ferrum CI `32211204897` success, and evidence-index CI `32211204902` success. The evidence-index artifact is `9350979798`, 5,368 bytes, SHA-256 `3be2e85975c3e68f8f0753ee4d04398183d1475b4dde11ac27ee941c57fbbd3e`, covering 11 required artifacts with zero missing artifacts and provider/download digest equality.

A recovery retry of the prior Petz exact-head job again ended as a zero-step private-runner failure, so the known GameSync private GitHub Actions hosted-runner allocation blocker remains. The refreshed branch must still actually execute the run-37 Petz/Ferrum/security surface before promotion; no zero-step result is treated as product proof.

## Current recovery checkpoint - PR #10 head and Ferrum run 39

As of the latest verified repository metadata in this documentation pass:

- GameSync Next `main`: `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`;
- draft PR: [#10 Fix Petz bridge persistence identity and restore path](https://github.com/Herbertofury/GameSync-Next/pull/10);
- branch: `automation/petz-bridge-persistence-20260818`;
- current GitHub PR head: `1b8ad1abb3c01065e03a6780d67db9e74ef11e71`;
- PR state: open, draft, mergeable, unmerged;
- changed scope now includes nine files: the Petz engine/bridge/save regression, the main persistence workflow, and four Ferrum acceptance workflows;
- current exact-head Petz verification: [32223490382](https://github.com/Herbertofury/GameSync-Next/actions/runs/32223490382), failure before step execution;
- current exact-head Secret Scan: [32223490469](https://github.com/Herbertofury/GameSync-Next/actions/runs/32223490469), failure before step execution;
- Ferrum follow-up job on the failed Petz run: skipped because its prerequisite job never executed successfully.

The latest PR-head change specifically updates the dynamic Ferrum acceptance lane to recognize newer durable Ferrum evolution-proof shapes and uses `npm ci` for Ferrum's own frozen dependency install. That matters because Ferrum run 39 moved the verified browser/app acceptance toolchain to a committed lockfile plus frozen `npm ci` installation, while rejecting npm caching after measured Linux/Windows trials did not produce a reliable end-to-end gain.

This checkpoint changes the documentation state, not the shipping product state: issue #9 remains a real defect on `main`, and PR #10 remains a staged repair until its exact current head executes and passes the full acceptance surface. Zero-step private-runner failures are retained as infrastructure evidence and are not relabeled as product failures or passes.
