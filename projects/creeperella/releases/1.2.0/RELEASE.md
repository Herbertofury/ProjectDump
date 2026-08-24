# Creeperella: Bloom & Boom 1.2.0 — Demolition Buddies

Released/checkpointed: 2026-08-23 (America/Denver)
Target: Minecraft 1.20.1 / Forge 47.4.23 / Java 17

## Verified code state

- Build branch: `build/creeperella-1.2.0`
- Verified head: `0cad39770e8ec6f1b1cdcec982b155c5ac9725a9`
- PR: #18
- GitHub Actions run: `32684075580`
- ForgeGradle + production Renamer build: PASS
- Real Forge 47.4.23 dedicated-server startup: PASS (`Done (25.010s)!`)
- Production-remapped CI JAR SHA-256: `7ae74797c6bacbb6f4998659532d208a124dc32d90a9339371f6a8ece491c9d9`
- Readable canonical continuation source: branch `export/creeperella-1.2.0-source`, path `projects/creeperella/source/1.2.0`.
- Continuation rule: work from readable canonical source or the full verified Drive source archive. Do not reconstruct working source from base64 CI transport chunks.

## Full release

- JAR: `Creeperella-Bloom-and-Boom-1.2.0-Forge-1.20.1.jar`
  - SHA-256: `235b286e0252219b3b671ec1c28bcc739899c38377556bd7e77f8c38aec8cac7`
  - size: 109680 bytes
  - Drive ID: `1veQhU10ES69vnM0WVAfuf76U3QIgSb8k`
  - Drive URL: https://drive.google.com/file/d/1veQhU10ES69vnM0WVAfuf76U3QIgSb8k/view?usp=drivesdk
  - Drive round-trip hash: MATCH
  - 20/20 compiled classes byte-identical to the production JAR that passed the server gate.
- Full source: `Creeperella-Bloom-and-Boom-1.2.0-Forge-1.20.1-source.zip`
  - SHA-256: `670bdc84a6c6e8eea9f3ea3f22fa10961872b54fec6db7fd025f3f8bf5180f35`
  - size: 123187 bytes
  - Drive ID: `1u4931diDe-m4NbsRP4RPqPW1cbPKgSzq`
  - Drive URL: https://drive.google.com/file/d/1u4931diDe-m4NbsRP4RPqPW1cbPKgSzq/view?usp=drivesdk
  - Drive round-trip hash: MATCH
  - ZIP integrity: PASS
  - exact canonical 14 Java files, 38 valid JSON resources, 7 PNG client assets.
- Checksums Drive ID: `1eCXZGb_65m-CStNW1T8ybRCSzY8iwuaK`
- Verification Drive ID: `1r91PlhL6y7MdFfp62NMH-nDJBcWIAGPK`
- Research Drive ID: `1PUmln_uZMHcbZg3dq6e1MqFUY4SO6YpO`
- Release receipt Drive ID: `1NhewpJuQnbF80FCwJXVWxUgoUh12tayC`
- Drive folder: `Creeperella - Bloom & Boom` (`1Rz2CyGTW0olVMO4o1_fSwcOnNEL9k3jc`)

## 1.2.0 shipped behavior

All five Creeperella variants can be deterministically bonded with their themed explosive treats, heal from those treats after taming, Follow/Stay, catch up safely, bind to a Fuse Whistle, perform line-of-sight Boom Runs against valid mobs/enemies, detonate immediately on command, reform beside their owner instead of dying, and observe separate normal/charged cooldowns. Owner/allied-player/sibling-Creeperella/owner-pet blast protection and non-griefing follower explosions are enabled by default. Tamed Creeperellas are hard-blocked from vanilla one-life Creeper ignition/fuse behavior.

All 1.1.0 transformation, spawn, model, legacy Pie tag, charged-state, and vanilla-Creeper non-replacement behavior is retained.

## Next verification / premium pass

Graphical Minecraft client QA remains the intentionally unclaimed proof surface: models, overlays, icons, particles, transformations, Follow/Stay, whistle targeting, and explosion/reformation presentation. After that, the strongest next premium feature is cross-dimension companion transfer + respawn resynchronization, followed by a Forge 1.20.1 compatibility matrix against Creeper Overhaul, Baby Creeper, Companions!, Moldyfishy's Baby Mobs, and Baby Mobs Rebrushed.
