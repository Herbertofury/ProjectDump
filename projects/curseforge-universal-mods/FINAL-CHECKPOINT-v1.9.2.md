# CurseForge Universal Mods v1.9.2 final checkpoint

Date: 2026-09-04
Target: CurseForge 1.319.0.38738
Supersedes: v1.9.1

## Objective closed

v1.9.2 makes the real Minecraft profile filesystem authoritative rather than allowing CurseForge InstalledProjects to decide which installed files exist.

Acceptance reproducer: **631 real JAR/disabled-JAR files on disk + 585 CurseForge native rows -> 631 unique native rows**. All **46** missing CurseForge-owned disk files are recovered with no duplicate filenames.

## Provider / provenance model

- CurseForge ownership, Modrinth identity, Local status, and Repaired provenance are separate concepts.
- A CurseForge-primary file may retain exact Modrinth SHA-512 identity at the same time.
- Repaired is an installed-file attribute, not a replacement project identity.
- Installed-via provider provenance is trusted only while its SHA-512 still matches the installed bytes.
- Changed bytes invalidate stale provenance; an exact-hash rename may safely recover it.
- Negative Modrinth misses are cached so unknown Local files are not re-queried on every passive scan.

## Native CurseForge UX

Provider/version actions are integrated into CurseForge's own native per-mod context menu rows. No custom popup, right-click DOM observer, or MutationObserver badge decorator is used.

Supported actions include provider links, CurseForge reinstall when the native capability permits it, Modrinth reinstall/version switch/changelog, explicit update-provider choice for dual-provider rows, and installed-file reveal for Local content. CurseForge's native Update/Update All flow remains the single bulk-update surface.

## Verification

- Go tests: PASS
- QOL JavaScript suite: PASS
- 631/585 filesystem-first regression: PASS
- 46 missing CurseForge-owned rows recovered: PASS
- dual-provider identity regression: PASS
- hash-bound provider provenance regression: PASS
- native provider/version context-menu regression: PASS
- production injected JS syntax: PASS
- real v1.9.1 DirectPatch -> v1.9.2: PASS
- second `-check`: installed
- restore-latest -> exact v1.9.1 EXE/ASAR: PASS
- restore -> repatch convergence to exact v1.9.2 bytes: PASS
- packed ASAR integrity: 244/244 full SHA-256 + all block hashes PASS
- ASAR header embedded exactly once in patched Windows EXE: PASS
- final Patcher ZIP integrity: PASS
- source inside final Patcher ZIP rebuilt Windows patcher byte-identically with Go 1.23.2 / `-trimpath -ldflags="-s -w"`: PASS
- standalone source archive equals source shipped inside Patcher ZIP: PASS
- final DirectPatch ZIP integrity/extraction: PASS
- Drive-downloaded Patcher/source byte-compare to frozen local release: PASS
- Drive-downloaded DirectPatch chunks reassemble byte-for-byte to final DirectPatch ZIP: PASS
- manual only: no watchdog, Scheduled Task, filesystem watcher, polling loop, or auto-repatch: PASS

## Canonical release hashes

- Patcher ZIP SHA-256: `bb681e4d42ce2e1e05cf7769f8439ce082e1a110b276e98e35e664298dfe57f3`
- DirectPatch ZIP SHA-256: `f339ad857f79fbdb02468ca2c05656ee133173ff52dbde191eaa7cfd8f6c38db`
- Source archive SHA-256: `b93c913571e776330c13524dce5fa2360de8a59b642eb431bbc6a417f544d709`
- Windows patcher EXE SHA-256: `c817f61a42d2bfaf9ca7436acf9327b8f49c890eac3c2ea00f6f3e83221169d5`
- Patched CurseForge.exe SHA-256: `693a9c42220a340e630d973cbf05591a944f31857470d5d6e27bf8e58fe191b6`
- Patched app.asar SHA-256: `248e6fe8375d1fa9cb895b649b68cf860aa7eae453c974d592f2e793d63100dd`
- ASAR header SHA-256: `f6b8d6088a01653445e9e78324e25e87c9d7aa9752e653fa455db0c93a45ccc9`

## Drive publication

Canonical folder: `1HcVsT6o1Za0yFrfk_TAyGxC6YHiLT7S5`

- Patcher: `1yU0Tnw8ZAPZTJTo74p-UpRa_MmKf00UX`
- Source: `1PxyiVTmjD0K8RdozVqLBWRG0dJLP4mXw`
- Final checkpoint: `1E86BuWGtGD-ulpF7vHpyq84nEHvv5JHK`
- Fresh extraction gate: `11EY8vP--RrCmgOS9O9q4raqCkbUxJTE1`
- Release checksums: `18s9InAKCxfKgDdH-4MGxzE1UsWa57la-`
- Drive readback receipt: `1Pf3qqoRRt8UzQS784VVqvCDAFXYdZoM9`
- DirectPatch part checksums: `1fFy2rIJctbukowe_ZHMKVp28ExI5moAI`
- DirectPatch multipart README: `1tEI6cuNIkCv1S84lZtx5RqGKwWNzUn34`
- Reassemble command: `1fPB5s5_UdabPQBJIvEueu4zcvC93uiIN`
- DirectPatch part000: `1ZZ_YzV0XCQ83Zb9tr9QAqpCP5cKdpsMi`
- DirectPatch part001: `1a-n02JtC77xYdBEcRjoRr6xJJCOEaeU8`
- DirectPatch part002: `1J-d-FHjjxnBI_9lg16EJsFoRHkUnP_Gx`

The redundant 110.8 MB one-file DirectPatch upload was rejected by the Drive create-only route. No release bytes were changed or rebuilt. The three-part Drive transport is canonical and was downloaded, reassembled, hash-verified, ZIP-tested, and byte-compared to the frozen complete DirectPatch.

## Exact next action

Patch the user's real Windows CurseForge 1.319.0.38738 installation with the v1.9.2 Patcher, reopen the affected profile, use CurseForge's native Refresh once if it was already open before patching, and verify the live profile now surfaces all filesystem entries (expected 631 for the reproducer) with correct CurseForge / Modrinth / Local / Repaired badges and native provider/version actions. Preserve these Drive IDs and hashes as the v1.9.2 baseline for any live-Windows delta.
