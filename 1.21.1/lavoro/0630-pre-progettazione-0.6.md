# Pre-progettazione della tappa 5 (0.6.x) — Minecraft 1.21.1

Documento vivo finché la tappa 5 non è finita. Prepara il lavoro: cosa c'è da fare, com'è oggi (ricontato il 19/10/2026 sull'inventario del pack), cosa deve decidere Matteo, in che ordine e come si prova. I formati dei file e i conti pianta per pianta restano in `0620-progetto-datapack.md` e `0621-copertura-vasi.md`; le config in `../docs/0302-config.md`; i problemi in `../docs/0402-bug-report.md`.

## 0. In breve

La tappa 5 ha otto parti (dal piano, `0501-piano.md`, più le correzioni degli artefatti), molto diverse per peso e rischio:

| Parte | Cosa | Peso | Tocca il mondo? |
|---|---|---|---|
| A. Every Compat | Meno blocchi e risorse generate una volta sola (B22, B33) | medio | **sì** se toglie blocchi |
| B. Artifacts | Config: solo Curios, niente Accessories | piccolo | **sì**: da fare prima del mondo vero |
| C. Altre config | Comodità decise in `0302` e paracadute di Jaden's | piccolo | no |
| D. Berserker (B02) | Un'etichetta nel datapack | piccolo | **sì**: solo strutture nuove |
| E. Artefatti (B01, B03) | 15 nomi vecchi da togliere, 8 casse tesoro da aggiungere, casse di Mowzie's e Born in Chaos | piccolo | no (vale per le casse non ancora aperte) |
| F. Esperienza | Valore del liquido di Cognition per Create, scambio nel Mescolatore | piccolo | no |
| G. Vasi | Circa 260 piante e 11 terreni | **grande** | no |
| H. Mercato | Semi e alberelli di una quindicina di mod | medio | no |

**Proposta** 🟢: dividere la tappa in tre versioni di prova, così ognuna si prova in fretta e un problema non blocca il resto:
- **0.6.0 — config e correzioni** (A–F): tutto quello che cambia il mondo, insieme, con un solo mondo nuovo di prova.
- **0.6.1 — vasi** (G): il lavoro più lungo, generato da uno script e rivisto mod per mod.
- **0.6.2 — mercato** (H): stesso metodo dei vasi, più piccolo.

Poi si passa alla tappa 6 (mondo di prova, poi 1.0.0). Le decisioni da prendere prima di cominciare sono raccolte nella sezione 9.

## 1. Stato verificato oggi

Ricontato il 19/10/2026 sull'inventario del pack (`../data/inventario/`, versione 0.5.3) e sui file del datapack.

| Parte | Com'è oggi |
|---|---|
| Every Compat | Config di serie: 10.733 blocchi (40,7% del pack), avvio da 51 a 78 secondi (B22). I suoi 12 moduli attivi sono tutti tra quelli da tenere (sezione 2). Rigenera le sue risorse a **ogni** ricaricamento (nel log: "REGEN_ON_EVERY_RELOAD"), anche dentro il gioco: è una delle cause probabili del crash per memoria finita (B33) |
| Artifacts | Config di serie: compatibilità sia con Curios sia con Accessories (slot doppi) |
| Berserker | L'etichetta `cataclysm:berserker_spawn` contiene solo `minecraft:fortress`; la fortezza di YUNG's (`betterfortresses:fortress`) esiste nell'inventario. Basta aggiungerla |
| Artefatti | 15 nomi di casse di When Dungeons Arise e Dungeons and Taverns (`nova_structures`) non esistono più (avvisi del controllo dei nomi): sono nomi vecchi di strutture che i nostri file coprono già con il nome nuovo; mancano invece 3 casse tesoro di When Dungeons Arise e 5 di Dungeons and Taverns (sezione 5). Mowzie's Mobs ha 2 tabelle di casse (`monastery_chest`, `umvuthana_grove_chest`); Born in Chaos ne ha 7, scritte con il namespace `minecraft` (`minecraft:chests/chest_level_1`…) |
| Esperienza | La tabella delle unità di Create: Enchantment Industry esiste (`create_enchantment_industry:unit/experience`): il nostro file si aggiunge a quella. Il liquido di Cognition è `cognition:cognitium_source` (lo conferma la sua etichetta `c:experience`). Supplementaries ha un suo tipo di liquido "esperienza" (per i barattoli), non nell'etichetta `c:experience`: da capire se conta |
| Vasi | Delle 526 piante contate il 17/10: **263 coperte** (nessuna in più nel frattempo), **254 scoperte** (comprese le 17 di Regions Unexplored: 9 mai coperte e 8 coperte solo con i nomi vecchi), **9 da chiarire** (sotto). Fuori dal conto del 17/10: **4 piante di Jaden's** e **2 di Nether Depths Upgrade**. Terreni: **11 da aggiungere**, più quelli facoltativi di Aether e Deep Aether |
| Mercato | Le voci delle mod del pack sono quelle già contate in `0620` (FD 15, Twilight 12, Ars 6, Cultural/Expanded/Rustic 3, My Nether's 2, Supplementaries 1, Create 1). Nessuna voce per una quindicina di mod, più Jaden's, Nether Depths e Roaster's |

Le 9 piante da chiarire:
- **Roaster's Delight** (5): il sorgente è chiuso, ma ora l'inventario legge i nomi dal file: `roasters_delight:coffee_plant`, `tea_bush`, `chamomile_crop`, `mint_crop`, `matcha_crop`. Problema risolto, restano da scrivere.
- **Bountiful Fares** (3): sambuco, lapisberry e frutto della passione crescono **sul graticcio** (un blocco con la pianta come proprietà), non come blocchi propri. Il vaso "deriva" la pianta da un blocco: va capito se si può fare (altrimenti si escludono).
- **Fagioli magici** di Twilight Forest: esclusi apposta (non adatti ai vasi).

## 2. Every Compat (parte A)

Verificato nel sorgente di Every Compat 2.11.54 (la versione del pack) il 19/10/2026.

**Correzione al piano.** I 12 moduli attivi nel pack (Create, Farmer's Delight, Friends & Foes, Handcrafted, Macaw's ×4, Rechiseled, Regions Unexplored, Storage Drawers, Twilight Forest) sono **tutti** nell'elenco da tenere di `0302`, e un modulo per Botany Pots non esiste. "Spegnere i moduli che non servono" quindi non toglie niente: B22 si riduce solo con le leve qui sotto.

| Leva | File e chiave | Effetto | Proposta |
|---|---|---|---|
| Varianti "connecting" di Rechiseled | `config/everycomp-hazardous.toml`, `[entryset] blacklist = ["rechiseled:.*_connecting"]` | Il modulo di Rechiseled crea 111 blocchi per ogni legno, 54 sono le varianti con le texture collegate: circa metà del modulo, quindi circa 1.000 blocchi in meno su 2.183 (stima) | 🟡 decidi tu: le varianti collegate ti servono per costruire? |
| Legni di singole mod | stesso file, `[woodtype] blacklist` (espressione sul nome del legno) | Toglie tutti i blocchi di quel legno, in tutti i moduli | 🟡 solo per legni che non userai mai |
| Generazione delle risorse | `config/everycomp-client.toml` `dynamic_assets_generation_mode` e `config/everycomp-common.toml` `server_assets_generation_mode`, di serie `ALWAYS` | `ALWAYS` rifà texture e modelli a **ogni** ricaricamento delle risorse, anche con F3+T: probabile causa di B33. `RUN_ONCE`: una volta per avvio. `CACHED`: salva su disco e rifà solo quando cambiano le mod; ma dopo ogni modifica alla config di Every Compat vanno cancellate a mano due cartelle della cache dell'istanza | 🟢 `RUN_ONCE`; 🟡 `CACHED` se si vuole anche un avvio più veloce |
| Etichette per tipo di blocco | `everycomp-common.toml` `generate_blocktype_tags = false` | Secondo la mod "rende il pack un po' più veloce" | 🔴 non toccare finché non si sa se qualche ricetta le usa |

Note:
- Solo il file `hazardous` toglie davvero i blocchi. `everycomp-entries.toml` li nasconde soltanto (schede e ricette) e non aiuta B22. Il file `hazardous` avverte "modpack makers DO NOT use it" pensando ai server con config diverse: nel single player non vale.
- Togliere blocchi va fatto **prima del mondo vero**; nel mondo di prova i blocchi tolti dovrebbero diventare aria (comportamento normale, non verificato).
- Da provare anche l'effetto di `RUN_ONCE` su B30 (ricette delle finestre di Create in un secondo mondo).
- Misure prima e dopo: tempo di avvio, numero di blocchi e ricette (B22), memoria dopo un F3+T (B33).

## 3. Artifacts e altre config (parti B e C)

Verificato nei sorgenti delle versioni del pack (o del ramo più vicino) il 19/10/2026.

**Regole dei file.** I file TOML di NeoForge possono essere parziali (le chiavi mancanti prendono il valore di serie), ma al primo avvio il gioco li "corregge" riscrivendoli, con un avviso nel log: conviene portare file **completi**. La base migliore sono i file che il gioco ha già generato nell'istanza di prova (serve il tuo permesso per leggere la cartella `config` dell'istanza). Nella 1.21.1 le config "server" sono globali, in `config/` (un mondo può sovrascriverle in `saves/<mondo>/serverconfig/`).

| Mod | File | Chiave | Di serie | Proposta | Decisione |
|---|---|---|---|---|---|
| Artifacts | `config/artifacts/general.toml` | `[slots] enableAccessoriesCompat` / `enableCuriosCompat` | `true` / `true` | `false` / `true` (serve un riavvio) | presa (`0302`) |
| Carry On | `config/carryon-common.toml` | `[settings] pickupAllBlocks` | `false` | `true` | presa (`0302`) |
| Inventory Essentials | `config/inventoryessentials-common.toml` | `enableShiftDrag` | `true` | `false` (doppione di Mouse Tweaks) | presa (`0302`) |
| FallingTree | `config/fallingtree.json` | `sneakMode` | `SNEAK_DISABLE` (abbatte l'albero intero, accovacciati no) | `SNEAK_ENABLE`: abbatte l'albero intero **solo** da accovacciati | da prendere |
| Traveler's Backpack | `config/travelersbackpack-server.toml` | `[server.backpackSettings] allowShulkerBoxes` | `false` | `true` se vuoi shulker box (e forse zaini Sophisticated) dentro | da prendere |
| Jaden's Nether Expansion | `config/netherexp-common.toml` | `[worldSettings] netherWorldGenOverhaul`, `improvedNetherBiomeSource` | `true` | lasciare: è solo un paracadute | nessun file |
| Moog's Nether Structures | `config/moogs_structures.json` | `presets.mns.replace_nether_fortress` | `false` | lasciare | nessun file |
| Cognition | `config/cognition-common.toml` | `AllowedFluids` | 6 liquidi d'esperienza di altre mod | lasciare (mai aggiungere il liquido di Create: `0303`) | nessun file |
| Subtle Effects, Sound Physics | client | increspature della pioggia, qualità del suono | — | solo se in gioco danno problemi | — |

I **tasti** in conflitto (B, C) non sono config delle mod ma di Minecraft (`options.txt`): restano fuori dal pack, tema in `0503-temi-aperti.md`.

## 4. Berserker (parte D, B02)

- File: `data/cataclysm/tags/worldgen/structure/berserker_spawn.json` con `{"replace": false, "values": ["betterfortresses:fortress"]}` (formato in `0620`, sezione 5). Senza YUNG's la voce non esiste: va scritta con `"required": false`, come le altre etichette del datapack.
- Effetto solo sulle fortezze **generate dopo**: per provarla serve un mondo nuovo o un Nether non ancora esplorato.
- Prova: `/locate structure betterfortresses:fortress`, entrare, aspettare la comparsa dei Berserker infuocati.

## 5. Artefatti nelle casse (parte E, B01 e B03)

I file sono in `config/paxi/datapacks/matteo_tweaks/data/matteo_tweaks/loot_modifiers/artifacts/` (15 file, uno per livello di rarità: readme nella cartella).

**B01, nomi sbagliati: in realtà sono nomi vecchi.** Ricontrollati sull'inventario, quasi tutti i 15 nomi corrispondono a strutture che i nostri file coprono **già** con il nome nuovo: per esempio il forte degli illager (`illager_fort/illager_fort_treasure`), il palazzo Shiraz, i templi abbandonato e infestato, le case e la miniera dei funghi, le torri dei banditi e di Thornborn sono già nei file. `desert_city_big` non ha più una struttura nella versione del pack. Quindi:
- i 15 nomi vecchi **si tolgono** (spariscono anche gli avvisi del controllo dei nomi);
- si **aggiungono** le casse "tesoro" che oggi non sono in nessun file: When Dungeons Arise `kisegi_sanctuary/kisegi_sanctuary_treasure`, `mechanical_nest/mechanical_nest_treasure`, `mining_complex/mining_complex_treasure`; Dungeons and Taverns (`nova_structures`) `ruin_loot_master`, `hamlet/hamlet_tresure`, `desert_ruins/desert_ruin_lesser_treasure`, `illager_hideout_lesser_tresure`, `shrine/shrine_lesser_treasure` (i nomi con "tresure" sono scritti così dalla mod);
- le tabelle `vault` (le ricompense dei blocchi "caveau" delle prove) restano fuori: non sono casse.

Copertura oggi: 40 tabelle di When Dungeons Arise e 41 di Dungeons and Taverns nei nostri file.

**B03, casse mancanti.** Aggiungere `mowziesmobs:chests/monastery_chest`, `mowziesmobs:chests/umvuthana_grove_chest` e le casse di Born in Chaos (`minecraft:chests/chest_level_1`, `_2`, `_3`, `basic_chest`…) al livello di rarità adatto. Per Born in Chaos va controllato che quei nomi siano davvero usati dalle sue strutture.

## 6. Esperienza (parte F)

Formati e regole in `0620`, sezione 4, e in `../docs/0303-note-tecniche.md` (Esperienza liquida: **mai** mescolare i liquidi per etichetta).
- **File 1**, unità di Cognition per Create: `data/create_enchantment_industry/data_maps/fluid/unit/experience.json` con `cognition:cognitium_source` = 20. Si aggiunge alla tabella di Create (che ha già Sophisticated e altre mod), senza sostituirla.
- **File 2 e 3**, Mescolatore nelle due direzioni: 50 mB del liquido di Create ↔ 1000 mB di cognitium (stesso valore: 50 punti). Condizioni: entrambe le mod caricate.
- **Da verificare prima**: capienza della bacinella del Mescolatore (1000 mB in uscita bastano?), se Supplementaries con il suo liquido "esperienza" va considerato.
- Prova: convertire una quantità esatta avanti e indietro e controllare che i punti tornino uguali; provare l'Experience Hatch.

## 7. Vasi (parte G, versione 0.6.1)

Formato, casi particolari e bilanciamento proposto in `0620`, sezione 2; tabella pianta per pianta in `0621`.

**Lavoro da fare**:
1. **Script generatore** (nuovo, `scripts/`): legge `../data/vasi/copertura.json` e l'inventario, scrive una ricetta per pianta con la sua condizione di caricamento (`bookshelf:block_exists`), i raccolti espliciti dove servono e i terreni. Rigenerabile quando una mod si aggiorna. Le 255 bozze del 17/10 sono il punto di partenza.
2. **Aggiornare il conteggio**: aggiungere a `copertura.json` le piante di Jaden's (zucca del dolore, torciafiore delle anime, viticci del crepuscolo, germogli cremisi) e di Nether Depths (alghe cremisi e distorte, che crescono nella lava: serve capire se Botany Pots ha un terreno di lava), i 5 nomi di Roaster's, i graticci di Bountiful Fares.
3. **Scrivere e controllare a gruppi** di mod (prima le Delight e i Let's Do, poi Aether, Undergarden, Unusual End, Twilight, Hexalia…), con il controllo dei nomi a ogni gruppo.
4. **Regions Unexplored**: provare in gioco se gli 8 nomi vecchi funzionano; se no, riscriverli.

**Prova in gioco** (`0620`, sezione 2.6): `/botanypots debug missing seeds`, `missing soils`, `check_crops` nel mondo di prova; il primo elenca anche le piante dimenticate.

## 8. Mercato (parte H, versione 0.6.2)

Formato in `0620`, sezione 3. Uno script genera una voce per seme e alberello delle mod senza voci, con una lista di esclusioni (piante rare o magiche, alberelli speciali). Prezzi: da decidere (sezione 9). Prova: aprire il mercato e controllare categorie e prezzi.

## 9. Decisioni da prendere

| # | Domanda | Proposta |
|---|---|---|
| 1 | Dividere la tappa in 0.6.0 (config e correzioni), 0.6.1 (vasi), 0.6.2 (mercato)? | 🟢 sì |
| 2 | Effetti nuovi della luna di sangue di EC2 (mostri più vicini, assedio di zombi ai villaggi): tenerli? | da decidere (oggi attivi) |
| 3 | Vasi: tempi di crescita di serie, raccolti uguali a quelli a mano, nessuna scorciatoia per piante rare (`0620`, 2.4) | 🟢 come proposto |
| 4 | Vasi: graticci di Bountiful Fares e alghe di lava di Nether Depths, se servono soluzioni particolari | 🟡 includerle solo se il formato standard funziona |
| 5 | Mercato: prezzo unico di 1 smeraldo, o più caro per piante di altre dimensioni (Aether, Undergarden, Nether, End)? | 🟡 1 smeraldo base, 2 per le altre dimensioni |
| 6 | Artefatti: aggiungere solo la cassa "tesoro" delle strutture mancanti, come per le altre? | 🟢 sì |
| 7 | Every Compat: togliere le varianti "connecting" di Rechiseled (circa 1.000 blocchi)? Togliere i legni di qualche mod? | 🟡 decidi tu (sezione 2) |
| 7b | Every Compat: generare le risorse una volta per avvio (`RUN_ONCE`) invece che a ogni ricaricamento | 🟢 sì |
| 8 | FallingTree: albero intero solo da accovacciati? Traveler's: shulker box dentro lo zaino? | da decidere (sezione 3) |
| 9 | Permesso di leggere la cartella `config` dell'istanza di prova, per usare i file generati dal gioco come base | 🟢 sì, solo lettura |

## 10. Rischi

- **Every Compat**: togliere blocchi (varianti, legni) li cancella dal mondo. Nessun problema prima del mondo vero, ma dopo la 0.6.0 le liste nere non si toccano più a cuor leggero. Con la generazione `CACHED`, dimenticare di svuotare la cache dopo un cambio di config lascia risorse vecchie.
- **Vasi**: ricette sbagliate non danno errori evidenti (la pianta cresce ma non lascia niente): per questo serve `check_crops` in gioco.
- **Mercato**: un errore di prezzo o una pianta "rara" in vendita cambiano il bilanciamento: lista di esclusioni rivista da Matteo.
- **Aggiornamenti delle mod** durante la tappa: i nomi cambiano (come Regions Unexplored 0.6). Lo script generatore e il controllo dei nomi servono proprio a rifare il lavoro in fretta.

## 11. Fuori da questa tappa

Gli argomenti non ancora affrontati (achievement, difficoltà, tasti, aggiornamento generale delle mod…) stanno in `0503-temi-aperti.md`.
