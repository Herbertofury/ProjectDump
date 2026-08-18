# UltraDeck Wiki

**Project Constellation ID:** `PRJ-025`  
**Status:** ACTIVE  
**Canonical connected repository:** [Herbertofury/UltraDeck](https://github.com/Herbertofury/UltraDeck)

## Purpose

UltraDeck is a lossless ultrawide multi-column feed engine for Tumblr, Patreon, X/Twitter and TikTok. Its core contract is to increase information density and preserve feed history without hiding, culling, virtualizing or degrading off-screen content.

## Current verified source line

The canonical repository still identifies **UltraDeck v8.5.0** as the package/source version. Commit `2b697933ff46513282cc8f0ef38df6e70dc79aab`, dated 2026-08-17, is the v8.5.0 release commit and updates the repository changelog/README to 8.5.0.

Current `main` has a newer verified post-release implementation head: `e1da516a7aad9a254443e4a3e48830b98a1c772b`, merged from pull request #1, **Recover interrupted opt-in Surround layout**. `package.json` still reports `8.5.0`, so the correct documentation boundary is: **v8.5.0 package identity with a verified post-release Surround-mode delta on current main**. Do not invent a newer semantic version until the project actually declares one.

This supersedes the older Project Constellation documentation that stopped at v8.1.0 and treated v8.2 as an incomplete bootstrap. The later repository history records complete v8.4 and v8.5 release work, cleanup of the one-shot v8.5 publisher, and the subsequent verified Surround recovery.

## Verified post-release Surround mode

Current main adds an optional **Surround mode** that preserves the familiar native center feed while UltraDeck keeps retained cards in adaptive side lanes around it.

The feature is deliberately **off by default**. Full-deck UltraDeck remains the default behavior.

### Product behavior

When Surround mode is enabled:

- the site's native center feed remains visible and interactive;
- UltraDeck uses two retained side lanes, one on each side of the native center feed;
- existing retained-card capture, Interaction Capsules, media behavior, buffering, TikTok recovery, site boot gates and the no-culling contract remain active;
- the presentation changes, but the retained cache and underlying product behavior are not replaced by a second feed engine;
- on narrow viewports the Surround shell is hidden rather than forcing unusable side lanes.

When Surround mode is disabled, UltraDeck returns to the normal full-deck presentation.

### Controls and persistence

Surround is available through:

- a current-site toggle in the popup;
- a runtime HUD toggle;
- per-site controls in Options for Tumblr, Patreon, X/Twitter and TikTok.

The extension stores per-site Surround preferences in:

```text
chrome.storage.local["ultradeckSurroundSites"]
```

Default values are false for every supported site:

```text
tumblr: false
patreon: false
x: false
tiktok: false
```

The bridge restores the current site's Surround value into the page runtime as `settings.surroundMode`. A per-site Surround change can be applied to the active enabled site without using the site-enable boot-gate reload path.

### Adaptive geometry

`shared-runtime-source/surround-mode.js` computes the center and side widths from the current viewport. Verified implementation constants include:

```text
SURROUND_MIN_SIDE = 184
SURROUND_MAX_SIDE = 430
SURROUND_MIN_CENTER = 440
SURROUND_MAX_CENTER = 760
```

The implementation targets two side columns while Surround is active. It temporarily constrains the shared column layout to two lanes and then restores the user's ordinary column settings outside that calculation, rather than overwriting the stored full-deck configuration.

### Important source files

| Path | Verified responsibility |
| --- | --- |
| `shared-runtime-source/surround-mode.js` | Surround state, adaptive center/side geometry, visibility and pointer-event presentation, two-lane layout wrapper, runtime HUD control and diagnostics. |
| `shared-runtime-source/build_runtime.py` | Includes `surround-mode.js` in generated runtimes. |
| `entrypoints/bridge.content.ts` | Restores and persists per-site Surround state through `ultradeckSurroundSites`. |
| `entrypoints/popup/index.html` / `entrypoints/popup/main.ts` | Current-site Surround toggle in the extension popup. |
| `public/options.html` / `public/options.js` | Per-site Surround settings for Tumblr, Patreon, X/Twitter and TikTok. |
| `tests/test_surround_contract.py` | Static source/build contract for default-off persistence, target wiring, two-column behavior, native-source visibility and the no-`content-visibility` requirement. |
| `tests/verify_surround_browser.py` | Real headless-Chromium toggle test using the built Tumblr userscript. |

### Verified runtime and CI evidence

The recovered Surround checkpoint records these passes before merge:

- npm dependency install;
- TypeScript typecheck;
- WXT Chromium MV3 production build;
- WXT Firefox MV3 production build;
- shared runtime generation;
- portable Chromium and Firefox builds;
- Python compile checks;
- JavaScript syntax checks for source and generated runtimes;
- Surround contract test;
- real headless-Chromium runtime toggle test.

The verified recovery branch head `d08cd7d9e80d2e96e0f2db973e9865b47c59733d` completed GitHub Actions verify run `32087223402` successfully before merge.

The real browser test loads the actual built Tumblr userscript against an eight-post synthetic feed and exercises **Surround off -> on -> off**. The recorded result proves:

- native retained-source nodes are hidden in the normal full-deck state;
- enabling Surround makes the native source visible and interactive with `pointer-events:auto`;
- diagnostics report Surround active;
- all eight posts remain retained;
- exactly two side columns are requested;
- center and side widths are measured from real browser layout state;
- turning Surround off restores the original full-deck source-visibility state.

This is real built-runtime browser proof. It is not authenticated end-to-end production-site proof across Tumblr, Patreon, X and TikTok, which remains part of live qualification.

## v8.5 first-class TikTok adapter

TikTok is now a first-class adapter rather than a generic fallback.

The canonical README records:

- canonical `/@user/video/<id>` identity plus feed-container/xgplayer discovery;
- retained Like, Repost, Comment/Reply, Share, Favorite/Bookmark, menu, poll, permalink and input actions through the Interaction Capsule system;
- direct TikTok media URLs retained as playable `<video>` elements with controls;
- safe fallback for blob/MSE-only media instead of creating a second blind decoder;
- native and retained-video playback observation;
- native Retry/Try Again preference before bounded media reload/play recovery;
- recovery coverage for network/decode/no-source/waiting/stalled and watchdog-detected stuck playback;
- per-video rate limiting so permanently unavailable media cannot create retry storms.

The important design boundary is that playback repair targets only failing/stalled media. It does not refresh the whole feed or mass-reload healthy videos.

## Per-site enable/disable is a real boot gate

The extension exposes an **Enabled sites** options page plus matching popup toggles for:

- Tumblr;
- Patreon;
- X / Twitter;
- TikTok.

All are enabled by default. Disabling a site is a true runtime boot gate: UltraDeck does not start its deck, media accelerators or site-specific playback hooks on that site. Changing a site setting reloads only affected open tabs.

This is separate from Surround mode. A disabled site must stay disabled even if its stored Surround preference is true. Surround changes presentation only after the site's main UltraDeck boot gate is enabled.

## Persistent native interaction

Retained cards reconnect actions to the source site's live controls. Current v8.5 documentation preserves the v8.3/v8.4 Interaction Capsule and post-context work, including Like/Reblog/Repost, Reply/Comment, Share, bookmarks, polls, menus and inputs.

Active draft text, expanded/thread state, menus, poll selections and other per-post context can survive source-card recycling and same-tab reload behavior. Raw saved HTML is not sufficient authority because framework handlers must be reconnected to current source controls.

Surround must preserve the same interaction contract in both the native center feed and UltraDeck side lanes. Do not treat the center feed as a decorative preview.

## Hard no-culling contract

UltraDeck must not solve performance problems by reducing feed content. Current source explicitly preserves:

- no viewport virtualization as a correctness shortcut;
- no card culling;
- no hidden retained posts as a data-loss/performance mechanism;
- no `content-visibility` shortcut that makes retained content unavailable;
- no quantity cap;
- no reduced media quality;
- no disabled off-screen controls.

Every retained card stays mounted and actionable. Performance work must improve scheduling, identity, event handling, DOM interaction, caching and targeted media recovery while preserving complete retained content.

Surround does not weaken this rule. The two visible side lanes are a presentation choice, not permission to discard retained records or stop processing off-screen content.

## Supported surfaces

Current v8.5 supports:

- Tumblr;
- Patreon;
- X;
- Twitter compatibility hostname/path behavior;
- TikTok.

Each adapter must preserve source-site identity and native actions rather than treating every feed as a generic card list.

## Feed identity model

A feed card's identity must be stable enough to retain history and restore native interactions without false merges.

### Route/feed identity

Top-level selected feed/tab state remains part of route identity where the URL alone is insufficient. Different logical feeds sharing one URL must not accidentally share retained history.

### X identity

Use the outer post's correct status/timestamp permalink identity. Quoted or referenced posts inside a card must not steal the outer card's identity.

### Patreon identity

Preserve semantic article detection and permalink-derived fallback identity so layout changes do not immediately destroy card identity.

### TikTok identity

Use canonical video identity from `/@user/video/<id>` where available, with current feed/xgplayer evidence as supporting discovery. Avoid false merges across reposted/referenced media or recycled native containers.

## Native controls and source restoration

Retained/off-screen content may require restoring or reconnecting native controls, but source recovery must not move, collapse or replace the visible UltraDeck deck.

In normal full-deck mode the native retained-source nodes remain hidden as part of source ownership/restoration behavior. In Surround mode the explicitly marked native source is made visible and interactive so the normal center feed can coexist with the retained side lanes.

For every supported platform, qualification must exercise the actual promised actions, not merely confirm that a selector matched.

## Jank reduction without culling

v8.5 preserves the prior Nocturne-style performance line:

- scroll storms are animation-frame coalesced;
- geometry audits are input-aware and time-sliced;
- irrelevant Patreon/X identity mutations are rejected early;
- exact source identities are cached;
- rail/top-chrome discovery is scoped before fallback scanning;
- repeated rail writes are idempotent;
- interaction metadata is captured lazily where practical;
- TikTok playback recovery is targeted and bounded.

Surround reuses the same runtime and geometry audit path. Any optimization remains subordinate to full-retention and exact-interaction correctness.

## Current build and packaging commands

The canonical v8.5 README exposes the shared-runtime and portable/release build path:

```text
python3 shared-runtime-source/build_runtime.py
python3 scripts/build_portable.py
python3 scripts/package_release.py
```

The repository also exposes the WXT extension checks used by the Surround verification path:

```text
npm install --no-audit --no-fund
npm run typecheck
npm run build
npm run build:firefox
python3 tests/test_surround_contract.py
python3 tests/verify_surround_browser.py
```

The v8.5 release line is described as producing unified Chromium and Firefox packages plus standalone Tumblr, Patreon, X and TikTok userscripts.

Current main's Surround merge was verified through Chromium/Firefox builds and the built Tumblr userscript browser test. A new tagged release artifact containing the post-release Surround delta has not been separately established by the evidence inspected here, so do not equate the source merge with a newer tagged binary release.

## Historical lineage retained as regression evidence

Earlier Project Constellation records remain useful:

- v7.5.0: startup/reload A/B tests, mutation-hotpath tests, off-screen interaction checks, no-cap scaling and MV3/media-network checks;
- v8.1.0: stronger route/feed identity, Patreon semantic identity and X outer-post identity/source restoration;
- v8.2 staging: historical bootstrap transfer phase, now superseded by later completed release lines;
- v8.3: Interaction Capsules;
- v8.4: persistent per-post context;
- v8.5.0 release: TikTok adapter, bounded playback recovery, site boot gates and deterministic release packaging;
- current post-release v8.5.0 main: verified default-off Surround mode with native center feed plus adaptive retained side lanes.

Preserve these as regression history rather than deleting older evidence when the current version advances.

## Exact live verification matrix

For each supported site:

1. feed detection works;
2. route/feed identity is correct;
3. card identity remains stable under recycling/navigation;
4. duplicate/quoted/referenced content cannot steal outer identity;
5. native actions remain usable from retained cards;
6. retained cards survive expected navigation/reload behavior;
7. top/bottom scrolling does not discard content;
8. retained quantity remains complete;
9. source restoration does not move the visible deck;
10. layout drift fails visibly instead of silently corrupting history.

Additional v8.5/TikTok gates:

11. each site toggle truly prevents runtime boot when disabled;
12. toggling one site reloads only affected tabs and preserves unrelated settings;
13. direct TikTok videos remain playable when the source is safely reusable;
14. blob/MSE-only media does not create a duplicate-decoder regression;
15. native TikTok Retry is preferred when available;
16. fallback recovery is bounded and per-video rate limited;
17. a permanently bad video does not create retry storms;
18. healthy TikTok videos are not mass-reloaded because another player stalls;
19. Chromium, Firefox and all standalone userscript packages contain the expected current adapters;
20. no test uses viewport culling, card caps or reduced fidelity to obtain a passing performance result.

Additional Surround gates:

21. Surround is off by default on a clean profile for every supported site;
22. each site's Surround preference persists independently;
23. enabling Surround leaves the native center feed visible and interactive;
24. the two UltraDeck side lanes remain independently interactive;
25. retained-card count and identity remain unchanged when toggling Surround;
26. full-deck column/layout settings survive a Surround on/off cycle;
27. disabling Surround restores the normal full-deck source-visibility behavior;
28. changing Surround on one site does not enable it on unrelated sites;
29. a disabled site's main boot gate still wins over any stored Surround preference;
30. narrow-window fallback does not corrupt persisted layout state;
31. Tumblr, Patreon, X/Twitter and TikTok each receive authenticated production-site Surround verification before claiming cross-site completion.

## Performance verification

Compare before/after on the same captured or live workload and record:

- card count;
- identity collisions;
- mutation processing cost;
- startup/reload cost;
- scrolling behavior;
- native-action restoration;
- media recovery attempts/success/failure;
- memory growth;
- responsiveness;
- errors and recovery;
- Surround center/side geometry and resize behavior;
- full-deck versus Surround interaction latency without reducing retained content.

A faster synthetic number is not an improvement if feed completeness, native controls, site-state persistence, Surround reversibility or video fidelity regresses.

## Troubleshooting

### Two logical feeds merge history

Check route identity and selected top-level feed/tab state. Same URL does not always mean same logical feed.

### X card gets the quoted post ID

Inspect the outer timestamp/permalink identity. Referenced or quoted status links must not override the outer post identity.

### Patreon cards stop resolving after layout changes

Check semantic article detection and permalink fallback before adding brittle one-off selectors.

### TikTok retained player stalls

Determine whether the source is a direct reusable media URL or blob/MSE-only. Prefer the source site's native Retry/Try Again control, then use only the bounded per-video fallback path. Do not reload the whole feed.

### Off-screen cards lose native actions

Use the source-restoration path without moving/hiding the visible UltraDeck deck. Verify the exact native action after restoration.

### Site is disabled but UltraDeck still partially runs

Treat that as a boot-gate regression. Verify document-start site settings before runtime/deck/media initialization rather than hiding UI after boot.

### Surround toggle is missing or disabled

Verify the active tab is one of the supported/enabled sites. The popup disables the Surround control when there is no supported active site or the site's UltraDeck boot gate is disabled.

### Surround does not match the current site's saved state

Inspect `chrome.storage.local["ultradeckSurroundSites"]` and the bridge restore path. The general UltraDeck settings store intentionally excludes the per-site `surroundMode` value in extension builds so one site's choice does not overwrite another's.

### Native center feed is visible after Surround is turned off

Treat that as a presentation-state regression. The verified browser test expects the native retained source to return to hidden full-deck behavior after the off transition.

### Side lanes overwrite the center feed

Inspect the calculated `--tu-surround-center`, `--tu-surround-side` and `--tu-surround-gap` values plus the two-column grid placement. Do not fix this by culling retained cards or replacing the native feed.

### Performance work suggests virtualizing cards

Reject that approach for UltraDeck's core retained-feed behavior. Optimize processing while preserving every retained card.

## Current next action

**Qualify current UltraDeck main at `e1da516a7aad9a254443e4a3e48830b98a1c772b` end to end in authenticated current Chromium and Firefox sessions across Tumblr, Patreon, X/Twitter and TikTok. Exercise Surround off -> on -> off, per-site persistence, native-center interaction, retained side-lane interaction, resize/narrow-window behavior, full-deck restoration, TikTok playback recovery and per-site boot gates. Compare card counts, identities, native actions, context persistence, media behavior and performance against the preserved v8.5 release and v8.4/v8.1 regression evidence. Do not promote any performance or layout change that reduces retained content or off-screen capability.**

## Wiki maintenance

Update this page when adapters, identity rules, Interaction Capsule/context behavior, playback recovery, site boot gates, Surround behavior, no-culling guarantees, release artifacts, build commands or the verified latest version/source head changes. Preserve older verification evidence as regression history.