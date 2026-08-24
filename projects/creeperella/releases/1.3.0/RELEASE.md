# Creeperella: Bloom & Boom 1.3.0 — Animated 3D Character Eggs

Released/checkpointed: 2026-08-24 (America/Denver)
Target: Minecraft 1.20.1 / Forge 47.4.23 / Java 17

## Change

Creeperella 1.3.0 adds an optional, client-side animated 3D presentation for all five spawn eggs while preserving the exact pack-authored 2D sprites introduced in 1.2.3 as the fallback and source-of-truth artwork.

Client config (`creeperella-client.toml`):
- `spawnEggs.use3DSpawnEggs=true`
- `spawnEggs.animate3DSpawnEggs=true`
- `spawnEggs.spawnEggAnimationSpeed=1.0` (range 0.25–4.0)

When 3D mode is disabled, the eggs render as the exact Pie/Cherry 2D sprites. When animation is disabled, the 3D character eggs remain 3D but idle/static.

Per-variant 3D identity:
- Female: Creeperella face, black fringe/crown tuft, twin ponytails, pink hair ties.
- Bunny: tall ears with pink inner ears, side puffs/mini ponytails, fluffy tail.
- Bee: honey body, burgundy side hair puffs, wings, antennae, bee belt.
- Cherry: pink Remake 3.0-family styling, bangs, high side ponytail, green sprout/leaves.
- Blossom: lilac/sakura shell, twin sakura ponytail puffs, flower crown/petals, green leaf accent.

The item property system exposes staggered idle/sway-left/sway-right/blink states so the five eggs do not animate in lockstep.

## Reference archive

User-supplied `Rethoughted Spawn Eggs.zip` v1.4 by CatFromNet was used as a visual/geometry reference for the concept of dimensional spawn eggs. No reference model JSON or texture bytes are redistributed in Creeperella.

- SHA-256: `9fa5737f85580895c155dbcb28f0916ab6df642253f9ed238e5bb94ab8cc2ebb`
- Drive Source Assets ID: `1IJD8xBAzXaRFsxaDK6A8k_KHSFDvERJ0`

## Verification

GitHub repository: `Herbertofury/ProjectDump`

- Verification branch: `build/creeperella-1.3.0-ci`
- Verification PR: #23
- Verified head: `bed080853ca177a732b7f15dd79e0181686010d2`
- GitHub Actions workflow: `Creeperella 1.3.0 Verified Build`
- Workflow run: `32766482885`
- Job: `97556980844`
- Artifact ID: `9534781132`
- Exact verified-lineage reconstruction and 1.3.0 patch hash gate: PASS
- Java 17 ForgeGradle production compile/remap: PASS
- Real Forge 47.4.23 dedicated-server startup: PASS
- Observed server ready line: `Done (31.332s)! For help, type "help"`
- Production-remapped CI JAR SHA-256: `ce7dbaf40c15ea9e41ceed44a2942cd2c52a998cb17581bf3f08de4719193231`
- Final release contains 23 compiled classes; **23/23 are byte-identical to the production-remapped JAR that passed the real Forge server gate.**

Static/resource verification:
- 17 Java source files
- 58 JSON resources, all parse successfully
- 20 authored 3D item model states (5 variants × idle/sway-left/sway-right/blink)
- 25 authored 3D material textures
- Exact 1.2.3 Pie/Cherry flat spawn-egg sprite hashes preserved 5/5
- All model and texture references resolve
- 3D cuboid/rotation bounds audit: PASS
- Generator determinism: PASS
- Reference-pack assets absent from active mod payload

## Final artifacts

- JAR: `Creeperella-Bloom-and-Boom-1.3.0-Forge-1.20.1.jar`
  - SHA-256: `d04f34a10e8f27d6ad44f21b31de479533665b618a9491f3ef3edc6e0aa84a67`
  - size: 159034 bytes
  - Drive ID: `14QCQJ0QaBzVElDkz1FYk7hA-G2XNsviS`
  - Drive full-byte round-trip SHA-256: MATCH
- Full source: `Creeperella-Bloom-and-Boom-1.3.0-Forge-1.20.1-source.zip`
  - SHA-256: `ed19a701a17e14d7f8a08153e62bdfb1d585b2001b563592eb5e3b1a24ffcea9`
  - size: 177932 bytes
  - Drive ID: `1Z8oB7DEhWgKlj70WslHVa52O9zL3crhv`
  - Drive full-byte round-trip SHA-256: MATCH
- Final verification: Drive ID `1xZfy3sFyUv8VRX644vlAKutw83fyBZNu`
- Checksums: Drive ID `1YlPENxXrJag1QeP4sbAFK_SPRiiJB_KR`
- Release receipt: Drive ID `1CT3wfxu63lXn6tDsdlVH2OQ8tCWiSqCr`
- 2D-vs-3D deterministic showcase:
  - SHA-256: `6b04720943008bee6650cadef35b1724f2941de6710c710c6331ac0a18ce051a`
  - size: 46867 bytes
  - Drive ID: `1Ocm5h2LvxhEPWpKsCxZ7nCTSqHKhbh2O`
- Animated deterministic 3D preview GIF:
  - SHA-256: `039f53c0c81ee580935ca582aef8dd649b85d26eb203399ce57db68be7f7ad3c`
  - size: 496848 bytes
  - Drive ID: `1IiMoYbr-6IWvxWmN5whIpFwSu7k7qlDS`
- Minecraft Model QA Renderer 1.3.0:
  - SHA-256: `15e1efd2725443bcda56031c809b5eb22985f7bf540ad51fda61390cc46ddd34`
  - size: 34210 bytes
  - Drive ID: `1aPSt4d1u8htoDXdjzLn7Y_0j_ubj8HsK`

Canonical Drive project folder: `Creeperella - Bloom & Boom` (`1Rz2CyGTW0olVMO4o1_fSwcOnNEL9k3jc`).

## Visual-proof boundary

No image-generation model was used. The showcase and GIF are deterministic renders of the authored Minecraft item-model JSON and textures. A live graphical Minecraft-client capture was not executed in this environment, so this release does not claim an in-game client screenshot; compile/remap, real Forge server load, package identity, and deterministic item-model visual QA are the verified surfaces.

## Continuation rule

Continue from the full 1.3.0 Drive source archive plus this receipt. Do not replace the exact pack-authored 2D fallback eggs with generic color-pair eggs. Preserve the Remake 3.0 Cherry/Blossom mob geometry and keep the 3D spawn-egg presentation client-configurable and cosmetic-only.
