#!/usr/bin/env python3
import json, hashlib, datetime, sys
from pathlib import Path

try:
    import yaml
except Exception as e:
    print("ERROR: missing PyYAML. Run: python3 -m pip install -r tools/requirements.txt", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parents[1]
LEM = ROOT / "meta" / "lemmas.yaml"
DEP = ROOT / "meta" / "deps.yaml"
OUT = ROOT / "meta" / "dag.json"
OUT_SHA = ROOT / "meta" / "dag.sha256"

def load_yaml(p: Path):
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256()
    h.update(b)
    return h.hexdigest()

def main():
    lem = load_yaml(LEM)
    dep = load_yaml(DEP)

    nodes = lem.get("lemmas", [])
    edges = dep.get("edges", [])

    dag = {
        "version": 1,
        "nodes": nodes,
        "edges": edges,
        "build": {
            "timestamp": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
            "inputs": ["meta/lemmas.yaml", "meta/deps.yaml"],
            "tool": "tools/compile_dag.py"
        }
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(dag, indent=2, sort_keys=True).encode("utf-8")
    OUT.write_bytes(data)

    digest = sha256_bytes(data)
    OUT_SHA.write_text(f"{digest}  meta/dag.json\n", encoding="utf-8")
    print(f"Wrote {OUT} and {OUT_SHA}")

if __name__ == "__main__":
    main()
