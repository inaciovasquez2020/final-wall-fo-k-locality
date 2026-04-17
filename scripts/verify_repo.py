#!/usr/bin/env python3
from pathlib import Path
import sys

required = [
    "README.md",
    "CITATION.cff",
    "FREEZE.md",
    "STATUS.md",
    "ARCHIVE.md",
    "Oblivion_Final_Wall.tex",
    "Oblivion_Final_Wall_Appendix_FO4.tex",
    "Oblivion_Final_Wall_FO4_Appendix.tex",
    "docs",
    "infra",
    "operator-theory",
]

missing = [p for p in required if not Path(p).exists()]
if missing:
    print({"valid": False, "missing": missing})
    sys.exit(1)

readme = Path("README.md").read_text(errors="ignore").lower()

checks = {
    "mentions_final_wall": "final wall" in readme,
    "mentions_fo_k_locality": "fo^k locality" in readme or "foᵏ locality" in readme or "fo k locality" in readme,
    "mentions_frozen_or_terminal": "frozen" in readme or "terminal" in readme,
    "mentions_no_executable_lean": "no executable lean code lives here by design" in readme,
}

failed = [k for k, v in checks.items() if not v]
if failed:
    print({"valid": False, "failed_checks": failed, "checks": checks})
    sys.exit(1)

print({"valid": True, "checked": required, "checks": checks})
