#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
from typing import List, Dict, Any, Tuple

HELP_TEXT = """
TU Seymour Deterministic Verifier

Usage
  tu_seymour_verify.py CERT.json

Description
  Verifies Seymour style Totally Unimodular decomposition certificates.

Exit Codes
  0 verification success
  nonzero verification failure

Output
  VERIFY_OK on success
  VERIFY_FAIL message on failure
"""

def die(msg: str) -> None:
    raise SystemExit(f"VERIFY_FAIL: {msg}")

def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def mat_from_flat(m: int, n: int, entries: List[int]) -> List[List[int]]:
    if len(entries) != m * n:
        die("matrix size mismatch")
    A = []
    k = 0
    for _ in range(m):
        row = []
        for _ in range(n):
            v = entries[k]
            if v not in (-1, 0, 1):
                die("matrix entry must be -1 0 or 1")
            row.append(v)
            k += 1
        A.append(row)
    return A

def submatrix(A: List[List[int]], rows: List[int], cols: List[int]) -> List[List[int]]:
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
    rows = node["A"]["rows"]
    cols = node["A"]["cols"]
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
        die("row_to_vertex mismatch")
    if len(col_to_edge) != n:
        die("col_to_edge mismatch")

    for j in range(n):
        e = col_to_edge[j]
        t = tail[e]
        h = head[e]
        pos = []
        neg = []
        for i in range(m):
            v = row_to_vertex[i]
            a = A[i][j]
            if a == 1:
                pos.append(v)
            elif a == -1:
                neg.append(v)
            elif a != 0:
                die("invalid entry")
        if len(pos) != 1 or len(neg) != 1:
            die("network column must have one +1 and one -1")
        if not ((neg[0] == t and pos[0] == h) or (neg[0] == h and pos[0] == t)):
            die("network sign mismatch")

def apply_signed_perm_matrix(A, pr, pc, sr, sc):
    m = len(A)
    n = len(A[0]) if m else 0
    B = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            B[i][j] = sr[i] * A[pr[i]][pc[j]] * sc[j]
    return B

def is_R10_canonical(A):
    if len(A) != 10 or len(A[0]) != 10:
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
        die("sum1 row mismatch")
    if parent_cols != cols1 + cols2:
        die("sum1 col mismatch")
    if not eq_matrix(parent, block_diag(child1, child2)):
        die("sum1 structure mismatch")

def verify_sumk_glue(parent, child1, child2, rows1, cols1, rows2, cols2,
                     glue_rows, glue_cols, parent_rows, parent_cols, k):
    if len(glue_rows) != k or len(glue_cols) != k:
        die("glue size mismatch")

    Srows1, Srows2 = set(rows1), set(rows2)
    Scols1, Scols2 = set(cols1), set(cols2)

    if set(glue_rows) != (Srows1 & Srows2):
        die("row glue mismatch")
    if set(glue_cols) != (Scols1 & Scols2):
        die("col glue mismatch")

    idx_r = {r: i for i, r in enumerate(parent_rows)}
    idx_c = {c: j for j, c in enumerate(parent_cols)}

    P = zeros_like(len(parent_rows), len(parent_cols))

    for i_r, r in enumerate(rows1):
        for j_c, c in enumerate(cols1):
            P[idx_r[r]][idx_c[c]] = child1[i_r][j_c]

    for i_r, r in enumerate(rows2):
        for j_c, c in enumerate(cols2):
            v = child2[i_r][j_c]
            cur = P[idx_r[r]][idx_c[c]]
            if cur != 0 and v != 0 and cur != v:
                die("overlap mismatch")
            if cur == 0:
                P[idx_r[r]][idx_c[c]] = v

    if not eq_matrix(parent, P):
        die("sumk structure mismatch")

def verify_node(A_full, node):
    kind = node["kind"]
    rows, cols = extract_rows_cols(node)
    parent = submatrix(A_full, rows, cols)

    if kind == "network":
        verify_network_incidence(parent, node["network_witness"])
        return parent

    if kind == "R10":
        wit = node["R10_witness"]
        B = apply_signed_perm_matrix(parent, wit["perm_rows"], wit["perm_cols"],
                                     wit["sign_rows"], wit["sign_cols"])
        if not is_R10_canonical(B):
            die("R10 normalization failed")
        return parent

    if kind == "transpose":
        child = node["children"][0]
        child_mat = verify_node(A_full, child)
        return parent

    left, right = node["children"]
    L = verify_node(A_full, left)
    R = verify_node(A_full, right)
    rowsL, colsL = extract_rows_cols(left)
    rowsR, colsR = extract_rows_cols(right)

    if kind == "sum1":
        verify_sum1(parent, L, R, rowsL, colsL, rowsR, colsR, rows, cols)
        return parent

    bd = node["sum_boundary"]
    glue_rows = bd["glue_rows"]
    glue_cols = bd["glue_cols"]

    if kind == "sum2":
        verify_sumk_glue(parent, L, R, rowsL, colsL, rowsR, colsR,
                         glue_rows, glue_cols, rows, cols, 1)
        return parent

    if kind == "sum3":
        verify_sumk_glue(parent, L, R, rowsL, colsL, rowsR, colsR,
                         glue_rows, glue_cols, rows, cols, 3)
        return parent

    die("unknown kind")

def main():
    if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
        print(HELP_TEXT.strip())
        return

    if len(sys.argv) != 2:
        die("usage tu_seymour_verify.py CERT.json")

    cert = load_json(sys.argv[1])
    M = cert["matrix"]
    A_full = mat_from_flat(M["m"], M["n"], M["entries"])
    verify_node(A_full, cert["root"])
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
