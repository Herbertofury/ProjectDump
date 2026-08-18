# ChatGPT Ultimate Optimizer Wiki

**Project Constellation ID:** `PCX-041`  
**Status:** ACTIVE / TRACKED  
**Latest verified release:** `v1.0.1`  
**Canonical release commit:** `78a92c68a07b49e152723457fcfb80fb03baf564`  
**Surface research checked:** `2026-08-18`

## Purpose

ChatGPT Ultimate Optimizer is a browser-side optimization/customization project for ChatGPT with both Manifest V3 extension and userscript delivery. Its continuity contract is to preserve working ChatGPT-specific behavior while adapting to current product surfaces instead of hard-coding assumptions from an older UI.

## Current verified release evidence

The durable Drive release manifest records `v1.0.1` as the canonical release line with these exact artifacts:

- `ChatGPT-Ultimate-Optimizer-v1.0.1.zip` — 252,802 bytes — SHA-256 `3fe54e8491c12ccab75001bf826eaffe5bd834034db1f2f82b147adaa7c2a1d8`
- `ChatGPT-Ultimate-Optimizer-Extension-v1.0.1.zip` — SHA-256 `cf24717a9e060a7a6fe937116187eaa00b26c6fddb55f1113b42a7de3fc6bb1a`
- `ChatGPT-Ultimate-Optimizer-Userscript-v1.0.1.user.js` — SHA-256 `866b613ccdac8c7c575635764ec7ef9d61967f0cd23108d2703e02d33c53776b`
- `ChatGPT-Ultimate-Optimizer-v1.0.1.git.bundle` — SHA-256 `76e749793b6471f90972e68adb461efe0907d6dc24de9216780843c44078be48`

The same manifest records 7/7 unit and performance-model tests passing, 23 JavaScript files passing syntax/safety/UI-control validation, fresh-extraction rebuild success, AGENTS repository doctor success, and canonical project-memory doctor success.

The connected Drive release tree was rechecked on 2026-08-18. `v1.0.1` remains the newest release folder and no newer project-owned release line was found.

## Runtime-verification boundary

The recorded disposable managed-Chromium smoke was blocked by `ERR_BLOCKED_BY_CLIENT` before the extension executed. That is an environment blocker, not runtime proof. Do not promote a newer ChatGPT UI adapter merely because static selectors compile.

## Current ChatGPT surface changes that matter

OpenAI's current ChatGPT release notes materially expand the compatibility matrix beyond the older Chat-only navigation model.

### Current official surface baseline

- ChatGPT Work is a first-class long-running task surface on supported plans.
- The desktop app has a clearer Chat / Work / Codex information architecture on macOS and Windows, with Projects available in the desktop app and cloud Work conversations continuing across devices.
- Chat and Work conversations share unified Recents.
- Search spans chats, Projects, images, and documents and supports opening the matched result directly.
- Custom instructions now support up to 5,000 characters on supported paid plans.
- File Library is a persistent reusable surface for uploaded/generated files, with recent files available from the composer and broader file search.
- Google file connectors are unified under the Google Drive app, covering Drive, Docs, Sheets, and Slides actions.
- Long pastes are converted into attachments on supported paid plans when the paste exceeds the current 5,000-character threshold rather than remaining ordinary composer text.
- Voice is available in Work and Codex in the desktop app for supported workspace/plan combinations.
- Atlas was retired as browser capabilities moved into ChatGPT/Codex product surfaces.

Primary OpenAI release-note source: https://help.openai.com/en/articles/6825453-chatgpt-release-notes

These changes mean UI targeting should be capability/role based and should not assume the older Chat-only navigation hierarchy. The optimizer must distinguish Chat, Work, Projects, Library/files, Google Drive-backed file actions, composer attachment state, Voice, desktop-native navigation, and global search.

## Anti-regression rules

- Preserve both MV3 extension and userscript delivery unless intentionally retired by verified project evidence.
- Do not replace resilient semantic targeting with brittle class-name snapshots.
- Do not hide, clamp, remove, or disable native ChatGPT messages or controls to make optimizer UI simpler or faster.
- Do not add viewport-only rendering, optimizer-owned conversation culling, reduced history datasets, or hidden message caps as a performance shortcut.
- Do not interfere with native ChatGPT virtualization, Projects, Work, Library/Drive flows, native paste-to-attachment conversion, Voice, or desktop navigation.
- Do not treat a successful build as proof that Chat, Work, Projects, Library, search, file surfaces, desktop flows, or userscript parity still behave correctly.
- Keep success/failure states truthful when a target surface is unavailable or has changed.

## Current research direction

The strongest immediate improvement is a **surface capability and data-source matrix** rather than more selector patches. Track at least:

`surface -> capability -> authoritative data source -> selector/anchor strategy -> fallback -> verified date -> real smoke evidence`

Initial surfaces should include:

- Chat conversation and composer;
- Work;
- Projects;
- Library and Google Drive-backed file views;
- unified search across chats/projects/files;
- conversation history/Recents;
- settings and custom instructions;
- long-paste attachment conversion;
- Voice where available;
- desktop navigation on the platforms the release actually claims to support;
- every optimizer-owned panel, command, shortcut, and setting.

For conversation-derived features such as search, timeline, export, or navigation, prefer complete data-backed discovery when available, then reconcile that data with the native virtualized UI. Do not require every historical message to remain mounted and do not create a second destructive virtualization layer.

## Acceptance test for the next release

A successor release should prove, in a real supported browser profile:

1. exact build identity is loaded;
2. optimizer controls render and operate on Chat without dead actions;
3. navigation between Chat, Work, Projects, Library, and search does not duplicate or orphan optimizer state;
4. Library/Drive file selection and native file actions remain functional where available;
5. long-paste conversion still follows the native attachment path rather than being intercepted by optimizer code;
6. conversation search/timeline/export logic retains complete data coverage without optimizer-owned message hiding or caps;
7. reload and browser restart preserve intended settings;
8. both extension and userscript builds either pass the same functional matrix or explicitly document intentional differences;
9. console/service-worker errors are inspected and material failures remain visible;
10. desktop-specific behavior is tested only on the desktop platforms the release actually claims to support.

## Exact next action

Resolve the canonical source repository/worktree or reconstruct it from the verified git bundle. Before changing selectors, add a read-only current-surface drift probe that records detected surface, semantic anchors, available conversation/file data sources, and optimizer control attachment points without mutating ChatGPT. Run it against Chat, Work, Projects, Library/Drive, unified search, and long-paste attachment conversion. Use the results to make the smallest compatibility change, then exercise both MV3 and userscript builds in a real supported browser with reload/restart evidence.

## Wiki maintenance

Update this page when a newer verified release/tag appears, the canonical repository is re-resolved, OpenAI materially changes ChatGPT navigation/host surfaces, or real browser/runtime evidence supersedes the current blocked smoke result.