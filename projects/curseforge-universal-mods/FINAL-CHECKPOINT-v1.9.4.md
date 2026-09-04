# CurseForge Universal Mods v1.9.4 hardening checkpoint

Date: 2026-09-04
Target: CurseForge 1.319.0.38738
Supersedes: v1.9.3
Live-user-machine acceptance: **pending**; do not claim the original Windows UI reproducer fixed until the user installs this build and confirms it.

## Purpose

v1.9.4 is a reliability hardening pass over the v1.9.3 live InstalledProjects bootstrap. It preserves the filesystem-first/multi-provider architecture while hardening races, profile selection, disk state, patch/recovery safety, exact status detection, and diagnostics.

## Hardened behavior

- Main-process scans are single-flight per profile. Identical requests join; materially different/forced requests serialize behind the active scan.
- Forced provider refresh cannot be silently downgraded behind a passive scan.
- Renderer keeps the newest meaningful live-collection request while a scan is in flight and replays it once after completion.
- Native collection cooldown applies only when the collection signature is unchanged. A changed installed set bypasses cooldown.
- InstalledProjects action-proxy readiness is single-flight and no longer blocks live filesystem inventory; the bounded handshake runs in parallel.
- Cache and provider-provenance writes are serialized and atomic (temp + fsync + rename), preventing lost concurrent provenance writes and truncated JSON.
- Filesystem overlap alone requires a 60% majority of the available live native filenames and a unique best candidate. Ties/insufficient matches fail closed.
- Runtime `__CFUM_DIAGNOSTICS__()` reports loaded/bridge version, route/GUID, profile resolution, native/filesystem counts, scan/pending state, and last live-sync error without mutating state.
- Patch/restore uses one exclusive install lock.
- CurseForge shutdown is verified before mutation.
- New backups are hashed and EXE/ASAR-linked before older recovery points are pruned.
- Malformed backup manifests fail closed.
- Restore Latest Backup skips a corrupt newest backup and tries the next verified recovery point.
- `-check` verifies exact embedded v1.9.4 main/preload/UI/CSS bytes, HTML markers, native anchors, and EXE/ASAR linkage rather than generic version markers.
- Post-patch status verification is mandatory; failure rolls back.
- Only stale Universal-Mods-owned temp patterns older than one hour are cleaned under the lock.

## Regression retained

- 631 actual JAR/disabled-JAR files + 585 native InstalledProjects rows -> 631 unique merged native rows in the deterministic regression.
- 46 disk files omitted from the 585-row native collection are recovered in that reproducer.
- CurseForge ownership, exact Modrinth identity, Local classification, and Repaired provenance remain distinct/coexisting concepts.
- Provider/version actions remain CurseForge-native context-menu rows; CurseForge native Update/Update All remains the bulk surface.
- No watchdog, Scheduled Task creation, filesystem watcher, recurring polling, or automatic repatching.

## Verification performed this run

- `go test ./...`: PASS
- `node tests/qol-tests.cjs`: PASS
- renderer/background/preload JS syntax checks: PASS
- backend scan single-flight + force escalation regression: PASS
- renderer pending refresh replay regression: PASS
- changed-collection-vs-cooldown regression: PASS
- concurrent provider-provenance write preservation: PASS
- profile ambiguity/60% confidence regression: PASS
- patch lock and stale-temp cleanup Go tests: PASS
- exact recovered v1.9.3 core -> v1.9.4: PASS
- v1.9.4 `-check`: installed on patched disposable real-lineage bundle
- 244/244 packed ASAR full SHA-256 records: PASS
- 244/244 ASAR block SHA-256 records: PASS
- v1.9.4 ASAR header occurs exactly once in patched CurseForge.exe: PASS
- production ASAR contains hardened renderer/background/preload/html/desktop payloads: PASS
- deliberately corrupt newest backup rejected; older verified backup restored exact v1.9.3 EXE/ASAR: PASS
- restore -> repatch converged byte-for-byte to the same v1.9.4 EXE/ASAR: PASS
- final Patcher ZIP fresh extraction: PASS
- source inside final Patcher ZIP rebuilt the Windows patcher byte-for-byte with `GOOS=windows GOARCH=amd64 CGO_ENABLED=0 go build -trimpath -ldflags="-s -w"`: PASS
- standalone source archive byte-content equals source shipped inside final Patcher ZIP: PASS
- fresh exact v1.9.3 core patched from freshly extracted source -> frozen v1.9.4 hashes: PASS
- Drive-downloaded patcher/source byte identity: PASS
- Drive-downloaded DirectPatch parts hash/reassembly/ZIP/byte identity: PASS
- Drive support text files byte identity: PASS
- Drive checkpoint/readback receipt byte identity: PASS

## Frozen release hashes

- Patcher ZIP: `98e2c0959893211731d97adc9d7bef5a20fbb3f5a206fd14ad99a134227e48e9`
- DirectPatch ZIP: `06d46ee84b5edd7ebbe459203738126ef24f9ce7d9bf7d4e21858bf81297a68d`
- Source archive: `71411fd7786cfaabbd674ff9d5ef6ddcbce299fa1797b14ac71956083a4e5507`
- Windows patcher EXE: `461b7f3d2e85a08743bafdcdda29023bc0e5e488786cc15a844ef0b17c951722`
- Patched CurseForge.exe: `9dab441b3a8d175bfbe79ffa5b70a1ebc5bc0bfb352a698d50c40366e75cb874`
- Patched app.asar: `40afa7cf8161ba9952620785e3072e497bae0de85a16b8afcc667992ab11bb33`
- ASAR header: `b39cdd7167d3ead4074974e112ce7897c83355d12fdc9025c56600fac3d281d4`

## Google Drive publication

Canonical folder: `1HcVsT6o1Za0yFrfk_TAyGxC6YHiLT7S5`

- Patcher: `1dFjvkEYHkxPq9jk51yzOXJ33JJsLX8La`
- Source: `1CRZkujnNVWzlqGCV-whIMHt_YK-jtipO`
- Fresh extraction gate: `11Pe7AOYneW_lge9G_vQiV3zGp91aujIx`
- Release checksums: `1mfhaeqqrGHojZmwGhkqPmB1BWshnzDiX`
- DirectPatch part checksums: `1UN2ar0lkBjhEbDg0RY2D-NEBBrZqnT4j`
- DirectPatch multipart README: `1roEGiv5NJfETgNFmFIg-qM7pR-9YQPlg`
- Reassemble command: `1qdzXpVzjzDYVPTusQWP_BN9nKkwrrbaD`
- DirectPatch part000: `1kibS5IfV-SgvB_7XK5_dzEMrd7RWTYSa`
- DirectPatch part001: `1eyNK5BVriNtjyRW0MpJHWwG9hCoGkjvD`
- DirectPatch part002: `1i3KxfYdbZEQK3hIurDHvvIIEqji91WP-`
- Final checkpoint: `1kEr-ssbsGWU11xtugtsIarGKDYpwYx1K`
- Drive readback receipt: `1II_HocZyUrjNWEYs_6IViZb-J-S5u_tT`

The complete 110.8 MB DirectPatch is represented on Drive by the verified three-part transport, reassembled to exact SHA-256 `06d46ee84b5edd7ebbe459203738126ef24f9ce7d9bf7d4e21858bf81297a68d`.

## Exact next action

Install v1.9.4 over the user's current v1.9.3 CurseForge 1.319.0.38738, reopen the affected profile Content page, and perform the real live-Windows acceptance test. Confirm the mod count leaves 585 toward the real filesystem count (631 for the unchanged reproducer) and that a normal CurseForge row exposes the native `Open on CurseForge` context action. If live behavior still fails, call `__CFUM_DIAGNOSTICS__()` in the CurseForge renderer console and use its exact state to fix the failing layer rather than guessing.
