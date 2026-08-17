# ProjectDump Project Wikis

This directory contains source-controlled wikis for the **projects tracked inside Project Constellation**. Project Constellation itself is the catalog/control plane and is not a normal documentation target. A legacy `PCX-036` continuity wiki remains preserved because it already exists, but it is excluded from target-project wiki coverage and should only be changed for a real control-plane continuity reason.

## Published detailed project wikis

- [PRJ-002 - Feature Foundry](PRJ-002-feature-foundry.md)
- [PRJ-003 - GameSync Platform](PRJ-003-gamesync-platform.md)
- [PRJ-005 - Mascot / Screenmate Platform](PRJ-005-mascot-screenmate-platform.md)
- [PRJ-006 - ACS Agent Parity Runtime](PRJ-006-acs-agent-parity-runtime.md)
- [PRJ-022 - Feral Unified Native Base](PRJ-022-feral-unified-native-base.md)
- [PRJ-023 - Feature Foundry Portable Feature Starter](PRJ-023-feature-foundry-portable-feature-starter.md)
- [PRJ-024 - MO2 Drag/Column Compatibility Pack](PRJ-024-mo2-drag-column-compatibility-pack.md)
- [PRJ-025 - UltraDeck](PRJ-025-ultradeck.md)
- [PCX-026 - Project Governance](PCX-026-project-governance.md)
- [PCX-027 - GameSync Archive Doctor](PCX-027-gamesync-archive-doctor.md)
- [PCX-028 - DirectoryMonitor](PCX-028-directorymonitor.md)
- [PCX-029 - PC Bridge / MCP Bridge](PCX-029-pc-mcp-bridge.md)
- [PCX-030 - Reliable Artifact Publisher](PCX-030-reliable-artifact-publisher.md)
- [PCX-031 - Auralis](PCX-031-auralis.md)
- [PCX-032 - Profit Nova](PCX-032-profit-nova.md)
- [PCX-033 - Sims4CreatorStudio](PCX-033-sims4creatorstudio.md)
- [PCX-034 - Ferrum Browser](PCX-034-ferrum-browser.md)
- [PCX-035 - MO2R](PCX-035-mo2r.md)
- [PCX-037 - Shimeji Desktop](PCX-037-shimeji-desktop.md)
- [PCX-038 - Shimeji Browser Extension](PCX-038-shimeji-browser-extension.md)
- [PCX-039 - Webmeji](PCX-039-webmeji.md)
- [PCX-040 - Pinterest Nocturne](PCX-040-pinterest-nocturne.md)
- [PCX-041 - ChatGPT Ultimate Optimizer](PCX-041-chatgpt-ultimate-optimizer.md)
- [PCX-042 - GameSync Next](PCX-042-gamesync-next.md)
- [PCX-043 - Feature Foundry Production App](PCX-043-feature-foundry-production-app.md)
- [PCX-044 - Feature Foundry Living Ecology](PCX-044-feature-foundry-living-ecology.md)
- [PCX-045 - Feature Foundry Object Intelligence](PCX-045-feature-foundry-object-intelligence.md)
- [PCX-046 - Feature Foundry Source Hubs](PCX-046-feature-foundry-source-hubs.md)
- [PCX-047 - Favorite Artist Worlds Database](PCX-047-favorite-artist-worlds-database.md)
- [PCX-048 - GameSync Theme Foundry](PCX-048-gamesync-theme-foundry.md)
- [PCX-049 - GameSync Live Mascot Tavern](PCX-049-gamesync-live-mascot-tavern.md)
- [PCX-050 - GameSync Real Library Performance](PCX-050-gamesync-real-library-performance.md)
- [PCX-051 - GameSync Capability Truth / UI QoL](PCX-051-gamesync-capability-truth-ui-qol.md)
- [PCX-052 - GameSync Release Factory](PCX-052-gamesync-release-factory.md)
- [PCX-053 - GameSync Bounty / Rewards Runtime](PCX-053-gamesync-bounty-rewards-runtime.md)
- [PCX-054 - GameSync Source Finder / Entity Resolver](PCX-054-gamesync-source-finder-entity-resolver.md)
- [PCX-055 - GameSync Script Polling Runtime](PCX-055-gamesync-script-polling-runtime.md)
- [PCX-056 - GameSync Mod Health](PCX-056-gamesync-mod-health.md)
- [PCX-057 - Project Catalog / Cross-Chat Database](PCX-057-project-catalog-cross-chat-database.md)
- [PCX-058 - Project Compass Northpoints](PCX-058-project-compass-northpoints.md)
- [PCX-059 - Feature Foundry Project Brain Bridge](PCX-059-feature-foundry-project-brain-bridge.md)
- [PCX-060 - ACS Voice / Speech Runtime](PCX-060-acs-voice-speech-runtime.md)
- [PCX-061 - Petz Shared Core](PCX-061-petz-shared-core.md)

Current detailed target-project wiki coverage: **43 tracked projects**.

## Preserved control-plane reference

- [PCX-036 - Project Constellation](PCX-036-project-constellation.md) - legacy continuity reference only; excluded from the target-project coverage count.

## Maintenance contract

The Project Constellation wiki maintainer should continue across the full tracked-project catalog, prioritizing active projects with current source repositories and documentation gaps. For each project it should:

1. resolve the newest canonical project source and branch;
2. preserve Project Constellation goal, requirements, next action, stop point, blockers, and continuity history;
3. inspect project-owned manifests, source layout, runtime, tests, releases, configuration, schemas, APIs, integrations, extension points, and troubleshooting evidence;
4. document install, configure, use, modify, build, test, package, and contribution workflows when verified;
5. distinguish verified runtime facts from historical recovery material, plans, prototypes, and unresolved gaps;
6. correct stale Project Constellation summaries when newer project-owned evidence proves a different current state;
7. avoid invented commands or architecture details;
8. publish scoped wiki changes to `Herbertofury/ProjectDump` and fetch the remote file or commit and verify it contains the intended content before treating the update as complete;
9. preserve useful existing detail rather than rewriting pages cosmetically;
10. document PCX-036 only when there is a real control-plane/continuity change, not as a substitute for project-specific documentation.

## Coverage rule

A project is not considered fully documented merely because it has a short Project Constellation HTML page or catalog entry. The Markdown wiki should grow toward enough verified detail that another developer can operate and modify the project without undocumented tribal knowledge.

Projects with incomplete/recovery-only source should still have truthful pages describing identity, lineage, blockers, recovery state, and the exact evidence needed before build/use instructions can be completed.
