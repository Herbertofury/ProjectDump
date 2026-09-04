# CurseForge Universal Mods v1.9.3 final checkpoint

Date: 2026-09-04
Target: CurseForge 1.319.0.38738
Supersedes: v1.9.2

## Why v1.9.3 exists

Live Windows acceptance of v1.9.2 failed visibly: the affected profile still showed **Mods (585)** and the per-mod context menu still showed only CurseForge's original **Disable project / Lock from changes / Delete Mod** actions. The v1.9.2 filesystem/provider model passed isolated tests, but the live renderer could still wait on a guessed React route before populating the real InstalledProjects collection.

v1.9.3 removes that route dependency from the production path.

## Production fix

- CurseForge's own `InstalledProjectsAppService.getProjects(gameInstanceGuid)` result is now the authoritative profile-open signal.
- The first real native collection result starts filesystem scanning directly, even with empty/unmatched route state.
- The live native collection is retained per GUID for later refresh/action rescans.
- Profile resolution uses app candidate paths when available, then the live `gameInstanceGuid`, then native installed-filename overlap across standard CurseForge profile roots.
- `codex-universal-mods.js` is injected before CurseForge `desktop.js`, so merge/context hooks exist before the first native collection request.
- The native context-menu integration receives the full live native row. A normal CurseForge row can show **Open on CurseForge** immediately even before filesystem/provider enrichment finishes.
- v1.9.3 explicitly recognizes the exact v1.9.2 patched context-menu lineage and upgrades it in place.

## Acceptance retained

The filesystem-first regression remains **631 real JAR/disabled-JAR files + 585 CurseForge native rows -> 631 unique rows**, recovering all 46 disk files omitted from InstalledProjects when those files are still present.

## Verification

- Go tests: PASS
- QOL JavaScript suite: PASS
- dynamic no-route collection bootstrap test: PASS; exactly one scan starts from the live GUID without route state
- 631/585 filesystem-first regression: PASS
- native filename-overlap + GUID profile-resolution regressions: PASS
- native context fallback regression: PASS
- payload JavaScript syntax: PASS
- real v1.9.2 patched EXE/ASAR -> v1.9.3: PASS
- `-check`: installed
- actual production ASAR contains v1.9.3 live bootstrap, GUID/filename resolution, context fallback, and pre-desktop script order: PASS
- restore-latest returns exact v1.9.2 EXE/ASAR: PASS
- restore -> repatch converges to identical v1.9.3 EXE/ASAR: PASS
- ASAR full integrity records: 244/244 PASS
- ASAR block integrity records: 244/244 PASS
- current ASAR header embedded exactly once in CurseForge.exe: PASS
- final Patcher ZIP integrity: PASS
- source inside final Patcher ZIP rebuilds Windows patcher byte-identically with Go 1.23.2 / `-trimpath -ldflags="-s -w"`: PASS
- fresh exact v1.9.2 output -> v1.9.3 from freshly extracted source: PASS
- standalone source archive equals source shipped inside Patcher ZIP: PASS
- Drive-downloaded patcher/source byte-equal to frozen release: PASS
- Drive-downloaded DirectPatch chunks reassemble byte-for-byte to frozen DirectPatch ZIP: PASS
- no watchdog / Scheduled Task creation / filesystem watcher / recurring polling / auto-repatch: PASS

## Canonical release hashes

- Patcher ZIP: `fa65d554a78ed3f38211637f83c04eb6adc46b346f6c2d699b0db351b6a2c8d4`
- DirectPatch ZIP: `d070ab0955d038f597b1074b3b8f3f903c69f22862a96ed630d3aeccc4166c4e`
- Source archive: `159d580600f28d26f1a2675ea6eaab531bd780249a7c52e515f18ebdbe29dd3a`
- Windows patcher EXE: `3f7a355373707823504aa88a3df7fc8b973dd82e888d64c7bda3bb7a770359cd`
- Patched CurseForge.exe: `01c1b45b5199ca588043313e9efde07350edd3fb81cbea2699da57a3aa5d29a2`
- Patched app.asar: `629a9095e0c512f1bda24b998a2c404e424ec05bd3f489ac2ea05f60238b8101`
- ASAR header: `7cb03d1d39b8008e4ca5dfd2156296363a7e8448287ae6fabd1e6884d6531d48`

## Google Drive publication

Canonical folder: `1HcVsT6o1Za0yFrfk_TAyGxC6YHiLT7S5`

- Patcher: `1Nvhhs8hek3wbJyYMBecf728MtWDYrhvL`
- Source: `1nVVUcqEL5k9jLJ3JasyAugXbW5gmdIeB`
- Final checkpoint: `1CgucOWqeQOuG1RiEr3IVy82sh7h-1wzR`
- Drive readback receipt: `1GuJt-gQici2WMvriV7nC3m63Od-sgOSe`
- Fresh extraction gate: `1yhKuHC_TN8K-9wdWaNkcKtoT7hzD_sQY`
- Release checksums: `1oxN4nktjB3r8swQxC4gnMAzQ-y1z68vq`
- DirectPatch part checksums: `16APe0gx8zDJDls5AwAHOsN7Wl8E3jM9-`
- DirectPatch multipart README: `1TS6lNjBGxLR2YD5Sjw9LIltlDLj_4d0n`
- Reassemble command: `1ZyaTt45Vv5dmnh7EIyCjfEMuoqkWhKyf`
- DirectPatch part000: `1xukZlf9sNBRkfVuZBsl6qcucQrd3Wt3o`
- DirectPatch part001: `10slIyVHzUeHB7AEwdqcMXx_3iHsaiIuh`
- DirectPatch part002: `1igUY0lXWDsuFHpFUJPPJaR7_YcgLBWW0`

The Drive copies of the patcher and source were downloaded and byte-compared to the frozen release. The three Drive DirectPatch parts were downloaded, reassembled to exact SHA-256 `d070ab0955d038f597b1074b3b8f3f903c69f22862a96ed630d3aeccc4166c4e`, ZIP-tested, and byte-compared to the frozen complete DirectPatch.

## Exact next action

Run the v1.9.3 Patcher over the user's currently-installed v1.9.2 CurseForge 1.319.0.38738 installation. Open the affected profile's Content page. The integration no longer needs the route detector to bootstrap. An ordinary CurseForge right-click menu should gain **Open on CurseForge** immediately where a native project URL exists, and the filesystem scan should then refetch the native list so filesystem-owned rows/providers appear. For the original unchanged reproducer, the mod count target is 631 rather than 585.
