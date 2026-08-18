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
- stable account-linking identifier when the provider exposes one;
- access-token lifetime and refresh behavior;
- refresh-token lifetime, reauthorization policy, and expiry handling where applicable;
- secret/token ownership and storage boundary;
- redirect requirements;
- rate-limit behavior;
- quota ownership, quota-error identity, and shared-budget behavior where applicable;
- pagination and result limits;
- cache restrictions and refresh strategy;
- source/provenance rules;
- fallback behavior;
- current API/version evidence;
- last review date;
- known degraded or unavailable capabilities.

The UI must derive promises from this capability record. A provider button must not imply playback, editing, library access, upload, or bulk-catalog access if its adapter only supports external navigation.

## Current authorization and provider research

### Spotify

Spotify currently recommends **Authorization Code with PKCE** for mobile apps, single-page apps, desktop-like public clients, and other clients where a secret cannot be safely stored. Spotify has deprecated the Implicit Grant flow.

Spotify's February 2026 Development Mode migration also changed the practical API contract. Development Mode requires the app owner to have Premium, newly created apps are limited to five authorized users per app, multiple batch/browse/other-user endpoints were removed or replaced, search result limits were reduced, and applications need to tolerate missing or renamed response fields. The original February one-Client-ID limit was later superseded by Spotify's July 23, 2026 quota update.

A further May 2026 identity change is important for durable Source Hub account linking: `GET /me` now returns `account_id`, which Spotify documents as a public, immutable, pseudoanonymous account identifier. Spotify recommends using `account_id` rather than the older user `id` when linking an account to an external service because `account_id` is stable for the lifetime of the account.

Source Hub consequence: store provider linkage against a provider-scoped stable account identifier such as Spotify `account_id`, while treating display names and older user IDs as profile data rather than durable internal identity.

### June 2026 refresh-token lifetime change

On June 18, 2026, Spotify introduced a **six-month lifetime for refresh tokens** issued to apps registered in the Developer Dashboard. New apps became subject to the change immediately, and existing apps became subject to it on July 20, 2026. Refreshing an access token does not extend that six-month lifetime. When the refresh token expires, the token endpoint returns `invalid_grant` and the user must complete authorization again to obtain a new refresh token.

Source Hub consequence: an authenticated Spotify adapter needs an explicit credential-lifecycle state that distinguishes ordinary one-hour access-token renewal from terminal refresh-token expiry requiring user reauthorization. Refresh-token expiry must not be reported as a generic provider outage, silently retried forever, or allowed to corrupt the user's saved provider or theme mappings.

### July 2026 Development Mode quota update

On July 23, 2026, Spotify increased the Development Mode limit to **25 Client IDs per developer account**. Development Mode quota counting also changed from a per-Client-ID budget to a **single quota shared across all Development Mode Client IDs owned by the developer account**. Spotify added a structured JSON `reason` field to quota-exceeded `429 Too Many Requests` responses; quota exhaustion is identified by `QUOTA_EXCEEDED`, allowing applications to distinguish development quota exhaustion from ordinary rate limiting.

Source Hub consequence: capability/auth metadata must model quota ownership at the developer-account level rather than assuming every Client ID has an independent budget. Error handling should preserve provider state and use the structured reason when present so quota exhaustion, rolling-window rate limiting, authorization expiry, and other provider failures remain distinguishable and actionable.

Primary documentation:

- https://developer.spotify.com/documentation/web-api/concepts/authorization
- https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow
- https://developer.spotify.com/documentation/web-api/tutorials/february-2026-migration-guide
- https://developer.spotify.com/documentation/web-api/references/changes/may-2026
- https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile
- https://developer.spotify.com/blog/2026-06-18-refresh-token-expiration
- https://developer.spotify.com/documentation/web-api/tutorials/refreshing-tokens
- https://developer.spotify.com/blog/2026-07-23-web-api-quota-updates
- https://developer.spotify.com/documentation/web-api/concepts/quota-modes
- https://developer.spotify.com/documentation/web-api/concepts/rate-limits

### Apple Music

Apple Music API requests require a signed developer token. Subscriber-specific requests also require a Music User Token. MusicKit automatically manages the Music User Token on Apple platforms and in web apps, which makes that path materially different from embedding signing credentials or manually persisting a browser-visible developer private key.

Apple now also exposes **Apple Music Feed** for bulk offline catalog metadata. The feed covers album, song, artist, and popularity-chart metadata, refreshes fully every 24 hours, and is delivered through Apple Media Feed API exports in Parquet format. It is a separate capability lane from MusicKit user-library/playback authorization and uses developer-token authentication.

The feed carries a strict usage boundary in Apple's current documentation: feed content is for publicly promoting Apple Music content in the app, not for powering general internal systems, third-party data sharing, or unrelated music/artist analysis. Source Hubs should therefore model Apple Music Feed as an optional, purpose-restricted catalog-promotion adapter rather than silently treating it as a general-purpose metadata warehouse.

Primary documentation:

- https://developer.apple.com/documentation/applemusicapi/generating-developer-tokens
- https://developer.apple.com/documentation/applemusicapi/user-authentication-for-musickit
- https://developer.apple.com/documentation/applemusicfeed
- https://developer.apple.com/documentation/applemusicfeed/requesting-a-feed-export
- https://developer.apple.com/documentation/applemusicfeed/generating-developer-tokens

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
- Durable provider identity must use the strongest current stable provider-scoped identifier available instead of mutable display/profile fields.
- Purpose-restricted bulk feeds must remain isolated from general-purpose internal indexing and analytics unless the provider contract explicitly allows that use.
- Refresh-token expiry that requires reauthorization must be represented explicitly and must not erase provider mappings, tokens owned by other adapters, or unrelated project state.
- Provider quota exhaustion and rate limiting must remain distinct failure states when the provider supplies enough evidence to distinguish them.

## Proposed capability and auth matrix

The next architecture increment should add a provider capability/auth matrix behind the adapter interface. Suggested fields:

`provider -> capability -> auth mode -> scopes -> account identity -> token owner -> access-token lifetime -> refresh-token lifetime/reauth policy -> quota owner -> quota error identity -> rate limit -> cache rule -> usage boundary -> fallback -> verified runtime -> reviewed date`

For Spotify, the first authenticated experiment should use PKCE, current Development Mode constraints, `account_id` for durable account linkage, six-month refresh-token expiry handling, and developer-account-scoped quota handling. For Apple Music web integration, the experiment should use MusicKit's managed user-token path and an appropriately protected developer-token service boundary rather than embedding a signing key in the browser.

If Apple Music Feed is evaluated, keep it a separate catalog-promotion capability with explicit 24-hour export freshness, Parquet ingestion, developer-token ownership, and usage-boundary metadata. It must not replace MusicKit's user-authorized library/playback path.

Other current V33 providers should remain external-navigation adapters until their API/auth/runtime paths are separately sourced and exercised.

## Smallest useful experiment

Implement the capability matrix without changing V33's existing provider UX. Add one feature-detected authenticated test lane for Spotify and one for Apple Music. Keep current external navigation as the fallback. Add schema support for a stable provider account identifier, explicit access/refresh credential lifetimes and reauthorization state, provider quota ownership/error identity, and a purpose-restricted bulk-catalog capability, but do not activate a capability in the UI until its real runtime flow is verified.

For the Spotify fixture, exercise successful PKCE authorization and `account_id` linkage, ordinary access-token refresh, a simulated or controlled expired-refresh-token path that requires reauthorization, a quota-exceeded `429` carrying `reason: QUOTA_EXCEEDED`, and a separate ordinary rate-limit path. Verify that each state is distinguishable and that the existing external-navigation fallback remains usable.

### Acceptance test

- all six current V33 providers still open correctly;
- existing per-theme provider and URL mappings survive migration and restart;
- capability UI never advertises an unsupported action;
- Spotify PKCE authorization succeeds, normal access-token refresh is exercised, `account_id` is captured for durable provider linkage, and failures are visible;
- Spotify refresh-token expiry transitions to a reauthorization-required state without infinite retry, false success, or loss of provider/theme mappings;
- Spotify quota-exceeded `429` responses are distinguishable from ordinary rate limiting when the structured reason is present, and shared developer-account quota ownership is represented correctly;
- Apple Music user authorization is exercised through MusicKit on the Web;
- no client secret or signing private key is present in browser-exportable state;
- Apple Music Feed, if enabled, remains a separate purpose-restricted bulk-catalog lane and its 24-hour export identity is recorded;
- provider-specific errors do not corrupt theme state;
- fallback external navigation still works when authenticated functionality is unavailable.

## Exact next action

Materialize the provider capability/auth matrix around the existing V33 soundtrack hub, adding stable provider-account identity, explicit credential-lifetime/reauthorization state, developer-account-scoped quota identity/error handling, and a separate purpose-restricted bulk-catalog capability. Then exercise Spotify PKCE plus `account_id` linkage, normal access-token refresh, six-month refresh-token reauthorization handling, quota-versus-rate-limit behavior, and Apple Music/MusicKit authorization without changing or removing the verified V33 fallback behavior.

## Evidence

- Feature Foundry V33 durable artifact: https://drive.google.com/file/d/1QL4u4MTrpATCVQxFrt4scEq32ky8hqvk/view
- Project Constellation Quick View v0.5.0 provider/source-hub continuity record: https://drive.google.com/file/d/1up9K9DTdUVg_fnW-v8bHVAIbjEWX7l77/view

## Wiki maintenance

Update this page when provider capabilities, authorization models, stable account identifiers, credential lifetimes, reauthorization rules, rate limits, quota ownership, API versions, credential boundaries, bulk-feed usage boundaries, cache rules, fallback behavior, or verified runtime coverage change. Preserve old provider evidence as lineage rather than rewriting history.