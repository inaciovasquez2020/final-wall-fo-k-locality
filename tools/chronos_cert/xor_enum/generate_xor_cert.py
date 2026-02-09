#!/usr/bin/env python3
import itertools, json, math, os

def mat_vec_mod2(A, x):
    return [sum(a*b for a,b in zip(row,x)) % 2 for row in A]

def satisfies(A, b, x):
    return mat_vec_mod2(A, x) == b

def entropy_bits(p):
    h = 0.0
    for v in p:
        if v > 0:
            h -= v * math.log2(v)
    return h

def posterior(solutions, predicate):
    keep = [s for s in solutions if predicate(s)]
    if len(keep) == 0:
        return None
    w = 1.0 / len(keep)
    return [w if s in keep else 0.0 for s in solutions]

def main():
    out_dir = "tools/chronos_cert/examples/xor_enum_3vars"
    os.makedirs(out_dir, exist_ok=True)
    out_path = f"{out_dir}/CERT.json"

    A = [
        [1,1,0],
        [0,1,1]
    ]
    b = [0,1]

    n = 3
    all_x = list(itertools.product([0,1], repeat=n))
    sols = [x for x in all_x if satisfies(A,b,list(x))]
    M = len(sols)

    P0 = [1.0/M]*M

    predicates = [
        lambda x: x[0] == 0,
        lambda x: x[1] == 0,
        lambda x: x[2] == 0,
        lambda x: x[0] == 1,
        lambda x: x[1] == 1,
        lambda x: x[2] == 1
    ]

    P1 = None
    P2 = None

    for q1 in predicates:
        P1_try = posterior(sols, q1)
        if P1_try is None:
            continue
        for q2 in predicates:
            P2_try = posterior(sols, lambda s: q1(s) and q2(s))
            if P2_try is None:
                continue
            if entropy_bits(P2_try) < entropy_bits(P1_try):
                P1 = P1_try
                P2 = P2_try
                break
        if P1 is not None:
            break

    if P1 is None or P2 is None:
        raise RuntimeError("failed to find valid posterior chain")

    H0 = entropy_bits(P0)
    H1 = entropy_bits(P1)
    H2 = entropy_bits(P2)

    C = max(H0-H1, H1-H2)

    cert = {
        "instance": {
            "name": "xor_enum_3vars",
            "n_states": M,
            "H0_lower": float(H0)
        },
        "bound": {
            "C": float(C),
            "epsilon": float(H2)
        },
        "trace": {
            "posteriors": [
                {"p": P0},
                {"p": P1},
                {"p": P2}
            ]
        }
    }

    with open(out_path, "w") as f:
        json.dump(cert, f, indent=2)

    print("wrote", out_path)
    print("entropies", H0, H1, H2)
    print("C", C)

if __name__ == "__main__":
    main()
