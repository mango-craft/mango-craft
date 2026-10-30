import json, sys, re
inv = json.load(open(sys.argv[1]))
EX = re.compile(r"(planks|stairs|slab|_wall$|fence|door|trapdoor|_sign|button|pressure_plate|_log$|_wood$|bricks?|tiles?|pillar|chiseled|polished|smooth|cut_|_ore$|glass|pane|lamp|lantern|candle|torch|chest|barrel|bookshelf|ladder|carpet|banner|bed$|_block$|cobbled|_bars|chain|_hanging_sign|_leaves$|_boat|stripped)")
for key in sys.argv[2:]:
    m = inv[key]
    ns = m["ns"][0]
    cand = {c["block"] for c in m["candidates"]}
    items = set(m["items"])
    # blocks from loot or bs: reconstruct from items that have blockstates? use items list
    allb = sorted(i for i in items if not EX.search(i.split(":",1)[1]) and i not in cand)
    print(f"#### {key}: non-candidate items ({len(allb)}):")
    print("  " + " ".join(i.split(":",1)[1] for i in allb))
