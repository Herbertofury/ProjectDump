# UltraDeck Wiki

**Project Constellation ID:** `PRJ-025`  
**Status:** ACTIVE  
**Canonical connected repository:** [Herbertofury/UltraDeck](https://github.com/Herbertofury/UltraDeck)

## Purpose

UltraDeck is a lossless ultrawide multi-column feed engine for Tumblr, Patreon, X, and the Twitter compatibility hostname. Its core contract is to increase information density and preserve feed history without hiding, culling, virtualizing, or degrading off-screen content.

## Current verified version

The current project-owned repository README identifies **UltraDeck v8.1.0** as the newest fully described recovered/hardened line. This supersedes the older Project Constellation catalog summary that still listed v7.5.0.

The repository describes v8.1.0 as reconstructed from the exact verified v8.0.0 source plus the recovered v8.1.0 WIP-009 prepackage source patch, followed by additional hardening for current Patreon and X feed semantics.

## v8.2 source staging detected

A newer **v8.2.0 source bootstrap is currently being staged in the canonical UltraDeck repository**, but it is not yet treated as the latest verified usable release in this wiki.

Current repository evidence at this checkpoint:

- commit `f7f06eedabdbbeda2df64ba02b447d46289cc3cb` began `Stage UltraDeck v8.2.0 source bootstrap`;
- commits have advanced through `da8730240779d1e2508737a0b8c5eee38a0bd11d`, message `Stage UltraDeck v8.2 bootstrap 005/018`;
- `bootstrap/` currently exposes `v82.b64.000` through `v82.b64.004`, each 8,000 bytes, plus the earlier `source.b64.000` bootstrap material;
- the numbered commit sequence explicitly indicates an 18-part transfer, so the currently visible five parts are incomplete.

Because the v8.2 source transfer is incomplete, do not promote v8.2.0 to the verified release line yet. The correct next step is to wait for all numbered parts, reconstruct the source deterministically, verify archive/hash integrity and version metadata, inspect the complete source tree and changelog, then run its own build/test/package/runtime gates. Until that succeeds, v8.1.0 remains the newest fully documented usable line and the v8.2 staging is recorded as an in-progress successor.

## v8.1.0 behavior recorded by the canonical README

Current hardening includes:

- selected top-level feed/tab state in route identity so same-URL feed switches do not mix retained histories;
- X timestamp-permalink identity so quoted/referenced status links do not steal the outer post ID;
- X exact-ID source restoration across every matching status link;
- Patreon semantic `role="article"` support with permalink-derived identity fallback;
- broader Patreon Share / Reshare / Repost action coverage;
- broader X Reply / Repost / Bookmark / Share / More native-action coverage;
- preserved off-screen native-control restoration without moving the visible UltraDeck deck;
- preserved no-culling behavior.

## Hard no-culling contract

UltraDeck must not solve performance problems by reducing the user's feed content. The current repository explicitly preserves:

- no viewport virtualization as a correctness shortcut;
- no hidden retained cards;
- no `content-visibility` behavior that makes retained content unavailable;
- no quantity cap.

Performance work should improve processing, identity, scheduling, caching, event handling, and DOM interaction while keeping every retained card fully available.

## Supported surfaces

The current README identifies support/recovery work for:

- Tumblr
- Patreon
- X
- Twitter compatibility hostname

Each adapter must preserve the source site's identity and native actions rather than treating every feed as a generic card list.

## Feed identity model

A feed card's identity must be stable enough to retain history and restore native interactions without false merges.

Important v8.1.0 rules include:

### Route/feed identity

Top-level selected feed/tab state is part of route identity where the URL alone is insufficient. Two different feeds that share a URL must not share retained history accidentally.

### X identity

Use the outer post's correct status/timestamp permalink identity. Quoted or referenced posts inside a card must not steal the outer card's identity.

### Patreon identity

Support semantic article containers and permalink-derived fallback identity so layout changes do not immediately destroy card identity.

## Native controls and source restoration

UltraDeck should preserve access to native source actions. Retained/off-screen content may require restoring or reconnecting native controls, but that work must not move or collapse the visible UltraDeck deck.

For current Patreon/X coverage, verify the real actions promised by the adapter rather than assuming a selector match means the interaction still works.

## Current repository packaging evidence

The canonical README references these v8.1.0 deliverables:

- complete v8.1.0 source archive;
- Chromium MV3 build;
- Firefox MV3 build;
- Patreon userscript;
- X/Twitter userscript;
- Tumblr userscript;
- recovered WIP-009 source patch.

The currently connected repository surface exposes the README plus bootstrap transfer material, but not the complete referenced v8.1.0 release tree through the root contents API. Treat the README as version/lineage evidence, while separately verifying release artifact presence before presenting any package as downloadable/current.

## Historical Project Constellation evidence

The older durable Project Constellation record preserved v7.5.0 performance and artifact history, including startup/reload A/B tests, mutation-hotpath A/B tests, off-screen interaction checks, no-cap scaling checks, real MV3 checks, media-network checks, and release/source artifacts.

That history remains valuable as regression evidence, but it is no longer the newest version claim because the project-owned repository records v8.1.0 and now also contains an incomplete v8.2 successor transfer.

## Development workflow

The canonical README says the complete source archive contains the WXT/TypeScript shell, portable builder, shared runtime, adapters, research notes, regression fixtures, and performance tests. Until the source archive is directly present/verified in the connected repository, do not invent package commands here.

When the complete verified source is resolved:

1. verify archive identity/hash;
2. extract to a fresh location;
3. read repository/package manifests;
4. install exact dependencies from lockfiles;
5. run project-provided lint/type/unit/performance checks;
6. build Chromium/Firefox/userscript outputs;
7. exercise Tumblr, Patreon, and X in real authenticated sessions where required;
8. compare retained-card counts and identities against source feeds;
9. verify native controls for visible and retained/off-screen cards;
10. verify reload/navigation/feed-tab behavior;
11. prove no viewport/culling regression.

For v8.2 specifically, add a prerequisite before step 1: reconstruct all numbered bootstrap parts and prove the reconstructed archive/source is complete before treating any v8.2 command or changelog as authoritative.

## Adapter verification checklist

For each supported platform:

- feed detection works;
- route/feed identity is correct;
- card identity is stable;
- duplicate cards are isolated correctly;
- quoted/referenced content cannot steal outer identity;
- native actions remain usable;
- retained cards survive expected navigation/reload behavior;
- top/bottom scrolling does not discard content;
- content quantity is preserved;
- source restoration does not move the visible deck;
- platform layout changes fail visibly rather than silently corrupting history.

## Performance verification

A performance change is acceptable only if it preserves the no-culling contract. Compare before/after on the same captured or live workload and record:

- card count;
- identity collisions;
- mutation processing cost;
- startup/reload cost;
- scrolling behavior;
- native action restoration;
- memory growth;
- responsiveness;
- errors/recovery.

Do not use one faster synthetic result as proof of overall improvement if feed completeness or native controls regress.

## Troubleshooting

### Two different feeds merge history

Check route identity and selected top-level feed/tab state. Same URL does not always mean same logical feed.

### X card gets the quoted post ID

Inspect outer timestamp/permalink identity. Referenced/quoted status links must not override the outer post identity.

### Patreon cards stop resolving after layout changes

Check semantic article detection and permalink fallback before adding brittle one-off selectors.

### Off-screen cards lose native actions

Use the restoration path without moving/hiding the visible UltraDeck deck. Verify exact source action behavior after restoration.

### Performance work suggests virtualizing cards

Reject that approach for UltraDeck's core retained-feed behavior. Optimize processing while preserving all retained cards.

### A v8.2 bootstrap part appears

Do not treat a partial chunk set as a complete release. Confirm the expected part count/order, reconstruct only after the full transfer is present, verify bytes/archive integrity, inspect the actual v8.2 manifests/changelog, then run the real verification suite before promotion.

## Current documentation gap

The connected repository now exposes the README and an actively growing v8.2 multi-part source bootstrap, but the complete v8.2 transfer is not yet present and the complete v8.1 release/source tree referenced by the README is not exposed at the repository root. The next documentation upgrade should ingest the fully reconstructed v8.2 source once all parts are present, then add exact install/build/test/package commands and module-level architecture from that verified source.

## Wiki maintenance

Update this page when platform adapters, route/card identity rules, no-culling guarantees, release artifacts, source layout, performance evidence, bootstrap completion, or the verified latest version changes. Preserve older performance/verification evidence as regression history rather than deleting it.