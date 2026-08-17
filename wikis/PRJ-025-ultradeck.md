# UltraDeck Wiki

**Project Constellation ID:** `PRJ-025`  
**Status:** ACTIVE  
**Canonical connected repository:** [Herbertofury/UltraDeck](https://github.com/Herbertofury/UltraDeck)

## Purpose

UltraDeck is a lossless ultrawide multi-column feed engine for Tumblr, Patreon, X/Twitter and TikTok. Its core contract is to increase information density and preserve feed history without hiding, culling, virtualizing or degrading off-screen content.

## Current verified source line

The canonical repository now identifies **UltraDeck v8.5.0** as the current source line. Commit `2b697933ff46513282cc8f0ef38df6e70dc79aab`, dated 2026-08-17, is the release commit and updates the repository changelog/README to 8.5.0.

This supersedes the older Project Constellation documentation that stopped at v8.1.0 and treated v8.2 as an incomplete bootstrap. The later repository history now records complete v8.4 and v8.5 release work, followed by cleanup of the one-shot v8.5 publisher. Do not keep presenting the old partial-bootstrap state as current.

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

The extension now exposes an **Enabled sites** options page plus matching popup toggles for:

- Tumblr;
- Patreon;
- X / Twitter;
- TikTok.

All are enabled by default. Disabling a site is a true runtime boot gate: UltraDeck does not start its deck, media accelerators or site-specific playback hooks on that site. Changing a site setting reloads only affected open tabs.

This is a functional contract, not a cosmetic toggle. Qualification must prove that a disabled site does not partially boot UltraDeck and that re-enabling restores the full adapter without resetting unrelated site preferences.

## Persistent native interaction

Retained cards reconnect actions to the source site's live controls. Current v8.5 documentation preserves the v8.3/v8.4 Interaction Capsule and post-context work, including Like/Reblog/Repost, Reply/Comment, Share, bookmarks, polls, menus and inputs.

Active draft text, expanded/thread state, menus, poll selections and other per-post context can survive source-card recycling and same-tab reload behavior. Raw saved HTML is not sufficient authority because framework handlers must be reconnected to current source controls.

## Hard no-culling contract

UltraDeck must not solve performance problems by reducing feed content. Current source explicitly preserves:

- no viewport virtualization as a correctness shortcut;
- no card culling;
- no hidden retained posts;
- no `content-visibility` shortcut that makes retained content unavailable;
- no quantity cap;
- no reduced media quality;
- no disabled off-screen controls.

Every retained card stays mounted and actionable. Performance work must improve scheduling, identity, event handling, DOM interaction, caching and targeted media recovery while preserving complete retained content.

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

Any optimization remains subordinate to full-retention and exact-interaction correctness.

## Current build and packaging commands

The canonical v8.5 README now exposes concrete build commands:

```text
python3 shared-runtime-source/build_runtime.py
python3 scripts/build_portable.py
python3 scripts/package_release.py
```

The v8.5 release line is described as producing unified Chromium and Firefox packages plus standalone Tumblr, Patreon, X and TikTok userscripts.

Do not treat these commands as fresh proof that a local build has passed in Project Constellation. They are current project-owned build instructions; release qualification still needs executed evidence.

## Historical lineage retained as regression evidence

Earlier Project Constellation records remain useful:

- v7.5.0: startup/reload A/B tests, mutation-hotpath tests, off-screen interaction checks, no-cap scaling and MV3/media-network checks;
- v8.1.0: stronger route/feed identity, Patreon semantic identity and X outer-post identity/source restoration;
- v8.2 staging: historical bootstrap transfer phase, now superseded by later completed release lines;
- v8.3: Interaction Capsules;
- v8.4: persistent per-post context;
- **v8.5.0: TikTok adapter, bounded playback recovery, site boot gates and deterministic release packaging.**

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

Additional v8.5 gates:

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
- errors and recovery.

A faster synthetic number is not an improvement if feed completeness, native controls, site-state persistence or video fidelity regresses.

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

### Performance work suggests virtualizing cards

Reject that approach for UltraDeck's core retained-feed behavior. Optimize processing while preserving every retained card.

## Current next action

**Qualify canonical UltraDeck v8.5.0 end to end in real current Chromium and Firefox sessions across Tumblr, Patreon, X/Twitter and TikTok. Exercise the new TikTok playback-recovery matrix and per-site boot gates, then compare card counts, identities, native actions, context persistence, media behavior and performance against the preserved v8.4/v8.1 regression evidence. Do not promote any performance change that reduces retained content or off-screen capability.**

## Wiki maintenance

Update this page when adapters, identity rules, Interaction Capsule/context behavior, playback recovery, site boot gates, no-culling guarantees, release artifacts, build commands or the verified latest version changes. Preserve older verification evidence as regression history.
