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

## Potenziamento ed evoluzione (valutazione iniziale del 23/10)

Idea di Matteo (`../lavoro/0503-temi-aperti.md`): gli accessori non crescono. Fatti dall'inventario:
- **Chi porta accessori** (oggetti nei tag `curios:`): Traveler's Backpack 44 (zaini), Twilight Forest 23 (soprattutto trofei e amuleti), Ars Elemental 18, Starcatcher 17 (cappelli e amuleti da pesca), Ars Nouveau 14, Cataclysm 13, Unusual End 13, Occultism 6; **Artifacts** 54 oggetti, ognuno a sé.
- **Catene già esistenti** (versione migliore = un altro oggetto, non un potenziamento): Ars Nouveau anello dello sconto minore → maggiore; Aether anelli e pendenti di ferro → oro → zanite (più quelli di ghiaccio) e guanti per materiale (cotta di maglia, oro, diamante, gravitite… con le finiture).
- **Vincolo**: il datapack non crea oggetti nuovi e non cambia gli effetti scritti nel codice (Artifacts ha una config, ma vale per tutti, non per livelli). Quindi "evolvere" nel datapack vuol dire solo **ricette che trasformano un accessorio esistente in un altro esistente** (es. A + materiale raro → B, se B è davvero migliore).

Valutazione:
- 🟢 Prima l'analisi: per ogni slot, gli accessori e il loro effetto; dove ci sono già "fratelli" più forti (come sopra) una ricetta di passaggio nel datapack è semplice e coerente.
- 🟡 Una mod dedicata ai livelli degli accessori (cresce con l'uso o con materiali): da cercare per 1.21.1 NeoForge e da mettere tra le candidate; aggiunge oggetti suoi più che potenziare quelli delle altre mod.
- 🟡 Apotheosis (affissi e gemme): potenzia armi e armature; se valga anche per gli accessori Curios **non è verificato**.
- 🔴 Riscrivere gli effetti degli accessori: serve codice, fuori dal datapack.

## Rimandi

Schede delle mod: `../mod-knowledge/aether.md`, `../mod-knowledge/artifacts.md`. Slot contesi tra Ars Nouveau e Artifacts (testa, collana, cintura): `../docs/0302-config.md`, Impostazioni decise.
