#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
from typing import List, Dict, Any, Tuple

def die(msg: str) -> None:
    raise SystemExit(f"VERIFY_FAIL: {msg}")

def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def mat_from_flat(m: int, n: int, entries: List[int]) -> List[List[int]]:
    if len(entries) != m * n:
        die(f"matrix entries length {len(entries)} != m*n {m*n}")
    A = []
    k = 0
    for i in range(m):
        row = []
        for j in range(n):
            v = entries[k]
            if v not in (-1, 0, 1):
                die(f"matrix entry not in {{-1,0,1}} at flat index {k}: {v}")
            row.append(v)
            k += 1
        A.append(row)
    return A

def submatrix(A: List[List[int]], rows: List[int], cols: List[int]) -> List[List[int]]:
    m = len(A)
    n = len(A[0]) if m else 0
    for r in rows:
        if r < 0 or r >= m:
            die(f"row index out of range: {r}")
    for c in cols:
        if c < 0 or c >= n:
            die(f"col index out of range: {c}")
    return [[A[r][c] for c in cols] for r in rows]

def eq_matrix(X: List[List[int]], Y: List[List[int]]) -> bool:
    if len(X) != len(Y):
        return False
    if len(X) == 0:
        return True
    if len(X[0]) != len(Y[0]):
        return False
    for i in range(len(X)):
        for j in range(len(X[0])):
            if X[i][j] != Y[i][j]:
                return False
    return True

def zeros_like(m: int, n: int) -> List[List[int]]:
    return [[0 for _ in range(n)] for _ in range(m)]

def block_diag(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    m1, n1 = len(A), (len(A[0]) if A else 0)
    m2, n2 = len(B), (len(B[0]) if B else 0)
    Z12 = zeros_like(m1, n2)
    Z21 = zeros_like(m2, n1)
    top = [A[i] + Z12[i] for i in range(m1)]
    bot = [Z21[i] + B[i] for i in range(m2)]
    return top + bot

def extract_rows_cols(node: Dict[str, Any]) -> Tuple[List[int], List[int]]:
    if "A" not in node:
        die("node missing A (rows/cols indices)")
    rows = node["A"]["rows"]
    cols = node["A"]["cols"]
    if not isinstance(rows, list) or not isinstance(cols, list):
        die("node.A.rows/cols must be lists")
    return rows, cols

def verify_network_incidence(A: List[List[int]], wit: Dict[str, Any]) -> None:
    V = wit["V"]
    E = wit["E"]
    tail = wit["tail"]
    head = wit["head"]
    row_to_vertex = wit["row_to_vertex"]
    col_to_edge = wit["col_to_edge"]
    m = len(A)
    n = len(A[0]) if m else 0
    if len(row_to_vertex) != m:
        die("network_witness.row_to_vertex length mismatch")
    if len(col_to_edge) != n:
        die("network_witness.col_to_edge length mismatch")
    if len(tail) != E or len(head) != E:
        die("network_witness tail/head length mismatch")
    for j in range(n):
        e = col_to_edge[j]
        if e < 0 or e >= E:
            die(f"col_to_edge[{j}] out of range: {e}")
        t = tail[e]
        h = head[e]
        seen_pos = []
        seen_neg = []
        for i in range(m):
            v = row_to_vertex[i]
            if v < 0 or v >= V:
                die(f"row_to_vertex[{i}] out of range: {v}")
            a = A[i][j]
            if a == 1:
                seen_pos.append(v)
            elif a == -1:
                seen_neg.append(v)
            elif a != 0:
                die("network base case: non {-1,0,1} entry")
        if len(seen_pos) != 1 or len(seen_neg) != 1:
            die(f"network base case: column {j} does not have exactly one +1 and one -1")
        if not ((seen_neg[0] == t and seen_pos[0] == h) or (seen_neg[0] == h and seen_pos[0] == t)):
            die(f"network base case: column {j} signs do not match tail/head vertices")

def apply_signed_perm_matrix(A: List[List[int]], perm_rows: List[int], perm_cols: List[int],
                             sign_rows: List[int], sign_cols: List[int]) -> List[List[int]]:
    m = len(A)
    n = len(A[0]) if m else 0
    if len(perm_rows) != m or len(sign_rows) != m:
        die("R10 witness row perm/sign length mismatch")
    if len(perm_cols) != n or len(sign_cols) != n:
        die("R10 witness col perm/sign length mismatch")
    B = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        pi = perm_rows[i]
        if pi < 0 or pi >= m:
            die("R10 perm_rows out of range")
        sr = sign_rows[i]
        if sr not in (-1, 1):
            die("R10 sign_rows not in {-1,1}")
        for j in range(n):
            pj = perm_cols[j]
            if pj < 0 or pj >= n:
                die("R10 perm_cols out of range")
            sc = sign_cols[j]
            if sc not in (-1, 1):
                die("R10 sign_cols not in {-1,1}")
            B[i][j] = sr * A[pi][pj] * sc
    return B

def is_R10_canonical(A: List[List[int]]) -> bool:
    m = len(A)
    n = len(A[0]) if m else 0
    if m != 10 or n != 10:
        return False
    for i in range(10):
        if sum(1 for x in A[i] if x != 0) != 3:
            return False
    for j in range(10):
        if sum(1 for i in range(10) if A[i][j] != 0) != 3:
            return False
    return True

def verify_sum1(parent, child1, child2, rows1, cols1, rows2, cols2, parent_rows, parent_cols):
    if parent_rows != rows1 + rows2:
        die("sum1 row order mismatch")
    if parent_cols != cols1 + cols2:
        die("sum1 col order mismatch")
    if not eq_matrix(parent, block_diag(child1, child2)):
        die("sum1 structure mismatch")

def verify_node(A_full, node):
    kind = node.get("kind")
    rows, cols = extract_rows_cols(node)
    parent = submatrix(A_full, rows, cols)

    if kind == "network":
        verify_network_incidence(parent, node["network_witness"])
        return parent

    if kind == "R10":
        wit = node["R10_witness"]
        B = apply_signed_perm_matrix(parent, wit["perm_rows"], wit["perm_cols"], wit["sign_rows"], wit["sign_cols"])
        if not is_R10_canonical(B):
            die("R10 normalization failed")
        return parent

    if kind == "transpose":
        child = node["children"][0]
        child_mat = verify_node(A_full, child)
        trans = [list(x) for x in zip(*child_mat)]
        if not eq_matrix(parent, trans):
            die("transpose mismatch")
        return parent

    if kind == "sum1":
        left, right = node["children"]
        L = verify_node(A_full, left)
        R = verify_node(A_full, right)
        rowsL, colsL = extract_rows_cols(left)
        rowsR, colsR = extract_rows_cols(right)
        verify_sum1(parent, L, R, rowsL, colsL, rowsR, colsR, rows, cols)
        return parent

    return parent

def main():
    if len(sys.argv) != 2:
        die("usage: tu_seymour_verify.py CERT.json")
    cert = load_json(sys.argv[1])
    M = cert["matrix"]
    A_full = mat_from_flat(M["m"], M["n"], M["entries"])
    verify_node(A_full, cert["root"])
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
