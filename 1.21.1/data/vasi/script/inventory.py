"""Inventory plant-like blocks of a mod from its resources.
Usage: python3 -I inventory.py COV.json OUT.json modkey repo_dir ns1[,ns2]
Appends/updates OUT.json (dict modkey -> data).
"""
import json, os, re, sys

PLANT_RE = re.compile(r"(sapling|propagule|mushroom|fungus|fungi|shroom|bush|crop|seed|flower|vine|sprout|roots?$|_root|lily|grass|fern|bloom|blossom|shrub|cactus|cane|reed|kelp|weed|petal|moss|plant|herb|berr|tulip|rose|daisy|lavender|wart|pod|stalk|stem|bud|leaf_pile|clover|ivy|lichen|algae|coral|sea_?grass|pickle|melon|pumpkin|gourd|squash|tomato|onion|cabbage|rice|corn|maize|garlic|pepper|bean|pea|potato|carrot|beet|lettuce|grape|tea|coffee|cotton|flax|hemp|hops|barley|oat|wheat|rye|tobacco|chili|eggplant|cucumber|avocado|nut|olive|lemon|orange|apple|cherr|plum|fruit|herbs?|mint|sage|basil|thyme|chamomile|fennel|ginger|turnip|radish|cauliflower|broccoli|zucchini|spinach|kale|leek|celery|asparagus|strawberr|blueberr|raspberr|cranberr|truffle|lotus|nettle|mandrake|belladonna|wolfsbane|mugwort|yellow_dock|sunflower|poppy|dandelion|orchid|allium|bluet|iris|lupine|aster|hyacinth|trillium|snowbelle|lilac|peony|tassel|cattail|duckweed|spanish_moss)", re.I)
EXCLUDE_RE = re.compile(r"(^potted_|_potted|potted$|_wall_|_wall$|_planks|_slab|_stairs|_fence|_door|_trapdoor|_button|_pressure_plate|_sign|_log$|_wood$|_leaves$|_crate|_basket|_bag$|_sack$|_pie$|_cake|_feast|_block_|_sandwich|_soup|_stew|_jam|_juice|_box|_shelf|_table|_cabinet|_barrel|_bottle|_jar|_pot$|cooking|_bench|_chair|_lamp|_lantern|_candle|_torch|_bricks?$|_tiles?$|_carpet|_bed$|_banner|_window|_pane|_glass|_wall_hanging|hanging_sign|_mosaic|_post$|_beam$|_bale$)", re.I)
INT_PROPS = {"age", "stage", "growth", "growth_stage", "berries", "half", "part", "segment", "type", "bites", "mature", "fruit", "flowering", "has_fruit", "harvest", "grown", "pickles", "flower_amount", "amount", "size", "height", "top", "bottom", "lit", "variant", "tall", "upper", "has_berries", "ripe", "cut", "sprouted", "big", "stalk", "fertilized", "mushrooms", "flowers", "pumpkins", "pollinated"}
PLANT_TAGS = {"minecraft:saplings", "minecraft:flowers", "minecraft:small_flowers", "minecraft:tall_flowers", "minecraft:crops", "minecraft:bee_growables", "minecraft:villager_plantable_seeds", "c:seeds", "c:crops", "c:mushrooms", "minecraft:replaceable_by_trees", "minecraft:enchantment_power_transmitter", "minecraft:maintains_farmland", "minecraft:cave_vines", "minecraft:nylium", "c:flowers", "minecraft:sniffer_egg_hatch_boost", "minecraft:mushroom_grow_block", "minecraft:dirt"}


def load(p):
    try:
        with open(p, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        try:
            with open(p, encoding="utf-8-sig") as fh:
                return json.load(fh)
        except Exception:
            return None


def parse_bs(j):
    props = {}
    if not isinstance(j, dict):
        return props
    if "variants" in j:
        for key in j["variants"].keys():
            if not key:
                continue
            for part in key.split(","):
                if "=" in part:
                    k, v = part.split("=", 1)
                    props.setdefault(k.strip(), set()).add(v.strip())
    if "multipart" in j:
        def walk_when(w):
            if isinstance(w, dict):
                for k, v in w.items():
                    if k in ("OR", "AND"):
                        for x in v:
                            walk_when(x)
                    else:
                        for vv in str(v).split("|"):
                            props.setdefault(k, set()).add(vv.lstrip("!"))
        for part in j["multipart"]:
            walk_when(part.get("when", {}))
    return props


def loot_items(j):
    items, conds = set(), []
    def walk(o):
        if isinstance(o, dict):
            if o.get("type") in ("minecraft:item", "item") and "name" in o:
                items.add(o["name"])
            if o.get("condition") in ("minecraft:block_state_property", "block_state_property"):
                conds.append(o.get("properties"))
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(j)
    return sorted(items), conds


def main():
    cov_path, out_path, modkey, repo, nss = sys.argv[1:6]
    nss = nss.split(",")
    cov = load(cov_path) or []
    blockstates, loots, tags, lang, item_models, botany = {}, {}, {}, {}, set(), []
    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in (".git", "build", "bin", "out", ".gradle", "run", "runs")]
        for f in files:
            p = os.path.join(root, f)
            rp = p.replace(os.sep, "/")
            if not f.endswith(".json"):
                continue
            m = re.search(r"/assets/([^/]+)/blockstates/(.+)\.json$", rp)
            if m and m.group(1) in nss:
                bid = f"{m.group(1)}:{m.group(2)}"
                j = load(p)
                pr = parse_bs(j)
                old = blockstates.get(bid, {})
                for k, v in pr.items():
                    old.setdefault(k, set()).update(v)
                blockstates[bid] = old
                continue
            m = re.search(r"/data/([^/]+)/loot_tables?/blocks/(.+)\.json$", rp)
            if m and m.group(1) in nss:
                j = load(p)
                if j is not None:
                    loots[f"{m.group(1)}:{m.group(2)}"] = loot_items(j)
                continue
            m = re.search(r"/data/([^/]+)/tags/(blocks?|items?)/(.+)\.json$", rp)
            if m:
                j = load(p)
                if isinstance(j, dict):
                    tname = f"{m.group(1)}:{m.group(3)}"
                    kind = "block" if m.group(2).startswith("block") else "item"
                    for v in j.get("values", []):
                        vid = v["id"] if isinstance(v, dict) else v
                        if isinstance(vid, str) and not vid.startswith("#") and vid.split(":")[0] in nss:
                            tags.setdefault(vid, set()).add(f"{kind}:{tname}")
                continue
            m = re.search(r"/assets/([^/]+)/lang/en_us\.json$", rp)
            if m and m.group(1) in nss:
                j = load(p)
                if isinstance(j, dict):
                    lang.update(j)
                continue
            m = re.search(r"/assets/([^/]+)/models/item/(.+)\.json$", rp)
            if m and m.group(1) in nss:
                item_models.add(f"{m.group(1)}:{m.group(2)}")
                continue
            m = re.search(r"/assets/([^/]+)/items/(.+)\.json$", rp)
            if m and m.group(1) in nss:
                item_models.add(f"{m.group(1)}:{m.group(2)}")

    # all ids known
    all_blocks = set(blockstates) | set(loots)
    # items from lang
    lang_items = set()
    for k in lang:
        mm = re.match(r"(item|block)\.([^.]+)\.([^.]+)$", k)
        if mm and mm.group(2) in nss:
            lang_items.add(f"{mm.group(2)}:{mm.group(3)}")
            if mm.group(1) == "block":
                all_blocks.add(f"{mm.group(2)}:{mm.group(3)}")
    all_items = item_models | lang_items

    # coverage lookup
    cov_by_block, cov_by_item = {}, {}
    for r in cov:
        if "error" in r:
            continue
        b = r.get("block")
        if isinstance(b, str):
            cov_by_block.setdefault(b, []).append(f"{r['src']}:{r['path']}")
        inp = r.get("input")
        ids = []
        def wi(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k in ("item", "id", "tag") and isinstance(v, str):
                        ids.append(("#" if k == "tag" else "") + v)
                    else:
                        wi(v)
            elif isinstance(o, list):
                for v in o:
                    wi(v)
        wi(inp)
        for i in ids:
            cov_by_item.setdefault(i, []).append(f"{r['src']}:{r['path']}")

    cands = []
    for bid in sorted(all_blocks):
        name = bid.split(":", 1)[1]
        props = {k: sorted(v, key=lambda x: (len(x), x)) for k, v in blockstates.get(bid, {}).items()}
        t = sorted(tags.get(bid, []))
        tagged = any(x.split(":", 1)[1] in PLANT_TAGS for x in t)
        has_age = any(k in ("age", "stage", "growth", "growth_stage") for k in props)
        if not (has_age or tagged or PLANT_RE.search(name)):
            continue
        if EXCLUDE_RE.search(name) and not has_age and not tagged:
            continue
        li = loots.get(bid)
        c = {
            "block": bid,
            "name": lang.get(f"block.{bid.replace(':', '.')}"),
            "props": {k: v for k, v in props.items() if k not in ("facing", "waterlogged", "axis", "north", "south", "east", "west", "up", "down", "persistent", "distance")},
            "tags": t,
            "loot": li[0] if li else None,
            "loot_conds": li[1][:3] if li else None,
            "has_item": bid in all_items,
            "cov_block": cov_by_block.get(bid, []),
            "cov_item": cov_by_item.get(bid, []),
        }
        cands.append(c)
    seeds = sorted(i for i in all_items if re.search(r"(seed|pit|kernel|bulb|spore|bean|sprout|cutting|_root|tuber|clove|rhizome)", i))
    out = load(out_path) or {}
    out[modkey] = {"repo": repo, "ns": nss, "n_blockstates": len(blockstates), "n_loot": len(loots),
                   "candidates": cands, "seed_like_items": [{"item": s, "cov_item": cov_by_item.get(s, [])} for s in seeds],
                   "items": sorted(all_items),
                   "blocks": {b: {"props": {k: sorted(v, key=lambda x: (len(x), x)) for k, v in blockstates.get(b, {}).items() if k not in ("facing", "waterlogged", "axis", "north", "south", "east", "west", "up", "down", "persistent", "distance")}, "loot": (loots.get(b) or [None])[0], "loot_conds": (loots.get(b) or [None, None])[1]} for b in sorted(set(blockstates) | set(loots))}}
    with open(out_path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(modkey, "bs", len(blockstates), "loot", len(loots), "cands", len(cands), "seeds", len(seeds), "items", len(all_items))

main()
