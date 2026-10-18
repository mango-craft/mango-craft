# Quanto integrare: tag, datapack o script? — valutazione del 16/10/2026

> **Documento storico**: fotografia del momento in cui è stato scritto, non si aggiorna. Lo stato attuale è nei documenti vivi (vedi il README della cartella).

| Livello | Cosa fa | Pro | Contro | Quando |
|---|---|---|---|---|
| **1. Tag con AlmostUnified** (`custom_tags`) | Rende intercambiabili gli ingredienti doppi in tutte le ricette che usano i tag; AlmostUnified può anche nascondere i doppioni in EMI | Globale per tutti i mondi, nessun file di mondo da toccare, regge bene gli aggiornamenti delle mod | Non crea ricette nuove; non aiuta le ricette che chiedono un oggetto preciso | **Subito** |
| **2. Ricette via datapack** (con Paxi) | Ricette nuove tra mod (es. erbe di Hexerei o Hexalia nel bollitore di HerbalBrews; conversione tra il tagliere di F&C e quello di FD, che Let's Do Addon Compat non fa) | Integrazione vera, mirata | Un file JSON per ricetta; i formati cambiano con gli aggiornamenti e le ricette possono rompersi senza avvisi | **Solo mirato**, dopo aver giocato, dove manca davvero qualcosa |
| **3. Script con KubeJS** | Togliere, sostituire e ribilanciare ricette e bottini in massa | Potentissimo | È un progetto a sé (una mod in più + codice JavaScript da mantenere) | **Non ora**; da tenere di riserva |

Integrazione a livello di ricette già presente senza fare nulla: Let's Do Addon Compat (pentole FD ↔ F&C, ciotola → Mixer di Create), Create: Central Kitchen e Slice & Dice (automazione di FD), Seasonal Let's Do, ricette di FD basate sui tag. Limite: Aspect Alchemy non è integrabile, perché i suoi ingredienti sono fissati nel codice.

**Proposta**: completare il livello 1 (oltre a farina e impasto: sale, mais, limoni; formaggi e latte con cautela, perché sono forme diverse), tenere il datapack per strutture e lune, e aggiungere ricette via datapack solo quando in gioco manca qualcosa.

---
