# Config del pack — Minecraft 1.21.1

Cosa fanno i file di configurazione del pack e quali impostazioni delle mod sono state decise. Documento vivo.

I file stanno in `pack/config/` e li installa packwiz-installer a ogni avvio dell'istanza (`../../docs/0101-installazione.md`). Prima del repository si copiavano a mano (storico in `../lavoro/0901-pacchetti-mrpack.md`).

## I file nel pack

| File | Cosa fa | Quando ha effetto | Stato |
|---|---|---|---|
| `config/almostunified/tags.json` | 19 tag personalizzati: rende intercambiabili gli ingredienti doppi tra le mod di cucina e magia (farina, impasto di grano, sale, mais, limone, porzioni di formaggio, formaggio di capra) | Al riavvio del gioco, in tutti i mondi | ✅ |
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

La documentazione del datapack sta **dentro il datapack**, così viaggia con i file: `../pack/config/paxi/datapacks/matteo_tweaks/README.md` (panoramica, cartelle, condizioni di caricamento, quando hanno effetto le modifiche) e un `readme.md` in ogni cartella di `data/`. Parti attuali: lune di sangue (Enhanced Celestials), artefatti nelle casse delle strutture modded, Ars Nouveau nei vasi di Botany Pots, pesce cotto di Starcatcher. Le parti in progettazione sono in `../lavoro/0620-progetto-datapack.md`.

- **Caricamento automatico in tutti i mondi** ✅: **Paxi** (vedi 0301). I datapack vanno in `config/paxi/datapacks/`; l'ordine si fissa in `config/paxi/datapack_load_order.json` (facoltativo). Verificato nel codice: Paxi li registra come pacchetti obbligatori, quindi valgono anche alla creazione del mondo
- **Lune di sangue** (deciso 16/10/2026): 5% delle notti, mostri ×2; super luna ×4 (datapack `matteo_tweaks`). Altre leve di difficoltà se servisse: pesi di Mutant Monsters, Born In Configuration, `invader_spawn_rules` di Apotheosis

## Impostazioni decise per le mod

Non sono ancora file del pack: vanno impostate a mano o entreranno come file di config (piano in `../lavoro/0501-piano.md`).

- **Difficoltà** (si sommano World Tier ed Elites di Apotheosis, mod di boss e buff permanenti di Cataclysm Delight):
  - World Tier di Apotheosis (si sceglie in gioco) + datapack per i Tier Augments
  - Config di Cataclysm
  - Born in Chaos: Born In Configuration, oppure la gamerule `naughtinessMechanics` per disattivare il Krampus
  - In Control! ed Enhanced AI sono state scartate nel round del 17/10 (`../lavoro/0602-mod-scartate.md`): da rivalutare solo se la difficoltà non bastasse
- **Carry On**: `pickupAllBlocks = true` per prendere in mano anche i blocchi normali (di default solo quelli con inventario o macchinari). La lista nera di default esclude già tutto Create, Ender Storage, Enchantment Industry e alcuni generatori di Mekanism (wind, heat)
- **FallingTree**: abbatte l'albero intero, stesso principio del vein mining → valutare l'opzione che lo attiva solo da accovacciati
- **Zaini**: Sophisticated e Traveler's aprono entrambi con **B** → cambiare il tasto di uno (es. Sophisticated su N). Traveler's: `allowShulkerBoxes = true` se si vogliono shulker box o zaini Sophisticated al suo interno
- **Inventory Essentials**: `enableShiftDrag = false` (doppione di Mouse Tweaks)
- **Artifacts** (`config/artifacts/general.toml`, sezione `[slots]`): `enableAccessoriesCompat = false`, lasciare `enableCuriosCompat = true`, **prima di creare il mondo**. Così Artifacts e Ars Nouveau condividono un'unica interfaccia Curios, non si possono indossare due copie dello stesso artefatto (con entrambe attive gli slot sono doppi e alcuni bonus si sommerebbero) e Artifacts non passa mai dal bug di Accessories. Non aggiungere l'Accessories Compatibility Layer. `artifactRarity` (default 1.0) regola la frequenza degli artefatti nel bottino: utile con tante mod di strutture
- **Slot Curios contesi**: Ars Nouveau e Artifacts usano entrambe testa, collana e cintura (1 slot ciascuno). Se diventano stretti, si possono aumentare con un file di slot Curios nel datapack del pack (da verificare il formato)
- **Subtle Effects**: se le increspature della pioggia compaiono doppie con Particle Rain, disattivare `rainWaterRipples`
- **Sound Physics Remastered**: costa un po' di CPU; se pesa, abbassarne la qualità
- **Tasto C**: Psi (tasto principale) e Ars Nouveau (apri libro) usano entrambi **C** → cambiarne uno (Controlling aiuta a trovare i conflitti)
- **Frantumatore di Occultism**: lasciato con i moltiplicatori di default (fino a 6 polveri per minerale con il Marid), **decisione dell'utente**: non modificarlo
- **Magazzino dimensionale di Occultism**: convive con Tom's Simple Storage (accettato: si sblocca con i rituali)
- **Akashic Tome**: lista dei nomi di libri ammessi, se qualche libro non viene riconosciuto

## Config previste per la 0.6.0

- **Every Compat**: spegnere i moduli che non servono; tenere Handcrafted, Macaw's ×4, credenze di FD, Storage Drawers, finestre di Create, Rechiseled, alveari di Friends & Foes, Twilight Forest, Regions Unexplored, Botany Pots. Va decisa prima di costruire molto: togliere un modulo cancella i blocchi già creati. Con la config di serie crea il 40% dei blocchi del pack e il modulo di Rechiseled è il più pesante (bug B22): decidere se tenerlo.
- **Jaden's Nether Expansion** (`config/netherexp-startup.toml`, sezione `packSettings`, serve riavvio), solo come paracadute se il Nether nuovo desse problemi: `improvedNetherBiomeSource = false` (disposizione dei biomi vanilla), `netherWorldGenOverhaul = false` (altezza vanilla).
- **Artifacts**: l'impostazione decisa sopra (solo Curios) diventa un file del pack.
- **Moog's Nether Structures**: niente da fare. La sostituzione della fortezza vanilla con la sua mega-fortezza è spenta di serie e deve restare così (la fortezza la rifà YUNG's).
- **Sparse Structures**: regolazioni per struttura dopo il mondo di prova.
- **Cognition**: lasciare `AllowedFluids` com'è.
