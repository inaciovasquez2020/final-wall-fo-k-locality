#!/usr/bin/env python3
import json, subprocess, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
P = ROOT / "PROVENANCE.json"

def sh(c): return subprocess.check_output(c, cwd=ROOT).decode().strip()

data = json.loads(P.read_text())
parent = sh(["git","rev-parse","HEAD^"])

if data["commit"] != parent:
    print("ERROR provenance mismatch", file=sys.stderr)
    sys.exit(1)

print("OK provenance stable")
