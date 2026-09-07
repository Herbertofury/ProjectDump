# Minecraft Dev Kit Handoff

## Restored objective

Continue upgrading the Minecraft Dev Kit until authorized images/GIFs can drive premium MCModels-level native Minecraft assets with measurable observable parity: mobs/bosses, weapons, armor/cosmetics, furniture/decor, textures, animation, VFX/SFX and gameplay presentation.

## Canonical checkpoint

- Drive active package: `skill.zip`
- Drive file ID: `1gvOuxqHGgP8isI1sC8izYeKhBX0TIxpi`
- Size: `301131` bytes
- SHA-256: `bfb9d8d21152197e9596b16e3954a9e3fdf4966caa6bf4b470f0e6ea9c4033e2`
- Drive checksum file ID: `1zz64UKIM-OzW3yseTlTT4mF1W4SKKimt`
- Drive folder ID: `1qAVqAzWUvZcbZ7EpHRWsrAQjOd62630J`
- GitHub continuity mirror: `Herbertofury/ProjectDump/tools/minecraft-dev-kit`

## Proven reconstruction stack

- reference media staging: hashes, timing, masks, edges, palettes, bboxes/centroids;
- still/GIF parity: silhouette IoU, silhouette-edge F1, internal-edge F1, SSIM, CIEDE2000 and DTW timing;
- multi-view cuboid/camera inverse fitting;
- zero-start visual hull from calibrated silhouettes;
- constant-camera turntable GIF calibration;
- semantic scaffolds for sword/staff/bow/armor/head-cosmetic/furniture/decor;
- evidence-constrained automatic scaffold refinement that refuses hidden-axis drift;
- internal geometry-edge fitting for details contained inside the outer silhouette;
- optical-flow motion partitions;
- GIF inverse fitting of bone rotation and translation channels;
- visible box-UV texture back-projection with coverage/confidence;
- conservative preview de-lighting/material draft;
- residual maps;
- rights-gated one-command reconstruction contract;
- existing premium 16-stage mob/boss production and authoring lane remains green.

## Verified release evidence

Packaged-copy results at the checkpoint:

- multi-view geometry fit IoU: `1.000000`;
- independent camera fit IoU: `0.998999`;
- GIF rotation pose fit IoU: `0.997519`;
- turntable GIF -> visual hull IoU: `0.964317`;
- internal geometry edge F1: `1.000000`;
- GIF translation fit IoU: `1.000000`;
- automatic front-view sword refinement IoU: `0.992023`, observable axes `[X,Y]` only;
- visible texture round-trip MAE on covered texels: `0.0`;
- packaged premium six-boss pipeline: all 16 jobs PASS;
- deliberately invalid event-marker fixture: correctly rejected.

## Rights/evidence invariant

Public marketplace previews are quality benchmark evidence, not automatic reproduction permission. Exact reconstruction of third-party commercial art requires user ownership/authorization. `Exact` is scoped to observable supplied views/times; hidden surfaces, unseen texels, original audio and server-only logic remain inferred/unknown until evidence supplies them. Native Minecraft proof is separate.

## No-repeat history

Do not redo already-green registry research, public Nazgul benchmark discovery, packaged inverse suites or premium six-boss suite unless a later mutation invalidates them. Do not dump Dev Kit state into `Minecraft-Mod-Vault`. Do not replace native project preview/render/model work with generated imagery.

## Exact next action

1. Add context-fit reconstruction:
   - held weapon/item transforms relative to player hand;
   - armor/cosmetic transforms against default + slim player-rig oracles;
   - furniture placement/seat/interaction anchor fitting.
2. Broaden semantic weapon scaffolds: dagger, greatsword, axe, mace/hammer, spear/polearm, scythe, shield, crossbow.
3. Add pack-level consistency audit for 16x material language, scale bands, motif/palette reuse, UV density, role/silhouette distinction and animation timing families.
4. Run only tests invalidated by those changes, then package/roundtrip/audit and promote the next Drive + GitHub checkpoint.
