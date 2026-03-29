#!/usr/bin/env python3
import json
import sys

def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: generate_tv_step_cert.py N OUT.json")

    n = int(sys.argv[1])
    out = sys.argv[2]

    # deterministic partition: 2 blocks
    k = max(2, n // 2)
    partition = [0 if i < k else 1 for i in range(n)]

    # deterministic step function values
    step_vals = [1.0, 0.5]

    # deterministic signed measure weights
    s = [((-1)**i) * (1.0 / n) for i in range(n)]

    f = [step_vals[partition[i]] for i in range(n)]

    lhs = abs(sum(f[i] * s[i] for i in range(n)))
    rhs = sum(abs(f[i]) * abs(s[i]) for i in range(n))
    tv = sum(abs(si) for si in s)

    cert = {
        "type": "TV_STEP_DUAL_CERT",
        "n": n,
        "partition": partition,
        "step_values": step_vals,
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
