# ProjectDump Project Wikis

This directory contains source-controlled wikis for the **projects tracked inside Project Constellation**. Project Constellation itself is normally the catalog/control plane, but it now has an explicit continuity wiki because Project Constellation is itself tracked as PCX-036 and the hourly evolution task explicitly requires inspecting and improving the control plane.

## Published detailed project wikis

- [PRJ-002 - Feature Foundry](PRJ-002-feature-foundry.md)
- [PRJ-003 - GameSync Platform](PRJ-003-gamesync-platform.md)
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
- [PCX-036 - Project Constellation](PCX-036-project-constellation.md)
- [PCX-037 - Shimeji Desktop](PCX-037-shimeji-desktop.md)
- [PCX-038 - Shimeji Browser Extension](PCX-038-shimeji-browser-extension.md)
- [PCX-039 - Webmeji](PCX-039-webmeji.md)
- [PCX-040 - Pinterest Nocturne](PCX-040-pinterest-nocturne.md)
- [PCX-042 - GameSync Next](PCX-042-gamesync-next.md)
- [PCX-053 - GameSync Bounty / Rewards Runtime](PCX-053-gamesync-bounty-rewards-runtime.md)

Current indexed detailed-wiki coverage: **23 tracked projects**.

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
