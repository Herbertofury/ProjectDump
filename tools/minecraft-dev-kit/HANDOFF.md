# Minecraft Dev Kit Handoff

## Restored objective

Continue upgrading and exercising the Minecraft Dev Kit until **authorized** images/GIFs can drive premium MCModels-level native Minecraft assets with measurable observable parity across mobs/bosses, weapons, armor/cosmetics, furniture/decor, icon sheets, textures, animation, VFX/SFX and gameplay presentation.

## Canonical checkpoint

- Drive active package: `skill.zip`
- Drive package ID: `1vW63Bd3-RQ2a_FpDMjAqir-UCn4iIQVe`
- Size: `325067` bytes
- SHA-256: `9ba8410cf6d3df12fa51f682e519c1807a0b2f236e700a51757c490a357875a4`
- Drive checksum ID: `1or2QVw6qa8VEU5YMm5E0HUEhbaZFCi0m`
- Drive exact-reconstruction playbook ID: `10VbDtHuLJU2XxByuGllAZCqqugI02ddo`
- Drive market study ID: `1nHiP0s4T-AZEOq2xfq6ahakAgezlqJ31`
- Drive reconstruction standard ID: `1a5J7tI0cGmujElaJFU0IGCOrxlq9-eto`
- Drive release receipt ID: `1o9ItDyiJ6XjnyytGk1TFbQDJhzMa-lGW`
- Drive folder ID: `1qAVqAzWUvZcbZ7EpHRWsrAQjOd62630J`
- GitHub continuity mirror: `Herbertofury/ProjectDump/tools/minecraft-dev-kit`

The superseded 301 KB package/checksum and previous canonical docs remain preserved under `PRE-MARKETPLACE-CONTEXT-RECONSTRUCTION-SUPERSEDED` names. Do not overwrite or delete lineage.

## Proven reconstruction stack

### Reference evidence and parity

- source/frame hashes, timing, masks, edges, palettes, bounding boxes and centroids;
- still/GIF parity with silhouette IoU, silhouette-edge F1, internal-edge F1, SSIM, foreground CIEDE2000 and DTW timing;
- missing/excess residual maps;
- strict observed-vs-inferred boundary.

### Geometry/camera/turntable

- multi-view cuboid/camera inverse fitting;
- zero-start voxel visual hull from calibrated silhouettes;
- constant-camera orthographic **and perspective** turntable GIF calibration;
- automatic evidence-constrained refinement that refuses unobservable-axis drift;
- internal projected geometry edges for guards, visors, plates, seams and inset detail.

### Semantic asset coverage

17 compiler-valid zero-start scaffold classes:

`sword, dagger, greatsword, axe, mace, hammer, spear, polearm/glaive, scythe, shield, crossbow, staff, bow, armor, head_cosmetic, furniture, decor`

Named locators cover grip/tip/strike/projectile/block/player/head/placement/seat/interaction anchors.

### Context fitting

- held-item similarity transforms around semantic anchors;
- player/world rig oracle constraints;
- furniture placement/seat/interaction fitting;
- context transforms are solved separately from underlying asset geometry.

### Motion

- optical-flow motion partitions as candidate bone boundaries;
- GIF inverse fitting for bone rotation **and translation**;
- internal-edge-aware pose fitting when visible detail moves inside an unchanged outer silhouette;
- local solve with global fallback rather than accepting weak frames silently.

### Texture/material/2D

- visible box-UV texture back-projection with coverage/confidence and cross-view disagreement;
- conservative preview de-light/palette draft plus emissive candidates;
- unobserved texels are never mislabeled as recovered;
- icon-sheet extraction by grid/components with nearest-neighbor-only scaling and per-icon hashes.

### Pack-level premium quality

- family texel-density and scale bands;
- shared palette/motif checks;
- normalized shape signatures;
- declared-distinct anti-shape-clone and anti-texture-clone gates;
- existing premium 16-stage mob/boss production and authoring lane remains green.

## Final packaged-copy evidence

- multi-view geometry IoU: `1.000000`;
- independent camera-fit IoU: `0.998999`;
- GIF rotation/pose IoU: `0.997519`;
- visible texture round-trip RGB MAE: `0.0` on covered texels;
- semantic scaffold classes: `17/17` validate;
- held-weapon screen RMSE: `0.000037 px`;
- held-weapon world RMSE: `0.000005` model units;
- furniture screen RMSE: `0.0 px`;
- furniture world RMSE: `0.000052` model units;
- icon-sheet fixture: `6/6` sprites;
- coherent distinct pack fixture: `PASS`, 0 errors / 0 warnings;
- declared-distinct clone fixture: correctly `FAILS` with `variety.shape_clone` and `variety.texture_clone`;
- perspective turntable -> visual hull IoU: `0.916118`;
- same-outer-silhouette internal-motion IoU: `1.000000`;
- internal-motion geometry-edge F1: `1.000000`;
- packaged premium six-boss suite: PASS, existing 16 stages remain green;
- invalid event-marker fixture: correctly rejected.

## Release-validation anti-stall split

Do **not** return to a monolithic marketplace regression. Preserve independent bounded lanes:

1. base inverse lane;
2. static/context marketplace lane;
3. motion/turntable marketplace lane;
4. premium mob/boss lane.

A timeout in one does not erase already-green evidence from the others. Retry only after changed code/input or new evidence.

## Rights/evidence invariant

Public marketplace previews are quality benchmark evidence, not automatic reproduction permission. Exact reconstruction of third-party commercial art requires user ownership/authorization. `Exact` is scoped to observable supplied views/times; hidden surfaces, unseen texels, source pivots, original audio and server-only logic remain inferred/unknown until evidence supplies them. Native Minecraft proof is separate and mandatory.

## No-repeat history

- Do not rebuild the server-plugin registry from scratch.
- Do not redo the Nazgul's Forge public benchmark survey unless freshness/product scope changes.
- Do not rerun green packaged lanes before a mutation invalidates them.
- Do not merge split marketplace regressions back into one timeout-prone release blocker.
- Do not dump Dev Kit state into `Minecraft-Mod-Vault`.
- Do not replace real model/runtime previews with generated imagery unless explicitly requested in the current message.

## Exact next action

The tooling frontier is now strong enough that more synthetic fixtures have diminishing value. The next acceptance milestone is a **real authorized vertical slice**:

1. ingest an actual user-owned/authorized image/GIF reference bundle;
2. run the rights-gated reconstruction contract through camera/geometry/motion/texture/context fitting and parity;
3. repair any real-world residuals by improving the earliest causal tool, preserving them as regression fixtures;
4. compile the reconstructed source into the least-lossy target renderer (for the normal target, Forge 1.20.1 + GeckoLib/native as appropriate);
5. perform deterministic multi-view/multi-time Project Visual QA;
6. launch the actual Minecraft client/integrated server and prove scale, lighting, culling, grounding, held/worn transforms, animation state, gameplay event sync, VFX/SFX and persistence;
7. package/hash/publish that vertical slice only after the native gate is green.
