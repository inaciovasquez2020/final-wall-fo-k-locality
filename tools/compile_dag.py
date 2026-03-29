#!/usr/bin/env python3
import json, hashlib, sys
from pathlib import Path
try:
    import yaml
except Exception:
    print("ERROR: missing PyYAML. Run: python3 -m pip install -r tools/requirements.txt", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parents[1]
LEM = ROOT / "meta" / "lemmas.yaml"
DEP = ROOT / "meta" / "deps.yaml"
OUT = ROOT / "meta" / "dag.json"
OUT_SHA = ROOT / "meta" / "dag.sha256"

def sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256(); h.update(b); return h.hexdigest()

def load_yaml(p: Path):
    return yaml.safe_load(p.read_text(encoding="utf-8"))

def main():
    lem = load_yaml(LEM)
    dep = load_yaml(DEP)
    dag = {
        "version": 1,
        "nodes": lem.get("lemmas", []),
        "edges": dep.get("edges", []),
        "build": {
            "timestamp": "DETERMINISTIC",
            "inputs": ["meta/lemmas.yaml", "meta/deps.yaml"],
            "tool": "tools/compile_dag.py"
        }
    }
    data = json.dumps(dag, indent=2, sort_keys=True).encode("utf-8")
    OUT.write_bytes(data)
    OUT_SHA.write_text(f"{sha256_bytes(data)}  meta/dag.json\n", encoding="utf-8")
    print(f"Wrote {OUT} and {OUT_SHA}")

if __name__ == "__main__":
    main()
