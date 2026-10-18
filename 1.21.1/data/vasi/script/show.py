import json, sys
inv = json.load(open(sys.argv[1]))
for key in sys.argv[2:]:
    m = inv[key]
    print(f"##### {key}  ns={m['ns']} bs={m['n_blockstates']} loot={m['n_loot']}")
    for c in m["candidates"]:
        props = ",".join(f"{k}={'/'.join(v) if len(v) < 6 else v[0]+'..'+v[-1]}" for k, v in c["props"].items())
        tags = ",".join(t.split(":", 1)[1].replace("minecraft:", "mc:") for t in c["tags"] if any(x in t for x in ("sapling", "flower", "crop", "seed", "mushroom", "bee_growable", "replaceable", "dirt", "nylium", "cave_vines", "plant")))
        cov = ";".join(c["cov_block"] + c["cov_item"])
        loot = ",".join(x.split(":", 1)[1] if x.startswith(c["block"].split(":")[0] + ":") else x for x in (c["loot"] or []))
        print(f"  {c['block'].split(':',1)[1]:34} [{props}] item={'Y' if c['has_item'] else 'n'} loot=({loot}) tags=({tags}) COV={cov or '-'}")
    print("  seeds:", ", ".join(s["item"].split(":", 1)[1] + ("*" if s["cov_item"] else "") for s in m["seed_like_items"]))
