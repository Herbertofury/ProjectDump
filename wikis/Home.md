# ProjectDump Wiki

This is the **live GitHub Wiki** for the projects tracked inside Project Constellation.

Project Constellation is the catalog and continuity control plane. Its legacy PCX-036 page is preserved as a control-plane reference, but normal wiki maintenance targets the projects tracked inside it.

## Browse the project documentation

- [[Complete Project Wiki Index|README]]
- [[GitHub Wiki Automation]]

The complete index currently contains detailed pages for **all 62 tracked project targets**. The preserved PCX-036 Project Constellation control-plane reference is intentionally excluded from that target-project count.

### Major active projects

- [[GameSync Platform|PRJ-003-gamesync-platform]]
- [[GameSync Next|PCX-042-gamesync-next]]
- [[Feature Foundry|PRJ-002-feature-foundry]]
- [[Sims4CreatorStudio|PCX-033-sims4creatorstudio]]
- [[MO2R|PCX-035-mo2r]]
- [[UltraDeck|PRJ-025-ultradeck]]
- [[Ferrum Browser|PCX-034-ferrum-browser]]
- [[RuneLite FlipForge Family|PRJ-010-runelite-flipforge-family]]
- [[Shimeji Desktop|PCX-037-shimeji-desktop]]
- [[Shimeji Browser Extension|PCX-038-shimeji-browser-extension]]
- [[Webmeji|PCX-039-webmeji]]

Use the sidebar for project families and the complete index for every currently documented tracked project.

## How this Wiki is maintained

The versioned source for these pages lives in [`wikis/`](https://github.com/Herbertofury/ProjectDump/tree/main/wikis) on the main ProjectDump repository. The `Sync GitHub Wiki` workflow publishes that source into GitHub's real separate `ProjectDump.wiki.git` repository.

A project-wiki change is not considered published merely because its source Markdown exists on `main`. The sync workflow must complete successfully and its publisher must fresh-clone the Wiki and byte-compare the remote page set with the intended source before the Wiki update is treated as complete.

This keeps the documentation source-controlled while making the actual reader-facing documentation the GitHub Wiki at:

https://github.com/Herbertofury/ProjectDump/wiki
