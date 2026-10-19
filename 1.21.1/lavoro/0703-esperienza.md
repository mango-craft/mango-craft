# Esperienza: deposito e farm — ricerche

> **Documento storico**: fotografia del momento in cui è stato scritto, non si aggiorna. Lo stato attuale è nei documenti vivi (vedi il README della cartella).

Due ricerche del 17/10/2026: la prima analisi in italiano (verificata nei sorgenti) e la ricerca completa in inglese che ha portato a Cognition. Decisioni: XP Tome e Cognition approvate (`0611-round-2026-10-17.md`); regole sui liquidi in `../docs/0303-note-tecniche.md`.

## Prima analisi (in italiano)

**Già possibile senza aggiunte**
- **Create: Enchantment Industry**: esperienza liquida (1 mB = 1 punto) in qualsiasi serbatoio di Create o Mekanism, mossa con tubi e Pipez. **Experience Hatch** su un serbatoio = banca XP (click per depositare, accovacciato per prelevare, quantità da 10 a 1000 punti o "tutto"). **Experience Lantern** risucchia le sfere entro 10 blocchi (⚠️ succhia anche il giocatore che la tocca). Macina meccanica: pepite e blocchi di esperienza e gemme di Ars → liquido; Item Drain: bottiglie d'incantesimo → 10 mB; Spout: liquido → bottiglie
- **Uccisioni automatiche**: il Deployer con spada dà XP grazie a CEI (in pepite nel suo inventario); le seghe e le altre uccisioni non da giocatore non danno XP (regola vanilla)
- **Apothic Spawners**: spawner prendibili con Tocco di velluto e potenziabili (ritardo, numero, ignora giocatori, nessuna IA, controllo redstone, silenziosi, frammento di eco = XP × fino a 4). La Mega Torcia blocca solo gli spawn naturali, non gli spawner
- **Occultism**: Campo di battaglia dimensionale (rituale dell'Afrit) simula le uccisioni da un mob catturato e dà bottino + 1 bottiglia d'incantesimo ogni 10 XP
- **Ars Nouveau**: gemme dell'esperienza (3 e 12 punti, impilabili) dalla henge del Drygmy e dal Rituale di disintegrazione
- **Sophisticated Backpacks**: l'upgrade Pompa XP (con upgrade Serbatoio) accetta solo i fluidi `c:experience` (20 mB per punto) e **non** il liquido di CEI. Non unirli via tag: rapporto 1 contro 20 → guadagni o perdite di XP
- Altro: ricompense XP dei Gateways; zaino Lapis di Traveler's (15% di XP doppia); Knowledge of the Ages di Apothic Enchanting (bottino → XP, solo uccisioni del giocatore)

**Candidate (build ufficiali NeoForge 1.21.1)**
| Mod | Versione · licenza | Cosa fa | Sovrapposizione |
|---|---|---|---|
| **XP Tome** | 2.4 (ottobre 2024) · MIT | Libro che contiene 1395 punti (configurabile), portatile | Piccola |
| **Global XP** | 1.12 (agosto 2024) · MIT | Blocco banca XP quasi infinita, raccoglie le sfere vicine | Hatch + serbatoio di CEI |
| **Mob Grinding Utils** | 1.1.10 (luglio 2025) · ARR · **solo CurseForge** | Kit classico per farm: Mob Masher (conta come giocatore), tramoggia che assorbe XP, serbatoi, rubinetto XP, spawner. Fluido `c:experience` → abilita la pompa XP degli zaini (mantieni livello) | Deployer + CEI, Apothic Spawners |
| **Cognition** (ex Experience Obelisk) | 2.4.13 (luglio 2026) · MIT | Obelisco da ~1000 livelli + molto altro | CEI; tanti contenuti estranei |
| **Bottle Your Xp** | 3.6 · ARR | Imbottiglia XP col click | Lo Spout di CEI lo fa già |
| **Easy Mob Farm** | 11.0.0 · MIT | Blocchi farm da mob catturati, XP solo come bottiglie (1 su 5) | Campo di battaglia di Occultism |

Escluse: Ender IO (solo beta), Cyclic (enorme, contenuti estranei).
✅ **XP Tome** approvato il 17/10/2026 (→ 0301). Il resto non serve. Mob Grinding Utils solo se si vuole la pompa "mantieni livello" degli zaini.
