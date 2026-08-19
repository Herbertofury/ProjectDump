# Webmeji Wiki

**Project Constellation ID:** `PCX-039`
**Status:** ACTIVE / TRACKED
**Canonical user-owned standalone source:** unresolved in connected GitHub
**Current lightweight external behavior reference:** [lars-rooij/webmeji](https://github.com/lars-rooij/webmeji) at `ead02b16acb7759588d8ee52480386dac2c25898`
**Current Shimeji-ee/WASM comparison reference:** [pixelomer/Shijima-Web](https://github.com/pixelomer/Shijima-Web) at `817237c07b5afdb4d37b4a5fc6b546045b986947`
**Current GameSync integration evidence:** [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync) at `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`

## Purpose

Webmeji is the lightweight website-embedded mascot runtime track. Its value is near-zero setup: a site owner should be able to add a companion directly to ordinary pages without turning the site into an application framework or breaking host-page input.

The intended project is related to Shimeji but is not interchangeable with the full Shimeji Desktop or browser-extension tracks. It should preserve web-native simplicity while borrowing only the behavior semantics that make sense for an embedded page companion.

## Current source boundary

The current connected GitHub environment does not expose a verified user-owned standalone Webmeji repository. Do not initialize a replacement project merely because public references are easy to find.

Three current evidence sources are useful:

1. `lars-rooij/webmeji`, a direct small JavaScript/CSS embedded-Webmeji implementation;
2. `pixelomer/Shijima-Web`, a more behavior-faithful WebAssembly browser runtime built on `libshijima` and `libshimejifinder`;
3. the current GameSync mascot contract, which already contains explicit Webmeji settings and allowances.

The next implementation action is to resolve the user-owned source and reconcile these references against it rather than choosing one by architecture alone.

## Lightweight external Webmeji reference

Checked against current repository head `ead02b16acb7759588d8ee52480386dac2c25898`. [lars-rooij/webmeji](https://github.com/lars-rooij/webmeji) describes itself as a Shimeji embedded directly into a website.

Its basic embed consists of only:

- `webmeji.css`
- `config.js`
- `webmeji.js`

No package manager or build step is required by that source tree.

Verified reference behavior includes:

- walking along the bottom edge;
- idle/sit/dance/trip actions;
- jumping to side/top edges;
- hanging/climbing/falling from edges;
- hover pet interaction;
- mouse and touch dragging;
- requestAnimationFrame movement;
- multiple instances and multiple skins;
- configurable allowances, movement speeds, animation frames, intervals, and loop counts.

The upstream roadmap mentions momentum while dragging/falling, collision-based edge clinging, jumping between edges, arbitrary edges, and a client-side behavior menu. Treat those as ideas, not as already-implemented facts.

## Shimeji-ee/WASM differential reference: Shijima-Web

[Shijima-Web](https://github.com/pixelomer/Shijima-Web) is more useful than a generic sprite demo because it preserves a real Shimeji-ee behavior-engine lineage in the browser. It remains experimental, but its current source provides concrete architecture and compatibility evidence that the standalone Webmeji track should test against.

The current repository head is `817237c07b5afdb4d37b4a5fc6b546045b986947`. Relevant recent history includes:

- touch/pointer input support;
- a low-power tick-speed repair;
- Shimeji-ee archive download/import support;
- an updated `libshijima` submodule.

These commits make Shijima-Web a materially stronger differential benchmark than a plain JavaScript character animation loop even though it is not the canonical Webmeji source.

### Source architecture

The current top-level source includes:

```text
CMakeLists.txt
bindings.cc
build.sh
main.js
wrapper.js
libshijima/       git submodule
libshimejifinder/ git submodule
zlib/             git submodule
shimejiee.zip
```

`CMakeLists.txt` verifies:

- CMake 3.18 minimum;
- C++17;
- Emscripten/WebAssembly output;
- `libshijima` as the behavior engine;
- `libshimejifinder` for Shimeji/archive discovery;
- zlib-backed archive support;
- Emscripten filesystem exposure;
- memory growth enabled;
- an embind-based JavaScript bridge.

The repository's `.gitmodules` uses GitHub SSH URLs for `libshijima` and `libshimejifinder` plus HTTPS for zlib. A clean source checkout therefore needs the submodules initialized and usable GitHub credentials/SSH configuration for the two pixelomer submodules, or an equivalent verified URL rewrite.

### Verified build path

The checked-in `build.sh` uses Emscripten's CMake wrapper:

```bash
emcmake cmake -DCMAKE_BUILD_TYPE=Release -Bbuild
make -Cbuild zlibstatic -j$(nproc)
emcmake cmake -DCMAKE_BUILD_TYPE=Release -Bbuild
make -Cbuild -j$(nproc)
```

This is reference-project evidence, not yet a required toolchain for the user-owned Webmeji project.

### Archive import path

`main.js` verifies a real archive pipeline rather than a hardcoded demo-only character:

1. the browser accepts dropped files;
2. file bytes are written to Emscripten FS at `/tmp/archive.bin` in 1 MiB chunks;
3. `extractShimeji()` extracts the archive;
4. each imported `.mascot` record provides `actions.xml` and `behaviors.xml`;
5. the runtime registers the template with `libshijima` and spawns it;
6. the included `shimejiee.zip` fixture is also fetched and imported automatically on startup.

That import path is valuable for future Webmeji compatibility testing because it exercises actual Shimeji-ee configuration instead of only a hand-authored JavaScript animation table.

### Pointer and touch model

`wrapper.js` uses Pointer Events rather than separate mouse-only handlers:

- each mascot image handles `pointerdown` and `pointerup`;
- document-level `pointermove` and `pointerup` maintain drag state;
- mascot dragging is forwarded into the `libshijima` manager/environment;
- the runtime removes its document pointer listeners in `delete()`.

This provides a concrete touch-capable comparison lane for the user-owned Webmeji runtime.

### Render and environment model

The current wrapper renders each mascot as a fixed-position `<img>` element and updates viewport geometry from `document.documentElement.clientWidth/clientHeight`.

Current source also verifies:

- `MascotEnvironment.setSubticks(2)`;
- breeding disabled through `setAllowsBreeding(false)`;
- a host tick loop driven by `setInterval(..., 20)` with accumulated catch-up time;
- runtime image loading from extracted mascot package files;
- horizontal sprite mirroring through CSS transforms;
- explicit mascot and manager disposal paths.

This is useful evidence for timing and lifecycle comparison, but the source inspected here does not establish arbitrary DOM-element edge surfaces. Its environment is viewport-oriented, which is an important boundary when comparing it with the user goal of eventually attaching mascots to selected page elements.

## Current GameSync Webmeji contract

The current GameSync mascot contract contains explicit Webmeji controls rather than treating Webmeji as an unnamed generic sprite mode.

Current defaults include:

- `webmejiCanvasRenderer: false`
- `webmejiEnabled: false`
- `webmejiSpawnCount: 3`
- `webmejiJumpChance: 0.08`
- `webmejiWalkSpeed: 50`
- `webmejiFallSpeed: 200`
- `webmejiJumpSpeed: 150`
- `webmejiGetUpMs: 2000`
- pet, drag, bottom, top, left, and right allowances enabled.

Related current mascot/runtime defaults include:

- `shimejiFixedSeedEnabled: false`
- fixed seed value `1337` when deterministic mode is enabled;
- `shimejiTickMs: 40`;
- `shimejiSpawnCap: 12`;
- automatic spawn-on-import enabled.

This is evidence that GameSync already treats Webmeji/Shimeji behavior as a first-class compatibility surface. Preserve that contract when reconciling standalone and integrated implementations.

## Architecture comparison

The three verified evidence lanes solve different problems and should remain distinct during recovery:

| Lane | Strength | Important boundary |
| --- | --- | --- |
| `lars-rooij/webmeji` | extremely small direct embed, plain JS/CSS, no build | lighter behavior model than Shimeji-ee |
| `pixelomer/Shijima-Web` | real Shimeji-ee archive/behavior engine through WASM, pointer/touch input | heavier build/runtime, viewport-oriented environment, experimental project |
| GameSync mascot contract | integrated settings, persistence, deterministic test knobs, browser-extension host | not proof of a standalone three-file Webmeji implementation |

Do not collapse these into one architecture prematurely. The user-owned source may already contain the best parts of more than one lane.

## Recommended architecture boundary

Keep the embeddable core small and host-neutral:

- configuration and sprite/animation data;
- creature state machine;
- page-edge/element-edge geometry;
- pointer/touch interaction;
- animation/movement scheduler;
- deterministic optional RNG for tests;
- explicit cleanup/dispose path.

Host-specific adapters can then provide:

- plain-script embed;
- GameSync integration;
- browser-extension integration;
- future Feature Foundry preview/runtime integration;
- optional Shimeji-ee/WASM compatibility adapter if differential tests prove it worthwhile.

Avoid coupling the core to extension APIs, React, a specific bundler, or a single host page.

## Differential compatibility experiment

Once the canonical user-owned Webmeji source is resolved, run the same representative mascot/interaction corpus across the user runtime, `lars-rooij/webmeji`, Shijima-Web, and the GameSync integration where applicable.

Capture at least:

| Area | Evidence |
| --- | --- |
| Startup | scripts/modules loaded, first visible mascot latency, errors |
| Input | mouse drag, touch/pointer drag, pet interaction, release/fall behavior |
| Edges | bottom/top/left/right movement and transition behavior |
| Pack import | direct config/skin load plus a representative Shimeji-ee archive where supported |
| Behavior | idle/walk/jump/fall/climb/hang selection and timing |
| Layout | viewport resize, scroll, dynamic layout change |
| Element surfaces | selected DOM-element attach/climb/hang behavior when supported |
| Multiple mascots | count, independent state, drag interaction, cleanup |
| Determinism | fixed-seed/replay capability where supported |
| Lifecycle | remove/dispose, listener cleanup, navigation/unload behavior |
| Performance | CPU time, animation cadence, memory, responsiveness |
| Host safety | links, forms, selection, scrolling, navigation and page input remain usable |

The acceptance goal is not to choose the largest engine. It is to preserve the simplest useful embed while proving any borrowed Shimeji-ee behavior adds compatibility or capability without making ordinary-page integration fragile.

## Current improvement experiment

Prototype two optional behaviors without changing the default lightweight embed contract:

1. momentum on drag release/falling;
2. arbitrary element-edge attachment so a Webmeji can treat selected page elements as climb/hang surfaces.

The experiment must be capability/config driven and disabled by default until verified.

### Acceptance gate

- existing bottom/top/left/right behavior stays identical when new options are off;
- pet, drag, jump, fall, get-up, and multi-instance behavior still works;
- mouse and touch remain supported;
- host-page clicks, text selection, scrolling, links, forms, and navigation are not intercepted incorrectly;
- element-edge attachment updates correctly as layout/scroll changes;
- cleanup removes listeners/animation work;
- no viewport culling or quantity cap is introduced as a performance shortcut;
- if a Shimeji-ee/WASM adapter is tested, the adapter must be optional and must not become a mandatory dependency for the plain embed unless real compatibility evidence justifies that tradeoff.

## Troubleshooting and comparison notes

### A Shimeji archive imports in Shijima-Web but not in the user runtime

Treat the archive as a compatibility fixture. Compare config discovery, archive layout, actions/behaviors XML parsing, path normalization, and image lookup before rewriting runtime behavior.

### Touch dragging behaves differently from mouse dragging

Use Pointer Events as the comparison baseline. Verify pointer capture/release semantics, page scrolling, text selection and multi-touch behavior rather than adding separate mouse-only fixes.

### Browser CPU usage is high

Record the scheduler model before tuning. The lightweight reference uses requestAnimationFrame movement, while Shijima-Web currently uses a 20 ms interval/catch-up loop around the behavior engine. Compare timing under active, background, low-power and hidden-tab conditions without reducing mascot count, behavior fidelity or off-screen correctness.

### Element-edge behavior is requested

Keep viewport-edge and element-edge geometry separate. Recompute selected element surfaces from current layout/scroll state and fail cleanly when an element disappears. Do not fake element support by pinning a mascot to stale coordinates.

## Exact current next action

Resolve the canonical user-owned Webmeji source. Establish its current build/runtime baseline, then run the differential corpus against:

1. `lars-rooij/webmeji` for minimal direct-embed behavior;
2. `pixelomer/Shijima-Web` for Shimeji-ee/WASM archive and behavior-engine compatibility;
3. the current GameSync Webmeji/Shimeji settings/runtime contract.

Use the results to implement the smallest evidence-backed compatibility or element-edge improvement in the real source and verify it on ordinary desktop and touch pages.

## Maintenance

Update this page when the canonical source is resolved, the embedded API/config schema changes, GameSync Webmeji settings change, or a current external implementation materially advances the state of the art.