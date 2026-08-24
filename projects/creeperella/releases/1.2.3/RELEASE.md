# Creeperella: Bloom & Boom 1.2.3 — Pack-Accurate Spawn Eggs

Released/checkpointed: 2026-08-24 (America/Denver)
Target: Minecraft 1.20.1 / Forge 47.4.23 / Java 17

## User correction / source of truth

The prior 1.2.2 visual QA treated Creeperella spawn eggs as Forge color-pair renderings. The user corrected this: the supplied resource packs already contain custom 16x16 spawn-egg/item sprites and those exact pixels are the intended art.

Visual source mapping is now authoritative:

- Female — `(Pie's) Female Creeper 1.2.zip/assets/minecraft/textures/item/creeper_spawn_egg.png` — SHA-256 `475a5fcfa6138dc00f58f77bbe99813043fbcdee97eda632655f535166251187`
- Bunny — Pie `assets/minecraft/textures/item/bunny.png` — SHA-256 `81c8c6db0ff013a4ad459ab7856486068e2977922f423ea769f27d779972e23e`
- Bee — Pie `assets/minecraft/textures/item/bee.png` — SHA-256 `64fe7c8a410a4317f584765afcb98f4397f367a0f0bec6dbeaf0865adf84163d`
- Cherry — `Cherry Creeper 1.0.2.zip/assets/minecraft/textures/item/creeper_spawn_egg.png` — SHA-256 `391c89f344f5b286539e696cbff107e0247afbd9e6adabfb1d2a60e26f2ba60f`
- Blossom — shares that exact provided Cherry-family pink sprite because none of the supplied packs contains a distinct Blossom egg PNG.

`Cherry_Creeper_remake(3.0).zip` remains the active Cherry/Blossom mob-model source but contains no spawn-egg PNG. The pink Cherry egg therefore comes from Cherry Creeper 1.0.2.

## Implementation

All five Creeperella spawn-egg item models now use `minecraft:item/generated` with direct `layer0` references to bundled `creeperella:item/*_creeper_spawn_egg` PNGs. The old `minecraft:item/template_spawn_egg` item models are no longer used. Existing Forge color values remain fallback metadata only and are no longer the visual source-of-truth.

## Regression verification

- Resource-only delta from 1.2.2; Java source unchanged.
- 22/22 final `.class` entries are byte-identical to the 1.2.2 class set that passed Java 17 ForgeGradle production remap and real Forge 47.4.23 dedicated-server startup in Actions run `32755567631`, job `97522183201`.
- Five exact custom spawn-egg PNGs bundled; all 16x16 RGBA.
- Female/Bunny/Bee/Cherry packaged texture hashes match the supplied source pack bytes exactly; Blossom is byte-identical to the supplied Cherry egg by design.
- All 38 JSON resources parse.
- No active `assets/minecraft` vanilla-replacement payload.
- Final JAR ZIP integrity: PASS.
- No image-generation model used for visual QA; the 1.2.3 showcase uses deterministic mob renders plus nearest-neighbor scaling of the actual supplied egg PNG pixels.

## Final artifacts

- JAR: `Creeperella-Bloom-and-Boom-1.2.3-Forge-1.20.1.jar`
  - SHA-256 `46af66dd380ddf2c41c6fc2064712e8def6849ca5f5df7a33779e2fa78682941`
  - size 124806 bytes
  - Drive ID `1qQtvqbrrPyMDcYD9mEsSKtgeFx99HwiX`
  - Drive round-trip SHA-256: MATCH
- Full source: `Creeperella-Bloom-and-Boom-1.2.3-Forge-1.20.1-source.zip`
  - SHA-256 `543829657a4c2b3b74117ecf1d42dac8ebe46bfba3ec514e0fc94ff400cede3f`
  - size 148460 bytes
  - Drive ID `1jkQoxGBPRNJ5RkLcfygXnLl782DqSeAm`
  - Drive round-trip SHA-256: MATCH
- Corrected mob + actual pack egg showcase: Drive ID `1MnrOzDU-It1n3U6nAbWWGH4i4tR0nUqb`, SHA-256 `ad81dd2cb3142b347e0d74872fc57b117d828a1ac63015d608b6ddc04d70b250`
- Final verification: Drive ID `1jQFih7gtkYWa_fCUrdO5ntYbiXkoAAM0`
- Checksums: Drive ID `1W27aw_5mRQ4ifIQtTcR9R64fQP2GlI2V`
- Spawn egg source map: Drive ID `1gzqltJ1Eq0BkWRIbT4puuVdWzJA3a4Wd`
- Pie source pack: Drive ID `1bKiUT3M6DzErRGGhAy_rfWz3D6rHnCPZ`
- Cherry 1.0.2 source pack: Drive ID `1SrGxrqfEtA24NgBwbeu2JxafOsbGGYPF`
- Cherry Remake 3.0 source pack: Drive ID `1k0gmGDe9DK7tNH4D2YA8ffaBAkb9TnYG`
- Minecraft Model QA Renderer 1.2.0: Drive ID `1QX7iVj3MJBYLMrz70SJ3GY2qCm1k3AIb`, SHA-256 `fc80cbc487255b1550ffbcfce55ce1db593ab1947e2c0892db3fcc23414d1185`

Canonical Drive folder: `Creeperella - Bloom & Boom` (`1Rz2CyGTW0olVMO4o1_fSwcOnNEL9k3jc`).

## Continuation rule

Continue from the full 1.2.3 Drive source archive plus this receipt. Do not revert the spawn eggs to generic/tinted Forge egg mockups when source pack sprites exist. Preserve the Remake 3.0 Cherry/Blossom mob geometry and the external legacy backup policy.