# Creeperella: Bloom & Boom 1.4.2 — Pie-family Animation Fidelity

Checkpointed: 2026-08-24 (America/Denver)
Target: Minecraft 1.20.1 / Forge 47.4.23 / Java 17

## Change

1.4.2 continues from the corrected 1.4.1 Cat Creeper baseline and brings Female, Bunny, and Bee up to the same source-driven animation standard as Cherry/Blossom. The native Forge model now executes the rich motion families already authored in the supplied Pie CEM files instead of relying on mostly vanilla Creeper locomotion plus a small blink/accessory approximation.

Female/Bunny/Bee now preserve and execute source-style body translation/lean, breathing sway, head counter-motion and head sway, four-leg phase gait with independent lift/stride, turn influence and stance roll/yaw, hair inertia, chest secondary motion, pupil tracking, exact Pie blink timing, hurt recoil, and deterministic per-entity idle phase. Bunny regains the source tail/ear behavior including the articulated second right-ear segment. Bee regains source tail/ear/wing motion; the invented generic high-frequency flap is removed.

The CEM hierarchy semantics are preserved deliberately: source top-level `body.*` and `leg1..4.*` animation channels drive the original vanilla proxy parts absolutely, while nested custom IDs drive their converted child parts. The detached native `head2` reconstruction reapplies the animated source body parent and then its local head channels, preserving the original body/head counter-motion without double-transforming the converted geometry.

Cat 1.4.1 animation and Cherry/Blossom animation methods remain byte-identical to the corrected 1.4.1 baseline.

## Deterministic source/animation verification

- Pie reference hashes: **8/8 exact** to the supplied Pie assets retained as project references.
- Source animation channel sets: **Female 53 / Bunny 61 / Bee 64**.
- Native CEM target hierarchy/gait/gaze/accessory mapping audit: PASS.
- Numeric source-expression parity: **712 sampled channel evaluations PASS** against expressions read directly from the supplied JEM files.
- Exact Pie blink/gaze semantics: PASS.
- Corrected Cat source audit: **5/5 source hashes, 39/39 base cubes, 14/14 charged cubes PASS**.
- No invented Cat tail yaw/roll: PASS.
- Cat animation method body: byte-identical to 1.4.1 baseline.
- Cherry/Blossom animation method body: byte-identical to 1.4.1 baseline.
- Original five 2D spawn-egg hashes unchanged; **24/24** six-variant 3D egg states resolve.
- **68/68 JSON resources** parse successfully.
- Fresh extraction of the packaged 1.4.2 source ZIP and rerun of deterministic audits: PASS.
- No image-generation model used for project QA.

## Deterministic Visual QA

A new 1.4.2 source renderer preserves the existing per-pixel depth buffer and renders actual generated ModelPart geometry, exact project textures, and the same source-derived runtime formulas. The showcase includes per-variant PNG/GIFs, six-mob gallery and animation lineup, MP4s, front/three-quarter/side/back Pie-family motion QA, and a 1.4.1-vs-1.4.2 Female/Bunny/Bee motion comparison.

The multi-angle and comparison outputs were visually inspected for obvious torso/limb/accessory bleed and pose/hierarchy defects. This is deterministic project-source QA, not a live Minecraft screenshot.

## Drive persistence

Canonical Drive folder: `Creeperella - Bloom & Boom` (`1Rz2CyGTW0olVMO4o1_fSwcOnNEL9k3jc`).

- Full source: `Creeperella-Bloom-and-Boom-1.4.2-Forge-1.20.1-source.zip`
  - SHA-256 `b886d7192a941132b4e454ceb4fcf59c2840ffac89734678e0164e088bf90bda`
  - size `236047` bytes
  - Drive ID `1rnYst4wLoB1e5wq7Fc_TD67WCBseqsYo`
  - Drive raw round-trip SHA-256: MATCH
- Visual QA showcase: `Creeperella-1.4.2-Visual-QA-Showcase.zip`
  - SHA-256 `499ad0043deb35981dda95de9667ea6f87f675ad80e97c13b8bf046215c6a813`
  - Drive ID `11xxyY1ilfv2aL2ukW2zotbHfQ-RXX4G-`
- Visual QA SHA manifest: `Creeperella-1.4.2-Visual-QA-SHA256SUMS.txt`
  - SHA-256 `af22fc62b05096e3ffae828ad7b5ffac55cc651e9ca00fec76359060988c071c`
  - Drive ID `1ZyRiKd8oHNif_W1ZTmJmFvKYUhWWvGsM`
- Verification snapshot: `Creeperella-1.4.2-FINAL_VERIFICATION.md`
  - Drive ID `1D6OSdPOCFLgmDRdrFDLEyXqbs40qB8-h`
- Pie native-port notes: `Creeperella-1.4.2-PIE-CEM-ANIMATION-PORT.md`
  - Drive ID `1rMNbtSNInotEqZS8MbwBTpKX_jIzkK_a`

## GitHub production gate

GitHub CI branch `build/creeperella-1.4.2-ci` has been created from the existing 1.4.1 verification lineage so production verification can continue without mixing this animation work into an older branch.

**A 1.4.2 production JAR is not claimed verified yet.** The remaining acceptance gate is a successful Java 17 ForgeGradle compile/remap followed by a real Forge 47.4.23 dedicated-server startup using the resulting remapped JAR. Until that gate passes, the full 1.4.2 source and deterministic visual/source parity artifacts above are the authoritative checkpoint.

## Continuation rule

Continue from the full 1.4.2 Drive source archive plus this receipt. Do not regress Pie's full source animation program back to vanilla locomotion or an invented generic accessory animation. Preserve exact Pie blink timing and source hierarchy semantics, preserve the corrected Cat 1.4.1 conversion, preserve Cherry/Blossom source motion, and use deterministic project-source visual QA only unless synthetic image generation is explicitly requested by the user.
