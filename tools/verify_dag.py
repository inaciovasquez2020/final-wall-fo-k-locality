#!/usr/bin/env python3
import json, sys, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAG = ROOT / "meta" / "dag.json"
SHA = ROOT / "meta" / "dag.sha256"
SCHEMA = ROOT / "meta" / "dag.schema.json"

def load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def check_hash():
    if not SHA.exists():
        print("WARN: meta/dag.sha256 missing; run tools/compile_dag.py", file=sys.stderr)
        return True
    line = SHA.read_text(encoding="utf-8").strip()
    want = line.split()[0]
    got = hashlib.sha256(DAG.read_bytes()).hexdigest()
    if want != got:
        print(f"FAIL hash mismatch: want {want} got {got}", file=sys.stderr)
        return False
    return True

# --- minimal JSON-schema-like validator (subset) ---
def require_keys(obj, keys, ctx):
    ok = True
    for k in keys:
        if k not in obj:
            print(f"FAIL missing key '{k}' in {ctx}", file=sys.stderr)
            ok = False
    return ok

def is_type(x, tname):
    if tname == "string":
        return isinstance(x, str)
    if tname == "object":
        return isinstance(x, dict)
    if tname == "array":
        return isinstance(x, list)
    return True

def validate_node(node):
    ok = True
    ok &= require_keys(node, ["id", "title", "type", "status"], "node")
    for k in ["id", "title", "type", "status"]:
        if k in node and not isinstance(node[k], str):
            print(f"FAIL node.{k} must be string", file=sys.stderr)
            ok = False
    if "tags" in node and not isinstance(node["tags"], list):
        print("FAIL node.tags must be array", file=sys.stderr); ok = False
    if "locations" in node:
        if not isinstance(node["locations"], list):
            print("FAIL node.locations must be array", file=sys.stderr); ok = False
        else:
            for loc in node["locations"]:
                if not isinstance(loc, dict):
                    print("FAIL location must be object", file=sys.stderr); ok = False; continue
                ok &= require_keys(loc, ["repo", "path"], "location")
                if "repo" in loc and not isinstance(loc["repo"], str):
                    print("FAIL location.repo must be string", file=sys.stderr); ok = False
                if "path" in loc and not isinstance(loc["path"], str):
                    print("FAIL location.path must be string", file=sys.stderr); ok = False
    return ok

def validate_edge(edge):
    ok = True
    ok &= require_keys(edge, ["from", "to", "kind"], "edge")
    for k in ["from", "to", "kind"]:
        if k in edge and not isinstance(edge[k], str):
            print(f"FAIL edge.{k} must be string", file=sys.stderr); ok = False
    if "note" in edge and not isinstance(edge["note"], str):
        print("FAIL edge.note must be string", file=sys.stderr); ok = False
    return ok

def schema_validate(dag):
    # Validate dag structure against meta/dag.schema.json (subset, no external deps).
    ok = True
    if SCHEMA.exists():
        schema = load_json(SCHEMA)
        ok &= require_keys(dag, schema.get("required_top_level", []), "dag")
    else:
        ok &= require_keys(dag, ["version", "nodes", "edges", "build"], "dag")

    if "nodes" in dag and not isinstance(dag["nodes"], list):
        print("FAIL dag.nodes must be array", file=sys.stderr); ok = False
    if "edges" in dag and not isinstance(dag["edges"], list):
        print("FAIL dag.edges must be array", file=sys.stderr); ok = False
    if "build" in dag and not isinstance(dag["build"], dict):
        print("FAIL dag.build must be object", file=sys.stderr); ok = False

    if isinstance(dag.get("nodes"), list):
        for n in dag["nodes"]:
            if not isinstance(n, dict):
                print("FAIL node must be object", file=sys.stderr); ok = False
            else:
                ok &= validate_node(n)

    if isinstance(dag.get("edges"), list):
        for e in dag["edges"]:
            if not isinstance(e, dict):
                print("FAIL edge must be object", file=sys.stderr); ok = False
            else:
                ok &= validate_edge(e)

    if isinstance(dag.get("build"), dict):
        ok &= require_keys(dag["build"], ["timestamp", "inputs"], "build")
        if "timestamp" in dag["build"] and not isinstance(dag["build"]["timestamp"], str):
            print("FAIL build.timestamp must be string", file=sys.stderr); ok = False
        if "inputs" in dag["build"] and not isinstance(dag["build"]["inputs"], list):
            print("FAIL build.inputs must be array", file=sys.stderr); ok = False
    return ok

def acyclic_uses(edges):
    uses = [(e["from"], e["to"]) for e in edges if e.get("kind") == "uses"]
    nodes = set()
    for a,b in uses:
        nodes.add(a); nodes.add(b)
    indeg = {v: 0 for v in nodes}
    adj = {v: [] for v in nodes}
    for a,b in uses:
        if a == b:
            print(f"FAIL self-loop uses edge: {a}->{b}", file=sys.stderr)
            return False
        adj[a].append(b)
        indeg[b] += 1
    q = [v for v,d in indeg.items() if d == 0]
    out = 0
    while q:
        v = q.pop()
        out += 1
        for w in adj[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)
    if out != len(nodes):
        print("FAIL cycle detected in kind=uses subgraph", file=sys.stderr)
        return False
    return True

def ids_exist(nodes, edges):
    ids = {n.get("id") for n in nodes}
    ok = True
    for e in edges:
        a = e.get("from"); b = e.get("to")
        if a not in ids:
            print(f"FAIL missing node id for edge.from: {a}", file=sys.stderr); ok = False
        if b not in ids:
            print(f"FAIL missing node id for edge.to: {b}", file=sys.stderr); ok = False
    return ok

def main():
    if not DAG.exists():
        print("FAIL meta/dag.json missing; run tools/compile_dag.py", file=sys.stderr)
        sys.exit(2)
    dag = load_json(DAG)
    nodes = dag.get("nodes", [])
    edges = dag.get("edges", [])

    ok = True
    ok &= check_hash()
    ok &= schema_validate(dag)
    ok &= ids_exist(nodes, edges)
    ok &= acyclic_uses(edges)

    if ok:
        print("OK dag verified")
        sys.exit(0)
    sys.exit(1)

if __name__ == "__main__":
    main()
