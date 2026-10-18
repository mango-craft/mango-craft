# Note tecniche — Minecraft 1.21.1

Fatti verificati (nei sorgenti delle mod o in gioco) e cose da non rompere di questa versione. Da leggere prima di toccare il pack. Documento vivo: un fatto nuovo verificato si aggiunge qui, nel posto giusto.

## Cose da non rompere

- **NeoForge fermo a 21.1.259**: dalla 21.1.261 NeoForge ha cambiato il codice di rete e owo-lib 0.12.15.5 (libreria di Accessories, incorporata nell'Aether) non "spacchetta" più i suoi pacchetti → "Connection lost" appena si entra nel mondo. Si torna all'ultimo NeoForge solo quando esce owo-lib 0.12.15.6 (correzione già scritta nella 0.12.15.6-beta.1, commit del 16/10/2026).
- **Esperienza liquida**: il liquido di Create: Enchantment Industry vale 1 mB per punto, gli altri 20. **Mai** mescolarli per etichetta o per config: tabella e regole nella sezione Esperienza liquida qui sotto.
- **Regions Unexplored 0.6** usa Lithostitched (non TerraBlender), ha 4 biomi nel Nether e ha rinominato alcuni blocchi: Botany Pots usa ancora 8 nomi vecchi.
- **Frantumatore di Occultism**: non modificarlo (scelta dell'utente: `0302-config.md`).
- **Starcatcher**: i pesci crudi sono `c:foods/raw_fish`; il pesce cotto è generico (`starcatcher:cooked_starcaught_fish`) e lo mettiamo noi nelle etichette del pesce cotto (datapack, dalla 0.3.0). Etichette, filetti e ricette: `0301-mod.md`, Animali e pesca.
- **Librerie già nel pack**: quando una mod nuova chiede una versione più recente di una libreria che c'è già, packwiz non la aggiorna. Ora il controllo dei nomi lo segnala come errore ("Versione non adatta"); la libreria si aggiorna con il workflow Modrinth, indicando `slug@id-versione` (bug B28).
- **Botany Pots 1.21.1**: le ricette in formato 1.20 vengono ignorate; le piante raccolte col click destro richiedono raccolti espliciti.
- **Iris e Sodium** (dalla 0.5.2): con Sodium 0.8 funziona solo **Iris 1.8.14-beta.1**; l'ultima release, la 1.8.12, va in crash. Il workflow Modrinth da solo sceglie la release, quindi Iris si aggiunge o aggiorna solo indicando la versione (`iris@<id versione>`), e il controllo dei nomi non fermerebbe l'errore (la 1.8.12 chiede `sodium [0.6,)`, che la 0.8 soddisfa). Prima di aggiornare Sodium, verificare che Iris lo supporti. Ricerca: `../lavoro/0709-shader.md`.

## Esperienza liquida

| Liquido | Mod | mB per punto | Etichetta standard `c:experience` | Chi lo accetta |
|---|---|---:|---|---|
| `create_enchantment_industry:experience` | Create: Enchantment Industry 2.4.2 | **1** | **no** | Incantatore (Blaze Enchanter), lanterna, stampante di CEI: **solo questo liquido** (verificato nel codice: l'incantatore accetta solo `CEIFluids.EXPERIENCE`) |
| `cognition:cognitium_source` | Cognition 2.4.13 | 20 | sì | Obelisco (più una lista di liquidi ammessi in config), pompa degli zaini Sophisticated |
| `sophisticatedcore:xp_still` | Sophisticated Core | 20 | sì | Pompa e calamita degli zaini; l'Obelisco lo accetta di serie |

Lo standard NeoForge è **20 mB per punto** (documentato in `Tags.java`).

**Regole** (per non duplicare o perdere esperienza):
- **Mai** mettere il liquido di Create nell'etichetta `c:experience`: la pompa degli zaini lo tratterebbe a 20 mB per punto → esperienza moltiplicata per 20.
- **Mai** aggiungere il liquido di Create alla lista `AllowedFluids` di Cognition: l'Obelisco copia i mB 1 a 1 → perdita del 95%.
- I serbatoi di Mekanism tengono **un solo liquido alla volta**: i due liquidi non si mescolano per sbaglio.
- **Experience Hatch** di Create con liquidi "stranieri": con la quantità impostata su "tutto", ogni click deposita solo 1/20 dell'esperienza (si perde al massimo l'arrotondamento). Usare quantità fisse (10–1000 punti).

## Altri fatti verificati

- **Ricette per etichetta nelle mod di cucina del pack**: `c:eggs` circa 70, `c:foods/raw_chicken` circa 17, `c:foods/raw_beef` circa 15, `c:foods/raw_meat` circa 9. Un ingrediente nuovo è utile solo se entra in una di queste etichette o ha ricette proprie.
- **Regions Unexplored 0.6**, biomi del Nether: Mycotoxic Undergrowth (da Nether Wastes), Glistering Meadow (da Soul Sand Valley), Blackstone Basin (da Crimson Forest), Infernal Holt (da Basalt Deltas). Le sue piante del Nether sono già nei vasi.
- **Cataclysm**: Burning Arena solo in Nether Wastes; Soul Black Smith nei 4 biomi vanilla; Berserker legati a `cataclysm:berserker_spawn`.
- **Mod per la 1.21 sulla 1.21.1**: NeoForge accetta anche le mod che dichiarano solo Minecraft 1.21 (per esempio Iris chiede `[1.21,1.21.1)`): nella 1.21.1 il caricatore prova anche la versione 1.21 quando il controllo normale fallisce (verificato nel sorgente di FancyModLoader, `VersionSupportMatrix`). Allo stesso modo accetta le mod scritte per NeoForge 21.0 (prova la 21.0.166).
- **Farming for Blockheads**: le sue 5 terre fertilizzate sono già terreni di Botany Pots (anche nel tag `botanypots:soil/dirt`).
- **Polveri di Occultism** ✅ verificato nel codice (16/10/2026): AlmostUnified 1.4.2 ha un adattatore dedicato a Occultism che trasforma i risultati "a tag" del frantumatore (e dei minatori) nell'oggetto scelto. Le 7 polveri in comune sono tutte nei materiali di default di AU: ferro, oro, rame, smeraldo, lapislazzuli, netherite → escono quelle di **Mekanism**; ossidiana → quella di **Create**. Le altre polveri del frantumatore (carbone, diamante, osmio, stagno…) esistono solo in Mekanism, nessun doppione. In gioco basta un'occhiata in EMI (si vedono solo le polveri di Mekanism). Nota: l'integrazione con AU interna a Occultism è disattivata nella 1.21.1, ma non serve perché lavora AU sulle ricette
