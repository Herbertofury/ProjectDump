# GameSync Bounty / Rewards Runtime Wiki

**Project Constellation ID:** `PCX-053`  
**Canonical implementation repository:** [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync)  
**Canonical branch:** `main`  
**Verified GameSync extension version:** `0.6.3`  
**Current repository commit observed for this documentation pass:** `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`  
**Architecture / validation evidence repository:** [Herbertofury/GameSync-Next](https://github.com/Herbertofury/GameSync-Next), `Bounty/`  
**Project state:** active GameSync feature with real shipping source, verified historical Opera GX runtime evidence, and newer source changes that supersede parts of the July 2026 coverage matrix.

## Purpose

Bounty is GameSync's rewards, giveaways, drops, ownership, deadline, claim, and collection runtime. It exists to answer practical questions such as:

- What free games, loot, codes, drops, campaigns, or rewards are available now?
- Which items are earnable, claimable, redeemable, already owned, wanted, missing, claimed, or verified?
- What deadlines are approaching?
- Which source supplied each fact and how authoritative is it?
- Can GameSync help perform a supported earning/claim workflow without inventing account state?
- Can the same information be viewed as cards, collection state, history, source diagnostics, or calendar occurrences?

The core correctness rule from Project Constellation remains binding: **no synthetic progress or fabricated ownership**. Manual user state is authoritative, account evidence must come from a verified source/session/API, and partial or unavailable sources remain visibly partial instead of being represented as successful.

## Canonical evidence and source priority

Use these sources in this order when maintaining Bounty documentation:

1. Current shipping source in [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync).
2. Current package manifest and build scripts in [`package.json`](https://github.com/Herbertofury/Gamesync/blob/main/package.json).
3. Project-owned Bounty architecture, validation, performance, migration, and coverage reports in [`GameSync-Next/Bounty`](https://github.com/Herbertofury/GameSync-Next/tree/main/Bounty).
4. Older Project Constellation catalog summaries only for continuity/history when current source does not answer the question.

The July 24, 2026 `BOUNTY_SOURCE_API_COVERAGE.md` and `BOUNTY_SPEC_COVERAGE.md` are valuable validation snapshots, but current shipping source is newer. In particular, current `Gamesync` source now registers real Twitch viewer, Steam library, and Battle.net adapters that go beyond the older foundation-only descriptions.

## Repository layout

The canonical shipping extension uses this layout:

```text
Gamesync/
├── app/                              # editable extension source
│   ├── src/features/bounty/
│   │   ├── adapters/
│   │   │   ├── battle-net.js
│   │   │   ├── gamerpower.js
│   │   │   ├── steam-library.js
│   │   │   └── twitch-viewer.js
│   │   ├── twitch-miner/
│   │   │   ├── client.js
│   │   │   ├── index.js
│   │   │   ├── normalizer.js
│   │   │   ├── queries.js
│   │   │   └── runtime.js
│   │   ├── background-service.js
│   │   ├── bounty-service.js
│   │   ├── browser-session.js
│   │   ├── calendar.js
│   │   ├── contracts.js
│   │   ├── index.js
│   │   └── source-registry.js
│   └── shared/ui/bounty/
│       ├── bounty-ui.js
│       └── bounty.css
├── dist/                             # generated production extension
├── package.json
├── package-lock.json
└── vite.config.ts
```

`app/` is the editable source. `dist/` is generated and is the only directory that should be loaded as the unpacked production extension after a build.

## Runtime architecture

The project-owned architecture report describes the primary production path as:

```text
popup / panel / full-page / interactive preview
        |
        v
shared/ui/bounty/bounty-ui.js + bounty.css
        |  BOUNTY_* messages
        v
src/features/bounty/background-service.js
        |
        v
src/features/bounty/bounty-service.js
   ├── source-registry.js
   ├── adapters/*
   ├── calendar.js
   └── src/storage/db.js / IndexedDB
```

The feature is intentionally a vertical slice. Host pages should register navigation and mounting, while Bounty behavior stays inside the Bounty feature/service/UI modules instead of leaking reward-specific logic across unrelated GameSync code.

## Main user surfaces

The verified Bounty information architecture includes:

- **Today**
- **Free Games**
- **Drops & Loot**
- **Quests & Codes**
- **FOMO**
- **Vault**
- **Calendar**
- **Claimed**
- **Automation**
- **Sources**
- **History**

The same Bounty slice is designed to work in GameSync's popup, pinned panel/sidebar, and full-page surfaces. The UI uses a compact item-first model with remembered density/layout preferences, a detailed inspector, filters, search, sorting, artwork, source evidence, deadlines, actions, and explicit failure states.

## Persistence model

The Bounty architecture introduced an additive IndexedDB migration with dedicated stores. Existing GameSync stores were not supposed to be replaced or rewritten.

| Store | Key | Purpose |
|---|---|---|
| `bountyRecords` | `recordId` | Canonical offers, campaigns, events, rewards |
| `bountyCollectibles` | `collectibleId` | Item-level collectible truth |
| `bountyAcquisitionRoutes` | `routeId` | Ways/times an item can be acquired |
| `bountyCalendar` | `occurrenceId` | Availability/deadline occurrences |
| `bountyOwnership` | `ledgerId` | User-authoritative owned/wanted/missing state |
| `bountyClaims` | `claimId` | Claim and verification state |
| `bountyArtwork` | `artworkId` | Provenance, validation, locks, last-known-good art |
| `bountySources` | `sourceId` | Adapter status, latency, errors, repair information |
| `bountyHistory` | `historyId` | Append-only user/sync history |
| `bountyPreferences` | `preferenceId` | Density, layout, filters, notifications |

### Authority rules

- Manual ownership state is authoritative and must survive synchronization.
- Locked manual artwork is authoritative and survives source refreshes.
- Source facts keep provenance/confidence rather than being flattened into certainty.
- External actions use validated HTTPS URLs supplied by source evidence.
- A failed source does not erase unrelated successful sources.

## Current source adapters

Current shipping `source-registry.js` registers four executable adapters and exposes two additional capability rows.

### GamerPower

**Status:** registered, ready  
**Authority:** curated aggregator  
**Purpose:** giveaways, free-to-keep games, loot, codes, betas.

This is the broad public-feed adapter. It supplies source links and artwork but is not treated as first-party account ownership proof.

### Twitch Drops

**Status:** registered, `session-ready`  
**Authority:** first-party authorized browser session.

Current source can read viewer reward/campaign evidence from the user's already-authorized Twitch pages and contains a dedicated Twitch mining runtime. GameSync does not need to persist browser cookies or bearer tokens for the browser-session extractor. Authentication remains in the user's browser session.

### Steam

**Status:** registered, `settings-ready`  
**Authority:** first-party account API.

The Steam adapter reuses Steam identity/API settings already saved in GameSync Options. It accepts a SteamID64 or vanity identity, resolves the effective Steam ID, loads owned games, attempts wishlist reconciliation, and emits per-game verified ownership evidence including Steam App ID and observed playtime/last-played metadata when available.

If neither Steam ID nor vanity identity is configured, the adapter returns an explicit authentication/configuration-required state instead of guessing ownership.

### Battle.net / Blizzard

**Status:** registered, `session-ready`  
**Authority:** first-party authorized browser session.

The adapter opens or reuses the user's authenticated `account.battle.net/games` page, validates the provider origin/path, extracts visible game-license evidence, and returns verified-account ownership rows. When the user is signed out, it returns an authentication-required state.

### Amazon Games / Prime Gaming

**Status:** capability row only, guided session.

Current registry describes account-bound offers and delivery evidence as requiring the user's authorized Amazon Games session. It is not registered as an executable production adapter in the current source registry.

### Guild Wars 2

**Status:** capability row only, credentials required.

The capability model anticipates API-key ownership reconciliation for skins, mounts, minis, dyes, outfits, titles, novelties, and other unlocks, but the current source registry does not register an executable GW2 adapter.

## Authorized browser-session extraction

`browser-session.js` provides a shared boundary for providers that are best read from an already-authenticated browser page.

Its rules are important when adding or modifying account adapters:

1. The target URL must pass an explicit allowed-origin and allowed-path-prefix check.
2. GameSync may reuse an existing matching tab or create a background tab.
3. It waits for the authorized page to finish loading.
4. A shipped self-contained extractor runs with `chrome.scripting.executeScript`.
5. The extractor returns structured evidence only.
6. Cookie values and bearer tokens are not read or persisted by this helper.
7. Returned/observed URLs are revalidated against the provider allowlist.

This pattern is currently used by Battle.net and underpins the current Bounty account-source direction.

## Twitch miner runtime

The current shipping repository contains a real `twitch-miner/` runtime rather than only a future design note.

### Start flow

`startTwitchMiner()` requires:

- a Bounty record from source `twitch-viewer`;
- the Drop not already being claimed/verified;
- an earning window that has not ended;
- browser tabs, scripting, session storage, and alarms to be available.

When started, GameSync:

1. closes an older miner tab if one is still tracked;
2. creates a background pinned tab;
3. resolves a Twitch participating-channel directory from the campaign evidence or the user's authenticated Drops campaign page;
4. chooses a valid live participating channel;
5. opens that channel in the pinned tab;
6. keeps playback muted;
7. creates the Bounty Twitch miner health alarm;
8. records state in `chrome.storage.session`;
9. optionally emits a browser notification that mining started.

### Runtime health and recovery

The miner health path validates that the pinned tab still exists and still points at a valid Twitch channel. It inspects the page's video playback state and attempts recovery when:

- the mining tab was closed;
- the tab left the valid channel URL shape;
- the video element disappears or ends;
- playback stops advancing long enough to qualify as a stall.

The current source uses a **three-minute playback stall recovery threshold** and a recurring miner health alarm. When a channel fails, recovery attempts to select another participating channel rather than silently reporting progress.

### Inventory synchronization

Active miner state tracks inventory synchronization attempts. Current code requests a new inventory-sync attempt after approximately **five minutes** without one and records both successful sync time and the most recent sync error.

### Stop behavior

`stopTwitchMiner()`:

- closes the tracked Twitch tab when present;
- clears the miner alarm;
- marks the miner inactive;
- records stop time/reason;
- clears active channel identity/error state.

A user-visible clean stop is part of the expected behavior. A closed/failed miner must not remain represented as active progress.

## Calendar and deadline model

Bounty models multiple meaningful dates instead of a single generic expiration:

- availability;
- earn deadline;
- claim deadline;
- redeem deadline.

The feature derives occurrences into the calendar store. The verified July runtime included month and agenda presentations and timezone-safe ICS export. External two-way calendar synchronization and recurrence prediction were still incomplete in the last project-owned coverage report.

## Artwork behavior

The architecture defines a truthful artwork hierarchy:

1. exact source-provided item artwork;
2. truthful source-provided parent/event artwork;
3. preserved last-known-good artwork when validation fails;
4. explicit invalid/missing state instead of invented imagery.

Artwork validation is bounded/parallelized. Manual locked artwork is user-authoritative and must not be overwritten by synchronization.

## Sync pipeline

The verified architecture describes the high-level pipeline as:

1. start enabled independent adapters concurrently;
2. normalize and validate at the adapter boundary;
3. merge by stable source identity without deleting unrelated existing records;
4. resolve/validate artwork with provenance;
5. derive availability/earn/claim/redeem occurrences;
6. batch-write normalized records, occurrences, source diagnostics, and history;
7. schedule the next reminder alarm from persisted occurrences;
8. return the complete matching snapshot to the active GameSync surface.

Independent adapter failures use partial-success semantics. One broken provider should not make successful providers disappear.

## Performance and quantity rules

Bounty follows GameSync's lossless rendering requirement:

- all matching records are admitted synchronously;
- no viewport virtualization is used to hide or defer off-screen records;
- no silent record cap is applied to search/filter results;
- the root remains mounted and interactions patch content in place;
- stable record/occurrence IDs are used for DOM identity;
- source I/O and artwork validation are parallelized with bounded concurrency.

The historical performance report includes synthetic scale verification with **zero records dropped**. Synthetic throughput is not proof that every provider has a complete live catalog.

## Installation and development setup

### Prerequisites

Install current [Node.js](https://nodejs.org/) with npm and [Opera GX](https://www.opera.com/gx) for the canonical extension runtime.

Clone the canonical GameSync repository and install the locked dependency set:

```powershell
git clone https://github.com/Herbertofury/Gamesync.git
cd Gamesync
npm ci
```

### Run the development server

```powershell
npm run dev
```

### Build the production extension

```powershell
npm run build
```

The build regenerates `dist/` from `app/`.

### Load in Opera GX

After the production build, load this directory as the unpacked extension:

```text
<clone-directory>\Gamesync\dist
```

Do not load `app/` as the production unpacked extension. `app/` is source; `dist/` is the generated production runtime.

## Bounty-specific verification commands

The current package exposes:

```powershell
npm run test:bounty
npm run benchmark:bounty
npm run build
```

`test:bounty` runs the Bounty Node test suite under `app/test/bounty/`. `benchmark:bounty` runs the dedicated Bounty benchmark harness. `npm run build` is still required because test success alone does not prove release-closure correctness.

## Historical real-runtime validation evidence

The July 24, 2026 Bounty validation pass used an isolated Opera GX profile and verified the then-current feature end to end.

Recorded results included:

- Bounty unit/schema/calendar/adapter/layout suite: **9/9 passed**;
- production Vite build passed;
- built HTML/manifest entrypoint closure passed;
- production ZIP validation: **5,329 entries**;
- scale benchmark passed with **0 records dropped**;
- Bounty mounted in real GameSync full-page runtime;
- live GamerPower synchronization completed;
- observed snapshot: 97 records, 112 occurrences, 97 artwork rows, six source capability rows;
- Today, Free Games, Calendar rendered;
- zero broken rendered images observed;
- claim-state persistence round-tripped;
- page and service-worker error collections were empty after the final reload;
- packaged `dist` was separately loaded as an unpacked extension and synchronized live data.

Historical production archive recorded in that report:

```text
GameSync-opera-extension-bounty-0.6.3-2026-07-24.zip
252,561,859 bytes
SHA-256 B1251ED001B6C8009E9258DF9E64ECCF8E47354D6553FE610A7CD90F31D91B6B
```

### Important freshness boundary

That validation report predates the newer shipping adapter/miner source now present in `Herbertofury/Gamesync`. It proves the July runtime baseline, not a fresh 2026-08-17 real-Opera acceptance pass for every newer Twitch/Steam/Battle.net path. Treat the current source as implemented code, but require a fresh provider-by-provider real-runtime pass before claiming all newer account paths are currently production-qualified.

## Defects already found and fixed historically

The Bounty validation pass documents several important failure classes that should remain regression cases:

- service-worker syntax failure in snapshot destructuring;
- source-diagnostics reference failure that quarantined artwork;
- page-context artwork validation blocked by browser CORS response-body access;
- Vite build initially omitted classic scripts/static runtime directories despite a successful exit code;
- persisted GameSync `view-grid` styling hid the `.gs-detail` Bounty host even though Bounty was mounted with data.

The release-closure plugin and Bounty stylesheet corrections were added to prevent those regressions.

## How to modify Bounty safely

### Add or change a source adapter

Adapter work belongs under:

```text
app/src/features/bounty/adapters/
```

Then register it through:

```text
app/src/features/bounty/source-registry.js
```

A registered adapter must have a stable `id` plus a `fetch()` or `sync()` function. New account adapters should:

- use documented provider APIs or the user's already-authorized browser session;
- return stable canonical identities;
- preserve provider/source evidence;
- expose authentication/partial/rate-limit failures truthfully;
- never invent profile, claim, inventory, or item URLs;
- avoid deep imports into UI internals.

### Change Bounty data contracts

Start with:

```text
app/src/features/bounty/contracts.js
app/src/features/bounty/bounty-service.js
```

Schema changes must preserve the additive-migration model and existing user-authoritative state. Never repurpose a store/key in a way that silently changes the meaning of already-persisted records.

### Change the UI

Use:

```text
app/shared/ui/bounty/bounty-ui.js
app/shared/ui/bounty/bounty.css
```

Keep the root mounted, preserve stable DOM identity, and ensure every visible action has a real implementation behind it. Do not add decorative claim/progress controls that are disconnected from source/service state.

### Change Twitch mining

Use:

```text
app/src/features/bounty/twitch-miner/
```

Preserve:

- strict Twitch URL validation;
- authenticated campaign/directory evidence;
- valid participating-channel selection;
- muted background playback;
- explicit stop/cleanup;
- health checks and stall recovery;
- truthful waiting/error states;
- source inventory synchronization.

Changes to DOM selectors or Twitch page parsing require a fresh real Twitch acceptance pass because provider markup can change independently of GameSync.

### Change calendar behavior

Use:

```text
app/src/features/bounty/calendar.js
```

Keep date handling explicit and timezone-safe. Verify occurrence identity, deadline type, export folding, and import/export semantics before shipping calendar changes.

## Troubleshooting

### Bounty tab is blank

First confirm the root mounted and inspect current GameSync layout state. A historical defect showed that persisted `view-grid` styling could hide `.gs-detail` even while Bounty had loaded records. Current CSS contains a targeted fix, so a recurrence should be treated as a layout regression rather than "no data" until source state is checked.

### A provider shows authentication required

Use the provider-specific setup rather than forcing a generic retry:

- **Steam:** configure SteamID64 or vanity identity in GameSync Options; API access may also require the saved Steam API key.
- **Battle.net:** sign into the Battle.net account site in Opera GX, then rerun Bounty sync.
- **Twitch:** sign into Twitch in Opera GX and open/sync Bounty again.
- **GW2:** the current registry advertises credentials-required capability but no executable adapter is registered yet.

### Twitch miner says the earning window ended

The selected Bounty record's earning deadline has passed. The miner intentionally refuses to start rather than representing post-deadline playback as productive progress.

### Twitch miner enters waiting-for-channel

No valid participating live channel could be resolved, or recovery exhausted the current candidates. Leave the state truthful. Do not convert waiting-for-channel into a synthetic progress state.

### Twitch mining tab was closed

The health check marks mining paused/inactive and records the error. Start the miner again from the Bounty item when appropriate.

### Twitch playback buffers continuously

The miner attempts automatic playback recovery after the stall threshold. If it remains waiting/buffering, inspect Twitch page/selector changes and current campaign participation rather than lowering correctness checks.

### Source sync is partial

Inspect the **Sources** surface and source diagnostics. Partial success is intentional: working providers remain usable while failed providers report repair details.

### Artwork disappears or becomes invalid

Inspect `bountyArtwork` provenance, validation state, manual lock state, and last-known-good data. Do not replace invalid source artwork with unrelated guessed images.

### Build succeeds but the extension is missing runtime files

Treat this as a release-closure failure. A historical Bounty pass found that Vite could exit successfully while omitting classic scripts/static runtime directories. Verify the built HTML/manifest entrypoint closure and load the generated `dist/` in Opera GX before calling the build usable.

## Known open gaps

The latest project-owned coverage evidence still leaves meaningful work:

- complete provider-specific account integration across every desired source;
- executable Prime Gaming and GW2 adapters in the current source registry;
- universal verified item/game catalog coverage;
- complete GameSync V2 and separate desktop parity for Bounty;
- recurrence prediction and external two-way calendar synchronization;
- complete Bounty JSON backup/import beyond ICS calendar export;
- full cross-feature library/wishlist reconciliation;
- automated accessibility/WCAG audit coverage;
- exhaustive regression testing across every unrelated GameSync subsystem;
- a fresh real-Opera acceptance matrix for the newer Twitch viewer/miner, Steam, and Battle.net implementation now present in shipping source.

## Recommended next verification checkpoint

The highest-value next documentation/verification pass is a **current-source provider matrix** against the real GameSync 0.6.3 extension:

1. build current `main`;
2. load current `dist/` in an isolated Opera GX profile;
3. verify GamerPower live sync;
4. verify Twitch authorized viewer sync, miner start, playback, inventory refresh, recovery, stop, and restart/session behavior;
5. verify Steam configured/unconfigured states and ownership reconciliation;
6. verify Battle.net signed-in/signed-out states and license extraction;
7. verify source diagnostics during one intentionally failed provider while another succeeds;
8. verify ownership/claim state persists and is not silently overwritten;
9. rerun `npm run test:bounty`, `npm run benchmark:bounty`, and `npm run build`;
10. record exact commit, Opera version/profile, counts, errors, screenshots, and artifact hash.

Only after that pass should the older July source-coverage matrix be rewritten as fully current runtime evidence.

## Maintenance triggers

Update this wiki when any of these change materially:

- GameSync extension version or canonical repository/branch;
- Bounty adapter registry;
- provider authentication/session approach;
- Twitch miner lifecycle or selectors;
- IndexedDB Bounty stores/schema;
- ownership/claim authority rules;
- calendar/deadline model;
- source capability statuses;
- UI information architecture;
- build/test/benchmark commands;
- production runtime verification evidence;
- known source/provider gaps.
