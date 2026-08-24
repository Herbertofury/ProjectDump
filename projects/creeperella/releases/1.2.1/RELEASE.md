# Creeperella: Bloom & Boom 1.2.1 — Visual QA Hotfix

Target: Minecraft 1.20.1 / Forge 47.4.23 / Java 17

## Why 1.2.1 exists

The new deterministic model QA gate found that the prior `blossom_creeper.png` had a different PNG file hash but identical decoded pixels to `cherry_creeper.png`. Because the renderer tint was neutral, Cherry and Blossom were visually indistinguishable.

1.2.1 gives Blossom a distinct pale sakura/lilac palette with spring-green foliage accents while preserving the authorized Cherry-derived geometry and art lineage.

## Regression boundary

No gameplay Java code changed from the server-verified 1.2.0 companion release.

- 20/20 compiled `.class` files are byte-identical to 1.2.0.
- Exactly two JAR entries differ: `META-INF/MANIFEST.MF` (version 1.2.1) and `assets/creeperella/textures/entity/blossom_creeper.png`.
- JAR ZIP integrity: PASS.
- Full source ZIP integrity: PASS.
- Deterministic model renders completed for Female, Bunny, Bee, Cherry, and Blossom.

## Artifacts

- JAR: `Creeperella-Bloom-and-Boom-1.2.1-Forge-1.20.1.jar`
  - SHA-256: `3e8efbbb69b1f4a4f560617e0173052da4cb1765cd06b3ad6254c86cb533ae02`
  - Drive ID: `1-vHUoLu6SNj2SEk3dyLB1xPa8Q-Ly9RB`
- Full source: `Creeperella-Bloom-and-Boom-1.2.1-Forge-1.20.1-source.zip`
  - SHA-256: `a08c41d09f9a72d6d82dc17b2cb7b4a9aa29f6d01da0c3cee9112551accb803a`
  - Drive ID: `17lv2DTbYjIQREjO-uvA_J1FmE-uNgwss`
- Visual QA folder: Drive ID `1nabqWxRuMO_Cm3rMCbE1iF0cFZ2VVTHY`
- All-model showcase: Drive ID `17uGfSFmdhSWEFENeRj9v7ioiO_5vQJsF`

## Reusable dev tooling

Created `Minecraft Model QA Renderer 1.0.0` as a reusable fast visual gate for CEM/JEM entity geometry and texture atlases.

- Dev Kit `AI Dev Tools` folder: Drive ID `1Has9vZPbe2OoquK55OYiGvuoxtJ1rvtl`
- Tool ZIP: Drive ID `1EGj9c69eJzDSx97fsqxJq4bAtUKYK-cQ`
- Standing Minecraft tooling policy: Drive ID `1RknUguPU2Bhsx9s6TPjGci_rZsDix781`

The global ProjectDump contract now also records the standing rule to ask for additional tooling when it would materially improve project correctness/speed/fidelity/verification, instead of silently accepting a weaker workflow.
