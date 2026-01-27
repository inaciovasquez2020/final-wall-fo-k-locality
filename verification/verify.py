#!/usr/bin/env python3
import json
import math
import re
import sys
from pathlib import Path

import numpy as np
from jsonschema import validate

# -------- Paths --------

SCHEMA_PATH = Path("standards/URF-SG/schema.json")

# -------- Utilities --------

def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def parse_exact(expr: str) -> float:
    """
    Parse tiny exact-expression language:
      - numbers, pi
      - +, -, *, /, parentheses
      - exponentiation via ^ or **
    """
    s = expr.strip().lower().replace("^", "**")
    # only allow 'pi' as symbol
    if re.search(r"[a-zA-Z_]", s.replace("pi", "")):
        raise ValueError(f"Illegal symbol in exact expression: {expr}")
    return eval(s, {"__builtins__": {}}, {"pi": math.pi})

def read_lower_bound(cert: dict) -> float:
    st = cert["statement"]
    if "lower_bound_exact" in st:
        return parse_exact(st["lower_bound_exact"])
    if "lower_bound" in st:
        return float(st["lower_bound"])
    raise ValueError("No lower bound provided")

# -------- Closed-form verifiers --------

def verify_closed_form(cert: dict) -> None:
    geom = cert["instance"]["geometry"]["name"]
    lb = read_lower_bound(cert)

    # T^2 exact
    if geom in ("T^2", "T2"):
        target = (2 * math.pi) ** 2
        if abs(lb - target) > 1e-12:
            raise AssertionError(f"T^2 gap mismatch: {lb} vs {target}")

    # T^2_L exact
    if geom in ("T^2_L", "T2_L"):
        periods = cert["instance"]["geometry"].get("periods", None)
        if not periods or len(periods) < 1:
            raise AssertionError("T^2_L requires geometry.periods with L as first entry")
        L = float(periods[0])
        target = (2 * math.pi / L) ** 2
        if abs(lb - target) > 1e-12:
            raise AssertionError(f"T^2_L gap mismatch: {lb} vs {target}")

# -------- Numeric verifiers --------

def verify_numeric(cert: dict) -> None:
    """
    Expects:
      - cert["P"] : square matrix (list of lists)
      - cert["n"] : dimension
      - statement.lower_bound : claimed gap
    """
    lb = read_lower_bound(cert)
    if lb <= 0:
        raise AssertionError("Numeric lower bound must be positive")

    if "P" not in cert:
        raise AssertionError("Numeric certificate requires matrix field 'P'")
    if "n" not in cert:
        raise AssertionError("Numeric certificate requires field 'n'")

    P = np.array(cert["P"], dtype=float)
    n = int(cert["n"])

    if P.shape != (n, n):
        raise AssertionError(f"Matrix dimension mismatch: {P.shape} vs ({n},{n})")

    # Symmetry check (tolerance)
    if not np.allclose(P, P.T, atol=1e-8):
        raise AssertionError("Matrix P is not symmetric")

    # Eigenvalues
    evals = np.linalg.eigvalsh(P)  # real for symmetric
    evals = sorted(abs(e) for e in evals)

    # spectral gap = smallest nonzero eigenvalue
    nonzero = [e for e in evals if e > 1e-8]
    if not nonzero:
        raise AssertionError("No nonzero eigenvalues found")

    gap = nonzero[0]

    if gap + 1e-10 < lb:
        raise AssertionError(f"Spectral gap {gap} < claimed {lb}")

# -------- Main dispatcher --------

def verify_cert(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        cert = json.load(f)

    # schema validation (if present)
    if SCHEMA_PATH.exists():
        schema = load_schema()
        validate(instance=cert, schema=schema)

    method = cert["checks"]["method"]

    if method == "closed_form":
        verify_closed_form(cert)
    elif method == "numeric":
        verify_numeric(cert)
    else:
        raise ValueError(f"Unknown verification method: {method}")

    print(f"[OK] {cert['cert_id']}  ({path})")

def main(argv):
    if len(argv) < 2:
        raise SystemExit("Usage: python verification/verify.py <cert.json> [more.json ...]")
    for p in argv[1:]:
        verify_cert(p)

if __name__ == "__main__":
    main(sys.argv)

