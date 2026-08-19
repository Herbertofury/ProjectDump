# ChatGPT Ultimate Optimizer Wiki

**Project Constellation ID:** `PCX-041`
**Status:** ACTIVE / TRACKED
**Latest verified release:** `v1.0.1`
**Canonical release commit:** `78a92c68a07b49e152723457fcfb80fb03baf564`
**Verified release date:** `2026-08-07`
**Surface research checked:** `2026-08-18`
**Canonical source repository/worktree:** unresolved in connected GitHub; exact v1.0.1 release source and Git bundle are preserved as project-owned release artifacts

## Purpose

ChatGPT Ultimate Optimizer, abbreviated CUO in its source, is a browser-side optimization, local-recovery, history-backup, export, and diagnostics project for ChatGPT. It ships in two forms:

- a Manifest V3 browser extension;
- a Tampermonkey/Violentmonkey-compatible userscript.

The project is deliberately broader than a CSS speed tweak. Its verified v1.0.1 source combines long-conversation rendering containment, dirty-turn snapshot scheduling, IndexedDB archival, optional save-before-freeze behavior, server-history mirroring, search, portable exports, diagnostics, and recovery controls.

The continuity contract is preservation-first: improve long-chat responsiveness without silently losing conversation content, rewriting ChatGPT network responses, hiding native functionality, or treating an optimizer-owned cache as the only copy of important chats.

## Source authority and current evidence

The connected Google Drive release manifest records `v1.0.1` as the canonical release line. The exact release source is also preserved in the user's File Library, including the combined userscript, verification report, and closeout receipt.

Current verified artifacts are:

| Artifact | Verified identity |
| --- | --- |
| `ChatGPT-Ultimate-Optimizer-v1.0.1.zip` | 252,802 bytes, SHA-256 `3fe54e8491c12ccab75001bf826eaffe5bd834034db1f2f82b147adaa7c2a1d8` |
| `ChatGPT-Ultimate-Optimizer-Extension-v1.0.1.zip` | SHA-256 `cf24717a9e060a7a6fe937116187eaa00b26c6fddb55f1113b42a7de3fc6bb1a` |
| `ChatGPT-Ultimate-Optimizer-Userscript-v1.0.1.user.js` | SHA-256 `866b613ccdac8c7c575635764ec7ef9d61967f0cd23108d2703e02d33c53776b` |
| `ChatGPT-Ultimate-Optimizer-v1.0.1.git.bundle` | SHA-256 `76e749793b6471f90972e68adb461efe0907d6dc24de9216780843c44078be48` |

The v1.0.1 closeout receipt records:

- `npm run verify` completed successfully;
- 7 of 7 unit/performance-model tests passed;
- 23 JavaScript files passed syntax, safety, and UI-control validation;
- the deterministic master package, extension ZIP, userscript, and Git bundle were verified;
- a clean extraction passed the release verification gates;
- child artifact hashes matched the release record;
- the release closeout recorded no remaining deterministic packaging failures.

The connected Drive release tree was rechecked on 2026-08-18. `v1.0.1` remains the newest project-owned release folder found there.

## Runtime-verification boundary

The recorded disposable managed-Chromium smoke was blocked by `ERR_BLOCKED_BY_CLIENT` before CUO executed. The release therefore has strong deterministic source/package verification but does **not** have a successful recorded current live-ChatGPT browser smoke from that environment.

This distinction matters throughout the page:

- source behavior described below is verified from the v1.0.1 artifact;
- deterministic tests are verified where explicitly stated;
- current ChatGPT integration behavior must still be re-exercised in a browser/profile that can actually load the extension or userscript against the live product.

Do not promote a selector, backend endpoint, performance assumption, or newer UI adapter merely because it builds or because an old fixture accepts it.

## Userscript identity

The verified v1.0.1 userscript declares:

```text
name: ChatGPT Ultimate Optimizer
version: 1.0.1
matches:
  https://chatgpt.com/*
  https://chat.openai.com/*
grant: none
run-at: document-idle
```

The userscript sets `globalThis.__CUO_USERSCRIPT_BUILD__ = true` and the shared runtime identifies its build kind as `userscript`, `extension`, or `web` depending on the host.

That shared code path is important. Extension and userscript builds are intended to exercise the same optimizer core rather than becoming two unrelated implementations.

## High-level architecture

The combined v1.0.1 userscript proves a modular source layout whose generated userscript concatenates project modules. Verified module responsibilities include:

```text
00-namespace.js   -> global CUO identity, runtime state, build-kind detection
10-util.js        -> clamping, scheduling helpers, hashes, sanitization, ZIP writer, downloads
20-settings.js    -> profile/default normalization and localStorage persistence
30-archive.js     -> IndexedDB chat/message archive, snapshot writes, restore/import/search data
40-chat.js        -> ChatGPT turn discovery, chat identity, streaming detection, server normalization
50-export.js      -> Markdown/JSON/backups/Markdown ZIP export
60-server-sync.js -> authenticated same-origin conversation-history mirroring
```

Additional generated UI/runtime modules follow these core modules in the release artifact. The product UI exposes four verified top-level optimizer panes:

```text
Performance
Recovery
Backup
Diagnostics
```

The architecture should remain layered. Changes to ChatGPT selectors belong in chat/surface discovery, persistence changes belong in archive/storage code, export changes belong in export logic, and server mirroring changes belong in the server-sync layer. Do not fold all compatibility fixes into the floating panel or a single mutation observer.

## Settings and profiles

CUO persists normalized settings in:

```text
localStorage key: cuo.settings.v1
```

Verified defaults are:

```text
enabled: true
profile: balanced
autoSnapshot: true
keepLiveTurns: 120
snapshotBatch: 24
restoreBatch: 12
freezeEnabled: false
autoRestoreFrozen: false
mediaOptimization: true
compactHeavyBlocks: false
reduceMotion: true
sidebarOptimization: true
heartbeatEnabled: false
heartbeatMinutes: 5
autoHistoryMirror: true
historyMirrorHours: 24
lastHistoryMirrorAt: 0
serverSyncDelayMs: 250
debug: false
```

The release defines four profiles:

| Profile | Verified behavior |
| --- | --- |
| `off` | optimization disabled, freezing disabled, compact-heavy-block behavior disabled, effectively keeps all live turns |
| `balanced` | optimization enabled, no freezing, 120 live turns target |
| `turbo` | optimization enabled, compact heavy blocks enabled, 80 live turns target |
| `extreme` | optimization enabled, compact heavy blocks and freezing enabled, 40 live turns target |

Normalization bounds verified in the release include:

- `keepLiveTurns`: 10 through 5,000;
- `snapshotBatch`: 5 through 100;
- `restoreBatch`: 5 through 100;
- heartbeat interval: 2 through 30 minutes;
- history mirror interval: 1 through 168 hours;
- server-sync delay: 0 through 5,000 ms.

Profile switching is persisted rather than being a display-only dropdown.

## Performance model

### Conversation containment

For non-Off profiles, the shipped CSS applies `content-visibility: auto` and an intrinsic height estimate to ChatGPT conversation-turn articles. This reduces layout/paint work for off-screen native turns while leaving the native turn elements in the document.

Turbo and Extreme additionally apply containment to older turns. Large preformatted blocks can be constrained to an internal scroll area when compact-heavy-block behavior is enabled. Old-turn media and sidebar links have separate containment/intrinsic-size optimizations.

### Motion reduction

When the setting is enabled, animation and transition durations inside old turns are reduced to near-zero duration. This is scoped to optimizer-marked old turns rather than a global page-wide animation ban.

### Dirty-turn scheduling

The archive layer does not blindly rewrite every visible message on every scan. A turn carries an optimizer snapshot hash and dirty marker. Snapshot capture skips unchanged turns and only writes changed/unsnapshotted entries.

The deterministic release gate includes a steady-state one-dirty-turn model and a 500-turn bounded snapshot model. These are model tests, not proof of current live ChatGPT performance.

### No network-response rewriting

The release validation explicitly checks that the shipped core does not replace `window.fetch`/`globalThis.fetch` and does not monkey-patch XMLHttpRequest `open`/`send` as a performance mechanism.

This is a permanent safety boundary for compatibility work unless a future verified design deliberately changes it with equivalent or stronger evidence.

## Local archive and recovery model

CUO uses IndexedDB database:

```text
cuoArchiveDB
schema version: 1
```

Verified object stores are:

```text
chats
  key: chatKey
  index: lastSeen

messages
  key: id
  indexes:
    byChat
    byChatSequence
    byUpdated
```

### Snapshot identity

A DOM snapshot stores:

- chat key;
- turn key;
- sequence;
- role;
- text;
- sanitized static HTML;
- approximate byte size;
- source (`dom` or `server-sync`);
- update timestamp;
- quick content hash.

Chat identity is derived from the current conversation route where possible. Verified route handling includes normal `/c/<id>` conversations and project conversations under `/g/.../c/<id>`. A non-conversation route falls back to a draft key based on origin/pathname.

### Snapshot sanitization

Before static HTML is persisted, the release removes active or unsafe embedded content such as scripts, iframes, object/embed nodes, base tags, refresh meta tags, inline event attributes, `srcdoc`, and `javascript:` URLs. Interactive cloned controls are marked static and made non-interactive.

The local archive is therefore intended as a recovery snapshot, not as a second fully live copy of ChatGPT's React component tree.

### Transaction ordering

Snapshot hashes are applied to the live turn only **after** the archive transaction completes. If persistence fails, the optimizer must not pretend the turn was safely archived.

This save-before-state-change rule is one of the v1.0.1 deterministic acceptance invariants.

## Extreme-mode freezing

Extreme mode can replace older, already-snapshotted live turns with optimizer-owned frozen cards to reduce live DOM cost. The frozen UI includes a restore action.

The key acceptance invariant is **save before freeze**. Release validation explicitly checks that the archive write completes before DOM replacement occurs.

Any future freeze implementation must preserve all of these conditions:

1. the exact turn has a durable local snapshot before replacement;
2. failed storage leaves the native turn intact;
3. restoring a frozen turn uses the corresponding archived identity, not a guessed sequence;
4. freezing never becomes a silent permanent-delete path;
5. Off and Balanced remain trustworthy non-freezing baselines;
6. a user can still export the complete locally archived history.

## Chat discovery and streaming detection

The v1.0.1 chat adapter primarily discovers turns through:

```text
article[data-testid^="conversation-turn-"]
[data-message-author-role]
```

A fallback walks role-bearing nodes to recover their containing turn when the primary article selector is unavailable.

Streaming detection checks for a visible Stop button and also treats very recent DOM mutation activity as a streaming signal. Current ChatGPT surface drift can invalidate either assumption, so selector success must be checked against actual message identity and streaming behavior, not only query-selector non-emptiness.

## Server-history mirror

CUO v1.0.1 contains a same-origin server-history mirroring layer. The verified source performs credentialed, no-cache JSON requests against ChatGPT's conversation-history endpoints and pages conversation listings in batches of 50.

The release path includes requests shaped like:

```text
/backend-api/conversations?offset=<offset>&limit=50&order=updated
```

Fetched conversation trees are normalized into ordered user/assistant messages before being written into the same local archive model.

### Important boundary

`/backend-api/...` is a ChatGPT web-application implementation path, not a stable project-owned public API contract. Treat it as a release-verified adapter that can drift. A future 2xx response alone is not sufficient verification; test pagination, conversation count, message ordering, project-conversation coverage, errors, cancellation, and restart behavior against the current product.

Do not turn a changed server endpoint into silent empty-history success.

## Export and portability

The v1.0.1 exporter supports:

- current chat to Markdown;
- current chat to JSON;
- complete CUO local archive to `.cuobackup.json`;
- complete local archive to a Markdown ZIP;
- an individual locally archived chat by key to Markdown or JSON.

The Markdown ZIP is generated client-side and contains:

```text
chats/<conversation>.md
index.json
README.txt
```

The exporter first snapshots the stable portion of the current conversation so a user-triggered export does not knowingly omit unsaved stable turns.

The backup schema is:

```text
chatgpt-ultimate-optimizer-backup
schemaVersion: 1
```

Import validates the schema before writing chat/message entries back into IndexedDB.

## Recovery and search

The local archive can:

- enumerate stored chats by most-recently-seen order;
- read messages in chat sequence order;
- remove one archived chat;
- clear the archive;
- export/import the complete backup object;
- search chat titles and message text.

Search has a default result limit of 50 in v1.0.1. Treat that as a UI/query result limit, not permission to truncate the underlying archive.

A destructive recovery control must never report success before its IndexedDB transaction completes.

## User interface

The release injects a floating `CUO` launcher that opens a dialog titled **ChatGPT Ultimate Optimizer**. Verified top-level tabs are:

```text
Performance
Recovery
Backup
Diagnostics
```

The Performance pane exposes the profile selector and live statistics including:

- turns on page;
- local snapshots;
- frozen turns.

Every optimizer control is part of the acceptance surface. A visible button or setting is not considered working because it renders. Its handler, persistence mutation, resulting archive/export/runtime behavior, error feedback, reload behavior, and restart behavior must be exercised where applicable.

## Installing the v1.0.1 userscript

The verified combined userscript is self-contained, uses `@grant none`, and declares both current and legacy ChatGPT hosts.

Practical installation path:

1. install a userscript manager such as Tampermonkey or Violentmonkey;
2. create/import a userscript from the exact `ChatGPT-Ultimate-Optimizer-Userscript-v1.0.1.user.js` release artifact;
3. confirm the manager reports version `1.0.1`;
4. open `https://chatgpt.com/`;
5. confirm the floating `CUO` launcher appears;
6. open the panel and exercise all four top-level panes;
7. verify profile persistence after reload;
8. verify archive creation before testing Extreme freeze behavior;
9. verify export/download behavior from an actual conversation.

A userscript-manager install is not equivalent to runtime proof. Confirm the page actually loaded the v1.0.1 build.

## Installing the v1.0.1 MV3 build

The verified release includes `ChatGPT-Ultimate-Optimizer-Extension-v1.0.1.zip`. For a development/unpacked Chromium-family install:

1. extract the exact extension ZIP to a stable directory;
2. open the browser's extension-management page;
3. enable developer mode;
4. load the extracted extension directory;
5. confirm the loaded extension identifies the expected v1.0.1 build;
6. open ChatGPT and verify the CUO launcher and panel;
7. inspect page and extension/service-worker errors;
8. reload ChatGPT and restart the browser before treating persistence as verified.

The historical managed-Chromium fixture did not reach CUO execution, so current live extension loading remains an open runtime verification item.

## Build and verification workflow

The v1.0.1 closeout directly verifies:

```text
npm run verify
```

The release lineage also separates build, validation, unit/performance-model, browser-smoke, packaging, and fresh-extraction checks. A future reconstructed canonical worktree should retain those gates rather than collapsing release qualification into one syntax check.

Verified release expectations include:

- deterministic build/package output;
- JavaScript syntax/safety/UI-control validation;
- unit and performance-model tests;
- no network-response rewrite hooks;
- save-before-freeze ordering;
- extension/userscript dual-build integrity;
- archive/package integrity;
- fresh extraction and rebuild verification;
- Git bundle verification;
- repository/project-memory doctors;
- a real browser smoke when the environment permits it.

## Modification map

### Change ChatGPT DOM discovery

Modify the chat/surface adapter responsible for turn discovery, role resolution, conversation identity, and streaming detection. Preserve fallbacks and add a real drift fixture before removing a working selector.

### Change performance profiles

Modify settings/profile definitions and the runtime/CSS consumer together. Update validation for defaults, normalization bounds, Off/Balanced/Turbo/Extreme behavior, and reload persistence.

### Change archive schema

Treat an IndexedDB version change as a migration. Preserve existing `cuoArchiveDB` data, exercise upgrade from schema version 1, verify old chat/message ordering, then verify export/import and restart behavior.

### Change freezing

Preserve save-before-freeze, failed-write safety, exact turn identity, restore behavior, and a non-freezing baseline. Never make freezing the only path to good performance.

### Change server-history mirroring

Keep server-history code isolated from DOM snapshot logic. Test current endpoint availability, authentication/session behavior, pagination, project conversations, ordering, partial failures, cancellation, and empty-result truthfulness.

### Change exports

Exercise Markdown, JSON, backup JSON, Markdown ZIP, and per-chat exports. Verify filenames, message counts, ordering, Unicode content, large conversations, duplicate chat titles, and import round trips.

### Change optimizer UI

Inventory every affected control in Performance, Recovery, Backup, and Diagnostics. Verify success, failure, repeat use, cancellation where supported, persistence, and restart behavior. Do not ship decorative or disconnected controls.

## Troubleshooting

### CUO launcher does not appear

- Confirm the expected v1.0.1 userscript/extension is enabled.
- Confirm the current URL matches a declared ChatGPT host.
- Check whether the page actually executed the CUO namespace initializer.
- Inspect page and extension/userscript-manager errors.
- If ChatGPT changed its route or CSP behavior, diagnose that instead of adding a second competing launcher.

### Long conversation is still slow

- Confirm the active profile is not `off`.
- Check whether conversation-turn discovery still identifies real turns.
- Confirm old-turn markers and containment styles are being applied to the intended content.
- Compare Balanced and Turbo before enabling Extreme.
- Keep native ChatGPT functionality and full archive coverage intact while profiling.

### Extreme mode removes a turn that cannot be restored

Treat this as a release-blocking data-preservation defect. Verify the archived turn exists in IndexedDB under the expected chat/turn identity before changing restore UI. Do not add a fallback that silently fabricates or skips the missing message.

### Local archive appears empty

- Verify IndexedDB `cuoArchiveDB` exists and can open.
- Check storage transaction failures and the latest optimizer error state.
- Confirm the current conversation has a stable chat key.
- If server mirroring is involved, distinguish DOM snapshot failure from `/backend-api` drift.

### Server history mirror reports an error

Do not convert an endpoint/auth/JSON error into an empty successful archive. Preserve the visible failure, verify the current authenticated product path, and keep existing local snapshots available.

### Export is missing the latest response

The exporter intentionally avoids treating a still-streaming response as stable. Confirm streaming detection is correct, wait until the native response is complete, then export again. If the response is complete but still excluded, debug the streaming/dirty-turn logic rather than weakening archive ordering.

### Browser smoke fails with `ERR_BLOCKED_BY_CLIENT`

The recorded v1.0.1 managed-Chromium fixture hit this before CUO executed. Confirm whether the current browser/profile or policy is blocking the disposable host. Do not report CUO runtime failure or success until the extension/userscript itself executes.

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
- Preserve the full local archive and portable export paths while optimizing rendering.
- Do not replace resilient semantic targeting with brittle class-name snapshots.
- Do not silently delete or lose native ChatGPT messages or controls to make optimizer UI simpler or faster.
- Do not add a second destructive message-culling layer without durable save-before-replacement and exact recovery proof.
- Do not turn a result limit, snapshot batch, or keep-live target into a cap on the underlying archived conversation dataset.
- Do not rewrite ChatGPT fetch/XHR responses as a performance shortcut.
- Do not interfere with Projects, Work, Library/Drive flows, native paste-to-attachment conversion, Voice, or desktop navigation.
- Do not treat a successful build as proof that Chat, Work, Projects, Library, search, file surfaces, desktop flows, server mirroring, or userscript parity still behave correctly.
- Keep success/failure states truthful when a target surface, authenticated history endpoint, export path, or storage operation is unavailable or has changed.

## Current research direction

The strongest immediate improvement is a **surface capability and data-source matrix** rather than more selector patches. Track at least:

```text
surface -> capability -> authoritative data source -> selector/anchor strategy -> fallback -> verified date -> real smoke evidence
```

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
- CUO local archive and restore;
- CUO server-history mirror;
- all export formats;
- every optimizer-owned panel, command, shortcut, and setting.

For conversation-derived features such as search, timeline, export, or navigation, prefer complete data-backed discovery when available, then reconcile that data with the native virtualized UI. Do not require every historical message to remain mounted and do not create an unverified destructive virtualization layer.

## Acceptance test for the next release

A successor release should prove, in a real supported browser profile:

1. exact build identity is loaded;
2. optimizer controls render and operate on Chat without dead actions;
3. all four CUO panes exercise their real handlers and truthful error paths;
4. navigation between Chat, Work, Projects, Library, and search does not duplicate or orphan optimizer state;
5. local IndexedDB snapshots survive reload and browser restart;
6. Extreme mode saves before freezing and restores the exact frozen turns;
7. local search and recovery operate on complete archived data rather than the mounted DOM only;
8. server-history mirroring either completes current authenticated pagination or reports a real failure without destroying local snapshots;
9. Markdown, JSON, backup JSON, Markdown ZIP, and per-chat export paths preserve expected messages and ordering;
10. Library/Drive file selection and native file actions remain functional where available;
11. long-paste conversion still follows the native attachment path rather than being intercepted by optimizer code;
12. conversation search/timeline/export logic retains complete data coverage without silent optimizer-owned caps;
13. reload and browser restart preserve intended settings;
14. both extension and userscript builds either pass the same functional matrix or explicitly document intentional differences;
15. console/service-worker errors are inspected and material failures remain visible;
16. desktop-specific behavior is tested only on desktop platforms the release actually claims to support.

## Exact next action

Reconstruct or resolve the canonical source worktree from the verified v1.0.1 Git bundle and release archive, preserving the current release hashes. Before compatibility edits, add a read-only drift probe that records:

- detected ChatGPT surface and route;
- turn/role selectors and counts;
- streaming-state evidence;
- available conversation-history data source and pagination result;
- CUO archive database/version and local chat/message counts;
- optimizer UI attachment state;
- active profile/settings identity;
- current build kind/version.

Run that probe against Chat, Work, Projects, Library/Drive, unified search, and long-paste attachment conversion without mutating ChatGPT. Then make the smallest compatibility repair supported by the probe and exercise both MV3 and userscript builds in a real supported browser with reload/restart, archive/restore, export, and server-mirror evidence.

## Wiki maintenance

Update this page when a newer verified release/tag appears, the canonical repository/worktree is re-resolved, the IndexedDB or backup schema changes, server-history mirroring changes, OpenAI materially changes ChatGPT navigation/host surfaces, or real browser/runtime evidence supersedes the current blocked smoke result.
