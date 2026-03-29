#!/usr/bin/env python3
import json
import sys
from typing import List

def l1_norm_signed(vals: List[float]) -> float:
    return sum(abs(v) for v in vals)

def signed_integral(f: List[float], s: List[float]) -> float:
    return sum(fi * si for fi, si in zip(f, s))

def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: generate_tv_finite_cert.py N OUT.json")

    n = int(sys.argv[1])
    out = sys.argv[2]

    # deterministic model
    f = [(i + 1) / n for i in range(n)]
    s = [(-1 if i % 2 else 1) * (1.0 / n) for i in range(n)]

    tv = l1_norm_signed(s)
    lhs = abs(signed_integral(f, s))
    rhs = sum(abs(fi) * abs(si) for fi, si in zip(f, s))

    cert = {
        "type": "TV_FINITE_DUAL_CERT",
        "n": n,
        "f": f,
        "signed_measure": s,
        "total_variation": tv,
        "lhs_abs_integral": lhs,
        "rhs_tv_bound": rhs,
        "inequality_holds": lhs <= rhs + 1e-12
    }

    with open(out, "w", encoding="utf-8") as fh:
        json.dump(cert, fh, indent=2)

if __name__ == "__main__":
    main()
