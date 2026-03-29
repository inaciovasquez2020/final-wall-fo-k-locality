#!/usr/bin/env python3
import sys, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAN = ROOT / "meta" / "MANIFEST.sha256"

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    if not MAN.exists():
        print("FAIL meta/MANIFEST.sha256 missing", file=sys.stderr); return 2
    ok = True
    for line in MAN.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line: continue
        parts = line.split()
        if len(parts) < 2:
            print(f"FAIL bad manifest line: {line}", file=sys.stderr); ok = False; continue
        want = parts[0]; rel = parts[-1]
        p = (ROOT / rel).resolve()
        if not p.exists():
            print(f"FAIL missing file in manifest: {rel}", file=sys.stderr); ok = False; continue
        got = sha256_file(p)
        if got != want:
            print(f"FAIL hash mismatch: {rel}\n  want {want}\n  got  {got}", file=sys.stderr); ok = False
    if ok:
        print("OK manifest verified"); return 0
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
