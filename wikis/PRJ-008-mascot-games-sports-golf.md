# PRJ-008 - Mascot Games / Sports and Golf Flagship

## Status and canonical evidence

**Project Constellation ID:** PRJ-008
**Tracked name:** Mascot Games / sports and Golf flagship
**Current documentation status:** ACTIVE implementation track with a verified shipping runtime
**Strongest verified implementation host:** [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync)
**Verified shipping baseline:** GameSync `0.6.3`, `main`, observed at commit `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`
**Canonical editable source root:** `app/`
**Generated production extension:** `dist/`

Project Constellation historically described this track through `mascotgames_master_agent_ordered_wxt_react_vite_v2_aligned_playable_contract_glorious_sports_golf_flagship.md`. That durable plan required Golf as the flagship, real playable sports loops, and popup/panel/full-view support aligned with the newer mascot stack.

Current project-owned source materially changes that picture. Shipping GameSync now contains a substantial mascot-game runtime with shared physics/rendering/progression systems and many playable game modes. However, **Golf is not present in the verified current game-launch allowlist and no Golf implementation was resolved in the current shared mascot-game source tree**. The historical Golf requirement therefore remains an unresolved product goal rather than verified shipping behavior.

This page documents the executable mascot-game layer that exists now and keeps the Golf requirement clearly separated from current proof.

## Product role

PRJ-008 is the **gameplay layer built on top of the Mascot / Screenmate Platform**, not the general mascot engine itself.

Its responsibilities currently include:

- starting mascot games in the active browser tab;
- loading only approved game scripts into the content-script world;
- providing shared canvas, input, physics, audio, particles, presentation, mascot-art, challenge, modifier, progression, loot, social, skin, and studio services;
- hosting individual sports, arcade, puzzle, action, survival, and casual game modes;
- preserving mascot identity and authored mascot artwork inside game experiences;
- keeping game presentation and character choice persistent per game;
- connecting game outcomes to inventory, currencies, relationships, challenges, unlocks, and career-like progression systems.

The historical project label emphasizes sports and Golf, but the current executable scope is broader and should be treated as a mascot arcade/sports framework until Golf is actually restored or implemented.

## Architecture

```text
GameSync UI / game launcher
 |
 | GS_START_GAME { game }
 v
background mascot-game-handler.js
 |
 | validates game id
 | resolves active last-focused tab
 v
active tab content script
 |
 | GS_START_GAME
 v
game overlay / requested game mode
 |
 +--> shared/mascot-games/game-core.js
 +--> shared/mascot-games/game-mascot-runtime.js
 +--> shared/mascot-games/game-openworld*.js
 +--> shared progression / challenge / modifier / unlock modules
 +--> content/<game>/<Mode>.js or shared game implementation
 |
 v
real mascot pack runtime + persistent local/browser state
```

A second controlled path supports dynamic game-script injection:

```text
content script -> GS_INJECT_GAME_SCRIPTS
 -> background allowlist validation
 -> chrome.scripting.executeScript(...)
```

The injection path is intentionally allowlisted. A requested filename that is not in the hardcoded list is discarded rather than executed.

## Important source files and modules

| Path | Verified responsibility |
| --- | --- |
| `app/modules/mascot-pack/background/mascot-game-handler.js` | Background message contract for game launch, script injection, inventory, social state, fishing, aquarium layouts, skins, Mascot Studio and related gameplay services. |
| `app/shared/mascot-games/game-core.js` | Shared canvas, input, physics, particles, rendering, audio hooks, native-refresh animation loop, 2D/3D presentation and optional webpage-ground presentation. |
| `app/shared/mascot-games/game-mascot-runtime.js` | Reuses the real Shimeji mascot runtime so games can draw authored mascot frames rather than replacing mascots with generic procedural characters. |
| `app/shared/mascot-games/game-openworld.js` | Large shared open-world/game bridge used by the mascot game layer. |
| `app/shared/mascot-games/game-openworld-3d.js` | Shared 3D presentation/runtime support. |
| `app/shared/mascot-games/game-challenges.js` | Deterministic daily challenges, weekly boss goals, streaks, local leaderboard state and challenge history. |
| `app/shared/mascot-games/game-modifiers.js` | Shared game modifiers and difficulty presets such as low gravity, slippery physics, giant/tiny mascots, turbo, one-hit KO, double points and chaos mode. |
| `app/shared/mascot-games/game-unlocks.js` | Persistent unlockables, loadouts, victory dances, titles, emotes and perks driven by levels, challenges and per-game careers. |
| `app/shared/mascot-games/mascot-loot.js` | Shared gameplay loot/progression integration. |
| `app/shared/mascot-games/mascot-social.js` | Shared mascot relationship/social state. |
| `app/shared/mascot-games/mascot-skins.js` | Shared skin integration. |
| `app/shared/mascot-games/mascot-studio.js` | Shared Mascot Studio integration for game use. |
| `app/content/mascot/game_compat.js` | Compatibility bridge between game modes and live mascot instances. |
| `app/content/mascot/game-overlay.js` | Shared game overlay used by individual modes. |
| `app/content/<game>/...Mode.js` | Individual game implementations where the mode is not implemented in the shared directory. |

## Current verified game registry

The current `GS_START_GAME` background contract accepts these game IDs:

1. `pinball`
2. `bowling`
3. `fishing`
4. `smash`
5. `survivors`
6. `racing`
7. `tennis`
8. `hideseek`
9. `pool`
10. `brickball`
11. `fruitninja`
12. `popcorn`
13. `alienshooter`
14. `slingshot`
15. `stackattack`
16. `whack`
17. `endlessrunner`
18. `rhythmtap`
19. `airhockey`
20. `volleyball`
21. `towerdefense`
22. `matchmerge`
23. `chess`

This is the authoritative current launch allowlist for the inspected shipping baseline. Do not add a game to documentation merely because an old plan named it. A new mode is not part of the verified runtime until it is wired through the launch and injection paths and exercised in the real extension.

### Historical Golf requirement

The preserved PRJ-008 plan names Golf as the flagship. In the current source inspected for this wiki:

- `golf` is not in the `GS_START_GAME` valid-game set;
- the inspected `app/shared/mascot-games` tree does not contain a Golf module;
- the current background script-injection allowlist does not contain a Golf mode.

Therefore the correct current status is **Golf requirement preserved, shipping Golf implementation not verified**.

## Game examples verified from current source

### Bowling

`app/content/bowling/BowlingMode.js` implements a real mascot bowling mode rather than a decorative screen. Current source includes:

- mascots used as bowling pins in a triangle formation;
- a player-aimed bowling ball;
- collisions that can fling live mascot instances;
- a 60 Hz fixed physics step;
- pin friction, pin gravity, ball speed, gutters and restitution;
- ten-frame bowling structure with two rolls per frame;
- strike, spare, gutter, collision and fling sound effects;
- particles and floating score feedback;
- temporary hiding/pausing of a mascot DOM node while it is physically flung, followed by restoration when it lands;
- use of the shared game overlay to draw mascot artwork.

This is strong evidence of a real playable loop in the shipping source. It is still not a substitute for a live Opera GX qualification run.

### Tennis

`app/content/tennis/TennisMode.js` implements a substantially deeper sports mode. Verified current source includes:

- a 3D-style ball state using x/y/z coordinates;
- spin, curve, bounce and shadow behavior;
- seven shot categories: flat, topspin, slice, lob, drop, smash and serve;
- deuce, advantage, game, set and best-of-three match scoring;
- match-point slow motion;
- court bounce marks;
- rally streak handling;
- player and adaptive AI state;
- stadium/crowd audio and celebration effects;
- live mascot discovery through the shared mascot compatibility bridge.

Tennis is currently better evidence of the project's sports direction than the unresolved Golf requirement.

## Shared presentation runtime

`game-core.js` is explicitly dt-based and uses `requestAnimationFrame` rather than imposing an artificial FPS cap.

Each game can persist a presentation state using keys derived from:

```text
gsMascotGamePresentation:<gameId>
gsMascotGamePresentation:<gameId>:camera
gsMascotGamePresentation:<gameId>:ground
```

Verified presentation choices include:

- 2D mode;
- 3D mode;
- first-person or third-person camera state in 3D mode;
- synthetic ground;
- webpage-ground mode.

Webpage-ground mode can capture the visible non-extension tab as a JPEG and use it as the game ground/reference presentation. The inspected implementation requests JPEG quality 72 and treats its captured ground as stale after 15 seconds. It intentionally avoids capturing GameSync's own extension URL.

Presentation settings are local state. If a mode appears stuck in an unexpected presentation, inspect these per-game localStorage keys before changing code.

## Real mascot artwork inside games

The game layer does not need to flatten mascots into placeholder circles or generic sprites.

`game-mascot-runtime.js` bridges to `window.__gsMascotGameOpenWorld`, discovers owned Shimeji packs, loads the selected pack's runtime, creates an animator, updates action/facing state and calls the real pack runtime's drawing function.

Per-game mascot selection persists under:

```text
gsMascotGameCharacter:<gameId>
```

The runtime exposes:

- `ensureRuntime()`
- `discoverCharacters()`
- `getSelectedCharacter()`
- `setSelectedCharacter()`
- `draw()`
- `reset()`

This is an important architecture rule for future work: **new game modes should reuse authentic mascot pack/runtime behavior instead of replacing it with a disconnected generic sprite system.**

## Challenge system

`game-challenges.js` stores state in:

```text
chrome.storage.local["gsGameChallengesV1"]
```

Verified behavior includes:

- three deterministic daily challenges;
- one deterministic weekly boss challenge;
- daily streak state;
- challenge history;
- local leaderboard entries;
- challenge XP tracking;
- seeded generation based on the current date/week rather than a required server;
- score, survival, play-count, win, combo, streak and modifier challenges;
- multi-game challenges;
- weekly goals such as total score, unique games, total wins, daily streaks and best combo.

The challenge module's current internal game registry covers the broad arcade/sports set, though its list is not identical to the background launch set. For example, the inspected challenge registry stops at `matchmerge` while `GS_START_GAME` also accepts `chess`. Treat this as a maintenance point: shared registries should be kept synchronized deliberately rather than assumed to match.

## Game modifiers and difficulty presets

`game-modifiers.js` stores state in:

```text
chrome.storage.local["gsGameModifiersV1"]
```

Verified built-in modifier categories include:

- physics: low gravity, high gravity, slippery, bouncy;
- scale: giant mascots, tiny mascots;
- speed: turbo speed, slow motion;
- difficulty: one-hit KO, shield start, mirrored controls;
- scoring: double points, no-points Zen mode;
- compound chaos mode;
- visual modifiers such as neon glow, retro mode and ghost/invisible mascots.

Verified presets are `chill`, `normal`, `spicy`, `extreme` and `chaos`.

Games should read modifier parameters through the shared modifier API instead of each game inventing incompatible global settings.

## Unlockables and loadouts

`game-unlocks.js` stores state in:

```text
chrome.storage.local["gsGameUnlocksV1"]
```

The current unlock model supports:

- hats;
- costumes;
- trails;
- victory dances;
- card frames;
- titles;
- emotes;
- perks.

Unlock conditions can use global level, challenge completion counts and per-game career level. The current data includes game-specific rewards for Fishing, Smash, Survivors, Hide & Seek, Tower Defense, Pool, Volleyball, Popcorn, Rhythm Tap, Air Hockey, Endless Runner, Brickball, Fruit Ninja, Pinball and other game careers.

Loadout state is persistent and includes equipment slots plus up to two perk slots.

## Loot, currencies, social state and auxiliary gameplay

The background game handler also owns or brokers several cross-game state surfaces.

### Loot and inventory

Current background state uses `mascotLootV1` for mascot-identity gameplay data. The handler can:

- return a mascot's loot/profile state;
- return inventory/profile state;
- favorite or lock inventory items;
- sell items/fish for tokens;
- equip gear;
- expose gameplay-video channels associated with games.

The current sell path awards a fixed token value for generic inventory quantity and rarity-based values for fish. Treat those values as implementation constants, not a permanent economy contract.

### Relationships

Relationship reads use `mascotSocialV1` and can filter pairs by mascot identity.

### Fishing and aquarium

The background contract includes fishing session/start/result/XP messages. Some of those message handlers currently only acknowledge the request, so the presence of a message type alone must not be interpreted as proof that all progression logic is centralized there.

Aquarium layouts persist under keys shaped like:

```text
gsAquariumLayout_<identityKey>
```

### Skins

The background skin store is:

```text
gsMascotSkinsV1
```

It tracks:

- available skins;
- currently equipped skin per mascot;
- per-game skin overrides;
- palette presets where present.

### Mascot Studio

The background studio store is:

```text
gsMascotStudioV1
```

It supports pack get/save/list/delete/import/export and physics/TV-frame state. Exported packs identify themselves as:

```text
gamesync-mascot-pack-v1
```

Pack import supports conflict behavior including `skip`, `keepBoth` and replacement behavior.

## Background message surface

Important verified message types include:

```text
GS_START_GAME
GS_INJECT_GAME_SCRIPTS
MASCOT_GET_LOOT
MASCOT_GET_INVENTORY
MASCOT_SET_INVENTORY_FLAGS
MASCOT_SELL_ITEMS
MASCOT_EQUIP_GEAR
MASCOT_GET_RELATIONSHIPS
MASCOT_FISHING_START
MASCOT_FISHING_RESOLVE_CATCH
MASCOT_FISHING_ADD_XP
MASCOT_AQUARIUM_SAVE_LAYOUT
MASCOT_GET_SKINS
MASCOT_SAVE_SKIN
MASCOT_DELETE_SKIN
MASCOT_EQUIP_SKIN
MASCOT_RESOLVE_SKIN
MASCOT_SET_GAME_SKIN
MASCOT_STUDIO_GET_PACK
MASCOT_STUDIO_SAVE_PACK
MASCOT_STUDIO_LIST_PACKS
MASCOT_STUDIO_DELETE_PACK
MASCOT_STUDIO_IMPORT_PACK
MASCOT_STUDIO_EXPORT_PACK
```

These names are implementation contracts between GameSync components. They are not a promise of a stable public third-party API unless separately versioned as one.

## Script-injection safety boundary

`GS_INJECT_GAME_SCRIPTS` does not accept arbitrary paths. It:

1. obtains the sender tab ID;
2. filters the requested paths against a hardcoded `ALLOWED` set;
3. rejects the request if no approved files remain;
4. calls `chrome.scripting.executeScript` only with the approved files.

When adding a new mode, do not weaken this control by allowing arbitrary runtime filenames.

## Installation and build workflow

The verified shipping repository uses a conventional Vite source/build layout.

### Prerequisites

- Node.js/npm suitable for the repository lockfile and Vite toolchain;
- Opera GX or another compatible Chromium browser for local extension testing;
- the `Herbertofury/Gamesync` repository checked out at the intended branch/commit.

### Install dependencies

```powershell
npm ci
```

### Development server

```powershell
npm run dev
```

### Production build

```powershell
npm run build
```

`app/` is canonical editable source. `dist/` is generated. After a source change, rebuild before testing the production extension.

### Load in Opera GX

Load the generated `dist/` directory as the unpacked extension. Do not load `app/` as the production extension target.

## Testing and verification status

The root package currently exposes `test:bounty` and `benchmark:bounty`, but **does not expose a dedicated Mascot Games test script**.

That means:

- `npm run build` proves that the extension packages successfully;
- source inspection proves that the game modes and shared systems exist;
- neither proves that every one of the 23 accepted game launch paths is playable end-to-end in the current Opera GX runtime.

### Required real-runtime qualification matrix

A meaningful release-quality verification pass for PRJ-008 should exercise every accepted `GS_START_GAME` game ID. For each game record at least:

- launch succeeds from the real GameSync UI/route that exposes it;
- correct game scripts are loaded;
- no service-worker or page console error blocks the flow;
- game controls visibly affect the game;
- score/win/loss or equivalent loop advances;
- live/authored mascot art is used where the mode promises mascot rendering;
- game exit restores the page and mascot state cleanly;
- repeated launch works;
- per-game character selection persists;
- relevant challenge/progression updates persist;
- reload does not corrupt local game state.

Sports-focused priority smoke tests should include Bowling, Racing, Tennis, Air Hockey and Volleyball. Pinball and Fishing are also useful cross-architecture representatives.

The shared presentation layer should additionally be tested in:

- 2D;
- 3D third-person;
- 3D first-person where supported;
- webpage-ground mode;
- restart/reload persistence.

## Adding a new game safely

A complete game addition normally requires more than creating one file.

1. Implement the game mode under the appropriate `app/content/<game>/` path or shared mascot-game module.
2. Reuse `game-core.js` for shared timing/rendering/input primitives when applicable.
3. Reuse `game-mascot-runtime.js` for authored mascot drawing instead of creating disconnected placeholder characters.
4. Add the new game ID to `VALID_GAMES` in `mascot-game-handler.js`.
5. Add every dynamically injected source file to the strict `ALLOWED` script set.
6. Wire the actual GameSync UI/overlay route that requests the game.
7. Decide whether the game participates in challenges, modifiers, unlocks, careers, loot and social state, then update those registries intentionally.
8. Verify startup, play loop, cleanup, repeated use and persistence in the built extension.
9. Verify no existing game path regressed.
10. Update this wiki only after the new behavior is present in the canonical source and verified to the appropriate level.

## Common failure modes and troubleshooting

### `Invalid game: <id>`

The requested identifier is not in the background `VALID_GAMES` set. Confirm the mode was fully integrated instead of bypassing the validation.

### `No active tab found`

`GS_START_GAME` forwards to the active tab in the last-focused browser window. Confirm the request is made while a normal target tab is active.

### `Missing sender tabId`

Dynamic injection requires a real sender tab. A message sent from a context without a tab cannot use the injection path as written.

### `No valid game script files`

Every requested file was absent from the hardcoded script allowlist. Add the legitimate new game files to the allowlist rather than removing validation.

### `Game script injection failed`

Inspect the returned browser error and the target tab. Common causes include an unavailable tab/context, restricted page, missing packaged file or incorrect wiring.

### Mascot art is missing

Check the shared mascot-game/open-world bridge and pack discovery path. `game-mascot-runtime.js` depends on the mascot open-world loader to discover owned Shimeji packs and load the corresponding runtime.

### Character choice does not persist

Inspect the per-game localStorage key `gsMascotGameCharacter:<gameId>` and confirm the normalized game ID is stable.

### 2D/3D/camera state appears stale

Inspect the `gsMascotGamePresentation:<gameId>` localStorage family before changing rendering code.

### Webpage-ground mode is unavailable

The implementation intentionally avoids capturing GameSync's own extension page, and capture can also fail if the browser context does not permit visible-tab capture. The game should remain usable with synthetic ground rather than treating capture failure as success.

### Challenge data and launcher disagree on available games

The challenge registry and background launch registry are separate arrays/sets. Reconcile both intentionally. Do not silently assume that adding a game to one surface adds it everywhere.

## Relationship to other Project Constellation tracks

### PRJ-005 - Mascot / Screenmate Platform

PRJ-005 owns the broader mascot runtime and character compatibility problem. PRJ-008 consumes that platform to make actual games. Core mascot import/runtime changes should generally be documented in PRJ-005, while game-specific use and progression belong here.

### PRJ-006 and PCX-060 - ACS runtime and speech

ACS agents may participate as mascot identities, but classic Agent parity and speech/voice semantics remain separate tracks. A game should not fake Agent behavior to compensate for missing ACS runtime features.

### PCX-061 / PRJ-007 - Petz

Petz has its own behavior/physics identity. If Petz characters participate in Mascot Games, preserve the Petz engine rather than flattening them into ordinary Shimeji animation merely to fit a game mode.

### PCX-042 - GameSync Next

The historical PRJ-008 plan called for WXT/React/Vite v2 alignment. The inspected GameSync Next package root does not currently establish a dedicated Mascot Games package as the canonical executable source. Shipping GameSync therefore remains the strongest verified implementation host for this wiki. V2 parity must be proven rather than inferred from the plan.

## Current unresolved items

1. **Golf flagship:** preserved historical requirement, but no current Golf game was verified in the shipping launch registry or inspected shared game tree.
2. **Full live qualification:** source exists for a broad set of modes, but this documentation pass does not claim all 23 were exercised end-to-end in Opera GX.
3. **Dedicated automated tests:** the root package has no `test:mascot-games` or equivalent dedicated suite.
4. **Registry parity:** the challenge registry and launch registry are not currently identical.
5. **GameSync Next parity:** the plan calls for v2 alignment, but current end-to-end parity has not been established here.
6. **Popup/panel/full-view promise:** the old plan requested all three surfaces. Current source proves active-tab game launch/injection and game implementations, but this pass does not claim every game works in every historical surface.

## Highest-value next proof

Run a real Opera GX game qualification pass against the built `dist/` extension, starting with Bowling, Tennis, Racing, Air Hockey, Volleyball, Pinball and Fishing, then cover the remaining accepted game IDs. Capture launch, controls, mascot rendering, score/progression, cleanup, persistence and restart evidence.

After the shipping runtime is qualified, compare the accepted game set and shared game contracts against GameSync Next and determine whether Golf should be restored as the flagship, implemented as a new mode, or formally superseded by the broader current mascot arcade/sports suite.

## Maintenance triggers

Update this wiki when any of the following materially changes:

- the `GS_START_GAME` registry;
- the allowed game-script list;
- a game mode is added, removed or substantially rewritten;
- Golf becomes implemented or is formally superseded;
- shared game-core presentation/physics changes;
- mascot drawing/runtime integration changes;
- challenge/modifier/unlock/economy schemas change;
- storage keys or migration behavior change;
- GameSync Next receives a canonical Mascot Games implementation;
- a real browser qualification pass establishes or disproves current gameplay behavior.