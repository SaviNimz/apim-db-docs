#!/usr/bin/env python3
"""diff.py <snapA> <snapB> [--rows N]: per-table inserted/deleted rows between two snapshots."""
import sys, re, os
from collections import defaultdict
def load(d):
    rows = defaultdict(list)
    for db in ("WSO2AM_DB", "WSO2SHARED_DB"):
        p = os.path.join(d, db + ".sql")
        if not os.path.exists(p): continue
        for line in open(p, encoding="utf-8", errors="replace"):
            m = re.match(r'INSERT INTO "?PUBLIC"?\."?(\w+)"?(?:\(.*?\))? VALUES ?\((.*)\);\s*$', line)
            if m: rows[m.group(1).upper()].append(m.group(2))
    return rows
a, b = load(sys.argv[1]), load(sys.argv[2])
nrows = int(sys.argv[sys.argv.index("--rows") + 1]) if "--rows" in sys.argv else 3
for t in sorted(set(a) | set(b)):
    A, B = a.get(t, []), b.get(t, [])
    sa, sb = set(A), set(B)
    add = [r for r in B if r not in sa]; rem = [r for r in A if r not in sb]
    if not add and not rem: continue
    kind = "UPDATED?" if add and rem else ("INSERT" if add else "DELETE")
    print(f"{t}: +{len(add)} -{len(rem)}  [{kind}]")
    for r in add[:nrows]: print("    + " + r[:260])
    for r in rem[:nrows]: print("    - " + r[:260])
