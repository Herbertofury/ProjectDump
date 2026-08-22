# PCX-061 - Petz Shared Core

**Project Constellation ID:** PCX-061
**Status:** ACTIVE / TRACKED
**Project goal:** preserve PF Magic Petz behavior in one shared core for GameSync hosts.
**Primary requirement:** one engine with adapters, preserved source/assets, and no flattening of Petz into ordinary mascot animation.
**Current strongest shared-core source:** `Herbertofury/GameSync-Next`, with dedicated typed `packages/petz-engine`, `packages/petz-compat`, `packages/petz-formats`, and `packages/petz-bridge` workspaces.
**Current GameSync Next main observed:** `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`.
**Current shipping parity baseline:** `Herbertofury/Gamesync` GameSync `0.6.3`, `main` observed at commit `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`.
**Active persistence repair:** draft [GameSync Next PR #10](https://github.com/Herbertofury/GameSync-Next/pull/10), current head `2612396804b44399b7b23b4f32f21217325da79c`, based on current `main`, remains unmerged and staging-only.
**Current implementation boundary:** current `main` still has the source-proven persistence defect tracked by [issue #9](https://github.com/Herbertofury/GameSync-Next/issues/9). PR #10 implements a preservation-first repair in source at exact head `2612396804b44399b7b23b4f32f21217325da79c`, but its fresh Petz verify run `32459020450` and Secret Scan run `32459020441` both failed before GitHub exposed executable job steps. Public Ferrum recovery infrastructure is healthy but currently stops at the explicit private GameSync read-token preflight, so the proposal remains unmerged and staging-only. Complete original PF Magic behavioral parity, merged and runtime-proven cross-restart persistence, complete use of every inventoried Petz resource, and end-to-end parity across shipping GameSync, Extension V2, and desktop are not yet proven.

## 1. Purpose and scope

Petz Shared Core is the reusable PF Magic Petz domain/runtime track for the wider GameSync and Mascot ecosystem. Its architectural rule is **one Petz behavior/runtime core with host adapters**, rather than separate browser, Extension V2, and desktop rewrites.

The source picture now has two important layers:

1. **GameSync Next typed shared core:** reusable simulation, compatibility, format parsing, save-state, custom-content, and mascot-bridge packages under `packages/petz-*`.
2. **Shipping GameSync parity baseline:** a substantial JavaScript Petz engine with routing, pack modules, Ballz rendering, extracted geometry, asset inventories, browser persistence, and real packaged extension resources.

The shipping source explicitly describes its Petz implementation as a **reimplementation-first Petz runtime**. The typed GameSync Next source goes further by separating domain behavior from host/rendering APIs. Neither statement should be interpreted as proof of perfect original-executable parity.

## 2. Relationship to other tracked projects

Petz Shared Core overlaps several Project Constellation tracks without being interchangeable with them:

- **PRJ-007 - PF Magic Petz Runtime Integration:** owns integration and rollout of the shared core into actual GameSync hosts. PCX-061 owns the reusable Petz domain/runtime boundary.
- **PRJ-005 - Mascot / Screenmate Platform:** larger umbrella host/runtime that can instantiate Petz alongside ACS, Shimeji, Webmeji, and generic mascot engines.
- **PCX-049 - GameSync Live Mascot Tavern:** user-facing GameSync host surface where live mascot engines can appear.
- **PCX-042 - GameSync Next:** now contains the strongest current reusable Petz architecture, not merely a future parity target.
- **Shipping GameSync:** remains the strongest user-facing browser parity baseline and the richest currently documented source of packaged Petz assets, Ballz geometry, and existing browser behavior.

Petz-specific motives, personality, breeds, actions, formats, Ballz geometry, physics, sounds, content packs, save state, and compatibility semantics must remain Petz-owned behavior. A generic sprite loop is not an acceptable substitute.

## 3. Current cross-host architecture

```mermaid
flowchart LR
 A[PF Magic originals / extracted source / mods] --> B[petz-formats]
 B --> C[Normalized breeds / pets / toys / clothing / scenes]
 D[petz-compat] --> E[Per-family compatibility rules]
 C --> F[petz-engine]
 E --> F
 F --> G[petz-bridge]
 G --> H[GameSync mascot contract]
 H --> I[Shipping GameSync browser host]
 H --> J[GameSync Next Extension V2]
 K[Shipping GameSync JS Petz runtime] --> L[Parity and resource baseline]
 L --> F
 L --> I
```

The key ownership rule is that parsing, family compatibility, simulation state, motives, personality, actions, physics, save data, and custom content belong in the shared Petz domain layer. Browser APIs, DOM rendering, extension storage, desktop windows, and host lifecycle belong at adapter boundaries.

### Typed shared-core packages

| Package | Verified role |
| --- | --- |
| `packages/petz-engine` | Platform-agnostic Petz simulation/domain core, state machine, physics, motives, personality, actions, save serialization/restore, breeds, content packs, custom content, and engine controller. |
| `packages/petz-compat` | Per-family compatibility packs for Dogz 1, Catz 1, Oddballz, Petz 2, Petz 3, Petz 4, Babyz, Petz 5, plus merged Mega compatibility. |
| `packages/petz-formats` | Readers/parsers/scanners for LNZ, breed files, pet saves/genetics, toys, clothing, scenes/environments, and source-content classification. |
| `packages/petz-bridge` | Adapter between `PetzEngine` and the GameSync mascot contract, including sprite/sound resolution, interaction mapping, simulation loop, state projection, and persistence callbacks. |

All four are private TypeScript workspace packages at version `0.1.0`. Each currently exposes `build` as `tsc --build` and `typecheck` as `tsc --noEmit`.

## 4. `@gamesync/petz-engine`

The typed engine is the current strongest reusable Petz core. Its public API exports:

- `PetzFamily` and `PetzCompatMode`;
- motive and personality models;
- semantic action and physics models;
- animations, breeds, toys, clothing, environments, save data, and content-pack types;
- custom breed, toy, clothing, scene, and bundle types;
- default motives, personality, physics, engine config, and known breeds;
- pure state-machine helpers;
- drag and petting interaction helpers;
- serialize/restore helpers;
- the `PetzEngine` controller.

### Supported family identifiers

The current typed model explicitly supports:

- `dogz1`
- `catz1`
- `oddballz`
- `petz2`
- `petz3`
- `petz4`
- `babyz`
- `petz5`

`PetzCompatMode` also supports `mega`.

### Motives

The typed engine defines six 0-100 motives:

- hunger
- happiness
- energy
- social
- fun
- comfort

This is the canonical typed motive vocabulary. The older shipping JavaScript runtime uses a different six-value vocabulary, documented later in this page. Cross-host parity work should define explicit migration/mapping instead of silently treating the two schemas as identical.

### Personality

The typed core models all 22 PF Magic-style personality fields:

- liveliness
- playfulness
- independence
- confidence
- naughtiness
- acrobaticness
- patience
- kindness
- nurturing
- finickiness
- intelligence
- messiness
- quirkiness
- insanity
- constitution
- metabolism
- dogginess
- love destiny
- fertility
- love loyalty
- libido
- offspring-sex tendency

The source records these as 0-100 values corresponding to the actual 22 hex-mapped personality positions in Petz data. It also defines the seven traits used by the community-standard unibreed personality reset.

### Typed action model

The typed action union includes locomotion, care, interaction, species behavior, breeding, and Oddballz-specific states:

`idle`, `walk`, `run`, `sit`, `sleep`, `eat`, `play`, `petting`, `pickup`, `thrown`, `fall`, `land`, `drag`, `toy_interact`, `groom`, `meow`, `bark`, `hiss`, `growl`, `purr`, `wag_tail`, `scratch`, `roll`, `jump`, `climb`, `arrive`, `leave`, `breed`, `nurse`, `bounce`, `zap`, `morph`, and `custom`.

This semantic action model is broader than the currently documented shipping JavaScript adapter vocabulary. Do not collapse one into the other without an explicit compatibility map.

### Typed physics

The typed default physics model currently records:

| Setting | Current typed default |
| --- | ---: |
| gravity | `980 px/s²` |
| friction | `0.85` |
| max fall speed | `600` |

Physics state also carries position, velocity, ground state, and left/right wall state. The shipping JavaScript runtime uses different constants, also preserved later in this page. Treat that difference as parity work, not documentation noise.

## 5. `@gamesync/petz-compat`

The compatibility package exports:

- `DOGZ1_COMPAT`
- `CATZ1_COMPAT`
- `ODDBALLZ_COMPAT`
- `PETZ2_COMPAT`
- `PETZ3_COMPAT`
- `PETZ4_COMPAT`
- `BABYZ_COMPAT`
- `PETZ5_COMPAT`
- `getCompatPack`
- `getAllCompatPacks`
- `buildMegaCompat`

This package is the correct home for family-specific differences that should not be hard-coded into one host UI. New host implementations should request the family compatibility pack instead of duplicating generation-specific behavior in browser or desktop adapters.

## 6. `@gamesync/petz-formats`

The formats package is the normalization boundary for original and community content. Its current public API includes:

### LNZ

- `parseLnz`
- cat and dog ball-name mappings
- Ballz/line/paint-ball/eyelid/whisker/texture/head-shot/project-ball data
- clothing adjustments and overrides
- fur/default-factor/sound-list data

### Breed files

- `readBreedFile`
- `buildSpriteBreedManifest`

### Content scanning

- `classifyFiles`
- `detectGameFamily`

### Toys

- `parseToyFile`
- `KNOWN_TOYS`

### Clothing

- `parseClothingFile`
- `KNOWN_CLOTHING`

### Scenes/environments

- `parseSceneFile`
- `KNOWN_SCENES`

### Pet save/genetics data

- `parsePetFile`
- `hasGeneticData`
- `getGeneration`
- default personality data
- ancestry and genetics types

A format parser proves the repository can inspect/normalize a format. It does not automatically prove every parsed field is used by the simulation or rendered in every host.

## 7. `@gamesync/petz-bridge`

`PetzMascotBridge` maps the shared Petz engine into the GameSync mascot contract. Its current-main source explicitly states that the file is consumed by both the shipping Opera extension and Extension V2.

Verified current-main responsibilities include:

- creating a `PetzEngine` with one selected compatibility family;
- resolving pack asset keys to display URLs;
- forwarding Petz sound events to the host sound callback;
- mapping Petz state into mascot display fields;
- running the simulation through `requestAnimationFrame`;
- capping per-frame delta time to 100 ms to avoid a spiral of death;
- forwarding drag and petting input to the engine;
- exposing the underlying engine and compatibility pack;
- invoking host callbacks for save/load operations.

### Current-main persistence defect

[GameSync Next issue #9](https://github.com/Herbertofury/GameSync-Next/issues/9) records two source-proven problems in current `main`:

1. `spawnPet()` loads saved data with `loadPetData(breedId)` but ignores the returned payload instead of restoring it;
2. `destroy()` serializes the whole engine and saves that payload under generated runtime `pet.id` keys, so later breed-key loading cannot find the same persisted identity.

That means the current-main bridge has persistence plumbing but does not provide a valid cross-restart restore path. Multiple pets of the same breed also need stable independent persistence identity rather than one implicit breed key.

### Draft PR #10 persistence repair

Draft [PR #10, Fix Petz bridge persistence identity and restore path](https://github.com/Herbertofury/GameSync-Next/pull/10), currently at head `2612396804b44399b7b23b4f32f21217325da79c` on top of current `main`, contains a source-level preservation-first repair. It remains unmerged and is not current product behavior.

The staged repair changes the shared core in several important ways:

- `PetzEngine.serializePet(petId)` persists one pet without converting every shutdown into a whole-engine save;
- `PetzEngine.restorePet(save)` restores one pet additively without clearing unrelated live pets;
- `PetzMascotBridge.spawnPet()` accepts an optional host-owned stable `persistenceId`, with the historical breed key retained as a compatibility default;
- reads and writes use the same stable persistence identity, with a legacy breed-key fallback;
- direct one-pet saves and historical whole-engine `{ pets: [...] }` saves remain readable when they contain the requested breed;
- optional `reportPersistenceError` diagnostics expose load, restore, and save failures to the host;
- live `pet.id -> persistenceId` mappings are removed when a pet is removed;
- `destroy()` becomes asynchronous, gathers all per-pet saves, reports individual failures, and does not resolve until every host persistence operation settles.

The staged save-state contract also preserves more runtime identity than the current-main bridge path: physics position/velocity, facing, action and action timers, animation/frame timing, drag/paused/asleep flags, ancestry/generation/offset identity, motives, personality, genetics, wardrobe, and other already-supported save data.

### Staged regression and verification contract

PR #10 adds `scripts/petz/persistence-regression.mjs` plus `.github/workflows/petz-persistence-verify.yml` to exercise the exact proposal source. The intended acceptance surface includes:

- two same-breed pets with distinct stable persistence slots;
- exact pet IDs and runtime state after a new bridge is created;
- non-destructive second-pet restore;
- post-restore drag and petting;
- legacy whole-engine save compatibility;
- corrupt-save fallback and host-visible diagnostics;
- a deliberately gated asynchronous host save proving `destroy()` stays pending until persistence is durable;
- Petz engine/bridge typecheck and build;
- Extension V2 build;
- parity regression/snapshot/audit;
- patch-integrity proof;
- exact-build Ferrum extension-host health, restart, identity, and diagnostics;
- Secret scan.

The exact current PR head is `2612396804b44399b7b23b4f32f21217325da79c`. Fresh private-repository checks on that head are **not product test results**: Petz persistence verify run `32459020450` / job `96701992871` and Secret Scan run `32459020441` / job `96701992684` both completed `failure` with `steps: null`, before any executable product-verification step ran.

A public recovery lane exists in Ferrum PR #62 at head `3e9e5371c03f4aac5be27c5e128a0cd60e1fa037`. Its runner-pool probe `32460964252`, registry freshness `32460964357`, Stack Playwright lock integrity `32460964247`, and Ferrum CI `32460964290` succeeded, proving the public runner path is healthy. The cross-repository Petz recovery matrix still stops at the explicit private GameSync read-token preflight before checkout, Node setup, lock regeneration, or candidate tests. This narrows the remaining acceptance blocker to private GameSync execution/read authorization; it does **not** convert source review or public infrastructure health into Petz acceptance. Keep PR #10 draft and unmerged until the exact current head actually executes and satisfies every gate.

### Current bridge environment boundary

The inspected current-main tick environment supplies real viewport/floor/wall dimensions, but uses placeholders for:

- `cursorX: 0`
- `cursorY: 0`
- `cursorNear: false`
- `nearbyToyId: null`

Host integration should feed real cursor and nearby-toy state before claiming those simulation inputs are wired end to end.

## 8. Shipping GameSync JavaScript Petz runtime

The current shipping `Herbertofury/Gamesync` repository remains essential because it contains the richest verified user-facing browser behavior and packaged Petz resources.

```mermaid
flowchart TD
 A[GameSync mascot request / imported pack] --> B[engine_router.js]
 B -->|engineOverride=petz or importType petz/pfmagic/oddballz| C[engine_petz.js]
 C --> D[PetzAdapter]
 C --> E[PetzCreature]
 E --> F[Motives + weighted AI]
 E --> G[Physics: gravity / drag / throw / bounce]
 E --> H[Animation + sound]
 E --> I{Renderer available?}
 I -->|Ballz geometry + skeletons| J[Canvas / Ballz renderer]
 I -->|Fallback / pack sprites| K[GIF/image renderer]
 L[Petz pack JS files] --> C
 M[breed-geometry-data.js] --> J
 N[default-skeletons.js] --> J
 O[app/assets/petz/**] --> L
 P[game-resource-catalog.json] --> Q[Source/resource inventory]
```

### Shipping core files

| File | Verified role |
| --- | --- |
| `app/content/mascot/engine_petz.js` | Dedicated PF Magic Petz runtime. Implements motive decay, weighted action selection, physics, dragging/throwing, petting, animation, sound, breed geometry lookup, creature lifecycle, and the Petz engine adapter. Exposes `window.__gsEnginePetz`. |
| `app/content/mascot/engine_router.js` | Detects Petz packs/overrides, lazy-loads `engine_petz.js`, creates creatures through the Petz engine, and supports engine snapshot/hot-swap behavior. |
| `app/Mascot_Engine.js` | Higher-level mascot host. Loads the Petz engine plus packs/geometry helpers and has Petz-specific creation/fallback paths. |
| `app/content/mascot/ballz-renderer.js` | Canvas/Ballz rendering support used when breed geometry and skeleton data are available. |
| `app/content/mascot/breed-geometry-data.js` | Large extracted breed geometry dataset consumed by the Petz engine. |
| `app/content/mascot/default-skeletons.js` | Skeleton/pose support used by Ballz rendering. |
| `app/content/mascot/anim-player.js` | Animation playback support used by the mascot/Petz stack. |
| `app/content/mascot/petz1-catz-pack.js` | Petz/Catz 1 pack definition. |
| `app/content/mascot/petz1-dogz-pack.js` | Dogz 1 pack definition. |
| `app/content/mascot/petz2-pack.js` | Petz 2 pack definition. |
| `app/content/mascot/petz3-catz-pack.js` | Petz 3 Catz/Dogz pack mapping real FunPack GIF/WAV resources into engine-consumable breed configs. |
| `app/content/mascot/petz4-pack.js` | Petz 4 pack definition. |
| `app/content/mascot/petz5-pack.js` | Petz 5 pack definition. |
| `app/content/mascot/oddballz-pack.js` | Oddballz pack definition. |
| `app/assets/petz/` | Packaged Petz resource tree exposed to the extension runtime. |
| `app/assets/petz/game-resource-catalog.json` | Generated inventory of preserved Petz/Oddballz resources. It is an evidence/index artifact, not proof that every entry is currently simulated. |
| `app/content/mascot/shared_commands.js` | Shared mascot command surface that Petz instances can join through the router/host. |
| `app/modules/mascot-pack/background/*` | Pack import, persistence, runtime, settings, messages, IndexedDB, memory, and session infrastructure used by the wider mascot system. |

## 9. Shipping engine routing and host contract

`engine_router.js` contains a dedicated `petz` engine entry:

- script: `content/mascot/engine_petz.js`
- expected global: `__gsEnginePetz`
- explicit `engineOverride: "petz"` routes to Petz
- import types `petz`, `pfmagic`, `pf-magic`, and `oddballz` route to Petz

The router can lazy-load the engine. On extension pages it injects engine scripts through DOM `<script>` elements. On ordinary web pages it first asks the background layer to inject the required engine scripts and falls back to DOM loading when necessary.

The router also provides a state-snapshot/hot-swap path that preserves the available position, velocity, facing, current action, animation frame, paused state, and scale when switching engines. Any typed/core adapter that replaces this path must preserve equivalent Petz-owned state rather than treating host/engine switching as a fresh spawn.

`Mascot_Engine.js` also contains a direct Petz creation path. When the selected engine resolves to `petz`, it uses `window.__gsEnginePetz`, resolves a Petz breed pack, creates the Petz instance at the selected or fallback position, primes mascot persistence, and registers the instance with shared commands.

## 10. Shipping JavaScript Petz API

The current `window.__gsEnginePetz` export includes:

- `create`
- `buildSpriteConfig`
- `getCreature(id)`
- `getAllCreatures()`
- `removeAll()`
- `registerPack`
- `getAvailablePacks`
- `getPack`
- `getBreed`
- `getAllBreeds`
- `PetzCreature`
- `PetzAdapter`
- `ACTION_WEIGHTS`
- `MOTIVE_DECAY`

The `PetzAdapter` is the shipping compatibility boundary presented to the broader engine/router system. Petz-specific methods include motive inspection and mutation (`getMotives()` and `setMotive(key, value)`) in addition to common creature/engine controls.

### Shipping native action surface

The shipping adapter declares actions covering:

`idle`, `walk`, `run`, `sit`, `sleep`, `eat`, `play`, `groom`, `meow`, `bark`, `purr`, `scratch`, `jump`, `roll`, `beg`, `headtilt`, `stretch`, `yawn`, `sniff`, `chase`, `pounce`, `wag`, `lick`, `hiss`, `scared`, `drag`, `pet`, and `fall`.

This is not identical to the typed action union. Maintain an explicit parity/migration ledger rather than relying on name similarity.

## 11. Shipping motives and autonomous behavior

The shipping JavaScript runtime tracks six motive dimensions on a 0-100 scale:

- hunger
- energy
- fun
- hygiene
- social
- fatigue

The implementation defines motive decay over time and weighted autonomous action selection. Action weights are motive-aware, so sleep, eat, play, groom, running, chasing, begging, and other activities are selected based on more than a generic random animation loop.

Selected actions also affect motives. Existing source examples include eating reducing hunger, sleeping reducing fatigue, play reducing the fun need while consuming energy, grooming reducing hygiene need, and movement/play actions changing energy/fun values.

### Motive-schema parity requirement

The typed core instead uses hunger, happiness, energy, social, fun, and comfort. `hygiene`/`fatigue` and `happiness`/`comfort` are not interchangeable by documentation alone. Migration between shipping and typed state must define and test the mapping.

## 12. Shipping physics and interaction model

Current shipping engine physics constants include:

| Setting | Current shipping value |
| --- | ---: |
| gravity | `900 px/s²` |
| terminal velocity | `800` |
| ground friction | `0.85` |
| throw multiplier | `1.6` |
| bounce coefficient | `0.3` |
| drag damping | `0.15` |

The runtime explicitly implements gravity, dragging, throwing, bouncing, petting, and action-driven motion. These are Petz runtime behaviors, not decorative CSS animation.

When changing or reconciling physics, verify at minimum:

1. drag starts and releases without losing the instance;
2. throw velocity is derived from the interaction rather than teleporting the pet;
3. gravity and terminal velocity remain bounded;
4. ground collision/bounce does not trap the creature outside the viewport;
5. petting remains distinguishable from dragging;
6. motive/action state survives the interaction;
7. state survives the supported router/bridge/persistence path;
8. typed and shipping constants differ only where the difference is intentional and evidence-backed.

## 13. Shipping rendering model

The shipping Petz engine supports two main rendering paths.

### Ballz/geometry path

If `window.PetzBallzRenderer` and `window.__gsPetzSkeletons` are available, the engine prefers a Canvas/Ballz-style path. It looks up breed geometry through `window.__gsPetzBreedGeometry`, using the pack family and breed. Breed-name normalization handles aliases and can fall back across Petz 5, Petz 4, Petz 3, Petz 2, and Oddballz geometry families.

This path preserves structured breed geometry instead of reducing every pet to a flat image.

### Pack sprite/GIF path

Pack definitions can also provide sprite/action arrays and sounds. `buildSpriteConfig()` normalizes a pack into the runtime action model, including FPS, scale, loop behavior, species, breed, sounds, and optional `ballzOnly` behavior.

### Rendering preservation rule

A missing geometry entry may use a verified fallback, but do not silently declare breed parity when the renderer is using a generic/default shape. Record the fallback and add a fixture for the affected breed.

The typed shared core deliberately does not own a rendering API. A host renderer should consume domain state without moving Petz simulation semantics into renderer-specific code.

## 14. Shipping content packs

The shipping repository contains separate pack modules for:

- Catz 1
- Dogz 1
- Petz 2
- Petz 3
- Petz 4
- Petz 5
- Oddballz

The Petz 3 pack is especially explicit about provenance: it maps **real PF Magic FunPack GIF assets and extracted WAV sounds** from ClipArt, Anims, and Sounds source material into breed definitions consumed by `engine_petz.js`.

The current Petz 3 pack source enumerates cat breeds including Orange Shorthair, Calico, Tabby, Persian, Siamese, Alley Cat, B&W Shorthair, Maine Coon, Chinchilla, and Russian Blue, plus dog breeds including Dalmatian, Chihuahua, Bulldog, Poodle, Scottish Terrier, Dachshund, Mutt, Labrador, and additional entries later in the file.

Do not infer complete original-game behavioral parity merely because a content pack exists. Pack presence proves content integration, not complete simulation fidelity.

## 15. Preserved resource inventory

`app/assets/petz/game-resource-catalog.json` is a generated source/resource inventory. Its current summary records:

- 6 Oddballz creatures
- 688 Oddballz WAV files
- 837 Oddballz NE resources
- 568 toys
- 553 clothing resources
- 59 environments
- 299 wallpapers
- 259 sounds

The asset tree also contains `catz`, `dogz`, `oddballz`, `petz2`, `petz3`, `petz4`, `petz5`, `sounds`, and `toyz` directories.

### Important boundary

An inventory entry means the resource was cataloged/preserved. It does **not** mean every toy, clothing item, environment, wallpaper, sound, or Oddballz resource has a working runtime interaction. The typed formats package can parse several of these content categories, but parsing still does not prove runtime use.

## 16. Manifest/runtime exposure in shipping GameSync

GameSync `0.6.3` exposes `assets/petz/**` as web-accessible resources. The manifest also exposes the mascot JS/bin/JSON resources needed by the engine stack. The extension runs as Manifest V3 with `background/background.js` as its module service worker.

The stable extension identity is pinned by the public `key` field in `app/manifest.json`. Preserve extension identity during Petz changes when testing upgrade/persistence behavior.

## 17. Development setup

### Shared typed core prerequisites

GameSync Next is an npm workspace monorepo. Install dependencies from the repository root:

```powershell
npm ci
```

Each Petz package currently has an explicit build and typecheck command:

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

### Important aggregate-build boundary

The current GameSync Next root `build:packages` script builds `schema`, `shared`, `engine`, `core`, `pixi-game`, and `ui`. It does **not** currently include the four Petz workspaces. A successful root `npm run build:packages` is therefore not proof that Petz packages compiled.

### Shipping GameSync prerequisites

Verified shipping tooling requires Node/npm and Vite.

From the canonical shipping extension working directory:

```powershell
npm ci
npm run dev
npm run build
```

`app/` is the canonical editable extension source. `dist/` is generated output. After source changes, rebuild; do not hand-edit `dist/` as the source of truth.

### Load in Opera GX

Load the generated absolute `dist` directory as the unpacked shipping extension. The shipping repository README identifies `dist/` as the only folder that should be loaded unpacked in Opera GX.

## 18. How to modify the shared core safely

### Add or change a family compatibility rule

1. Put family-specific compatibility behavior in `packages/petz-compat`, not in one host UI.
2. Keep family identifiers stable.
3. Update `getCompatPack`/Mega behavior only when the new rule has source evidence.
4. Build and typecheck `petz-engine`, `petz-compat`, and any dependent bridge/host.
5. Compare the change against the shipping browser baseline when it affects existing behavior.

### Add or change a format parser

1. Put normalization/parser behavior in `packages/petz-formats`.
2. Preserve raw source provenance and avoid destructive rewriting of originals.
3. Keep unknown fields or unsupported versions visible rather than silently discarding them.
4. Add deterministic fixtures for every newly supported file variant.
5. Verify parsed output can round-trip or map into the typed Petz model where the format supports it.

### Add or change a breed

For shipping GameSync:

1. identify the correct Petz family and verified source assets/geometry;
2. add or update the appropriate `petz*-pack.js` module;
3. give the breed a stable breed ID and correct `species`/`family`;
4. map only verified animation/sound resources;
5. ensure Ballz geometry resolves through `breed-geometry-data.js` or an intentional alias;
6. avoid generic fallback geometry unless explicitly marked;
7. build the extension and verify the breed appears through `getBreed`/`getAllBreeds` or the host picker;
8. spawn the exact breed and exercise idle, walk, interaction, drag/throw, petting, audio, and persistence/reload behavior.

For the typed core, represent the breed through the typed content-pack/breed model and keep rendering/resource resolution in the host adapter.

### Add an action

1. Define the semantic action in the typed Petz action/state model first when it is shared behavior.
2. Add compatibility constraints in `petz-compat` if the action is family-specific.
3. Map the action into shipping/V2 host adapters without changing its meaning.
4. Decide whether motives/personality affect selection or recovery.
5. Test direct invocation and autonomous selection separately.
6. Verify interruption/state transitions so the pet cannot become stuck.

### Change motive logic

Keep motive values bounded to 0-100. Because the shipping and typed motive schemas differ, update the migration/parity mapping explicitly. Validate decay over time, autonomous selection, action recovery, save/restore, and cross-host migration.

### Change physics

Treat physics constants as behavior, not styling. Test low/high-speed drag release, edge collisions, viewport resize, repeated throws, pause/resume, and state migration. Record any intentional difference between the typed defaults and shipping JavaScript constants.

### Add a new Petz-family pack

Use the typed family/content-pack model and the existing Petz registry instead of creating a parallel engine. Use stable family/breed IDs, document provenance, keep resource paths host-portable, and make renderer fallback decisions explicit.

## 19. Host adapter requirements

A host adapter is not complete because it can display a Petz image. It should prove creation, behavior, interaction, persistence, and state migration from the shared model.

Every host should preserve, or explicitly map:

- family/breed identity
- typed motives
- personality traits
- semantic Petz actions
- physics state
- pack/resource identity
- sound semantics
- save/persistence identifiers
- custom-content identity
- deterministic import/export where supported
- renderer-specific Ballz/skeleton state or an explicitly equivalent representation

### Shipping GameSync

Shipping GameSync already has a substantial JavaScript implementation and resource stack. Treat it as the current behavioral parity baseline, not as disposable legacy code.

### Extension V2

The typed bridge source explicitly says it is consumed by Extension V2. Source presence proves integration architecture, but this documentation pass does not claim a fresh end-to-end Extension V2 Petz qualification.

### Desktop

The typed core is designed to be renderer/API independent and its source comments describe browser-extension and desktop consumers. However, this pass did not verify a complete desktop Petz adapter/runtime flow. Treat desktop parity as open until exercised in the actual desktop host.

## 20. Verification and test strategy

### Current automated-command boundary

Current `main` still exposes `build` and `typecheck` for each typed Petz workspace but does not expose a dedicated Petz regression command in those package manifests, and the root aggregate package build omits the Petz workspaces.

Draft PR #10 adds a dedicated exact-source persistence regression and workflow. Because the PR remains unmerged, those new gates are **staging evidence**, not a current-main guarantee.

The shipping GameSync package has general development/build commands but no dedicated Petz test script identified in the current project documentation. A successful build is necessary but is not sufficient Petz runtime evidence.

### Required shared-core qualification matrix

| Area | Required proof |
| --- | --- |
| Typed build closure | All four `packages/petz-*` workspaces build and typecheck from a clean install. |
| Typed state machine | Motive decay/recovery, personality influence, semantic actions, physics, drag/pet interactions, serialize and restore behave deterministically under fixtures. |
| Compatibility | Dogz 1, Catz 1, Oddballz, Petz 2, Petz 3, Petz 4, Babyz, Petz 5, and Mega compatibility are exercised. |
| Formats | Representative LNZ, breed, pet, toy, clothing, scene, and content-scan fixtures parse without silent data loss. |
| Bridge lifecycle | Spawn, tick, drag, pet, sound, save, destroy, restore, and restart work through real host callbacks. |
| Persistence identity | Two same-breed pets retain distinct host-owned stable persistence IDs; restoring one pet never clears another. |
| Teardown durability | Bridge destruction does not resolve until all asynchronous host save operations have settled. |
| Legacy compatibility | Historical breed-key whole-engine saves remain readable where a matching pet record exists. |
| Corrupt-save behavior | Invalid saves fall back safely and expose host-visible diagnostics. |
| Environment | Real cursor and nearby-toy state reach the bridge tick environment. |
| Shipping routing | `engineOverride=petz` and Petz/PF Magic/Oddballz import types resolve to the shipping Petz engine. |
| Shipping pack discovery | Catz/Dogz/Petz2/Petz3/Petz4/Petz5/Oddballz packs register and report expected breeds. |
| Rendering | At least one sprite/GIF breed and one Ballz/geometry breed render correctly. |
| Interaction | Pet, drag, throw, collision, bounce, and viewport-edge behavior work. |
| Audio | Verified mapped sound actions play without blocking the state machine. |
| Persistence | Selected breed/instance and typed save state survive the supported reload/restart paths. |
| Cross-host parity | The same representative pet behaves equivalently across shipping GameSync, Extension V2, and desktop for the fields each host promises. |
| Resource packaging | Petz assets resolve from built artifacts, not only from source paths. |
| Errors | Missing geometry/sprite/sound/parser data fails visibly and safely rather than silently corrupting the pet. |

## 21. Troubleshooting

### Current-main Petz save data does not restore after restart

Check whether the tested build is current `main` or the unmerged PR #10 staging branch.

On current `main`, issue #9 remains valid: bridge reads use `breedId`, shutdown writes use generated `pet.id`, and loaded values are ignored. Do not debug host storage first when the loaded bridge is the known-defective current-main implementation.

On PR #10 staging, verify the host supplies a stable `persistenceId` when same-breed pets must remain distinct, that the same key is used for load and save, and that the exact changed build is loaded. The staged code also exposes optional persistence diagnostics for load/restore/save failures.

### Shutdown returns before Petz state is durably saved

Current-main `destroy()` fires asynchronous saves without awaiting durable completion. PR #10 changes `destroy()` to return `Promise<void>` and await all per-pet persistence operations. Until that repair is merged and executed through the real host, treat teardown persistence as an open correctness risk.

### Staged PR #10 looks correct but CI is red

Inspect workflow job steps before inferring a product failure. On exact head `2612396804b44399b7b23b4f32f21217325da79c`, Petz verify run `32459020450` / job `96701992871` and Secret Scan run `32459020441` / job `96701992684` failed with `steps: null`, so no Petz build, regression, browser, restart, integrity, or security command actually executed. Public Ferrum recovery jobs are healthy, but the cross-repository lane currently stops at the private GameSync read-token preflight. Treat both conditions as infrastructure/authorization evidence, not product pass/fail evidence.

### Cursor or toy-aware behavior never triggers through the typed bridge

The inspected current-main bridge environment uses placeholder cursor coordinates/proximity and `nearbyToyId: null`. Wire real host environment data before debugging the Petz state machine itself.

### Shipping Petz instance does not appear

Check, in order:

1. the pack/import resolves to `petz` in `engine_router.js`;
2. `content/mascot/engine_petz.js` is packaged and loadable;
3. `window.__gsEnginePetz` exists after engine loading;
4. the selected pack is registered;
5. the selected breed exists;
6. the resource URL resolves from the built extension;
7. the instance was not placed outside the viewport by stale persisted coordinates.

### Pet renders as a generic/default shape

The Ballz renderer may not have found exact breed geometry. Check family/breed IDs, normalization aliases, `breed-geometry-data.js`, and skeleton availability. Do not label the fallback as breed-accurate until exact geometry resolves.

### Pet uses static/GIF rendering instead of Ballz rendering

Verify `window.PetzBallzRenderer`, `window.__gsPetzSkeletons`, and breed geometry lookup. Sprite/GIF fallback can be valid for a pack, but the choice should be intentional and documented.

### Breed exists in assets but not in picker/runtime

Asset presence is not registration. Confirm the corresponding shipping pack module exports/registers the breed and that the engine discovers the pack. For the typed core, confirm the breed is present in the content pack/registry supplied to `PetzEngine`.

### Toy/clothing/environment exists in a catalog or parses but cannot be used

Inventory and parsing are not runtime implementation. Locate an actual simulation/host handler before claiming interaction support. If none exists, record it as preserved/parsed source material awaiting integration.

### Pet stops acting after interaction

Inspect current action duration/state transition, pause state, motive selection, drag release, and physics loop. Verify the adapter/bridge still reports a live pet and no invalid action mapping was introduced.

### Shipping Petz works in source but not built extension

Rebuild `dist/`, then verify the manifest's web-accessible Petz resources and actual generated paths. Do not load `app/` directly as the production extension.

## 22. Current verification boundaries

The following are **not** claimed complete by this documentation pass:

- perfect behavioral parity with every original PF Magic Petz release;
- exact reproduction of the original executable's hidden AI/state machine;
- complete runtime use of all 568 inventoried toys, 553 clothing resources, 59 environments, 299 wallpapers, 259 sounds, or 837 inventoried Oddballz NE resources;
- complete Petz 1 through Petz 5, Babyz, and Oddballz gameplay parity merely because typed compatibility/formats or shipping packs exist;
- a fresh real-Opera Petz end-to-end qualification during this documentation update;
- automatic Petz coverage through GameSync Next root `build:packages`;
- merged and current-main cross-restart persistence repair;
- exact-head execution of PR #10's Petz package, regression, Extension V2, parity, Ferrum, patch-integrity, and security gates;
- real cursor/toy-proximity input through the inspected typed bridge;
- fresh Extension V2 and desktop end-to-end Petz parity proof;
- proof that the historical local `C:\Users\Owner\Desktop\GameSync\PF Magic` tree and current GitHub packages are byte-for-byte the same lineage.

These gaps should drive the next verification work rather than being hidden behind a generic “implemented” status.

## 23. Contribution and preservation rules

When contributing to Petz Shared Core:

1. work from the newest verified shared Petz source, currently the GameSync Next `packages/petz-*` workspaces, while preserving shipping GameSync as parity evidence;
2. preserve original/extracted resource provenance and do not overwrite source material with generated derivatives;
3. keep Petz behavior in the Petz engine/domain layer and host-specific browser/desktop behavior in adapters;
4. keep format parsing in `petz-formats` and family differences in `petz-compat`;
5. preserve stable pack/breed/pet IDs once user state can reference them;
6. treat persistence identity as a host/shared-core contract and preserve independent same-breed pets;
7. do not substitute generic mascot behavior for motives, personality, Ballz geometry, Petz actions, or pack semantics;
8. add runtime proof for every newly advertised action/control;
9. document typed-vs-shipping schema differences instead of silently normalizing them;
10. keep inventory/parser facts separate from implemented-runtime claims;
11. verify both workspace-specific typed builds and the real built host runtime;
12. preserve `dist/` as generated shipping output from `app/`;
13. update this wiki when engine API, compatibility coverage, format coverage, asset lineage, bridge behavior, host parity, persistence, build commands, or verification status materially changes.

## 24. Next documentation and engineering checkpoint

The highest-value next checkpoint is now **execute and qualify the staged persistence repair without weakening its acceptance surface**, not another source-discovery pass:

1. keep PR #10 draft and unmerged until its exact current head actually receives a runner and executes all required steps;
2. require Petz engine/bridge typecheck and build plus the exact-source persistence regression, including two same-breed slots, additive restore, runtime state, legacy save compatibility, corrupt-save diagnostics, and awaited async teardown;
3. require the affected Extension V2 build, current parity regression/snapshot/audit, patch integrity, exact-build Ferrum runtime/restart/identity/diagnostics, and Secret scan;
4. after successful staging proof, recreate the coherent repair from then-current `main` on the required fresh bug branch and rerun every affected gate before merge;
5. after merge, prove a real host restart loads the changed build and restores the same pet identity/state through the host storage path;
6. feed real cursor and nearby-toy state into the bridge environment;
7. keep Petz workspaces in an explicit aggregate or dedicated required build/test lane;
8. run representative Catz, Dogz, and Oddballz scenarios through shipping GameSync and Extension V2, with motive/action/physics/save-state parity evidence;
9. qualify desktop only after a real desktop adapter path is identified and exercised;
10. preserve exact commit/artifact identity and restart evidence for every host;
11. reconcile the historical local PF Magic source tree against current GitHub package provenance when that source becomes readable.

Until those checks pass, GameSync Next remains the strongest **shared-core source**, shipping GameSync remains the strongest **user-facing browser parity and resource baseline**, and PR #10 remains a **staging repair**, not released product behavior.
