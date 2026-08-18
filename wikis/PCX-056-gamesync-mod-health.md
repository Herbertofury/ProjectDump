# GameSync Mod Health Wiki

**Project Constellation ID:** PCX-056  
**Project:** GameSync Mod Health  
**Status:** ACTIVE / TRACKED  
**Canonical implementation:** `Herbertofury/Gamesync`  
**Verified source baseline:** GameSync `0.6.3`, `main` observed at commit `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`  
**Primary goal:** Detect meaningful mod-health, compatibility, version, and source signals without destructive automation. Preserve current mod state, evidence findings, and keep repairs explicit and reversible.

## What this project is

GameSync Mod Health is the mod-risk and evidence-analysis subsystem inside the shipping GameSync browser extension. It has two related but distinct jobs:

1. Maintain per-game health knowledge from configured CSV/text sources, including known-bad, needs-update, and working signals.
2. Analyze live Nexus Mods evidence from Posts and Bugs, classify issue signals, cluster them into health findings, calculate an overall Green/Yellow/Red state, generate evidence-backed notes, and feed those findings into GameSync AutoNotes.

The current implementation is not a generic one-click mod repair engine. It is an evidence and decision-support system. Its current source does not silently edit a user's installed mod state as part of the analysis path documented here.

## Canonical source map

| File | Responsibility |
| --- | --- |
| `app/src/modhealth/modhealth.js` | Core ModHealth analysis engine, issue classification, NLP augmentation, clustering, confidence, category summaries, overall health state, trend persistence, markdown generation, and AutoNotes handoff. |
| `app/src/modhealth/templates.js` | Issue-report templates for crash, performance, conflict, missing dependency, installer error, save corruption, and general bug findings. |
| `app/modules/mods-intel-suite/background/mod-health.js` | Per-game health database, CSV/text ingestion, source synchronization, normalization, merge rules, source metadata, and user override container. |
| `app/modules/mods-intel-suite/background/mod-health-evidence-bg.js` | Evidence cache, background job lifecycle, Nexus Posts/Bugs acquisition, background analysis orchestration, overlay launch, and delayed AutoNotes evidence sync. |
| `app/modules/mods-intel-suite/background/intel-message-handler.js` | Public extension-message API for `MODHEALTH_*` operations. |
| `app/content/mod-health.js` | In-page Mod Health overlay and evidence collection UI injected into Nexus pages. |
| `app/background/background.js` | Manifest V3 service-worker wiring for `ModHealthEngine`, source-sync helpers, evidence services, and Intel message routing. |
| `app/shared/keywords.js` | Shared Mod Health keyword pack, scan terms, reproduction cues, evidence-token patterns, anti-noise rules, category labels, and severity ranks consumed by the engine. |
| `app/shared/nlp-engine.js` | Shared NLP helpers used for problem likelihood, severity/confidence adjustment, sentiment, frustration, urgency, expertise, mod-tool, and error-type signals. |

## High-level architecture

```text
Configured health sources
  -> CSV/text fetch
  -> normalize + parse
  -> merge by normalized URL/name
  -> gsModHealthDb in chrome.storage.local

Nexus mod page
  -> Mod Health overlay OR background scan
  -> Nexus Posts + optional Bugs acquisition
  -> offscreen parsing
  -> evidence dedupe
       -> overlay path: evidence cache + delayed cache-based AutoNotes sync
       -> background path: direct ModHealthEngine analysis/job result
  -> ModHealthEngine
       -> classify comments
       -> apply time window
       -> build evidence hits
       -> cluster issues
       -> confidence + severity
       -> category summaries
       -> Green / Yellow / Red health
       -> trend record / alert
       -> markdown + issue templates
  -> AutoNotes ingestion
  -> user-visible evidence and follow-up workflow
```

## Shipping extension baseline

The canonical GameSync repository declares version `0.6.3`. `app/` is the editable extension source and `dist/` is generated production output. The production extension is Manifest V3 with a module service worker at `background/background.js`.

The current manifest grants the extension `scripting`, `storage`, `tabs`, `activeTab`, `alarms`, and related capabilities required by the wider GameSync runtime. Nexus pages have dedicated content-script coverage, and host permissions currently include HTTPS broadly enough for the configured evidence/source fetch paths.

## Per-game health database

The source-sync layer stores its normalized database under:

```text
gsModHealthDb
```

The current database schema is version 1 and is shaped around:

```text
{
  version: 1,
  games: {
    [modsKey]: {
      key,
      title,
      gameKey,
      sources,
      master: {
        entries,
        updatedAt
      },
      user: {
        overrides
      },
      lastSyncAt
    }
  }
}
```

### Health statuses

The current canonical statuses are:

- `bad`
- `needs_update`
- `good`

Normalization accepts common equivalents. For example, broken/crash/dead/deprecated-style wording maps toward `bad`; outdated/requires-update wording maps toward `needs_update`; working/ok wording maps toward `good`.

Severity precedence for merged source entries is intentionally conservative:

```text
bad > needs_update > unknown > good
```

When duplicate entries are merged, the more severe incoming status is retained rather than downgrading an existing warning automatically.

### Entry identity and dedupe

Health-source entries are primarily matched by:

1. normalized first URL, when available;
2. normalized mod/file name otherwise.

URL normalization removes fragments and query strings, lowercases host/path, removes `www.`, and strips trailing slashes. Name normalization lowercases text, converts `_`/`-` to spaces, removes punctuation, collapses whitespace, and trims.

### Supported source formats

The current source layer accepts:

- CSV sources;
- plain text sources parsed with health heuristics.

CSV column detection recognizes common headers for mod/name/title, status/state, URL/link/source, notes/reason/details, and file/filename/package/plugin.

Text heuristics detect health wording and recognize common mod file extensions including:

- `.package`
- `.ts4script`
- `.esp`
- `.esm`
- `.esl`

### Default Sims 4 health source

For titles inferred as The Sims 4, the current source automatically seeds a community CSV source defined by `MOD_HEALTH_DEFAULT_SIMS4_CSV` in `mod-health.js`.

This wiki documents that the shipping code references that source. It does not claim the external sheet's current contents were independently validated during this documentation pass.

### Source synchronization behavior

`mhSyncGame()` currently:

1. ensures the per-game health entry exists;
2. iterates enabled configured sources;
3. applies the injected Mod Health throttle;
4. fetches each source with `cache: "no-store"`;
5. parses CSV or heuristic text;
6. merges incoming findings;
7. records `lastFetchedAt` for successful sources;
8. records `lastSyncAt` for the game;
9. persists the normalized database;
10. returns added/updated/fetched counts plus per-source errors.

A game with no configured sources returns successfully with a `No sources configured for this game yet.` message instead of pretending it performed analysis.

## Nexus evidence-analysis pipeline

The richer Mod Health pipeline is centered on Nexus Mods evidence.

### Input context

The analysis engine accepts context including:

- mod name and version;
- game title/key/domain/version;
- Nexus mod URL and mod ID;
- scan profile;
- time window;
- operating system/hardware summary;
- mod manager and version;
- template values;
- collected comments/evidence.

Nexus URLs are normalized and parsed into game domain, mod ID, base mod URL, and Posts URL when possible.

### Scan profiles

The engine exposes three scan profiles from the shared keyword pack:

- `quick`
- `standard`
- `deep`

Unknown profile values fall back to `standard`.

The public configuration also currently reports:

- Mode A enabled;
- Mode B disabled;
- configured category labels;
- available report templates;
- a minimum search-character threshold from the keyword pack.

### Time windows

The analysis engine supports numeric day windows and all-time behavior. Background/overlay call sites currently default to 90 days when no explicit window is supplied.

### Background page limits

Background scans currently default to three Nexus Posts pages. The page cap is clamped to a minimum of 1 and maximum of 20.

### Bugs collection

Bugs collection is enabled by default unless `includeBugs` is explicitly set to false. The background job starts the Bugs request in parallel with Posts acquisition and later merges both sources before analysis.

### Evidence dedupe

Collected comments/evidence are deduplicated before classification. Evidence records are also deduplicated by a composite of:

- matched term;
- leading snippet text;
- evidence URL or page URL.

The in-memory/IndexedDB evidence cache retains at most 2,000 normalized evidence rows per cache entry.

## Evidence cache and background jobs

### Evidence cache

The background evidence layer uses:

- an in-memory `Map` for hot access;
- the Intel IndexedDB `cacheEntries` table for persistence across the immediate in-memory lifecycle.

Current evidence TTL:

```text
2 hours
```

Cache rows are stored under keys prefixed with:

```text
modhealth:evidence:
```

The overlay creates a logical cache key containing the game, mod ID, and normalized Nexus URL, then uses the `MODHEALTH_EVIDENCE_APPEND`, `MODHEALTH_EVIDENCE_GET`, and `MODHEALTH_EVIDENCE_CLEAR` message paths. The evidence helper itself adds the storage prefix when it persists that logical key to `cacheEntries`.

### Background jobs

Background scan jobs are stored in an in-memory `Map` and carry status, progress, phase, message, input, result, and timestamps.

Current background-job TTL:

```text
30 minutes since last update
```

This matters operationally: background job status is not a durable long-term task log. After cleanup or a service-worker lifecycle change, a previously returned job ID may no longer resolve.

### Verified background-scan evidence-cache divergence

A source-level completeness pass found an important distinction between the interactive overlay path and `MODHEALTH_RUN_BACKGROUND`.

In the current `mod-health-evidence-bg.js` background job implementation:

1. Posts and optional Bugs evidence are fetched and deduplicated into `allCollected`.
2. A local `evidenceCacheKey` is built as `modhealth:evidence:<normalized source URL>`.
3. That key is passed to `modHealthEvidenceClear()`.
4. The same `evidenceCacheKey` symbol has no later append/read use in the background-job path.
5. `allCollected` is passed directly to `intel.modHealth.analyzeRun(...)`.
6. The resulting analysis is stored on the transient background job and may be ingested by the analysis engine into AutoNotes.

This means a successful background scan is **not currently proven to populate the overlay evidence cache** that `MODHEALTH_EVIDENCE_GET` rehydrates. It also uses a different logical key shape from the overlay's game/mod/URL key. The direct analysis result is still real and the analysis engine's direct AutoNotes handoff can still occur; the gap is specifically continuity between background-collected evidence and the overlay/cache surface.

This is source-proven behavior, not a claim that evidence disappears from every user workflow. It matters because a user can complete a background scan, later open the overlay for the same mod, and reasonably expect the previously collected evidence rows to be available through the same two-hour cache. Current source does not establish that guarantee.

#### Repair/acceptance contract

If background and overlay evidence are intended to share one continuity surface, the repair should use one canonical logical cache-key builder and one append path rather than introducing another store or hidden compatibility layer.

At minimum, regression verification should prove:

1. start `MODHEALTH_RUN_BACKGROUND` for a known Nexus mod;
2. wait until `MODHEALTH_BACKGROUND_STATUS` reports `done`;
3. capture the exact evidence rows used by the completed analysis;
4. open the Mod Health overlay for the same game/mod/URL;
5. verify `MODHEALTH_EVIDENCE_GET` returns the same deduplicated evidence set under the canonical key;
6. reload the extension/service worker while the two-hour TTL remains valid and verify persisted evidence rehydrates from IndexedDB;
7. clear the evidence and prove both memory and IndexedDB copies for that canonical key are removed;
8. verify direct analysis AutoNotes ingestion and cache-triggered delayed AutoNotes synchronization do not duplicate the same finding;
9. verify a different mod, game, or Nexus URL cannot collide with the first mod's evidence key.

Until that is implemented and exercised, treat background-job `result`/AutoNotes output and overlay evidence-cache continuity as separate verified behaviors.

## Core analysis engine

`ModHealthEngine` is the authoritative health-analysis layer.

### Processing sequence

`analyzeRun()` currently performs this sequence:

1. normalize project/mod/game context;
2. derive Nexus identifiers when possible;
3. batch-run NLP over comment text on a best-effort basis;
4. classify individual comments;
5. deduplicate classified comments;
6. apply the configured time window;
7. build and merge evidence hits;
8. aggregate issue clusters;
9. summarize categories;
10. compute Green/Yellow/Red overall health;
11. record daily trend state and compute a trend alert in parallel;
12. generate per-issue report text;
13. generate summary Markdown;
14. compute aggregate NLP statistics;
15. ingest the complete finding into AutoNotes when available.

The returned analysis contains:

- context;
- scanned and analyzed comment counts;
- issue count;
- evidence hits;
- overall health;
- categories;
- issue clusters;
- issue notes;
- summary Markdown;
- NLP aggregate;
- trend record;
- trend alert;
- AutoNotes ingestion result.

## Classification and confidence behavior

### Recency weighting

Current recency weights are:

| Evidence age | Weight |
| --- | ---: |
| 0 to 14 days | 1.0 |
| 15 to 30 days | 0.8 |
| 31 to 90 days | 0.6 |
| older/unknown | 0.4 |

### Issue aggregation

Findings are grouped by:

```text
category + signatureKey
```

Each issue cluster tracks:

- severity;
- matching comments;
- source links;
- unique reporters;
- confidence;
- NLP aggregate information when available.

Issue ordering favors, in order:

1. higher severity;
2. higher confidence;
3. more unique reporters;
4. more mentions.

### Confidence boosts

The current engine can raise cluster confidence based on additional independent evidence:

- 3 or more unique reporters: +0.06;
- 5 or more unique reporters: +0.12;
- high average frustration: up to +0.08;
- multiple NLP error-type classes: up to +0.06;
- expert-reporter signal: +0.05;
- at least 3 recent comments within 14 days and at least 5 mentions total: +0.07.

Confidence remains clamped to 1.0.

## Overall Green / Yellow / Red health

The overall indicator is derived from issue severity, confidence, reporter diversity, NLP frustration, and issue volume.

Current Red paths include:

- critical stability issue with confidence at least 0.70 and at least 3 reporters;
- major compatibility/installation issue with at least 5 reporters and confidence at least 0.62;
- critical issue with average NLP frustration above 0.65 and confidence at least 0.55;
- at least 3 high-confidence major-or-higher issue clusters.

Current Yellow paths include:

- major-or-higher issue with confidence at least 0.50;
- moderate-or-higher issue with confidence at least 0.40;
- at least 15 total mentions across at least 4 issue clusters.

Otherwise the current engine reports Green.

These are implementation thresholds, not a guarantee that every community report is correct. The evidence links and confidence breakdown are part of the decision surface for that reason.

## Trend tracking

The engine can persist daily trend records in the Intel database table:

```text
modTrendDaily
```

Trend identity includes game, mod, and day. Daily records accumulate warning count, stability/crash mentions, update signals, and severity.

A trend alert requires enough history. The current implementation returns no trend alert until at least eight records exist. It compares recent severity totals and emits an alert when the current window reaches at least 2x the previous window under the engine's minimum-signal conditions.

## AutoNotes integration

Mod Health is integrated with AutoNotes in two ways.

### Analysis result ingestion

After `analyzeRun()` produces a complete finding, the engine calls:

```text
autonotes.ingestModHealthFinding(...)
```

when AutoNotes is available.

Username redaction is enabled by default unless explicitly disabled by the caller.

### Evidence-cache sync

The interactive evidence path can queue a short delayed AutoNotes synchronization after evidence is appended. This prevents each individual evidence row from requiring an immediate full note rebuild while still keeping AutoNotes aligned with the evidence cache.

The current background-job path should be considered separate: it passes collected comments directly to `analyzeRun()` and does not currently prove an append into the overlay evidence cache described above.

## Report templates

The current template system provides specialized generated reports for:

- Crash / CTD;
- Performance;
- Conflict / Load Order;
- Missing Dependency / Version Mismatch;
- Installer Error;
- Save Corruption;
- General Bug.

Templates preserve evidence-oriented fields such as confidence, environment, reproduction steps, source links, requested logs, dependency/load-order context, suggested isolation steps, and generated-by version metadata.

## Extension message API

`intel-message-handler.js` currently exposes these `MODHEALTH_*` operations:

| Message | Purpose |
| --- | --- |
| `MODHEALTH_GET_CONFIG` | Read public scan profiles/categories/templates/config. |
| `MODHEALTH_ANALYZE` | Run the ModHealth engine directly on supplied evidence/context. |
| `MODHEALTH_EVIDENCE_APPEND` | Append normalized evidence rows to a cache key and optionally queue AutoNotes sync. |
| `MODHEALTH_EVIDENCE_GET` | Read cached evidence. |
| `MODHEALTH_EVIDENCE_CLEAR` | Clear cached evidence. |
| `MODHEALTH_RUN_BACKGROUND` | Queue a background Nexus scan and return a job ID. |
| `MODHEALTH_BACKGROUND_STATUS` | Read the current in-memory background job state. |
| `MODHEALTH_OPEN` | Open/inject the interactive Mod Health overlay for a Nexus target. |

These messages run through the same Intel message router used by AutoNotes, relations, packs, folders, and other GameSync intelligence systems.

## Interactive overlay

`app/content/mod-health.js` provides the injected Nexus-side overlay.

Verified overlay behavior includes:

- one-instance bootstrap via `window.__gsModHealthOpen`;
- local running/paused/abort state;
- scan progress state;
- evidence collection and dedupe;
- persisted evidence reload through `MODHEALTH_EVIDENCE_GET`;
- background evidence append with optional AutoNotes sync;
- direct navigation back into the GameSync library/AutoNotes view;
- a fixed high-z-index dark UI intended to coexist with Nexus pages;
- safe-area-aware placement and scrollable internal content.

The overlay can be injected by the background service worker after opening/reusing the target Nexus Posts tab.

## Building and installing GameSync with Mod Health changes

Work in the canonical GameSync checkout containing `package.json` and `app/`.

```powershell
npm ci
npm run build
```

For development mode:

```powershell
npm run dev
```

The current repository README defines:

- `app/` as editable source;
- `dist/` as generated production extension output;
- `dist/` as the folder to load unpacked in Opera GX.

After any Mod Health source change, rebuild so `dist/` is regenerated from `app/`.

## Test and verification reality

The shipping `package.json` currently exposes:

- `npm run dev`
- `npm run build`
- Bounty-specific tests/benchmark
- preview and legacy WASM build support

It does **not** currently expose a dedicated `test:modhealth` npm script in this repository. The current `app/test/` tree contains the dedicated Bounty suite plus WASM performance fixtures, but no Mod Health test directory.

Therefore a Mod Health change should not be declared verified merely because the extension builds. The minimum practical qualification should include the real affected paths below.

### Recommended Mod Health qualification checklist

1. `npm ci` succeeds from a clean checkout.
2. `npm run build` succeeds.
3. Load the rebuilt `dist/` into the actual target Opera/Chromium profile.
4. Confirm the extension service worker starts without Mod Health import errors.
5. Open a valid Nexus mod target through the real GameSync UI.
6. Verify `MODHEALTH_OPEN` creates/reuses the correct tab and injects the overlay.
7. Run Quick, Standard, and Deep profiles on representative evidence.
8. Verify time-window filtering.
9. Verify Posts pagination up to the configured cap.
10. Verify Bugs inclusion and Bugs-disabled behavior.
11. Verify evidence rows retain direct source links.
12. Verify duplicate evidence does not multiply findings.
13. Verify a background scan transitions queued -> running -> done/error truthfully.
14. Verify `MODHEALTH_BACKGROUND_STATUS` reports the same job while it remains live.
15. Verify background-collected evidence can be rehydrated through the intended overlay/cache path if shared continuity is part of the product contract; current source does not prove this.
16. Verify source-fetch failure is surfaced in returned errors rather than converted into a false success finding.
17. Verify CSV and text health-source import with malformed/partial rows.
18. Verify severe existing entries are not silently downgraded by a weaker duplicate.
19. Verify AutoNotes receives the intended Mod Health finding and preserves evidence without duplicate ingestion between direct analysis and delayed cache sync.
20. Verify username redaction default behavior.
21. Verify evidence cache reload and expiration behavior, including service-worker restart while the TTL remains valid.
22. Verify extension reload/restart does not corrupt `gsModHealthDb`.
23. Inspect extension/page console logs for Mod Health errors.

## How to modify the subsystem

### Add or change a health-source parser

Work primarily in:

```text
app/modules/mods-intel-suite/background/mod-health.js
```

Preserve:

- normalized identity rules;
- severity-preserving merge behavior;
- source labels;
- source-specific fetch errors;
- user overrides;
- existing per-game history.

Do not turn parser ambiguity into a destructive status change.

### Add a new scan signature/category

Start with the shared keyword/category definitions used by `ModHealthEngine`, then update templates only if the new category needs a specialized report.

Verify that:

- anti-noise rules still suppress obvious false positives;
- the new signature does not swallow unrelated categories;
- severity ordering remains sensible;
- evidence links remain attached;
- existing Green/Yellow/Red thresholds do not become accidentally over-sensitive.

### Change overall-health thresholds

Modify only with evidence-backed tests/fixtures. Threshold changes alter user-facing risk classification across every supported mod and should be treated as behavior changes, not cosmetic tuning.

### Add a new report template

Add it to:

```text
app/src/modhealth/templates.js
```

Then make sure category-to-template selection is defined and the public config still exposes the intended template list.

### Change overlay behavior

Work in:

```text
app/content/mod-health.js
```

Preserve:

- one-instance behavior;
- canonical evidence cache key semantics;
- truthfully displayed progress;
- source links;
- pause/abort state;
- Nexus page usability;
- ability to close/reopen the overlay.

### Change background acquisition

Work in:

```text
app/modules/mods-intel-suite/background/mod-health-evidence-bg.js
```

Preserve bounded pagination, explicit Bugs inclusion, per-phase progress, job errors, and evidence dedupe. Avoid unbounded crawling or hidden background loops.

If the background path is made cache-aware, reuse the same logical cache-key contract and evidence append helpers as the overlay. Do not create a third evidence identity model.

## Troubleshooting

### Overlay does not open

Check:

1. the target URL is a valid Nexus mod URL;
2. the service worker is loaded from the newest `dist/` build;
3. `scripting` and `tabs` permissions are present;
4. `content/mod-health.js` exists in the generated build;
5. the tab reached a completed load state;
6. the page console has not rejected the injected bootstrap.

`MODHEALTH_OPEN` returns an explicit error if a Nexus URL cannot be normalized, the Posts URL cannot be built, a tab cannot be opened, or the overlay bootstrap is missing.

### Background job ID is not found

The job registry is in memory and has a 30-minute inactivity TTL. A service-worker restart or cleanup can make an old job ID unavailable. Treat the returned analysis/AutoNotes record as the durable result surface, not the transient job map.

### Background scan completed but the overlay has no cached notes

First distinguish the background analysis result from the overlay cache. Current source proves that `MODHEALTH_RUN_BACKGROUND` can collect comments and pass them directly to `analyzeRun()`, but the background-job path does not currently prove a matching `MODHEALTH_EVIDENCE_APPEND` into the overlay cache. Opening the overlay later can therefore legitimately expose an empty cache even though the earlier job completed.

Check the background job's `result`, direct AutoNotes output, and the overlay's logical cache key separately. If shared continuity is expected, fix the source to reuse one canonical cache-key builder and append path, then run the background-to-overlay regression contract above.

### Evidence appears empty

Check:

- target Nexus URL and game domain;
- Posts/Bugs fetch success;
- the configured time window;
- scan-profile terms;
- offscreen extraction output;
- cache-key consistency;
- whether the evidence came from the interactive overlay path or only a background job;
- whether evidence expired after its two-hour TTL.

### Health-source sync finds nothing

A per-game source sync can validly have zero sources. Confirm `sources` exists for the game and that each desired source is enabled and has a URL.

For CSV sources, confirm headers map to recognized name/status/url/notes/file fields or use the fallback column order.

### A known warning was downgraded unexpectedly

The merge layer is designed to retain the more severe status. Check whether the incoming row matched the same normalized URL/name. If identity changed, the system may be creating a separate entry rather than merging.

### Too many false positives

Review:

- keyword/signature rules;
- anti-noise patterns;
- scan profile;
- time window;
- source duplication;
- reporter diversity;
- NLP frustration/expertise boosts;
- category thresholds.

Do not solve false positives by hiding evidence. Preserve the source rows and correct classification logic upstream.

### Overall health changes unexpectedly

Inspect the issue clusters that contributed to the overall state. Red/Yellow classification is threshold-based and can change when reporter count, confidence, severity, frustration, issue diversity, or mention volume crosses a boundary.

## Data preservation rules

When changing Mod Health:

- do not overwrite user overrides silently;
- do not convert ambiguous source text into a destructive automated repair;
- preserve direct evidence URLs;
- preserve source labels and timestamps;
- preserve the user's current mod/library state;
- prefer additive migration for schema changes;
- keep findings distinguishable from user decisions;
- keep scan failures visible instead of generating a false Green state;
- keep status/analysis changes reversible at the data layer where possible.

## Current verified boundary

This documentation pass verified the current source structure and behavior from the canonical GameSync repository at version `0.6.3` and observed `main` commit `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`.

The pass additionally verified from source that the interactive overlay and background scan do not currently share a proven evidence-cache append lifecycle: the background job builds and clears its own local cache key, then analyzes `allCollected` directly, while the overlay owns the append/get path. No fresh live Opera Mod Health scan, external Nexus fetch, source-sheet fetch, or end-to-end AutoNotes round trip was executed during this wiki update, so the user-visible impact of that continuity gap remains a required runtime qualification item rather than an inferred failure count.

The previous Project Constellation summary for PCX-056 was intentionally generic. This wiki supersedes that summary with current project-owned implementation evidence while preserving the original project goal: evidence-backed detection without destructive automation.

## Maintenance triggers

Update this wiki when any of the following materially changes:

- GameSync version or canonical repository/branch;
- `ModHealthEngine` scoring or overall-health thresholds;
- keyword/signature packs;
- scan profiles;
- evidence TTL or background-job lifecycle;
- evidence-cache keying or background/overlay continuity;
- database schema/storage keys;
- source formats or default sources;
- Nexus acquisition/parsing behavior;
- AutoNotes integration;
- overlay workflow;
- `MODHEALTH_*` message API;
- report templates;
- build/install procedure;
- dedicated Mod Health tests or runtime qualification evidence.
