#!/usr/bin/env python3
"""Base dati dei vasi di Botany Pots: terreni, colture, tag e le nostre scelte di rarità, in SQLite.

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
- <versione>/data/vasi/*.csv: le regole nostre, scritte a mano.
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
  versione TEXT,
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
"""


class ErroreDati(Exception):
    pass


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
                 *self.mercato.glob("*.csv"), *([self.rarita_csv] if self.rarita_csv.exists() else []),
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
            for m in dichiarate:
                if m["modid"] not in visti:  # l'inventario può ripetere un id
                    visti.add(m["modid"])
                    modid_righe.append((m["modid"], fonte, m.get("name"), m.get("version")))
            for i in {*d.get("items", {}), *d.get("blocks", {})}:
                ns_conta[i.split(":")[0]][fonte] += 1
            for amb, cat in (("oggetti", "tags/item"), ("blocchi", "tags/block")):
                for nome, vals in (d.get("tags", {}).get(cat) or {}).items():
                    for v in vals:
                        tag_voci[amb][nome].append((fonte, v.rstrip("?"), v.endswith("?")))
            for r in d.get("botanypots") or []:
                ricette.append({**r, "_fonte": fonte, "_strato": "originale"})
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
        for f in self.datapack.glob("*/recipe/**/*.json"):
            d = _carica_json(f)
            rel = f.relative_to(self.datapack).parts
            rid = f"{rel[0]}:{'/'.join(rel[2:])[:-5]}"
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
        return {"items": items, "blocks": blocks, "mods": mods, "tag_voci": tag_voci, "ricette": ricette,
                "mod": mod_righe, "mod_id": modid_righe, "mod_namespace": ns_righe,
                "voci": voci, "preset": preset, "categorie": categorie, "config_preset": config_preset}

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
        c.executemany("INSERT INTO MOD_ID VALUES (?,?,?,?)", dati["mod_id"])
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
