# Potatoptimize Forge 1.20.1 - Parity-Safe Port r1

Native Forge 1.20.1 production port targeting Forge 47.4.23 and Java 17.

## Vanilla-parity default profile
Behavior-changing, RNG-sequence-changing, loading, threading, save, profiler-removal, unsafe-random, and other semantically risky optimizations are **OFF by default**.

Enabled by default:
- sign ticking optimization
- packed-int/data-bit arithmetic optimization
- nearest item/player sensor stream-removal optimization

Everything else is explicit opt-in where available.

## Certification
Source commit: `c74675a97fd415f5fedbd168ba5553c0b55ad6c7`

Release JAR SHA-256: `5292a29d99eb4f51ef130043b5189b316d8f9274c459a47c8c03a2e0408832c6`

Passed:
1. Production Runtime QA `34153631803`: clean Forge 47.4.23 build/remap, gameplay/world exercise, save, clean shutdown, then second boot of the same world/config.
2. Optimization Stack QA `34153631787`: ModernFix + ServerCore + FerriteCore + Krypton Reno/FNP with compatibility and Mixin/runtime assertions.
3. Aggressive Profile QA `34153631764`: isolated server/common option families plus all-on challenge with zero family, individual-rule, or combination failures.

The optional entity-ticking path was hardened for Forge: concurrent entity storage remains, while gameplay/world entity actions stay on Minecraft's authoritative tick thread to prevent chunk-system circular waits.

Client-only experimental opt-ins remain OFF by default and are not claimed as dedicated-server certified.

GPL-3.0 upstream licensing is preserved.
