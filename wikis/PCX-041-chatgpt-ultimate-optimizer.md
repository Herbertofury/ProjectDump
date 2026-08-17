# ChatGPT Ultimate Optimizer Wiki

**Project Constellation ID:** `PCX-041`  
**Status:** ACTIVE / TRACKED  
**Latest verified release:** `v1.0.1`  
**Canonical release commit:** `78a92c68a07b49e152723457fcfb80fb03baf564`

## Purpose

ChatGPT Ultimate Optimizer is a browser-side optimization/customization project for ChatGPT with both Manifest V3 extension and userscript delivery. Its continuity contract is to preserve working ChatGPT-specific behavior while adapting to current product surfaces instead of hard-coding assumptions from an older UI.

## Current verified release evidence

The durable Drive release manifest records `v1.0.1` as the canonical release line with these exact artifacts:

- `ChatGPT-Ultimate-Optimizer-v1.0.1.zip` — 252,802 bytes — SHA-256 `3fe54e8491c12ccab75001bf826eaffe5bd834034db1f2f82b147adaa7c2a1d8`
- `ChatGPT-Ultimate-Optimizer-Extension-v1.0.1.zip` — SHA-256 `cf24717a9e060a7a6fe937116187eaa00b26c6fddb55f1113b42a7de3fc6bb1a`
- `ChatGPT-Ultimate-Optimizer-Userscript-v1.0.1.user.js` — SHA-256 `866b613ccdac8c7c575635764ec7ef9d61967f0cd23108d2703e02d33c53776b`
- `ChatGPT-Ultimate-Optimizer-v1.0.1.git.bundle` — SHA-256 `76e749793b6471f90972e68adb461efe0907d6dc24de9216780843c44078be48`

The same manifest records 7/7 unit and performance-model tests passing, 23 JavaScript files passing syntax/safety/UI-control validation, fresh-extraction rebuild success, AGENTS repository doctor success, and canonical project-memory doctor success.

## Runtime-verification boundary

The recorded disposable managed-Chromium smoke was blocked by `ERR_BLOCKED_BY_CLIENT` before the extension executed. That is an environment blocker, not runtime proof. Do not promote a newer ChatGPT UI adapter merely because static selectors compile.

## Current ChatGPT surface changes that matter

OpenAI's current ChatGPT release notes record major product-surface changes relevant to this project:

- ChatGPT Work is now a first-class long-running task surface.
- The desktop app unifies Chat, Work, and Codex while keeping distinct modes/workflows.
- Projects are available in the desktop app and Work can use project context.
- Recents are unified across Chat and Work.
- Search spans chats, projects, images, and documents.
- Custom instructions now support a larger saved character budget on supported plans.
- Atlas has been retired in favor of browser capabilities integrated into ChatGPT/Codex.

These changes mean UI targeting should be capability/role based where possible and should not assume the older Chat-only navigation hierarchy.

## Anti-regression rules

- Preserve both MV3 extension and userscript delivery unless intentionally retired by verified project evidence.
- Do not replace resilient semantic targeting with brittle class-name snapshots.
- Do not hide or disable native ChatGPT controls to make optimizer UI simpler.
- Do not treat a successful build as proof that Chat, Work, Projects, search, file surfaces, or desktop flows still behave correctly.
- Keep success/failure states truthful when a target surface is unavailable or has changed.

## Current research direction

The strongest immediate improvement is a **surface capability matrix** rather than more selector patches. Track at least:

`surface -> capability -> selector/anchor strategy -> fallback -> verified date -> real smoke evidence`

Initial surfaces should include Chat, Work, Projects, unified search, file/document results, conversation history/Recents, settings, and any optimizer-owned panel/commands.

## Acceptance test for the next release

A successor release should prove, in a real supported browser profile:

1. exact build identity is loaded;
2. optimizer controls render and operate on Chat without dead actions;
3. navigation between Chat/Work/Projects does not duplicate or orphan optimizer state;
4. search/Recents changes do not break target discovery;
5. reload and browser restart preserve intended settings;
6. both extension and userscript builds either pass the same functional matrix or explicitly document intentional differences;
7. console/service-worker errors are inspected and material failures remain visible.

## Exact next action

Resolve the canonical source repository/worktree or reconstruct it from the verified git bundle, then run a current UI-drift audit against Chat, Work, Projects, unified search, and desktop/browser navigation before changing selectors.

## Wiki maintenance

Update this page when a newer verified release/tag appears, the canonical repository is re-resolved, OpenAI materially changes ChatGPT navigation or host surfaces, or real browser/runtime evidence supersedes the current blocked smoke result.