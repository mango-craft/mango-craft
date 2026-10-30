# Accessori che evolvono o si potenziano: ricerca del 23/10/2026

Ricerca in sola lettura per Mango Craft (Minecraft 1.21.1, NeoForge). Il repository non è stato toccato.
Legenda: **[V]** verificato (file, sorgente, API, con la fonte in fondo) · **[NV]** non verificato (pagina descrittiva, memoria o deduzione) · 🟢 consigliata · 🟡 dipende · 🔴 sconsigliata.

---

## 0. Risposte brevi

1. **Mod esterne che potenziano Artifacts.** Ce n'è **una sola diretta**: **Reliquified Artifacts**, che trasforma i 48 artefatti in reliquie della mod **Relics**, con livelli che salgono usandole. Però stravolge Artifacts. Ignora la nostra config, rompe il bottino delle nostre 152 casse e vuole esattamente Artifacts 13.2.5 [V]. Le altre strade sono deboli:
   - **BaublesReforked**: dà attributi casuali agli accessori Curios e li rifà sull'incudine. Codice chiuso: non si sa quali accessori tocchi.
   - **Tiered More**: con Accessories presente (è dentro l'Aether) spegne da sola il supporto a Curios, quindi agli artefatti non arriverebbe niente [V].
   - **Apothic Curios**: esiste solo per 1.20.1 Forge.
2. **Mod con accessori propri che crescono.** **Relics** ha 20 reliquie, livelli con l'uso, punti, rilancio delle statistiche e "rango". È in beta, ARR e usa Curios [V]. Poi:
   - **More Relics**, legata a build precise di Relics.
   - **L2 Artifacts**: set da GdR lungo, si potenziano con bottiglie d'esperienza.
   - **Baubley Heart Canisters**: cuori a gradi rosso → giallo → verde → blu.
   - **Ancient Forgemastery**: artefatti suoi, non Curios.

   Il resto aggiunge accessori nuovi ma non li fa crescere.
3. **Già nel pack.**
   - **Apotheosis non tocca gli accessori Curios.** La categoria Curios è commentata nel codice 8.9.0: affissi, gemme e rifacimento valgono solo per armi, armature e scudi negli slot vanilla [V]. L'unico accessorio di Apotheosis è il Talismano di pozione: con l'infusione al tavolo d'incantamento diventa indistruttibile [V].
   - **Catene vere** (si conserva l'oggetto o si sale di grado) [V]:
     - Ars Elemental: focus minore → focus, conservando i dati.
     - Ars Nouveau: anello dello sconto minore → maggiore.
     - Twilight Forest: 4 amuleti di grado 1 → 1 di grado 2 (vita, conservazione fino al 3).
     - Deep Aether: guanti e anello alla forgia.
     - Aether: guanti di diamante → netherite.
   - **Crescita con l'uso già presente** [V]:
     - Anello e pendente di zanite dell'Aether: più si consumano, più velocizzano lo scavo.
     - Guanti della fenice: in acqua diventano d'ossidiana.
     - Famiglio fabbro di Occultism: potenzia gli altri famigli.
   - **Config di Artifacts.** In `items.toml` ogni valore vale per un tipo di oggetto e per tutte le sue copie. Non ha livelli.
4. **Datapack.** Novità importante, verificata nel codice di Artifacts 13.2.5: le abilità degli artefatti sono **componenti dei dati dell'oggetto**, e i valori possono essere **numeri fissi** invece dei rimandi alla config [V]. Un datapack può quindi creare un **"Guanto potenziato"**: stesso oggetto `artifacts:power_glove`, ma con +6 danno invece di +4, nome, rarità e scintillio. Lo si ottiene con:
   - una ricetta (formato verificato);
   - un'infusione al tavolo d'incantamento di Apothic Enchanting (formato verificato);
   - una cassa del bottino.

   In più, il componente `curios:attribute_modifiers` di Curios aggiunge attributi o slot extra a un accessorio quando è indossato [V]. È il potenziamento vero più vicino all'idea che si possa fare senza mod nuove. **Non** si possono fare con un datapack: oggetti nuovi, effetti nuovi, livelli che salgono con l'uso.

**Raccomandazione:** 🟢 una prova pilota nel datapack, 3–5 artefatti con un "livello II" per infusione, dopo i test con `/give` della sezione 5. 🟡 Relics + Reliquified Artifacts solo se Matteo vuole proprio la crescita con l'uso, in un'istanza a parte e prima del mondo vero.

---

## 1. Mod candidate

| Mod (slug Modrinth) | 1.21.1 NeoForge: ultima versione | Licenza | Libreria accessori e dipendenze | Cosa fa | Contenuto | Giudizio |
|---|---|---|---|---|---|---|
| [Reliquified Artifacts](https://modrinth.com/mod/reliquified-artifacts) (`reliquified-artifacts`) | 1.0.9 **beta**, 12/10/2026 [V] | ARR | **Curios** (≥ 9.3.1), **Relics** ≥ 0.12.3, **OctoLib**, **Artifacts esattamente `[13.2.5]`** [V, `neoforge.mods.toml`] | Sostituisce, con gli stessi nomi `artifacts:*`, **tutti i 48 artefatti** con reliquie di Relics: abilità nuove, livelli, ranghi (sez. 2) | 48 oggetti rifatti, 1 oggetto nuovo (`mimi_dust`), slot nuovi `bracelet` e `charm` | 🟡 È proprio l'idea, ma rifà da capo gli artefatti e rompe config e bottino nostri |
| [Relics](https://modrinth.com/mod/relics-mod) (`relics-mod`) | 0.12.9 **beta**, 18/10/2026 [V] (tutte le 0.12.x sono beta) | ARR (uso nei modpack permesso dall'autore) | **Curios** ≥ 9.3.1, **OctoLib/ShatterLib** (`shatterbyte-lib`, ARR) [V] | Reliquie con livello che sale **usando l'abilità**; ogni livello dà un punto; abilità migliorate con punti + esperienza del giocatore; rilancio della qualità (costa esperienza); "rango" quando il livello è al massimo; abilità da sbloccare con una "ricerca" [V, codice] | **20 reliquie** nella 0.12.9 [V, `RelicsItems`], bottiglia d'esperienza per reliquie; si trovano nelle casse; config per ogni reliquia | 🟡 Mod autonoma interessante; i mantelli vanno nello slot `back`, lo stesso degli zaini |
| [More Relics](https://modrinth.com/mod/more-relics) | 1.7.7-forRelics-0.12.8, beta, 11/09/2026 [V] | ARR | Relics, Curios, OctoLib, Architectury [V] | Addon di Relics, con "evoluzioni" | 25+ reliquie | 🔴 Legata a build precise di Relics in beta |
| [L2 Artifacts](https://modrinth.com/mod/l2artifacts) | 3.0.7, 17/01/2026 [V] | LGPL-2.1 | Curios + L2 Library [V]; la pagina cita anche AttributeFix e MaxHealthFix [NV] | Set di artefatti con statistiche casuali; si salgono di livello con bottiglie d'esperienza all'incudine; qualità fino a 20 | Grande, pensata per "lunghe progressioni GdR" | 🔴 Si sovrappone ad Apotheosis e cambia il bilanciamento |
| [BaublesReforked](https://modrinth.com/mod/baublesreforked) | 1.0.3, 26/02/2026 [V] | ARR, codice non pubblico | Curios [V] | Attributi casuali sugli accessori, rifatti sull'incudine con materiali ed esperienza; esclusione per mod (changelog 1.0.2) [V]. **Quali accessori tocchi: NV** | Solo meccanica | 🟡 Da provare solo in un'istanza a parte; codice chiuso |
| [Tiered More](https://modrinth.com/mod/tiered-more) | 1.2.6, 03/10/2026 [V] | MIT | Architectury, Cloth Config; Curios e Accessories facoltativi [V] | Gradi e modificatori per armi, armature e accessori | Meccanica | 🔴 Con Accessories caricata spegne il supporto a Curios (`CuriosCompat.init`: `if (... Platform.isModLoaded("accessories")) return;`) [V], quindi niente per Artifacts; in più si sovrappone ad Apotheosis |
| [Baubley Heart Canisters](https://modrinth.com/mod/baubley-heart-canisters) | 1.21.1-1.4.1, 17/06/2026 [V] | MIT | Curios [V] | Cuori in un amuleto, a gradi rosso → giallo → verde → blu (+ anima), ognuno fatto anche dal grado precedente [NV, pagina] | Piccola | 🟡 Una vera catena a gradi, ma solo vita massima (si sovrappone al Cuore di cristallo) |
| [Artifacts Merging](https://modrinth.com/mod/artifacts-merging) | 1.2.1, 03/10/2026 [V] | MIT | Artifacts (Relics facoltativa nelle versioni vecchie) [V] | 2 artefatti (da 2 a 9 in config) → 1 artefatto **a caso** [NV, pagina] | Utilità | 🟡 Ricicla i doppioni, non potenzia |
| [Artifacts crafting](https://modrinth.com/mod/artifacts-crafting) | 1.1.2, 15/02/2026; 1.1.0-RPG, 22/03/2026 [V] | ARR | Artifacts [V] | Ricette per costruire ogni artefatto | Solo ricette | 🔴 Toglie l'esplorazione; non è un potenziamento |
| [Ancient Forgemastery](https://modrinth.com/mod/ancient-forgemastery) | 1.4.1, 23/04/2026 [V] | ARR, codice non pubblico | Nessuna dipendenza dichiarata [V]; Curios non citata | 10 "artefatti dorati" propri, potenziati su un altare [NV] | Piccola, con una struttura | 🔴 Non agisce sugli accessori Curios |
| [Psionic Relics](https://modrinth.com/mod/psionic-relics) | 1.0.2, 27/12/2025 [V] | MIT | Psi (obbligatoria), Curios (facoltativa) [V] | 7 reliquie per Psi in uno slot Curios; nessun livello; la Loopcast "rotta" [NV, pagina] | Piccola | 🟡 Solo se si usa Psi; non evolve |
| [More Curios Slots](https://modrinth.com/mod/more-curios-slots) | in elenco per 1.21.1 NeoForge [V]; versione non controllata | MIT | Curios | Oggetti costosi che aggiungono slot | Piccola | 🟡 Lo stesso si fa nel datapack (sez. 4.E) |
| Apothic Curios | **solo 1.20.1 / 1.19.2 Forge** [NV, modpackindex] | — | — | Affissi di Apotheosis sugli accessori Curios | — | Non esiste per 1.21.1 |
| [Apothic Category Compat](https://modrinth.com/mod/apothic-category-compat) | 1.21.1 [V] | MIT | Apotheosis ≥ 8.5 | Categorie di Apotheosis per armi e armature di altre mod | — | 🔴 Niente sugli accessori (pagina) |
| Accessori nuovi senza crescita: Dream Relics (MIT, Curios), Relics (RPG Series) (ARR, Spell Engine), Terra Curio (LGPL, 150+, Curios), BountifulBaubles:Reforked (ARR), Trinkets and Baubles Reforked (LGPL), Lost Trinkets Renewed, Nameless Trinkets, Moonstone | sì, 1.21.1 [V, ricerca Modrinth] | varie | Curios in gran parte | Aggiungono accessori, nessun livello [NV, pagine] | Da piccole a molto grandi | 🔴 Più accessori non vuol dire accessori che evolvono |

Già nelle nostre liste: **Enigmatic Legacy+** è scartata (port non autorizzato, `0602`). **Malum** è candidata e ha molti accessori Curios, ma nessun livello. Le categorie **Iron's Spells** ed **Equipaggiamento** (Apotheotic Creations e altre) erano state saltate.

---

## 2. Reliquified Artifacts nel dettaglio

Dal sorgente `Octo-Studios/rar-compat`, ramo 1.21.1, versione 1.0.9 [V]:
- **Conversione totale.** `ModItemsMixin` registra al posto degli artefatti (stessi nomi) **48 classi di reliquie**: la pagina Modrinth che dice "35%" è vecchia. Le abilità cambiano. Esempio, il Guanto del potere:
  - oggi: +4 danno fisso;
  - con la mod: "ogni N colpi, +X% danno", con modifiche ai ranghi 1 (rompe gli scudi), 3 (ignora l'armatura) e 5 (colpo a eco).
  - Esperienza: +1 per ogni Colpo potente, +1 per ogni uccisione con il Colpo potente.
- **La config di Artifacts non viene più letta.** `ConfigManagerMixin` e `ModConfigMixin` annullano `setup` e `readValuesFromConfig`, quindi valgono i valori di serie (`ConfigValue` parte dal valore di serie). Il nostro `enableAccessoriesCompat = false`, deciso il 16/10, tornerebbe `true`: gli artefatti tornerebbero anche nel menu di Accessories.
- **Il bottino degli artefatti cambia.** La mod riscrive `artifacts:roll_loot_table` in modo da scartare ogni reliquia. È proprio il tipo usato dai **15 file del nostro datapack** (`data/matteo_tweaks/loot_modifiers/artifacts/*.json`, campo `lootTable`): le **152 casse** non darebbero più artefatti. Le reliquie escono dal bottino proprio di Relics: il Guanto, per esempio, solo da miniere e grotte.
- **Slot.** Aggiunge lo slot `bracelet` (anello di cipolla, braccialetto avvizzito) e sposta 7 artefatti della cintura nello slot `charm`. Relics porta i suoi slot (`back`, `belt`, `charm`, `feet`, `hands`, `head`, `necklace`, `ring`, `curio`, tutti `size: 1`). I mantelli di Relics vanno in `back`, lo stesso degli zaini. Come si sommano con gli slot di Ars e Artifacts: [NV].
- **Versione bloccata.** Ogni aggiornamento di Artifacts richiede una nuova Reliquified Artifacts (1.0.8 voleva 13.2.3, la 1.0.9 vuole 13.2.5).
- **Quando.** Cambia oggetti e bottino, quindi va decisa **prima del mondo vero**.

---

## 3. Cosa c'è già nel pack

| Mod (versione nel pack) | Accessori | "Versione migliore = altro oggetto" | Potenziamento vero dello stesso oggetto | Fonte |
|---|---|---|---|---|
| **Artifacts** 13.2.5 | 48 artefatti (45 indossabili + ombrello, manzo eterno e bistecca eterna) | Nessuna: nessuna ricetta di accessori (solo la cottura della bistecca), nessuna etichetta di incantabilità [V, inventario] | **Config**: una sezione per oggetto in `items.toml`, valori globali per tutte le copie, nessun livello [V]. **Componenti**: le abilità sono componenti dei dati con valore da config **o costante** (`ValueType.codec()` = alternativa tra rimando alla config e costante); Artifacts li legge **dalla singola copia** (`stack.get(type)` in `EquipmentHelper.reduceAbilities`) [V]. Quindi si possono fare copie potenziate col datapack (sez. 4.B) | jar, config, sorgente |
| **Apotheosis** 8.9.0 + Apothic Attributes 2.11.0 + Apothic Enchanting 1.6.4 | Talismano di pozione (`curios:charm`) | — | Affissi, gemme, rifacimento e **potenziamento degli affissi** (Augmenting: 2 sigilli + 225 livelli) solo per le categorie bow, breaker, helmet, chestplate, leggings, boots, shield, trident, melee_weapon, shears, ognuna legata a slot **vanilla**. La categoria Curios è **commentata** in `compat/curios/CuriosCompat.java` ("Experimental"). Apothic Attributes ha il tipo `CurioEquipmentSlot` ma **non ne registra nessuno**. La data map `apotheosis:loot_category_overrides` dà una categoria a un oggetto, ma gli attributi varrebbero solo negli slot vanilla → **no sugli accessori** [V]. **Talismano**: infusione al tavolo d'incantamento → `minecraft:unbreakable` (`CharmInfusionRecipe`; requisiti eterna 100, quanta 8,5–13,5, arcana 32,5–37,5) [V]. Config: `Restrict Charms to Curios = false` | jar, sorgente, `apotheosis.cfg` |
| **Ars Nouveau** 5.13.3 | 14 (anelli, amuleti, cinture, corona, focus) | Anello del potenziale → **sconto minore → sconto maggiore** (Apparato, reagente = anello minore, `keepNbtOfReagent: false`); ninnolo opaco → amuleti; cintura comune → cinture | Armature con fili e potenziamento di grado (`armor_upgrade`, non sono accessori) | sorgente, inventario |
| **Ars Elemental** 0.7.10.4 | 19 | Anello del potenziale → bracciale base → 6 bracciali elementali; focus d'evocazione → focus necrotico | **Focus minore → focus** (4 elementi, Apparato con Marchio di maestria, `keepNbtOfReagent: true`) | sorgente |
| **The Aether** 1.5.10 (menu suo, Accessories) | 32 | Anelli e pendenti fatti direttamente da ferro, oro o zanite (non in catena); anello/pendente di ferro o d'oro → **di ghiaccio** (Congelatore); guanti per materiale | Guanti di diamante → **netherite** (forgia); **zanite**: velocità di scavo × (1,4 + usura / (3 × durata massima)), quindi cresce **consumandosi**; guanti della **fenice → d'ossidiana** in acqua o pioggia; riparazione all'Altare | jar, sorgente (ramo 1.21.1-develop) |
| **Deep Aether** 1.1.5.1 | 13 | — | Forgia: guanti di skyjade → **stormforged**; guanti di gravitite → **stratus**; anello di gravitite → **anello stratus** | jar |
| **Twilight Forest** 4.8.3345 | 23 (amuleti, trofei) | **4 × amuleto della vita 1 → 2**; **4 × amuleto della conservazione 1 → 2 → 3** (senza forma) | — (gli amuleti si consumano alla morte) | sorgente |
| **Unusual End** 2.3.1 | 14 | Sfera del golem → sfere di fiamma, shulker e avvizzimento (con citrino + materiale); più sfere indossate sommano gli effetti | — | jar |
| **Occultism** 1.224.5 | 6 (anello del famiglio, occhiali…) | — | Il **famiglio fabbro** potenzia altri 16 tipi di famigli (18 ferro, `blacksmithFamiliarUpgradeCost`) | sorgente (ramo version/1.21.1) |
| **L_Ender's Cataclysm** 3.33 | 13 | Ci sono ricette per cintura del principiante, prese ardenti e guanti appiccicosi; nessuna catena visibile (contenuto non leggibile: jar non disponibile, sorgente non pubblico) [NV] | Fusione d'armi (Incudine a fusione meccanica) solo per armi | inventario |
| **Starcatcher** 3.3.6 | 18 (cappelli da pescatore in 16 colori, radar) | — | Potenziamenti delle canne alla forgia (non sono accessori) | inventario |
| **Psi**, **Hexerei**, **Cognition** | Psi nessuno; Hexerei occhiali; Cognition 2 amuleti | — | Psi: componenti del CAD e sensori; Hexerei: amuleto del corvo (per il famiglio) e portachiavi della scopa | inventario |
| **Zaini** (Sophisticated Backpacks 3.26.12, Traveler's Backpack 10.1.39) | slot `back` | — | Zaino → rame → ferro → oro → diamante → netherite **conservando il contenuto** (`backpack_upgrade`, `smithing_backpack_upgrade`) | inventario |

---

## 4. Idee fattibili con il datapack (Paxi, `matteo_tweaks`)

Regole del pack valide anche qui: condizione `neoforge:conditions` in ogni file; nomi in minuscolo; nomi verificati sull'inventario. Lo script `scripts/check_ids.py` **non controlla i componenti**: in 330 righe non compare la parola "component" [V]. Che accetti gli ingredienti `neoforge:components` e `neoforge:difference`: [NV].

### A. Ricette di passaggio verso un oggetto esistente (🟢 semplice, poco valore)
- Aether: anello o pendente di ferro o d'oro + zanite → di zanite. Gli anelli e i pendenti di ferro e d'oro non hanno un'abilità propria [NV].
- Guanti dell'Aether a gradi (cuoio → cotta di maglia → ferro → oro → diamante) **alla forgia**, così da conservare gli incantesimi come fa la netherite. Che i componenti del risultato si applichino alla forgia: [NV].
- Per Artifacts non ci sono "fratelli" più forti: un passaggio A → B fra artefatti sarebbe uno scambio, non un potenziamento.

### B. Lo stesso artefatto potenziato tramite componenti (🟢 l'idea principale)
Ogni artefatto ha le sue abilità come componenti; un risultato di ricetta o una voce di bottino può portarli con **valori costanti** [V, sorgente]. Esempi di componenti (Artifacts 13.2.5):
- `artifacts:attribute_modifiers`: lista di `{attribute, amount, operation, id}`; l'`id` di serie è `artifacts:<oggetto>/<percorso dell'attributo>`. Esempio: `artifacts:power_glove/generic.attack_damage`.
- `artifacts:enchantment_level_modifiers`: lista di `{enchantment, level}` (Sciarpa fortunata: Fortuna).
- `artifacts:tool_tier_upgrade`: `{tier}` (Artigli da scavo: `stone` → `iron`).
- Altri: `double_jump`, `mob_effects`, `attack_effects`, `retaliation_effects`, `damage_absorption`…

Componenti vanilla utili: `minecraft:custom_name`, `minecraft:lore`, `minecraft:rarity`, `minecraft:enchantment_glint_override`, e `minecraft:custom_data` come marcatore di livello.

**Tre stazioni possibili:**
1. **Tavolo da lavoro.** Risultato con `components`: formato verificato nei jar del pack (`apotheosis:book.json`, `aether:swet_banner.json`).
2. **Infusione al tavolo d'incantamento** (Apothic Enchanting): `apothic_enchanting:infusion` con `input`, `requirements`/`max_requirements` (eterna, quanta, arcana) e `result` (`ItemStack.CODEC`, quindi con componenti) [V, `InfusionRecipe`]. È **la più coerente col pack**, perché i livelli diventano tappe dell'incantamento. Non usare `keep_nbt_infusion`: copia i componenti dell'ingresso **sopra** quelli del risultato, e un livello II diventerebbe di nuovo livello I [V].
3. **Forgia.** Conserva gli incantesimi; il comportamento con i componenti del risultato è da provare [NV].

**Livelli distinti:** per non rifare all'infinito lo stesso livello, l'ingresso del livello I esclude i già potenziati con `{"type":"neoforge:difference","base":{"item":"artifacts:power_glove"},"subtracted":{"type":"neoforge:components","items":"artifacts:power_glove","components":{"minecraft:custom_data":{"mango_livello":2}}}}`. Il livello II → III usa direttamente `neoforge:components` con `mango_livello: 2`. Entrambi i tipi esistono in NeoForge 1.21.1 (campi `base`/`subtracted` e `items`/`components`/`strict`) [V]. Che l'infusione accetti questi ingredienti: [NV].

**Esempio di infusione** (da provare prima con `/give`):
```json
{
  "neoforge:conditions": [
    {"type": "neoforge:mod_loaded", "modid": "artifacts"},
    {"type": "neoforge:mod_loaded", "modid": "apothic_enchanting"}
  ],
  "type": "apothic_enchanting:infusion",
  "input": {
    "type": "neoforge:difference",
    "base": {"item": "artifacts:power_glove"},
    "subtracted": {"type": "neoforge:components", "items": "artifacts:power_glove",
                   "components": {"minecraft:custom_data": {"mango_livello": 2}}}
  },
  "requirements": {"eterna": 30, "quanta": 15, "arcana": 10},
  "max_requirements": {"eterna": 40, "quanta": 30, "arcana": 30},
  "result": {
    "id": "artifacts:power_glove",
    "count": 1,
    "components": {
      "artifacts:attribute_modifiers": [
        {"attribute": "minecraft:generic.attack_damage", "amount": 6.0,
         "operation": "add_value", "id": "artifacts:power_glove/generic.attack_damage"}
      ],
      "minecraft:rarity": "epic",
      "minecraft:enchantment_glint_override": true,
      "minecraft:custom_data": {"mango_livello": 2}
    }
  }
}
```
**Limiti:**
- I valori costanti **non seguono più `items.toml`**.
- Dopo un aggiornamento di Artifacts i nomi dei componenti vanno ricontrollati: nel codice c'è un `TODO (>1.21.1)` sui componenti.
- Non si possono indossare due copie dello stesso artefatto (scheda `artifacts`).
- Il bilanciamento lo decidiamo noi.

### C. Attributi o slot in più con `curios:attribute_modifiers` (🟡)
Formato [V, Curios 9.5.1]: `{"modifiers":[{"type":"<attributo>","id":"<ns:nome>","amount":2.0,"operation":"add_value","slot":"hands"}],"show_in_tooltip":true}`. L'attributo vale **solo** quando l'oggetto è nello slot indicato. Con `type` = `curios:<slot>` dà **uno slot in più**, per esempio `curios:ring` +1.

Attenzione: se il componente c'è, **sostituisce** i modificatori Curios propri dell'oggetto. Per Artifacts non è un problema, perché il suo `WearableArtifactCurio` non ne definisce: gli effetti passano dai suoi componenti [V]. Per gli accessori di altre mod va controllato oggetto per oggetto.

### D. Bottino potenziato (🟢)
Tabelle nostre (`matteo_tweaks:…`) con `minecraft:set_components`, iniettate nelle casse dei boss o dei tesori con lo stesso tipo che usiamo già, `artifacts:roll_loot_table` (campo `lootTable`). Per esempio, una piccola probabilità di un artefatto di "livello II" nelle casse finali.

### E. Numero di slot (🟢, risponde al tema aperto «formato da verificare»)
File `data/<ns>/curios/slots/<slot>.json` con `size`, `operation` (`SET`/`ADD`/`REMOVE`, di serie `SET`), `replace`, `add_cosmetic`, `drop_rule`… [V, `CuriosSlotManager`]. Le entità si assegnano con `data/<ns>/curios/entities/*.json` (`entities`, `slots`).

### F. Non fattibile col datapack
Oggetti nuovi, effetti nuovi, livelli o esperienza che crescono con l'uso, affissi e gemme di Apotheosis sugli accessori Curios (servirebbe una mod che registri le categorie: Apothic Curios non esiste per 1.21.1), fondere due artefatti in uno a caso.

---

## 5. Cosa provare in gioco (istanza di prova)

1. **Componente di Artifacts:** `/give @s artifacts:power_glove[artifacts:attribute_modifiers=[{attribute:"minecraft:generic.attack_damage",amount:6.0,operation:"add_value",id:"artifacts:power_glove/generic.attack_damage"}]]`. Atteso: il tooltip mostra +6 e, indossato, il danno sale (schermata degli attributi di Apothic Attributes).
2. **Altri componenti:** Sciarpa fortunata con `artifacts:enchantment_level_modifiers=[{enchantment:"minecraft:fortune",level:2}]`; Artigli da scavo con `artifacts:tool_tier_upgrade={tier:"iron"}`.
3. **Attributo Curios:** `/give @s artifacts:lucky_scarf[curios:attribute_modifiers={modifiers:[{type:"minecraft:generic.armor",id:"matteo_tweaks:prova",amount:2.0,operation:"add_value",slot:"necklace"}]}]`. Atteso: +2 armatura solo indossata nella collana, e la Fortuna funziona ancora.
4. **Slot in più:** lo stesso con `type:"curios:ring"`, `amount:1`. Atteso: un anello in più nel menu Curios.
5. **Ricetta di prova** (tavolo da lavoro e infusione) con risultato a componenti: compare in JEI/EMI, si fabbrica, gli ingredienti `neoforge:difference`/`neoforge:components` filtrano i livelli. Verificare anche il comportamento alla **forgia**.
6. **Apotheosis:** un artefatto non entra nel tavolo del rifacimento e non riceve incastonature (conferma della categoria `none`).
7. **Solo se si valuta Reliquified Artifacts**, in un'istanza separata (non dev):
   - nessun artefatto nelle 152 casse nostre;
   - artefatti presenti anche nel menu di Accessories;
   - zaino e mantello di Relics nello slot `back`;
   - schermata di ricerca e livelli di Relics;
   - errori nel log.

---

## 6. Fonti

**Repository e file locali**
- `1.21.1/theme-knowledge/accessori.md`, `1.21.1/lavoro/0601-mod-candidate.md`, `0602-mod-scartate.md`, `0503-temi-aperti.md`, `1.21.1/mod-knowledge/artifacts.md`.
- Inventario: `1.21.1/data/inventario/mods/*.json` (tag `curios:*`, ricette, tipi di ricetta, versioni).
- Datapack: `1.21.1/pack/config/paxi/datapacks/matteo_tweaks/data/matteo_tweaks/loot_modifiers/artifacts/*.json`.
- `scripts/check_ids.py`.
- Jar letti con `python3 -I` + `zipfile`: `artifacts-neoforge-13.2.5`, `Apotheosis-1.21.1-8.9.0`, `ApothicAttributes-1.21.1-2.11.0`, `aether-1.21.1-1.5.10-neoforge`, `deep_aether-1.21.1-1.1.5.1`, `unusualend-2.3.1b`.
- Config: `config/artifacts/items.toml`, `general.toml`, `config/apotheosis/apotheosis.cfg`.

**Sorgenti** (cloni in `/tmp/claude-0/-home-claude/d3876890-5907-520c-8a85-0a2ec892bcbc/scratchpad/repos/`)

| Progetto | Commit, data | Versione |
|---|---|---|
| Shadows-of-Fire/Apotheosis | 7dd7cec | 8.9.0 |
| Apothic-Attributes | d596c09 | 2.11.0 |
| Apothic-Enchanting | 3df39de | 1.6.4 |
| ochotonida/artifacts | 7cf7dc4 | 13.2.5 |
| TheIllusiveC4/Curios | 6b122c8 | 9.5.1 |
| SSKirillSS/relics, ramo 1.21.1 | da846fc, 22/10/2026 | 0.12.9 |
| Octo-Studios/rar-compat, ramo 1.21.1 | 2b6d624, 22/10/2026 | 1.0.9 |
| NeoForge, ramo 1.21.1 | 00c6a3f, 14/10/2026 | `DataComponentIngredient`, `DifferenceIngredient`, `NeoForgeMod` |
| Ars-Nouveau | fd8c952 | 5.13.3 |
| Ars-Elemental | b1b1e1d | 0.7.10.4 |
| twilightforest, ramo 1.21.1 | 9e40a75 | 4.8 |
| occultism, ramo version/1.21.1 | 354da9f, 11/10/2026 | — |
| The-Aether, ramo 1.21.1-develop | e07d30e | — |
| KevzCz/tiered, ramo 1.21.1-arch | 2962360 | 1.2.6 |

**API di Modrinth:** ricerche `relics`, `artifacts`, `curios`, `trinkets`, `accessories`, `baubles`, `affix`, `apothic`, `tiered`, `leveling`, `reforge`, con i filtri 1.21.1 + NeoForge. Progetti e versioni per 1.21.1 + NeoForge: `reliquified-artifacts` (incluse le versioni `1.0.8` e `1.0.9`), `relics-mod`, `more-relics`, `arcane-abilities`, `shatterbyte-lib`, `l2artifacts`, `baublesreforked`, `curio-attribute-fantasy`, `tiered-more`, `baubley-heart-canisters`, `artifacts-merging`, `artifacts-crafting`, `ancient-forgemastery`, `compat-artifacts`, `terra-curio`, `bountifulbaublesreforked`, `psionic-relics`, `more-curios-slots`, `ancient-reforging`, `apothic-category-compat`, `relics-rpg`, `dream-relics`.

**Web (non verificato nel codice)**
- [Apothic Curios su modpackindex](https://www.modpackindex.com/mod/53914/apothic-curios): solo 1.20.1/1.19.2 Forge.
- [BaublesReforked su mado-hosting](https://www.mado-hosting.com/minecraft-mods/baublesreforked).
- [Apothic Compats su 9minecraft](https://www.9minecraft.net/apothic-compats-mod/): nessun accenno agli accessori.
