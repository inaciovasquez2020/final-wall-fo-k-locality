#!/usr/bin/env python3
from __future__ import annotations
import json
import os
import subprocess
import sys
import hashlib
from pathlib import Path
from dataclasses import dataclass

def die(msg: str) -> None:
  raise SystemExit(f"REFEREE_VERIFY_FAIL: {msg}")

def sh(cmd: list[str]) -> None:
  r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
  if r.returncode != 0:
    sys.stdout.write(r.stdout)
    die("command failed: " + " ".join(cmd))

def sha256_file(path: Path) -> str:
  h = hashlib.sha256()
  with path.open("rb") as f:
    for chunk in iter(lambda: f.read(1024 * 1024), b""):
      h.update(chunk)
  return h.hexdigest()

def list_required() -> list[str]:
  return [
    ".github/workflows/verify-tu-tv.yml",
    "tools/tu/tu_seymour_verify.py",
    "tools/tu/testdata/network_minimal_CERT.json",
    "tools/tv_cert/generate_tv_finite_cert.py",
    "tools/tv_cert/verify_tv_finite_cert.py",
    "tools/tv_step_cert/generate_tv_step_cert.py",
    "tools/tv_step_cert/verify_tv_step_cert.py",
    "meta/deps/DEPENDENCY_GRAPH.json",
    "meta/obstructions/TV_CRI.md",
    "docs/governance/REPO_LATTICE.md"
  ]

def main() -> None:
  root = Path(".").resolve()

  for rel in list_required():
    p = root / rel
    if not p.exists():
      die(f"missing required artifact: {rel}")

  sh(["python3", "tools/tu/tu_seymour_verify.py", "tools/tu/testdata/network_minimal_CERT.json"])
  sh(["python3", "tools/tv_cert/generate_tv_finite_cert.py", "8", "/tmp/tv_finite_n8_CERT.json"])
  sh(["python3", "tools/tv_cert/verify_tv_finite_cert.py", "/tmp/tv_finite_n8_CERT.json"])
  sh(["python3", "tools/tv_step_cert/generate_tv_step_cert.py", "10", "/tmp/tv_step_n10_CERT.json"])
  sh(["python3", "tools/tv_step_cert/verify_tv_step_cert.py", "/tmp/tv_step_n10_CERT.json"])

  run_lean = os.environ.get("URF_REFEREE_RUN_LEAN", "1") == "1"
  if run_lean:
    sh(["lake", "build"])

  artifacts = {}
  for rel in list_required():
    artifacts[rel] = sha256_file(root / rel)

  head = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()

  tuple_path = root / "meta/referee/REFEREE_TUPLE.json"
  payload = {
    "repo": "inaciovasquez2020/urf-core",
    "ref": head,
    "artifacts_sha256": artifacts,
    "ran_lean": run_lean
  }
  tuple_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

  print("VERIFY_OK")

if __name__ == "__main__":
  main()
