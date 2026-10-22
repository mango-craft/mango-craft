# Tema: strumenti con materiali avanzati

Aggiornata il 23/10/2026 · stato: **valutazione iniziale** (idea di Matteo, `../lavoro/0503-temi-aperti.md`) · mod coinvolte: The Twilight Forest, The Aether, Deep Aether, The Undergarden, Deeper and Darker, Occultism, L_Ender's Cataclysm, Unusual End, Mekanism, Truly Modular (Modular Item API, Armory, Arsenal, Archery) · fonti: inventario del pack (oggetti, tag dei livelli di scavo, dati `miapi` letti dai .jar). Statistiche dei materiali (durata, velocità, danno) **non ancora lette**: stanno nel codice delle mod.

## Fatti verificati (inventario, 23/10)

- **Set di strumenti delle mod** (conteggio dei picconi): Twilight Forest 6 (ironwood, steeleaf, knightmetal, fiery, giant, mazebreaker), Aether 5 (skyroot, holystone, zanite, gravitite, valkyrie), Undergarden 4 (cloggrum, froststeel, utherium, forgotten), Deep Aether 2 (skyjade, stratus), Deeper and Darker 2 (resonarium, warden), Occultism 2 (infused, iesnium), uno ciascuno Cataclysm (black steel), Unusual End (pearlescent), Cognition, Psi, Scriptor, Create Confectionery; più il Meka-Tool di Mekanism.
- **Livelli di scavo**: quasi tutte le mod usano i livelli vanilla (`needs_stone/iron/diamond_tool`). Hanno cancelli propri solo: **Undergarden** (alcuni blocchi sono in `incorrect_for_netherite_tool` e richiedono gli strumenti `forgotten`), **Twilight Forest** (un tag `incorrect_for_<materiale>_tool` per materiale), **Deeper and Darker** (resonarium, warden) e **Mekanism** (Meka-Tool). Quindi oggi le tappe vere sono date dall'**accesso alle dimensioni e ai boss**, non dal livello di scavo.
- **Truly Modular**: i 110 materiali definiti nei dati (`miapi/materials`) sono **solo vanilla** (legni, pietre, rame, ferro, oro, netherite, cristalli, ossa…); Armory e Arsenal aggiungono estensioni e incastonature per materiali vanilla. I materiali delle mod (zanite, knightmetal…) non sono nei dati: o Truly Modular li ricava da solo dagli strumenti delle mod, o non si possono usare. **Da verificare in gioco** (banco modulare con un lingotto di zanite).

## Valutazione iniziale (23/10)

- 🟢 **Prima l'analisi**, con lo stesso metodo dei vasi: tabella dei materiali con il momento in cui si ottengono (dimensione, boss, struttura) e le statistiche lette dai .jar; ne esce una scala, e si vede dove ci sono salti o doppioni.
- 🟡 **Truly Modular come asse portante**: i suoi materiali sono dati (file JSON con le statistiche), quindi una progressione si potrebbe scrivere nel datapack senza riscrivere le ricette di decine di strumenti. Dipende dalla verifica qui sopra.
- 🟡 **Cancelli nelle ricette** (es. il materiale del gradino prima tra gli ingredienti del successivo, come la netherite): fattibile nel datapack, ma sono molte ricette (5–6 strumenti per materiale) e cambia il bilanciamento delle mod.
- 🔴 **Cambiare i livelli di scavo dei blocchi**: tocca il mondo di tutte le mod, rischioso.
- Vincolo: il datapack non crea oggetti nuovi e non cambia le statistiche scritte nel codice; può cambiare ricette, tag, bottino e i dati di Truly Modular.

## Rimandi

- Temi aperti: `../lavoro/0503-temi-aperti.md`, sezione 2. Metodo di analisi: `../mod-knowledge/botany-pots/analisi.md`.
