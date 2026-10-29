# packwiz + GitHub + Prism: how to organise the repository

> **Documento storico** (ricerca del 17/10/2026, in inglese): da qui vengono la cartella per versione di Minecraft e i tag `<MC>-vX.Y.Z`. Le regole attuali del repository, che nel frattempo sono cambiate (ramo `dev`, merge in `main`, documenti numerati), sono in `AGENTS.md`. I nomi di file citati sono quelli di allora.

Research date: 2026-10-17. Sources: the packwiz, packwiz-installer (v0.5.14 = current `main`) and bootstrap source code, the packwiz docs, the Prism Launcher source and docs, and about 20 public packwiz modpack repositories. I cloned the repositories and read them; I did not run any of their code. I also tested raw.githubusercontent.com URLs live. I found almost no Reddit or Discord discussion, so the claims below rest on code and on real repositories.

---

## 0. Short answer

* **Recommendation: one public repo, with one folder per Minecraft version ("line").** Each line folder holds its own packwiz root (`<line>/pack/pack.toml`) and its own docs. Material shared by all lines (general docs, scripts, CI) sits at the top level. Git **tags** mark releases. There is **no long-lived `stable` branch**.
* Each Prism instance chooses a version **through the URL alone**:
  * the dev instance uses `main` (or `packwiz serve` on your own machine);
  * the "real world" instance uses a release tag, and you edit the tag in the URL to upgrade. If you want it to update automatically, CI can move a pointer branch for it instead;
  * archive instances use an old tag. Tag URLs never change, so the archive instances stay frozen whatever you later do on `main`.
* **One repo per Minecraft version works, but you don't need it.** Freezing comes from tags, not from the repo layout. A new Minecraft version means a new Prism instance anyway. Separate repos would duplicate the docs, the CI and the README. The one real advantage is plain tags and a separate Releases page per version, which a tag prefix also gives you. If you ever want a separate repo, `git filter-repo --subdirectory-filter 1.21.1` extracts the folder later with its history.
* **Fixed costs of the approach, whatever the layout:**
  * The Prism instance's Minecraft and NeoForge versions must be set by hand. Current Prism ignores the `mmc-pack.json` changes that packwiz-installer makes during the pre-launch command; see 3.1.
  * If the 6 CurseForge-only mods have third-party distribution disabled, each instance asks once for a manual download.
  * `packwiz modrinth export` puts CurseForge jars *inside* the `.mrpack`. A public release must therefore not attach that file as-is; see 4.2 and 6.

---

## 1. Layouts for several Minecraft versions: what real packs do

| Layout | Real examples (packwiz) | Notes |
|---|---|---|
| **One repo, folder per MC version** (each with its own `pack.toml`) | **Fabulously Optimized**: `Packwiz/1.16.5 … 1.21.11, 26.1 … 26.3` (more than 30 folders) on `main`. Its `Packwiz/README.md` says: *"Because Packwiz cannot upgrade the MC itself, the modpack versions are foldered by Minecraft versions (always latest for the version)."* The bundled MultiMC instance points to `https://raw.githubusercontent.com/Fabulously-Optimized/fabulously-optimized/main/Packwiz/1.21.4/pack.toml`.<br>**Additive / Adrenaline** (SkywardMC): `versions/fabric/<mc>/`; a `justfile` loops `packwiz refresh/update/export` over every folder; unsupported lines move to `archived/`; one tag (`26.5.1`) covers all lines; `pack.toml` version is `26.5.1+mc1.21.1.fabric`.<br>**jimsimon/minecraft-modpacks**: `packs/<name>/`, tags `<pack>-v<version>`.<br>**mc-modpack-kit** (template): one subfolder per variant, release-please `monorepo-tags`.<br>**PackWize** (CLI): `Modpack/<mc>/<platform>/pack.toml` and runs packwiz across every folder. | Most common among multi-version packs. One CI, one place for docs, one README. Tags need a line prefix, or one tag covers every line as Additive does. |
| **One repo, branch per MC version** | **Venture**: branches `1.19.2`, `1.20.1`, `1.21.1`; default branch = current line.<br>**Cabricality**: branches such as `fabric/1.20.2/modrinth/main`, `fabric/1.20.4/modrinth/dev`, plus a `stale/…` prefix for dead lines.<br>**Tinkerer's Quilt**: `1.18`, `1.19`, `1.20`, `1.20_plus`… with tags `3.4.3+1.19`.<br>**CobbleCreations**: `fabric/1.19.2`, `fabric/1.20.1`, `quilt/1.19.2`, plus `v2` as default. | A port is a branch, so history continues and you can cherry-pick fixes across lines. But docs, scripts and CI drift apart on each branch. GitHub shows only the default branch. Releases from all lines mix together. For one person, this is the layout most prone to mistakes. |
| **Repo per MC version** | I found no packwiz pack doing this deliberately. Separate repos appear mostly when a pack is remade or a sequel starts, e.g. TerraFirmaGreg's "Modpack-Modern" repo. | Plain tags, separate Releases and issues, and GitHub's "Archive repository" switch for a dead line. The price is duplicated docs, CI and README, and shared material needs submodules or copies. |
| **Single version only** (for comparison) | Create: Astral (1.18.2): `main` plus an `Astral-Experimental` branch and tags `v2.1.x`. Create: Grand Expanse, Cobbleblock and ame-modpacks/cobblemon: one pack at the repo root. | — |

Pros and cons for your case:

* **History.** A folder copy loses `git log` continuity, though `--follow` partly recovers it. Branches keep history. Separate repos keep it only if you fork or copy.
  * In practice, a new Minecraft version for you is a *new pack* with a re-checked mod list. History continuity matters little.
* **Shared docs, scripts and datapack.** Easiest with a monorepo. With branches or repos you need copies or submodules.
  * Datapacks are tied to one MC version anyway: `pack_format` differs, and 1.21 renamed the data folders.
* **CI.** A monorepo needs one workflow with a folder or matrix parameter. Repo-per-version duplicates the workflow, or calls a reusable workflow kept in another repo.
* **Discoverability.** A monorepo has one README listing the lines. With several repos you need a separate index.
* **Raw URL stability.** It is the same in every layout. A URL is `raw.githubusercontent.com/<owner>/<repo>/<ref>/<path>/pack.toml`. If `<ref>` is a tag or a commit SHA, the URL never changes, even if you later move or delete the folder on `main`. So archived instances are safe in any layout.

---

## 2. Pack versions inside one MC version: dev, stable, frozen

### 2.1 Mechanisms seen in practice

* **Follow a branch.** FO follows `main`. Adrenaline's README follows a CI-built branch: `https://raw.githack.com/skywardmc/adrenaline/dist/versions/fabric/1.21.1/pack.toml`.
  * Additive and Adrenaline keep `no-internal-hashes = true` on `main`. CI runs `packwiz refresh --build` into an orphan `dist` branch and tags it `dist/<version>`.
* **Pin to a tag or commit.** A tag or commit SHA in place of the branch in the raw URL. The tags of Additive, Tinkerer's Quilt and Feather are all usable this way.
* **Experimental branch.** Create: Astral has `Astral-Experimental` next to `main`.
* **Pinned GitHub Release assets.** For example jimsimon's `.mrpack` at `releases/download/<pack>-v<ver>/<pack>-<ver>.mrpack`, plus *"Always cut a new version rather than re-uploading an asset."*
  * Release assets **cannot host a packwiz pack**. Asset names are flat, while packwiz needs `mods/*.pw.toml` paths next to `pack.toml`. Releases are only for `.mrpack` and zip files.
* **GitHub Pages.** The packwiz docs suggest it. It works, but it serves one deployment. Several channels mean deploying into subfolders, which is more moving parts than raw URLs.

### 2.2 Tested live

All returned HTTP 200 with the correct content:
* `raw.githubusercontent.com/<o>/<r>/<tag>/…`, including tags with a slash (`dist/26.5.1`) and tags with a `+` (`3.4.3+1.19`);
* the explicit forms `…/refs/tags/<tag>/…` and `…/refs/heads/<branch>/…`;
* branch names with slashes (`fabric/1.20.2/modrinth/main`);
* a full 40-character commit SHA.

The explicit `refs/tags/…` and `refs/heads/…` forms avoid ambiguity when a branch and a tag share a name.

packwiz-installer accepts any http(s) URL. It resolves `index.toml` and the metafiles relative to the folder of `pack.toml` (`Main.kt`: `HttpUrlPath(url.resolve("."), lastSegment)`). Tag and SHA URLs therefore work unchanged.

### 2.3 Caching and other limits

* **raw.githubusercontent.com** returns `cache-control: max-age=300` for *every* ref, measured: branch, tag and SHA alike.
  * For tags and SHAs this does not matter, because the content never changes.
  * For a branch, an instance may see an update up to about 5 minutes late. Each file is cached separately. Right after a push you can therefore get a new `pack.toml` with an old cached `index.toml`, or the reverse. packwiz-installer then stops with *"Your index file hash is invalid! The pack developer should packwiz refresh on the pack again"* (from `UpdateManager.kt`), or with "Hash invalid!" for one file. Wait a few minutes and launch again.
  * packwiz-installer itself does no HTTP caching: plain OkHttp, no cache.
* **Rate limits.** GitHub tightened limits for unauthenticated requests in May 2025, explicitly including `raw.githubusercontent.com` (changelog, no numbers given).
  * A first install fetches `pack.toml`, `index.toml`, every `.pw.toml` (about 230) and every config and datapack file from the raw host: several hundred requests. Later updates fetch only the files whose hash changed.
  * For one user this is normally fine. If you ever see HTTP 429, see the alternatives in the next bullet.
* **Alternatives:**
  * **jsDelivr** (`https://cdn.jsdelivr.net/gh/<o>/<r>@<tag>/<path>/pack.toml`): tags and commits are cached "effectively forever", branches for 12 hours, and semver ranges (`@1`) for 7 days with a purge API. Limit: 20 MB per file. Branches are too slow for dev, and semver ranges don't work with line-prefixed tags. So use it only as a tag mirror.
  * **raw.githack / rawcdn.githack**: the same idea.
  * **GitHub Pages** (about 10 minutes of cache).
  * **`packwiz serve`** on localhost for dev.
* **Private repos.** packwiz-installer cannot send credentials for the pack URL; `--bootstrap-update-token` only covers the installer's own self-update. Raw hosting therefore requires a **public** repo. GitHub Pages from a private repo requires a paid plan.

### 2.4 Cleanest scheme for dev, stable and frozen instances

| Instance | Points to | Notes |
|---|---|---|
| **dev / test** | `packwiz serve` on your PC (`http://localhost:8080/pack.toml`), or `refs/heads/main/...` | `serve` refreshes the index on every request and needs no push. `main` means "latest pushed", with up to 5 minutes of lag. |
| **real world** | `refs/tags/<line>-v<x.y.z>/...` | You upgrade deliberately: back up the world, edit the tag in Prism, launch. Simplest option; nothing moves on its own. |
| real world, auto-follow variant | `refs/heads/stable-<line>/...` | A *pointer* branch that CI force-moves to each release commit (`git push origin +$GITHUB_SHA:refs/heads/stable-1.21.1`). Nobody commits to it, so there is none of the merging a main/stable split brings. Better than moving a tag: tags are expected to be immutable and git does not re-fetch moved tags. |
| **archive** | `refs/tags/<old tag>/...` or a commit SHA | Never changes. Add a GitHub **tag ruleset** blocking deletion or update of `*-v*`, so these URLs cannot break. |

---

## 3. packwiz-installer behaviour (read from the v0.5.14 source)

### 3.1 Minecraft and loader version: it tries, but current Prism defeats it

* `LauncherUtils.handleMultiMC()` reads `../mmc-pack.json`, the instance folder Prism shares with the MultiMC format. It compares `net.minecraft`, `net.neoforged` and the other loaders with `[versions]` in `pack.toml`.
* If they differ, it shows the dialog "Updating MultiMC versions" with **Cancel / Continue anyways / Update**. On *Update* it rewrites `mmc-pack.json`. So the claim "it never touches the version" is not quite right.
* **However, in Prism** the pre-launch command runs *after* Prism has loaded the instance components. Order in `MinecraftInstance::createLaunchTask`:
  1. pre-load command, which is new;
  2. `MinecraftLoadAndCheck`;
  3. Java checks;
  4. **pre-launch command**;
  5. update tasks;
  6. launch.
* Prism issue #3944 ("Instance update over pre command no longer works", from 9.4 on) reports that edits made there are ignored and *"overridden on minecraft exit"*. A maintainer explains that the version must be loaded before pre-launch, for Java selection.
* **Practical rule:** set Minecraft 1.21.1 and the NeoForge version by hand in each instance so they match `pack.toml`. When packwiz-installer shows that dialog after a NeoForge bump:
  1. press **Cancel**: the installer exits 1 and Prism aborts the launch;
  2. change NeoForge in the instance's Version tab;
  3. launch again.
* Prism `develop` gained a **"Pre-Load command"** (PR #6041, merged 2026-09-10). It runs *before* metadata loading, *"so this can help users to run a script that changes the Minecraft version before the meta is loaded."* It is not yet in a tagged release; 11.1.1 is the latest. Once it ships, moving the packwiz command there should make loader bumps apply by themselves.
  * Caveat: `$INST_JAVA` comes from the instance's Java path setting. On a brand-new instance where Prism hasn't picked Java yet, it may be empty.
* **Pre-launch details** from the Prism source:
  * the command runs with working directory = the instance's `minecraft/` folder (`setWorkingDirectory(gameRoot())`). That is why the relative `packwiz-installer-bootstrap.jar` works. The Prism wiki says "launcher's working folder", but the code says otherwise;
  * it is run directly, **not through a shell**, so `|| true` and similar do not work;
  * a non-zero exit **aborts the launch**;
  * variables: `$INST_JAVA`, `$INST_MC_DIR`, `$INST_DIR`, `$INST_NAME`, `$INST_ID`.

### 3.2 Files

* **Local edits survive.** A file in the index counts as up to date when its hash in the index equals the hash cached in `packwiz.json`; the disk is not re-checked (`DownloadTask.updateFromCache`). So your edits to a pack-managed config survive **until the pack ships a new version of that file**, which then overwrites them. A missing file is re-downloaded.
* **`preserve = true`** on an `index.toml` entry means "install only if missing, never overwrite" (`DownloadTask.download`). Use it for `options.txt` and other files you tune in-game. There is no CLI flag: edit `index.toml` by hand. `packwiz refresh` keeps the flag, because entries are updated in place.
  * The alternative is a defaults mod (Additive uses `config/modpack_defaults`, Feather uses `config/yosbr`).
* **Mods removed from the pack** are deleted, but only files the installer itself had installed (tracked in `packwiz.json`). Mods or files you added by hand are never touched.
* **Gotchas in Prism:**
  * Disabling a mod in Prism's Mods tab renames it to `.disabled`. The installer sees the file "missing" and re-downloads it on the next launch; its source says "TODO: add .disabled support". Use packwiz optional mods (`[option] optional = true`) instead.
  * Prism's own mod updater creates duplicates, because the old file name is "missing" and gets re-downloaded. Don't use Prism's mod management in packwiz-managed instances.
* **Switching URLs** (dev to tag, tag to older tag) is fine: the installer reconciles by hash, including downgrades. The installer never touches worlds, but downgrading a world's mods is Minecraft's own risk. Give archive instances their own worlds.

### 3.3 Side

* The default is `-s client`. It installs `side = client` and `both`, and skips `server`.
* packwiz maps Modrinth environments carefully (`modrinth.go getSide`): `server_only` becomes `both`, because it *"also works in singleplayer"*; only `dedicated_server_only` becomes `server`. So single player is mostly safe.
* Still run `packwiz list -s server` once. Anything listed there will **not** be installed in a client instance; set it to `both` if you need it in single player.

### 3.4 CurseForge mods with third-party distribution disabled

* The installer asks the CurseForge API for download URLs. When `downloadUrl` is null, it shows an error per mod: *"This mod is excluded from the CurseForge API and must be downloaded manually. Please go to <url> and save this file to <absolute path>"*.
* Save the file there and choose Continue. The installer re-validates by hash and accepts it, and caches it in `packwiz.json`. You are asked again only when that mod's version changes.
* This happens **once per instance**: dev, real and each archive instance.

### 3.5 Local install

* Yes, from a local file. `Main.kt` accepts `http(s)://`, `file:` URIs and plain file paths.
* With a file path the index must be up to date, so run `packwiz refresh` first. `packwiz serve` refreshes for you on each request (`-p` sets the port, `--basic` turns off refreshing).
* **Flatpak Prism** (likely on Bazzite) has no filesystem access outside the sandbox apart from `xdg-download:ro`, according to the Flathub manifest. A path into your git checkout won't be readable without `flatpak override --user --filesystem=<dir>:ro org.prismlauncher.PrismLauncher`. `packwiz serve` on localhost works without that, since the network is shared.

### 3.6 Other behaviour

* **Bootstrap self-update:** on every launch the bootstrap calls `api.github.com/repos/comp500/packwiz-installer/releases/latest` (60 requests per hour unauthenticated). `--bootstrap-no-update` skips the call, but the `packwiz-installer.jar` must already be present from an earlier run.
* **Offline:** in GUI mode a failed `pack.toml` download offers "Continue without updating", which exits 0 so the game starts. With `-g` (no GUI) the launch fails. Keep the GUI on for client instances.
* **Changing side** (`-s`) invalidates and re-checks everything.

---

## 4. GitHub Actions

### 4.1 What existing packs use

* **Installing packwiz.** packwiz has **no tagged releases**. Options:
  * `go install github.com/packwiz/packwiz@<commit>`: jimsimon pins a commit "since the commit is the only reproducible pin"; Additive and Feather use `@latest`;
  * `actionhippie/install-packwiz@v1`/`v2`, which downloads the nightly.link build of `main` (CobbleCreations uses it);
  * the CI artifact of the packwiz repo (FO);
  * a fork's static release (Create: Astral uses `The-Shortman/packwiz`).
* **Validation** (jimsimon `validate.yml`): on push and PR, run `packwiz refresh`, fail if the committed index differs, and export every pack as an artifact.
* **Release on tag** (jimsimon `release.yml`): parse `<pack>-v<version>`, check it matches the `pack.toml` version, `packwiz modrinth export`, then `gh release create <tag> dist/*.mrpack --notes-file …`.
  * FO exports from `Packwiz/${MC_VERSION}` and publishes with `Kira-NT/mc-publish` (formerly Kir-Antipov) plus build-provenance attestation.
  * Create: Astral uses `softprops/action-gh-release`, caches `~/.cache/packwiz/cache` with `actions/cache`, and builds a server pack by running `packwiz-installer-bootstrap.jar -g -s server ../pack.toml` in CI.
  * Feather uses a matrix over platforms with `git-cliff` changelogs.
  * mc-modpack-kit uses release-please with `monorepo-tags` and a matrix over folders.
* **`dist` branch pattern** (Additive): keep `no-internal-hashes = true`, which avoids hash merge conflicts with several contributors. CI runs `packwiz refresh --build` into a `dist` branch and tags `dist/<tag>`. Not needed for a single author: just commit the refreshed index.

### 4.2 CurseForge-only mods in exports (from packwiz `modrinth/export.go`)

* An entry goes into the `.mrpack` as a *download URL* only if it is a URL-mode mod. CurseForge metadata-mode mods (`mode = "metadata:curseforge"`) are **always downloaded by packwiz and embedded as jars** in `overrides/` (or `client-overrides/`, `server-overrides/`). packwiz prints a licensing disclaimer when it does this.
* `--restrictDomains` (default `true`) only affects URL-mode mods. With `true`, URL mods whose host is not `cdn.modrinth.com`, `github.com`, `raw.githubusercontent.com` or `gitlab.com` get embedded. With `false` they stay as URLs, which Prism accepts but Modrinth's site would reject. **It does not change anything for CurseForge mods.**
* If a CurseForge mod has distribution disabled, the export prints "Found N manual downloads…", lists them, and **exits 1**. To continue you put the jars in the packwiz cache import folder: on Linux `~/.cache/packwiz/cache/import`, or `cache.directory` if configured.
  * In CI that folder is empty, so the export fails. You cannot commit those jars to a public repo.
* `packwiz curseforge export` is the mirror image: Modrinth mods get embedded as jars and need CurseForge staff approval. It is useless for this setup.
* **Consequence:**
  * A public GitHub Release with a full `.mrpack` would redistribute up to 6 CurseForge jars; if their distribution is disabled, CI could not build it at all.
  * In CI, export a **"Modrinth-only" `.mrpack`**: copy the pack to a temp dir, delete the `.pw.toml` files containing `metadata:curseforge`, refresh, export. Attach the list of excluded CurseForge mods to the release.
  * Or build the full `.mrpack` locally only, as a private backup.

---

## 5. Where non-pack material lives

* **packwiz indexes only files under the folder containing `pack.toml`.**
  * Built-in ignores (`core/index.go`): `.git/**`, `.gitattributes`, `.gitignore`, `.DS_Store`, `/*.zip`, `*.mrpack`, `packwiz`, `packwiz.exe`.
  * Anything else inside the pack root is shipped. jimsimon's README: *"Every file in the pack directory that is not a .pw.toml ships as an override, so list docs … in .packwizignore."*
* **Pack root = repo root** (Create: Astral, Cobbleblock, CobbleCreations, Grand Expanse): docs, scripts and art live in the same tree and are excluded through `.packwizignore`.
  * Create: Astral excludes `/README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `.github`, `.vscode`, `flake.nix`, scripts…
  * Cobbleblock excludes `**.md`, `scripts`, `reference_data`, `working_notes.txt`, `dev_mods`; it also generates datapack JSON with TypeScript scripts.
  * CobbleCreations excludes `project_files`, `assets`.
* **Pack root in a subfolder** (FO, Additive, jimsimon, Feather): docs and tools sit next to the pack folders and need no ignore rules. This is safer: you cannot accidentally ship a docs file.
* No pack I looked at keeps docs in a **separate** repo.
* Recommended `.gitattributes`: `* -text`, or at least `<line>/pack/** -text` as FO does (`Packwiz/** -text`). This stops line-ending conversion, which would change hashes on Windows.
* **Datapack via Paxi:**
  * Paxi loads from `config/paxi/datapacks/` either a `.zip` **or a folder containing `pack.mcmeta`** (`PaxiRepositorySource`: `isValidPackFolder = isDirectory && pack.mcmeta`).
  * So the datapack *source folder can live directly inside the pack* at `config/paxi/datapacks/<name>/`. No build step: packwiz indexes each file, and the installer adds, updates and deletes them one by one.
  * Downside: many files mean many raw requests on first install.
  * If you generate JSON with scripts, keep the generator outside the pack root and commit the generated output into the pack folder. Raw hosting serves only what is committed.

---

## 6. Public repo: downsides and checks

* **Mod licences.** packwiz metadata contains only IDs, file names, hashes and CDN URLs, never jars. Public packwiz repos are normal practice; FO's DEVELOPER-README: *"this repo will not include JAR files of any kind to respect the modders."*
  * Never commit jars.
  * Never publish a Prism instance export, or an `.mrpack` with embedded CurseForge jars, unless the licences allow it (packwiz docs link Modrinth's "Obtaining modpack permissions").
  * Shipping mod config files is generally accepted.
* **Datapack and docs.**
  * Add a LICENSE for your own content (e.g. MIT for datapack and scripts, CC BY 4.0 for docs). Cobbleblock's README clarifies that the licence covers only original content.
  * Credit anything copied or derived from other datapacks or mods (recipes or loot tables lifted from mod jars, textures, etc.) and check those licences.
* **Privacy.** Use the GitHub no-reply commit email. Don't commit `saves/`, `logs/`, `screenshots/`, `servers.dat`, `usercache.json` or `options.txt` with personal paths. Research notes become public too.
* **Upsides of public.** Raw hosting needs it. Actions minutes on standard runners are free for public repos.
* **Protection.** A tag ruleset on `*-v*` (no deletion, no update) protects the archive URLs.

---

## 7. Recommendation for this case

### 7.1 Tree

```
modpack/                                (public GitHub repo)
├── README.md                           what it is + table of lines/instances + install steps
├── LICENSE                             own content (datapack, scripts; docs e.g. CC BY)
├── .gitattributes                      * -text
├── .gitignore                          dist/  *.mrpack  *.zip  packwiz  packwiz.exe
├── docs/                               cross-version docs (conventions, workflow, decisions)
├── scripts/                            helper scripts (refresh-all, release, datapack generators…)
├── .github/workflows/
│   ├── check.yml                       push/PR: packwiz refresh in every */pack + git diff --exit-code
│   └── release.yml                     tag <line>-v<ver>: .mrpack (Modrinth-only) + docs zip → GitHub Release
└── 1.21.1/                             one folder per Minecraft "line" (later 1.21.x, 26.x …)
    ├── docs/                           this line's Italian design/research docs (context.md, verifica-versioni…)
    └── pack/                           ← packwiz root
        ├── pack.toml                   [versions] minecraft = "1.21.1", neoforge = "21.1.x"; version = "0.5.0"
        ├── index.toml                  (committed, refreshed; preserve = true on options.txt if shipped)
        ├── .packwizignore              (only if you ever put notes inside pack/)
        ├── mods/*.pw.toml              ~230 Modrinth + 6 CurseForge metafiles
        ├── config/…  defaultconfigs/…
        ├── config/paxi/datapacks/<datapack>/   datapack source = shipped files (pack.mcmeta, data/…)
        └── resourcepacks/…
```

Why this layout:
* It gives you "one container per MC version" without a second repo.
* Docs for a line sit next to that line's pack, while shared docs, scripts and CI exist once.
* Nothing outside `*/pack/` can leak into the pack.
* When a line dies you either leave it or `git mv` it to `archive/`. Tag URLs keep working; only `main` URLs would break, and nothing should follow `main` for a dead line.

### 7.2 Tags, branches and releases

* **Work on `main` only.** Commit freely; the dev instance follows it. Use short-lived feature branches if you like, but no permanent `stable` branch.
* **Release steps:**
  1. Bump `version` in `1.21.1/pack/pack.toml`, run `packwiz refresh`, commit.
  2. Tag `1.21.1-v0.5.0` and push the tag.
* The release workflow then:
  1. checks the tag version against `pack.toml`;
  2. installs packwiz pinned to a commit;
  3. restores `~/.cache/packwiz/cache`;
  4. checks with refresh plus `git diff --exit-code`;
  5. exports a Modrinth-only `.mrpack` with the CurseForge mods removed in a temp copy, and writes their list;
  6. zips `docs/` and `1.21.1/docs/`;
  7. runs `gh release create`;
  8. optionally force-moves `stable-1.21.1` to this commit, for an auto-follow real instance.
* Release notes: `--generate-notes` or a CHANGELOG section.
* Add a tag ruleset protecting `*-v*`.

Release workflow outline (adapt names):

```yaml
on: { push: { tags: ['*-v*'] } }
permissions: { contents: write }
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - id: t
        run: |
          [[ "$GITHUB_REF_NAME" =~ ^(.+)-v([0-9].*)$ ]] || exit 1
          echo "line=${BASH_REMATCH[1]}" >> "$GITHUB_OUTPUT"; echo "ver=${BASH_REMATCH[2]}" >> "$GITHUB_OUTPUT"
      - uses: actions/setup-go@v5
        with: { go-version: stable }
      - run: go install github.com/packwiz/packwiz@<pinned-commit> && echo "$(go env GOPATH)/bin" >> "$GITHUB_PATH"
      - uses: actions/cache@v4
        with: { path: ~/.cache/packwiz/cache, key: "pw-${{ hashFiles('*/pack/index.toml') }}", restore-keys: pw- }
      - env: { LINE: "${{ steps.t.outputs.line }}", VER: "${{ steps.t.outputs.ver }}", GH_TOKEN: "${{ github.token }}" }
        run: |
          set -euo pipefail
          grep -q "^version = \"$VER\"" "$LINE/pack/pack.toml"
          (cd "$LINE/pack" && packwiz refresh) && git diff --exit-code
          mkdir dist; tmp=$(mktemp -d); cp -r "$LINE/pack/." "$tmp"
          (cd "$tmp" && grep -l 'metadata:curseforge' mods/*.pw.toml | tee "$GITHUB_WORKSPACE/dist/curseforge-mods-to-add-manually.txt" | xargs -r rm \
             && packwiz refresh && packwiz modrinth export -o "$GITHUB_WORKSPACE/dist/Modpack-$LINE-$VER-modrinth-only.mrpack")
          zip -r "dist/docs-$GITHUB_REF_NAME.zip" docs "$LINE/docs"
          gh release create "$GITHUB_REF_NAME" dist/* --title "$LINE v$VER" --generate-notes
          # optional: git push origin "+$GITHUB_SHA:refs/heads/stable-$LINE"
```

### 7.3 Prism instances and their pre-launch commands

**Setting up an instance:**
1. In Prism, create the instance with **Minecraft 1.21.1 + NeoForge = `[versions] neoforge` of the target ref**.
2. Put `packwiz-installer-bootstrap.jar` (v0.0.3) in the instance's `minecraft/` folder.
3. Go to Edit Instance → Settings → Custom commands and set the pre-launch command.
4. For the next instance, use "Copy instance" and change only the URL (and the NeoForge version if it differs).

**Command per instance** (`OWNER/REPO` = your repo):

| Instance | Pre-launch command |
|---|---|
| **dev, local** (run `packwiz serve` in `1.21.1/pack` first) | `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar http://localhost:8080/pack.toml` |
| **dev, pushed work** | `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/OWNER/REPO/refs/heads/main/1.21.1/pack/pack.toml` |
| **real world** (pinned; upgrade = back up the world, edit the tag) | `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/OWNER/REPO/refs/tags/1.21.1-v0.5.0/1.21.1/pack/pack.toml` |
| real world, auto-follow variant | `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/OWNER/REPO/refs/heads/stable-1.21.1/1.21.1/pack/pack.toml` |
| **archive** (frozen) | `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar --bootstrap-no-update https://raw.githubusercontent.com/OWNER/REPO/refs/tags/1.21.1-v0.3.0/1.21.1/pack/pack.toml` |

Notes for the archive row:
* Run the first launch without `--bootstrap-no-update`, so `packwiz-installer.jar` gets downloaded.
* A commit SHA can replace `refs/tags/…`.
* For a truly offline archive, delete the pre-launch command after the first full install. Keep a local Prism export of the instance with its jars as a private backup, in case mod files ever disappear from the CDNs.

The URL is the only thing that differs between the instances. In the local dev variant the installer reads your working copy on every launch. If `packwiz serve` isn't running, the dialog offers "Continue without updating".

### 7.4 Is "one repo per MC version" useful?

Mostly unnecessary here:
* **What it would give you:**
  * plain `v0.5.0` tags;
  * a separate Releases and issues page per line;
  * GitHub's "Archive repository" switch.
* **Why you don't need it:**
  * Every one of your three instance needs (dev, vetted, frozen) is solved by refs: branch, tag, SHA. That works the same in one repo.
  * A new MC version already means a new Prism instance, because Prism won't take the version switch from packwiz-installer.
  * Separate repos duplicate the shared docs, scripts, CI and README.
* **Comparison with the alternatives:**
  * Folder per line in one repo is what FO and Additive/Adrenaline (multi-version packs used by many people) do.
  * Branch per line (Venture, Cabricality, Tinkerer's Quilt) suits packs that maintain several versions in parallel and port fixes with cherry-picks. You don't.
* The folder layout above keeps each line self-contained (`1.21.1/docs` + `1.21.1/pack`). If you ever do want a separate repo, `git filter-repo --subdirectory-filter 1.21.1` (or `git subtree split -P 1.21.1`) extracts it with its history. Starting with one repo is the reversible choice.

---

## Sources

* packwiz docs:
  * [packwiz-installer tutorial](https://packwiz.infra.link/tutorials/installing/packwiz-installer/)
  * [additional options](https://packwiz.infra.link/reference/additional-options/) (`no-internal-hashes`, `datapack-folder`, `acceptable-game-versions`)
  * [Modrinth export](https://packwiz.infra.link/tutorials/hosting/modrinth/)
  * [CurseForge export](https://packwiz.infra.link/tutorials/hosting/curseforge/)
  * [git](https://packwiz.infra.link/tutorials/creating/git/)
  * docs source: [packwiz/packwiz-website](https://github.com/packwiz/packwiz-website)
* packwiz source, [packwiz/packwiz](https://github.com/packwiz/packwiz) (main @ 170b22d, 2026-10-14): `modrinth/export.go` (restrictDomains and embedding), `cmdshared` (manual downloads, disclaimer), `core/index.go` (default ignores), `core/indexfiles.go` (preserve), `core/storeutil.go` (cache path), `modrinth/modrinth.go` (`getSide`)
* packwiz-installer source, [packwiz/packwiz-installer](https://github.com/packwiz/packwiz-installer) v0.5.14: `Main.kt`, `UpdateManager.kt`, `LauncherUtils.kt`, `DownloadTask.kt`, `metadata/curseforge/CurseForgeSourcer.kt`, `ui/gui/GUIHandler.kt`
* Bootstrap source: [packwiz/packwiz-installer-bootstrap](https://github.com/packwiz/packwiz-installer-bootstrap) (`Bootstrap.java`)
* Example pack: [packwiz/packwiz-example-pack](https://github.com/packwiz/packwiz-example-pack) (`.gitattributes`, `.gitignore`, `.packwizignore`)
* Packs:
  * [Fabulously Optimized](https://github.com/Fabulously-Optimized/fabulously-optimized)
  * [Additive](https://github.com/skywardmc/additive)
  * [Adrenaline](https://github.com/skywardmc/adrenaline)
  * [Create: Astral](https://github.com/Laskyyy/Create-Astral)
  * [Create: Grand Expanse](https://github.com/Aiz0/create-grand-expanse)
  * [Cabricality](https://github.com/DM-Earth/Cabricality)
  * [Venture](https://github.com/steves-underwater-paradise/venture)
  * [Tinkerer's Quilt](https://github.com/sleepingdragoninn/tinkerers-quilt)
  * [CobbleCreations](https://github.com/LilydevMC/CobbleCreations)
  * [Cobbleblock](https://github.com/lucyawrey/cobbleblock)
  * [jimsimon/minecraft-modpacks](https://github.com/jimsimon/minecraft-modpacks) (Cobblemon)
  * [mc-modpack-kit](https://github.com/jh-devv/mc-modpack-kit)
  * [Feather](https://github.com/SamLolo/Feather)
  * [PackWize](https://github.com/Alfakynz/PackWize)
  * [GitHub topic: packwiz](https://github.com/topics/packwiz)
* Actions: [actionhippie/install-packwiz](https://github.com/actionhippie/install-packwiz), [Kira-NT/mc-publish](https://github.com/Kira-NT/mc-publish), [softprops/action-gh-release](https://github.com/softprops/action-gh-release)
* Prism:
  * [Custom commands wiki](https://prismlauncher.org/wiki/help-pages/custom-commands/)
  * source: `launcher/minecraft/MinecraftInstance.cpp` (`createLaunchTask`, `getVariables`) and `launcher/launch/steps/LaunchCommand.cpp` in [PrismLauncher](https://github.com/PrismLauncher/PrismLauncher)
  * [issue #3944](https://github.com/PrismLauncher/PrismLauncher/issues/3944)
  * [PR #6041 pre-load command](https://github.com/PrismLauncher/PrismLauncher/pull/6041)
  * [Flathub manifest](https://github.com/flathub/org.prismlauncher.PrismLauncher)
* GitHub raw:
  * [raw caching discussion #46691](https://github.com/orgs/community/discussions/46691)
  * [2025 unauthenticated rate limits](https://github.blog/changelog/2025-05-08-updated-rate-limits-for-unauthenticated-requests/)
  * headers measured live: `cache-control: max-age=300` on branch, tag and SHA URLs
* jsDelivr: [README caching section](https://github.com/jsdelivr/jsdelivr), [GitHub usage](https://www.jsdelivr.com/github)
* Paxi source: [YUNGNICKYOUNG/Paxi](https://github.com/YUNGNICKYOUNG/Paxi), `Common/.../PaxiRepositorySource.java` (zip or folder with `pack.mcmeta`)
* Modrinth: [Obtaining modpack permissions](https://support.modrinth.com/en/articles/8797527-obtaining-modpack-permissions)
