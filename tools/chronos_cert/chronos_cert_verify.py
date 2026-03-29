#!/usr/bin/env python3
import json, sys
from typing import List, Dict, Any


def load_cert(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def verify(cert: Dict[str, Any]) -> int:
    inst = cert["instance"]
    bound = cert["bound"]
    trace = cert["trace"]

    M = int(inst["n_states"])
    H0_lower = float(inst.get("H0_lower", 0.0))
    C = float(bound["C"])
    eps = float(bound.get("epsilon", 0.0))
    post = trace["posteriors"]

    if C <= 0:
        raise ValueError("C must be > 0")
    if len(post) < 2:
        raise ValueError("need at least 2 posteriors")

    Ps = []
    for i, obj in enumerate(post):
        p = obj["p"]
        if len(p) != M:
            raise ValueError(f"posterior {i} has len {len(p)} != {M}")
        from entropy_utils import normalize
        p = normalize([float(x) for x in p])
        Ps.append(p)

    from entropy_utils import entropy_bits
    Hs = [entropy_bits(p) for p in Ps]
    drops = [Hs[t] - Hs[t+1] for t in range(len(Hs)-1)]
    max_drop = max(drops)

    ok = True
    for t, d in enumerate(drops):
        if d > C + 1e-8:
            ok = False
            print(f"FAIL step {t}: drop={d:.12g} > C={C:.12g}")
    HT = Hs[-1]
    if HT > eps + 1e-8:
        ok = False
        print(f"FAIL terminal: H_T={HT:.12g} > eps={eps:.12g}")

    T = len(Hs) - 1
    lb = (H0_lower - eps) / C

    print("PASS" if ok else "FAIL")
    print(f"T={T}")
    print(f"H0={Hs[0]:.12g}")
    print(f"HT={HT:.12g}")
    print(f"max_drop={max_drop:.12g}")
    print(f"lower_bound_T >= (H0_lower-eps)/C = {lb:.12g}   (H0_lower={H0_lower:.12g})")
    return 0 if ok else 2

def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print("usage: chronos_cert_verify.py CERT.json", file=sys.stderr)
        return 1
    cert = load_cert(argv[1])
    return verify(cert)

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
