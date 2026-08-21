# PCX-055 - GameSync Script Polling Runtime

**Project Constellation ID:** PCX-055
**Status:** ACTIVE / TRACKED
**Canonical implementation:** [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync)
**Verified repository version:** GameSync `0.6.3`
**Observed canonical commit:** `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`
**Primary implementation area:** `app/src/script-tracker/` plus `app/modules/library/background/script-tracker-handler.js`

## Purpose

The GameSync Script Polling Runtime is the background polling and persistence layer behind Script Tracker. Project Constellation defines the project goal as running bounded background script/poll workflows with reliable catch-up and state persistence, with explicit scheduling, truthful progress, and protection against runaway workers.

The current GameSync source provides a real Manifest V3 implementation rather than only a continuity placeholder. It uses `chrome.alarms` for recurring wakeups, IndexedDB-backed state for sources/mods/creators/subscriptions/poll history/preferences, source adapters that normalize remote or imported catalogs, and a message-handler API that exposes scheduler, source, mod, subscription, import/export, advisory, and preference operations to the rest of GameSync.

## Current architecture

```text
GameSync UI / callers
 |
 v
SCRIPT_* background messages
 |
 v
app/modules/library/background/script-tracker-handler.js
 |
 +--------------------+
 | |
 v v
ScriptPollScheduler ScriptDb
 | |
 v v
Source adapters IndexedDB tables
 |
 +--> ScarletRealmAdapter
 +--> CustomListAdapter
```

The extension background service worker imports `scriptDb`, the Script Tracker message handler, and the Script Tracker polling scheduler. GameSync's Manifest V3 manifest grants the `alarms` and `storage` permissions required for the scheduler and persistence path.

## Repository map

| Path | Responsibility |
| --- | --- |
| `app/src/script-tracker/ScriptPollScheduler.js` | Recurring alarm setup, due-source selection, per-source polling, catalog processing, overlap guard, poll status. |
| `app/src/script-tracker/ScriptDb.js` | IndexedDB access for sources, normalized mods, per-source mod evidence, creators, subscriptions, poll logs, preferences, stats, import/export, and status aggregation. |
| `app/src/script-tracker/SourceAdapterBase.js` | Adapter contract and shared deterministic source/mod identity helpers. |
| `app/src/script-tracker/adapters/index.js` | Adapter registry and adapter metadata. |
| `app/src/script-tracker/adapters/ScarletRealmAdapter.js` | Pollable Google Sheets source for Scarlet's Realm Sims 4 mod status data. |
| `app/src/script-tracker/adapters/CustomListAdapter.js` | Manual CSV/JSON catalog import adapter. |
| `app/modules/library/background/script-tracker-handler.js` | Background `SCRIPT_*` request API used by GameSync surfaces. |
| `app/background/background.js` | Main MV3 service worker that imports and integrates the Script Tracker components. |
| `app/src/storage/db.js` | Shared `gamesync_intel` IndexedDB schema. Script Tracker tables were introduced in the DB v9 lineage and remain in the current DB v10 schema. |
| `app/manifest.json` | MV3 declaration and permissions including `alarms` and `storage`. |

## Scheduler behavior

### Alarm identity

`ScriptPollScheduler` uses one alarm named:

`script-tracker-poll`

The constructor installs an alarm listener when `chrome.alarms` exists. When that named alarm fires, the listener calls `runScheduledPolls()`.

### Starting recurring polling

The scheduler exposes:

`pollScheduler.schedulePolls(intervalMinutes = 1440)`

The default recurrence is **1440 minutes**, or 24 hours. The method creates the `script-tracker-poll` alarm using `periodInMinutes` and reports `{ ok: true, intervalMinutes }` when scheduling succeeds.

If the Alarms API is unavailable, the scheduler returns a truthful failure result rather than pretending background polling is active.

### Stopping recurring polling

`stopScheduledPolls()` clears the named alarm, removes the scheduler's alarm listener when present, clears its in-memory running flag, and returns `{ ok: true }`.

### Current source-level re-arm defect

At the verified `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928` source head, the stop/start lifecycle has a concrete listener re-arm defect that was not documented in the earlier wiki pass.

The sequence is:

1. the singleton constructor calls `setupAlarms()` and installs `alarmListener`;
2. `SCRIPT_STOP_SCHEDULER` calls `stopScheduledPolls()`, which clears the alarm, removes that listener from `chrome.alarms.onAlarm`, and sets `alarmListener = null`;
3. `SCRIPT_SCHEDULE_POLLS` calls `schedulePolls()`, which recreates the named alarm but does **not** call `setupAlarms()` or otherwise re-add the listener.

Therefore, if a user stops and then restarts recurring polling while the same service-worker instance remains alive, source inspection shows that the alarm can exist again while the scheduler instance has no registered alarm callback. A later service-worker reconstruction would run the singleton constructor again and reinstall the listener, but relying on worker teardown/recreation is not an acceptable start/stop contract.

This is a source-proven lifecycle defect, not a claim that a live Opera reproduction was executed during this documentation pass.

The narrow repair should preserve one of these invariants:

- `stopScheduledPolls()` clears only scheduling state and leaves the long-lived alarm listener registered for the lifetime of the scheduler singleton; or
- `schedulePolls()` explicitly calls the idempotent `setupAlarms()` before or after creating the recurring alarm.

Whichever repair is chosen should have a focused regression test that drives the real `SCRIPT_STOP_SCHEDULER -> SCRIPT_SCHEDULE_POLLS -> alarm fire` sequence and proves `runScheduledPolls()` is invoked without requiring a service-worker restart.

### Manifest V3 alarm and service-worker contract

Current Chrome extension-platform guidance materially tightens the scheduler acceptance contract beyond the source-level re-arm defect.

The current `chrome.alarms` documentation states that:

- alarms can be delayed beyond their requested time for performance reasons;
- an alarm does not wake a sleeping device;
- when a device wakes, missed alarms fire, but a repeating alarm fires at most once and is then rescheduled from the wake time rather than replaying every missed interval;
- normal packaged extensions cannot rely on periods below **30 seconds / 0.5 minutes**;
- Chrome limits an extension to 500 active alarms, while Script Tracker currently uses only one;
- Chrome 150 adds `persistAcrossSessions`, but the same documentation says that property is unsupported in other browsers and earlier Chrome versions, and recommends checking that important alarms exist whenever the service worker starts.

Chrome's Manifest V3 service-worker guidance also requires extension API event listeners to be registered synchronously at global script evaluation so an event can wake the worker and immediately find its handler. GameSync currently imports the singleton from the background service-worker graph, so the constructor's initial `setupAlarms()` call is synchronous during module evaluation. However, later removing that listener as part of an ordinary user-visible **Stop scheduler** operation breaks the intended long-lived event-listener model.

For GameSync's Opera GX target, do **not** make `persistAcrossSessions` a correctness dependency until exact target-browser support is proven. Treat it as an optional platform optimization when supported, not as a substitute for durable scheduler intent plus startup reconciliation.

### Recommended durable scheduler state machine

The current handler does not persist scheduler-enabled state or the currently requested scheduler interval. `SCRIPT_SCHEDULE_POLLS` passes `intervalMinutes` directly to `schedulePolls()`, and `SCRIPT_STOP_SCHEDULER` clears the alarm; the existing Script Tracker preference keys cover source/user preferences but not an explicit scheduler-enabled intent record.

A robust repair should separate **user intent** from the browser's transient alarm object:

```text
Persisted scheduler intent
  enabled: boolean
  intervalMinutes: number
        |
        v
service-worker startup reconciliation
        |
        +--> listener registered synchronously
        +--> read durable intent
        +--> chrome.alarms.get('script-tracker-poll')
        +--> recreate missing alarm only when enabled
        +--> run one due-source catch-up pass when appropriate
```

Recommended lifecycle invariants:

1. Register the `chrome.alarms.onAlarm` listener once for each service-worker instance and keep it installed for that worker's lifetime.
2. `SCRIPT_SCHEDULE_POLLS` validates the requested interval, persists `enabled: true` and the interval, creates/replaces the named alarm, then verifies the alarm exists.
3. `SCRIPT_STOP_SCHEDULER` persists `enabled: false`, clears the named alarm, and **does not** remove the long-lived event listener.
4. Service-worker startup reads scheduler intent and reconciles the actual alarm with that intent. If polling is enabled but the alarm is missing, recreate it.
5. If polling is disabled but an orphan alarm exists, clear it.
6. Alarm delivery rechecks the alarm name and durable enabled state before running due-source work.
7. Startup/wake catch-up uses persisted per-source `lastPollAt` timestamps; it should not attempt to replay every missed wall-clock interval.
8. If a target browser supports `persistAcrossSessions`, use it only as an explicitly feature-qualified enhancement. Startup reconciliation remains the source of truth.

This design also gives `SCRIPT_GET_SCHEDULER_STATUS` enough durable information to report **intended state**, **actual alarm state**, and **active poll state** separately instead of conflating them.

### Preventing overlapping poll loops

The runtime has a single-process overlap guard:

- `isRunning` is checked before a scheduled pass starts.
- A second `runScheduledPolls()` invocation while a pass is active returns `{ ok: false, error: 'Poll already in progress' }`.
- `isRunning` is reset in a `finally` block.

This prevents duplicate scheduled loops within the same live service-worker instance.

### Deciding which sources are due

A scheduled pass loads sources whose status is `active`. For every active source, it converts the source's `pollInterval` to milliseconds and compares the current time against `lastPollAt`.

Supported source intervals are:

| Source interval | Due threshold |
| --- | ---: |
| `hourly` | 1 hour |
| `daily` | 24 hours |
| `weekly` | 7 days |
| `manual` | Infinity, so the normal due check will not automatically poll it |

Unknown interval values fall back to the daily threshold.

A source is due when it has never been polled or when the elapsed time since `lastPollAt` meets or exceeds its configured interval. This means a delayed scheduled pass can identify overdue sources from persisted timestamps instead of depending only on an in-memory timer.

### Failure isolation

One source failure does not abort the rest of a scheduled pass. Each source poll is wrapped separately, with successful source IDs recorded under `results.polled` and failures recorded under `results.failed` with the source ID and error message.

## Per-source poll workflow

`pollSource(sourceId)` executes the following sequence:

1. Read the source from ScriptDb.
2. Fail explicitly if the source does not exist.
3. Create a durable poll-log row with status `running`.
4. Expose the active poll through `currentPoll` for status reporting.
5. Instantiate the configured adapter through the adapter registry.
6. Fetch and normalize the source catalog.
7. Process the normalized catalog into persistent Script Tracker state.
8. Update `lastPollAt` and `lastPollStats` on the source.
9. Persist the source update and mark the poll log `completed` with stats and catalog size.
10. On failure, persist the poll log as `error` with the error message.
11. Clear `currentPoll` in a `finally` block.

This is the main truthful-progress path. A poll has durable `running`, `completed`, or `error` history rather than being represented only by a transient progress indicator.

## Catalog processing

The scheduler normalizes catalog results into creators, mods, per-source mod evidence, and aggregated mod statuses.

### Creator processing

Catalog entries containing both `creatorId` and `creatorName` are deduplicated by creator ID. Existing creators are loaded first, and only previously unknown creator records are bulk inserted.

### Mod processing

Catalog entries are processed in batches of **100**.

Each item is handled with `Promise.allSettled`, so one bad mod row does not reject the entire batch. The runtime records counts for:

- `modsAdded`
- `modsUpdated`
- `creatorsAdded`
- `errors`

After each batch, the scheduler yields back to the event loop with a zero-delay timeout. This keeps large source catalogs from becoming one uninterrupted synchronous processing block.

### Existing mod updates

For an existing mod, the current scheduler updates:

- aggregated status;
- merged metadata;
- `updatedAt`;
- current per-source evidence when present.

It then recomputes the canonical aggregated status from all known source records for that mod.

## Status aggregation

When multiple Script Tracker sources describe the same mod, `ScriptDb.recomputeModStatus()` applies the following precedence:

1. `broken`
2. `obsolete`
3. `deprecated`
4. `updated`
5. `working`
6. `unknown`

A worse advisory state therefore wins over a better state when multiple sources disagree. This behavior is deliberate and should not be casually replaced by last-write-wins semantics.

## Persistent data model

Script Tracker uses the shared GameSync IndexedDB database, `gamesync_intel`. Current source declares database version 10; Script Tracker tables originated in the DB v9 schema lineage.

The Script Tracker layer operates on these logical stores:

| Store | Purpose |
| --- | --- |
| `scriptSources` | Source configuration, adapter identity, source status, polling interval, last poll state. |
| `scriptMods` | Canonical normalized mod records. |
| `scriptModSources` | Source-specific status/evidence for a mod. |
| `scriptCreators` | Normalized creators discovered through Script Tracker sources. |
| `scriptUserSubs` | User subscriptions and notification preferences. |
| `scriptPollLog` | Durable running/completed/error poll history. |
| `scriptUserPrefs` | Script Tracker preference values. |

`ScriptDb` also exposes dashboard counts, mod searching/sorting/filtering, subscription operations, poll history, export/import, source deletion cascades, and advisory lookup support.

## Source adapters

### Adapter contract

Every source adapter extends `SourceAdapterBase` and is expected to provide the source-specific implementations of:

- `fetchCatalog()`
- `getModStatus(modId)`
- `normalizeMod(rawEntry)`

Adapters may also override configuration checks, connection testing, polling interval behavior, and creator normalization.

The base class supplies deterministic mod IDs and per-source mod-evidence IDs. New adapters should preserve deterministic identity so repeated polls update existing records instead of creating duplicate logical mods.

### Scarlet's Realm adapter

The registered `scarlet-realm` adapter is a pollable Sims 4 source backed by a Google Sheet. Its adapter metadata declares:

- no required API key for basic public-sheet use;
- polling support;
- a default `daily` interval.

The implementation reads the `Working`, `Broken`, `Updated`, and `Obsolete` tabs by default, requests them in one Google Sheets batch call when possible, and falls back to sequential tab requests if the batch call fails.

Recognized tab states normalize to GameSync statuses such as `working`, `broken`, `updated`, `obsolete`, `deprecated`, and `unknown`.

The row parser recognizes common variants of these logical columns:

- mod name;
- creator/author;
- category/type;
- game patch;
- notes;
- URL/download link.

### Custom List adapter

The registered `custom-list` adapter is intended for manual import rather than recurring network polling. Its registry metadata reports `supportsPolling: false` and a default interval of `manual`.

It accepts:

- CSV text;
- a JSON array;
- a JSON string representing an array.

The CSV parser supports quoted fields and escaped double quotes without requiring another CSV package. Both CSV and JSON imports normalize common field aliases for mod name, creator, category, status, patch, notes, and URL.

Status aliases such as `ok`, `good`, `fixed`, `patched`, `outdated`, `old`, `abandoned`, and common check/cross glyphs are normalized into Script Tracker's canonical status vocabulary.

## Background message API

The Script Tracker handler exposes the runtime to other GameSync surfaces through `SCRIPT_*` messages.

### Scheduler commands

- `SCRIPT_GET_SCHEDULER_STATUS`
- `SCRIPT_SCHEDULE_POLLS`
- `SCRIPT_STOP_SCHEDULER`
- `SCRIPT_RUN_SCHEDULED_POLLS`

### Source commands

- `SCRIPT_SOURCE_LIST`
- `SCRIPT_SOURCE_GET`
- `SCRIPT_SOURCE_ADD`
- `SCRIPT_SOURCE_REMOVE`
- `SCRIPT_SOURCE_ENABLE`
- `SCRIPT_SOURCE_DISABLE`
- `SCRIPT_SOURCE_POLL_NOW`
- `SCRIPT_SOURCE_TEST`

### Mod and advisory commands

- `SCRIPT_MOD_LIST`
- `SCRIPT_MOD_GET`
- `SCRIPT_MOD_SEARCH`
- `SCRIPT_MOD_SUBSCRIBE`
- `SCRIPT_MOD_UNSUBSCRIBE`
- `SCRIPT_MOD_GET_STATUS`
- `SCRIPT_GET_MOD_ADVISORY`
- `SCRIPT_GET_ADVISORIES_FOR_LIST`

### Import/export and subscriptions

- `SCRIPT_CATALOG_IMPORT`
- `SCRIPT_SUB_LIST`
- `SCRIPT_SUB_ADD`
- `SCRIPT_SUB_REMOVE`
- `SCRIPT_EXPORT_DATA`
- `SCRIPT_IMPORT_DATA`

### Stats and preferences

- `SCRIPT_GET_STATS`
- `SCRIPT_GET_UPDATES`
- `SCRIPT_ADAPTER_LIST`
- `SCRIPT_GET_PREFS`
- `SCRIPT_SET_PREF`

These message names are part of the effective integration contract. Renaming them requires updating every caller, not only the background handler.

## Adding a source

A caller adds a source through `SCRIPT_SOURCE_ADD` with an adapter configuration.

The handler creates a source record containing:

- source ID;
- display name;
- adapter type;
- adapter configuration;
- `active` status;
- poll interval;
- null initial `lastPollAt`;
- creation/update timestamps.

The adapter type must exist in `ADAPTER_REGISTRY`. Unknown adapters are rejected explicitly.

## Manual polling and connection testing

Use `SCRIPT_SOURCE_TEST` to instantiate the configured adapter and execute its `testConnection()` implementation without performing the full persistent poll workflow.

Use `SCRIPT_SOURCE_POLL_NOW` when an immediate full source poll is required regardless of the normal recurring due calculation.

Use `SCRIPT_RUN_SCHEDULED_POLLS` to run the due-source selection logic immediately.

## Subscriptions and update views

Mods can be subscribed through the background API. A mod subscription defaults to notifications for:

- `broken`
- `updated`

`SCRIPT_GET_UPDATES` reads subscribed mods and returns those whose aggregated status is currently `updated` or `broken`.

The current handler stores these subscription preferences and state, but this wiki does not treat that storage alone as proof that every notification UI or delivery path has been freshly runtime-qualified.

## Import and export

### Full export

`ScriptDb.exportAllData()` returns a versioned export containing sources, mods, per-source mod evidence, creators, and subscriptions, together with export time and summary counts.

### Full import

`ScriptDb.importData()` supports importing the exported data model. Source imports can skip already-existing source IDs. Imported creators, mods, mod-source rows, and subscriptions are written through the same persistent stores used by live polling.

### Direct catalog import

`SCRIPT_CATALOG_IMPORT` uses the Custom List adapter to ingest supplied CSV/JSON content in batches of **50**. This is separate from the recurring ScriptPollScheduler catalog path.

## Building GameSync

The canonical GameSync repository currently declares version `0.6.3`.

From a clean checkout of [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync):

```powershell
npm ci
npm run build
```

For local development:

```powershell
npm run dev
```

The editable extension source is under `app/`; the generated production extension is under `dist/`. The repository README identifies `dist/` as the folder to load unpacked in Opera GX after a production build.

GameSync's manifest is Manifest V3 and declares both `alarms` and `storage`, which are required for this runtime.

## How to modify the polling runtime

### Add another network-backed source

1. Add a new adapter class under `app/src/script-tracker/adapters/`.
2. Extend `SourceAdapterBase`.
3. Implement `fetchCatalog()`, `getModStatus()`, and `normalizeMod()`.
4. Keep generated mod and source IDs deterministic.
5. Add the adapter to `ADAPTER_REGISTRY`.
6. Add accurate `getAdapterInfo()` metadata, especially `supportsPolling`, `requiresApiKey`, and `defaultInterval`.
7. Test configuration failure and connection failure paths.
8. Test an empty source, a large source, repeated polls, changed statuses, and duplicate identities.
9. Build the extension and exercise the real source through the actual GameSync UI/message flow.

### Add another interval type

Update `parseInterval()` in `ScriptPollScheduler.js` and ensure every UI or source-configuration surface accepts the same value. Preserve the special meaning of `manual` unless a deliberate migration is implemented.

For any future direct minute-based scheduler control, validate against the target browser's alarm floor rather than blindly accepting sub-minute values. Current Chrome documentation enforces a normal packaged-extension floor of 0.5 minutes; the existing hourly/daily/weekly source intervals are safely above it.

### Change status precedence

Change status aggregation only with explicit regression coverage. The current order is safety-oriented: `broken` outranks `working`. Changing this can hide a bad advisory when another source reports a healthier state.

### Change batch sizes

There are two different batch sizes today:

- scheduler catalog processing: 100;
- direct CSV/JSON catalog import: 50.

Treat them independently. Benchmark large catalogs before changing either value, and preserve error isolation plus event-loop yielding where relevant.

## Verification checklist

A meaningful runtime qualification should exercise all of the following:

1. Build GameSync successfully from canonical source.
2. Load the generated `dist/` extension in the intended browser.
3. Add a test source through the real UI or message flow.
4. Confirm the source survives service-worker suspension and browser restart.
5. Schedule recurring polling and verify the `script-tracker-poll` alarm exists.
6. Trigger an immediate due-source run and inspect the source's `lastPollAt` and `lastPollStats`.
7. Verify poll-log transitions from `running` to `completed`.
8. Force an adapter failure and verify a durable `error` poll record is produced while other sources continue.
9. Start two poll runs close together and confirm the overlap guard prevents a concurrent scheduler pass.
10. Exercise hourly, daily, weekly, and manual source intervals.
11. Verify a deliberately overdue source is polled when the due-source loop next runs.
12. Exercise `SCRIPT_STOP_SCHEDULER`, then `SCRIPT_SCHEDULE_POLLS` in the same live service-worker instance, fire the named alarm, and prove the listener was re-armed and `runScheduledPolls()` executes.
13. Persist scheduler-enabled intent, force the alarm object to disappear, restart/reconstruct the service worker, and prove startup reconciliation recreates the alarm only when polling is enabled.
14. Restart the browser/service worker after missing at least one expected polling window and prove one startup/wake catch-up pass polls every source that is due from persisted `lastPollAt` without replaying duplicate missed intervals.
15. Prove the alarm listener is installed synchronously when the service-worker module graph loads and that repeated worker reconstruction does not accumulate duplicate listeners in one worker instance.
16. On Opera GX, verify the actual target browser's alarm persistence behavior; do not count Chrome 150 `persistAcrossSessions` semantics as proven unless that target exposes and honors them.
17. Verify custom scheduler intervals below the target browser's supported floor are rejected or normalized truthfully rather than accepted and silently delayed.
18. Import CSV and JSON catalogs, including quoted CSV fields and duplicate rows.
19. Export Script Tracker data and import it into a clean test profile.
20. Verify mod-status precedence using conflicting multi-source evidence.
21. Verify source enable/disable and removal cascades.
22. Inspect extension/service-worker console errors after each failure case.

## Troubleshooting

### Scheduling reports that the Alarms API is unavailable

Confirm the code is running inside the built GameSync extension context and that the loaded manifest is the current Manifest V3 manifest with the `alarms` permission. A plain webpage execution context will not provide the extension Alarms API.

### Polling was stopped and then restarted, but recurring polls no longer fire

At the current verified source head, inspect the listener lifecycle first. `SCRIPT_STOP_SCHEDULER` removes the singleton's `chrome.alarms.onAlarm` listener, while `SCRIPT_SCHEDULE_POLLS` recreates only the alarm. Until the listener is explicitly reinstalled or the service worker is reconstructed, the same live scheduler instance can be left with an alarm and no callback.

Do not work around this by forcing a browser restart as the normal start path. Repair the listener lifecycle and add a stop/start regression test.

### The scheduler was enabled, but its alarm disappeared after a browser/service-worker restart

Treat scheduler intent and alarm existence as two different facts. Current GameSync source does not persist an explicit scheduler-enabled/interval record and does not reconcile the named alarm on worker startup. Platform guidance recommends checking that important alarms exist whenever the service worker starts, especially across browsers and versions where alarm persistence is not guaranteed.

A correct repair should read durable scheduler intent, call `chrome.alarms.get('script-tracker-poll')`, recreate the alarm only when enabled, and then verify actual alarm state. Do not infer that an absent alarm means the user disabled polling.

### An alarm fired later than its nominal schedule

Late delivery is permitted by the browser platform and can also follow device sleep. Do not calculate catch-up by assuming one callback per missed interval. Use persisted `lastPollAt` and the due-source loop to determine what work is actually overdue. A repeating alarm that was missed during sleep may fire once after wake and then continue from the wake-time schedule.

### A source never polls automatically

Check:

1. the source status is `active`;
2. the source's `pollInterval` is not `manual`;
3. `lastPollAt` is not newer than expected;
4. durable scheduler intent says recurring polling is enabled after the lifecycle repair;
5. the recurring scheduler alarm actually exists;
6. the scheduler's alarm listener is currently installed, especially after a prior stop/start cycle;
7. the configured adapter exists;
8. the adapter is configured and its connection test succeeds;
9. the service-worker console for scheduler or adapter errors;
10. `scriptPollLog` for durable failure history.

### A scheduled pass says a poll is already in progress

This is the intended `isRunning` guard. Inspect `SCRIPT_GET_SCHEDULER_STATUS` and current poll state before assuming the scheduler is stuck. If the browser/service worker was interrupted mid-operation, verify behavior after worker restart rather than manually forcing in-memory flags in production code.

### A single source fails but the pass continues

That is expected. Scheduled source failures are collected under `results.failed` and do not stop later sources. Inspect the corresponding `scriptPollLog` error row for the durable failure detail.

### Imported statuses look wrong

Check the source adapter's normalization rules. Custom List maps many aliases into canonical states, while Scarlet's Realm derives status primarily from the source tab name.

### A mod appears healthier than expected

Inspect every `scriptModSources` row for that mod and recompute the precedence manually. The intended order is `broken > obsolete > deprecated > updated > working > unknown`.

## Current verification boundary and open work

This documentation pass inspected the current canonical GameSync source at commit `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`. It verifies that the scheduler, IndexedDB layer, adapter registry, Scarlet's Realm adapter, Custom List adapter, message API, manifest permissions, and build scripts exist in current source.

It also verifies two related source-level lifecycle gaps in the current scheduler:

1. `stopScheduledPolls()` removes the alarm listener, while `schedulePolls()` recreates the alarm without reinstalling that listener.
2. Scheduler-enabled state and the requested global alarm interval are not durably persisted by `SCRIPT_SCHEDULE_POLLS` / `SCRIPT_STOP_SCHEDULER`, and current scheduler startup does not reconcile persisted user intent against actual alarm existence.

The first defect is directly visible in `ScriptPollScheduler.js`. The second gap is confirmed by both `ScriptPollScheduler.js` and `script-tracker-handler.js`: the scheduler messages call the methods directly, while the existing preference API does not establish a dedicated scheduler-enabled/interval contract.

This documentation pass did not execute a live Opera stop/start/restart reproduction, so these are source-proven architecture findings and still require exact runtime regression tests after repair.

Project Constellation specifically requires reliable startup catch-up. Current source proves an important part of that behavior: every due-source pass uses persisted `lastPollAt` timestamps, so an overdue source can be recognized and polled the next time `runScheduledPolls()` executes. Current browser-platform behavior strengthens the reason to keep that timestamp-driven design: delayed or sleep-missed repeating alarms do not guarantee one callback for every missed interval.

The next project-specific checkpoint should therefore repair and prove the complete state machine: same-worker stop/start listener continuity, durable scheduler intent, startup alarm reconciliation, delayed/sleep catch-up, and exact target-browser behavior. Only after those paths pass in the real built Opera GX extension should the recurring polling lifecycle be described as fully qualified.

## External platform references

These references are implementation constraints, not substitutes for GameSync runtime evidence:

- [Chrome for Developers: `chrome.alarms`](https://developer.chrome.com/docs/extensions/reference/api/alarms) - alarm delay, sleep/wake behavior, minimum period, persistence semantics, and startup-reconciliation guidance. Page last updated July 24, 2026.
- [Chrome for Developers: Events in extension service workers](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers/events) - global synchronous event-listener registration requirement.
- [Chrome for Developers: Extension service worker lifecycle](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers/lifecycle) - worker termination/restart behavior and durable-state guidance.

## Maintenance triggers

Update this wiki when any of the following materially changes:

- Script Tracker adapter registry;
- scheduling API or alarm name;
- supported poll intervals;
- alarm persistence / target-browser compatibility behavior;
- durable scheduler-intent storage;
- startup alarm reconciliation;
- overlap/cancellation behavior;
- stop/start listener lifecycle;
- startup catch-up semantics;
- IndexedDB Script Tracker tables or database version;
- status aggregation precedence;
- background `SCRIPT_*` message contract;
- source import/export schema;
- GameSync version/build layout;
- runtime qualification evidence.