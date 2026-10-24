# Tema: accessori (Curios, Accessories e il menu dell'Aether)

Aggiornata il 23/10/2026 · mod coinvolte: Curios API, Accessories (dentro l'Aether), The Aether, Deep Aether, Artifacts, Sophisticated Backpacks, Traveler's Backpack, SeasonHUD, Ars Nouveau e le mod che indossano oggetti · fonti: inventario del pack (tag `curios:` e `accessories:` letti dai .jar), log dell'istanza dev del 21/10, codice di Accessories 1.1.0-beta.48 (`wisp-forest/accessories`, tag `1.1.0-beta.48+1.21.1`) e dell'Aether 1.5.10 (`The-Aether-Team/The-Aether`, tag `1.21.1-1.5.10-neoforge`). **Non visto a schermo**: l'elenco dei menu è dedotto dal codice e dall'inventario; la conferma è nelle prove (`../lavoro/0502-prove-in-gioco.md`).

## In breve

Nel pack ci sono **due librerie di accessori che non si parlano** (Curios e Accessories) e l'Aether ha in più un **menu suo**: in gioco, nell'inventario, ci sono quindi **tre menu** dove indossare oggetti. È il comportamento previsto dalle mod, non un errore del pack.

| Menu | Libreria | Cosa ci va (dai tag dell'inventario) |
|---|---|---|
| **Curios** (pulsante Curios, 18 tipi di slot caricati all'avvio) | Curios API 9.5.1 | Artifacts (dalla 0.6.0 solo qui), Ars Nouveau con Elemental e QOL, L_Ender's Cataclysm, Occultism, Hexerei, The Twilight Forest, Unusual End, Starcatcher, Supplementaries, Tom's Simple Storage, Create (slot testa), Friends & Foes, Apotheosis, Cognition, e anche zaini e calendario (sotto) |
| **Aether** (pulsante e tasto dell'Aether) | Accessories, con la schermata propria dell'Aether | Gli oggetti dell'Aether e di Deep Aether (tag `aether:accessories_*`): guanti, pendenti, mantelli, anelli, scudo, vari |
| **Accessories standard** (pulsante di Accessories) | Accessories 1.1.0-beta.48 | Gli zaini (slot schiena) e il calendario di SeasonHUD, che sono validi **sia qui sia in Curios**. Altre mod che usino Accessories senza tag: non controllato |

## Fatti verificati

- **Curios** è obbligatoria per Ars Nouveau (con Controle e QOL), Cataclysm e Occultism; facoltativa per Apotheosis e Cognition (inventario, dipendenze). **Accessories** non è un .jar a parte: è incorporata nell'Aether (log: `accessories-neoforge-1.1.0-beta.48+1.21.1.jar [parent: aether-1.21.1-1.5.10-neoforge.jar, locator: jarinjar]`).
- Le due librerie non sono collegate. Accessories le collega a Curios solo con una mod a parte, l'Accessories Compatibility Layer: nel codice di Accessories il suo adattamento a Curios si attiva solo se Curios c'è e il layer **no**, e AllTheLeaks scrive nel log che il layer non è presente. Decisione del 16/10 (scheda `../mod-knowledge/artifacts.md`): il layer non si aggiunge.
- **Menu dell'Aether**: di serie (`use_default_accessories_menu = false`, sezione Gameplay della config comune dell'Aether) l'Aether usa la sua schermata `AetherAccessoriesScreen`, con slot suoi (guanti, pendente, mantello, anello, scudo, vario: file `aether/accessories/slot/aether/*_slot.json` del suo .jar) caricati dal datapack interno `builtin/aether_accessories` (compare nel log). Il pulsante dell'Aether si aggiunge a quello standard di Accessories, non lo toglie: `AetherAccessoriesScreen` si apre con il suo pulsante o con il suo tasto; quello standard di Accessories è aggiunto all'inventario e all'inventario creativo senza condizioni (`AccessoriesClient.initLayer`). Con `use_default_accessories_menu = true` gli oggetti dell'Aether vanno invece negli slot standard (guanti in `hand`, pendente in `necklace`, mantello in `cape`, scudo di repulsione in `back`); la config avverte di svuotare prima gli accessori equipaggiati. Il pulsante dell'Aether si toglie con `disable_accessory_button` (client).
- **Zaini e calendario in due menu**: Sophisticated Backpacks e Traveler's Backpack hanno sia `curios:back` sia `accessories:back`; SeasonHUD sia `curios:calendarslot` sia `accessories:calendarslot`. Non è stato verificato se uno stesso zaino si può indossare in tutti e due i menu allo stesso tempo (due zaini addosso).
- **Artifacts**: nel .jar ha tag per entrambe le librerie (`curios:*` e `accessories:*`); con `enableAccessoriesCompat = false` (dalla 0.6.0) l'overlay del suo `pack.mcmeta` svuota i tag di Accessories, quindi gli artefatti stanno solo in Curios. Da confermare a schermo: nessun artefatto indossabile nel menu standard di Accessories.
- Log del 21/10: `Loaded 18 curio slots`; nessun dato su quanti slot carica Accessories. L'avviso `It seems the given player has no slots bound to it within a init call` di Accessories compare anche nei log precedenti.
- Per ridurre i menu le strade sono: Aether con il menu standard (`use_default_accessories_menu = true`, ma lo scudo di repulsione e gli zaini si contendono lo slot `back`), il Compatibility Layer (scartato il 16/10), oppure togliere l'Aether (che porta con sé Accessories). **Deciso il 21/10/2026 (Matteo): «ok così»**, restano tre menu e nessuna config da cambiare (`../lavoro/versioni/v0.6.0.md`, Decisioni). Le strade restano qui come memoria, se un giorno servisse ridurli.

## Potenziamento ed evoluzione (ricerca del 23/10)

Idea di Matteo (`../lavoro/0503-temi-aperti.md`): gli accessori non crescono. Grezzo della ricerca: `../../ai-agents/stage/2026-10-23_accessori-evoluzione/` (jar e config dell'istanza, sorgenti delle versioni del pack, API di Modrinth).

**Cosa c'è già nel pack**
- **Catene "versione migliore = altro oggetto"**: Ars Nouveau anello del potenziale → sconto minore → sconto maggiore (Apparato); Ars Elemental focus minore → focus (conserva i dati); Twilight Forest 4 amuleti della vita di grado 1 → 1 di grado 2, conservazione fino al 3; Aether anelli e pendenti di ferro/oro → di ghiaccio, guanti per materiale e guanti di diamante → netherite alla forgia; Deep Aether alla forgia guanti di skyjade → stormforged, guanti e anello di gravitite → stratus; Unusual End sfera del golem → sfere di fiamma, shulker, avvizzimento. Zaini: dal base alla netherite conservando il contenuto.
- **Crescono con l'uso**: gli strumenti di zanite dell'Aether (più sono consumati, più sono veloci), i guanti della fenice che diventano d'ossidiana; il famiglio fabbro di Occultism potenzia gli altri famigli.
- **Artifacts** (48 oggetti): nessuna ricetta di accessori e nessun livello; la config (`items.toml`) vale per tipo di oggetto e per tutte le copie. Ma le **abilità sono componenti dell'oggetto** che accettano anche **valori fissi**: vedi la scheda `../mod-knowledge/artifacts.md`.
- **Apotheosis 8.9.0 non agisce sugli accessori Curios**: affissi, gemme e rifacimento valgono solo per armi, armature, scudi e attrezzi negli slot vanilla; la categoria per Curios è commentata nel codice (`compat/curios/CuriosCompat.java`, "Experimental"). Il suo unico accessorio, il talismano di pozione, con l'infusione diventa indistruttibile.
- **Slot (risponde al «formato da verificare» dei temi aperti)**: `data/<ns>/curios/slots/<slot>.json` con `size` e `operation` (`SET`, `ADD`, `REMOVE`; di serie `SET`), `replace`, `add_cosmetic`, `drop_rule`; le entità in `data/<ns>/curios/entities/*.json` (Curios 9.5.1, `CuriosSlotManager`). Il componente `curios:attribute_modifiers` dà a un accessorio attributi in più **o uno slot in più** (`type: "curios:<slot>"`) solo mentre è indossato nello slot indicato; se presente, sostituisce i modificatori Curios propri dell'oggetto.

**Mod esterne (1.21.1 NeoForge, dati di Modrinth del 23/10)**

| Mod | Versione | Licenza | Usa | Cosa fa | Giudizio |
|---|---|---|---|---|---|
| Reliquified Artifacts | 1.0.9 beta, 12/10/2026 | ARR | Curios, Relics, OctoLib; vuole esattamente Artifacts 13.2.5 (la nostra) | Rifà tutti i 48 artefatti come reliquie di Relics, con livelli e ranghi | 🟡 È l'idea. Casse e slot di Accessories si sistemano col datapack; la config di Artifacts viene ignorata: scheda `artifacts` |
| Relics | 0.12.9 beta, 18/10/2026 | ARR (uso nei modpack permesso) | Curios, OctoLib/ShatterLib | 20 reliquie sue, il livello sale usandole, punti, rilancio delle statistiche, ranghi, ricerca | 🟡 Mod autonoma interessante; i mantelli vanno nello slot `back` degli zaini |
| More Relics | 1.7.7 beta, legata a build precise di Relics (l'ultima vuole la 0.12.8, è uscita la 0.12.9) | ARR | Relics | Reliquie in più, con evoluzioni | 🔴 |
| L2 Artifacts | 3.0.7 | LGPL-2.1 | Curios, L2 Library | Set di artefatti suoi con statistiche casuali, che salgono di livello | 🔴 |
| BaublesReforked | 1.0.3 | ARR, codice chiuso | Curios | Attributi casuali sugli accessori, rifatti sull'incudine | 🟡 Non si sa quali accessori tocchi |
| Tiered More | — | — | Curios o Accessories | Livelli di qualità sugli oggetti | 🔴 Con Accessories presente (nell'Aether) spegne il supporto a Curios |
| Apothic Curios | solo 1.20.1 / 1.19.2 Forge | — | — | Affissi di Apotheosis sugli accessori | Non esiste per 1.21.1 |

**Diffusione e affidabilità (23/10)**: Relics e Reliquified Artifacts sono in **All The Mods 10** e in **Craftoria** (elenchi delle mod del 16/10); More Relics in nessuno dei due. Download: Relics 64,6 milioni su CurseForge e 3,3 su Modrinth, usata in circa 12.400 modpack (Modpack Index); Reliquified Artifacts 28,7 milioni su CurseForge; More Relics 160 mila su Modrinth. Recensioni vere non ce ne sono: Moddex 4,1/5 con 5 voti e nessun commento, nessuna discussione trovata su Reddit. Segnali dai changelog dei modpack: Craftoria ha abbassato la probabilità delle reliquie dal 20% al 10% (1.36.0); un suo aggiornamento ha azzerato i livelli delle reliquie (1.3.0) e un altro ha cancellato le reliquie vecchie con il «nuovo sistema» (1.34.0, insieme alla rimozione di due addon Reliquified); più correzioni di crash all'indossare certe reliquie. Su GitHub Relics ha 63 segnalazioni aperte, diverse di crash su 1.21.1; la pagina CurseForge dice che l'API di Relics «è ancora instabile e cambia spesso».

**Cosa si può fare col nostro datapack** (non crea oggetti né effetti nuovi, non fa crescere con l'uso):
- 🟢 **Lo stesso artefatto "potenziato"** con valori fissi più alti (es. guanto del potere +6 danno invece di +4), ottenuto con un'infusione al tavolo d'incantamento di Apothic Enchanting (le tappe diventano tappe dell'incantamento), una ricetta, o il bottino delle casse dei boss. Formati verificati nei jar; scheda `artifacts`.
- 🟢 **Ricette di passaggio** dove ci sono già "fratelli" più forti (es. anelli e pendenti dell'Aether di ferro o d'oro + zanite → di zanite).
- 🟡 **Attributi o slot in più** con `curios:attribute_modifiers` sugli accessori potenziati.
- 🔴 Livelli che crescono con l'uso, effetti nuovi, affissi di Apotheosis sugli accessori: servono mod.

**Da provare in gioco** (con `/give`, comandi nel grezzo, sezione 5): un guanto del potere con il componente a +6; sciarpa fortunata con Fortuna II; `curios:attribute_modifiers` con +2 armatura e con uno slot anello in più; una ricetta di prova con risultato a componenti (anche alla forgia); un artefatto nel tavolo del rifacimento di Apotheosis (atteso: non entra).

**Valutazione** (aggiornata la notte del 23/10): 🟢 prima le prove con `/give`, poi un pilota nel datapack con 3–5 artefatti di "livello II" per infusione. 🟡 In alternativa Relics + Reliquified Artifacts, insieme e solo dopo una prova in un'istanza a parte, prima del mondo vero; 🔴 More Relics. Strade, decisioni e versione proposta: `../lavoro/0503-temi-aperti.md`, sezione 6. **Decisione di Matteo del 24/10: Relics + Reliquified Artifacts, nella 0.7.0** (`../lavoro/versioni/v0.7.0.md`).

## Rimandi

Schede delle mod: `../mod-knowledge/aether.md`, `../mod-knowledge/artifacts.md`. Slot contesi tra Ars Nouveau e Artifacts (testa, collana, cintura): `../docs/0302-config.md`, Impostazioni decise.
