# DirectoryMonitor Wiki

**Project Constellation ID:** `PCX-028`
**Status:** ACTIVE / TRACKED
**Confidence:** Medium
**Canonical source repository:** unresolved in connected evidence

## Purpose

DirectoryMonitor is the filesystem-change-awareness track for reliable, low-latency detection of directory and file changes without silently losing events. Its core requirement is correctness under burst load, watcher overflow, rename/move behavior, disconnects, restarts, and filesystem races.

## Current verified Project Constellation contract

The current durable Project Constellation record defines the goal as reliable, low-latency filesystem change awareness and explicitly requires the monitor to detect overflow or stale watchers and reconcile against authoritative filesystem state.

That requirement is more important than any specific watcher library. A watcher event is a hint about state change; the filesystem remains the authority when event streams overflow, disconnect, coalesce, or lose continuity.

## Current stop point

No standalone DirectoryMonitor source repository or current implementation artifact was resolved in the connected GitHub/Drive search for this pass. Therefore implementation language, API, host integration, and current test coverage are intentionally left unclaimed.

## Exact next action

Resolve the project-owned DirectoryMonitor implementation, then add a deterministic watcher-overflow/reconciliation harness before adopting or upgrading any watcher backend.

## Current technology research

### notify-rs

The official [notify-rs/notify](https://github.com/notify-rs/notify) repository's current `main` manifest identifies the core `notify` crate as **9.0.0-rc.4**. It is a cross-platform filesystem notification library with native backends including Windows filesystem APIs, Linux inotify, and macOS FSEvents/kqueue.

Because 9.0.0 is still an RC on the inspected main branch, it is a **bleeding-edge experiment candidate**, not an automatic production upgrade.

### Watchman

The official [facebook/watchman](https://github.com/facebook/watchman) repository is active and was pushed on 2026-08-16. Watchman is a long-running filesystem watcher/service intended to watch files and trigger actions when they change.

**Proposal:** benchmark two adapters behind one normalized, lossless DirectoryMonitor contract:

- an embedded `notify` adapter for lightweight in-process use;
- an optional Watchman adapter for large trees, long-running subscriptions, or cases where a dedicated watcher service improves resilience.

Neither adapter may become the sole source of truth. Both must support reconciliation against an authoritative scan/index after overflow or lost continuity.

**Integration cost:** medium to high depending on the current project architecture, which is still unresolved.

**Risks:** event coalescing, platform-specific rename semantics, buffer overflows, symlinks, network filesystems, and large-tree startup can produce different streams across backends. A fast watcher that silently loses changes is a regression.

**Small experiment:** capture the same fixed mutation script across Windows/Linux where available: create, modify, atomic replace, rename, move across directories, delete, rapid burst, directory tree delete/recreate, watcher restart, and forced overflow/reconcile.

**Acceptance test:** after every scenario, the final monitored model equals an authoritative filesystem scan; no event loss remains undetected; duplicate/coalesced events do not corrupt state; restart restores correct state; the adapter can report when continuity is uncertain instead of pretending success.

## Proposed normalized event contract

A backend-neutral event should preserve enough evidence for reconciliation:

- monotonic observation sequence
- backend name/version
- root identity
- event kind
- old/new path when known
- file identity when available
- observation timestamp
- overflow/rescan-required flag
- raw backend metadata for diagnostics
- reconciliation generation

## Anti-degradation contract

- Never reduce polling/reconciliation frequency merely to lower CPU if it can miss required changes.
- Never discard off-screen or "uninteresting" paths when the project contract expects the full directory state.
- Never infer that a watcher is healthy only because its process/thread is alive.
- Never accept a benchmark win that produces a different final filesystem model.

## Documentation gaps

- Canonical source repository unresolved.
- Current language/runtime unresolved.
- Current consumers/integrations unresolved.
- Current performance baseline and supported filesystems unresolved.

## Wiki maintenance

Update this page when the canonical implementation is found, watcher backends are verified, platform support is established, or reconciliation/overflow behavior changes. Keep backend-specific behavior separate from the normalized correctness contract.