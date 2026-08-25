# Creeperella: Bloom & Boom 1.4.5

Target: Minecraft 1.20.1 / Forge 47.4.23 / Java 17.

## Cherry TNT correction
- Runtime Cherry TNT now uses vanilla `minecraft:block/cube_bottom_top` geometry instead of the source resource pack's format-specific Blockbench UV adapter.
- Exact 64x64 source Cherry TNT atlas remains preserved byte-for-byte in provenance.
- Deterministic generator extracts exact authored 16x16 side/top/bottom pixels for the vanilla cube model.
- Dedicated Cherry TNT block/item/primed entity remains intact with redstone, flint-and-steel, fire charge, flaming projectile, chain reaction, shortened chained fuse, swell/flash and normal TNT explosion behavior.
- Vanilla `minecraft:tnt` remains untouched.

## Standalone source-pack rule
Author-intended companion content must be ported as standalone namespaced content rather than discarded simply because the original pack globally replaced vanilla. Cherry Gunpowder, Cherry TNT, Cherry Creeper Head, Creebet painting and source EN/RU identities remain standalone.

## QA / parity
- 45/45 supplied source files exact and accounted for.
- 0 source particle assets, 0 source sound assets.
- 84/84 runtime JSON resources parse.
- Pie animation parity: 712 sampled evaluations.
- Cherry animation parity: 235 sampled evaluations.
- Cat geometry: 39/39 base cubes + 14/14 charged cubes; no invented tail yaw/roll.
- 24/24 six-variant 3D spawn-egg states resolve.
- Deterministic QA renderer updated to resolve vanilla `cube_bottom_top` / `cube_all` parent templates.
- No image generation is used for deterministic project QA.

## Production boundary
Source/model/data/animation/visual gates are green. Do not label a 1.4.5 JAR production-verified until Java 17 ForgeGradle remap/build and a real Forge 47.4.23 dedicated-server startup pass.
