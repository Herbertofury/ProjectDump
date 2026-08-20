# Feature Foundry Source Hubs Wiki

**Project Constellation ID:** `PCX-046`  
**Status:** ACTIVE / TRACKED  
**Goal:** Manage external media and asset providers through explicit source adapters.  
**Current production authority:** `Herbertofury/Feature-Foundry` v24.0.0, current verified head `e1ba080b5c7590f1c844a6ed13b3a471709920b9`.  
**Historical implementation authority:** Feature Foundry V33 remains useful non-regression and lineage evidence, but it is no longer the current production implementation boundary.

## Current verified state

Feature Foundry v24.0.0 now contains a real typed **Music Hub / Source Hubs** implementation under `src/music/` rather than only the V33 soundtrack-provider concept.

Current project-owned source verifies six provider adapters:

- Spotify
- Apple Music
- Deezer
- SoundCloud
- TIDAL
- YouTube Music

The six providers share one provider catalog and one Music Hub runtime, but they intentionally do **not** advertise identical capabilities.

Current v24 source proves:

- provider metadata and capability records in `src/music/providerCatalog.ts`;
- a real `MusicHub` controller in `src/music/MusicHub.ts`;
- per-theme/per-room soundtrack mappings;
- validated provider URLs and provider-specific search routes;
- browser external handoff and Tauri native external handoff;
- session-only provider credential material;
- Spotify Authorization Code with PKCE implementation;
- a native Tauri loopback callback listener for Spotify authorization;
- Spotify account identity verification through `/me`;
- explicit Spotify access-token refresh, terminal reauthorization, quota-exhausted, and rate-limited states;
- Spotify authorized playback and next-item controls;
- Apple Music MusicKit v3 loading, user authorization, queue playback, and next-item controls;
- Deezer, SoundCloud, TIDAL, and YouTube Music as truthful external-handoff adapters rather than fake embedded integrations;
- localStorage mapping persistence for browser operation;
- native SQLite room-soundtrack persistence in the Tauri host;
- synchronized provider status and Music Hub diagnostics;
- a music signal bus that lets soundtrack actions pulse the living-world runtime.

This is materially stronger implementation evidence than the older V33 provider hub. It is still **not** proof that every provider has authenticated library, upload, editing, bulk-catalog, or embedded playback support.

## Source ownership map

### `src/music/providerCatalog.ts`

Owns the provider IDs, names, accent metadata, home/search URLs, allowed hosts, and capability records.

The typed provider set is:

```text
spotify
apple
deezer
soundcloud
tidal
youtube
```

Each provider capability record declares:

- public-catalog availability;
- authenticated-library availability;
- embedded-playback availability;
- external-handoff availability;
- authorization mode;
- account identity rule;
- token ownership boundary;
- quota ownership boundary;
- fallback behavior;
- review date.

Spotify and Apple Music currently advertise feature-detected authenticated-library and in-app playback capability. The other four adapters advertise verified external handoff only.

### `src/music/MusicHub.ts`

Owns:

- the Music Hub modal and provider navigation;
- room/theme soundtrack mappings;
- provider URL validation;
- provider search and home navigation;
- provider session state;
- Spotify PKCE and API requests;
- Apple Music MusicKit authorization/playback;
- external fallback;
- provider status/error display;
- native room mapping hydration/persistence;
- diagnostics;
- living-world music signal events.

### `src-tauri/src/lib.rs`

Owns the native Spotify OAuth loopback callback and exposes Tauri commands including:

```text
start_spotify_callback
assign_room_soundtrack
room_soundtrack
list_music_routes
catalog_summary
record_native_history
```

The loopback listener binds dynamically to `127.0.0.1:0`, returns the actual callback URL, validates the callback through the frontend PKCE state flow, emits `spotify-oauth-callback`, and does not require a fixed application port.

### `src-tauri/src/database.rs`

Owns the native SQLite source and soundtrack data. Relevant tables include:

```text
music_routes
room_soundtracks
history
```

`room_soundtracks` uses `(theme_id, room_id)` as its primary key and stores provider, URL, label, status, optional source ID, and update time.

The native database uses foreign keys, WAL journaling, and `synchronous=NORMAL` for the current persistence profile.

### `src/data/artist-worlds-v4.0.1.json`

Provides the current artist-world music-route source records loaded into the native `music_routes` table. The Music Hub preserves each route's approval status rather than silently promoting candidate routes to approved material.

## Music Hub user workflow

### Open the hub

The current product exposes Music Hub launchers including the quick soundtrack action. The browser UI verification suite exercises `#musicQuick` and waits for `#musicHub.open`.

The provider menu must contain:

1. Home
2. Spotify
3. Apple Music
4. Deezer
5. SoundCloud
6. TIDAL
7. YouTube Music
8. Settings

The current browser UI gate explicitly asserts all eight routes.

### Search without credentials

All six provider definitions expose a provider search URL. Searching from Music Hub opens the selected provider's real search destination.

This is the baseline capability and must remain available even when authenticated provider functionality is unavailable.

### Assign a soundtrack to a room

A room mapping stores:

```text
provider
url
label
status
sourceId (optional)
updatedAt
```

The URL must be HTTPS and must match the selected provider's allowlisted hosts.

The browser state is stored under:

```text
ff.music-hub.v2
```

When running inside Tauri, the same mapping is also written through `assign_room_soundtrack` to native SQLite. On context changes, `room_soundtrack` can hydrate native state back into the Music Hub.

A native persistence failure does not erase the active browser mapping; the UI reports the degraded durability state.

## Provider capability matrix

| Provider | Search / external handoff | Auth implementation in v24 source | In-app playback implementation | Current truthful boundary |
| --- | --- | --- | --- | --- |
| Spotify | Yes | Authorization Code with PKCE | Yes, through Web API player endpoints when connected | Live account/runtime qualification still required for release-grade auth proof |
| Apple Music | Yes | MusicKit v3 user authorization using a supplied developer token | Yes, through MusicKit queue/play/skip | Live subscriber/runtime qualification still required for release-grade auth proof |
| Deezer | Yes | Not activated | No | External handoff only |
| SoundCloud | Yes | Not activated | No | External handoff only |
| TIDAL | Yes | Not activated | No | External handoff only |
| YouTube Music | Yes | Not activated | No | External handoff only |

Do not infer capabilities beyond this matrix merely because a provider offers a public API.

## Spotify implementation

### Configuration

Music Hub settings accept:

- Spotify Client ID;
- redirect URI for browser use;
- session-scoped provider configuration.

The Client ID is stored in `sessionStorage`, not durable project or theme state.

Current keys include:

```text
ff.spotify.client-id
ff.spotify.session.v1
ff.spotify.pkce.verifier
ff.spotify.pkce.state
ff.spotify.pkce.redirect
```

### PKCE flow

The runtime:

1. generates a PKCE verifier;
2. hashes it with SHA-256 to create an S256 challenge;
3. generates and stores an OAuth state value;
4. starts the native loopback callback when running in Tauri;
5. opens Spotify authorization;
6. validates returned state;
7. exchanges the code using the original verifier;
8. stores the resulting session only in `sessionStorage`;
9. calls `/me` to verify account identity;
10. preserves provider mappings independently of authorization state.

The requested Spotify scopes currently include:

```text
user-read-private
playlist-read-private
playlist-read-collaborative
user-read-playback-state
user-modify-playback-state
streaming
```

### Durable account identity

The current Spotify Web API exposes `account_id` as a public, immutable, pseudoanonymous account identifier intended for account linking. Current v24 source uses `profile.account_id` when available and falls back to the older profile `id` only when necessary.

### Access and refresh lifetime

Spotify access tokens continue to be short-lived. Current Spotify documentation gives dashboard-issued refresh tokens a six-month terminal lifetime; refreshing an access token does not extend that lifetime.

Current v24 source:

- tracks access-token expiry from `expires_in`;
- records an approximate local six-month refresh-expiry boundary at authorization time;
- handles `invalid_grant` from the token endpoint as a reauthorization-required state;
- preserves room/provider mappings when reauthorization is required.

The provider does not expose a refresh-token issuance timestamp in the refresh token itself, so the app-owned authorization timestamp remains important evidence.

### Quota versus rate limit

Spotify Development Mode now uses a quota shared across a developer account rather than one independent budget per Client ID, and quota exhaustion can return:

```json
{"reason":"QUOTA_EXCEEDED"}
```

Current v24 source distinguishes:

- `quota-exhausted` for the structured `QUOTA_EXCEEDED` case;
- `rate-limited` for ordinary `429` responses;
- a `Retry-After` hint when present.

The Music Hub keeps external handoff available when provider API controls are unavailable.

### Playback

When Spotify is connected and the room mapping is a Spotify URL, the current implementation can:

- derive Spotify context URIs for album, artist, playlist, and show URLs;
- `PUT /me/player/play`;
- `POST /me/player/next`.

A playback failure is surfaced to the user instead of being replaced by fake success. When no usable authorized Spotify session exists, the action falls back to opening the mapped provider URL.

## Apple Music implementation

Current v24 source loads:

```text
https://js-cdn.music.apple.com/musickit/v3/musickit.js
```

The Music Hub expects a **server-issued developer token**. The signing private key is not part of the Feature Foundry browser runtime.

The developer token is stored only for the current session under:

```text
ff.apple.developer-token
```

After loading MusicKit, the runtime configures it for Feature Foundry 24.0.0 and calls user authorization.

When authorized, current source can:

- set a MusicKit queue from the room mapping URL;
- play the queue;
- skip to the next item when the MusicKit runtime exposes that action.

Apple's current documentation confirms that MusicKit on the Web automatically manages the Music User Token for web apps, while Apple Music API requests require a developer token. Keep those two responsibilities separate.

## External-handoff providers

Deezer, SoundCloud, TIDAL, and YouTube Music currently use the common external capability model.

For these adapters:

- public search/home routes are real;
- provider URLs are validated against allowlisted hosts;
- soundtrack mappings are real and persistent;
- external navigation is real;
- authenticated-library and embedded-playback controls are intentionally not advertised.

Do not create fake connection state simply to make their UI match Spotify or Apple Music.

## Mapping and persistence model

### Browser

Music Hub state version 2 is stored in localStorage. Credential/configuration material remains in sessionStorage.

This separation is deliberate:

- soundtrack mappings should survive ordinary app use and restart;
- provider authorization material should not leak into exported worlds, catalog data, or durable project state.

### Native desktop

The Tauri host persists room soundtrack assignments into `feature-foundry.sqlite3` under the application data directory.

The native database also seeds the artist-world music-route catalog from the verified Feature Foundry data file.

### Failure behavior

If browser durable storage is unavailable, the mapping remains active for the current view and the UI reports the limitation.

If native SQLite persistence fails, the browser mapping remains active and the UI reports that native durability failed.

A provider failure must not destroy mappings for that provider or any other provider.

## Living-world integration

Music Hub emits `ff:music-signal` events with reason, intensity, and the current theme/room context.

The current UI describes these signals as driving living-world reactions such as:

- water;
- particles;
- specular light;
- grass;
- atmosphere;
- mascot reactions.

The local ambient score remains a separate path from provider playback. Provider failure must not disable local living-world audio behavior.

## Verification status

### Repository verification command

From the canonical v24 source:

```powershell
npm install
npm run verify
```

`npm run verify` currently chains:

```text
npm run test
npm run typecheck
npm run build
cargo check --manifest-path src-tauri/Cargo.toml
npm run test:ui
```

The UI test currently verifies:

- the application reaches self-test pass state;
- full living-world regions render;
- Theme Atlas exposes all 27 catalog worlds;
- Music Hub opens from the product UI;
- Music Hub exposes Home + six providers + Settings;
- runtime diagnostics report `credentialStorage: "session-only"`;
- no browser page errors occur in that exercised flow.

### Important current boundary

The repository UI suite **does not use real Spotify or Apple Music credentials** and therefore does not by itself prove live account authorization, user-library access, provider playback, token renewal, quota handling, or terminal reauthorization against the real services.

Current provider auth/playback behavior is therefore classified as:

- **source-implemented**: yes;
- **statically/build verified**: yes through current project verification;
- **live-account runtime verified in repository evidence**: not yet established by the current test suite.

Do not collapse those three states into one "verified" checkbox.

## Build and package

Canonical commands from the current v24 package manifest:

```powershell
npm install
npm run dev
npm run desktop:dev
npm run verify
npm run desktop:build
npm run package
```

`npm run package` uses `scripts/package-release.ps1` and the current release process produces web, source, native installer, and SHA-256 artifacts under `artifacts/`.

## Configuration guidance

### Baseline no-account setup

No provider credential is required to use:

- provider search;
- external provider home pages;
- per-room soundtrack mappings;
- provider URL validation;
- external provider handoff;
- local living score behavior.

This should remain the zero-credential baseline.

### Spotify

For desktop operation:

1. register a Spotify application;
2. configure a loopback callback compatible with the app's native callback flow;
3. enter only the Client ID in Music Hub settings;
4. connect Spotify;
5. complete browser authorization;
6. return to Feature Foundry after the callback;
7. verify the connected account identity in the Music Hub;
8. exercise playback only when an appropriate Spotify device/session exists.

Never require a Spotify client secret inside the Feature Foundry browser or desktop frontend.

### Apple Music

1. generate the MusicKit developer token outside the Feature Foundry client using the protected signing key;
2. enter the resulting developer token into the current Music Hub session;
3. connect Apple Music;
4. complete MusicKit user authorization;
5. verify queue/playback behavior against an authorized subscriber session.

The signing private key must never be placed in Feature Foundry session storage, local storage, SQLite, project exports, or source control.

## Historical V33 lineage

V33 remains important because it established the product's truthful provider philosophy:

- six soundtrack providers;
- per-theme mappings;
- real external navigation;
- no false remote-playback claims;
- provider failure isolation.

Feature Foundry v24 extends that lineage with a typed provider catalog, real auth implementations for Spotify and Apple Music, native room-mapping persistence, and stronger diagnostics.

When v24 and V33 disagree about current implementation, current project-owned v24 source wins. Preserve V33 as non-regression evidence rather than treating it as the shipping source.

## Provider research retained for future Source Hubs

### Spotify

Current primary documentation confirms:

- Authorization Code with PKCE remains the public-client authorization path used by the current implementation;
- `account_id` is the stable account-linking identifier from `/me`;
- dashboard-issued refresh tokens have a six-month terminal lifetime;
- `invalid_grant` requires reauthorization;
- Development Mode quota is shared at developer-account scope;
- quota-exceeded responses can carry `reason: QUOTA_EXCEEDED`.

Primary references:

- https://developer.spotify.com/documentation/web-api/concepts/authorization
- https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow
- https://developer.spotify.com/documentation/web-api/tutorials/refreshing-tokens
- https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile
- https://developer.spotify.com/documentation/web-api/references/changes/may-2026
- https://developer.spotify.com/blog/2026-06-18-refresh-token-expiration
- https://developer.spotify.com/blog/2026-07-23-web-api-quota-updates

### Apple Music

Current primary documentation confirms:

- developer tokens authorize Apple Music API requests;
- subscriber-specific data requires a Music User Token;
- MusicKit on the Web automatically manages the Music User Token;
- MusicKit on the Web can support in-browser playback.

Primary references:

- https://developer.apple.com/documentation/applemusicapi/generating-developer-tokens
- https://developer.apple.com/documentation/applemusicapi/user-authentication-for-musickit
- https://developer.apple.com/musickit/

### Apple Music Feed

Apple Music Feed remains a **research-only future capability** for Source Hubs. It is not implemented by the current v24 Music Hub and must not be confused with MusicKit authorization/playback.

If evaluated later, model it as a separate bulk catalog capability with its own freshness, export, token, and usage-boundary metadata.

## Anti-regression rules

- Preserve all six provider adapters.
- Preserve the zero-credential external-handoff baseline.
- Preserve per-room and per-theme soundtrack mappings.
- Preserve browser mapping persistence and native SQLite mapping persistence.
- Never store signing private keys, client secrets, refresh tokens, or access tokens in exported worlds, project-brain state, source-controlled configuration, logs, or catalog datasets.
- Keep provider authorization state separate from soundtrack mapping state.
- Preserve the Spotify state check and PKCE verifier lifecycle.
- Preserve terminal refresh-token reauthorization as a distinct state.
- Preserve quota-exhausted versus ordinary rate-limited states.
- Preserve real failure messages instead of replacing provider failures with success UI.
- Preserve the provider URL allowlists.
- Preserve external handoff when provider API controls fail.
- Do not advertise authenticated functionality for Deezer, SoundCloud, TIDAL, or YouTube Music until real implementation and runtime evidence exist.
- Do not promote Apple Music Feed into a general-purpose internal metadata warehouse without an explicit capability and usage-boundary decision.
- Do not let a provider outage break local living-world audio or unrelated providers.

## Required next verification increment

The smallest useful next increment is **provider-auth runtime qualification**, not another provider UI redesign.

Create a dedicated Source Hubs verification lane that covers:

### Deterministic local/provider-fixture tests

- Spotify PKCE state mismatch rejection;
- missing verifier/client/redirect recovery;
- successful token exchange fixture;
- `/me` account identity using `account_id`;
- access-token expiry and refresh;
- `invalid_grant` transition to reauthorization required;
- `429` ordinary rate limiting with `Retry-After`;
- `429` with `reason: QUOTA_EXCEEDED`;
- `401` refresh-and-retry behavior;
- disconnect preserving room mappings;
- native callback listener returning the same redirect URI passed into the token exchange;
- provider URL allowlist rejection;
- native SQLite mapping round-trip;
- browser mapping restart persistence;
- Spotify/Apple failure leaving the other four external adapters usable.

### Authorized live smoke tests

Using controlled test accounts and non-exported credentials:

- complete Spotify PKCE authorization in the actual browser/desktop flow;
- verify `account_id` linkage;
- verify a real Spotify playback call with an active device;
- exercise disconnect and reconnect without losing mappings;
- complete Apple Music MusicKit authorization;
- verify real queue/playback and next-item behavior;
- restart the application and confirm durable mappings survive while session credentials do not silently become durable project state.

### Acceptance boundary

Only after these live flows pass should the Wiki classify Spotify or Apple Music account-controlled behavior as **live-runtime verified** rather than source-implemented.

## Troubleshooting

### Music Hub opens but the provider cannot connect

Check the selected provider's capability record first. Only Spotify and Apple Music currently expose authenticated connection controls.

### Spotify authorization opens but never returns to Feature Foundry

For the native app, verify that the loopback callback started successfully and that the authorized redirect exactly matches the callback URI returned by `start_spotify_callback`.

For browser operation, verify the configured redirect URI matches the registered application redirect and the current page route.

### Spotify says authorization state did not match

Treat this as a rejected authorization attempt. Do not bypass the state comparison. Start a fresh authorization flow so a new verifier and state are generated.

### Spotify requires authorization again

This can be the terminal refresh-token lifetime or an `invalid_grant` response. Reauthorize the provider. Do not delete room mappings.

### Spotify playback returns an error even though authorization succeeded

The current playback endpoint requires a usable Spotify playback context/device. Keep external handoff available and surface the real status code rather than treating authorization as proof that a device is ready.

### Spotify quota is exhausted

If the response carries `reason: QUOTA_EXCEEDED`, treat it as developer-account quota exhaustion rather than ordinary rolling rate limiting. External handoff should remain available.

### Apple Music authorization does not start

Verify the session has a valid server-issued developer token and that the MusicKit v3 script loads successfully.

### Apple Music token setup asks for a signing key in the app

That is the wrong boundary. The private signing key belongs outside the Feature Foundry client. The app consumes a developer token, not the signing key.

### A Deezer, SoundCloud, TIDAL, or YouTube Music page shows a Connect button

Treat that as a regression unless a real authenticated adapter and verification evidence were added. Those providers currently guarantee external handoff only.

### A saved mapping works in the browser but disappears in the native app

Inspect the Tauri `assign_room_soundtrack` command and SQLite `room_soundtracks` table. The browser mapping and native persistence are intentionally separate failure domains.

### A native mapping cannot be loaded

The Music Hub must keep the active local mapping and report degraded native persistence. Do not erase current state simply because SQLite hydration failed.

## Exact next action

Add a dedicated provider-auth verification suite around the current v24 implementation, then perform controlled live Spotify and Apple Music authorization/playback smokes in the actual Feature Foundry runtime. Preserve all six providers, the external-handoff baseline, session-only credential boundary, native/browser mapping durability, and truthful capability reporting. Promote account-controlled behavior to live-runtime verified only after those end-to-end flows pass.

## Evidence

### Current project-owned source

- Feature Foundry repository: https://github.com/Herbertofury/Feature-Foundry
- Current verified head: `e1ba080b5c7590f1c844a6ed13b3a471709920b9`
- Provider catalog: `src/music/providerCatalog.ts`
- Music Hub: `src/music/MusicHub.ts`
- Native host: `src-tauri/src/lib.rs`
- Native database: `src-tauri/src/database.rs`
- UI verification: `tests/ui.test.ts`
- Package/verification commands: `package.json`

### Historical evidence

- Feature Foundry V33 durable artifact: https://drive.google.com/file/d/1QL4u4MTrpATCVQxFrt4scEq32ky8hqvk/view

## Wiki maintenance

Update this page when the Feature Foundry production head, provider capability records, provider set, authorization model, token/secret ownership, stable account identity, credential lifetime, quota behavior, room-mapping persistence, native database contract, live provider verification, source-hub scope, or provider API evidence changes. Preserve older V33 and provider-research evidence as lineage rather than rewriting history.