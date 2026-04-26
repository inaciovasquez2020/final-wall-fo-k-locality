#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from locality_boundary_certificate import locality_boundary_certificate


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    doc = ROOT / "docs/status/LOCALITY_BOUNDARY_CERTIFICATE.md"
    source = ROOT / "src/locality_boundary_certificate.py"
    status = ROOT / "STATUS.md"
    if not status.exists():
        status = ROOT / "README.md"
    require(doc.exists(), "missing locality boundary certificate doc")
    require(source.exists(), "missing certificate source")
    require(status.exists(), "missing status/readme boundary source")
    boundary_text = doc.read_text(encoding="utf-8") + "\n" + status.read_text(encoding="utf-8")
    cert = locality_boundary_certificate(
        ROOT,
        [
            "docs/status/LOCALITY_BOUNDARY_CERTIFICATE.md",
            "scripts/verify_locality_boundary_certificate.py",
            "src/locality_boundary_certificate.py",
            "tests/test_locality_boundary_certificate.py",
        ],
        boundary_text,
    )
    require(cert.theorem_id == "FWFK-LBC-1", "wrong theorem id")
    require(cert.status == "PASS", f"certificate failed: {cert}")
    require(cert.all_required_present, "required manifest is incomplete")
    require(cert.boundary_declared, "locality boundary missing")
    doc_text = doc.read_text(encoding="utf-8")
    for literal in [
        "Status: CLOSED repository-scope certificate.",
        "Theorem ID: FWFK-LBC-1.",
        "No repository-level claim of universal FO^k locality completeness.",
        "No repository-level claim that finite locality closure implies external validation.",
        "No repository-level claim of peer-reviewed acceptance unless explicitly documented.",
        "No repository-level claim that finite locality-boundary closure equals theorem-level completion.",
    ]:
        require(literal in doc_text, f"missing doc literal: {literal}")
    print(json.dumps(cert.__dict__, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
