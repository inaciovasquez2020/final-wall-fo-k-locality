#!/usr/bin/env python3
import subprocess
import sys

ROLE = sys.argv[1] if len(sys.argv) > 1 else "core"

FORBIDDEN_SUBSTRINGS = [
    "/.lake/",
    "\\.lake\\",
    ".lake/",
    ".lake\\",
    "ProofWidgets4.tar.gz",
]

def git_tracked_files():
    out = subprocess.check_output(["git", "ls-files"], text=True)
    return [line.strip() for line in out.splitlines() if line.strip()]

def rolecheck_core():
    tracked = git_tracked_files()
    bad = []
    for f in tracked:
        for rule in FORBIDDEN_SUBSTRINGS:
            if rule in f:
                bad.append(f)
                break
    if bad:
        print(f"ROLECHECK_FAIL: forbidden tracked files for role=core: {bad}")
        sys.exit(1)
    print("ROLECHECK_OK")

if ROLE == "core":
    rolecheck_core()
else:
    print("ROLECHECK_OK (non-core role)")
