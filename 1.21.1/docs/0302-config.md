# Config del pack — Minecraft 1.21.1

Cosa fanno i file di configurazione del pack e quali impostazioni delle mod sono state decise. Documento vivo.

I file stanno in `pack/config/` e li installa packwiz-installer a ogni avvio dell'istanza (`../../docs/0101-installazione.md`). Prima del repository si copiavano a mano (storico in `../../ai-agents/stage/2026-10-16_pre-repo_pacchetti-mrpack/pacchetti-mrpack.md`).

## I file nel pack

| File | Cosa fa | Quando ha effetto | Stato |
|---|---|---|---|
| `config/almostunified/tags.json` | 19 tag personalizzati: rende intercambiabili gli ingredienti doppi tra le mod di cucina e magia (farina, impasto di grano, sale, mais, limone, porzioni di formaggio, formaggio di capra) | Al riavvio del gioco, in tutti i mondi | ✅ |
| `config/enhancedcelestials2core/translations.json` | Traduzioni di Enhanced Celestials 2: modalità `DISABLED`, cioè niente traduzioni scaricate dal sito dell'autore (con `AUTOMATIC`, che sembra il valore di serie, le scarica e le applica da sola) e nessuna richiesta di aiutare a tradurre. Senza il file la mod scrive in chat, a ogni ingresso nel mondo, di configurarle (B32). Nomi dei campi letti dal codice della mod. Per cambiare: `/ecc translate config` in gioco (la modifica resta finché il pack non porta una versione nuova del file) | Al riavvio del gioco | ✅ 0.5.2 |
| `config/artifacts/general.toml` | Artifacts solo con Curios: `enableAccessoriesCompat = false`, il resto di serie (file completo copiato dall'istanza). **Dalla 0.7.0 non viene più letto**: Reliquified Artifacts ignora la config di Artifacts; lo stesso effetto (niente slot di Accessories) lo dà il datapack. Resta nel pack, innocuo, per il caso in cui Reliquified Artifacts venga tolta | Al riavvio del gioco | ✅ 0.6.0: provato il 21/10 · 0.7.0: superato dal datapack |
| `config/carryon-common.toml` | Carry On prende in mano anche i blocchi normali (`pickupAllBlocks = true`), il resto di serie | Al riavvio del gioco | ✅ 0.6.0: provato il 21/10 |
| `config/inventoryessentials-common.toml` | Inventory Essentials senza trascinamento con Shift (`enableShiftDrag = false`: doppione di Mouse Tweaks), il resto di serie | Al riavvio del gioco | ✅ 0.6.0: provato il 21/10 |
| `config/fallingtree.json` | FallingTree abbatte l'albero intero solo da accovacciati (`"sneakMode": "SNEAK_ENABLE"`), il resto di serie | Al riavvio del gioco | ✅ 0.6.0: provato il 21/10 |
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

La documentazione del datapack sta **dentro il datapack**, così viaggia con i file: `../pack/config/paxi/datapacks/matteo_tweaks/README.md` (panoramica, cartelle, condizioni di caricamento, quando hanno effetto le modifiche) e un `readme.md` in ogni cartella di `data/`. Parti attuali: lune di sangue (Enhanced Celestials), reliquie e artefatti nelle casse e negli scavi (dalla 0.7.0, vedi sotto), Ars Nouveau nei vasi di Botany Pots, pesce cotto di Starcatcher, Berserker nelle fortezze di YUNG's (0.6.0, preparato). Le parti in lavorazione sono nei file delle versioni in corso (`../lavoro/versioni/`: 0.6.0 correzioni ed esperienza, 0.6.1 vasi, 0.6.2 mercato).

- **Caricamento automatico in tutti i mondi** ✅: **Paxi** (vedi 0301). I datapack vanno in `config/paxi/datapacks/`; l'ordine si fissa in `config/paxi/datapack_load_order.json` (facoltativo). Verificato nel codice: Paxi li registra come pacchetti obbligatori, quindi valgono anche alla creazione del mondo
- **Reliquie e artefatti nelle casse** (dalla 0.7.0, scelte di Matteo del 24/10, `../lavoro/versioni/v0.7.0.md`): le reliquie (comprese quelle di Artifacts, rifatte da Reliquified Artifacts) le mette **Relics** nelle casse `<mod>:chests/…`, abbassato dal 20% al **10%** con la nostra copia di `relics:relic_loot`; le **25 casse** che Relics non vede (Twilight Forest, YUNG's Better Dungeons, nave dell'End, Galeone, cittadella) hanno 10 modificatori nostri (`neoforge:add_table` sulle tabelle di Artifacts); gli **scavi** (5 tabelle vanilla) danno artefatti a 1/16 come prima; gli artefatti si indossano solo negli slot di Curios (etichette di Accessories con `remove`). Fino alla 0.6.3 c'erano 15 modificatori per 152 casse (le casse escluse di allora sono nella scheda `../mod-knowledge/artifacts.md`).
- **Vasi di Botany Pots** (dalla 0.6.1): colture e terreni delle mod che Botany Pots non conosce, **generati** da `scripts/botanypots_genera.py` dalle regole in `1.21.1/data/vasi/*.csv` (dal 22/10) (279 colture il 24/10 e 18 terreni, più 8 alberi di Bountiful Fares copiati da Botany Trees; nomi verificati sui jar con `scripts/vasi_verifica_jar.py`; 16 piante che senza cesoie non darebbero niente hanno il raccolto scritto) nelle cartelle `<mod>/` di `data/matteo_tweaks/recipe/botanypots/`, più l'etichetta `data/botanypots/tags/item/soil/dirt.json`; Ars Nouveau resta scritta a mano. Dettagli e cosa manca: `../lavoro/versioni/v0.6.1.md`; readme nel datapack.
  Scelte (approvate con la 0.6.x il 22/10/2026, da confermare con le prove; dettaglio in `../lavoro/versioni/v0.6.1.md`):
  - **Bilanciamento di serie**: tempi di crescita di Botany Pots, raccolti uguali a quelli della raccolta a mano; i bonus dei terreni seguono la **scala di rarità** decisa il 22/10 e ritoccata il 24/10 (`../data/vasi/rarita_pots_settings.csv`: 10 classi «natura» da common a mythic e 10 «craft-diff-0…9»; crescita 0, 0, 20, 20, 40, 40, 60, 60, 70, 80% e resa 0, 15, 6, 15, 6, 15, 6, 15, 25, 35%: più forti di prima, ma sempre sotto i livelli di Botany Pots Tiers; la classe di ogni terreno con il motivo in `terreno_rarita.csv`, 130 terreni, 12 file delle mod sostituiti allo stesso percorso; analisi e simulazioni in `../mod-knowledge/botany-pots/analisi.md`); **nessuna scorciatoia** per piante rare o magiche (fagioli magici esclusi; tronco della vite di Vinery escluso).
  - **Senza cesoie nello slot attrezzo**: piante la cui tabella dà qualcosa solo con le cesoie (erba e liane di Undergarden, Unusual End, Deep Aether, Hexerei, Jaden's) (16 con i germogli cremisi di Jaden's) hanno il **raccolto scritto a mano** (confermato da Matteo il 22/10), così funzionano senza fare nulla; le 49 piante selvatiche che senza cesoie danno il loro prodotto (semi, carota, patata…) invece della pianta intera **restano così**. Se si preferisse l'altra strada (cesoie obbligatorie), basta togliere le voci da `raccolti_diretti` in `1.21.1/data/vasi/aggiunte.json`.
  - **Terreni facoltativi** di Aether e Deep Aether scritti (i blocchi esistono); i terreni senza oggetto (`vinery:loam`, `deep_aether:aerglow_grass_block`) non si possono scrivere.
  - **Graticci e lava**: sambuco, lapisberry e frutto della passione di Bountiful Fares (dati, non blocchi) sono colture normali con raccolto fisso; le alghe di Nether Depths crescono sul secchio di lava (`botanypots:soil/lava`).
  - **Non scritte**: fagioli magici, tronco della vite di Vinery, sei piante di Jaden's (due usano gli stessi semi di torchflower e zucca vanilla, una liana non esiste senza Cinderscapes, `sorroweed` è un blocco di terreno, due edere sono a più facce e non si vedono nel vaso), 8 piante di Regions Unexplored con i nomi vecchi (se gli alias non bastano) e i terreni senza oggetto; i motivi nel file della versione, sezione 4.
- **Lista nera degli amuleti di pozione di Apotheosis** (dalla 0.7.2): l'etichetta `apotheosis:potion_charm_blacklist`, **generata** da `scripts/pozioni_genera.py` dalla regola in `1.21.1/data/pozioni/pozione_custom.csv` (una riga per pozione: tutta la famiglia o solo quella, in lista o riammessa, motivo). Scelta di Matteo (24/10/2026, `../lavoro/versioni/v0.7.2.md`): fuori solo ciò che rompe il gioco se dura per sempre, cioè Flying (Apothic Attributes), Weightlessness (Reactive), Acidity e Stupor (Bountiful Fares), Serenity (Unusual End), con le varianti (11 pozioni); i potenziamenti forti restano, perché l'amuleto infrangibile è già un traguardo di fine gioco. Readme in `data/apotheosis/`.
- **Mercato di Farming for Blockheads** (dalla 0.6.2): le piante delle mod che il mercato non vende (438 voci), **generate** da `scripts/mercato_genera.py` dalle regole in `1.21.1/data/mercato/*.csv`, con i listini della mod per semi e alberelli riscritti allo stesso percorso. Scelte (24/10/2026, dettaglio in `../lavoro/versioni/v0.6.2.md`):
  - **Prezzi alti**, perché il mercato non sostituisca l'esplorazione: moneta e quantità base per **origine** e intervallo di rarità (`mercato_base.csv`) × moltiplicatore della classe (×1 … ×10, `rarita_mercato_settings.csv`), per eccesso; sopra 64 in blocchi. Overworld: common e uncommon a 9 smeraldi base, da rare in su 3 diamanti base. Altre dimensioni, il loro materiale più raro: frammento di netherite (Nether), guscio di shulker (End, base 4), gravitite incantata (Aether), cristallo di regalium (Undergarden), steeleaf (Twilight Forest), cristallo d'anima (Otherside).
  - **Classe per mod** (`mercato_mod_custom.csv`): Overworld common solo Minecraft, uncommon le mod di cucina e agricoltura comuni, poi rare, super-rare (Regions Unexplored), ultra-rare (Hexalia, Hexerei), ultimate-rare (Reactive, Occultism), secret-rare (Ars); le mod delle altre dimensioni **mai sotto rare** (Deep Aether super-rare).
  - **Non si vendono**: le piante decorative (erba, cespugli, liane, coralli) e quelle magiche o rare (alberelli magici di Twilight Forest e di Occultism, torciafiore e baccello vanilla, golden oak, fiore incantato di Deep Aether, blocchi di sculk).
- **Esperienza Create ↔ Cognition** (0.6.3, provata il 24/10): la tabella delle unità di Create: Enchantment Industry capisce il cognitium di Cognition (20 mB per punto; il file si aggiunge a quello della mod) e il Mescolatore converte 50 mB di esperienza di Create ↔ 1000 mB di cognitium, senza perdite né guadagni. Le due direzioni restano (scelta del 24/10): nella stessa bacinella fanno avanti e indietro, quindi per convertire in un verso solo si mette nel **filtro della bacinella** il secchio del liquido da ottenere. Dettagli e regole: tema `../theme-knowledge/esperienza.md`, readme in `data/matteo_tweaks/recipe/create/mixing/experience/`.
- **Berserker nelle fortezze di YUNG's** (0.6.0, preparato; prova nel tempo): l'etichetta `data/cataclysm/tags/worldgen/structure/berserker_spawn.json` aggiunge `betterfortresses:fortress` (con `required: false`: senza YUNG's non dà errore). Vale solo per le fortezze generate **dopo**; prova: `/locate structure betterfortresses:fortress`, poi cercare i Berserker infuocati. Spiegazione nel `readme.md` della cartella.
- **Lune di sangue** (deciso 16/10/2026; dalla 0.5.1 con Enhanced Celestials 2): più rare (peso 5 invece di 10 nel calendario, obiettivo circa 3 ogni 100 giorni), mostri ×2; super luna ×4 (datapack `matteo_tweaks`). Gli effetti nuovi di EC2 (mostri più vicini, assedio ai villaggi) restano attivi. Altre leve di difficoltà se servisse: pesi di Mutant Monsters, Born In Configuration, `invader_spawn_rules` di Apotheosis

## Impostazioni decise per le mod

Decisioni prese che non sono ancora file del pack. Quelle che diventano file entrano con la versione indicata (dettaglio e chiavi: `../lavoro/versioni/` e le schede in `../mod-knowledge/`).

**Preso il 19/10/2026, provato il 21/10** (nel pack dalla 0.6.0, vedi la tabella dei file sopra): Artifacts solo con Curios (un'unica interfaccia con Ars Nouveau, niente doppi slot, niente bug di Accessories; **non aggiungere l'Accessories Compatibility Layer**); Carry On che prende in mano anche i blocchi normali; Inventory Essentials senza trascinamento con Shift; FallingTree solo da accovacciati. In gioco restano **tre menu** per indossare oggetti (Curios, Accessories standard, Aether): Matteo ha deciso il 21/10 di lasciarli così (tema `../theme-knowledge/accessori.md`).

**Deciso, senza file**: Traveler's Backpack lascia le shulker box fuori dallo zaino (`allowShulkerBoxes = false`, di serie); Every Compat **tiene tutte le varianti e tutti i legni** (nessuna lista nera: decisione del 19/10, scheda `../mod-knowledge/every-compat.md`). Niente `RUN_ONCE` (decisione del 19/10, sera): la generazione resta quella di serie, nessun file di config di Every Compat nel pack.

**Decisioni che restano a mano o di principio**:
- **Difficoltà** (si sommano World Tier ed Elites di Apotheosis, mod di boss e buff permanenti di Cataclysm Delight): World Tier di Apotheosis (si sceglie in gioco) + datapack per i Tier Augments; config di Cataclysm; Born in Chaos: Born In Configuration, oppure la gamerule `naughtinessMechanics` per disattivare il Krampus. In Control! ed Enhanced AI sono state scartate nel round del 17/10 (`../lavoro/0602-mod-scartate.md`): da rivalutare solo se la difficoltà non bastasse. Tema aperto in `../lavoro/0503-temi-aperti.md`.
- **Impostazioni video** (Minecraft, Sodium, Iris): **nessun file nel pack**, decisione dell'utente del 19/10/2026: si regolano a seconda del PC. Sodium di serie è già impostato per le prestazioni e in parte si adatta da solo; Iris non regola niente da sola, la qualità si sceglie nel profilo di ogni pacchetto di shader (schede `sodium`, `iris`).
- **Tasti in conflitto**: Sophisticated e Traveler's aprono entrambi con **B**, Psi e Ars Nouveau usano entrambi **C**: si cambiano a mano nelle impostazioni di Minecraft (Controlling aiuta a trovare i conflitti). Tema aperto in `0503`.
- **Slot Curios contesi**: Ars Nouveau e Artifacts usano entrambe testa, collana e cintura (1 slot ciascuno). Se diventano stretti, si possono aumentare con un file di slot Curios nel datapack (formato da verificare). Dalla 0.7.0 la frequenza delle reliquie nelle casse si regola nel datapack (`relics:relic_loot`, readme in `data/relics/`), non più con `artifactRarity` (la config di Artifacts è ignorata); Relics aggiunge slot di Curios suoi (charm, back, ring…).
- **Frantumatore di Occultism**: lasciato con i moltiplicatori di default (fino a 6 polveri per minerale con il Marid), **decisione dell'utente**: non modificarlo.
- **Magazzino dimensionale di Occultism**: convive con Tom's Simple Storage (accettato: si sblocca con i rituali).
- **Akashic Tome**: lista dei nomi di libri ammessi, se qualche libro non viene riconosciuto.
- **Subtle Effects** e **Sound Physics Remastered**: si toccano solo se in gioco danno problemi (increspature doppie con Particle Rain, CPU): chiavi nelle schede.
- **Jaden's Nether Expansion**, **Moog's Nether Structures**, **Cognition**: nessun file, config di serie (motivi nelle schede e in `v0.6.0.md`).
- **Sparse Structures**: regolazioni struttura per struttura dopo il mondo di prova (`../lavoro/0501-piano.md`).
