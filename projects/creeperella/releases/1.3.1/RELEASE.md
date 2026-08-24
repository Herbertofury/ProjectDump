# Creeperella: Bloom & Boom 1.3.1 — 3D Egg-Head Rework

Released/checkpointed: 2026-08-24 (America/Denver)
Target: Minecraft 1.20.1 / Forge 47.4.23 / Java 17

## Change

The optional 3D spawn eggs were rebuilt after the 1.3.0 mini-character/statue look was rejected. 1.3.1 keeps the exact pack-authored 2D Pie/Cherry egg PNGs byte-for-byte and uses those exact pixels as the visible surface of rounded convex 3D egg-heads. There is no separate torso/body. Character identity is limited to compact head details: Female side ponytail/hair lobes, Bunny ears, Bee antennae/wing relief, Cherry high-side ponytail plus leaf/stem, and Blossom sakura puffs/crown plus leaf.

Animation is still client-side/configurable but moves the egg-head coherently with subtle whole-item sway/bob/squish. The rejected generic 1.3.0 `textures/item/3d/*` material tiles are absent. `Rethoughted Spawn Eggs.zip` remains reference-only; no reference model or texture bytes are redistributed.

## Exact 2D non-regression hashes

- Female `475a5fcfa6138dc00f58f77bbe99813043fbcdee97eda632655f535166251187`
- Bunny `81c8c6db0ff013a4ad459ab7856486068e2977922f423ea769f27d779972e23e`
- Bee `64fe7c8a410a4317f584765afcb98f4397f367a0f0bec6dbeaf0865adf84163d`
- Cherry `391c89f344f5b286539e696cbff107e0247afbd9e6adabfb1d2a60e26f2ba60f`
- Blossom `391c89f344f5b286539e696cbff107e0247afbd9e6adabfb1d2a60e26f2ba60f`

## Verification

- Verification branch: `build/creeperella-1.3.1-ci`
- Verification PR: #24
- Verified head: `85b8fa501d606c44a0d0d772c3847a3953468373`
- GitHub Actions run: `32771910054`
- Job: `97573941921`
- Artifact: `9536667796`
- Java 17 ForgeGradle production compile/remap: PASS
- Real Forge 47.4.23 dedicated-server startup: PASS
- Observed ready line: `Done (28.657s)! For help, type "help"`
- Production-remapped CI JAR SHA-256: `ef0bad82cb81a4c44b189026f70b97c18c3e92f44cc8a7ab4423cfadddb2876c`
- Final release class identity: **23/23 class files byte-identical** to the server-tested production-remapped JAR
- 58 Creeperella JSON resources parse successfully
- 20/20 3D model states resolve
- 5/5 3D idle models use the exact fallback egg PNG as their egg surface
- 15/15 animation child models inherit the egg-head geometry
- 74/74 canonical source resources byte-identical to final JAR entries
- 5/5 2D fallback sprites byte-identical to 1.3.0 baseline
- generator determinism: PASS
- no image generation used

## Final Drive artifacts

Canonical Drive folder: `Creeperella - Bloom & Boom` (`1Rz2CyGTW0olVMO4o1_fSwcOnNEL9k3jc`).

- JAR `Creeperella-Bloom-and-Boom-1.3.1-Forge-1.20.1.jar`
  - SHA-256 `61a9b3bdc54c13ee86830f0222b1dbbe5bdede52eceb54848d287a7bd7b848b1`
  - size 153283 bytes
  - Drive ID `14sUW_YCtj5Qs1TUkgu2VHA0gW-3xqR2l`
  - full-byte Drive round-trip: MATCH
- Full source `Creeperella-Bloom-and-Boom-1.3.1-Forge-1.20.1-source.zip`
  - SHA-256 `c706019f9f411c221833fc780d4edb6955265d3b506cc19bc5491fb87995b33b`
  - size 181442 bytes
  - Drive ID `1dPjEQUeVGATiMCqQMaP2vF6O9WvKuJUo`
  - full-byte Drive round-trip: MATCH
- Static preview `Creeperella-1.3.1-2D-vs-3D-Egg-Heads.png`
  - SHA-256 `9fbc5a3f9624e27536dc88ed787e2e9127302122458ae96181489ec4e86fca7b`
  - Drive ID `10NK59N4NrTEHno9lEckLdAhOTCUOOEEa`
- Animated preview `Creeperella-1.3.1-Animated-3D-Egg-Heads.gif`
  - SHA-256 `7175e682f8065fdba21c5782db54212d9f88bdb90703583a7de201619d9b1961`
  - Drive ID `1aV1WZH8mdT_49pzW3GQxajD0BdFENvxn`
- Verification `Creeperella-1.3.1-FINAL_VERIFICATION.md`
  - SHA-256 `fc66de61ce96bd785b75d755d42cdbb6ea49341859d573a1117502563046980c`
  - Drive ID `1BW5rWn5g3o2LQ8pO52267vBGOYD_f0-a`
- Checksums `Creeperella-Bloom-and-Boom-1.3.1-SHA256SUMS.txt`
  - Drive ID `1gZQ-sroGNiT6vpI_-8ZUosGCXUE2W1Yj`
- Release receipt `Creeperella-1.3.1-RELEASE-RECEIPT.md`
  - Drive ID `1UU7V-gYskpk4fPe46rsl_4voj1s4UFae`
- Minecraft Model QA Renderer 1.4.0
  - SHA-256 `57b39fafcd5924ce514f77579018aabe5b904c07b5b29e02aa9710769950bf54`
  - Drive ID `1OGZIAWyh6FMLrPjie5-1XBnTdX0hKAzQ`
  - full-byte Drive round-trip: MATCH

The earlier 1.3.1 WIP source/preview are superseded recoverable checkpoints, not the final release.

## Proof boundary

No image-generation model was used. The PNG/GIF previews are deterministic renders of the actual authored Minecraft item-model JSON and texture pixels. A live graphical Minecraft-client screenshot was not executed in this environment and is not claimed.

## Continuation rule

Continue from the full 1.3.1 Drive source archive plus this receipt. Preserve the exact 2D fallback bytes and keep the optional 3D mode visually equivalent to those supplied head/egg sprites with dimensional egg depth—not a mini mob, statue, torso, or generic recolored spawn egg.
