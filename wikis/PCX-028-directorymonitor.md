# DirectoryMonitor Wiki

**Project Constellation ID:** `PCX-028`  
**Status:** ACTIVE / TRACKED  
**Confidence:** Medium  
**Canonical source repository:** unresolved in connected GitHub and Drive evidence  
**Current documentation authority:** durable Project Constellation contract plus current primary-source watcher/platform evidence

## Purpose

DirectoryMonitor is the filesystem-change-awareness track for reliable, low-latency detection of directory and file changes without silently losing events. Its core requirement is **correct final state**, not merely a fast stream of watcher callbacks.

A watcher event is evidence that something may have changed. The filesystem remains authoritative when notifications overflow, disconnect, coalesce, arrive out of order, are dropped during restart, or differ across operating systems and network filesystems.

The project therefore needs two distinct layers:

1. **low-latency observation** from a watcher backend; and
2. **authoritative reconciliation** whenever continuity is uncertain.

A backend that is fast but cannot prove when it lost continuity is not acceptable for DirectoryMonitor.

## Current verified Project Constellation contract

The current durable Project Constellation record requires DirectoryMonitor to:

- provide reliable low-latency filesystem change awareness;
- detect watcher overflow or stale watcher state;
- reconcile against authoritative filesystem state after continuity loss;
- preserve complete monitored state rather than silently discarding paths to reduce work.

No standalone implementation repository, executable, package manifest, or build system has yet been resolved. Implementation language, current consumers, API shape, and current runtime coverage therefore remain intentionally unclaimed.

## Current stop point

The architecture/correctness contract is now strong enough to qualify a recovered implementation, but there is still no source-backed DirectoryMonitor runtime to install or build from this page.

**Do not initialize a replacement project simply because the source is unresolved.** Search and identify the existing implementation first, then verify it against the qualification matrix below.

## Exact next action

1. Resolve the project-owned DirectoryMonitor source or artifact identity.
2. Record repository, branch/commit, manifest/package identity, supported operating systems, and current consumers.
3. Run the deterministic mutation/overflow/restart corpus in this page against the recovered implementation.
4. Add an authoritative reconciliation path before optimizing throughput or swapping watcher libraries.
5. Only after parity is proven, evaluate backend upgrades such as notify 9 or a Watchman service lane.

## Current watcher technology baseline

### notify-rs stable lane: notify 8.2.0

The official notify-rs release history identifies **notify 8.2.0** as the latest stable `notify` release. It was released on 2025-08-03.

Relevant stable behavior includes:

- reporting when Linux inotify `max_user_watches` is exhausted;
- native platform backends rather than a synthetic polling-only model;
- companion debouncer/file-ID support for higher-level event handling.

Reference: <https://github.com/notify-rs/notify/releases/tag/notify-8.2.0>

**Production-candidate rule:** if the recovered DirectoryMonitor is Rust and does not already have a stronger verified backend, qualify stable 8.2.0 first. Do not upgrade merely because a prerelease exists.

### notify-rs bleeding-edge lane: notify 9.0.0-rc.4

The current prerelease is **notify 9.0.0-rc.4**, released 2026-05-02.

Changes directly relevant to DirectoryMonitor qualification include:

- preserving watched-path representation in emitted event paths;
- replacing an existing same-path watch rather than leaking duplicate Windows watch handles or FSEvents paths;
- earlier 9.0 RC work adding `Watcher::watched_paths`, explicit path updates, Windows separator-style controls, synchronous watch removal, Linux `UNMOUNT` surfacing, and panic hardening.

Reference: <https://github.com/notify-rs/notify/releases>

**Bleeding-edge rule:** rc.4 is a controlled experiment candidate, not an automatic production replacement for stable 8.2.0. Run the same final-state corpus against both versions and require equal correctness before considering promotion.

### Watchman service lane: v2026.08.10.00

The current official Watchman release is **v2026.08.10.00**, released 2026-08-10.

Reference: <https://github.com/facebook/watchman/releases/tag/v2026.08.10.00>

Watchman is useful as a **separate service-backed qualification lane** for large trees, long-running subscriptions, or repositories where a dedicated watcher service gives better operational resilience.

It must not become a second source of truth. DirectoryMonitor still needs an explicit reconciliation contract when subscriptions are recrawled, invalidated, disconnected, or restarted.

## Native platform correctness requirements

### Windows: ReadDirectoryChangesW

Microsoft documents an important fail-closed behavior for `ReadDirectoryChangesW`:

- changes occurring between reads accumulate in a buffer associated with the directory handle;
- if that buffer overflows, detailed contents are discarded and the result can indicate zero transferred bytes;
- `ERROR_NOTIFY_ENUM_DIR` means the system could not record all directory changes;
- in either loss condition, the application must compute the changes by enumerating the directory or subtree;
- when monitoring a directory over the network, buffers larger than **64 KiB** can fail with `ERROR_INVALID_PARAMETER` because of the underlying packet-size limit.

References:

- <https://learn.microsoft.com/windows/win32/api/winbase/nf-winbase-readdirectorychangesw>
- <https://learn.microsoft.com/windows/win32/fileio/obtaining-directory-change-notifications>

**DirectoryMonitor requirement:** zero-byte/overflow and `ERROR_NOTIFY_ENUM_DIR` are not ordinary empty event batches. They are continuity-loss signals and must force reconciliation before the model is trusted again.

### Windows NTFS/ReFS recovery lane: USN change journal

Microsoft documents the USN change journal as a persistent per-volume record of filesystem changes and explicitly notes that it can be more efficient than registering large numbers of directory notifications.

Important integrity rules:

- records identify the changed object and reason, not a reversible copy of the change;
- old records can be trimmed;
- the journal has an identifier that changes when prior records may no longer be valid;
- consumers must track both the journal identifier and USN position;
- when needed history is unavailable, the correct recovery is a re-index/reconciliation scan rather than pretending continuity survived.

References:

- <https://learn.microsoft.com/windows/win32/fileio/change-journals>
- <https://learn.microsoft.com/windows/win32/fileio/using-the-change-journal-identifier>
- <https://learn.microsoft.com/windows/win32/fileio/change-journal-records>

**DirectoryMonitor proposal:** on supported local NTFS/ReFS volumes, qualify an optional USN catch-up/recovery lane. It may reduce the cost of recovering missed events, but it must never replace the authoritative directory model or make network/non-journal filesystems unsupported by accident.

### Linux: inotify overflow is explicit state loss

Linux inotify emits `IN_Q_OVERFLOW` when its event queue overflows. The event uses watch descriptor `-1`.

Reference: <https://man7.org/linux/man-pages/man7/inotify.7.html>

**DirectoryMonitor requirement:** treat `IN_Q_OVERFLOW` as an immediate model-invalidating signal. Reconcile the affected root before returning to a trustworthy steady state.

## Proposed normalized event contract

A backend-neutral observed event should preserve enough evidence to diagnose behavior and decide whether reconciliation is required:

```text
sequence              monotonic DirectoryMonitor observation sequence
backend               backend/library/API identity
backendVersion        exact version when available
rootId                 stable monitored-root identity
kind                   create/modify/remove/rename/metadata/other
path                   observed path
oldPath/newPath        rename/move pair when the backend can prove it
fileIdentity           inode/file ID when available and trustworthy
observedAt             monotonic + wall-clock timestamp pair
rawFlags               original backend flags/error data
continuity             intact | uncertain | lost
reconcileGeneration    authoritative-scan generation after recovery
```

Do not force every backend into fake precision. If a backend cannot prove a rename pair or file identity, preserve that uncertainty rather than fabricating it.

## Required monitor state

A recovered implementation should expose or persist enough state to answer:

- Which roots are actively watched?
- Which backend/version owns each watch?
- When was each root last authoritatively reconciled?
- Has continuity been lost since that reconciliation?
- What overflow/unmount/disconnect/restart signal caused the current uncertainty?
- Which generation of the authoritative model is currently served?
- Are events still draining from an older watcher instance after replacement?

A watcher thread/process being alive is not proof that any of those conditions are healthy.

## Deterministic qualification corpus

Run the same corpus against every candidate backend. Use a temporary tree whose final expected state is known independently of watcher events.

### Basic mutations

1. Create a file.
2. Append and overwrite content.
3. Change size and metadata independently.
4. Delete the file.
5. Create and remove directories.
6. Rename a file within one directory.
7. Rename a directory containing children.
8. Move a file across watched directories.
9. Replace a file atomically using write-temp + rename/replace.
10. Create a file and delete it before the debounce window closes.

### Identity and path cases

11. Watch a relative root and verify emitted-path representation.
12. Use Unicode and non-ASCII filenames.
13. Exercise case-only rename where the filesystem supports it.
14. Exercise symlink/junction behavior without silently following a different tree.
15. Replace an existing same-root watch and verify no duplicate watcher remains active.

### Burst and overflow cases

16. Generate a burst large enough to trigger the backend's documented overflow condition.
17. Prove the implementation marks continuity lost.
18. Perform authoritative reconciliation.
19. Prove the recovered model exactly matches a direct filesystem enumeration.
20. Prove no stale pre-reconciliation event can corrupt the new generation.

### Lifecycle cases

21. Stop and restart the watcher while mutations occur.
22. Crash/kill the watcher process or thread where practical, then recover.
23. Unmount/disconnect the watched filesystem where the platform permits a safe fixture.
24. Reconnect/recreate the root and prove stale handles are not treated as healthy.
25. Restart the host application and prove the rebuilt model equals the authoritative tree.

### Network/filesystem cases

26. Qualify local NTFS/ReFS, ext4 or the project's actual production filesystems separately.
27. Qualify SMB/network roots separately from local Windows roots; do not reuse unsafe buffer assumptions.
28. Mark unsupported filesystems explicitly rather than silently downgrading correctness.

## Acceptance criteria

A backend is acceptable only when all applicable cases satisfy these rules:

- final DirectoryMonitor model exactly equals authoritative filesystem enumeration;
- every forced continuity-loss condition is detected;
- overflow recovery completes without dropping surviving files or resurrecting deleted ones;
- duplicate/coalesced callbacks do not produce duplicate model entries;
- same-path watcher replacement does not leave duplicate active watches;
- restart restores a correct final model;
- backend-specific event ordering differences do not change final state;
- performance comparisons use the same mutation corpus and the same correctness requirements.

A faster backend that ends with a different model automatically loses the comparison.

## Reconciliation algorithm contract

The implementation is free to optimize, but the state transition should remain conceptually equivalent to:

1. mark the root `uncertain` or `lost` when continuity cannot be proven;
2. stop publishing watcher-derived state as authoritative;
3. snapshot/enumerate the authoritative root;
4. diff that snapshot against the last trusted generation;
5. atomically publish a new model generation;
6. discard or reclassify watcher events that belong to the old generation;
7. resume low-latency watcher updates only after the new generation is active.

If an optional USN/Watchman catch-up path can prove a complete interval, it may reduce the reconciliation cost. If it cannot prove completeness, fall back to authoritative enumeration.

## Performance qualification

Measure correctness first, then performance.

Useful metrics include:

- cold initial scan duration;
- steady-state event-to-model latency;
- CPU and memory at idle;
- CPU and memory during a fixed mutation burst;
- overflow recovery duration;
- restart recovery duration;
- number of duplicate/coalesced raw callbacks;
- number of authoritative rescans;
- maximum monitored-root and file counts reached without state divergence.

Do not optimize by hiding off-screen paths, dropping "uninteresting" files, capping the model, or deferring correctness work indefinitely.

## Troubleshooting

### Watcher appears alive but changes stop arriving

Treat the root as stale until proven otherwise. Verify the backend's active-watch list/handle state when available, mark continuity uncertain, and reconcile the filesystem before resuming trusted output.

### Windows returns zero bytes or `ERROR_NOTIFY_ENUM_DIR`

Assume detailed changes were lost. Enumerate/reconcile the directory or subtree. Do not interpret this as a harmless empty batch.

### Windows network watch fails with a large buffer

`ReadDirectoryChangesW` documents a 64 KiB network-buffer limit. Qualify SMB roots with a safe buffer size and a separate fixture rather than copying local-volume tuning blindly.

### Linux emits `IN_Q_OVERFLOW`

Mark continuity lost and reconcile. The overflow event is itself evidence that the queue no longer contains a complete history.

### USN journal identifier changed or needed records were trimmed

Discard the saved journal cursor as authoritative. Perform a full reconciliation/re-index and start from a newly verified journal position.

### Rename arrives as separate remove/create events

Do not fabricate a rename pair unless file identity or backend semantics prove it. Final-state reconciliation is more important than preserving an aesthetically pleasing event stream.

### Duplicate callbacks appear after replacing a watch

Verify the old watch is fully removed before trusting the replacement. Candidate backends must pass the same-path replacement fixture.

## Anti-degradation contract

- Never treat an overflow/lost-continuity signal as success.
- Never reduce correctness by dropping paths, capping results, viewport-culling, or ignoring off-screen state.
- Never infer health only from a live watcher thread/process.
- Never publish a watcher-derived model as authoritative while reconciliation is pending.
- Never auto-promote a prerelease backend because its version number is newer.
- Never use a USN journal or Watchman service as an excuse to remove full reconciliation support.
- Never compare backend performance unless both produce the same final filesystem model.
- Never overwrite or delete user files as part of a watcher correctness test; use isolated fixtures.

## Current documentation boundaries

Verified now:

- durable Project Constellation correctness requirement;
- latest stable/prerelease notify lanes and their relevant watcher behavior;
- current Watchman release lane;
- Windows overflow/re-enumeration behavior from Microsoft documentation;
- Windows USN journal integrity/recovery semantics;
- Linux `IN_Q_OVERFLOW` semantics;
- a backend-neutral reconciliation and acceptance contract suitable for qualifying the recovered source.

Still unresolved:

- canonical DirectoryMonitor source repository/artifact;
- implementation language/runtime;
- actual backend currently used by the project;
- current consumers/integrations;
- supported filesystems and operating systems;
- current performance baseline;
- exact build/install/package commands.

## Wiki maintenance

Update this page when the canonical implementation is found, watcher backends are verified or upgraded, platform support is established, reconciliation/overflow behavior changes, or an actual performance/runtime baseline is produced. Preserve stable-vs-prerelease qualification history and backend-specific evidence rather than rewriting it into a generic "watcher works" claim.
