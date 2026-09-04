# CurseForge Universal Mods v1.8.0 final checkpoint

## Canonical release

- Target: CurseForge 1.319.0.38738
- Verification target: official native Linux CurseForge 1.319.0~38738-38738 plus converged Windows overlay bytes
- Wine: not used in the v1.8 validation pass
- Patcher ZIP: CurseForge-Universal-Mods-Patcher-v1.8.0.zip
- Patcher ZIP SHA-256: 49aca4c5f55dfcb98c8a29b0c257903aa020ff0f9d6c33339b60dd96fa49d531
- DirectPatch ZIP: CurseForge-Universal-Mods-DirectPatch-1.319.0-38738-v1.8.0.zip
- DirectPatch ZIP SHA-256: 281807c6bea4717db6ea13e4cb2e9f1023ec221b3f9926961b40f556889150c3
- Windows patcher EXE SHA-256: 0fd66ca2e8fa9efed41509f34ac7f541f3fb16ca4a69caf553552617eec05461
- Patched CurseForge.exe SHA-256: 5aac369845a53f45064367f63a30d1b4c820fb18850cbcf57821cd2874eaf0ad
- Patched app.asar SHA-256: 8cbc1eb92e1edf42b888f0108dce1e10f9c1534714ac5d2a99169eeea335ca4f
- Patched ASAR header SHA-256: 88a7b46b0a76c78d0a8c100ee8bbdd49aec7410e8ff9329f08bc6d970a0ecf48

## Acceptance implemented

- No standalone Modrinth tab/browser/Add Content button/second Update All button.
- Modrinth + unmatched Local content merges at CurseForge's native InstalledProjects profile result boundary.
- Profile Content Filter uses CurseForge's native Source state/options: CurseForge / Modrinth / Local.
- Mods and Resource Packs supported; Resource Packs include ZIPs and unpacked pack.mcmeta folders.
- Native profile Update All count/enabled flow includes applicable Modrinth updates after CurseForge's existing confirmation.
- Per-row Modrinth update remains on the native project row; source marker is informational only.
- Resource Packs suppress unsupported mod enable/disable and active-state bulk selection rather than exposing a dead control.
- Scanner refresh is event-driven; no recurring watchdog/poll/repatch loop.
- Manual patch/update workflow only; no Scheduled Task creation. The only scheduled-task operation is deletion of the obsolete v1.0-v1.4 auto-repatch task.

## v1.7 defects found and fixed in v1.8

1. Double merge could erase synthetic action identity after rows were already visible.
2. Leftover status toolbar still modified the Add Content area.
3. Modrinth source marker looked like a clickable control.
4. Duplicate Update All events could start concurrent Modrinth batches.
5. Dependency installation could inherit a parent Resource Pack's folder instead of resolving the dependency's own project type.
6. Unpacked Resource Pack folders could duplicate a native recognized folder pack.
7. Exact same CurseForge release has two proven Windows/Linux minified profile-anchor variants; v1.8 handles both explicitly instead of assuming identical minification.
8. An installed dependency with unknown version ID could incorrectly satisfy an exact required dependency version.
9. MutationObserver woke on unrelated CurseForge pages instead of only active Minecraft profile routes.
10. Synthetic Resource Packs could expose mod-JAR active-state UI that the backend correctly refused; v1.8 suppresses those controls and preflights direct mixed calls.

## Verification

- Clean final source Go tests: PASS.
- QOL JavaScript suite: PASS.
- Injected renderer/main/preload syntax: PASS.
- Official native Linux 1.319.0.38738 upstream integration audit: PASS.
- Native Linux test series: real CurseForge window painted; main/preload/renderer bridges observed in the v1.8 series.
- Exact-final-source native smoke: main bridge, Electron App Ready, SessionStarted, and real Curse.Agent.Host observed.
- Native sandbox boundary: CurseForge core cannot finish because its games catalog cannot be downloaded; final live Minecraft Content-page click-through is not claimed.
- Windows v1.5 -> v1.8 using Linux-native patcher: PASS.
- Windows v1.6 -> v1.8 using Linux-native patcher: PASS.
- Windows v1.7 -> v1.8 using Linux-native patcher: PASS.
- All three final Windows EXE and ASAR outputs converge byte-for-byte: PASS.
- ASAR integrity: 244 packed / 244 full SHA-256 / 244 block SHA-256 records PASS; no overlap or out-of-bounds.
- Windows EXE contains current ASAR header hash exactly once; v1.5/v1.6/v1.7 old header hashes are absent.
- Exact production desktop/background/preload/injected-renderer JavaScript syntax: PASS.
- Production marker audit: native Source filter, resource-pack toggle guard, native Update All bridge present; removed standalone/ghost Modrinth controls absent.
- Injected code: no setInterval, no filesystem watcher, no 15-minute cadence, no Scheduled Task creation.
- Final ZIP integrity: PASS for both archives.
- Fresh final Patcher ZIP extraction: bundled Go/QOL/syntax/Linux-upstream tests PASS.
- Fresh-extracted source rebuilt natively on Linux and patched a new untouched v1.5 Windows overlay to the exact canonical v1.8 EXE/ASAR hashes: PASS.
- Fresh patch status after that install: installed.

## Exact next action

Use the v1.8 Patcher ZIP on the user's normal Windows CurseForge 1.319.0.38738 installation. If the live Windows profile Content page produces a new concrete mismatch, preserve v1.8 as the canonical baseline and fix only that observed delta. Do not restore the removed Modrinth split UI and do not add a watchdog/background repatcher.
