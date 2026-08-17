# ProjectDump Project Wikis

This directory contains source-controlled wikis for the **projects tracked inside Project Constellation**. Project Constellation itself is the catalog/control plane and is intentionally not a wiki target here unless explicitly requested.

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
- [PCX-033 - Sims4CreatorStudio](PCX-033-sims4creatorstudio.md)
- [PCX-034 - Ferrum Browser](PCX-034-ferrum-browser.md)
- [PCX-038 - Shimeji Browser Extension](PCX-038-shimeji-browser-extension.md)
- [PCX-042 - GameSync Next](PCX-042-gamesync-next.md)

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
10. avoid documenting Project Constellation itself in place of its tracked projects.

## Coverage rule

A project is not considered fully documented merely because it has a short Project Constellation HTML page or catalog entry. The Markdown wiki should grow toward enough verified detail that another developer can operate and modify the project without undocumented tribal knowledge.

Projects with incomplete/recovery-only source should still have truthful pages describing identity, lineage, blockers, recovery state, and the exact evidence needed before build/use instructions can be completed.