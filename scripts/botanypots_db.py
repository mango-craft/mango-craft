#!/usr/bin/env python3
"""Base dati dei vasi di Botany Pots (terreni, colture, tag e le nostre scelte di rarità), del mercato di Farming for
Blockheads e delle pozioni, in SQLite.

Uso:  python3 scripts/botanypots_db.py <cartella versione> refresh
      python3 scripts/botanypots_db.py <cartella versione> query "SELECT ..."
      python3 scripts/botanypots_db.py <cartella versione> analisi <nome>     (esegue mod-knowledge/botany-pots/query/<nome>.sql)
      python3 scripts/botanypots_db.py <cartella versione> tabelle | controlli

Da Python:  db = BotanyPotsDB("1.21.1"); db.query("SELECT ..."); db.analisi("nome"); db.refresh(); db.tabelle(); db.controlli()
`query` e `analisi` creano il database se non esiste o se inventario, datapack, CSV o questo script sono più
recenti (così non si lavora mai su dati vecchi). `refresh` lo ricostruisce da zero e lo sostituisce solo se
tutti i vincoli e i controlli passano. Modello, fatti verificati e query: 1.21.1/mod-knowledge/botany-pots/.

Fonti (si leggono direttamente, niente copie intermedie):
- <versione>/data/inventario/: ricette e tag di ogni jar (generato dai workflow), più minecraft.json e neoforge.json;
- <versione>/pack/config/paxi/datapacks/matteo_tweaks/data/: le nostre ricette e i nostri tag;
- <versione>/data/vasi/*.csv, mercato/*.csv, pozioni/*.csv e rarita.csv: le regole nostre, scritte a mano.
Il file <versione>/data/vasi/vasi.sqlite non va nel repository: si rigenera.

Tabelle (chiavi e vincoli nello SCHEMA qui sotto):
  anagrafiche   MOD (un file installato: slug del metafile), MOD_ID (gli id dichiarati dentro ogni file), MOD_NAMESPACE
                (il prefisso dei nomi di oggetti e blocchi → il file che li porta), TAG, TERRENO, COLTURA
  file del vaso POTS_TERRENO, POTS_COLTURA, POTS_COLTURA_SEME, POTS_COLTURA_TAG   (chiave: ricetta + fonte)
  viste         POTS_TERRENO_VINCENTE, POTS_COLTURA_VINCENTE (il file che il gioco usa per ogni id; `avviso` se due jar
                portano lo stesso id, caso in cui l'ordine non è noto e non blocca)
  esplosa       TERRENO_TAG   (per ogni terreno, tutti i tag in cui sta, con il tag che lo elenca davvero)
  scelte        RARITA_POTS_SETTINGS, TERRENO_RARITA, TERRENO_TAG_CUSTOM, TERRENO_CUSTOM, COLTURA_CUSTOM, COLTURA_TAG_CUSTOM,
                COLTURA_RACCOLTO_CUSTOM   (le regole nostre, lette anche da scripts/botanypots_genera.py)
                POTS_COMPATIBILITA   (terreno × coltura, dai file vincenti, con il tag che fa da ponte)
  mercato       MERCATO_* (0.6.2, scripts/mercato_genera.py)
  pozioni       EFFETTO, POZIONE (censimento dall'inventario), POZIONE_CUSTOM (regole), viste POZIONE_REGOLA e
                POZIONE_LISTA_NERA (0.7.2, scripts/pozioni_genera.py)

Regole lette nel sorgente di Botany Pots 21.1.44 e Bookshelf 21.1.81:
- il vaso cerca il file di terreno con l'oggetto nello slot del terreno e il file di coltura con l'oggetto nello
  slot del seme; la coltura cresce se il terreno sta in almeno uno dei tag del suo campo `soil` (vuoto = soil/dirt);
- i bonus (crescita, resa, luce) stanno nel file di terreno; il tempo e la resa base nel file di coltura;
- un tag di blocchi si confronta con l'oggetto di ogni blocco: qui l'oggetto ha sempre lo stesso nome del blocco
  (lo script si ferma se non è così);
- tra più file con lo stesso id vince il pacchetto più in alto: il nostro datapack (Paxi lo mette sopra a tutti).
"""
import csv
import glob
import json
import os
import sqlite3
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

DP = "pack/config/paxi/datapacks/matteo_tweaks/data"
NOSTRO = "matteo_tweaks"
TAG_DIRT = ("oggetti", "botanypots:soil/dirt")
TIPI_TERRENO = ("botanypots:soil", "botanypots:block_derived_soil")
TIPI_COLTURA = ("botanypots:crop", "botanypots:block_derived_crop")
TIPO_MERCATO = "farmingforblockheads:market"
# tag di oggetti da cui si ricava che cos'è un piantabile (alberello, fiore, seme…): si esplodono in OGGETTO_TAG
TAG_MERCATO = [("oggetti", t) for t in ("minecraft:saplings", "minecraft:flowers", "c:seeds", "c:crops", "farmersdelight:wild_crops")]
CATEGORIA_DI_TIPO = {"alberello": "farmingforblockheads:saplings", "fiore": "farmingforblockheads:flowers",
                     "selvatica": "farmingforblockheads:flowers", "seme": "farmingforblockheads:seeds",
                     "coltura": "farmingforblockheads:seeds", "colonia": "farmingforblockheads:other",
                     "fungo": "farmingforblockheads:other", "vegetazione": "farmingforblockheads:other",
                     "altro": "farmingforblockheads:other"}
# riconoscimento del tipo dal nome, quando i tag non bastano (suffissi, nell'ordine in cui si provano)
SUFFISSI_FUNGO = ("mushroom", "mushrooms", "fungus", "fungi", "shroom", "bioshroom", "sporeshroom", "toadstool", "spores")
SUFFISSI_VEGETAZIONE = ("shrub", "grass", "bush", "vines", "vine", "roots", "root", "litter", "fan", "coral", "pad", "lily",
                        "lichen", "leaf", "leaves", "fern", "dripleaf", "kelp", "seagrass", "algae", "deepturf", "turf",
                        "sprouts", "sprout", "tendrils", "moss", "cactus", "bamboo", "sculk", "patch", "siltmarram",
                        "swirls", "stem", "plant", "pile", "carpet", "weed", "reed", "reeds", "sedge", "cattails", "flower")
# Seme delle colture ricavate da un blocco il cui oggetto ha un altro nome (Botany Pots usa block.asItem()).
# Verificati: vanilla nel codice del gioco, palma nel sorgente di Bountiful Fares, Rustic Delight sugli oggetti del jar.
SEMI_ECCEZIONI = {
    "minecraft:beetroots": "minecraft:beetroot_seeds", "minecraft:carrots": "minecraft:carrot",
    "minecraft:cave_vines": "minecraft:glow_berries", "minecraft:cocoa": "minecraft:cocoa_beans",
    "minecraft:melon_stem": "minecraft:melon_seeds", "minecraft:potatoes": "minecraft:potato",
    "minecraft:pumpkin_stem": "minecraft:pumpkin_seeds", "minecraft:sweet_berry_bush": "minecraft:sweet_berries",
    "rusticdelight:bell_peppers": "rusticdelight:bell_pepper_seeds", "rusticdelight:cotton": "rusticdelight:cotton_seeds",
    "bountifulfares:palm_sapling": "bountifulfares:coconut",
    # il blocco ha un oggetto omonimo che però è il raccolto, non il seme (trovato il 24/10/2026)
    "minecraft:wheat": "minecraft:wheat_seeds",
}

SCHEMA = """
-- ================================================================ anagrafiche condivise
CREATE TABLE MOD (
  slug    TEXT PRIMARY KEY,             -- nome del metafile di packwiz (es. regions-unexplored); minecraft e neoforge a parte
  nome    TEXT NOT NULL,
  file    TEXT,                         -- il .jar
  origine TEXT,                         -- modrinth, curseforge, gioco
  lato    TEXT                          -- both, client, server
);
CREATE TABLE MOD_ID (
  modid    TEXT NOT NULL,               -- id dichiarato nel jar (neoforge.mods.toml); un jar può portarne più d'uno
  slug     TEXT NOT NULL REFERENCES MOD,
  nome     TEXT,
  versione TEXT,                        -- quella di neoforge.mods.toml (il vecchio mods.toml solo se manca)
  annidata INTEGER NOT NULL,            -- 1: dichiarato da un jar incorporato in quello della mod (jar-in-jar)
  PRIMARY KEY (modid, slug)
);
CREATE TABLE MOD_NAMESPACE (
  namespace TEXT PRIMARY KEY,           -- prefisso dei nomi (es. farm_and_charm); il file che porta più oggetti e blocchi
  slug      TEXT NOT NULL REFERENCES MOD,
  oggetti   INTEGER NOT NULL            -- quanti oggetti e blocchi con quel prefisso porta quel file
);
-- Le dimensioni conformi (24/10/2026): ogni id di blocco e di oggetto del pack, dall'inventario. Tutte le colonne
-- che nominano un oggetto o un blocco puntano qui, così «il nome esiste» è un vincolo e non un controllo.
CREATE TABLE BLOCCO (
  blocco_id TEXT PRIMARY KEY,
  namespace TEXT NOT NULL REFERENCES MOD_NAMESPACE,
  nome      TEXT                        -- nome inglese dalla lingua, se c'è
);
CREATE TABLE OGGETTO (
  oggetto_id TEXT PRIMARY KEY,
  namespace  TEXT NOT NULL REFERENCES MOD_NAMESPACE,
  nome       TEXT,
  blocco_id  TEXT REFERENCES BLOCCO    -- il blocco con lo stesso nome, se esiste (regola del pack: l'oggetto di un blocco si chiama come lui)
);
CREATE TABLE TAG (
  tag_id   INTEGER PRIMARY KEY,
  ambito   TEXT NOT NULL CHECK (ambito IN ('oggetti', 'blocchi')),
  nome     TEXT NOT NULL,
  UNIQUE (ambito, nome)
);
-- Anagrafica della rarità (24/10/2026): solo le etichette; i valori stanno nelle specializzazioni
-- RARITA_POTS_SETTINGS (vasi) e RARITA_MERCATO_SETTINGS (mercato). CSV: <versione>/data/rarita.csv.
CREATE TABLE RARITA (
  classe   TEXT PRIMARY KEY,
  famiglia TEXT NOT NULL CHECK (famiglia IN ('natura', 'craft')),  -- si trova nel mondo / si crafta
  ordine   INTEGER NOT NULL,            -- 0 = la più facile da ottenere, dentro la famiglia
  UNIQUE (famiglia, ordine)
);

-- ================================================================ vasi di Botany Pots
CREATE TABLE TERRENO (
  terreno_id TEXT PRIMARY KEY REFERENCES OGGETTO,  -- ruolo di OGGETTO: l'oggetto che va nello slot del terreno
  stato      TEXT NOT NULL CHECK (stato IN ('in_vaso', 'candidato'))  -- candidato: nei tag delle colture, senza file
);
CREATE TABLE COLTURA (
  coltura_id TEXT PRIMARY KEY,          -- la pianta: il blocco; per le colture senza blocco (graticci), il seme
  blocco_id  TEXT REFERENCES BLOCCO,    -- NULL per le colture senza blocco
  namespace  TEXT NOT NULL REFERENCES MOD_NAMESPACE,  -- la mod (resta qui perché non tutte le colture hanno un blocco)
  stato      TEXT NOT NULL CHECK (stato IN ('in_vaso'))
);
CREATE TABLE POTS_TERRENO (
  ricetta_id TEXT NOT NULL,             -- id del file nel gioco, es. botanypots:farmersdelight/soil/rich_soil
  fonte      TEXT NOT NULL,             -- jar (slug) o matteo_tweaks
  strato     TEXT NOT NULL CHECK (strato IN ('originale', 'nostro')),
  terreno_id TEXT NOT NULL REFERENCES TERRENO,
  crescita   REAL NOT NULL DEFAULT 0,
  resa       REAL NOT NULL DEFAULT 0,
  luce       INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (ricetta_id, fonte)
);
CREATE TABLE POTS_COLTURA (
  ricetta_id TEXT NOT NULL,
  fonte      TEXT NOT NULL,
  strato     TEXT NOT NULL CHECK (strato IN ('originale', 'nostro')),
  coltura_id TEXT NOT NULL REFERENCES COLTURA,
  tempo      INTEGER NOT NULL DEFAULT 1200,  -- tick
  resa_base  REAL NOT NULL DEFAULT 1,
  scala_resa REAL NOT NULL DEFAULT 1,
  PRIMARY KEY (ricetta_id, fonte)
);
CREATE TABLE POTS_COLTURA_SEME (
  ricetta_id TEXT NOT NULL,
  fonte      TEXT NOT NULL,
  seme       TEXT NOT NULL REFERENCES OGGETTO,  -- l'oggetto che va nello slot del seme
  origine    TEXT NOT NULL CHECK (origine IN ('file', 'blocco', 'eccezione')),  -- da dove viene il nome
  PRIMARY KEY (ricetta_id, fonte, seme),
  FOREIGN KEY (ricetta_id, fonte) REFERENCES POTS_COLTURA
);
CREATE TABLE POTS_COLTURA_TAG (
  ricetta_id TEXT NOT NULL,
  fonte      TEXT NOT NULL,
  tag_id     INTEGER NOT NULL REFERENCES TAG,
  implicito  INTEGER NOT NULL CHECK (implicito IN (0, 1)),  -- 1: il file non scrive `soil`, vale soil/dirt
  PRIMARY KEY (ricetta_id, fonte, tag_id),
  FOREIGN KEY (ricetta_id, fonte) REFERENCES POTS_COLTURA
);
CREATE TABLE TERRENO_TAG (
  terreno_id     TEXT NOT NULL REFERENCES TERRENO,
  tag_id         INTEGER NOT NULL REFERENCES TAG,   -- il tag raggiunto
  tag_diretto_id INTEGER NOT NULL REFERENCES TAG,   -- il tag il cui file elenca il terreno (l'origine)
  livello        INTEGER NOT NULL,                  -- 0 = elencato direttamente
  da_noi         INTEGER NOT NULL CHECK (da_noi IN (0, 1)),  -- 1: esiste solo grazie al nostro datapack
  PRIMARY KEY (terreno_id, tag_id, tag_diretto_id)
);
CREATE TABLE RARITA_POTS_SETTINGS (
  classe   TEXT PRIMARY KEY REFERENCES RARITA,
  crescita REAL NOT NULL,
  resa     REAL NOT NULL
);
CREATE TABLE TERRENO_RARITA (
  terreno_id TEXT PRIMARY KEY REFERENCES TERRENO,
  classe     TEXT NOT NULL REFERENCES RARITA,
  motivo     TEXT NOT NULL              -- come si ottiene
);
-- Le altre regole nostre (CSV a mano, lette da scripts/botanypots_genera.py): qui per le analisi.
CREATE TABLE TERRENO_TAG_CUSTOM (
  terreno_id TEXT NOT NULL REFERENCES TERRENO,
  ambito     TEXT NOT NULL CHECK (ambito IN ('oggetti', 'blocchi')),
  tag        TEXT NOT NULL,
  PRIMARY KEY (terreno_id, ambito, tag)
);
CREATE TABLE TERRENO_CUSTOM (
  terreno_id     TEXT PRIMARY KEY REFERENCES OGGETTO,  -- un terreno che non è un blocco (un secchio)
  display_blocco TEXT NOT NULL REFERENCES BLOCCO,      -- il blocco mostrato nel vaso
  fluido         TEXT,                  -- non vuoto: mostrato come liquido
  nota           TEXT
);
CREATE TABLE COLTURA_CUSTOM (
  coltura_id     TEXT PRIMARY KEY,      -- il blocco della pianta, o l'id del file per le colture senza blocco
  mod            TEXT NOT NULL REFERENCES MOD,  -- lo slug
  seme           TEXT REFERENCES OGGETTO,
  tempo          INTEGER,
  richiesti      TEXT,                  -- blocchi richiesti dalla condizione di caricamento, separati da |
  display_blocco TEXT,
  display_offset TEXT,
  rotazione      TEXT,
  da_provare     TEXT,
  nota           TEXT
);
CREATE TABLE COLTURA_TAG_CUSTOM (
  coltura_id TEXT NOT NULL REFERENCES COLTURA_CUSTOM,
  ordine     INTEGER NOT NULL,
  ambito     TEXT NOT NULL CHECK (ambito IN ('oggetti', 'blocchi')),
  tag        TEXT NOT NULL,
  PRIMARY KEY (coltura_id, ordine)
);
CREATE TABLE COLTURA_RACCOLTO_CUSTOM (
  coltura_id TEXT NOT NULL REFERENCES COLTURA_CUSTOM,
  gruppo     INTEGER NOT NULL,
  tipo       TEXT NOT NULL CHECK (tipo IN ('oggetto', 'tabella')),
  id         TEXT NOT NULL,
  count      INTEGER,
  chance     REAL,
  PRIMARY KEY (coltura_id, gruppo, id)
);
-- File vincenti: tra file con lo stesso id vince il nostro datapack (Paxi lo carica sopra a tutti). Se due jar
-- portano lo stesso id l'ordine non è noto: `avviso` = 1 e si tiene il primo per nome di fonte.
CREATE VIEW POTS_TERRENO_VINCENTE AS
  SELECT p.*, (SELECT count(*) FROM POTS_TERRENO q WHERE q.ricetta_id = p.ricetta_id AND q.strato = 'originale') > 1 AS avviso
  FROM POTS_TERRENO p
  WHERE p.fonte = (SELECT fonte FROM POTS_TERRENO q WHERE q.ricetta_id = p.ricetta_id
                   ORDER BY q.strato = 'nostro' DESC, q.fonte LIMIT 1);
CREATE VIEW POTS_COLTURA_VINCENTE AS
  SELECT p.*, (SELECT count(*) FROM POTS_COLTURA q WHERE q.ricetta_id = p.ricetta_id AND q.strato = 'originale') > 1 AS avviso
  FROM POTS_COLTURA p
  WHERE p.fonte = (SELECT fonte FROM POTS_COLTURA q WHERE q.ricetta_id = p.ricetta_id
                   ORDER BY q.strato = 'nostro' DESC, q.fonte LIMIT 1);
CREATE VIEW POTS_COMPATIBILITA AS
  SELECT tt.terreno_id, pc.coltura_id, pct.tag_id, MIN(tt.da_noi) AS da_noi
  FROM TERRENO_TAG tt
  JOIN POTS_COLTURA_TAG pct ON pct.tag_id = tt.tag_id
  JOIN POTS_COLTURA_VINCENTE pc ON pc.ricetta_id = pct.ricetta_id AND pc.fonte = pct.fonte
  GROUP BY tt.terreno_id, pc.coltura_id, pct.tag_id;

-- ================================================================ mercato di Farming for Blockheads (24/10/2026)
-- Fatti letti dal sorgente 21.1.14 (MarketPresetRegistry.isRecipeEnabled, MarketMenu): una voce è attiva se il suo
-- oggetto esiste e il suo preset esiste ed è acceso (enabled nel file, salvo le due liste della config); il pagamento
-- è uno stack in uno slot, quindi non può superare 64; una voce può portare un pagamento proprio, ma il preset
-- deve comunque esistere ed essere acceso.
CREATE TABLE MERCATO_CATEGORIA (
  categoria_id TEXT PRIMARY KEY,        -- le schede del mercato: farmingforblockheads:seeds, saplings, flowers, other
  fonte        TEXT NOT NULL
);
CREATE TABLE MERCATO_PRESET (
  preset_id      TEXT NOT NULL,         -- es. farmersdelight:seeds (data/<ns>/market_presets/<nome>.json)
  fonte          TEXT NOT NULL,         -- jar (slug) o matteo_tweaks
  strato         TEXT NOT NULL CHECK (strato IN ('originale', 'nostro')),
  pagamento_id   TEXT REFERENCES OGGETTO,  -- l'oggetto chiesto (NULL se il file chiede un tag)
  pagamento_tag  TEXT,
  quantita       INTEGER NOT NULL,
  acceso_default INTEGER NOT NULL CHECK (acceso_default IN (0, 1)),  -- `enabled` del file (1 se manca)
  PRIMARY KEY (preset_id, fonte)
);
CREATE TABLE MERCATO_PRESET_CONFIG (
  preset_id TEXT PRIMARY KEY,           -- le due liste della config di FFB nel pack (enabledOptionalPresets, disabledDefaultPresets)
  acceso    INTEGER NOT NULL CHECK (acceso IN (0, 1))
);
CREATE TABLE MERCATO_VOCE (
  ricetta_id         TEXT NOT NULL,     -- es. farmingforblockheads:market/farmersdelight/tomato_seeds
  fonte              TEXT NOT NULL,
  strato             TEXT NOT NULL CHECK (strato IN ('originale', 'nostro')),
  oggetto_id         TEXT NOT NULL REFERENCES OGGETTO,   -- cosa si compra
  quantita           INTEGER NOT NULL DEFAULT 1,
  categoria_id       TEXT NOT NULL REFERENCES MERCATO_CATEGORIA,
  preset_id          TEXT NOT NULL,     -- il listino (non è chiave esterna perché il preset può venire da un'altra fonte: controllo a parte)
  pagamento_id       TEXT REFERENCES OGGETTO,  -- pagamento scritto nella voce (raro); se NULL vale quello del preset
  pagamento_quantita INTEGER,
  PRIMARY KEY (ricetta_id, fonte)
);
CREATE VIEW MERCATO_PRESET_VINCENTE AS
  SELECT p.*, COALESCE(k.acceso, p.acceso_default) AS acceso,
         (SELECT count(*) FROM MERCATO_PRESET q WHERE q.preset_id = p.preset_id AND q.strato = 'originale') > 1 AS avviso
  FROM MERCATO_PRESET p
  LEFT JOIN MERCATO_PRESET_CONFIG k ON k.preset_id = p.preset_id
  WHERE p.fonte = (SELECT fonte FROM MERCATO_PRESET q WHERE q.preset_id = p.preset_id
                   ORDER BY q.strato = 'nostro' DESC, q.fonte LIMIT 1);
CREATE VIEW MERCATO_VOCE_VINCENTE AS
  SELECT v.*, (SELECT count(*) FROM MERCATO_VOCE q WHERE q.ricetta_id = v.ricetta_id AND q.strato = 'originale') > 1 AS avviso
  FROM MERCATO_VOCE v
  WHERE v.fonte = (SELECT fonte FROM MERCATO_VOCE q WHERE q.ricetta_id = v.ricetta_id
                   ORDER BY q.strato = 'nostro' DESC, q.fonte LIMIT 1);
-- Il mercato come lo vede il gioco: voce vincente con preset esistente e acceso; il pagamento effettivo.
CREATE VIEW MERCATO_VOCE_ATTIVA AS
  SELECT v.ricetta_id, v.fonte, v.strato, v.oggetto_id, v.quantita, v.categoria_id, v.preset_id,
         COALESCE(v.pagamento_id, p.pagamento_id) AS pagamento_id,
         COALESCE(v.pagamento_quantita, p.quantita) AS pagamento_quantita
  FROM MERCATO_VOCE_VINCENTE v
  JOIN MERCATO_PRESET_VINCENTE p ON p.preset_id = v.preset_id AND p.acceso = 1;
-- Tutto ciò che si può piantare nel pack: i semi delle colture vincenti dei vasi, più alberelli e fiori dai tag.
CREATE TABLE PIANTABILE (
  oggetto_id         TEXT PRIMARY KEY REFERENCES OGGETTO,
  origine            TEXT NOT NULL CHECK (origine IN ('pots_seme', 'tag_saplings', 'tag_flowers')),  -- da dove è entrato (la prima che lo trova)
  coltura_id         TEXT REFERENCES COLTURA,  -- la coltura dei vasi che pianta, se c'è
  tipo               TEXT NOT NULL CHECK (tipo IN ('seme', 'coltura', 'alberello', 'fiore', 'selvatica', 'colonia', 'fungo', 'vegetazione', 'altro')),
                                        -- coltura: pianta commestibile che si pianta con il suo prodotto (cipolla, cocco);
                                        -- vegetazione: piante decorative (erba, cespugli, liane); altro: solo dai tag
  categoria_proposta TEXT NOT NULL REFERENCES MERCATO_CATEGORIA  -- dal tipo, con le regole che FFB usa per Farmer's Delight
);
CREATE TABLE OGGETTO_TAG (                        -- esplosa come TERRENO_TAG, ma per i tag del mercato (alberelli, fiori, semi)
  oggetto_id     TEXT NOT NULL REFERENCES OGGETTO,
  tag_id         INTEGER NOT NULL REFERENCES TAG,
  tag_diretto_id INTEGER NOT NULL REFERENCES TAG,
  livello        INTEGER NOT NULL,
  da_noi         INTEGER NOT NULL CHECK (da_noi IN (0, 1)),
  PRIMARY KEY (oggetto_id, tag_id, tag_diretto_id)
);
-- Regole nostre (CSV a mano in <versione>/data/mercato/, lette anche da scripts/mercato_genera.py)
CREATE TABLE RARITA_MERCATO_SETTINGS (
  classe         TEXT PRIMARY KEY REFERENCES RARITA,
  moltiplicatore REAL NOT NULL
);
CREATE TABLE MERCATO_BASE (                       -- la moneta e la quantità base per origine e intervallo di rarità
  origine    TEXT NOT NULL,             -- overworld, nether, end, aether, undergarden, twilight
  ordine_min INTEGER NOT NULL,
  ordine_max INTEGER NOT NULL,
  pagamento_id TEXT NOT NULL REFERENCES OGGETTO,
  quantita   INTEGER NOT NULL,
  blocco_id  TEXT REFERENCES OGGETTO,   -- l'oggetto «blocco di» per la conversione sopra i 64 (NULL: non si può superare 64)
  motivo     TEXT,
  PRIMARY KEY (origine, ordine_min),
  CHECK (ordine_min <= ordine_max)
);
CREATE TABLE MERCATO_MOD_CUSTOM (                 -- origine e classe predefinite di tutte le piante di una mod
  slug    TEXT PRIMARY KEY REFERENCES MOD,
  origine TEXT NOT NULL,
  classe  TEXT NOT NULL REFERENCES RARITA,
  motivo  TEXT
);
CREATE TABLE MERCATO_TIPO_CUSTOM (                -- regola per tipo di piantabile: categoria e se si vende
  tipo         TEXT PRIMARY KEY,
  categoria_id TEXT REFERENCES MERCATO_CATEGORIA,
  vendi        INTEGER NOT NULL DEFAULT 1 CHECK (vendi IN (0, 1)),
  motivo       TEXT
);
CREATE TABLE MERCATO_VOCE_CUSTOM (                -- eccezioni per oggetto: categoria, origine o classe diverse, o escluso
  oggetto_id   TEXT PRIMARY KEY REFERENCES OGGETTO,
  categoria_id TEXT REFERENCES MERCATO_CATEGORIA,
  origine      TEXT,
  classe       TEXT REFERENCES RARITA,
  escluso      TEXT,                    -- non vuoto: non si vende
  motivo       TEXT
);
CREATE TABLE MERCATO_PRESET_CUSTOM (              -- i preset delle mod riscritti con il nostro prezzo (stesso percorso) o spenti
  preset_id TEXT PRIMARY KEY,
  origine   TEXT,
  classe    TEXT REFERENCES RARITA,
  acceso    INTEGER NOT NULL DEFAULT 1 CHECK (acceso IN (0, 1)),
  motivo    TEXT
);
-- Il prezzo di ogni (origine, classe): base × moltiplicatore per eccesso; sopra 64, blocchi per eccesso.
CREATE VIEW MERCATO_PREZZO AS
  WITH q AS (
    SELECT b.origine, r.classe, r.ordine, b.pagamento_id, b.blocco_id,
           CAST(b.quantita * s.moltiplicatore AS INTEGER)
             + (b.quantita * s.moltiplicatore > CAST(b.quantita * s.moltiplicatore AS INTEGER)) AS n
    FROM MERCATO_BASE b
    JOIN RARITA r ON r.ordine BETWEEN b.ordine_min AND b.ordine_max
    JOIN RARITA_MERCATO_SETTINGS s ON s.classe = r.classe)
  SELECT origine, classe, ordine,
         CASE WHEN n > 64 AND blocco_id IS NOT NULL THEN blocco_id ELSE pagamento_id END AS pagamento_id,
         CASE WHEN n > 64 AND blocco_id IS NOT NULL THEN (n + 8) / 9 ELSE n END AS quantita,
         n AS quantita_unitaria, n > 64 AND blocco_id IS NULL AS oltre_limite
  FROM q;
-- I candidati: piantabili senza una voce attiva, con la regola che li governa (oggetto > mod) e il prezzo.
CREATE VIEW MERCATO_CANDIDATO AS
  SELECT p.oggetto_id, o.nome, o.namespace, n.slug, p.tipo,
         COALESCE(vc.categoria_id, tc.categoria_id, p.categoria_proposta) AS categoria_id,
         COALESCE(vc.origine, mc.origine) AS origine,
         COALESCE(vc.classe, mc.classe) AS classe,
         COALESCE(vc.escluso, CASE WHEN tc.vendi = 0 THEN 'tipo ' || p.tipo END) AS escluso,
         COALESCE(vc.motivo, mc.motivo) AS motivo,
         z.pagamento_id, z.quantita
  FROM PIANTABILE p
  JOIN OGGETTO o ON o.oggetto_id = p.oggetto_id
  JOIN MOD_NAMESPACE n ON n.namespace = o.namespace
  LEFT JOIN MERCATO_VOCE_CUSTOM vc ON vc.oggetto_id = p.oggetto_id
  LEFT JOIN MERCATO_TIPO_CUSTOM tc ON tc.tipo = p.tipo
  LEFT JOIN MERCATO_MOD_CUSTOM mc ON mc.slug = n.slug
  LEFT JOIN MERCATO_PREZZO z ON z.origine = COALESCE(vc.origine, mc.origine) AND z.classe = COALESCE(vc.classe, mc.classe)
  WHERE NOT EXISTS (SELECT 1 FROM MERCATO_VOCE_ATTIVA a WHERE a.oggetto_id = p.oggetto_id AND a.strato = 'originale');
-- Ciò che il generatore scrive: le voci nostre (candidati con regola e non esclusi) e i preset (nostri e sostituiti).
CREATE VIEW MERCATO_PIANO_VOCE AS
  SELECT oggetto_id, namespace, slug, categoria_id, origine, classe, 'matteo_tweaks:' || origine || '_' || classe AS preset_id, pagamento_id, quantita
  FROM MERCATO_CANDIDATO
  WHERE escluso IS NULL AND origine IS NOT NULL AND classe IS NOT NULL;
-- I preset da scrivere: i nostri (uno per origine e classe usate) e quelli delle mod riscritti allo stesso percorso
-- (prezzo nostro se la regola dà origine e classe, altrimenti quello della mod; `acceso` dalla regola).
CREATE VIEW MERCATO_PIANO_PRESET AS
  SELECT DISTINCT preset_id, pagamento_id, quantita, 1 AS acceso, 'nostro' AS tipo FROM MERCATO_PIANO_VOCE
  UNION ALL
  SELECT c.preset_id, COALESCE(z.pagamento_id, p.pagamento_id), COALESCE(z.quantita, p.quantita), c.acceso, 'sostituito'
  FROM MERCATO_PRESET_CUSTOM c
  LEFT JOIN MERCATO_PREZZO z ON z.origine = c.origine AND z.classe = c.classe
  LEFT JOIN MERCATO_PRESET p ON p.preset_id = c.preset_id AND p.strato = 'originale';

-- ================================================================ pozioni ed effetti (0.7.2)
-- Due fonti: l'inventario (nomi, traduzioni, descrizioni: dai file dei jar, lo rifà il workflow) e il dump del gioco
-- (<versione>/data/dump/, scritto da /mango_dump di KubeJS e importato con scripts/dump_importa.py: categoria degli
-- effetti, effetti delle pozioni, alambicco, cibi). Senza dump le colonne del gioco restano vuote (NULL).
-- Tema 1.21.1/theme-knowledge/pozioni.md.
CREATE TABLE DUMP_MOD (                  -- le mod caricate nel gioco quando è stato fatto il dump
  modid    TEXT PRIMARY KEY,
  versione TEXT NOT NULL
);
CREATE TABLE DUMP_INFO (                 -- data del dump, formato, impronta del datapack a cui si riferisce (dall'importatore)
  chiave TEXT PRIMARY KEY,
  valore TEXT
);
CREATE TABLE EFFETTO (
  effetto_id  TEXT PRIMARY KEY,          -- es. apothic_attributes:flying
  slug        TEXT NOT NULL REFERENCES MOD,
  nome        TEXT,                      -- nome inglese (il gioco base non ce l'ha nell'inventario)
  descrizione TEXT,                      -- descrizione inglese, se la mod la dà
  categoria   TEXT CHECK (categoria IN ('beneficial', 'harmful', 'neutral')),  -- dal gioco (MobEffectCategory)
  istantaneo  INTEGER CHECK (istantaneo IN (0, 1)),                            -- dal gioco (cura, danno istantanei…)
  colore      INTEGER,                   -- dal gioco (colore delle particelle, RGB)
  inventario  INTEGER NOT NULL CHECK (inventario IN (0, 1)),  -- 1 = trovato nei file dei jar
  gioco       INTEGER CHECK (gioco IN (0, 1))                 -- 1 = nel dump; NULL = nessun dump
);
CREATE TABLE POZIONE (
  pozione_id TEXT PRIMARY KEY,           -- es. apothic_attributes:long_flying
  slug       TEXT NOT NULL REFERENCES MOD,
  nome       TEXT,                       -- nome inglese (il gioco base non ce l'ha nell'inventario)
  famiglia   TEXT NOT NULL,              -- il nome senza «long», «strong», «extra»: le varianti della stessa pozione
  dedotta    INTEGER NOT NULL CHECK (dedotta IN (0, 1)),  -- 1 = nome del registro dedotto dalla traduzione nell'inventario
  traduzione TEXT,                       -- dal gioco: il nome usato per la traduzione (Potion.getName)
  inventario INTEGER NOT NULL CHECK (inventario IN (0, 1)),
  gioco      INTEGER CHECK (gioco IN (0, 1))
);
CREATE TABLE POZIONE_EFFETTO (           -- dal gioco: gli effetti di ogni pozione
  pozione_id TEXT NOT NULL REFERENCES POZIONE,
  ordine     INTEGER NOT NULL,
  effetto_id TEXT NOT NULL REFERENCES EFFETTO,
  durata     INTEGER NOT NULL,           -- tick (20 = 1 secondo; 1 per gli istantanei)
  livello    INTEGER NOT NULL,           -- 0 = I, 1 = II…
  PRIMARY KEY (pozione_id, ordine)
);
CREATE TABLE OGGETTO_CIBO (              -- dal gioco: gli oggetti che si mangiano o si bevono (componente food)
  oggetto_id  TEXT PRIMARY KEY REFERENCES OGGETTO,
  nutrizione  INTEGER NOT NULL,
  saturazione REAL NOT NULL,
  sempre      INTEGER NOT NULL CHECK (sempre IN (0, 1)),  -- si mangia anche senza fame
  secondi     REAL NOT NULL
);
CREATE TABLE OGGETTO_EFFETTO (           -- dal gioco: effetti dei cibi e degli oggetti con una pozione dentro
  oggetto_id  TEXT NOT NULL REFERENCES OGGETTO,
  origine     TEXT NOT NULL CHECK (origine IN ('cibo', 'pozione')),
  ordine      INTEGER NOT NULL,
  effetto_id  TEXT NOT NULL REFERENCES EFFETTO,
  durata      INTEGER NOT NULL,
  livello     INTEGER NOT NULL,
  probabilita REAL NOT NULL,             -- 1 = sempre
  PRIMARY KEY (oggetto_id, origine, ordine)
);
CREATE TABLE ALAMBICCO (                 -- dal gioco: le ricette dell'alambicco
  riga              INTEGER PRIMARY KEY,
  fonte             TEXT NOT NULL CHECK (fonte IN ('miscela', 'ricetta')),  -- provata davvero / elencata da NeoForge
  ingresso_id       TEXT NOT NULL REFERENCES OGGETTO,  -- nello slot della bottiglia
  ingresso_pozione  TEXT REFERENCES POZIONE,
  ingrediente_id    TEXT NOT NULL REFERENCES OGGETTO,  -- nello slot in alto
  risultato_id      TEXT NOT NULL REFERENCES OGGETTO,
  risultato_pozione TEXT REFERENCES POZIONE
);
CREATE TABLE ALAMBICCO_CLASSE (          -- dal gioco: le ricette NeoForge per classe
  classe     TEXT PRIMARY KEY,
  ricette    INTEGER NOT NULL,
  elencabili INTEGER NOT NULL            -- quelle con le combinazioni note: elencate (BrewingRecipe) o trovate provando
);
-- Le scelte nostre (CSV <versione>/data/pozioni/pozione_custom.csv): `varianti` = 'tutte' vale per tutta la famiglia
-- della pozione indicata, 'questa' solo per lei (e vince sulla famiglia). amuleto = 0: lista nera degli amuleti di Apotheosis.
CREATE TABLE POZIONE_CUSTOM (
  pozione_id TEXT PRIMARY KEY REFERENCES POZIONE,
  varianti   TEXT NOT NULL CHECK (varianti IN ('tutte', 'questa')),
  amuleto    INTEGER NOT NULL CHECK (amuleto IN (0, 1)),
  motivo     TEXT NOT NULL
);
-- Per ogni pozione la regola che vale (pozione > famiglia; senza regola l'amuleto si può fare).
CREATE VIEW POZIONE_REGOLA AS
  SELECT p.pozione_id, p.slug, p.nome, p.famiglia, p.dedotta,
         COALESCE(q.amuleto, f.amuleto, 1) AS amuleto,
         COALESCE(q.motivo, f.motivo) AS motivo,
         COALESCE(q.pozione_id, f.pozione_id) AS regola
  FROM POZIONE p
  LEFT JOIN POZIONE_CUSTOM q ON q.pozione_id = p.pozione_id AND q.varianti = 'questa'
  LEFT JOIN (SELECT c.pozione_id, c.amuleto, c.motivo, x.famiglia
             FROM POZIONE_CUSTOM c JOIN POZIONE x ON x.pozione_id = c.pozione_id
             WHERE c.varianti = 'tutte') f ON f.famiglia = p.famiglia;
-- Ciò che scripts/pozioni_genera.py scrive nell'etichetta apotheosis:potion_charm_blacklist.
CREATE VIEW POZIONE_LISTA_NERA AS
  SELECT r.pozione_id, r.slug, r.nome, r.famiglia, r.dedotta, p.gioco, r.motivo
  FROM POZIONE_REGOLA r JOIN POZIONE p ON p.pozione_id = r.pozione_id WHERE r.amuleto = 0;
-- Per ogni pozione: gli effetti, e se fa un amuleto di Apotheosis (PotionCharmItem.isValidPotion: un solo effetto,
-- non istantaneo, fuori dalla lista nera). NULL = la pozione non è nel dump (o non c'è dump): non si sa.
CREATE VIEW POZIONE_AMULETO AS
  SELECT p.pozione_id, p.slug, p.nome, r.amuleto AS regola,
         count(pe.effetto_id) AS effetti,
         group_concat(pe.effetto_id || ' ' || (pe.livello + 1) || ' ' || (pe.durata / 20) || 's', ', ') AS dettaglio,
         CASE WHEN p.gioco IS NOT 1 THEN NULL
              WHEN count(pe.effetto_id) = 1 AND max(e.istantaneo) = 0 THEN 1 ELSE 0 END AS valida,
         CASE WHEN p.gioco IS NOT 1 THEN NULL
              WHEN count(pe.effetto_id) = 1 AND max(e.istantaneo) = 0 AND r.amuleto = 1 THEN 1 ELSE 0 END AS amuleto_possibile
  FROM POZIONE p
  JOIN POZIONE_REGOLA r ON r.pozione_id = p.pozione_id
  LEFT JOIN POZIONE_EFFETTO pe ON pe.pozione_id = p.pozione_id
  LEFT JOIN EFFETTO e ON e.effetto_id = pe.effetto_id
  GROUP BY p.pozione_id;
-- Le mod dell'inventario che nel dump mancano o hanno un'altra versione: se ce ne sono, il dump è vecchio.
-- Solo le mod dei jar del pack: delle librerie incorporate in più jar NeoForge carica una copia sola, e il confronto
-- non direbbe niente. (Le versioni scritte come ${file.jarVersion} nell'inventario non si confrontano.)
CREATE VIEW DUMP_MOD_DIVERSA AS
  SELECT m.modid, m.versione AS inventario, d.versione AS gioco
  FROM (SELECT modid, max(versione) AS versione FROM MOD_ID WHERE annidata = 0 GROUP BY modid) m
  LEFT JOIN DUMP_MOD d ON d.modid = m.modid
  WHERE EXISTS (SELECT 1 FROM DUMP_MOD)
    AND (d.versione IS NULL OR (d.versione <> m.versione AND m.versione NOT LIKE '%$%'));

-- ---- Dal gioco, formato 2 del dump (26/10/2026): per controllare con il gioco il lavoro di tutte le versioni ----
CREATE TABLE GIOCO_ID (                  -- i nomi registrati nel gioco (anche quelli creati all'avvio: Every Compat)
  registro TEXT NOT NULL,                -- item, block, fluid, entity_type, mob_effect, potion
  id       TEXT NOT NULL,
  PRIMARY KEY (registro, id)
);
CREATE TABLE GIOCO_RICETTA (             -- le ricette caricate davvero
  ricetta_id TEXT PRIMARY KEY,
  tipo       TEXT NOT NULL
);
CREATE TABLE GIOCO_TAG (                 -- le etichette finali, dopo tutti i datapack
  registro TEXT NOT NULL,
  tag      TEXT NOT NULL,
  voci     INTEGER NOT NULL,             -- quante voci ha l'etichetta nel gioco
  valori   INTEGER NOT NULL,             -- 1: le voci sono in GIOCO_TAG_VOCE (solo per i namespace scelti dallo script)
  PRIMARY KEY (registro, tag)
);
CREATE TABLE GIOCO_TAG_VOCE (
  registro TEXT NOT NULL,
  tag      TEXT NOT NULL,
  id       TEXT NOT NULL,
  PRIMARY KEY (registro, tag, id),
  FOREIGN KEY (registro, tag) REFERENCES GIOCO_TAG
);
CREATE TABLE GIOCO_TABELLA (             -- le tabelle del bottino caricate (solo i nomi)
  tabella_id TEXT PRIMARY KEY
);
CREATE TABLE GIOCO_STRUTTURA_SET (       -- gli insiemi di strutture come il gioco li vede (dopo Sparse Structures)
  set_id      TEXT PRIMARY KEY,
  tipo        TEXT,
  spaziatura  INTEGER,
  separazione INTEGER,
  sale        INTEGER,
  frequenza   REAL
);
CREATE TABLE GIOCO_STRUTTURA_SET_VOCE (
  set_id    TEXT NOT NULL REFERENCES GIOCO_STRUTTURA_SET,
  struttura TEXT NOT NULL,
  peso      INTEGER NOT NULL,
  PRIMARY KEY (set_id, struttura)
);
-- I nostri file del datapack, per confrontarli con il gioco: ricette, tag, tabelle e modificatori del bottino.
CREATE TABLE NOSTRA_RICETTA (
  ricetta_id TEXT PRIMARY KEY,
  tipo       TEXT NOT NULL,
  percorso   TEXT NOT NULL,
  caricabile INTEGER NOT NULL            -- 1 se le condizioni di caricamento sono vere con l'inventario
);
CREATE TABLE NOSTRO_TAG_VOCE (
  registro    TEXT NOT NULL,             -- item, block, fluid, potion…
  tag         TEXT NOT NULL,
  id          TEXT NOT NULL,             -- un nome (non #altro_tag)
  facoltativo INTEGER NOT NULL,          -- required: false
  PRIMARY KEY (registro, tag, id)
);
CREATE TABLE NOSTRA_TABELLA (            -- le tabelle del bottino nostre
  tabella_id TEXT PRIMARY KEY,
  percorso   TEXT NOT NULL,
  caricabile INTEGER NOT NULL
);
CREATE TABLE NOSTRO_MODIFICATORE (       -- i modificatori del bottino: ognuno con le tabelle che tocca e quella che aggiunge
  modificatore_id TEXT NOT NULL,
  elencato        INTEGER NOT NULL,      -- 1 se sta nel nostro global_loot_modifiers.json (i file con il nome di una mod
                                         --   sostituiscono i suoi e sono elencati dalla mod)
  caricabile      INTEGER NOT NULL,
  tabella_id      TEXT,                  -- la tabella a cui si applica (NULL: nessuna condizione di tabella)
  aggiunge        TEXT,                  -- la tabella aggiunta (neoforge:add_table)
  PRIMARY KEY (modificatore_id, tabella_id)
);
-- Le nostre ricette caricabili che il gioco non ha, e quelle non caricabili che invece ha (condizione sbagliata)
CREATE VIEW NOSTRA_RICETTA_DIVERSA AS
  SELECT n.ricetta_id, n.tipo, n.percorso, n.caricabile, g.ricetta_id IS NOT NULL AS nel_gioco
  FROM NOSTRA_RICETTA n LEFT JOIN GIOCO_RICETTA g ON g.ricetta_id = n.ricetta_id
  WHERE EXISTS (SELECT 1 FROM GIOCO_RICETTA) AND n.caricabile <> (g.ricetta_id IS NOT NULL);
-- Le voci dei nostri tag che nel gioco mancano: le obbligatorie sempre, le facoltative solo se il nome esiste nel gioco
CREATE VIEW NOSTRO_TAG_MANCANTE AS
  SELECT n.registro, n.tag, n.id, n.facoltativo,
         (SELECT valori FROM GIOCO_TAG g WHERE g.registro = n.registro AND g.tag = n.tag) AS tag_nel_gioco
  FROM NOSTRO_TAG_VOCE n
  WHERE EXISTS (SELECT 1 FROM GIOCO_TAG g WHERE g.registro = n.registro)   -- solo i registri che il dump riporta
    AND NOT EXISTS (SELECT 1 FROM GIOCO_TAG_VOCE v WHERE v.registro = n.registro AND v.tag = n.tag AND v.id = n.id)
    AND (NOT n.facoltativo OR EXISTS (SELECT 1 FROM GIOCO_ID i WHERE i.registro = n.registro AND i.id = n.id));
-- Le tabelle del bottino nominate dai nostri modificatori (toccate o aggiunte) e le nostre che il gioco non ha
CREATE VIEW NOSTRA_TABELLA_MANCANTE AS
  SELECT DISTINCT t.tabella_id, t.fonte FROM (
    SELECT tabella_id, 'modificatore ' || modificatore_id AS fonte FROM NOSTRO_MODIFICATORE WHERE caricabile AND tabella_id IS NOT NULL
    UNION ALL SELECT aggiunge, 'aggiunta da ' || modificatore_id FROM NOSTRO_MODIFICATORE WHERE caricabile AND aggiunge IS NOT NULL
    UNION ALL SELECT tabella_id, 'nostra: ' || percorso FROM NOSTRA_TABELLA WHERE caricabile) t
  WHERE EXISTS (SELECT 1 FROM GIOCO_TABELLA)
    AND NOT EXISTS (SELECT 1 FROM GIOCO_TABELLA g WHERE g.tabella_id = t.tabella_id);
-- I nomi registrati nel gioco che l'inventario non conosce (creati all'avvio) e viceversa
CREATE VIEW GIOCO_ID_DIVERSO AS
  SELECT 'item' AS registro, g.id, 'solo nel gioco' AS dove FROM GIOCO_ID g WHERE g.registro = 'item' AND NOT EXISTS (SELECT 1 FROM OGGETTO o WHERE o.oggetto_id = g.id)
  UNION ALL
  SELECT 'item', o.oggetto_id, 'solo nell''inventario' FROM OGGETTO o WHERE EXISTS (SELECT 1 FROM GIOCO_ID) AND NOT EXISTS (SELECT 1 FROM GIOCO_ID g WHERE g.registro = 'item' AND g.id = o.oggetto_id);
"""


class ErroreDati(Exception):
    pass


VARIANTI_POZIONE = {"long", "strong", "extra"}


def famiglia_pozione(pid: str) -> str:
    """La pozione senza le parole delle varianti: minecraft:long_swiftness, ars_nouveau:mana_regen_potion_long,
    netherdepthsupgrade:glowdine_long_glowing, bountifulfares:bountifulfares.long_acidic → la stessa senza long/strong."""
    ns, path = pid.split(":", 1)
    return ns + ":" + ".".join("_".join(w for w in s.split("_") if w not in VARIANTI_POZIONE) for s in path.split("."))


def _carica_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8-sig"))


class BotanyPotsDB:
    def __init__(self, versione: str | Path):
        self.ver = Path(versione)
        if not self.ver.is_absolute():
            self.ver = Path(__file__).resolve().parent.parent / self.ver
        self.inventario = self.ver / "data" / "inventario"
        self.datapack = self.ver / DP
        self.vasi = self.ver / "data" / "vasi"
        self.mercato = self.ver / "data" / "mercato"
        self.pozioni = self.ver / "data" / "pozioni"
        self.dump = self.ver / "data" / "dump"
        self.rarita_csv = self.ver / "data" / "rarita.csv"
        self.config_ffb = self.ver / "pack" / "config" / "farmingforblockheads-common.toml"
        self.db_path = self.vasi / "vasi.sqlite"
        self.query_dir = self.ver / "mod-knowledge" / "botany-pots" / "query"

    # ---------------------------------------------------------------- uso
    def aggiornato(self) -> bool:
        """Vero se il database esiste ed è più recente di inventario, datapack e CSV delle regole."""
        if not self.db_path.exists():
            return False
        t = self.db_path.stat().st_mtime
        fonti = [*self.inventario.rglob("*.json"), *self.datapack.rglob("*.json"), *self.vasi.glob("*.csv"),
                 *self.mercato.glob("*.csv"), *self.pozioni.glob("*.csv"),
                 *self.dump.glob("*.json"), *([self.rarita_csv] if self.rarita_csv.exists() else []),
                 *([self.config_ffb] if self.config_ffb.exists() else []), Path(__file__)]
        return all(f.stat().st_mtime <= t for f in fonti)

    def connetti(self) -> sqlite3.Connection:
        if not self.aggiornato():
            self.refresh()
        c = sqlite3.connect(self.db_path)
        c.execute("PRAGMA foreign_keys = ON")
        c.row_factory = sqlite3.Row
        return c

    def query(self, sql: str, params=()) -> list[sqlite3.Row]:
        with self.connetti() as c:
            return c.execute(sql, params).fetchall()

    def analisi(self, nome: str, params=()) -> list[sqlite3.Row]:
        """Esegue la query salvata in mod-knowledge/botany-pots/query/<nome>.sql."""
        p = self.query_dir / f"{nome}.sql"
        if not p.exists():
            disponibili = ", ".join(sorted(q.stem for q in self.query_dir.glob("*.sql")))
            raise FileNotFoundError(f"query {nome} non trovata in {self.query_dir} (disponibili: {disponibili})")
        return self.query(p.read_text(encoding="utf-8"), params)

    def tabelle(self) -> list[tuple[str, str, int]]:
        out = []
        with self.connetti() as c:
            for nome, tipo in c.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table','view') ORDER BY type DESC, name"):
                n = c.execute(f'SELECT count(*) FROM "{nome}"').fetchone()[0]
                out.append((nome, "vista" if tipo == "view" else "tabella", n))
        return out

    def controlli(self, conn: sqlite3.Connection | None = None) -> list[tuple[str, bool, str]]:
        """Controlli di coerenza oltre ai vincoli: (nome, esito, dettaglio)."""
        c = conn or self.connetti()
        out = []

        def ctl(nome, sql, atteso=0, dettaglio=""):
            n = c.execute(sql).fetchone()[0]
            out.append((nome, n == atteso, f"{dettaglio or 'trovati'}: {n}"))

        out.append(("chiavi esterne valide", not c.execute("PRAGMA foreign_key_check").fetchall(), ""))
        ctl("un solo file vincente per terreno", "SELECT count(*) FROM (SELECT terreno_id FROM POTS_TERRENO_VINCENTE GROUP BY terreno_id HAVING count(*)>1)")
        ctl("un solo file vincente per coltura", "SELECT count(*) FROM (SELECT coltura_id FROM POTS_COLTURA_VINCENTE GROUP BY coltura_id HAVING count(*)>1)")
        ctl("un seme non trova due colture vincenti", "SELECT count(*) FROM (SELECT s.seme FROM POTS_COLTURA_SEME s JOIN POTS_COLTURA_VINCENTE p ON p.ricetta_id=s.ricetta_id AND p.fonte=s.fonte GROUP BY s.seme HAVING count(*)>1)")
        ctl("ogni coltura ha almeno un seme", "SELECT count(*) FROM POTS_COLTURA p WHERE NOT EXISTS (SELECT 1 FROM POTS_COLTURA_SEME s WHERE s.ricetta_id=p.ricetta_id AND s.fonte=p.fonte)")
        ctl("ogni coltura ha almeno un tag", "SELECT count(*) FROM POTS_COLTURA p WHERE NOT EXISTS (SELECT 1 FROM POTS_COLTURA_TAG t WHERE t.ricetta_id=p.ricetta_id AND t.fonte=p.fonte)")
        ctl("ogni coltura vincente ha almeno un terreno", "SELECT count(*) FROM POTS_COLTURA_VINCENTE p WHERE NOT EXISTS (SELECT 1 FROM POTS_COMPATIBILITA k WHERE k.coltura_id=p.coltura_id)")
        ctl("i terreni in_vaso hanno un file vincente", "SELECT count(*) FROM TERRENO t WHERE (stato='in_vaso') <> EXISTS (SELECT 1 FROM POTS_TERRENO_VINCENTE p WHERE p.terreno_id=t.terreno_id)")
        n = c.execute("SELECT count(*) FROM (SELECT ricetta_id FROM POTS_TERRENO_VINCENTE WHERE avviso UNION ALL SELECT ricetta_id FROM POTS_COLTURA_VINCENTE WHERE avviso)").fetchone()[0]
        out.append(("avviso: id portati da due jar (non blocca)", True, f"trovati: {n}"))
        n = c.execute("SELECT count(*) FROM TERRENO t WHERE t.stato='in_vaso' AND NOT EXISTS (SELECT 1 FROM TERRENO_RARITA r WHERE r.terreno_id=t.terreno_id)").fetchone()[0]
        out.append(("avviso: terreni in vaso senza classe di rarità (non blocca)", True, f"trovati: {n}"))
        # mercato
        ctl("ogni voce vincente ha il suo preset", "SELECT count(*) FROM MERCATO_VOCE_VINCENTE v WHERE NOT EXISTS (SELECT 1 FROM MERCATO_PRESET_VINCENTE p WHERE p.preset_id=v.preset_id)")
        ctl("un oggetto non ha due voci attive", "SELECT count(*) FROM (SELECT oggetto_id FROM MERCATO_VOCE_ATTIVA GROUP BY oggetto_id HAVING count(*)>1)")
        ctl("nessun prezzo oltre i 64 senza blocco", "SELECT count(*) FROM MERCATO_PREZZO WHERE oltre_limite")
        ctl("i prezzi crescono con la classe dentro ogni intervallo", """
            SELECT count(*) FROM MERCATO_BASE x
            JOIN MERCATO_PREZZO a ON a.origine=x.origine AND a.ordine BETWEEN x.ordine_min AND x.ordine_max
            JOIN RARITA ra ON ra.classe=a.classe
            JOIN MERCATO_PREZZO b ON b.origine=x.origine AND b.ordine=a.ordine+1 AND b.ordine<=x.ordine_max
            JOIN RARITA rb ON rb.classe=b.classe AND rb.famiglia=ra.famiglia
            WHERE b.quantita_unitaria <= a.quantita_unitaria
               OR (b.pagamento_id = a.pagamento_id AND b.quantita <= a.quantita)""")
        ctl("gli intervalli di MERCATO_BASE coprono 0–9 senza sovrapporsi", """
            SELECT count(*) FROM (SELECT origine FROM MERCATO_BASE GROUP BY origine
              HAVING sum(ordine_max-ordine_min+1) <> 10 OR min(ordine_min) <> 0 OR max(ordine_max) <> 9)""")
        ctl("i preset sostituiti esistono nei jar", "SELECT count(*) FROM MERCATO_PRESET_CUSTOM c WHERE NOT EXISTS (SELECT 1 FROM MERCATO_PRESET p WHERE p.preset_id=c.preset_id AND p.strato='originale')")
        ctl("le origini delle regole del mercato esistono in MERCATO_BASE", "SELECT count(*) FROM (SELECT origine FROM MERCATO_MOD_CUSTOM UNION SELECT origine FROM MERCATO_VOCE_CUSTOM WHERE origine IS NOT NULL UNION SELECT origine FROM MERCATO_PRESET_CUSTOM WHERE origine IS NOT NULL) o WHERE NOT EXISTS (SELECT 1 FROM MERCATO_BASE b WHERE b.origine=o.origine)")
        n = c.execute("SELECT count(*) FROM MERCATO_CANDIDATO WHERE escluso IS NULL AND (origine IS NULL OR classe IS NULL)").fetchone()[0]
        out.append(("avviso: candidati del mercato senza regola (non blocca)", True, f"trovati: {n}"))
        # datapack
        ctl("i modificatori del bottino con il nostro nome sono elencati in global_loot_modifiers.json", "SELECT count(*) FROM NOSTRO_MODIFICATORE WHERE NOT elencato AND modificatore_id LIKE 'matteo_tweaks:%'")
        # pozioni
        ctl("una sola regola 'tutte' per famiglia di pozioni", "SELECT count(*) FROM (SELECT x.famiglia FROM POZIONE_CUSTOM c JOIN POZIONE x ON x.pozione_id=c.pozione_id WHERE c.varianti='tutte' GROUP BY x.famiglia HAVING count(*)>1)")
        dump = c.execute("SELECT count(*) FROM DUMP_MOD").fetchone()[0] > 0
        n = c.execute("SELECT count(*) FROM POZIONE_LISTA_NERA WHERE dedotta AND gioco IS NOT 1").fetchone()[0]
        out.append(("avviso: pozioni in lista nera con il nome dedotto e non confermato dal gioco (non blocca)", True, f"trovate: {n}"))
        if not dump:
            out.append(("avviso: nessun dump del gioco in data/dump/ (non blocca)", True, "lanciare /mango_dump e scripts/dump_importa.py"))
        else:
            vecchio = c.execute("SELECT count(*) FROM DUMP_MOD_DIVERSA").fetchone()[0]
            out.append(("avviso: mod con versione diversa tra inventario e dump: dump vecchio (non blocca)", True, f"trovate: {vecchio}"))
            if not vecchio:
                ctl("le pozioni in lista nera esistono nel gioco", "SELECT count(*) FROM POZIONE_LISTA_NERA WHERE gioco = 0")
            for nome, sql in (("pozioni dell'inventario che il gioco non ha", "SELECT count(*) FROM POZIONE WHERE inventario AND gioco = 0"),
                              ("pozioni del gioco che l'inventario non ha", "SELECT count(*) FROM POZIONE WHERE NOT inventario"),
                              ("pozioni in lista nera che l'amuleto rifiuta comunque", "SELECT count(*) FROM POZIONE_AMULETO WHERE regola = 0 AND valida = 0")):
                n = c.execute(sql).fetchone()[0]
                out.append((f"avviso: {nome} (non blocca)", True, f"trovate: {n}"))
            if self._saltati_dump:
                out.append(("avviso: righe del dump saltate (non blocca)", True, ", ".join(f"{k} {v}" for k, v in sorted(self._saltati_dump.items()))))
            # formato 2: il lavoro di tutte le versioni confrontato con il gioco (bloccano solo se il dump è aggiornato)
            if c.execute("SELECT count(*) FROM GIOCO_RICETTA").fetchone()[0]:
                info = dict(c.execute("SELECT chiave, valore FROM DUMP_INFO").fetchall())
                dp_cambiato = info.get("datapack_sha256") != info.get("datapack_attuale")
                if dp_cambiato:
                    out.append(("avviso: il datapack è cambiato dopo il dump: i confronti con il gioco non bloccano (non blocca)", True, "rilanciare /mango_dump"))
                blocca = not vecchio and not dp_cambiato
                for nome, sql in (("le nostre ricette caricabili sono nel gioco (e le altre no)", "SELECT count(*) FROM NOSTRA_RICETTA_DIVERSA"),
                                  ("le voci dei nostri tag sono nelle etichette finali del gioco", "SELECT count(*) FROM NOSTRO_TAG_MANCANTE"),
                                  ("le tabelle del bottino nostre e quelle dei nostri modificatori esistono nel gioco", "SELECT count(*) FROM NOSTRA_TABELLA_MANCANTE")):
                    n = c.execute(sql).fetchone()[0]
                    out.append((nome if blocca else f"avviso: {nome} (dump non aggiornato, non blocca)", n == 0 or not blocca, f"trovati: {n}"))
                n = c.execute("SELECT count(*) FROM GIOCO_ID_DIVERSO WHERE dove = 'solo nel gioco'").fetchone()[0]
                m = c.execute("SELECT count(*) FROM GIOCO_ID_DIVERSO WHERE dove <> 'solo nel gioco'").fetchone()[0]
                out.append(("avviso: oggetti creati all'avvio, non nell'inventario / dell'inventario non nel gioco (non blocca)", True, f"{n} / {m}"))
            else:
                out.append(("avviso: dump senza le sezioni del formato 2: ricette, tag, tabelle non confrontate (non blocca)", True, "rilanciare /mango_dump"))
        if self._coppie_attese is not None:
            n = c.execute("SELECT count(*) FROM (SELECT DISTINCT terreno_id, coltura_id FROM POTS_COMPATIBILITA)").fetchone()[0]
            out.append(("coppie terreno-coltura = conteggio diretto sui file", n == self._coppie_attese, f"vista {n}, diretto {self._coppie_attese}"))
        if conn is None:
            c.close()
        return out

    # ---------------------------------------------------------------- costruzione
    _coppie_attese = None

    def refresh(self) -> list[tuple[str, bool, str]]:
        dati = self._leggi_fonti()
        fd, tmp = tempfile.mkstemp(suffix=".sqlite", dir=self.vasi)
        os.close(fd)
        try:
            c = sqlite3.connect(tmp)
            c.execute("PRAGMA foreign_keys = ON")
            c.executescript(SCHEMA)
            self._carica(c, dati)
            c.commit()
            esiti = self.controlli(c)
            c.close()
            falliti = [e for e in esiti if not e[1]]
            if falliti:
                raise ErroreDati("controlli falliti: " + "; ".join(f"{n} ({d})" for n, _, d in falliti))
            os.replace(tmp, self.db_path)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)
        return esiti

    def _leggi_fonti(self) -> dict:
        items, blocks, mods = {}, {}, set()   # id -> nome inglese ("" se manca)
        tag_voci = {"oggetti": defaultdict(list), "blocchi": defaultdict(list)}  # (fonte, voce, facoltativa)
        ricette, voci, preset, categorie = [], [], [], {}
        mod_righe, modid_righe = [], []
        effetti, descrizioni, pozioni, dedotte = {}, {}, {}, set()  # id -> (slug, nome)
        ns_conta = defaultdict(Counter)  # namespace -> {slug: oggetti+blocchi}
        files = [self.inventario / "minecraft.json", self.inventario / "neoforge.json", *sorted((self.inventario / "mods").glob("*.json"))]
        for f in files:
            if not f.exists():
                continue
            d = _carica_json(f)
            fonte = f.stem
            for k, v in (d.get("items") or {}).items():
                items[k] = items.get(k) or v or ""
            for k, v in (d.get("blocks") or {}).items():
                blocks[k] = blocks.get(k) or v or ""
            mods |= {m["modid"] for m in d.get("mods", [])}
            for cat in (d.get("data") or {}).get("market_categories") or []:
                categorie.setdefault(cat, fonte)
            for r in d.get("market") or []:
                voci.append({**r, "_fonte": fonte, "_strato": "originale"})
            for r in d.get("market_presets") or []:
                preset.append({**r, "_fonte": fonte, "_strato": "originale"})
            dichiarate = d.get("mods") or []
            nome = d.get("name") or (dichiarate[0]["name"] if dichiarate else fonte)
            mod_righe.append((fonte, nome, d.get("file"), d.get("source") or "gioco", d.get("side")))
            visti = set()
            # l'inventario può ripetere un id (più copie incorporate, o il vecchio mods.toml accanto al nuovo):
            # vince la voce di neoforge.mods.toml del jar della mod, l'unico file che NeoForge 1.21.1 legge
            for m in sorted(dichiarate, key=lambda m: (bool(m.get("jar")), bool(m.get("legacy")))):
                if m["modid"] not in visti:
                    visti.add(m["modid"])
                    modid_righe.append((m["modid"], fonte, m.get("name"), m.get("version"), 1 if m.get("jar") else 0))
            for i in {*d.get("items", {}), *d.get("blocks", {})}:
                ns_conta[i.split(":")[0]][fonte] += 1
            for amb, cat in (("oggetti", "tags/item"), ("blocchi", "tags/block")):
                for nome, vals in (d.get("tags", {}).get(cat) or {}).items():
                    for v in vals:
                        tag_voci[amb][nome].append((fonte, v.rstrip("?"), v.endswith("?")))
            for r in d.get("botanypots") or []:
                ricette.append({**r, "_fonte": fonte, "_strato": "originale"})
            for k, v in (d.get("effects") or {}).items():
                effetti.setdefault(k, (fonte, v or None))
            for k, v in (d.get("effect_descriptions") or {}).items():
                descrizioni.setdefault(k, v)
            for k, v in (d.get("potions") or {}).items():
                pozioni.setdefault(k, (fonte, v or None))
            dedotte |= set(d.get("potions_deduced") or [])
        if not items:
            raise ErroreDati(f"inventario vuoto o assente: {self.inventario}")
        # datapack: tag e ricette
        for f in self.datapack.glob("*/tags/*/**/*.json"):
            rel = f.relative_to(self.datapack).parts
            amb = {"item": "oggetti", "block": "blocchi"}.get(rel[2])
            if amb is None:
                continue
            d = _carica_json(f)
            if d.get("replace"):
                raise ErroreDati(f"tag con replace=true non previsto: {f}")
            nome = f"{rel[0]}:{'/'.join(rel[3:])[:-5]}"
            for v in d.get("values", []):
                vid, fac = (v, False) if isinstance(v, str) else (v["id"], not v.get("required", True))
                tag_voci[amb][nome].append((NOSTRO, vid, fac))
        nostri = {"ricette": [], "tag": [], "tabelle": [], "modificatori": []}
        for f in self.datapack.glob("*/recipe/**/*.json"):
            d = _carica_json(f)
            rel = f.relative_to(self.datapack).parts
            rid = f"{rel[0]}:{'/'.join(rel[2:])[:-5]}"
            nostri["ricette"].append((rid, str(d.get("type", "")), "/".join(rel), int(self._caricabile({**d, "id": rid}, items, blocks, mods))))
            if str(d.get("type", "")) in TIPI_TERRENO + TIPI_COLTURA:
                d["id"] = rid
                ricette.append({**d, "_fonte": NOSTRO, "_strato": "nostro"})
            elif d.get("type") == TIPO_MERCATO:
                res, pay = d.get("result") or {}, d.get("payment")
                voci.append({"id": rid, "item": res.get("item"), "count": int(res.get("count", 1)),
                             "category": d.get("category"), "preset": d.get("preset"),
                             "item_exists": [c.get("item") for c in d.get("neoforge:conditions") or []
                                             if c.get("type") == "neoforge:item_exists"],
                             "payment": pay, "_fonte": NOSTRO, "_strato": "nostro"})
        for f in self.datapack.glob("*/tags/*/**/*.json"):
            rel = f.relative_to(self.datapack).parts
            d = _carica_json(f)
            nome = f"{rel[0]}:{'/'.join(rel[3:])[:-5]}"
            for v in d.get("values", []):
                vid, fac = (v, False) if isinstance(v, str) else (v["id"], not v.get("required", True))
                if not vid.startswith("#"):
                    nostri["tag"].append((rel[2], nome, vid, int(fac)))
        for f in self.datapack.glob("*/loot_table/**/*.json"):
            rel = f.relative_to(self.datapack).parts
            d = _carica_json(f)
            tid = f"{rel[0]}:{'/'.join(rel[2:])[:-5]}"
            nostri["tabelle"].append((tid, "/".join(rel), int(self._caricabile({**d, "id": tid}, items, blocks, mods))))
        elencati = set()
        glm = self.datapack / "neoforge" / "loot_modifiers" / "global_loot_modifiers.json"
        if glm.exists():
            elencati = set(_carica_json(glm).get("entries") or [])
        for f in self.datapack.glob("*/loot_modifiers/**/*.json"):
            if f == glm:
                continue
            rel = f.relative_to(self.datapack).parts
            d = _carica_json(f)
            mid = f"{rel[0]}:{'/'.join(rel[2:])[:-5]}"
            tabelle = []

            def cerca(x):
                if isinstance(x, dict):
                    if x.get("condition") == "neoforge:loot_table_id":
                        tabelle.append(x["loot_table_id"])
                    for v in x.values():
                        cerca(v)
                elif isinstance(x, list):
                    for v in x:
                        cerca(v)
            cerca(d.get("conditions"))
            agg = d.get("table") if d.get("type") == "neoforge:add_table" else None
            ok = int(self._caricabile({**d, "id": mid}, items, blocks, mods))
            for t in tabelle or [None]:
                nostri["modificatori"].append((mid, int(mid in elencati), ok, t, agg))
        for f in self.datapack.glob("*/market_presets/*.json"):
            d = _carica_json(f)
            rel = f.relative_to(self.datapack).parts
            pay = d.get("payment") or {}
            ing = pay.get("ingredient") or {}
            preset.append({"id": f"{rel[0]}:{f.stem}", "enabled": bool(d.get("enabled", True)),
                           "payment_item": ing.get("item"), "payment_tag": ing.get("tag"),
                           "payment_count": int(pay.get("count", 1)), "_fonte": NOSTRO, "_strato": "nostro"})
        # config di FFB nel pack: le due liste che accendono o spengono i preset
        config_preset = {}
        if self.config_ffb.exists():
            import tomllib
            cfg = tomllib.loads(self.config_ffb.read_text(encoding="utf-8"))
            for k, v in cfg.items():
                if isinstance(v, dict):
                    cfg = {**cfg, **v}
            for pid in cfg.get("enabledOptionalPresets") or []:
                config_preset[pid] = 1
            for pid in cfg.get("disabledDefaultPresets") or []:
                config_preset[pid] = 0
        ns_righe = [(ns, c.most_common(1)[0][0], c.most_common(1)[0][1]) for ns, c in sorted(ns_conta.items())]
        # dump del gioco (facoltativo)
        dump = {}
        if (self.dump / "meta.json").exists():
            for s in ("meta", "effetti", "pozioni", "alambicco", "oggetti", "registri", "ricette", "tag", "tabelle", "strutture"):
                f = self.dump / f"{s}.json"
                dump[s] = _carica_json(f) if f.exists() else None
        return {"items": items, "blocks": blocks, "mods": mods, "tag_voci": tag_voci, "ricette": ricette,
                "mod": mod_righe, "mod_id": modid_righe, "mod_namespace": ns_righe,
                "voci": voci, "preset": preset, "categorie": categorie, "config_preset": config_preset,
                "effetti": effetti, "descrizioni": descrizioni, "pozioni": pozioni, "dedotte": dedotte, "dump": dump,
                "nostri": nostri}

    # -- condizioni di caricamento
    @staticmethod
    def _caricabile(r: dict, items: set, blocks: set, mods: set) -> bool:
        for cnd in r.get("bookshelf:load_conditions", []):
            t, vals = cnd["type"], cnd.get("values", [])
            if t == "bookshelf:block_exists":
                if not all(v in blocks for v in vals):
                    return False
            elif t == "bookshelf:item_exists":
                if not all(v in items for v in vals):
                    return False
            else:
                raise ErroreDati(f"condizione non prevista {t} in {r['id']}")
        for cnd in r.get("neoforge:conditions", []):
            t = cnd["type"]
            if t == "neoforge:mod_loaded":
                if cnd["modid"] not in mods:
                    return False
            elif t == "neoforge:item_exists":
                if cnd["item"] not in items:
                    return False
            else:
                raise ErroreDati(f"condizione non prevista {t} in {r['id']}")
        return True

    # -- ingredienti
    @staticmethod
    def _tag_di_soil(ing, rid: str) -> list[tuple[str, str]]:
        """Le alternative del campo `soil`: lista di (ambito, nome del tag)."""
        if ing is None:
            return [TAG_DIRT]
        if isinstance(ing, list):
            return [x for i in ing for x in BotanyPotsDB._tag_di_soil(i, rid)]
        t = ing.get("type")
        if t is None and "tag" in ing:
            return [("oggetti", ing["tag"])]
        if t == "bookshelf:block_tag":
            tags = ing["tag"] if isinstance(ing["tag"], list) else [ing["tag"]]
            return [("blocchi", x) for x in tags]
        if t in ("bookshelf:either", "neoforge:compound"):
            return [x for i in ing.get("ingredients", ing.get("children", [])) for x in BotanyPotsDB._tag_di_soil(i, rid)]
        raise ErroreDati(f"forma di `soil` non prevista in {rid}: {json.dumps(ing)[:120]}")

    @staticmethod
    def _oggetti_di_input(ing, rid: str) -> list[str]:
        if isinstance(ing, list):
            return [x for i in ing for x in BotanyPotsDB._oggetti_di_input(i, rid)]
        if isinstance(ing, dict) and "item" in ing and ing.get("type") is None:
            return [ing["item"]]
        raise ErroreDati(f"forma di `input` non prevista in {rid}: {json.dumps(ing)[:120]}")

    def _carica(self, c: sqlite3.Connection, dati: dict) -> None:
        items, blocks, mods, tag_voci = dati["items"], dati["blocks"], dati["mods"], dati["tag_voci"]
        ricette = [r for r in dati["ricette"] if self._caricabile(r, items, blocks, mods)]
        terreni_r = [r for r in ricette if r["type"] in TIPI_TERRENO]
        colture_r = [r for r in ricette if r["type"] in TIPI_COLTURA]
        c.executemany("INSERT INTO MOD VALUES (?,?,?,?,?)", dati["mod"])
        c.executemany("INSERT INTO MOD_ID VALUES (?,?,?,?,?)", dati["mod_id"])
        c.executemany("INSERT INTO MOD_NAMESPACE VALUES (?,?,?)", dati["mod_namespace"])
        c.executemany("INSERT INTO BLOCCO VALUES (?,?,?)", [(b, b.split(":")[0], n or None) for b, n in sorted(blocks.items())])
        c.executemany("INSERT INTO OGGETTO VALUES (?,?,?,?)",
                      [(i, i.split(":")[0], n or None, i if i in blocks else None) for i, n in sorted(items.items())])

        # file vincenti (stessa regola della vista): il datapack vince; tra jar, il primo per nome di fonte
        def vincenti(rs):
            best = {}
            for r in sorted(rs, key=lambda r: (r["_strato"] != "nostro", r["_fonte"])):
                best.setdefault(r["id"], r)
            return {(r["id"], r["_fonte"]) for r in best.values()}

        vinc_t, vinc_c = vincenti(terreni_r), vincenti(colture_r)

        # tag: quelli nominati dalle colture e tutto ciò che contengono
        nominati = set()
        for r in colture_r:
            nominati |= set(self._tag_di_soil(r.get("soil"), r["id"]))
        def chiusura(semi: set) -> set:
            """I tag dati e tutti quelli che contengono, a qualsiasi profondità."""
            visti, pila = set(), list(semi)
            while pila:
                amb, nome = pila.pop()
                if (amb, nome) in visti:
                    continue
                visti.add((amb, nome))
                for _f, v, _o in tag_voci[amb].get(nome, []):
                    if v.startswith("#"):
                        pila.append((amb, v[1:]))
            return visti

        tag_terreni, tag_mercato = chiusura(nominati), chiusura(set(TAG_MERCATO))
        tag_ids = {t: i + 1 for i, t in enumerate(sorted(tag_terreni | tag_mercato))}
        c.executemany("INSERT INTO TAG VALUES (?,?,?)", [(i, a, n) for (a, n), i in tag_ids.items()])

        # esplosione: per ogni terreno, i tag che lo elencano (diretti) e tutti i loro antenati
        def madri(con_nostre: bool, sotto: set) -> dict[tuple, set]:
            m = defaultdict(set)
            for (amb, nome) in sotto:
                for f, v, _o in tag_voci[amb].get(nome, []):
                    if v.startswith("#") and (con_nostre or f != NOSTRO):
                        m[(amb, v[1:])].add((amb, nome))
            return m

        def diretti(con_nostre: bool, sotto: set) -> dict[str, set]:
            d = defaultdict(set)  # oggetto -> {(ambito, nome)}
            for (amb, nome) in sotto:
                reg = items if amb == "oggetti" else blocks
                for f, v, fac in tag_voci[amb].get(nome, []):
                    if v.startswith("#") or (con_nostre is False and f == NOSTRO):
                        continue
                    if v not in reg:
                        if fac:
                            continue
                        raise ErroreDati(f"il tag {nome} ({amb}) elenca {v}, che non esiste")
                    if amb == "blocchi" and v not in items:
                        continue  # blocco senza oggetto con lo stesso nome: non può stare nello slot
                    d[v].add((amb, nome))
            return d

        def esplodi(con_nostre: bool, sotto: set) -> set[tuple]:
            m, d = madri(con_nostre, sotto), diretti(con_nostre, sotto)
            righe = set()  # (terreno, tag, tag_diretto, livello)
            for terreno, tags in d.items():
                for t0 in tags:
                    visti, fronte, liv = {t0}, [t0], 0
                    while fronte:
                        for t in fronte:
                            righe.add((terreno, t, t0, liv))
                        liv += 1
                        fronte = [p for t in fronte for p in m.get(t, ()) if p not in visti]
                        visti |= set(fronte)
                        if liv > 50:
                            raise ErroreDati(f"ciclo nei tag a partire da {t0}")
            return righe

        def esplosione(sotto: set):
            senza, con = esplodi(False, sotto), esplodi(True, sotto)
            esploso = {}
            for ogg, t, t0, liv in con:
                k = (ogg, t, t0)
                esploso[k] = min(liv, esploso.get(k, 99))
            senza_k = {(a, b, c0) for a, b, c0, _ in senza}
            return esploso, senza_k

        esploso, senza_k = esplosione(tag_terreni)
        esploso_m, senza_m = esplosione(tag_mercato)

        # anagrafiche
        for r in terreni_r:
            ogg = r["input"]["item"] if r.get("input") else r["block"]
            if r.get("input") and r["input"].get("type"):
                raise ErroreDati(f"input del terreno non previsto in {r['id']}")
            if ogg not in items:
                raise ErroreDati(f"terreno {ogg} di {r['id']} non è un oggetto")
            r["_terreno"] = ogg
        vinc_terreni = {r["_terreno"] for r in terreni_r if (r["id"], r["_fonte"]) in vinc_t}
        tutti_terreni = vinc_terreni | {r["_terreno"] for r in terreni_r} | {k[0] for k in esploso}
        c.executemany("INSERT INTO TERRENO VALUES (?,?)",
                      [(t, "in_vaso" if t in vinc_terreni else "candidato") for t in sorted(tutti_terreni)])
        for r in colture_r:
            if r.get("input"):
                semi, orig = self._oggetti_di_input(r["input"], r["id"]), "file"
            elif r["block"] in SEMI_ECCEZIONI:  # prima delle altre: il blocco può avere un omonimo che non è il seme
                semi, orig = [SEMI_ECCEZIONI[r["block"]]], "eccezione"
            elif r["block"] in items:
                semi, orig = [r["block"]], "blocco"
            else:
                raise ErroreDati(f"seme sconosciuto per {r['id']} (blocco {r['block']})")
            for s in semi:
                if s not in items:
                    raise ErroreDati(f"seme {s} di {r['id']} non è un oggetto")
            r["_semi"], r["_orig"] = semi, orig
            r["_coltura"] = r.get("block") or semi[0]
        c.executemany("INSERT OR IGNORE INTO COLTURA VALUES (?,?,?,?)",
                      [(r["_coltura"], r.get("block"), r["_coltura"].split(":")[0], "in_vaso") for r in colture_r])

        # file del vaso
        c.executemany("INSERT INTO POTS_TERRENO VALUES (?,?,?,?,?,?,?)", [
            (r["id"], r["_fonte"], r["_strato"], r["_terreno"], r.get("growth_modifier", 0), r.get("yield_modifier", 0),
             r.get("light_level", 0)) for r in terreni_r])
        c.executemany("INSERT INTO POTS_COLTURA VALUES (?,?,?,?,?,?,?)", [
            (r["id"], r["_fonte"], r["_strato"], r["_coltura"], r.get("grow_time", 1200), r.get("yield", 1),
             r.get("yield_scale", 1)) for r in colture_r])
        c.executemany("INSERT INTO POTS_COLTURA_SEME VALUES (?,?,?,?)",
                      [(r["id"], r["_fonte"], s, r["_orig"]) for r in colture_r for s in r["_semi"]])
        righe = set()
        for r in colture_r:
            for amb, nome in self._tag_di_soil(r.get("soil"), r["id"]):
                righe.add((r["id"], r["_fonte"], tag_ids[(amb, nome)], int(r.get("soil") is None)))
        c.executemany("INSERT INTO POTS_COLTURA_TAG VALUES (?,?,?,?)", sorted(righe))
        c.executemany("INSERT INTO TERRENO_TAG VALUES (?,?,?,?,?)", [
            (t, tag_ids[tag], tag_ids[t0], liv, int((t, tag, t0) not in senza_k)) for (t, tag, t0), liv in esploso.items()])

        # scelte
        self._carica_csv(c, "RARITA", self.rarita_csv, ("classe", "famiglia", "ordine"))
        self._carica_csv(c, "RARITA_POTS_SETTINGS", "rarita_pots_settings.csv", ("classe", "crescita", "resa"))
        self._carica_csv(c, "TERRENO_RARITA", "terreno_rarita.csv", ("terreno_id", "classe", "motivo"))
        self._carica_csv(c, "TERRENO_TAG_CUSTOM", "terreno_tag_custom.csv", ("terreno_id", "ambito", "tag"))
        self._carica_csv(c, "TERRENO_CUSTOM", "terreno_custom.csv", ("terreno_id", "display_blocco", "fluido", "nota"))
        self._carica_csv(c, "COLTURA_CUSTOM", "coltura_custom.csv", ("coltura_id", "mod", "seme", "tempo", "richiesti", "display_blocco", "display_offset", "rotazione", "da_provare", "nota"))
        self._carica_csv(c, "COLTURA_TAG_CUSTOM", "coltura_tag_custom.csv", ("coltura_id", "ordine", "ambito", "tag"))
        self._carica_csv(c, "COLTURA_RACCOLTO_CUSTOM", "coltura_raccolto_custom.csv", ("coltura_id", "gruppo", "tipo", "id", "count", "chance"))

        # ---- mercato di Farming for Blockheads
        c.executemany("INSERT INTO MERCATO_CATEGORIA VALUES (?,?)", sorted(dati["categorie"].items()))
        righe = []
        for r in dati["preset"]:
            if r.get("payment_item") and r["payment_item"] not in items:
                raise ErroreDati(f"il preset {r['id']} ({r['_fonte']}) chiede {r['payment_item']}, che non esiste")
            righe.append((r["id"], r["_fonte"], r["_strato"], r.get("payment_item"), r.get("payment_tag"),
                          int(r.get("payment_count", 1)), int(bool(r.get("enabled", True)))))
        c.executemany("INSERT INTO MERCATO_PRESET VALUES (?,?,?,?,?,?,?)", righe)
        c.executemany("INSERT INTO MERCATO_PRESET_CONFIG VALUES (?,?)", sorted(dati["config_preset"].items()))
        righe = []
        for r in dati["voci"]:  # solo le voci caricabili: oggetto esistente e condizioni soddisfatte (come per i vasi)
            if not r.get("item") or r["item"] not in items or any(i not in items for i in r.get("item_exists") or []):
                continue
            if r.get("category") not in dati["categorie"]:
                raise ErroreDati(f"la voce {r['id']} ({r['_fonte']}) usa la categoria sconosciuta {r.get('category')}")
            pay = r.get("payment") or {}
            pag_id = (pay.get("ingredient") or {}).get("item") if pay else None
            righe.append((r["id"], r["_fonte"], r["_strato"], r["item"], int(r.get("count", 1)), r["category"], r["preset"],
                          pag_id, int(pay["count"]) if pay else None))
        c.executemany("INSERT INTO MERCATO_VOCE VALUES (?,?,?,?,?,?,?,?,?)", righe)
        c.executemany("INSERT INTO OGGETTO_TAG VALUES (?,?,?,?,?)", [
            (o, tag_ids[tag], tag_ids[t0], liv, int((o, tag, t0) not in senza_m)) for (o, tag, t0), liv in esploso_m.items()])

        # piantabili: i semi delle colture vincenti, poi alberelli e fiori dai tag; il tipo dai tag e dal nome
        in_tag = defaultdict(set)
        for (o, tag, _t0) in esploso_m:
            in_tag[o].add(tag)
        semi_coltura = {}
        for r in colture_r:
            if (r["id"], r["_fonte"]) in vinc_c:
                for sm in r["_semi"]:
                    semi_coltura.setdefault(sm, r["_coltura"])
        piantabili = {sm: "pots_seme" for sm in semi_coltura}
        for o, tags in in_tag.items():
            if ("oggetti", "minecraft:saplings") in tags:
                piantabili.setdefault(o, "tag_saplings")
            elif ("oggetti", "minecraft:flowers") in tags:
                piantabili.setdefault(o, "tag_flowers")

        def tipo_di(o: str, origine: str) -> str:
            n, tags = o.split(":")[1], in_tag.get(o, set())
            if ("oggetti", "minecraft:saplings") in tags or n.endswith("_sapling"):
                return "alberello"
            if ("oggetti", "farmersdelight:wild_crops") in tags or n.startswith("wild_"):
                return "selvatica"
            if n.endswith("_colony"):
                return "colonia"
            if ("oggetti", "minecraft:flowers") in tags:
                return "fiore"
            if ("oggetti", "c:seeds") in tags or n.endswith(("_seeds", "_seed", "_pips", "_kernels")):
                return "seme"
            ultimo = n.rsplit("_", 1)[-1]
            if ultimo in SUFFISSI_FUNGO:
                return "fungo"
            if ultimo in SUFFISSI_VEGETAZIONE:
                return "vegetazione"
            if origine == "pots_seme":
                return "coltura"   # si pianta con il suo prodotto (cipolla, cocco, bacche)
            return "altro"

        c.executemany("INSERT INTO PIANTABILE VALUES (?,?,?,?,?)", [
            (o, orig, semi_coltura.get(o), tipo_di(o, orig), CATEGORIA_DI_TIPO[tipo_di(o, orig)])
            for o, orig in sorted(piantabili.items())])
        self._carica_csv(c, "RARITA_MERCATO_SETTINGS", self.mercato / "rarita_mercato_settings.csv", ("classe", "moltiplicatore"))
        self._carica_csv(c, "MERCATO_BASE", self.mercato / "mercato_base.csv", ("origine", "ordine_min", "ordine_max", "pagamento_id", "quantita", "blocco_id", "motivo"))
        self._carica_csv(c, "MERCATO_MOD_CUSTOM", self.mercato / "mercato_mod_custom.csv", ("slug", "origine", "classe", "motivo"))
        self._carica_csv(c, "MERCATO_TIPO_CUSTOM", self.mercato / "mercato_tipo_custom.csv", ("tipo", "categoria_id", "vendi", "motivo"))
        self._carica_csv(c, "MERCATO_VOCE_CUSTOM", self.mercato / "mercato_voce_custom.csv", ("oggetto_id", "categoria_id", "origine", "classe", "escluso", "motivo"))
        self._carica_csv(c, "MERCATO_PRESET_CUSTOM", self.mercato / "mercato_preset_custom.csv", ("preset_id", "origine", "classe", "acceso", "motivo"))

        self._carica_pozioni(c, dati, items)
        self._carica_gioco(c, dati)
        self._carica_csv(c, "POZIONE_CUSTOM", self.pozioni / "pozione_custom.csv", ("pozione_id", "varianti", "amuleto", "motivo"))

        # conteggio diretto delle coppie, indipendente dalla vista: per ogni coltura vincente, gli oggetti dei suoi tag
        membri = defaultdict(set)
        for (t, tag, _t0) in esploso:
            membri[tag].add(t)
        coppie = set()
        for r in colture_r:
            if (r["id"], r["_fonte"]) in vinc_c:
                for tag in self._tag_di_soil(r.get("soil"), r["id"]):
                    coppie |= {(t, r["_coltura"]) for t in membri[tag]}
        self._coppie_attese = len(coppie)

    _saltati_dump = None

    def _impronta_datapack(self) -> str:
        """La stessa impronta che scripts/dump_importa.py salva in meta.json (`datapack_sha256`)."""
        import hashlib
        h = hashlib.sha256()
        for f in sorted(self.datapack.rglob("*")):
            if f.is_file():
                h.update(f.relative_to(self.datapack).as_posix().encode()); h.update(b"\0"); h.update(f.read_bytes()); h.update(b"\0")
        return h.hexdigest()

    def _carica_gioco(self, c: sqlite3.Connection, dati: dict) -> None:
        """I nostri file del datapack e, se c'è, il dump del gioco nel formato 2: registri, ricette, etichette,
        tabelle del bottino, insiemi di strutture."""
        n = dati["nostri"]
        c.executemany("INSERT INTO NOSTRA_RICETTA VALUES (?,?,?,?)", n["ricette"])
        c.executemany("INSERT OR IGNORE INTO NOSTRO_TAG_VOCE VALUES (?,?,?,?)", n["tag"])
        c.executemany("INSERT INTO NOSTRA_TABELLA VALUES (?,?,?)", n["tabelle"])
        c.executemany("INSERT OR IGNORE INTO NOSTRO_MODIFICATORE VALUES (?,?,?,?,?)", n["modificatori"])
        dump = dati["dump"]
        for reg, ids in (dump.get("registri") or {}).items():
            c.executemany("INSERT OR IGNORE INTO GIOCO_ID VALUES (?,?)", [(reg, i) for i in ids])
        for tipo, ids in (dump.get("ricette") or {}).items():
            c.executemany("INSERT OR IGNORE INTO GIOCO_RICETTA VALUES (?,?)", [(i, tipo) for i in ids])
        for reg, tags in (dump.get("tag") or {}).items():
            for tag, v in tags.items():
                if isinstance(v, list):
                    c.execute("INSERT INTO GIOCO_TAG VALUES (?,?,?,1)", (reg, tag, len(v)))
                    c.executemany("INSERT OR IGNORE INTO GIOCO_TAG_VOCE VALUES (?,?,?)", [(reg, tag, i) for i in v])
                else:
                    c.execute("INSERT INTO GIOCO_TAG VALUES (?,?,?,0)", (reg, tag, v or 0))
        c.executemany("INSERT OR IGNORE INTO GIOCO_TABELLA VALUES (?)", [(t,) for t in dump.get("tabelle") or []])
        for sid, r in (dump.get("strutture") or {}).items():
            c.execute("INSERT INTO GIOCO_STRUTTURA_SET VALUES (?,?,?,?,?,?)",
                      (sid, r.get("tipo"), r.get("spaziatura"), r.get("separazione"), r.get("sale"), r.get("frequenza")))
            c.executemany("INSERT OR IGNORE INTO GIOCO_STRUTTURA_SET_VOCE VALUES (?,?,?)",
                          [(sid, e["struttura"], e["peso"]) for e in r.get("strutture") or []])

    def _carica_pozioni(self, c: sqlite3.Connection, dati: dict, items: dict) -> None:
        """Effetti e pozioni da inventario e dump; dal dump anche effetti delle pozioni, cibi e alambicco."""
        # la mod è quella che porta il namespace (una traduzione può stare nel jar di un'altra mod); per ciò che c'è
        # solo nel dump, la mod con quell'id
        ns_slug = {ns: slug for ns, slug, _n in dati["mod_namespace"]}
        modid_slug = {m: s for m, s, _n, _v, _a in dati["mod_id"]}
        def mod_di(rid: str, fonte: str | None) -> str | None:
            ns = rid.split(":")[0]
            return ns_slug.get(ns) or fonte or modid_slug.get(ns)
        dump = dati["dump"]
        saltati = Counter()
        g_eff = {r["id"]: r for r in (dump.get("effetti") or [])} if dump else {}
        g_poz = {r["id"]: r for r in (dump.get("pozioni") or [])} if dump else {}
        gioco = (lambda rid, g: int(rid in g)) if dump else (lambda rid, g: None)
        righe = []
        for e in sorted(set(dati["effetti"]) | set(g_eff)):
            s, n = dati["effetti"].get(e, (None, None))
            slug, g = mod_di(e, s), g_eff.get(e) or {}
            if slug is None:
                saltati["effetti senza mod"] += 1
                continue
            righe.append((e, slug, n, dati["descrizioni"].get(e), g.get("categoria"),
                          None if "istantaneo" not in g else int(g["istantaneo"]), g.get("colore"),
                          int(e in dati["effetti"]), gioco(e, g_eff)))
        c.executemany("INSERT INTO EFFETTO VALUES (?,?,?,?,?,?,?,?,?)", righe)
        righe = []
        for p in sorted(set(dati["pozioni"]) | set(g_poz)):
            s, n = dati["pozioni"].get(p, (None, None))
            slug = mod_di(p, s)
            if slug is None:
                saltati["pozioni senza mod"] += 1
                continue
            righe.append((p, slug, n, famiglia_pozione(p), int(p in dati["dedotte"]), (g_poz.get(p) or {}).get("traduzione"),
                          int(p in dati["pozioni"]), gioco(p, g_poz)))
        c.executemany("INSERT INTO POZIONE VALUES (?,?,?,?,?,?,?,?)", righe)
        self._saltati_dump = saltati
        if not dump:
            return
        meta = dump.get("meta") or {}
        c.executemany("INSERT INTO DUMP_MOD VALUES (?,?)", sorted((meta.get("mod") or {}).items()))
        c.executemany("INSERT INTO DUMP_INFO VALUES (?,?)", [(k, str(meta.get(k))) for k in ("data", "formato", "datapack_sha256") if meta.get(k) is not None])
        c.execute("INSERT INTO DUMP_INFO VALUES ('datapack_attuale', ?)", (self._impronta_datapack(),))
        effetti = {r[0] for r in c.execute("SELECT effetto_id FROM EFFETTO")}
        pozioni = {r[0] for r in c.execute("SELECT pozione_id FROM POZIONE")}

        def ok_eff(lista):
            if any(x["effetto"] not in effetti for x in lista):
                saltati["effetti sconosciuti"] += 1
                return False
            return True

        c.executemany("INSERT INTO POZIONE_EFFETTO VALUES (?,?,?,?,?)", [
            (p, i, x["effetto"], x["durata"], x["livello"])
            for p, r in sorted(g_poz.items()) if p in pozioni and ok_eff(r["effetti"])
            for i, x in enumerate(r["effetti"])])
        cibi, ogg_eff = [], []
        for r in dump.get("oggetti") or []:
            if r["id"] not in items:
                saltati["oggetti non nell'inventario"] += 1
                continue
            if r.get("cibo"):
                f = r["cibo"]
                cibi.append((r["id"], f["nutrizione"], f["saturazione"], int(f["sempre"]), f["secondi"]))
                if ok_eff(f["effetti"]):
                    ogg_eff += [(r["id"], "cibo", i, x["effetto"], x["durata"], x["livello"], x.get("probabilita", 1))
                                for i, x in enumerate(f["effetti"])]
            if r.get("pozione") and ok_eff(r["pozione"]["effetti"]):
                ogg_eff += [(r["id"], "pozione", i, x["effetto"], x["durata"], x["livello"], 1)
                            for i, x in enumerate(r["pozione"]["effetti"])]
        c.executemany("INSERT INTO OGGETTO_CIBO VALUES (?,?,?,?,?)", cibi)
        c.executemany("INSERT INTO OGGETTO_EFFETTO VALUES (?,?,?,?,?,?,?)", ogg_eff)
        alb = dump.get("alambicco") or {}
        viste, righe = set(), []

        def aggiungi(fonte, ing, ingr, ris):
            k = (ing["oggetto"], ing.get("pozione"), ingr, ris["oggetto"], ris.get("pozione"))
            if k in viste:
                return
            if any(x not in items for x in (k[0], k[2], k[3])) or any(x and x not in pozioni for x in (k[1], k[4])):
                saltati["ricette dell'alambicco con nomi sconosciuti"] += 1
                return
            viste.add(k)
            righe.append((len(righe) + 1, fonte, *k))

        for m in alb.get("miscele") or []:
            aggiungi("miscela", m["ingresso"], m["ingrediente"], m["risultato"])
        classi = defaultdict(lambda: [0, 0])
        for r in alb.get("ricette") or []:
            classi[r["classe"]][0] += 1
            if "risultato" in r and r.get("ingresso") and r.get("ingrediente"):
                classi[r["classe"]][1] += 1
                for ing in r["ingresso"]:
                    for ingr in r["ingrediente"]:
                        aggiungi("ricetta", ing, ingr["oggetto"], r["risultato"])
            elif r.get("provate"):  # classe propria della mod: combinazioni trovate provando ogni oggetto
                classi[r["classe"]][1] += 1
                for m in r["provate"]:
                    aggiungi("ricetta", m["ingresso"], m["ingrediente"], m["risultato"])
        c.executemany("INSERT INTO ALAMBICCO VALUES (?,?,?,?,?,?,?)", righe)
        c.executemany("INSERT INTO ALAMBICCO_CLASSE VALUES (?,?,?)", [(k, *v) for k, v in sorted(classi.items())])
        self._saltati_dump = saltati

    def _carica_csv(self, c: sqlite3.Connection, tabella: str, nome, colonne: tuple) -> None:
        p = nome if isinstance(nome, Path) else self.vasi / nome
        if not p.exists():
            return
        with p.open(encoding="utf-8", newline="") as f:
            righe = list(csv.DictReader(f))
        for r in righe:
            mancanti = [k for k in colonne if k not in r]
            if mancanti:
                raise ErroreDati(f"{nome}: colonne mancanti {mancanti}")
        c.executemany(f"INSERT INTO {tabella} ({','.join(colonne)}) VALUES ({','.join('?' * len(colonne))})",
                      [tuple(r[k] if r[k] != "" else None for k in colonne) for r in righe])


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    db, cmd = BotanyPotsDB(argv[0]), argv[1]
    if cmd == "refresh":
        for nome, ok, det in db.refresh():
            print(("✅" if ok else "❌"), nome, det)
        print("scritto", db.db_path)
    elif cmd in ("query", "analisi"):
        righe = db.query(argv[2]) if cmd == "query" else db.analisi(argv[2])
        if righe:
            print("\t".join(righe[0].keys()))
            for r in righe:
                print("\t".join("" if v is None else str(v) for v in r))
        print(f"({len(righe)} righe)")
    elif cmd == "tabelle":
        for nome, tipo, n in db.tabelle():
            print(f"{tipo:8s} {nome:24s} {n:6d}")
    elif cmd == "controlli":
        for nome, ok, det in db.controlli():
            print(("✅" if ok else "❌"), nome, det)
    else:
        print("comando sconosciuto:", cmd)
        return 2
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except BrokenPipeError:  # output troncato da `head` e simili
        sys.exit(0)
