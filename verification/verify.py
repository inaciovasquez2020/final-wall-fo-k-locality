import json
import math
import re
from pathlib import Path

from jsonschema import validate

SCHEMA_PATH = Path("standards/URF-SG/schema.json")

def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def parse_exact(expr: str) -> float:
    s = expr.strip().lower().replace("^", "**")
    # allow only numbers, operators, parentheses, whitespace, and 'pi'
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

def verify_closed_form(cert: dict) -> None:
    geom = cert["instance"]["geometry"]["name"]
    lb = read_lower_bound(cert)

    if geom in ("T^2", "T2"):
        target = (2 * math.pi) ** 2
        if abs(lb - target) > 1e-12:
            raise AssertionError(f"T^2 gap mismatch: {lb} vs {target}")

    if geom in ("T^2_L", "T2_L"):
        periods = cert["instance"]["geometry"].get("periods", None)
        if not periods or len(periods) < 1:
            raise AssertionError("T^2_L requires geometry.periods with L as first entry")
        L = float(periods[0])
        target = (2 * math.pi / L) ** 2
        if abs(lb - target) > 1e-12:
            raise AssertionError(f"T^2_L gap mismatch: {lb} vs {target}")

def verify_numeric(cert: dict) -> None:
    lb = read_lower_bound(cert)
    if lb <= 0:
        raise AssertionError("Numeric lower bound must be positive")

def verify_cert(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        cert = json.load(f)

    schema = load_schema()
    validate(instance=cert, schema=schema)

    method = cert["checks"]["method"]
    if method == "closed_form":
        verify_closed_form(cert)
    elif method == "numeric":
        verify_numeric(cert)
    else:
        raise ValueError(f"Unknown method: {method}")

    print(f"[OK] {cert['cert_id']}  ({path})")

def main(argv):
    if len(argv) < 2:
        raise SystemExit("Usage: python verification/verify.py <cert.json> [more.json...]")
    for p in argv[1:]:
        verify_cert(p)

if __name__ == "__main__":
    import sys
    main(sys.argv)
