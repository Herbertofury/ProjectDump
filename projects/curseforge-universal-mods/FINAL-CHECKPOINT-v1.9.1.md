# CurseForge Universal Mods v1.9.1 final checkpoint

Date: 2026-09-04
Target: CurseForge 1.319.0.38738
Supersedes: v1.9.0

## User reproducer fixed

Observed live UI before fix: **Source -> CurseForge (584), Modrinth (0), Local (0)** despite the profile containing Modrinth and manual/local content.

Root cause in v1.9.0:

1. CurseForge's native scanner can create/discover rows for files it did not install.
2. v1.9.0 used `!m.native` as a prerequisite for Modrinth hash identification.
3. It then effectively treated `mod.native` as CurseForge provider ownership during source assignment.
4. Therefore a file merely discovered by CurseForge was never allowed to become Modrinth or Local.

v1.9.1 fixes provider ownership:

- trusted CurseForge project/file provenance -> CurseForge
- otherwise exact Modrinth SHA-512 identity -> Modrinth
- otherwise -> Local
- repaired CurseForge provenance stays CurseForge even if cross-posted
- provider-classified files correct ambiguous native rows in place; no duplicate synthetic row
- Local files retain embedded metadata/icon even if CurseForge's scanner discovered them first

Regression reproducer: 584 source=CurseForge native rows + one exact Modrinth file + one unmatched Local file -> **584 total rows, 582 CurseForge / 1 Modrinth / 1 Local**.

## Canonical release

- Patcher ZIP SHA-256: `21fa2f08610bcac02eebcd48e64ffe49c079012dc995f7c52aeee432e1b6d3ee`
- DirectPatch ZIP SHA-256: `6301e7797c2b8666c9150cbd318070f8e9695b880f1c7553b1e51ce36585b092`
- Source archive SHA-256: `2bc9b033a2aef44415988e2b7063ff95dea559d5d895fcd0e72ea736bb8502fc`
- Windows patcher EXE SHA-256: `2264a31f397e78438b46c59c61ddda4dc4a9b662811f056168004dc5675d1ebc`
- Patched CurseForge.exe SHA-256: `5c78060ec08320c8f59ca5e4fa1519c105bdd5bdaf40f808707ff944ac91db62`
- Patched app.asar SHA-256: `f9ff3439e37029312b3c51152dcdeaf1c49a8d0dfe616be6216d9c9685424c6b`
- ASAR header SHA-256: `7fa889ee139d9875f7b7fc42def247f277a022bdf4eeb786a6bd187a5bb1ca3a`

## Verification

- Go tests: PASS
- QOL JavaScript suite: PASS
- exact 584/0/0 source regression: PASS
- native discovery vs provider ownership regression: PASS
- official native Linux upstream anchor audit: PASS
- exact native Linux production ASAR built/syntax checked: PASS
- native Linux runtime smoke: v1.9.1 bridge + Electron App Ready + SessionStarted; no v1.9.1 TypeError/ReferenceError/uncaught renderer failure before known sandbox DNS boundary
- v1.8 -> v1.9.1: PASS
- v1.9 -> v1.9.1: PASS
- both lineages converge byte-for-byte: PASS
- ASAR integrity: 244/244 full hashes + all block hashes PASS
- ASAR header embedded exactly once in patched Windows EXE: PASS
- final ZIP integrity: PASS
- fresh final Patcher ZIP extraction: PASS
- patcher rebuilt from source inside final ZIP byte-identical: PASS
- fresh untouched v1.9 target -> v1.9.1: PASS
- fresh `-check`: installed

## Drive publication

Canonical Drive folder: `1HcVsT6o1Za0yFrfk_TAyGxC6YHiLT7S5`

- Patcher: `1rbtWjCaryVPjiRJDhGKYY0Tx3r6xUH0M`
- Source: `1zqmLQcq5kRfRmhClhDiD8TpQlYysnIlW`
- Final checkpoint: `1EOx6wXK2RvVV6GnQlcLJm1-vsu9AelZH`
- Fresh gate: `14l-vdW91SkSnocfepKC-xPNM_v_Kx5c5`
- Release checksums: `13oSKbIMl2qu1iq7zouKmKNnrvPOFUdFA`
- Drive readback receipt: `1Nh_5d2ImngYnTRLc8xVYWZfroGCaw8WM`

DirectPatch was transported as three verified Drive-safe parts. The three Drive-downloaded chunks reassembled to exact SHA-256 `6301e7797c2b8666c9150cbd318070f8e9695b880f1c7553b1e51ce36585b092`, passed ZIP integrity, and byte-compared equal to the local release.

## Exact next action

Patch the real Windows CurseForge install with v1.9.1, reopen the affected Minecraft profile, and use CurseForge's native Refresh once. Verify Source counts are no longer pinned to 584/0/0 and that Modrinth/Local rows appear without duplicates. Preserve v1.9.1 as the baseline for any further live-Windows delta.
