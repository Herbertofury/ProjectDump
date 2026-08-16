# Feature Foundry Wiki

**Project Constellation ID:** `PRJ-002`  
**Status:** ACTIVE, major production rebuild  
**Connected repository:** [Herbertofury/Feature-Foundry](https://github.com/Herbertofury/Feature-Foundry)  
**Current repository evidence boundary:** the connected repository currently contains only a minimal `README.md` naming the project. The production application source has not yet been verified from that repository.

## Mission

Feature Foundry is intended to be a professional, deeply moddable authoring application for living theme worlds rather than a static theme generator or prototype gallery. Project Constellation preserves a V11 production directive/data lineage covering living worlds, UI skins, rooms, objects, weather, time, soundtracks, UI sounds, mascots, interactions, assets, research, mixing, packaging, and exports to multiple hosts.

The key continuity rule is that database validation, standalone HTML demonstrations, generated starter packages, and design directives are not substitutes for proving the real production application and its workflows.

## Current durable V11 state

Project Constellation identifies the current recovered line as **V11 production data platform and living-world directive**. The current exact next action is to locate the canonical app repository and reconcile it against V11 before coding.

### Recovered V11 artifacts

The durable project record identifies these V11-era artifacts:

- `feature-foundry-aesthetic-worlds-codex-master-directive.md`
- `feature-foundry-codex-final-implementation-directive-v11.md`
- `feature-foundry-aesthetic-world-guide-v11.md`
- `feature-foundry-living-world-prototype-v11-bundle-reference.html`
- `V11-VALIDATION-REPORT.md`
- Object Atlas SQLite database
- Theme Worlds SQLite database

These filenames are continuity evidence. Their exact canonical storage location/hash should be recorded here when re-resolved from current project-owned storage.

## V11 validation evidence

The preserved V11 validation report is recorded as **61 passed, 0 failed** for the supplied data/schema bundle. Project Constellation records validated counts including:

- 178 object archetypes and families
- 52 materials
- 178 behavior profiles
- 12 affordances
- 17 themes and versions
- 72 districts
- 17 room presets
- 51 weather profiles
- 17 soundtrack profiles
- 17 mascot profiles
- 170 object-pool members
- database integrity and foreign-key checks
- FTS and RTree checks
- cross-database references
- manifest hashes

### Critical verification boundary

Those checks validate the supplied data/schema bundle. They do **not** prove final artwork, production runtime integration, Blender conversion, provider authentication, complete editor workflows, packaging, export behavior, or the finished application.

## Approved V11 theme set

The durable V11 record preserves 17 full themes:

1. Frutiger Aero
2. Utopian Scholastic
3. Wacky Pomo
4. Contempo Eclectic
5. Vaporwave
6. Neo-Y2K
7. Liminal Leisure
8. Diner Kitsch
9. Cassette Futurism
10. Googie Kitsch
11. French Synthpop
12. Memphis
13. Ethereal CGI
14. Divine Machinery
15. Dark Fantasy
16. Atomic Age
17. Jazz / Solo Jazz

The broader aesthetics/research guide must not silently promote every researched aesthetic into a shipping theme.

## Major product subsystems

The durable V11 direction covers:

- professional application shell and configurable workspace
- living left/right worlds
- focused full UI
- performance mode
- Theme Studio
- Aesthetic Explorer and Mixer
- Asset Vault
- World Studio
- Room Studio
- Object Studio
- semantic affordance and rig system
- weather, time, lighting, soundtrack, UI sound, mascot, and interaction studios
- package/export system
- Object Atlas database
- Theme Worlds database
- multi-provider Music Hub
- GameSync migration and host adapters

Each top-level workspace must be a real functional workspace rather than a tab that merely changes highlighting or exposes placeholder UI.

## Professional workspace contract

Feature Foundry should behave like a serious authoring application. Workspaces and panels should be configurable and support professional layout behavior where implemented, including docking, resizing, moving, hiding, tabs, floating panels, saved layouts, task-specific workspaces, multi-monitor use, customizable toolbars/shortcuts/density/inspectors, and safe layout reset/restore.

This is a product requirement from the preserved project direction, not proof that the current runtime already provides all of it.

## Living-world behavior contract

Feature Foundry's living environments are meant to be interactive systems, not decorative backgrounds. Theme-native objects, weather, time, lighting, sound, mascots, and interactions should have bounded causal behavior while preserving user-input sovereignty, accessibility variants, performance variants, and deterministic/recoverable authoring state.

## Object intelligence contract

The Object Atlas / Object Studio direction requires semantic identity rather than treating assets as anonymous pictures. Preserve:

- object identity
- archetype/family
- materials
- affordances
- rigs
- behavior profiles
- source/provenance
- immutable originals
- reversible derivation lineage

Generated or transformed assets should remain traceable back to originals.

## Asset Vault contract

The Asset Vault is intended to be a real asset operating system, not an empty drawer. The durable project record specifically calls out the need for persistent assets, source provenance, visual DNA, hot-drop/capture flows, search, organization, and reversible operations.

## Aesthetic Explorer / Mixer contract

The preserved project record identifies prior Explorer implementations as generic/flat and not sufficient as a real mixing/research workflow. A valid Explorer should support actual discovery, comparison, mixing, source evidence, saved decisions, and promotion into production themes without conflating research with shipping content.

## Room Studio contract

The preserved record identifies Room Studio as a major repair area because prior versions were described as mostly empty scenes with pasted objects and weak editing tools. A production Room Studio needs real authoring operations, persistent scene state, object placement/manipulation, environment controls, and proof that saved content can be reopened and modified.

## Source Hubs and external providers

External media/asset providers should be represented through explicit source adapters with recorded:

- provider identity
- authentication mode
- capabilities
- limits
- cache behavior
- fallback behavior
- provenance/evidence
- review date

Provider research is not equivalent to production integration until authenticated/runtime flows are exercised.

## GameSync relationship

Feature Foundry is a source/authoring system for content that may be consumed by GameSync hosts. Avoid implementing theme behavior independently in each host. The intended pattern is one source-of-truth theme/content contract plus explicit host adapters and migration/parity evidence.

## Current failure and repair focus

Project Constellation currently preserves three prominent repair targets:

### Room Studio

Needs to become a convincing, persistent authoring environment rather than an underbuilt scene surface.

### Aesthetic Explorer

Needs to become a real research/mixing workflow instead of a generic flat browser.

### Asset Vault

Needs to become an operational asset system rather than an empty or underbuilt drawer.

The preserved history also warns that the best Explorer/media base may be a branch before an apparently newer numbered branch. A higher version number alone is not enough to select the latest-good implementation.

## Current repository problem

The connected [Feature-Foundry repository](https://github.com/Herbertofury/Feature-Foundry) currently exposes only a minimal project README. That means the repository does not yet provide enough verified source to document truthful install/build/run commands for the production app.

### Required source reconciliation before coding

1. Locate the canonical app repository/worktree/branch containing the real implementation.
2. Compare it against the V11 directive/data artifacts by identity, version, hashes, and substantive content.
3. Preserve newer user work instead of replacing it with V11 merely because V11 is well documented.
4. Reproduce the current Room Studio, Explorer, and Vault failures in the real runtime.
5. Build a migration ledger from current implementation to the V11 requirements.
6. Establish runtime proof for the affected workflows.

## Modification rules

When the canonical production source is resolved:

- create a recoverable checkpoint before broad changes;
- preserve existing working behavior and user content;
- avoid framework/dependency churn unrelated to the task;
- implement complete end-to-end workflows rather than decorative controls;
- keep project/source provenance for imported assets and data;
- verify workspace navigation, persistence, reload, restart, and export/import as applicable;
- test production builds rather than prototypes alone;
- maintain GameSync export/adapter compatibility explicitly.

## Verification ladder

Feature Foundry should maintain separate evidence for:

1. data/schema validation;
2. build/type/lint/unit checks;
3. application launch;
4. workspace navigation;
5. real authoring operations;
6. save/reopen persistence;
7. source-provider/authenticated flows;
8. package/export behavior;
9. host import behavior;
10. restart persistence and regression checks.

Do not collapse these into a single "validated" label.

## Exact current next action

Locate the canonical production application source and reconcile it against the V11 artifacts **before further implementation**. The connected placeholder repository is not enough to establish the production runtime.

## Wiki maintenance

Update this page whenever the canonical production repository is resolved, the V11 lineage changes, a workspace becomes runtime-verified, data schema counts change, host/export contracts change, or a previously documented gap is closed. Preserve the distinction between verified production behavior and design/data evidence.