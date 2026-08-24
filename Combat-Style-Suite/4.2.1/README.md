# Combat Style Suite 4.2.1 - Canonical Continuity Record

This directory records the verified 4.2.1 lineage for Combat Style Suite (Minecraft 1.20.1 / Forge 47.x / Java 17).

## Release artifacts

| Artifact | Size | SHA-256 |
|---|---:|---|
| combat-style-director-4.2.1.jar | 144086 | `e465c27cc996ae547909344c4fa11632614626f49406314a907a0fa6a4643bfe` |
| punchy-style-compat-4.2.1.jar | 37006 | `6f4dfa12ef7c320cb3d222ea29dccdcc321753d97d17aded6d552f51a401b443` |
| combat-style-suite-4.2.1-project.zip | 329478 | `744d2b4cfb1e0d21a9be3e1ac77491b8c9fb7abad234cfee853b29aabe774390` |
| Combat-Style-Suite-4.2.1-RELEASE-NOTES.md | 6872 | `f92d22271a7a5bca69ac22e19f4242cc97f452a904ec16ef9258a6490f47c14b` |
| Combat-Style-Suite-4.2.1-VERIFICATION.txt | 1575 | `635a2fcbcb5f6b0fc7510b3a92c281cf5187528217e5fd246bbf73cfde0e9898` |
| repair-history.jsonl after 4.2.1 lineage update | 32 records | `34eaceb81813ba8a21c34da0db7b3a346f971ce0bcf5202f8cbb127e09bc2ea3` |

## Canonical Drive release

Google Drive folder ID: `1fyDCPEtnLghGnYFt0P1rI7g4_3iWRP1x`

The complete deterministic project ZIP is stored there and contains the release JARs, complete Director/Compat source, compile stubs, all regression harnesses, README, MIT license, build scripts, strict verifier, release notes, verification transcript, and checksums.

## 4.2.1 hardening delta

- Zero production `ClientTickEvent` / `ServerTickEvent` listeners across both mods.
- Dynamic NBT correctness fallback moved from Forge ticking to a one-second re-armed one-shot sample dispatched onto the Minecraft client executor, with generation-token cancellation.
- Multiplayer presentation bursts now preserve the newest state via one delayed coalesced flush instead of silently dropping the final transition.
- Presentation protocol isolated to `presentation_sync_v4` / protocol 421.
- `verify-release.sh` fails closed before build work when any pinned exact target JAR is absent; `verify.sh` cannot mislabel a skipped binary audit as a full release verification.
- ControlFlex `ControllerBinding.getAnalogueNow()` uses the already sampled per-input-epoch analogue cache instead of repeating the API read.
- New regression coverage protects all of the above.
- A clean extraction of the final project ZIP ran `verify.sh` successfully and rebuilt both release JARs byte-for-byte identical to the frozen JARs.

## Exact compatibility baseline

- Epic Fight 20.14.17: `69566cf70ae2d91d3f2564c608f014c87e290cef6215c2a27719851165485f73`
- YSM 2.6.5 Forge 1.20.1: `25b5e902b96f4c298690208f8b433cbc31737c23f87590354dbd86f00207bc8f`
- Punchy 2.7d Forge 1.20.1: `180347c82d6b738cdb8bc5aef2f84f1a34781d20e3aea03a28f3ad84ff82ec76`
- Better Combat 1.9.0 Forge 1.20.1: `49c69dccf2c641246b4e3deca81ebac21f0ee119e81fc713b838b8e33569eea1`

## Verification honesty

The current execution environment did not expose the four exact upstream JAR bytes, so this release does **not** claim that their pinned binary API inspection was re-run here. The strict release gate was deliberately tested and correctly failed immediately when those files were absent. Real GPU-backed Minecraft profiling, physical controller testing, and live two-player/dedicated multiplayer also remain pending machine-side smoke tests.

Repair Brain lineage: `mc-1.20.1-forge-combat-style-suite-zero-tick-hardening-4.2.1`, superseding `mc-1.20.1-forge-combat-style-suite-event-driven-no-always-on-tick-4.2.0`.
