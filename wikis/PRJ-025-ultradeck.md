# UltraDeck Wiki

**Project Constellation ID:** `PRJ-025`
**Status:** ACTIVE
**Canonical connected repository:** [Herbertofury/UltraDeck](https://github.com/Herbertofury/UltraDeck)

## Purpose

UltraDeck is a lossless ultrawide multi-column feed engine for Tumblr, Patreon, X/Twitter and TikTok. Its core contract is to increase information density and preserve feed history without hiding, culling, virtualizing or degrading off-screen content.

## Current verified source line

The canonical repository now identifies **UltraDeck v8.6.0** in `package.json`. Current `main` head `d9278d4a0fd33d184e9c6f928556262668af4125`, dated 2026-08-18, merges the verified **site-regression and challenge-safe loading repair** from pull request #2.

The exact verified pull-request head is `0e7b68f9e0cf3c3a908b366c4088384c5a0edd24`. GitHub Actions verify run `32159116689` completed successfully on that exact head before merge. The job built Chromium and Firefox, generated the portable runtime, ran typechecking, Python/JavaScript syntax checks, the site-regression contract, Surround regression, real browser Surround verification, headed cross-site visual verification, extension-options verification, package assertions and artifact upload.

The CI artifact is `UltraDeck-v8.6.0-regression-fixed`, 616,444 bytes, with GitHub artifact digest:

`sha256:7bb11d10d12cb23b01e6456c931d205a4f1121eb4f3a2a5a09d6b354e60709b7`

The repository `README.md` and `CHANGELOG.md` still begin at v8.5.0, so they currently lag the package/source identity. For v8.6 implementation facts, prefer current source, the verified pull request, tests and exact-head CI over those stale top-level prose files. Preserve the v8.5 release notes as lineage rather than rewriting history.

This supersedes the older Project Constellation state that treated v8.5 plus Surround as the newest line. The current source is **v8.6.0 with Surround preserved and a new cross-site startup/geometry regression repair**.

## v8.6 site-regression and challenge-safe loading repair

Version 8.6.0 changes how the extension reaches each site's page-owned runtime and adds explicit cross-site regression evidence without weakening full retention, native actions or Surround mode.

### Isolated extension bootstrap with explicit MAIN-world injection

Tumblr, Patreon, X/Twitter and TikTok no longer start their page runtime directly from a WXT `world: 'MAIN'` content script. Each site now uses an **ISOLATED** content-script bootstrap that calls the shared `src/extension/site-runtime-loader.ts`, and each page-owned runtime has a separate unlisted main-world entrypoint.

The loader:

- reads the existing per-site `ultradeckSites` enable state before startup;
- watches for site-specific application evidence with a `MutationObserver`;
- injects the corresponding main-world runtime only after the page is considered safe;
- keeps startup bounded by a 15-second wait;
- allows a conservative post-load fallback on Tumblr, Patreon and TikTok when normal app evidence is delayed;
- deliberately does **not** use that generic fallback for X when application identity remains unproven;
- uses WXT `injectScript()` rather than assuming an early MAIN-world content script can safely execute on every intermediate document.

Current site evidence and fallback values are source-defined in `SITE_RUNTIME`:

| Site | Main-world entrypoint | Application evidence | Fallback delay |
| --- | --- | --- | ---: |
| Tumblr | `/tumblr-main-world.js` | timeline markers or `main` | 1800 ms |
| Patreon | `/patreon-main-world.js` | `main`, `role=main`, or post permalink | 1800 ms |
| X/Twitter | `/x-main-world.js` | `#react-root`, primary column, or main role | 2600 ms, but no generic final fallback |
| TikTok | `/tiktok-main-world.js` | `#app`, recommend list, or `main` | 2200 ms |

This architecture keeps the extension's low-level boot gate available early while delaying page-owned runtime mutation until the real site application is present.

### X / Cloudflare challenge-page safety

The shared loader now detects challenge/interstitial evidence including:

- challenge-oriented page titles such as `Just a moment`, `Checking your browser`, `Verify you are human`, `Security verification` or `Attention required`;
- `/cdn-cgi/` routes;
- Cloudflare challenge elements and challenge-platform scripts.

On those pages UltraDeck stays inactive. The X bridge independently checks the same challenge state, waits for actual X application evidence and refuses settings commands/runtime messages while the verification page is active.

The headed browser regression contains a dedicated X challenge fixture and requires:

- no `window.__UltraDeck` runtime;
- no UltraDeck deck shell;
- no `data-tu-site-enabled` gate marker;
- no UltraDeck site marker.

This is a startup-safety boundary, not a generic anti-bot bypass. The correct behavior on an X verification page is to avoid booting or mutating the page until the real application loads.

### Cross-site deck-top hardening

`shared-runtime-source/site-hardening.js` now wraps `resolveDeckTop()` with a site-configured maximum. This prevents route controls, oversized SPA placeholders or utility wrappers from creating a large blank band between site chrome and the first retained UltraDeck row.

Current verified caps are:

```text
Tumblr: 154 px
Patreon: 156 px
X/Twitter: 132 px
```

The hardening is deliberately conservative. It caps an already discovered top anchor when it exceeds the configured site maximum; it does not replace the normal discovery path or hardcode one universal offset.

### Patreon semantic post recovery

The Patreon adapter is now version 3. It prefers semantic article shells and post permalinks, with bounded fallback-shell and ancestor scoring. It no longer depends on an over-broad wildcard test-id selector or blindly returns a permalink's parent element.

The current candidate resolver:

- accepts explicit `data-post-id` / `data-post_id` identities;
- extracts canonical numeric IDs from `/posts/...<id>` permalinks;
- prefers `article` / `role=article` shells;
- falls back to specific post-card markers;
- walks at most ten ancestors when semantic shells are absent;
- rejects main/root containers;
- requires useful geometry plus controls/media/heading evidence before promoting a generic ancestor;
- deduplicates candidates by canonical post ID.

This addresses Patreon feed-capture drift without replacing stable permalink identity with brittle visual position.

### v8.6 source and verification files

| Path | Verified responsibility |
| --- | --- |
| `src/extension/site-runtime-loader.ts` | Per-site enable gate, challenge detection, application-evidence wait and safe MAIN-world injection. |
| `entrypoints/*-main.content.ts` | ISOLATED site bootstrap for Tumblr, Patreon, X and TikTok. |
| `entrypoints/*-main-world.ts` | Unlisted site-specific page-world startup entrypoints. |
| `entrypoints/bridge.content.ts` | Settings/runtime bridge plus X application/challenge safety checks. |
| `shared-runtime-source/site-hardening.js` | Site-specific deck-top cap applied after normal top discovery. |
| `shared-runtime-source/adapters/patreon.js` | Patreon v3 semantic/permalink-first candidate and identity recovery. |
| `shared-runtime-source/adapters/tumblr.js` | Tumblr boot evidence and 154 px maximum deck top. |
| `shared-runtime-source/adapters/x.js` | X boot evidence and 132 px maximum deck top. |
| `tests/test_site_regression_contract.py` | Static 8.6 contract for isolated loading, challenge safety, site caps, Patreon v3 and portable-build invariants. |
| `tests/verify_site_visuals.py` | Real browser cross-site visual/layout regression for Tumblr, Patreon, X, TikTok plus X challenge inactivity. |
| `.github/workflows/verify.yml` | Exact-head CI build, browser setup, regression tests, package assertions and v8.6 artifact upload. |

### v8.6 exact-head CI evidence

Verify run `32159116689` passed all of these steps on pull-request head `0e7b68f9e0cf3c3a908b366c4088384c5a0edd24`:

- Node dependency install;
- Python Playwright install;
- Playwright Chromium install;
- shared-runtime generation;
- TypeScript typecheck;
- WXT Chromium production build;
- WXT Firefox production build;
- portable build;
- Python compile checks for build/package and browser-regression scripts;
- JavaScript syntax checks for runtime, hardening, Surround, generated site loader and bridge;
- `tests/test_site_regression_contract.py`;
- `tests/test_surround_contract.py`;
- `tests/verify_surround_browser.py`;
- headed `tests/verify_site_visuals.py` with expected version 8.6.0;
- headed site-options persistence/boot-gate verification;
- manifest/package assertions for both Chromium and Firefox;
- upload of Chromium/Firefox 8.6 packages plus visual-verification screenshots/report.

The merge commit explicitly records that the stale verified v8.6 repair was recovered only after exact-head CI completed successfully.

## Verified Surround mode retained in v8.6

Current main retains the optional **Surround mode** that preserves the familiar native center feed while UltraDeck keeps retained cards in adaptive side lanes around it.

The feature remains deliberately **off by default**. Full-deck UltraDeck remains the default behavior.

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

### Important Surround source files

| Path | Verified responsibility |
| --- | --- |
| `shared-runtime-source/surround-mode.js` | Surround state, adaptive center/side geometry, visibility and pointer-event presentation, two-lane layout wrapper, runtime HUD control and diagnostics. |
| `shared-runtime-source/build_runtime.py` | Includes `site-hardening.js` and `surround-mode.js` in generated runtimes. |
| `entrypoints/bridge.content.ts` | Restores and persists per-site Surround state through `ultradeckSurroundSites`. |
| `entrypoints/popup/index.html` / `entrypoints/popup/main.ts` | Current-site Surround toggle in the extension popup. |
| `public/options.html` / `public/options.js` | Per-site Surround settings for Tumblr, Patreon, X/Twitter and TikTok. |
| `tests/test_surround_contract.py` | Static source/build contract for default-off persistence, target wiring, two-column behavior, native-source visibility and the no-`content-visibility` requirement. |
| `tests/verify_surround_browser.py` | Real Chromium toggle test using the built Tumblr userscript. |

### Preserved Surround verification evidence

The original Surround recovery checkpoint records these passes before its merge:

- npm dependency install;
- TypeScript typecheck;
- WXT Chromium MV3 production build;
- WXT Firefox MV3 production build;
- shared runtime generation;
- portable Chromium and Firefox builds;
- Python compile checks;
- JavaScript syntax checks for source and generated runtimes;
- Surround contract test;
- real Chromium runtime toggle test.

The verified recovery branch head `d08cd7d9e80d2e96e0f2db973e9865b47c59733d` completed GitHub Actions verify run `32087223402` successfully before merge. The v8.6 exact-head CI reruns the Surround contract and browser toggle gate so the site-regression repair cannot silently break that feature.

The real browser test loads the actual built Tumblr userscript against an eight-post synthetic feed and exercises **Surround off -> on -> off**. The recorded result proves:

- native retained-source nodes are hidden in the normal full-deck state;
- enabling Surround makes the native source visible and interactive with `pointer-events:auto`;
- diagnostics report Surround active;
- all eight posts remain retained;
- exactly two side columns are requested;
- center and side widths are measured from real browser layout state;
- turning Surround off restores the original full-deck source-visibility state.

This is real built-runtime browser proof. It is not authenticated end-to-end production-site proof across Tumblr, Patreon, X and TikTok, which remains part of live qualification.

## v8.5 first-class TikTok adapter preserved

TikTok remains a first-class adapter rather than a generic fallback.

The v8.5 release line records:

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

In v8.6, the boot gate runs from the isolated bootstrap before page-world injection, so a disabled site avoids starting the site runtime at all.

## Persistent native interaction

Retained cards reconnect actions to the source site's live controls. Current v8.6 preserves the v8.3/v8.4 Interaction Capsule and post-context work, including Like/Reblog/Repost, Reply/Comment, Share, bookmarks, polls, menus and inputs.

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

The v8.6 site-regression contract explicitly checks that `content-visibility` is absent from the retained-runtime, site-hardening and Surround source used by the verification path.

## Supported surfaces

Current v8.6 supports:

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

Preserve canonical `/posts/` permalink IDs and semantic article/fallback-shell discovery so layout changes do not immediately destroy card identity. Version 8.6 strengthens this path with bounded ancestor scoring instead of promoting arbitrary permalink parents.

### TikTok identity

Use canonical video identity from `/@user/video/<id>` where available, with current feed/xgplayer evidence as supporting discovery. Avoid false merges across reposted/referenced media or recycled native containers.

## Native controls and source restoration

Retained/off-screen content may require restoring or reconnecting native controls, but source recovery must not move, collapse or replace the visible UltraDeck deck.

In normal full-deck mode the native retained-source nodes remain hidden as part of source ownership/restoration behavior. In Surround mode the explicitly marked native source is made visible and interactive so the normal center feed can coexist with the retained side lanes.

For every supported platform, qualification must exercise the actual promised actions, not merely confirm that a selector matched.

## Jank reduction without culling

v8.6 preserves the prior Nocturne-style performance line:

- scroll storms are animation-frame coalesced;
- geometry audits are input-aware and time-sliced;
- irrelevant Patreon/X identity mutations are rejected early;
- exact source identities are cached;
- rail/top-chrome discovery is scoped before fallback scanning;
- repeated rail writes are idempotent;
- interaction metadata is captured lazily where practical;
- TikTok playback recovery is targeted and bounded;
- oversized route/control wrappers cannot push the deck arbitrarily far below site chrome when a site maximum is configured.

Surround reuses the same runtime and geometry audit path. Any optimization remains subordinate to full-retention and exact-interaction correctness.

## Current build and packaging commands

The shared-runtime and portable/release path remains:

```text
python3 shared-runtime-source/build_runtime.py
python3 scripts/build_portable.py
python3 scripts/package_release.py
```

The current v8.6 extension verification path includes:

```text
npm install --no-audit --no-fund
python3 -m pip install playwright
python3 -m playwright install chromium
python3 shared-runtime-source/build_runtime.py
npm run typecheck
npm run build
npm run build:firefox
python3 scripts/build_portable.py
python3 tests/test_site_regression_contract.py
python3 tests/test_surround_contract.py
python3 tests/verify_surround_browser.py
ULTRADECK_EXPECT_VERSION=8.6.0 python3 tests/verify_site_visuals.py
ULTRADECK_EXPECT_VERSION=8.6.0 python3 tests/test_v85_site_options.py
```

CI runs the cross-site visual and options flows headed under Xvfb and packages both Chromium and Firefox v8.6.0 extension directories into upload artifacts.

A normal GitHub release tag containing these exact v8.6 bytes was not independently established by the evidence inspected for this wiki update. Treat the exact-head CI artifact and current source as verified v8.6 evidence without silently claiming a tagged release that has not been separately verified.

## Historical lineage retained as regression evidence

Earlier Project Constellation records remain useful:

- v7.5.0: startup/reload A/B tests, mutation-hotpath tests, off-screen interaction checks, no-cap scaling and MV3/media-network checks;
- v8.1.0: stronger route/feed identity, Patreon semantic identity and X outer-post identity/source restoration;
- v8.2 staging: historical bootstrap transfer phase, now superseded by later completed release lines;
- v8.3: Interaction Capsules;
- v8.4: persistent per-post context;
- v8.5.0 release: TikTok adapter, bounded playback recovery, site boot gates and deterministic release packaging;
- post-release v8.5 main: verified default-off Surround mode with native center feed plus adaptive retained side lanes;
- v8.6.0 current main: isolated per-site bootstrap with typed page-world injection, X challenge-page inactivity, cross-site deck-top hardening, Patreon v3 capture repair, TypeScript 7.0.2 and headed cross-site visual regression evidence.

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

Additional v8.5/TikTok gates retained by v8.6:

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

Additional v8.6 site-regression gates:

32. built Chromium and Firefox manifests report version 8.6.0 and preserve all required host permissions;
33. each site uses the isolated bootstrap plus a separate unlisted page-world runtime;
34. disabled-site settings prevent main-world runtime injection;
35. Tumblr oversized route/filter wrappers cannot push the verified deck top beyond the 154 px cap fixture;
36. Patreon permalink-first capture returns the intended semantic post card and preserves numeric post identity;
37. X/Twitter real application pages boot only after application evidence;
38. X/Cloudflare challenge fixtures remain completely free of UltraDeck runtime, shell and gate markers;
39. X/Twitter deck top stays within the 132 px fixture cap;
40. Patreon deck top stays within the 156 px fixture cap;
41. cross-site browser screenshots are generated from the exact built Chromium extension and contain no task-related console errors;
42. site-options persistence/boot-gating still passes after the loader architecture change;
43. Surround contract and real browser toggle pass on the same 8.6 exact head;
44. Chromium and Firefox v8.6 package artifacts are generated from the verified head rather than a stale working tree.

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
- full-deck versus Surround interaction latency without reducing retained content;
- time from document start to safe site-runtime injection;
- false startup on challenge/interstitial pages;
- top-anchor/deck-top stability across route controls and SPA placeholders;
- Patreon candidate/identity correctness under wrapper changes.

A faster synthetic number is not an improvement if feed completeness, native controls, site-state persistence, Surround reversibility, challenge-page safety or video fidelity regresses.

## Troubleshooting

### Two logical feeds merge history

Check route identity and selected top-level feed/tab state. Same URL does not always mean same logical feed.

### X card gets the quoted post ID

Inspect the outer timestamp/permalink identity. Referenced or quoted status links must not override the outer post identity.

### X verification page shows UltraDeck UI or changes

Treat this as a v8.6 startup-safety regression. Check `isChallengePage()` evidence, the isolated site loader and the bridge's `waitForXApplication()` / challenge guards. UltraDeck should not inject or expose its normal gate/runtime on the verification page.

### X normal timeline never starts UltraDeck

Verify the page contains real X application evidence such as `#react-root`, `[data-testid="primaryColumn"]` or `main[role="main"]`. Check that challenge selectors/titles are not falsely matching the real application. Do not weaken the challenge guard by blindly injecting at document start.

### Tumblr has a large blank gap above the first deck row

Inspect the discovered top anchor, `state.topAnchorSource` and the Tumblr `maxDeckTop: 154` hardening path. Do not repair the gap by hiding cards or moving the entire retained history into a viewport-only renderer.

### Patreon cards stop resolving after layout changes

Check canonical `/posts/` permalink identity, semantic article shells and the bounded v3 ancestor-scoring fallback before adding brittle one-off selectors. Do not restore the old broad wildcard test-id candidate path as a shortcut.

### TikTok retained player stalls

Determine whether the source is a direct reusable media URL or blob/MSE-only. Prefer the source site's native Retry/Try Again control, then use only the bounded per-video fallback path. Do not reload the whole feed.

### Off-screen cards lose native actions

Use the source-restoration path without moving/hiding the visible UltraDeck deck. Verify the exact native action after restoration.

### Site is disabled but UltraDeck still partially runs

Treat that as a boot-gate regression. In v8.6 the isolated site loader should read `ultradeckSites` and return before main-world injection. Verify that path rather than hiding UI after the site runtime has already started.

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

**Qualify UltraDeck v8.6.0 current main at `d9278d4a0fd33d184e9c6f928556262668af4125` end to end in authenticated current Chromium and Firefox sessions across Tumblr, Patreon, X/Twitter and TikTok. Reproduce the exact v8.6 regression targets on current production pages: Tumblr top-gap behavior, Patreon post capture/identity, X normal-app delayed bootstrap and challenge-page inactivity, TikTok boot/media behavior, per-site enable gates, Surround off -> on -> off, native-center interaction, retained side-lane interaction and no-culling/full-retention guarantees. Compare against the verified CI artifact and preserved v8.5/v8.4/v8.1 evidence, and do not promote any change that reduces retained content, off-screen capability, native actions or verification safety.**

## Wiki maintenance

Update this page when adapters, identity rules, site-loader/challenge behavior, top-anchor hardening, Interaction Capsule/context behavior, playback recovery, site boot gates, Surround behavior, no-culling guarantees, release artifacts, build commands or the verified latest version/source head changes. Preserve older verification evidence as regression history.