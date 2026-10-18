# Prove in gioco — Minecraft 1.21.1

Le prove e i controlli da fare nell'istanza di prova. Documento vivo: una prova fatta si spunta e il risultato va dove serve (un problema nel bug report `../docs/0402-bug-report.md`, un fatto verificato in `../docs/0303-note-tecniche.md`).

## Prove prioritarie 🧪

- [ ] **Nether della 0.5.0** (mondo nuovo): nel log la riga di Elysium "MosaicBiomeSource successfully patched surface rules from Terrablender" (✅ presente il 18/10); in gioco `/locate biome regions_unexplored:infernal_holt` (i biomi di Regions Unexplored devono esserci ancora), `/locate structure mns:mega_fortress` e `/locate structure betterfortresses:fortress` (le fortezze di YUNG's restano), alghe nei mari di lava, la canna di Nether Depths Upgrade accanto a quella di Starcatcher. Se il Nether nuovo desse problemi: paracadute in `../docs/0302-config.md`. Procedura completa in `0701-nether.md`, sezione 6
- [ ] **Miapi + Accessories** (bug B07; l'Aether è nel pack dalla 0.1.0 per scelta dell'utente, quindi se il test fallisce va tolta lei; log del 17/10/2026: Accessories 1.1.0-beta.48 arriva **dentro l'Aether**, quindi il test serve ancora): mondo di prova con Truly Modular + Hexalia + Forgified Fabric API; prendere e infliggere danno. Issue Miapi #118 e Accessories #387 aperte al 12/10/2026. Se passa → resta tutto così. Se non passa → si tolgono Aether, Deep Aether e Aether's Delight (con loro esce Accessories) e si tiene Truly Modular, finché il bug non viene corretto
- [ ] **Curios + Accessories**: Cataclysm usa Curios, Miapi e Hexalia usano Accessories; verificare che convivano
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

Obbligatorio prima del mondo vero (deciso il 17/10/2026, `0611-round-2026-10-17.md`):
- [ ] **Pre-generazione** con Chunky e controllo sulla mappa di Xaero, Overworld e Nether
- [ ] **Densità delle strutture**: regolarla con Sparse Structures struttura per struttura invece di togliere mod (`../docs/0302-config.md`)
- [ ] **Jaden's Nether Expansion**: Nether più alto e biomi; paracadute nella sua config (`../docs/0302-config.md`)
- [ ] **Vasi**: comandi di debug di Botany Pots (`0620-progetto-datapack.md`, Verifica in gioco)
- [ ] **Esperienza**: conversione Create ↔ Cognition avanti e indietro, Experience Hatch su un serbatoio di Mekanism (`0620-progetto-datapack.md`, Prova nel mondo di prova)
- [ ] **Every Compat**: quanti blocchi crea e quanto allunga l'avvio, prima di costruire molto (toglierla cancella i blocchi creati)
