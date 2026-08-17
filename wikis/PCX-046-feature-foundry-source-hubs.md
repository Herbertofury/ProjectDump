# Feature Foundry Source Hubs Wiki

**Project Constellation ID:** `PCX-046`  
**Status:** ACTIVE / TRACKED  
**Goal:** Manage external media and asset providers through explicit source adapters.  
**Current evidence authority:** Feature Foundry V33 durable runtime artifact plus current provider documentation.

## Verified current state

The strongest recovered Feature Foundry runtime evidence is the durable V33 artifact `Feature-Foundry-V33-RECOVERED-ECOLOGY-OUTSIDE-BOX.html`. It contains a real **Functional Soundtrack Provider Hub** rather than a decorative provider chooser.

Verified V33 provider behavior includes:

- provider choice stored per theme;
- per-theme soundtrack URL mappings stored locally;
- provider controls that perform real external navigation;
- assigned-soundtrack controls that open the stored URL;
- a local Web Audio handoff cue;
- explicit refusal to claim remote playback unless a host supplies authorized playback state.

The V33 provider set currently contains:

- Spotify
- Apple Music
- Deezer
- SoundCloud
- TIDAL
- YouTube Music

This is verified evidence for a soundtrack-provider subset of Source Hubs. It is **not** proof that a broad authenticated source-hub layer for all media, assets, discovery, libraries, or publishing providers is complete.

## Source Hub contract

A Source Hub adapter should own provider-specific behavior instead of spreading provider assumptions through Feature Foundry workspaces. Each adapter should expose a machine-readable capability record containing at least:

- stable provider ID and display name;
- provider type and supported content classes;
- public-catalog capabilities;
- authenticated/user-library capabilities;
- playback or launch capabilities;
- authorization mode and required scopes;
- secret/token ownership and storage boundary;
- redirect requirements;
- rate-limit behavior;
- pagination and result limits;
- cache restrictions and refresh strategy;
- source/provenance rules;
- fallback behavior;
- current API/version evidence;
- last review date;
- known degraded or unavailable capabilities.

The UI must derive promises from this capability record. A provider button must not imply playback, editing, library access, or upload if its adapter only supports external navigation.

## Current authorization research

### Spotify

Spotify currently recommends **Authorization Code with PKCE** for mobile apps, single-page apps, desktop-like public clients, and other clients where a secret cannot be safely stored. Spotify has deprecated the Implicit Grant flow. Its February 2026 Development Mode migration also changed endpoint and app-limit behavior, so a Source Hub cannot assume an older Web API surface remains unchanged.

Primary documentation:

- https://developer.spotify.com/documentation/web-api/concepts/authorization
- https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow
- https://developer.spotify.com/documentation/web-api/tutorials/february-2026-migration-guide
- https://developer.spotify.com/documentation/web-api/references/changes/february-2026

### Apple Music

Apple Music API requests require a signed developer token. MusicKit on the Web automatically manages the Music User Token for subscriber-specific requests. Directly managed developer-token requests are rate-limited and can return HTTP 429 responses.

Primary documentation:

- https://developer.apple.com/documentation/applemusicapi/generating-developer-tokens
- https://developer.apple.com/documentation/applemusicapi/user-authentication-for-musickit

### General OAuth boundary

RFC 9700 / BCP 240 is the current OAuth 2.0 security best-current-practice document. Public clients must use PKCE for authorization-code injection protection, and redirect-based flows require strict handling.

Primary source:

- https://www.rfc-editor.org/rfc/rfc9700.html

## Anti-regression rules

- Do not replace the working V33 external-navigation provider hub with a mocked authenticated layer.
- Do not store provider secrets in theme packages, project-brain data, logs, exported worlds, or source-controlled configuration.
- Do not mark a provider capability active because its documentation advertises the capability. Exercise the real authorized flow first.
- Preserve theme-level provider and soundtrack mappings across schema migrations.
- Preserve V33's truthful remote-playback boundary until a real provider session has been exercised.
- Provider failure must be visible and isolated. One provider outage or authorization failure must not break the full Source Hub.

## Proposed capability and auth matrix

The next architecture increment should add a provider capability/auth matrix behind the adapter interface. Suggested fields:

`provider -> capability -> auth mode -> scopes -> token owner -> rate limit -> cache rule -> fallback -> verified runtime -> reviewed date`

For Spotify, the first authenticated experiment should use PKCE and the current Development Mode constraints. For Apple Music web integration, the experiment should use MusicKit's managed user-token path and an appropriately protected developer-token service boundary rather than embedding a signing key in the browser.

Other current V33 providers should remain external-navigation adapters until their API/auth/runtime paths are separately sourced and exercised.

## Smallest useful experiment

Implement the capability matrix without changing V33's existing provider UX. Add one feature-detected authenticated test lane for Spotify and one for Apple Music. Keep current external navigation as the fallback.

### Acceptance test

- all six current V33 providers still open correctly;
- existing per-theme provider and URL mappings survive migration and restart;
- capability UI never advertises an unsupported action;
- Spotify PKCE authorization succeeds, refresh behavior is exercised, and failures are visible;
- Apple Music user authorization is exercised through MusicKit on the Web;
- no client secret or signing private key is present in browser-exportable state;
- provider-specific errors do not corrupt theme state;
- fallback external navigation still works when authenticated functionality is unavailable.

## Exact next action

Materialize the provider capability/auth matrix around the existing V33 soundtrack hub, then exercise the first authenticated provider lanes without changing or removing the verified V33 fallback behavior.

## Evidence

- Feature Foundry V33 durable artifact: https://drive.google.com/file/d/1QL4u4MTrpATCVQxFrt4scEq32ky8hqvk/view
- Project Constellation Quick View v0.5.0 provider/source-hub continuity record: https://drive.google.com/file/d/1up9K9DTdUVg_fnW-v8bHVAIbjEWX7l77/view

## Wiki maintenance

Update this page when provider capabilities, authorization models, rate limits, API versions, credential boundaries, cache rules, fallback behavior, or verified runtime coverage change. Preserve old provider evidence as lineage rather than rewriting history.