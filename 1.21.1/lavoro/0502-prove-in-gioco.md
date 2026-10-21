# Prove in gioco — Minecraft 1.21.1

Le prove e i controlli da fare nell'istanza di prova. Documento vivo: i controlli che valgono finché non sono fatti. Una prova fatta si spunta e il risultato va dove serve (un problema nel bug report `../docs/0402-bug-report.md`, un fatto verificato nella scheda della mod in `../mod-knowledge/`, l'esito della versione nel suo file in `versioni/`). Le prove di una versione in lavorazione stanno nel suo file.

**Questo documento raccoglie le prove «nel tempo»**: si fanno giocando, **non bloccano** nessuna uscita (le prove di uscita, poche e rapide, stanno nella sezione 5 del file di ogni versione: regola in `../../AGENTS.md`, sezione 5). Un controllo qui non ancora fatto vuol dire «da tenere d'occhio», non «versione incompleta».

## Prove prioritarie 🧪

- [ ] **Shader** (Iris, dalla 0.5.2/0.5.3; risultati delle prove già fatte in `versioni/v0.5.2.md` e `v0.5.3.md`). Da fare: accendere a turno **Complementary Reimagined** e **MakeUp - Ultra Fast** e guardare macchinari di Create in movimento, foglie e luci delle mod (MakeUp le riconosce, Complementary no), cielo e luna con una luna di sangue (colori di EC2), Twilight Forest e Aether, blocchi Skyweave di Ars Nouveau (con gli shader diventano neri), effetti di Lodestone nel Nether; poi spegnere gli shader e controllare che il gioco torni com'era; **riprovare con 12 GB di memoria** dopo un ricaricamento delle risorse (B33). Rischi nel tema `../theme-knowledge/shader.md`

- [ ] **Correzioni della 0.6.0** (rilasciata il 22/10, prove di uscita del 21/10; dettagli in `versioni/v0.6.0.md`): nel log dell'istanza dev nessun nome di cassa inesistente e, in una struttura nuova di Dungeons and Taverns con tesoro «vault» (`nether_keep`, `piglin_donjon`, `toxic_lair`, `trident_trial_monument`), un artefatto nella sua cassa; `/locate structure betterfortresses:fortress` e, in una fortezza **nuova**, i Berserker infuocati; con Artifacts solo Curios (`enableAccessoriesCompat = false`) nessun doppio slot e nessun artefatto nel menu standard di Accessories (i tre menu per indossare oggetti restano, deciso il 21/10: tema `../theme-knowledge/accessori.md`); Carry On che solleva un blocco normale; FallingTree che abbatte l'albero intero solo da accovacciati; Inventory Essentials senza trascinamento con Shift; con Every Compat intero e 12 GB, tempo di avvio e memoria dopo un F3+T (B22, B33)
- [ ] **Lune** (Enhanced Celestials 2, dalla 0.5.1; log già controllato: `versioni/v0.5.1.md`). Nel mondo di prova: `/ec lunarForecast` per contare le lune di sangue (obiettivo circa 3 ogni 100 giorni; se sono molte di più o di meno si cambia il peso); `/ec dumpModifiers` sulla luna di sangue deve mostrare mostri ×2 (×4 la super); `/ec setLunarEvent` per avviarne una e provarla (anche con gli shader). Scheda `../mod-knowledge/enhanced-celestials-2.md`
- [ ] **Nether** (dalla 0.5.0; prova del 18/10 già fatta: `versioni/v0.5.0.md`). Nel mondo di prova: biomi di Regions Unexplored nel Nether (`/locate biome regions_unexplored:infernal_holt`), fortezze di YUNG's accanto alle strutture di Moog's (`/locate structure betterfortresses:fortress`, `mns:mega_fortress`), la canna di Nether Depths accanto a quella di Starcatcher. Tema `../theme-knowledge/nether.md`
- [ ] **Miapi + Accessories** (bug B07; l'Aether è nel pack dalla 0.1.0 per scelta dell'utente, quindi se il test fallisce va tolta lei; log del 17/10/2026: Accessories 1.1.0-beta.48 arriva **dentro l'Aether**, quindi il test serve ancora): mondo di prova con Truly Modular + Hexalia + Forgified Fabric API; prendere e infliggere danno. Issue Miapi #118 e Accessories #387 aperte al 12/10/2026. Se passa → resta tutto così. Se non passa → si tolgono Aether, Deep Aether e Aether's Delight (con loro esce Accessories) e si tiene Truly Modular, finché il bug non viene corretto
- [ ] **Curios + Accessories**: Cataclysm usa Curios, Miapi e Hexalia usano Accessories; verificare che convivano. Dal 21/10 si sa che in gioco i menu sono tre (tema `../theme-knowledge/accessori.md`): confermare a schermo che gli artefatti sono solo in Curios e controllare se uno stesso zaino si può indossare in due menu insieme
- [ ] **BotanyPotsAdditions** e **Roaster's Delight**: provarle da sole prima di affidarci un mondo lungo (mod recenti, pochi download)
- [ ] **Botany Pots Tiers + BotanyPotsAdditions** insieme (blocchi diversi, dovrebbe funzionare)
- [ ] **Create: Central Kitchen + Create Slice & Dice** insieme: entrambe automatizzano Farmer's Delight, nei pack famosi non compaiono mai insieme
- [ ] **Create: Enchantment Industry + Apothic Enchanting**: incantamento automatico con il sistema di Apotheosis
- [ ] **HerbalBrews**: il Brewing Cauldron accetta anche le pozioni delle altre mod? (punto d'arrivo della catena delle pozioni)
- [ ] **Create Confectionery** con Create 6.0.10: sorgente chiuso, compatibilità probabile ma da confermare (macchine e ricette funzionano?)
- [ ] **Apotheosis + Truly Modular** (bug B04): all'avvio Apotheosis va in errore leggendo il "tier" delle armi e degli attrezzi modulari di Miapi (NullPointerException in Miapi, 20 oggetti). Nessun crash; da provare se le armi Miapi ricevono affissi, gemme e riforgiatura e se i nomi generati sono corretti
- [ ] **owo-lib 0.12.15.6**: quando esce su Modrinth, aggiornarla e riprovare con l'ultimo NeoForge (perché NeoForge è fermo: `../docs/0303-note-tecniche.md`, bug B17)
- [ ] **Psi + Sodium**: issue Psi #853 (particelle di altre mod corrotte, peggio con Sodium) → provare con Particle Rain e Subtle Effects attive
- [ ] **Zaini nello slot schiena + morte**: morire con Traveler's (e Sophisticated) addosso e verificare che Corail Tombstone li conservi

## Controlli durante la creazione

- [ ] **Addon FD**: ogni addon deve dichiarare compatibilità con FD 1.3.x; aggiungerli a piccoli gruppi
- [ ] **Polymorph**: `/polymorph conflicts` per elencare i conflitti di ricette
- [ ] **Botany Pots**: `/botanypots debug ...` per trovare semi non supportati (addon FD, alberi di Twilight Forest e Aether); l'opzione `gen_files` genera i datapack mancanti
- [ ] **Truly Modular**: controllare quali materiali delle altre mod mancano (Mekanism, Twilight Forest, Aether…) e coprirli con il Material Helper
- [ ] **OmniTools**: verificare in gioco cosa copre oltre a Create e Mekanism (es. Pipez)
- [ ] **Chunk Loaders**: confermare che sia la mod "a tier" usata in passato
- [ ] **Serene Seasons**: valutare l'impatto delle stagioni sul farming di FD
- [ ] **RightClickHarvest**: provarlo con le colture di FD e degli addon (es. rampicanti, colture a più blocchi)
- [ ] **Carry On**: provarlo su casse, cassetti di Storage Drawers e macchine Mekanism
- [ ] **Inventory Essentials**: provare l'ordinamento nelle GUI modded (toolbox di Create, macchine Mekanism, pentola di FD); se una dà problemi, aggiungerla alla lista ignorati
- [ ] **Ars Nouveau**: il Worn Notebook si aggancia all'Akashic Tome? **Ars nei vasi** (Magebloom, Sourceberry, frutti di archwood sui tronchi): provarli in gioco; come sono fatti è spiegato nel readme dei vasi dentro il datapack. Il file per i vasi incluso in Ars Elemental non si carica (bug B19, risolto dal nostro datapack)
- [ ] **Addon di Ars**: Ars Creo chiede Create 6.0.9+; Ars Unification va provato con AlmostUnified attivo (glifi Frantuma/Taglia sulle ricette di Mekanism e FD); Ars QOL aggiunge uno slot Curios per il libro, controllare che non sposti gli altri
- [ ] **Doppioni di cibo**: cercare in EMI pomodoro, cipolla, farina, impasto, sale (FD, Farm & Charm, Create); di solito le ricette accettano i tag comuni
- [ ] **Zinco**: Mekanism non ha la lavorazione 3×/5× per lo zinco di Create; JAOPCA (MIT) può generarla, solo se serve
- [ ] **Strutture**: `/dumpstructuresets` per controllare la distanza tra le strutture; Structure Layout Optimizer da verificare in gioco
- [ ] **Scriptor Magicae**: incisione di incantesimi sugli oggetti all'incudine insieme ad Apothic Enchanting (stesso punto del codice dell'incudine)

## Rischi e note di compatibilità

- **Accessories su NeoForge 1.21.1**: bug nel codice di Accessories (chiamata a Fabric Loader quando una mod chiede uno slot fuori range); Miapi lo fa scattare quando un'entità subisce danno, ma può farlo qualunque mod. Riguarda già Hexalia. Fix: Forgified Fabric API, che fornisce la classe mancante (nell'issue di Miapi un utente l'ha risolto con Sinytra Connector, stesso principio ma più pesante)
- **Curios + Accessories** nello stesso pack: due librerie accessori diverse
- **FD 1.3.x**: ha cambiato tag e meccaniche, gli addon vecchi possono rompersi
- **Mod molto recenti** (Roaster's Delight, BotanyPotsAdditions): possibili bug
- **Hexerei**: versione 1.21.1 ferma al 2025, sviluppo rallentato
- **When Dungeons Arise**: ramo 1.21.1 fermo da ottobre 2025 (stabile, ma niente fix nuovi)
- **The Undergarden**: versione beta
- **Tante strutture insieme**: rischio di mondo affollato → una sola mod di spacing, massimo due mod di villaggi
- **Difficoltà cumulativa**: vedi 0302; niente Improved Mobs
- **Occult Delight**: una sola release finora
- **Psi**: issue aperte su particelle (#853) e su un trucco dell'Exosuit (#869)

## Mondo di prova (tappa 6, prima della 1.0.0)

Obbligatorio prima del mondo vero (deciso il 17/10/2026, `versioni/v0.2.3.md`). Sono le prove di uscita della **1.0.0**, con la soglia più alta decisa il 19/10/2026 (`0503-temi-aperti.md`, sezione 4, n. 5):
- [ ] **Pre-generazione** con Chunky e controllo sulla mappa di Xaero, Overworld e Nether
- [ ] **Densità delle strutture**: regolarla con Sparse Structures struttura per struttura invece di togliere mod (`../docs/0302-config.md`)
- [ ] **Jaden's Nether Expansion**: Nether più alto e biomi; paracadute nella sua config (`../docs/0302-config.md`)
- [ ] **Vasi**: comandi di debug di Botany Pots (scheda `../mod-knowledge/botany-pots.md`; prove in `versioni/v0.6.1.md`)
- [ ] **Esperienza**: conversione Create ↔ Cognition avanti e indietro, Experience Hatch su un serbatoio di Mekanism (tema `../theme-knowledge/esperienza.md`; prove in `versioni/v0.6.3.md`)
- [ ] **Every Compat**: quanti blocchi crea e quanto allunga l'avvio, prima di costruire molto (toglierla cancella i blocchi creati)
