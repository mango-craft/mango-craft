# Config del pack — Minecraft 1.21.1

Cosa fanno i file di configurazione del pack e quali impostazioni delle mod sono state decise. Documento vivo.

I file stanno in `pack/config/` e li installa packwiz-installer a ogni avvio dell'istanza (`../../docs/0101-installazione.md`). Prima del repository si copiavano a mano (storico in `../../ai-agents/stage/2026-10-16_pre-repo_pacchetti-mrpack/pacchetti-mrpack.md`).

## I file nel pack

| File | Cosa fa | Quando ha effetto | Stato |
|---|---|---|---|
| `config/almostunified/tags.json` | 19 tag personalizzati: rende intercambiabili gli ingredienti doppi tra le mod di cucina e magia (farina, impasto di grano, sale, mais, limone, porzioni di formaggio, formaggio di capra) | Al riavvio del gioco, in tutti i mondi | ✅ |
| `config/enhancedcelestials2core/translations.json` | Traduzioni di Enhanced Celestials 2: modalità `DISABLED`, cioè niente traduzioni scaricate dal sito dell'autore (con `AUTOMATIC`, che sembra il valore di serie, le scarica e le applica da sola) e nessuna richiesta di aiutare a tradurre. Senza il file la mod scrive in chat, a ogni ingresso nel mondo, di configurarle (B32). Nomi dei campi letti dal codice della mod. Per cambiare: `/ecc translate config` in gioco (la modifica resta finché il pack non porta una versione nuova del file) | Al riavvio del gioco | ✅ 0.5.2 |
| `config/artifacts/general.toml` | Artifacts solo con Curios: `enableAccessoriesCompat = false`, il resto di serie (file completo copiato dall'istanza). Va portato **prima di creare il mondo** | Al riavvio del gioco | 🔧 0.6.0: preparato, da provare |
| `config/carryon-common.toml` | Carry On prende in mano anche i blocchi normali (`pickupAllBlocks = true`), il resto di serie | Al riavvio del gioco | 🔧 0.6.0: preparato, da provare |
| `config/inventoryessentials-common.toml` | Inventory Essentials senza trascinamento con Shift (`enableShiftDrag = false`: doppione di Mouse Tweaks), il resto di serie | Al riavvio del gioco | 🔧 0.6.0: preparato, da provare |
| `config/fallingtree.json` | FallingTree abbatte l'albero intero solo da accovacciati (`"sneakMode": "SNEAK_ENABLE"`), il resto di serie | Al riavvio del gioco | 🔧 0.6.0: preparato, da provare |
| `config/sparsestructures.json5` | Distanze tra le strutture: generale 1.4, villaggi 1, magione 2 | Al riavvio, solo nei chunk nuovi → mondo nuovo | ⚠️ da completare (vedi Strutture) |
| `config/paxi/datapacks/matteo_tweaks/` | Datapack caricato da Paxi in tutti i mondi (vedi Datapack) | Artefatti e vasi con `/reload`, lune riaprendo il mondo, modificatori di struttura col riavvio del mondo; il bottino vale per le casse non ancora aperte | ✅ |

AlmostUnified e Sparse Structures generano un file di default al primo avvio: i nostri lo **sostituiscono**.

## Ingredienti intercambiabili (AlmostUnified, `tags.json`)

AlmostUnified lavora sui tag già risolti: un oggetto aggiunto a un tag "figlio" non arriva al tag "padre". Per questo ogni oggetto è aggiunto a **tutti** i tag che le ricette usano davvero (ricavati dai sorgenti delle mod).

| Ingrediente | Prima | Dopo |
|---|---|---|
| **Farina** | Create (`c:flours/wheat`), Farm & Charm e Bountiful Fares (`c:flour`) non si scambiavano | Tutte e tre valgono ovunque |
| **Impasto** | FD e Create (`c:foods/dough`), Farm & Charm (`c:dough`) separati | Impasto di grano intercambiabile tra le tre. Gli impasti speciali (mais, patata dolce) restano separati |
| **Sale** | Expanded e Cultural Delights (`c:dusts/salt`), Meadow (`c:salts`), Hexalia (`c:salt`) | Ogni sale vale nelle ricette di tutte (Hexalia li accettava già) |
| **Mais** | Cultural Delights e Farm & Charm (`c:crops/corn`), Bountiful Fares (`c:foods/corn`), Brewin' And Chewin' (solo `c:crops`) | Intercambiabile. ⚠️ Le 5 ricette di Brewin' che chiedono proprio il **suo** mais restano così (non si sistemano con i tag) |
| **Limone** | Cultural Delights (`c:fruits/lemon`), Bountiful Fares (`c:foods/lemons`) | Intercambiabile |
| **Formaggio (porzioni)** | Meadow (fetta), Expanded Delight (fetta), Brewin' (spicchi), Cultural Delights (spicchio): quattro tag diversi | Le porzioni base valgono ovunque; le fette speciali di Meadow (ametista, distorta…) restano solo di Meadow. Formaggio di capra di Meadow valido per Expanded Delight |

Burro: già condiviso (`c:butter`). Latte: lasciato com'è (secchi, bottiglie e cocco sono forme diverse).

**Come verificare**: nel log di avvio, le righe `[CustomTags]` segnalano eventuali oggetti inesistenti (vengono saltati, il gioco non si rompe). In EMI, cercando `#c:dusts/salt` (il `#` cerca per tag) devono comparire tutti e quattro i sali.

La config di default di AlmostUnified unifica già i metalli; i cibi sono gestiti dai tag personalizzati di `tags.json`.

## Strutture (Sparse Structures, `sparsestructures.json5`)

- **Generale 1.4**: tutte le strutture un po' più rade (decisione del pack)
- **Villaggi a 1**: frequenza originale
- **Magione 2**: default della mod
- **Da completare** (istruzioni dentro il file): Witch Villa e Swamp Village di Dungeons and Taverns con fattore **3** (molto più rare, scelta dell'utente) e When Dungeons Arise a 2. I nomi esatti si leggono in gioco con `/dumpstructuresets` (crea un file con tutti i gruppi) oppure `/locate structure nova_structures:` + Tab

- **Fattore generale**: scelto 1.4 dentro la forbice 1.3–1.5
- **Sparse Structures** accetta in `customSpreadFactors` sia il nome di un gruppo (`structure_set`) sia quello di una struttura (in quel caso cambia tutto il gruppo); i fattori sono rispetto ai valori originali, non si moltiplicano con quello generale (verificato nel codice)
- **Strutture di palude** (deciso 16/10/2026): restano le capanne di Hexalia, Hexerei e YUNG's; Witch Villa e Swamp Village di Dungeons and Taverns restano ma molto più rare (fattore 3 in Sparse Structures)
- **Strutture di palude, dati verificati**: Hexalia `hexalia:herbalist_hut` (paludi, spacing 32); Hexerei `hexerei:witch_hut` (paludi, 20) e `hexerei:dark_coven` (paludi, 29), più `nature_coven`, `baba_yaga_hut` e `owl_post_office` nelle foreste; Dungeons and Taverns sotto `nova_structures` (sorgente non pubblico: nomi da leggere in gioco)
- Le strutture cambiano solo nei chunk nuovi.

## Datapack `matteo_tweaks`

La documentazione del datapack sta **dentro il datapack**, così viaggia con i file: `../pack/config/paxi/datapacks/matteo_tweaks/README.md` (panoramica, cartelle, condizioni di caricamento, quando hanno effetto le modifiche) e un `readme.md` in ogni cartella di `data/`. Parti attuali: lune di sangue (Enhanced Celestials), artefatti nelle casse delle strutture modded (nomi corretti nella 0.6.0: 148 casse, vedi sotto), Ars Nouveau nei vasi di Botany Pots, pesce cotto di Starcatcher, Berserker nelle fortezze di YUNG's (0.6.0, preparato). Le parti in lavorazione sono nei file delle versioni in corso (`../lavoro/versioni/`: 0.6.0 correzioni ed esperienza, 0.6.1 vasi, 0.6.2 mercato).

- **Caricamento automatico in tutti i mondi** ✅: **Paxi** (vedi 0301). I datapack vanno in `config/paxi/datapacks/`; l'ordine si fissa in `config/paxi/datapack_load_order.json` (facoltativo). Verificato nel codice: Paxi li registra come pacchetti obbligatori, quindi valgono anche alla creazione del mondo
- **Artefatti nelle casse** (corretti nella 0.6.0, preparati e da provare): 15 modificatori, uno per livello di rarità, con una cassa per struttura (non tutte, per non riempire ogni barile). I nomi sono verificati sull'inventario e sui file delle mod; **le casse escluse sono elencate**, struttura per struttura, nella scheda `../mod-knowledge/artifacts.md`, che porta anche le quattro strutture di Dungeons and Taverns ancora da decidere (`../lavoro/versioni/v0.6.0.md`, sezione 3).
- **Berserker nelle fortezze di YUNG's** (0.6.0, preparato e da provare): l'etichetta `data/cataclysm/tags/worldgen/structure/berserker_spawn.json` aggiunge `betterfortresses:fortress` (con `required: false`: senza YUNG's non dà errore). Vale solo per le fortezze generate **dopo**; prova: `/locate structure betterfortresses:fortress`, poi cercare i Berserker infuocati. Spiegazione nel `readme.md` della cartella.
- **Lune di sangue** (deciso 16/10/2026; dalla 0.5.1 con Enhanced Celestials 2): più rare (peso 5 invece di 10 nel calendario, obiettivo circa 3 ogni 100 giorni), mostri ×2; super luna ×4 (datapack `matteo_tweaks`). Gli effetti nuovi di EC2 (mostri più vicini, assedio ai villaggi) restano attivi. Altre leve di difficoltà se servisse: pesi di Mutant Monsters, Born In Configuration, `invader_spawn_rules` di Apotheosis

## Impostazioni decise per le mod

Decisioni prese che non sono ancora file del pack. Quelle che diventano file entrano con la versione indicata (dettaglio e chiavi: `../lavoro/versioni/` e le schede in `../mod-knowledge/`).

**Preso il 19/10/2026, ancora da provare** (nel pack con la 0.6.0, vedi la tabella dei file sopra): Artifacts solo con Curios (un'unica interfaccia con Ars Nouveau, niente doppi slot, niente bug di Accessories; **non aggiungere l'Accessories Compatibility Layer**); Carry On che prende in mano anche i blocchi normali; Inventory Essentials senza trascinamento con Shift; FallingTree solo da accovacciati.

**Deciso, senza file**: Traveler's Backpack lascia le shulker box fuori dallo zaino (`allowShulkerBoxes = false`, di serie); Every Compat **tiene tutte le varianti e tutti i legni** (nessuna lista nera: decisione del 19/10, scheda `../mod-knowledge/every-compat.md`). Niente `RUN_ONCE` (decisione del 19/10, sera): la generazione resta quella di serie, nessun file di config di Every Compat nel pack.

**Decisioni che restano a mano o di principio**:
- **Difficoltà** (si sommano World Tier ed Elites di Apotheosis, mod di boss e buff permanenti di Cataclysm Delight): World Tier di Apotheosis (si sceglie in gioco) + datapack per i Tier Augments; config di Cataclysm; Born in Chaos: Born In Configuration, oppure la gamerule `naughtinessMechanics` per disattivare il Krampus. In Control! ed Enhanced AI sono state scartate nel round del 17/10 (`../lavoro/0602-mod-scartate.md`): da rivalutare solo se la difficoltà non bastasse. Tema aperto in `../lavoro/0503-temi-aperti.md`.
- **Impostazioni video** (Minecraft, Sodium, Iris): **nessun file nel pack**, decisione dell'utente del 19/10/2026: si regolano a seconda del PC. Sodium di serie è già impostato per le prestazioni e in parte si adatta da solo; Iris non regola niente da sola, la qualità si sceglie nel profilo di ogni pacchetto di shader (schede `sodium`, `iris`).
- **Tasti in conflitto**: Sophisticated e Traveler's aprono entrambi con **B**, Psi e Ars Nouveau usano entrambi **C**: si cambiano a mano nelle impostazioni di Minecraft (Controlling aiuta a trovare i conflitti). Tema aperto in `0503`.
- **Slot Curios contesi**: Ars Nouveau e Artifacts usano entrambe testa, collana e cintura (1 slot ciascuno). Se diventano stretti, si possono aumentare con un file di slot Curios nel datapack (formato da verificare). `artifactRarity` di Artifacts (default 1.0) regola la frequenza degli artefatti nel bottino: utile con tante mod di strutture.
- **Frantumatore di Occultism**: lasciato con i moltiplicatori di default (fino a 6 polveri per minerale con il Marid), **decisione dell'utente**: non modificarlo.
- **Magazzino dimensionale di Occultism**: convive con Tom's Simple Storage (accettato: si sblocca con i rituali).
- **Akashic Tome**: lista dei nomi di libri ammessi, se qualche libro non viene riconosciuto.
- **Subtle Effects** e **Sound Physics Remastered**: si toccano solo se in gioco danno problemi (increspature doppie con Particle Rain, CPU): chiavi nelle schede.
- **Jaden's Nether Expansion**, **Moog's Nether Structures**, **Cognition**: nessun file, config di serie (motivi nelle schede e in `v0.6.0.md`).
- **Sparse Structures**: regolazioni struttura per struttura dopo il mondo di prova (tappa 6).
