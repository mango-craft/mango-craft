# Tema: pozioni ed effetti

Aggiornata il 24/10/2026 · stato: **analisi iniziale**, nessuna decisione (richiesta di Matteo del 24/10, `../lavoro/0503-temi-aperti.md`) · mod coinvolte: tutte quelle con effetti o pozioni (sotto) · fonti: inventario del pack; scansione dei 253 jar dell'istanza di prova (traduzioni inglesi e nomi nelle classi, script in `../../ai-agents/stage/2026-10-24_pozioni/`); sorgente di Create (`PotionMixingRecipes`, ramo `mc1.21.1/dev`, commit `7ff2760`); jar di Apotheosis 8.9.0 e Born in Chaos 1.7.6; config dell'istanza di prova. Schede vicine: `cucina.md` (bevande), `accessori.md`, `esperienza.md`.

**Cosa non si vede dai file**: durate, livelli e ricette dell'alambicco aggiunte dalle mod stanno nel codice. I numeri qui sotto contano ciò che esiste; come si ottiene ogni pozione si legge in gioco (EMI) o nel sorgente della mod.

## Cose da non rompere (e leve che abbiamo)

- **Amuleti di pozione di Apotheosis**: si fanno con 3 pozioni e 6 polveri di blaze e danno l'effetto **finché sono nell'inventario** (o in uno slot di Curios, se la config lo chiede: oggi no, `Restrict Charms to Curios=false`); con Apothic Enchanting si rendono infrangibili. La lista nera è un'**etichetta di pozioni** nel datapack, `apotheosis:potion_charm_blacklist`, oggi **vuota**: qualsiasi pozione di qualsiasi mod può diventare un effetto permanente. È la leva più forte che abbiamo sul bilanciamento delle pozioni.
- **Automazione con Create**: il Mescolatore prepara le pozioni nella bacinella convertendo da solo le ricette dell'alambicco, ma solo quelle «semplici» (le miscele del gioco base, comprese quelle che le mod aggiungono con `addMix`, e le `BrewingRecipe` di NeoForge). Le ricette scritte come classi proprie (`IBrewingRecipe`) **non** passano: è il caso delle 12 ricette di Born in Chaos (verificato nel jar). Ogni pozione diversa è un **liquido diverso** per Create, anche se dà lo stesso effetto.

## Il censimento (24/10/2026)

- **Effetti**: 344 in 30 mod (inventario). I più numerosi: Born in Chaos 54, Jaden's Nether Expansion 28 (24 sono «immunità» a un effetto), Corail Tombstone 27, Ars Nouveau 19, Ars Elemental 18, Cataclysm 15, Vinery 15, Hexalia 11, Farm & Charm 10. Molti sono **solo dei mostri o dei boss** (debuff di Cataclysm, Born in Chaos, Aquamirae, Mowzie's) o **solo dei cibi e delle bevande**.
- **Pozioni registrate**: 96 contando le varianti lunghe e forti, circa 70 diverse, in 18 mod: Ars Nouveau 6 (esplosione, gelo, rigenerazione del mana, recupero, scudo, danno degli incantesimi), Unusual End 13, Corail Tombstone 10, Apothic Attributes 11, Nether Depths Upgrade 4, Undergarden 4, Born in Chaos 4, Ars Elemental 2, Bountiful Fares 2, Deeper and Darker 2, Friends & Foes 2, Reactive 2, una ciascuna Mowzie's, Occultism, Rustic Delight, Deep Aether, Illager Invasion, Mutant Monsters.
- **Ricette dell'alambicco nel codice**: circa 16 mod (le stesse delle pozioni, più Paraglider).
- **Altri sistemi per ottenere effetti** (ricette nei file, dall'inventario):

| Sistema | Mod | Cosa fa |
|---|---|---|
| Calderone da mescola | Hexerei | 37 ricette; scaldato prepara anche le pozioni dell'alambicco; candele con 14 effetti ad area (`../docs/0301-mod.md`) |
| Calderone e infusione celeste | Hexalia | 8 + 6 ricette; effetti con un vantaggio e un difetto (Bloodlust, Spikeskin, Slimewalker…) |
| Bollitore e calderone | HerbalBrews | 10 ricette; tè con effetti **per i giocatori vicini** (Tough, Feral, Fortune, Lifeleech…) |
| Botte e fermentazione | Brewin' and Chewin' | 48 ricette; alcolici (Tipsy, Raging, Sweet Heart) |
| Distillazione | Delightful Fares | 7 ricette (tè) |
| Calderone degli aspetti | Aspect Alchemy | effetti vanilla fino al livello V, ma solo da 49 oggetti vanilla fissati nel codice |
| Crogiolo | Reactive Alchemy | effetti ad area con regole diverse in ogni mondo |
| Infusione e amuleti | Apotheosis / Apothic Enchanting | amuleti di pozione (sopra) |
| Fiaschette e incantesimi | Ars Nouveau | fiaschette di pozione; molti effetti vengono dagli incantesimi |
| Cibi e vini | Farmer's Delight e addon, Let's Do (Vinery 15 effetti, Farm & Charm 10), Bountiful Fares, Roaster's Delight | effetti dei cibi, spesso forti (Vinery: camminare sull'acqua e sulla lava, doppio salto, magnete) |
| Accessori, famigli, preghiere | Artifacts, Occultism, Corail Tombstone | effetti continui finché si indossa o si è legati |

## Sovrapposizioni

**Pozioni diverse per lo stesso effetto vanilla** (nessun errore, ma doppioni in EMI e liquidi diversi in Create):

| Effetto | Pozioni |
|---|---|
| Rapidità (haste) | Apothic Attributes, Unusual End (normale e «avanzata»), Rustic Delight |
| Resistenza | Apothic Attributes, Unusual End, Nether Depths (pesce d'ossidiana) |
| Bagliore (glowing) | Undergarden, Deeper and Darker, Nether Depths |
| Levitazione | Apothic Attributes, Unusual End |
| Avvizzimento (wither) | Apothic Attributes, Nether Depths |
| Rigenerazione, forza | gioco base e Unusual End (che aggiunge anche rigenerazione II) |
| Aumento della salute, assorbimento, affaticamento, oscurità | Unusual End, Apothic Attributes, Corail Tombstone |

**Stesso nome, effetti diversi o quasi uguali** (confondono nell'elenco degli effetti):
- *Stun* in quattro mod (Cataclysm, Truly Modular, Born in Chaos, Hexalia); *Bleeding* in due (Apothic Attributes, Hexalia); *Frozen/Freezing/Frosted/Frostbite/Chilly* in sei;
- *Reach* in quattro (Friends & Foes, Corail Tombstone, Reactive, Undergarden Delight), oltre all'attributo di Apothic Attributes;
- *Intoxication* in tre (Born in Chaos, Cultural Delights, Brewin' and Chewin') più l'*Inebriation* dell'Aether;
- *Glide*: in Friends & Foes rende scivoloso il terreno, in Ars Nouveau fa planare come con le elitre;
- *Double Jump* (Vinery, Occultism), *Lifesteal* (Born in Chaos, Occultism, HerbalBrews, Hexalia), *Bone Fracture* (Cataclysm, Born in Chaos), *Phasing* (Ender's Delight, Scriptor), *Stimulation* (Create Confectionery, Born in Chaos), *Magnet* (Vinery, Artifacts, Hexalia).

**Effetti che bloccano o puliscono gli altri**: Cheesy (Cultural Delights), Eclipse (Mowzie's), Stupor (Bountiful Fares), Farmer's Blessing (Farm & Charm), le 24 immunità di Jaden's. **Acidic** (Bountiful Fares) fa il contrario: alza di un livello tutti gli altri effetti.

## Rischi di bilanciamento

Con la lista nera degli amuleti vuota, diventano permanenti anche effetti pensati per durare poco. I più delicati (nomi dalle pozioni registrate; l'effetto preciso va visto in gioco):
- **Flying** di Apothic Attributes (dal nome, volo: da verificare);
- **Serenity** di Unusual End (protegge da cadute, fame e alcuni effetti negativi), **Swift Strikes**, rapidità «avanzata»;
- **Acidic** di Bountiful Fares (alza tutti gli altri effetti di un livello);
- **Giant Strength** e **Little World** di Corail Tombstone; **Weightless** (no_gravity) di Reactive;
- scudo, recupero e danno degli incantesimi di Ars Nouveau.

Effetti dei cibi e dei vini spesso equivalgono a pozioni forti e non costano un alambicco: è un tema della cucina (`cucina.md`), da guardare insieme.

## Strade possibili (da decidere)

1. 🟢 **Lista nera degli amuleti** nel datapack: un file, le pozioni che non devono diventare permanenti. Piccola, reversibile, da fare prima del mondo vero.
2. 🟢 **Censimento nella base dati**, come per vasi e mercato: inventario esteso a pozioni ed effetti (da traduzioni e classi), tabelle `EFFETTO`, `POZIONE`, `FONTE`, e una nostra classificazione (beneficio, danno, utilità; potenza) da cui generare la lista nera e le altre scelte.
3. 🟡 **Automazione** delle pozioni che Create non converte (Born in Chaos): ricette del Mescolatore scritte da noi, se servono.
4. 🟡 **Doppioni**: nasconderli in EMI (da verificare come) o lasciarli.
5. 🟡 **Una progressione delle pozioni** (alambicco → calderoni delle mod → amuleti), legata alla rarità come i terreni e il mercato.
