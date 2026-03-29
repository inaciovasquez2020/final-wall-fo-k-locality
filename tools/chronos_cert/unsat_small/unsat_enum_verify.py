import itertools, json, sys
from typing import List, Dict, Any

def eval_clause(cl: List[int], a: List[int]) -> bool:
    for lit in cl:
        v = a[abs(lit)-1]
        if lit > 0 and v == 1:
            return True
        if lit < 0 and v == 0:
            return True
    return False

def eval_cnf(cnf: List[List[int]], a: List[int]) -> bool:
    return all(eval_clause(cl,a) for cl in cnf)

def load(path: str) -> Dict[str, Any]:
    with open(path,"r",encoding="utf-8") as f:
        return json.load(f)

def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print("usage: unsat_enum_verify.py CERT.json")
        return 1

    cert = load(argv[1])
    inst = cert["instance"]
    n = int(inst["n_vars"])
    cnf = inst["cnf"]

    if n > 10:
        print("FAIL n_vars > 10")
        return 2

    for a in itertools.product([0,1], repeat=n):
        if eval_cnf(cnf, list(a)):
            print("FAIL found satisfying assignment", list(a))
            return 2

    print("PASS UNSAT by enumeration")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
