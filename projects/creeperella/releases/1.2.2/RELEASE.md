# Creeperella: Bloom & Boom 1.2.2 — Cherry Remake 3.0

Released/checkpointed: 2026-08-24 (America/Denver)
Target: Minecraft 1.20.1 / Forge 47.4.23 / Java 17

## Change

Cherry Creeper and Blossom Creeper now use the user-supplied `Cherry_Creeper_remake(3.0).zip` topology, credited in the supplied CEM to Poolb / Kotisimo. Cherry uses the supplied 64x64 texture and emissive pixels. Blossom uses the same improved topology with a distinct lilac/sakura Creeperella palette and matching emissive. Native Forge model code carries body/head/leg motion, foliage/hair sway and three-frame face blinking. The retired pre-3.0 Cherry/Blossom geometry is absent from the active source/JAR and is retained only in the Google Drive legacy backup.

All five existing spawn-egg color pairs are unchanged. Cherry remains `0xE7A0AF / 0x6C7D4C`.

## Verification

- Verification branch: `build/creeperella-1.2.2`
- Draft audit PR: #19
- Verified head: `e3a5b15869e93dbf60cf10dc636eee3605870891`
- GitHub Actions run: `32755567631`
- Job: `97522183201`
- Java 17 exact-source reconstruction/hash gate: PASS
- ForgeGradle production compile/remap: PASS
- Real Forge 47.4.23 dedicated-server startup: PASS (`Done (26.717s)!`)
- Production-remapped server-tested JAR SHA-256: `7a79188e41f15cfd9ebf57f6b565b6a4a7b41c50ec497a2b977d7e4448edf865`
- Final release: 22/22 compiled classes byte-identical to the server-tested production JAR.
- Final JAR archive integrity: PASS; Java class major 61.
- Static source: 16 Java / 38 valid JSON / 9 PNG.
- Deterministic source-model visual QA: PASS for Female, Bunny, Bee, Cherry Remake 3.0, Blossom Remake 3.0.
- Live graphical Minecraft-client rendering is not claimed by this receipt.

## Final artifacts

- JAR: `Creeperella-Bloom-and-Boom-1.2.2-Forge-1.20.1.jar`
  - SHA-256: `7aa84f44c218e485af4f4c2d8433d92e3ec9eec59c72a940a8e024c203ebca69`
  - size: 120887 bytes
  - Drive ID: `1d6NzgK5MSgDqjtGQULC94yr1O-p6ghDw`
  - Drive round-trip SHA-256: MATCH
- Full source: `Creeperella-Bloom-and-Boom-1.2.2-Forge-1.20.1-source.zip`
  - SHA-256: `d3104919ea40e6af856ca3f3fd1b316a636c5edeb84a7319ce38979387615c7e`
  - size: 118876 bytes
  - Drive ID: `1OMXvRvEWcKaylnhyCp0Bsrsgzc9WpA8N`
  - Drive round-trip SHA-256: MATCH
- Final verification: Drive ID `1yJKZrJCSlJiWzYA-1l334EwIpRGYdLAQ`
- Checksums: Drive ID `1GYfVycjL4bOiBkexdeNBEIrJLtT43o-J`
- Mob + spawn-egg showcase: Drive ID `1_X8V9sG5adoNX0-wIiZp0O7zK-ZeO49Q`
- Legacy pre-3.0 Cherry/Blossom backup: Drive ID `1_ueggcGFzf23LEFrwgOKHmRVH_ZKED37`, SHA-256 `af6ef503b6267730499b79a5dc6b2667387b295db66d100246b3dbc92bcaa64c`
- Original supplied Remake 3.0 source archive: Drive ID `1k0gmGDe9DK7tNH4D2YA8ffaBAkb9TnYG`, SHA-256 `7904385b5d36692d738db915203f3fb0e507bd2d47d3a39ab9be39856426368d`
- Model QA Renderer 1.1.0: Drive ID `1Guq9eQDTsG5i1s5zD0V_sIDFOwQ_6Xfw`, SHA-256 `f9a1ddf1563b363179308816e8a9abb043a9c6d08d561ba370a0b48b79fcb8d2`

Canonical Google Drive project folder: `Creeperella - Bloom & Boom` (`1Rz2CyGTW0olVMO4o1_fSwcOnNEL9k3jc`).

## Continuation rule

Continue from the full 1.2.2 Drive source archive plus this GitHub verification state. Do not reintroduce the retired pre-3.0 Cherry/Blossom geometry. Preserve the five current spawn-egg color pairs unless explicitly changed by the user. The next client-visual gate should exercise actual Minecraft rendering of the 3.0 model, blink animation, emissive layer and charged state while retaining deterministic source-model QA as the fast regression gate.
