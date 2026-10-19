# Every Compat (Wood Good) + Moonlight

Aggiornata il 19/10/2026 · nel pack dalla 0.4.0 (ruolo e licenza: `../docs/0301-mod.md`; versione: `../docs/0403-distinta-mod.md`) · fonti: sorgente di Every Compat (WoodGood @bdb551e8, versione 2.11.54) e di Moonlight (@1a3802e8, 3.7.2), inventario del pack, log dell'istanza di prova. Materiale grezzo: `../../ai-agents/stage/2026-10-19_1.21.1-v0.6.0_config-mod/`.

## Cosa fa nel pack

Crea le varianti (credenze, cassetti, tetti, finestre, blocchi cesellati…) di tutti i legni delle mod per 12 moduli: Create (finestre), Farmer's Delight (credenze), Friends & Foes (alveari), Handcrafted, Macaw's Roofs, Paths, Bridges e Windows, Rechiseled, Regions Unexplored, Storage Drawers, Twilight Forest. Sono esattamente i moduli decisi da tenere il 17/10 (`../lavoro/versioni/v0.2.3.md`); **un modulo per Botany Pots non esiste** (l'unico codice per Botany Pots riguarda le siepi di Quark, che non è nel pack). Every Compat 2.11.54 ha 64 moduli in tutto; altre mod possono registrarne tramite la sua API, nessuna nel pack lo fa.

## Peso (B22, B33)

- Con la config di serie crea **10.733 blocchi**, il 40,7% di tutti i blocchi del pack; il modulo più pesante è Rechiseled (2.183 blocchi). Avvio da 51 a 78 secondi, ricette da 22.123 a 28.026 (B22).
- Il modulo di Rechiseled crea 37 voci × 3 (blocco, lastra, scala) = **111 blocchi per ogni legno**; 54 sono le varianti `_connecting` (texture collegate): escluderle dimezza il modulo.
- Rigenera texture e modelli a **ogni** ricaricamento delle risorse, anche con F3+T dentro il gioco (nel log: "REGEN_ON_EVERY_RELOAD"): causa probabile del crash per memoria finita (B33).

## Config

| File | Lato | Chiave | Di serie | Note |
|---|---|---|---|---|
| `config/everycomp-hazardous.toml` | comune | `[module] blacklist` | `[]` | id esatto del modulo, es. `["rechiseled"]` |
| stesso | comune | `[entryset] blacklist` | `[]` | espressione su `modid:voce`, es. `"rechiseled:.*_connecting"` |
| stesso | comune | `[woodtype] blacklist`, `[leavestype] blacklist` | `[]` | espressione sul nome del legno, es. `"deep_aether:.*"` |
| stesso | comune | `[block] blacklist` | `[]` | espressione su `modulo/namespace del legno/blocco` |
| stesso | comune | `[other] include_all_wood_modules` | `true` | `false` spegne tutti i moduli |
| `config/everycomp-entries.toml` | comune | `[types.wood_type.<ns>]`, `[entries.wood_type.<modid>]` | tutto `true` | **nasconde soltanto** (schede e ricette): le risorse vengono generate lo stesso. Non aiuta B22 |
| `config/everycomp-client.toml` | client | `[general] dynamic_assets_generation_mode` | `ALWAYS` | `NEVER`, `RUN_ONCE`, `CACHED`, `CACHED_ZIPPED`, `ALWAYS` |
| `config/everycomp-common.toml` | comune | `[general] server_assets_generation_mode` | `ALWAYS` | stesse scelte; serve riaprire il mondo |
| stesso | comune | `[general] generate_blocktype_tags` | `true` | `false` "rende il pack un po' più veloce" (commento della mod); da capire se qualche ricetta usa quelle etichette |
| `config/moonlight-common.toml`, `moonlight-client.toml` | — | `multi_threaded_generation`, `faster_cache_search`, `merge_dynamic_resource_packs` | `true` | lasciare |

- Solo il file `hazardous` toglie davvero i blocchi (`EveryCompat.addModule`, `HardcodedBlockType`). Il file avverte "modpack makers DO NOT use it" pensando ai server con config diverse dal client: nel single player non vale.
- Togliere blocchi li cancella dal mondo (dovrebbero diventare aria: comportamento normale, non verificato nel sorgente). Va fatto **prima del mondo vero**.
- `RUN_ONCE` genera una volta per avvio e non rigenera con F3+T. `CACHED` salva in `dynamic-resource-pack-cache/` e `dynamic-data-pack-cache/` dell'istanza e rigenera solo quando cambia l'impronta (elenco delle mod con versioni più i resource pack): **le modifiche alla config di Every Compat non invalidano la cache**, quindi dopo ogni cambio vanno cancellate a mano le due cartelle. Moonlight non ha una strategia di cache propria.
- I file sono TOML di NeoForge: parziali ammessi, ma meglio completi (scheda `../theme-knowledge/neoforge.md`).

## Problemi

B22 (peso), B24 (48 traduzioni mancanti dei tronchi cavi di Twilight Forest), B25 (ricetta di Unusual End che cita una credenza non creata), B30 (ricette delle finestre di Create in un secondo mondo della stessa sessione), B33 (memoria finita dopo un ricaricamento): `../docs/0402-bug-report.md`.

## Storia nel pack

0.4.0 aggiunta con la config di serie (`../lavoro/versioni/v0.4.0.md`); 0.6.0 config (`../lavoro/versioni/v0.6.0.md`).
