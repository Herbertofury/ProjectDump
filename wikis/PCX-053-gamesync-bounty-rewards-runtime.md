# GameSync Bounty / Rewards Runtime Wiki

**Project Constellation ID:** `PCX-053`
**Canonical shipping implementation repository:** [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync)
**Canonical shipping branch:** `main`
**Verified shipping GameSync extension version:** `0.6.3`
**Current shipping repository commit observed for this documentation pass:** `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`
**Verified typed next-generation implementation:** [Herbertofury/GameSync-Next](https://github.com/Herbertofury/GameSync-Next) at `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`, Extension V2 `0.8.0`
**Project-owned architecture / validation lineage:** [`Herbertofury/GameSync-Next/Bounty`](https://github.com/Herbertofury/GameSync-Next/tree/main/Bounty)
**Project state:** active GameSync feature with a richer shipping implementation, verified historical and current Opera GX evidence, plus a separately verified typed GameSync Next Bounty slice. Provider breadth is not yet identical between the two hosts.

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

1. Current shipping source in [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync) for the richest production Bounty provider/runtime contract.
2. Current typed Extension V2 source in [Herbertofury/GameSync-Next](https://github.com/Herbertofury/GameSync-Next), especially `apps/extension-v2/src/features/bounty/`, `apps/extension-v2/src/ui/app/bounty/`, and the background bootstrap, for migration/parity state.
3. Current package manifests and build scripts in the owning repository for the host being tested.
4. Project-owned Bounty architecture, validation, performance, migration, and coverage reports in [`GameSync-Next/Bounty`](https://github.com/Herbertofury/GameSync-Next/tree/main/Bounty).
5. Older Project Constellation catalog summaries only for continuity/history when current source does not answer the question.

The July 24, 2026 `BOUNTY_SOURCE_API_COVERAGE.md` and `BOUNTY_SPEC_COVERAGE.md` remain valuable validation snapshots, but both active repositories contain newer source. Current shipping `Gamesync` registers Twitch viewer, Steam library, and Battle.net adapters that go beyond the older foundation-only descriptions. Current GameSync Next now contains an independently executable typed Bounty slice instead of only architecture/reference material.

## Shipping GameSync repository layout

The canonical shipping extension uses this layout:

```text
Gamesync/
├── app/ # editable extension source
│ ├── src/features/bounty/
│ │ ├── adapters/
│ │ │ ├── battle-net.js
│ │ │ ├── gamerpower.js
│ │ │ ├── steam-library.js
│ │ │ └── twitch-viewer.js
│ │ ├── twitch-miner/
│ │ │ ├── client.js
│ │ │ ├── index.js
│ │ │ ├── normalizer.js
│ │ │ ├── queries.js
│ │ │ └── runtime.js
│ │ ├── background-service.js
│ │ ├── bounty-service.js
│ │ ├── browser-session.js
│ │ ├── calendar.js
│ │ ├── contracts.js
│ │ ├── index.js
│ │ └── source-registry.js
│ └── shared/ui/bounty/
│ ├── bounty-ui.js
│ └── bounty.css
├── dist/ # generated production extension
├── package.json
├── package-lock.json
└── vite.config.ts
```

`app/` is the editable source. `dist/` is generated and is the only directory that should be loaded as the unpacked production extension after a build.

## Shipping runtime architecture

The project-owned architecture report describes the primary shipping path as:

```text
popup / panel / full-page / interactive preview
 |
 v
shared/ui/bounty/bounty-ui.js + bounty.css
 | BOUNTY_* messages
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

## GameSync Next typed Bounty parity slice

GameSync Next current main now contains a real typed Bounty implementation under:

```text
apps/extension-v2/src/features/bounty/
├── contracts.ts
├── index.ts
└── service.ts

apps/extension-v2/src/ui/app/bounty/
├── BountyView.tsx
├── bounty.css
└── index.ts
```

`App.tsx` lazy-loads `BountyView`, recognizes `bounty` as a real top-level tab, accepts `#tab/bounty`, and exposes Bounty on popup/panel and full application surfaces. This closes the old GameSync Next gap where Bounty existed only as parity/reference material.

### Typed current data contract

The current Next slice is deliberately smaller than the shipping multi-provider model. Its primary record types are:

```text
BountyRecord
BountyClaim
BountyHistoryEntry
BountyPreferences
BountySourceStatus
BountyStore
BountySnapshot
```

Current typed kinds are:

```text
free-game
loot
beta
code
```

Current computed states are:

```text
available
upcoming
claimed
verified
expired
```

The Next slice currently fixes `sourceId` to `gamerpower`. It does not yet model the shipping Twitch/Steam/Battle.net provider breadth as executable typed adapters.

### Next persistence and lifecycle

The current typed service uses `chrome.storage.local` key:

```text
gs_bounty_v1
```

rather than the richer shipping Bounty IndexedDB store family. The stored object contains:

- normalized live records;
- claim state keyed by `recordId`;
- append-style history entries;
- active-view/search/platform/kind/hide-claimed/notification preferences;
- GamerPower source health/count state;
- schema version and update timestamp.

Current default reminder offsets are 24 hours, 2 hours, and 15 minutes before a published end time. The service owns alarm `gamesync:bounty:next-reminder`. The background bootstrap routes that alarm back to `bountyService.handleReminderAlarm()` and routes all `BOUNTY_*` messages into the feature-owned handler.

### Next background message contract

Current main handles:

```text
BOUNTY_GET_SNAPSHOT
BOUNTY_SYNC
BOUNTY_SET_PREFERENCES
BOUNTY_SET_CLAIM
BOUNTY_EXPORT_ICS
```

Claim state supports `claimed`, `verified`, and `unclaimed` mutations. `BOUNTY_EXPORT_ICS` returns an iCalendar document built from current Bounty records.

### Next live-source behavior

`bountyService.sync()` fetches `https://www.gamerpower.com/api/giveaways`, validates normalized HTTPS claim/source/artwork URLs, converts source rows into stable `gamerpower:<externalId>` records, replaces the current typed record set with the accepted live snapshot, updates source health/history, persists state, and reschedules the next reminder.

This is intentionally not documented as equivalent to the shipping multi-provider merge pipeline. The typed Next slice currently has one live source and a much simpler persistence model.

### Next user surface

The verified React view exposes:

- Today
- Free Games
- Drops & Loot
- Quests & Codes
- FOMO Radar
- Calendar
- Claimed
- Sources
- History

It also provides:

- live sync;
- search;
- kind filter;
- platform filter;
- claim/open-source actions;
- claim, verify, and undo state;
- source-health display;
- ICS export;
- available/upcoming/claimed/ending-soon statistics.

The typed Next UI currently does **not** expose the shipping Bounty `Vault` and `Automation` surfaces as equivalent first-class views. Do not infer those from the older Bounty information architecture.

### Current GameSync Next runtime evidence

At verified GameSync Next head `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`, the isolated Opera acceptance pass:

- synchronized **107 live GamerPower records**;
- rejected zero source rows in that run;
- persisted healthy GamerPower source state;
- rendered the Bounty calendar;
- kept the React root mounted exactly once.

That evidence closes the prior GameSync Next Bounty tab/calendar parity gap. It does **not** prove provider-by-provider parity with shipping Twitch, Steam, Battle.net, Amazon/Prime, GW2 capability rows, Twitch mining, shipping artwork provenance, or the richer shipping IndexedDB schema.

## Cross-host parity rule

Treat shipping GameSync and GameSync Next as two verified Bounty hosts with different current breadth:

| Area | Shipping GameSync 0.6.3 | GameSync Next 0.8.0 |
| --- | --- | --- |
| GamerPower live source | verified implementation | verified implementation and current isolated Opera runtime |
| Bounty top-level UI | verified | verified |
| Claim state | richer production model | typed claimed/verified/unclaimed ledger |
| Calendar / ICS | richer calendar model | typed calendar view plus ICS export |
| Twitch viewer | implemented | not present in current typed slice |
| Twitch miner | implemented | not present in current typed slice |
| Steam ownership | implemented | not present in current typed slice |
| Battle.net ownership | implemented | not present in current typed slice |
| Amazon / Prime | capability row | not present in current typed slice |
| GW2 | capability row | not present in current typed slice |
| Persistence | additive IndexedDB Bounty stores | `chrome.storage.local` `gs_bounty_v1` |
| Artwork provenance | richer provenance/lock/last-known-good model | direct normalized GamerPower artwork URL |
| Multi-provider partial success | shipping architecture | not applicable to current single-source Next slice |

Do not delete richer shipping Bounty behavior merely because the typed Next slice now exists. Migration is complete only when paired runtime evidence proves the required capability on the intended successor host.

## Main user surfaces

The verified shipping Bounty information architecture includes:

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

The same shipping Bounty slice is designed to work in GameSync's popup, pinned panel/sidebar, and full-page surfaces. The UI uses a compact item-first model with remembered density/layout preferences, a detailed inspector, filters, search, sorting, artwork, source evidence, deadlines, actions, and explicit failure states.

The current GameSync Next view set is listed separately above because it is not yet identical.

## Shipping persistence model

The shipping Bounty architecture introduced an additive IndexedDB migration with dedicated stores. Existing GameSync stores were not supposed to be replaced or rewritten.

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

## Current shipping source adapters

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

Shipping Bounty models multiple meaningful dates instead of a single generic expiration:

- availability;
- earn deadline;
- claim deadline;
- redeem deadline.

The feature derives occurrences into the calendar store. The verified July runtime included month and agenda presentations and timezone-safe ICS export. External two-way calendar synchronization and recurrence prediction were still incomplete in the last project-owned coverage report.

The typed Next slice currently uses a simpler `startAt` / `endAt` model and exports the available end/start time as the ICS event start. Preserve this distinction when comparing calendar parity.

## Artwork behavior

The shipping architecture defines a truthful artwork hierarchy:

1. exact source-provided item artwork;
2. truthful source-provided parent/event artwork;
3. preserved last-known-good artwork when validation fails;
4. explicit invalid/missing state instead of invented imagery.

Artwork validation is bounded/parallelized. Manual locked artwork is user-authoritative and must not be overwritten by synchronization.

The typed Next slice currently normalizes an HTTPS GamerPower image or thumbnail and displays it directly. It does not yet reproduce the shipping provenance/lock/last-known-good artwork ledger.

## Shipping sync pipeline

The verified shipping architecture describes the high-level pipeline as:

1. start enabled independent adapters concurrently;
2. normalize and validate at the adapter boundary;
3. merge by stable source identity without deleting unrelated existing records;
4. resolve/validate artwork with provenance;
5. derive availability/earn/claim/redeem occurrences;
6. batch-write normalized records, occurrences, source diagnostics, and history;
7. schedule the next reminder alarm from persisted occurrences;
8. return the complete matching snapshot to the active GameSync surface.

Independent adapter failures use partial-success semantics. One broken provider should not make successful providers disappear.

By contrast, the typed Next service currently replaces its single-source `records` array from each accepted GamerPower payload. Do not port that replacement behavior into the shipping multi-provider store.

## Performance and quantity rules

Bounty follows GameSync's lossless rendering requirement:

- all matching records are admitted synchronously;
- no viewport virtualization is used to hide or defer off-screen records;
- no silent record cap is applied to search/filter results;
- the root remains mounted and interactions patch content in place;
- stable record/occurrence IDs are used for DOM identity;
- source I/O and artwork validation are parallelized with bounded concurrency where the owning host implements them.

The historical shipping performance report includes synthetic scale verification with **zero records dropped**. Synthetic throughput is not proof that every provider has a complete live catalog.

The current Next acceptance also preserved one React root mount during the live Bounty run. Future larger-record Next tests should retain complete matching-record availability and must not introduce viewport culling or hidden record caps as a performance shortcut.

## Shipping installation and development setup

### Prerequisites

Install current [Node.js](https://nodejs.org/) with npm and [Opera GX](https://www.opera.com/gx) for the canonical shipping extension runtime.

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

## GameSync Next build and verification setup

From a clean GameSync Next checkout:

```text
npm ci
npm --workspace apps/extension-v2 run build
npm run verify:extension-v2:opera
```

The maintained real Extension V2 Opera verifier is `scripts/verify-extension-v2-opera.js`. The root `test:e2e-opera` command currently points at an absent compatibility file and is not the current acceptance path.

When validating Bounty in Next, prove the loaded source head or an unmistakable descendant. The package version remains `0.8.0` across multiple source changes, so version string alone is not sufficient build identity.

## Shipping Bounty-specific verification commands

The current shipping package exposes:

```powershell
npm run test:bounty
npm run benchmark:bounty
npm run build
```

`test:bounty` runs the Bounty Node test suite under `app/test/bounty/`. `benchmark:bounty` runs the dedicated Bounty benchmark harness. `npm run build` is still required because test success alone does not prove release-closure correctness.

## Historical shipping real-runtime validation evidence

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

That shipping validation report predates the newer shipping adapter/miner source now present in `Herbertofury/Gamesync`. It proves the July runtime baseline, not a fresh current real-Opera acceptance pass for every newer Twitch/Steam/Battle.net path. Treat the current source as implemented code, but require a fresh provider-by-provider real-runtime pass before claiming all newer account paths are currently production-qualified.

The newer GameSync Next isolated Opera Bounty pass is current evidence for the typed GamerPower/claim/calendar slice only. It is not substitute runtime proof for the richer shipping providers.

## Defects already found and fixed historically

The shipping Bounty validation pass documents several important failure classes that should remain regression cases:

- service-worker syntax failure in snapshot destructuring;
- source-diagnostics reference failure that quarantined artwork;
- page-context artwork validation blocked by browser CORS response-body access;
- Vite build initially omitted classic scripts/static runtime directories despite a successful exit code;
- persisted GameSync `view-grid` styling hid the `.gs-detail` Bounty host even though Bounty was mounted with data.

The release-closure plugin and Bounty stylesheet corrections were added to prevent those regressions.

## How to modify Bounty safely

### Add or change a shipping source adapter

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

### Add or change a GameSync Next source

Current typed Next ownership lives under:

```text
apps/extension-v2/src/features/bounty/
```

Before adding a second provider, first redesign the single `BountySourceStatus` and fixed `sourceId: "gamerpower"` contract so provider identity, partial failure, source-specific diagnostics, stable cross-provider record identity, and existing user claim state remain unambiguous. Do not bolt a second source onto the current single-source replacement array and call it shipping parity.

### Change shipping Bounty data contracts

Start with:

```text
app/src/features/bounty/contracts.js
app/src/features/bounty/bounty-service.js
```

Schema changes must preserve the additive-migration model and existing user-authoritative state. Never repurpose a store/key in a way that silently changes the meaning of already-persisted records.

### Change GameSync Next data contracts

Start with:

```text
apps/extension-v2/src/features/bounty/contracts.ts
apps/extension-v2/src/features/bounty/service.ts
```

If `gs_bounty_v1` changes meaning, add a migration rather than silently normalizing incompatible stored data into the new contract. Preserve claim/history/preferences state and test restart persistence.

### Change the shipping UI

Use:

```text
app/shared/ui/bounty/bounty-ui.js
app/shared/ui/bounty/bounty.css
```

Keep the root mounted, preserve stable DOM identity, and ensure every visible action has a real implementation behind it. Do not add decorative claim/progress controls that are disconnected from source/service state.

### Change the GameSync Next UI

Use:

```text
apps/extension-v2/src/ui/app/bounty/BountyView.tsx
apps/extension-v2/src/ui/app/bounty/bounty.css
```

Keep `#tab/bounty` working in popup/panel/full surfaces, preserve live sync, filters, claim/verify/undo, source status, calendar, history, and ICS download behavior. Verify errors stay visible rather than being converted into silent empty states.

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

Shipping uses:

```text
app/src/features/bounty/calendar.js
```

GameSync Next calendar export is currently implemented in:

```text
apps/extension-v2/src/features/bounty/service.ts
```

Keep date handling explicit and timezone-safe. Verify occurrence identity, deadline type, export folding, and import/export semantics before shipping calendar changes.

## Troubleshooting

### Bounty tab is blank in shipping GameSync

First confirm the root mounted and inspect current GameSync layout state. A historical defect showed that persisted `view-grid` styling could hide `.gs-detail` even while Bounty had loaded records. Current CSS contains a targeted fix, so a recurrence should be treated as a layout regression rather than "no data" until source state is checked.

### Bounty tab is missing in GameSync Next

Confirm the loaded source is `cd906ff0831bf7fc33b41fea31b6f0c004cc1562` or a verified descendant, rebuild Extension V2, and verify `App.tsx` recognizes `bounty` and `#tab/bounty`. An older build can still report package version `0.8.0`, so verify source/build identity rather than version string alone.

### GameSync Next Bounty is empty on first open

`BountyView` requests `BOUNTY_GET_SNAPSHOT` and automatically requests `BOUNTY_SYNC` when the local snapshot has no records and source status is not already `error`. Inspect the returned source error and background logs before treating an empty view as valid no-data state.

### A shipping provider shows authentication required

Use the provider-specific setup rather than forcing a generic retry:

- **Steam:** configure SteamID64 or vanity identity in GameSync Options; API access may also require the saved Steam API key.
- **Battle.net:** sign into the Battle.net account site in Opera GX, then rerun Bounty sync.
- **Twitch:** sign into Twitch in Opera GX and open/sync Bounty again.
- **GW2:** the current shipping registry advertises credentials-required capability but no executable adapter is registered yet.

### Twitch miner says the earning window ended

The selected Bounty record's earning deadline has passed. The miner intentionally refuses to start rather than representing post-deadline playback as productive progress.

### Twitch miner enters waiting-for-channel

No valid participating live channel could be resolved, or recovery exhausted the current candidates. Leave the state truthful. Do not convert waiting-for-channel into a synthetic progress state.

### Twitch mining tab was closed

The health check marks mining paused/inactive and records the error. Start the miner again from the Bounty item when appropriate.

### Twitch playback buffers continuously

The miner attempts automatic playback recovery after the stall threshold. If it remains waiting/buffering, inspect Twitch page/selector changes and current campaign participation rather than lowering correctness checks.

### Shipping source sync is partial

Inspect the **Sources** surface and source diagnostics. Partial success is intentional: working providers remain usable while failed providers report repair details.

### GameSync Next source sync fails

The current typed slice has one live GamerPower source. Its error state persists source detail and the UI exposes it through Sources. Fix the actual fetch/validation failure rather than falling back to stale synthetic records.

### Artwork disappears or becomes invalid in shipping GameSync

Inspect `bountyArtwork` provenance, validation state, manual lock state, and last-known-good data. Do not replace invalid source artwork with unrelated guessed images.

### Build succeeds but the shipping extension is missing runtime files

Treat this as a release-closure failure. A historical Bounty pass found that Vite could exit successfully while omitting classic scripts/static runtime directories. Verify the built HTML/manifest entrypoint closure and load the generated `dist/` in Opera GX before calling the build usable.

## Known open gaps

Meaningful current work remains:

- complete provider-specific account integration across every desired shipping source;
- executable Prime Gaming and GW2 adapters in the current shipping source registry;
- universal verified item/game catalog coverage;
- provider-by-provider GameSync Next parity beyond the verified typed GamerPower slice;
- migration of shipping Twitch mining, Steam ownership, Battle.net ownership, artwork provenance, multi-provider partial success, and richer Bounty persistence into Next where successor parity is intended;
- recurrence prediction and external two-way calendar synchronization;
- complete Bounty JSON backup/import beyond ICS calendar export;
- full cross-feature library/wishlist reconciliation;
- automated accessibility/WCAG audit coverage;
- exhaustive regression testing across every unrelated GameSync subsystem;
- a fresh real-Opera acceptance matrix for the newer Twitch viewer/miner, Steam, and Battle.net implementation now present in shipping source.

## Recommended next verification checkpoint

The highest-value next Bounty checkpoint is a **paired cross-host provider/parity matrix** rather than another single-host smoke test.

### Shipping GameSync lane

1. build current `Herbertofury/Gamesync` `main`;
2. load current `dist/` in an isolated Opera GX profile;
3. verify GamerPower live sync;
4. verify Twitch authorized viewer sync, miner start, playback, inventory refresh, recovery, stop, and restart/session behavior;
5. verify Steam configured/unconfigured states and ownership reconciliation;
6. verify Battle.net signed-in/signed-out states and license extraction;
7. verify source diagnostics during one intentionally failed provider while another succeeds;
8. verify ownership/claim state persists and is not silently overwritten;
9. rerun `npm run test:bounty`, `npm run benchmark:bounty`, and `npm run build`;
10. record exact commit, Opera version/profile, counts, errors, screenshots, and artifact hash.

### GameSync Next lane

1. build verified current GameSync Next main or a known descendant;
2. run `npm run verify:extension-v2:opera`;
3. open `#tab/bounty` in the actual Extension V2 surface;
4. verify live GamerPower sync, source-health state, Today/filter/FOMO/calendar/history views, claim/verify/undo, ICS export, reminder scheduling, and restart persistence;
5. confirm all matching records remain available without viewport culling or a hidden record cap;
6. compare shared GamerPower records and claim/calendar semantics with the shipping lane;
7. record every missing shipping provider/runtime capability as an explicit migration gap rather than silently treating Bounty parity as complete.

The prior current-main acceptance already proves the typed Next Bounty tab/calendar vertical slice at 107 live GamerPower records. The paired matrix should now focus on migration completeness and behavior equivalence, not re-proving that the tab exists.

## Maintenance triggers

Update this wiki when any of these change materially:

- GameSync or GameSync Next source heads that own Bounty behavior;
- GameSync extension or Extension V2 package version;
- shipping or Next Bounty adapter/source registry;
- provider authentication/session approach;
- Twitch miner lifecycle or selectors;
- shipping IndexedDB Bounty stores/schema;
- GameSync Next `gs_bounty_v1` schema or storage ownership;
- ownership/claim authority rules;
- calendar/deadline model;
- source capability statuses;
- UI information architecture;
- build/test/benchmark commands;
- production runtime verification evidence;
- migration/parity status;
- known source/provider gaps.
