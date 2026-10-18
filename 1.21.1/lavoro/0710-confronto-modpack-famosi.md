# Grandi aggiunte dal confronto con i modpack famosi (16/10/2026)

> **Documento storico**: fotografia del momento in cui è stato scritto, non si aggiorna. Lo stato attuale è nei documenti vivi (vedi il README della cartella).

Pack confrontati il 16/10/2026 (tutti 1.21.1): ATM10 v8.2, Craftoria 1.37.0, FTB Evolution 1.45.1, FTB StoneBlock 4 1.23.0, All of Create 2.6, Create Chronicles: The Endventure 2.0.0, Better MC (BMC5), Fresh & Smooth. Tutte le altre proposte del confronto sono state approvate (0301) o scartate (0602).

| Mod | Licenza | Note |
|---|---|---|
| ✅ Biomi: **Regions Unexplored** scelta il 17/10/2026 (→ 0301); ⛔ Oh The Biomes We've Gone | ARR / MIT | Unica grande categoria assente. Usano TerraBlender (già presente per Deep Aether). BWG è nei pack più famosi e in BMC5 convive con Serene Seasons e Aether; Regions Unexplored è open source. Da decidere **prima** di creare il mondo; poi generare i datapack di Botany Pots per gli alberi nuovi |
| **Geophilic** 3.7 · **YUNG's Cave Biomes** 3.1.1 | ARR | Ritocco dei biomi vanilla (pensato per BWG); biomi di grotta YUNG |
| ✅ Decorazione (17/10/2026, → 0301): **Supplementaries** + **Handcrafted** + **Construction Sticks** (+ **Rechiseled**); non scelte Another Furniture, Chisel Reborn, Chipped; Amendments da valutare | custom / Terrarium / custom / MIT | Barattoli, sacchi, cartelli, vasi; mobili; bacchetta da costruzione. Amendments resta fuori (conflitto con il calderone di Toil and Trouble) |
| ~~**Ars Nouveau**~~ | — | ✅ Approvata il 16/10/2026 → 0301 (Iron's Spells resta l'alternativa, vedi 0707) |
| Trasporti: **Create Aeronautics** 1.3.2 **oppure** **Immersive Aircraft** 1.5.0 | custom / GPL-3.0 | Aeronavi e veicoli costruiti con Create (grande novità 2026, pesante) oppure biplani e dirigibili semplici |
| ~~**Artifacts**~~ | — | ✅ Approvata il 16/10/2026 → 0301 |
| **Mekanism Tools** 10.7.19 | MIT | Ufficiale: attrezzi e armature in osmio, bronzo, acciaio. Si sovrappone a Truly Modular |

**Archivio — confronti già decisi**

**Zaino — confronto**

| | Sophisticated Backpacks | Traveler's Backpack | Backpacked 3 |
|---|---|---|---|
| NeoForge 1.21.1 | 3.26.12 (13/10/2026) + Sophisticated Core | 10.1.39 (29/08/2026) | 3.0.5 (03/04/2026), richiede Framework |
| Licenza | ARR (era GPL-3.0 fino a febbraio 2025) | LGPL-3.0 | LGPL-2.1 |
| Sviluppo | Release ogni pochi giorni | Circa mensile | Lento, molte issue aperte |
| Capienza | Da 27 a 120 slot, 1–7 upgrade (cuoio → netherite) | Da 27 a 99 slot, 2–6 upgrade + slot attrezzi | 9 slot, ampliabili spendendo XP |
| Funzioni | Magnete, raccolta, auto-alimentazione, rifornimento, scambio attrezzi, crafting, fornaci, incudine, serbatoi, batteria, compattazione, cestino… | Magnete, raccolta, auto-alimentazione, crafting, fornaci, serbatoi, cestino, sacco a pelo integrato, varianti a tema | Potenziamenti in stile vanilla: raccolta, semina, torce, riparazione; niente crafting né serbatoi |
| Dove si indossa | Slot del petto oppure slot schiena (Curios/Accessories) | Slot schiena (Curios/Accessories) | Slot proprio |
| Integrazioni | EMI, Mouse Tweaks, wrench di Create, chiavi di Storage Drawers; addon Create (zaini sui contraption) | EMI, backup degli zaini persi | — |
| Problemi noti | Duplicazione piazzandolo (#1719) | Crash se piazzato su una tramoggia (#1595) | Crash premendo Esc (#309); morte gestita solo con YIGD |

Consiglio: **Sophisticated Backpacks** (+ Core, eventualmente l'addon Create), indossato nello slot schiena per lasciare libero il pettorale. È il più completo e il più curato, e i suoi upgrade si sposano con Create, Mekanism e il cibo FD. Prezzo: licenza ARR (conta solo se un giorno si redistribuisce il pack o si vuole tutto open). Alternativa open: **Traveler's Backpack** (meno upgrade; il sacco a pelo integrato fa doppione con Comforts). Con Tombstone: provare una morte con lo zaino nello slot schiena.

Zaini dentro zaini (verificato nel codice, 16/10/2026):
- **Sophisticated dentro Sophisticated**: solo con l'**Inception Upgrade** (e lo zaino interno non deve averne uno a sua volta). Shulker box ammesse di default
- **Traveler's dentro Traveler's**: mai, è bloccato nel codice. Shulker box e altri oggetti con inventario solo attivando `allowShulkerBoxes` nella config
- **Traveler's dentro Sophisticated**: sì, di default
- **Sophisticated dentro Traveler's**: solo con `allowShulkerBoxes = true` nella config di Traveler's

Tenerli **entrambi** è possibile (l'utente ci sta pensando): lo slot schiena è uno solo, quindi uno si indossa (Traveler's si vede sulla schiena) e l'altro va nello slot del petto o resta nell'inventario (gli upgrade di Sophisticated funzionano anche da lì). Entrambi aprono con **B** → cambiare il tasto di uno.

**Ordinamento inventario — confronto**

| | Inventory Essentials | Client Sort | Inventory Profiles Next |
|---|---|---|---|
| NeoForge 1.21.1 | 21.1.20 (02/10/2026) | 3.89.2 (26/09/2026) | 2.2.5 (25/03/2026) |
| Licenza | ARR (sorgente visibile) | Apache-2.0 | AGPL-3.0 |
| Sviluppo | Molto attivo | Molto attivo | Ramo 1.21.1 fermo da marzo |
| Dipendenze | Balm (già presente) | Cloth Config | Kotlin for Forge + libIPN |
| Come si ordina | Click centrale | Pulsanti + click centrale | Pulsanti + tasto R |
| Ricarica attrezzi e stack | Sì | No | Sì (anche armature) |
| Slot bloccati / set di equipaggiamento | No (hotbar e armatura mai toccate) | Slot ignorati per contenitore | Sì / sì |
| Note | Stesso autore di Crafting Tweaks; disattivare `enableShiftDrag` (doppione di Mouse Tweaks) | Default già pensati per toolbox di Create, terminali di Tom's, Traveler's Backpack | La più completa ma la più macchinosa; da verificare con le versioni recenti di Kotlin for Forge |

Consiglio: **Inventory Essentials** (leggera, zero config, ricarica gli attrezzi, aggiornata spesso). Se conta più la licenza: **Client Sort** (open source, pulsanti visibili, ma niente ricarica). IPN solo se servono slot bloccati e set di equipaggiamento. Uno solo: usano tutti il click centrale. Sophisticated Backpacks ha già un suo ordinamento interno.

**Esito (16/10/2026)**: approvati il doppio zaino (Sophisticated + Traveler's) e Inventory Essentials → 0301.
