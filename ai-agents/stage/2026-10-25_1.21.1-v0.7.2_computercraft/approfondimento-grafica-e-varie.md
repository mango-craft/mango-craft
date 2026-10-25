# Deep research (25/10/2026): Tom's Peripherals, Classic Peripherals, CC: Terminals

Raw report of a research agent (sources read, nothing run). Spot-checked by the main session: AP 0.8.2a Redstone Integrator commented out and `advancedperipherals:keyboard` item, Classic Peripherals `enderModemNerf = true`, Tom's `redstone_relay.json` recipe from `toms_peripherals:redstone_port`.

## Key findings
- AP 0.8.2a has **no Redstone Integrator** (`PeripheralsConfig.java` L208-212 commented; `BlockStatesAndModelsProvider.java` L44 commented; not in `APBlocks`). Multi-side redstone: CC:T **Redstone Relay** (`computercraft:redstone_relay`, full set incl. bundled — `RedstoneMethods.java` L28-143).
- AP 0.8.2a has a **Keyboard** item (`advancedperipherals:keyboard`, `APItems.java` L29): sneak + right-click to bind to a computer; opens an invisible screen sending keystrokes; no distance check found (`KeyboardItem.java`, `KeyboardContainer.java` L51-53).
- Sable Companion 1.6.0 (embedded in Classic Peripherals) is harmless and already in the pack (embedded by Create: Connected, Create Crafts & Additions, Psi, Slice & Dice, Supplementaries); MIT; without Sable it uses default code (`DefaultSableCompanion.java` L39-85).
- None of the three has Iris/Sodium code. All compatible on paper with NeoForge 21.1.259 and CC 1.120.2 (CC internals compared between build version and 1.120.2: unchanged).
- No world generation, no loot (except block drops), no structures.

## 1. Tom's Peripherals 1.21-1.3.1 (MIT)
- Blocks (`Content.java` L39-49): `toms_peripherals:gpu`, `monitor`, `wdt`, `redstone_port`, `keyboard`, `keyboard_dongle`. Items: `gpu_chip`, `gpu_chip_raw`, `laser_pointer`, `portable_keyboard`.
- `tm_gpu` (`GPUBlockEntity.java` L60): drives a wall of bitmap monitors, touching the bottom-left block; 16 px per block default, up to 64 with `setSize` (L339-340); wall up to 16×16 blocks (`maxScreenSize`; CC monitors 8×6); 24-bit colour; 2D (`BaseGPU.java`): `fill`, `filledRectangle`, `rectangle`, `line`, `drawText`, `drawTextSmart`, custom font, `drawImage`, `drawBuffer`, `createWindow`, `sync`; images: `decodeImage` (PNG), `newImage`/`newBuffer`, pixels, `saveImage`; 3D `createWindow3D` (`GPU3D.java` L40-288): OpenGL-1-style immediate mode in software (glBegin/glVertex/glTexCoord, matrices, textures, glFrustum, glDirLight); events `tm_monitor_touch`, `tm_monitor_<mouse event>`.
- `tm_wdt` (`WatchDogTimerBlockEntity.java` L33-112): `setEnabled`, `setTimeout` (≥20 ticks), `reset`; reboots the facing computer if not reset (`ComputerControl.java` L11-17). Not in CC or AP.
- `tm_rsPort`: full CC redstone set + `getSides`, absolute directions, event `tm_redstone`; recipes convert 1:1 to/from CC Redstone Relay → duplicate.
- `tm_keyboard` (`setFireNativeEvents`): real `key`, `char`, `paste` events; GUI can click CC advanced monitors and Tom's monitors; range 16 blocks (block), 64 (portable keyboard + dongle) (`KeyboardBlockEntity.java` L115-118); laser pointer clicks monitors up to 32 blocks.
- Jade/The One Probe tooltips for CC wired modems and the watchdog.
- Cost: raw GPU chip = 4 redstone, amethyst, 2 gold, copper, diamond, smelted; GPU = chip + iron + iron bars + redstone + copper; **each monitor block** = CC advanced monitor + 3 iron + redstone lamp + 3 glass panes.
- Config: `toms_peripherals-common.toml` (notice only); `serverconfig/toms_peripherals-server.toml`: `maxScreenSize` 16 (1–64), `maxVRAMSize` 16777216 — ignored, VRAM hardcoded 16 MiB (`GPUBlockEntity.java` L52, issue #45).
- Rendering: one block-entity renderer per monitor block, single quad `RenderType.entityTranslucent` on an in-memory texture (`MonitorBlockEntityRenderer.java` L43); world light, block light 12; no Iris/Sodium code; not skipped in shadow pass. Expected to work, not verified in game. Pixels not saved (update tag only): blank after reload until redrawn.
- Versions: NeoForge [21.0.0-beta,), computercraft `*`; built against CC 1.115.1; uses CC internals (`RedstoneUtil`, `BundledRedstone`, `ServerComputer.reboot`, …): identical in 1.120.2. Peripheral types `tm_*` unique.
- Maintenance: releases 1.2.2 (2024-07-21), 1.3.0 (2024-10-12), 1.3.1 (2026-05-17); last commit 2026-05-17; 18 open issues: #46 (Aug 2026, users say the author seems to have given up), #44 (official examples cube3d, cubeTex, gpuDraw draw nothing on NeoForge 1.21.1), #45 (VRAM config ignored), #35 (`drawText` background alpha quirk), #24 (GPU cannot connect to monitors above it), #28 (`refreshSize` needs `sleep(0)`); PR #43 waiting since June 2026.
- High Level Peripherals fork: 374 downloads, three releases 1.4.1–1.4.3 all on 2026-07-02, no source link; claims 32×32 blocks, 4096 px per block, ~2 GiB VRAM default, GLSL-like shader engine on the client → 🔴; mod id not verified (may clash with Tom's).
- Verdict: 🟡 (only for in-world graphics dashboards; test with shaders).

## 2. Classic Peripherals 0.6.5 (MIT; docs CC BY-SA 4.0)
- Blocks (`ModRegistry.java` L129-288): `classicperipherals:tower_base`, `tower_segment`, `tower_head` (radio tower, height 2–24), `antenna`, `nfc_reader`, `rfid_scanner`, `cryptographic_accelerator`, `cryptographic_accelerator_slim`, `scanner`. Items: `copper_coil`, `nfc_card`, `rfid_badge`. Peripherals `radio_tower`, `nfc_reader`, `rfid_scanner`, `cryptographic_accelerator`, `scanner`; turtle/pocket upgrades `radio`, `crypto`, `rfid`; pocket NFC API, `os.ban` short-range network; events `radio_message`, `nfc_data`, `nfc_write`, `nfc_sign`, `rfid_scan`.
- Radio `broadcast`, `setFrequency`…; NFC `write` (label, read-only, signing key), `sign`; RFID `scan` within 8 blocks (worn, injected into mobs, dropped); scanner reads CC printouts; crypto MD5/SHA/BLAKE3/HMAC, AES, Ed25519/X25519, base64, deflate.
- CC tweaks on by default via 7 mixins (`defaultRequire: 1`) into CC `WirelessNetwork`, `WirelessModemPeripheral`, `RedstoneRelayPeripheral`, `ComputerSystem` and vanilla `Entity`, `Item`, `LivingEntity`: **Ender Modem nerf** (range 2× wireless modem, cross-dimension only within 8 blocks after 1:8 scaling) — off with `enderModemNerf = false`; Redstone Relay `redstone` event gains the relay name.
- Config `config/classicperipherals.toml` (Kaleido; name from source): `enderModemNerf=true`, `enderModemRangeMultiplier=2`, `enderModemCrossDimensionalRange=8`, `betterRedstoneRelayEvent=true`, `radioTowerMaxHeight=24`, `radioTowerSegmentRange=128`, `radioTowerLossFactor=0.15`, `antennaCanBroadcast=true`, `rfidScanRange=8`, `nfcMaxDataSize=128`, `cryptographicRandomBytesMaxSize=65536`.
- Curios: `belt` slot file (size 1), `rfid_badge` in `curios:belt` (Relics already brings `belt`).
- Embedded: Sable Companion 1.6.0 (in pack), **new** BouncyCastle bcprov 1.78.1, Kaleido Config 0.3.3 (LGPL-3.0).
- Versions: NeoForge [21.1.228,), computercraft [1.120.0,), Curios optional. Very active (27 versions Oct 2025 – 2026-09-20); issues via Discord only.
- Verdict: 🔴 for this pack (🟡 with the nerf off if keycards wanted).

## 3. CC: Terminals 0.1.1 (MIT)
- Blocks `ccterminals:terminal_normal`, `terminal_advanced`; peripheral `terminal` (full CC `term` API via `TermMethods`); right-click opens a GUI (51×19 default); events `terminal_key`, `terminal_key_up`, `terminal_char`, `terminal_paste`, mouse events on advanced; ROM program `terminal <side> <program>`.
- Cost: CC monitor + button. Config `ccterminals-server.toml`: `term_sizes.terminal.width` 51, `height` 19 (1–255). Optional CC: Graphics ≥ 0.2.1.
- NeoForge [21.1,21.2), CC [1.117.0,); internals identical up to 1.120.2. NeoForge 0.1.1 file declares no dependencies on Modrinth. 2 releases (2026-04-15, 2026-08-02), 1 open issue (Fabric).
- Verdict: 🔴 not needed.
