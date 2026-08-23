# Creeperella: Bloom & Boom 1.1.0 — Verified Release

- Minecraft: 1.20.1
- Forge: 47.4.23
- Java: 17
- Mod ID: `creeperella`
- Verification workflow run: `32662363893`
- Verification head: `80a2f1691f399370287b209d4b24f0fa361804a5`

## Runtime verification

The production-remapped JAR was built with ForgeGradle 7 + Forge Renamer 1.1.2 and launched on a real Forge 1.20.1-47.4.23 dedicated server. The server reached ready state (`Done (28.059s)!`) with Creeperella loaded.

Server-tested production code JAR SHA-256:
`6e33a33396dd17fa849bf5c18e1f742f91bf616f871f44ed65af0bd1a6f4b90e`

## Final release package

Final release JAR SHA-256:
`0cad30ea822b11313f332a303ee9667c12912e8234c3b27228b459d573498a40`

Source ZIP SHA-256:
`abd425fa9fdaf3a6ea6ed09e623288b72bf6a4d71446a0e6d2d52d5270ecaad2`

The final release was made from the exact server-tested JAR by adding only the complete user-authorized client asset set (7 PNG resources) plus asset/license documentation. All 19 `.class` entries were compared byte-for-byte and are identical to the server-tested production JAR. Final JAR ZIP integrity passed.

## Google Drive checkpoint

Folder: `Creeperella - Bloom & Boom`
Folder ID: `1Rz2CyGTW0olVMO4o1_fSwcOnNEL9k3jc`

- Final JAR: `1DYx8rmsyPjlt-jEjjoFjBnph1l0uCdcl`
- Source ZIP: `1HmjfKMcOQOftrMBhx90o5JzYwp3lfFxd`
- SHA-256 manifest: `1tSXeUtCfaiyz5QjS_02fFbFPUBzNSevt`
- Final verification report: `1jaQS4WiFMMytwsCoLb8mfkvBPfCmGOpH`
- Creeper pack research: `10aFeBiZCUL90LHjuHlNB6nzWWcCWjY08`

The final JAR and source ZIP were downloaded back from Drive and their SHA-256 values matched the local release byte-for-byte.

## Remaining acceptance gate

A graphical Minecraft client was not available in the build environment, so visual/in-game model presentation still needs the normal player-side visual QA pass. Runtime registration, production remapping, dedicated-server loading, packaging integrity, and resource structure are verified.
