#!/usr/bin/env python3
from __future__ import annotations
import argparse
import os
import sys
from pathlib import Path
from fnmatch import fnmatch

def die(msg: str) -> None:
  raise SystemExit(f"ROLECHECK_FAIL: {msg}")

def iter_files(root: Path) -> list[str]:
  out: list[str] = []
  for p in root.rglob("*"):
    if p.is_file():
      rel = p.relative_to(root).as_posix()
      out.append(rel)
  return out

def match_any(path: str, patterns: list[str]) -> bool:
  for pat in patterns:
    if fnmatch(path, pat):
      return True
  return False

def main() -> None:
  ap = argparse.ArgumentParser()
  ap.add_argument("role", choices=["core", "prefab", "infra", "app"])
  args = ap.parse_args()

  root = Path(".").resolve()
  files = iter_files(root)

  core_forbidden = [
    "dist/*",
    "release/*",
    "prefab_bundle/*",
    "docker/*",
    "*.tar.gz",
    "*.zip"
  ]

  prefab_forbidden = [
    "spine/lean/**",
    "lemmas/**",
    "theorems/**",
    "proofs/**"
  ]

  infra_forbidden = [
    "spine/lean/**"
  ]

  app_forbidden = []

  forb = {
    "core": core_forbidden,
    "prefab": prefab_forbidden,
    "infra": infra_forbidden,
    "app": app_forbidden
  }[args.role]

  bad = [f for f in files if match_any(f, forb)]
  if bad:
    die(f"forbidden files for role={args.role}: {bad[:20]}")

  print("ROLECHECK_OK")

if __name__ == "__main__":
  main()
