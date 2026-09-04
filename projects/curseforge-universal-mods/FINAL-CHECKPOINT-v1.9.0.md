# CurseForge Universal Mods v1.9.0 FINAL CHECKPOINT

Date: 2026-09-04
Canonical target: CurseForge 1.319.0.38738
Canonical patch: v1.9.0
Validation policy: native Linux CurseForge runtime oracle plus deterministic Windows file patching; Wine was not used for v1.9.

## Canonical release artifacts

- Patcher ZIP: `CurseForge-Universal-Mods-Patcher-v1.9.0.zip`
  - bytes: 2460799
  - SHA-256: `4df5efbbc39b2a710a8b36ab3061ff1453d30ff441afa108dd3aa5ccebf5ee40`
  - Drive ID: `10W2YJbxmgn3djaIPxsErriRgQznu9xR6`
- DirectPatch ZIP: `CurseForge-Universal-Mods-DirectPatch-1.319.0-38738-v1.9.0.zip`
  - bytes: 110791401
  - SHA-256: `1445d954cf16c10bf000948e5f000b6dc07a893d45d05cf669b17558b3fdceb7`
  - Drive transport: exact ZIP split into three verified parts because the connector has a 100 MiB single-transfer ceiling.
- Source archive: `CurseForge-Universal-Mods-v1.9.0-source.tar.gz`
  - bytes: 65744
  - SHA-256: `676f29553e85a49abd2dea5aca1bf6eb578b6b4ebc85c715e30301cdebb5829b`
  - Drive ID: `1srnEtnduAUABcdUnHhVj15bhqt80FWEg`

Canonical Windows binary hashes:

- Patcher EXE: `8d96f426d50ce30616e97fb1898aa448ee4026386b4ca02c620c42da00c546b8`
- Patched `CurseForge.exe`: `3b5cfcd795eeefaf1c6d6a1b7b71e753df67242caa6475a5476bf3a377d8f0e9`
- Patched `resources/app.asar`: `170d1eb7f39a6b0bfd45fbf56d0efa634b610dd3a13149ea867089b7e56c3d27`
- Patched ASAR header SHA-256: `f50dcdbbe4883468dda0cb602dd2baf2cac28a57a27343a859fbb9bbe5fc05f9`

## v1.9 acceptance state

### First-class native integration

- No standalone Modrinth tab, browser, Add Content button, second Update All button, or second confirmation flow.
- Modrinth and unmatched Local projects join CurseForge's normal profile Content collection at the native InstalledProjects result boundary.
- Mods and Resource Packs share CurseForge's native search, sort, filtering, virtualization, card/list/table render paths, and action plumbing.
- Existing profile Filter popover includes Source = CurseForge / Modrinth / Local through CurseForge's own filter state.
- Source badges render inside CurseForge's React rows before paint; no post-render DOM badge mutation.
- Repaired badge also renders before paint and is additive provenance rather than replacement provider identity.
- Modrinth update state uses CurseForge's native Out-of-Date / Update control.
- CurseForge's existing Update All modal is the only bulk confirmation; applicable Modrinth updates join the same flow after confirmation.
- Failures use CurseForge's native floating Error toast; renderer contains no browser alert()/confirm().
- Provider-aware row navigation prevents projectId=0 routes: CurseForge remains native, Modrinth opens its real provider project/version page, Local reveals the installed file.
- Local rows suppress empty View Project / View Links / Copy Mod Link provider actions.
- External authors remain visible as native-styled text without masquerading as CurseForge author identities.

### Repaired-mod provenance and identity

Repair is an attribute, not an identity rewrite:

- repaired CurseForge -> still CurseForge
- repaired Modrinth -> still Modrinth
- unknown unmatched file -> Local

Trusted repair provenance can be supplied by:

- `META-INF/cfum-repair.json`
- `CFUM-*` attributes in `META-INF/MANIFEST.MF`
- `<mod-file>.cfum-repair.json` sidecar
- profile `.cf-universal-mods/repairs.json` registry

Supported provenance includes provider, projectId, versionId/fileId, original/current SHA-512, repair tool, reason, and timestamp. Hash-bound metadata is ignored if the file changed, so stale repair identity cannot attach to a replacement JAR.

Repaired CurseForge JARs that no longer match CurseForge's normal file hash can recover real project/file identity from profile/repair metadata and ask CurseForge's own GameInstance-scoped services for the project. Native installedModId, status, updateVersion, artwork, author, summary, and actions are preserved when the service can prove them. If update state cannot be proven, v1.9 does not invent an Update button.

Repaired Modrinth projects can recover through exact versionId, projectId, or original SHA-512 and continue using compatible-provider update detection instead of comparing the repaired binary hash as if it were the published artifact.

Repair sidecars participate in update/toggle/delete transactions and rollback. An official replacement does not inherit stale Repaired provenance.

### Detection coverage

- `.jar`
- `.jar.disabled`
- `.jar.disable`
- Resource Pack `.zip`
- unpacked Resource Pack directories containing `pack.mcmeta`
- recognized CurseForge, Modrinth, repaired provider-linked, and unmatched Local content
- native/external dedupe including unpacked Resource Packs

Resource Pack rows suppress unsupported mod-JAR active-state controls and mixed active-state calls are preflighted before native items can be partially modified.

### Performance / no-jank state

- Injected MutationObserver: none.
- Post-render badge/action decoration: none.
- CSS relational `:has(...)` row selector: none.
- React stamps a direct `cfum-has-badge` class before paint.
- Unchanged external content signature: zero native list refetch.
- Byte-identical cache state: zero cache file rewrite.
- File hash/metadata reuse when size + mtime are unchanged.
- Positive Modrinth identity/update cache for passive re-entry/focus: 5 minutes.
- Hash-bound negative Local identity cache: 5 minutes; changing file hash invalidates it immediately.
- Explicit native Refresh bypasses provider caches.
- Passive focus refresh respects the real 90-second scan cooldown.
- Modrinth version/project/update requests batched to 100 items with bounded concurrency.
- Development synthetic merge benchmark: 1000 native + 1000 external projects, 100 runs, 6.732 ms average per 2000-row merge.

## Verification

- Go test suite: PASS.
- QOL JavaScript suite: PASS.
- Injected renderer/main/preload syntax: PASS.
- Official native Linux CurseForge 1.319.0.38738 upstream anchor audit: PASS.
- Static premium/safety audit: PASS.
  - renderer alert/confirm: 0
  - injected MutationObserver: 0
  - injected setInterval: 0
  - 15-minute cadence: 0
  - filesystem watcher: 0
  - Scheduled Task creation: 0
  - only remaining schtasks behavior is one-time deletion of the obsolete v1.0-v1.4 auto-repatch task
- Native Linux v1.9 bounded runtime smoke: PASS for loaded/runtime evidence.
  - app version 1.319.0.38738
  - OS linux
  - v1.9 main bridge ready
  - Electron App Ready
  - SessionStarted
  - real Mods Agent started and connected
  - real 1440x816 CurseForge window created
  - v1.9 TypeError/ReferenceError/Uncaught renderer failures observed: 0
  - runtime was intentionally stopped at the environment's known external-DNS boundary; a full internet-backed Minecraft profile click-through is not claimed from this sandbox.
- Windows lineage convergence using final Linux-native v1.9 patcher:
  - v1.5 -> v1.9 PASS
  - v1.6 -> v1.9 PASS
  - v1.7 -> v1.9 PASS
  - v1.8 -> v1.9 PASS
  - all four output exact canonical EXE/ASAR bytes
- Deep ASAR integrity:
  - 244/244 packed files full SHA-256 PASS
  - 244/244 block-hash sets PASS
  - packed offsets contiguous/in bounds PASS
  - current ASAR header hash appears exactly once in Windows EXE
  - v1.5/v1.6/v1.7/v1.8 old ASAR header hashes absent
- Deterministic Windows patcher rebuild: PASS.
- Final Patcher and DirectPatch ZIP integrity: PASS.
- Fresh extraction gate from the actual final Patcher ZIP: PASS.
  - bundled source tests PASS
  - source rebuild reproduces exact shipping Windows patcher hash
  - fresh untouched v1.5 target patches to canonical Windows v1.9 hashes
  - patch status reports installed
  - README/package sanity PASS

## Drive publication and readback proof

Drive project folder: `1HcVsT6o1Za0yFrfk_TAyGxC6YHiLT7S5`.

Uploaded artifacts:

- Patcher ZIP ID `10W2YJbxmgn3djaIPxsErriRgQznu9xR6`
- Source archive ID `1srnEtnduAUABcdUnHhVj15bhqt80FWEg`
- ZIP checksums ID `16YsEg4OgBL74TzGBi-DXdkjTgnv-Kj4H`
- Fresh-extraction receipt ID `1_3I6XLSntvTA7crqqoWqEqNJWUTwsdBV`
- DirectPatch part000 ID `1Jf8fV_Fu5pYZEnbnI3P3Hy-_Tg4qcHkv`
- DirectPatch part001 ID `152wIeg2hbuJ28FbR2V3VBh3bQD1g3y4m`
- DirectPatch part002 ID `1_EYoe9VowIjji78lRdlPk7f7yUeMQvXo`
- part checksums ID `19xg3yNYjcutQHOhl5T15bBHf80ZRLJ74`
- reassembler ID `1DUjB9Ue0jHHYn1VxhIYnIMwQUgW_PlR7`
- multipart README ID `1DenxiCYNuBVF1Jpb2A-GyFgKINanWC3p`
- final checkpoint Drive ID `1D0u23BiUd37483sVBteJgRKVtDRS3hjK`
- Drive readback verification ID `19AaNcgDtdt6MpidBbomff242LKSBy-yu`

Drive metadata sizes match the local release. Patcher ZIP and source archive were downloaded back and matched their exact local SHA-256. All three DirectPatch parts were downloaded back, individually matched their exact local hashes, concatenated from the Drive copies only, produced the exact canonical DirectPatch SHA-256 `1445d954cf16c10bf000948e5f000b6dc07a893d45d05cf669b17558b3fdceb7`, passed ZIP integrity, and byte-compared equal to the local DirectPatch. Publication is therefore byte-for-byte verified rather than inferred from upload acknowledgements.

## Exact next action

Use `CurseForge-Universal-Mods-Patcher-v1.9.0.zip` on the real Windows CurseForge 1.319.0.38738 installation and inspect the exact Noxviola Content profile that previously exposed the missing-content/filter defects. If a concrete live Windows mismatch remains, preserve v1.9 as the canonical baseline and patch only that observed delta. Do not restore the removed split Modrinth UI, browser alerts, watchdog, poller, or background autorepatcher.
