from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from locality_boundary_certificate import missing_required_paths, locality_boundary_certificate


BOUNDARY = """
No repository-level claim of universal FO^k locality completeness.
No repository-level claim that finite locality closure implies external validation.
No repository-level claim of peer-reviewed acceptance unless explicitly documented.
No repository-level claim that finite locality-boundary closure equals theorem-level completion.
"""


def test_missing_required_paths_detects_absence() -> None:
    missing = missing_required_paths(ROOT, ["docs/status/LOCALITY_BOUNDARY_CERTIFICATE.md", "definitely_missing.file"])
    assert "definitely_missing.file" in missing


def test_locality_boundary_certificate_passes_for_manifest() -> None:
    cert = locality_boundary_certificate(
        ROOT,
        [
            "docs/status/LOCALITY_BOUNDARY_CERTIFICATE.md",
            "scripts/verify_locality_boundary_certificate.py",
            "src/locality_boundary_certificate.py",
            "tests/test_locality_boundary_certificate.py",
        ],
        BOUNDARY,
    )
    assert cert.theorem_id == "FWFK-LBC-1"
    assert cert.status == "PASS"
    assert cert.required_count == 4
    assert cert.present_count == 4
    assert cert.missing == ()
    assert cert.all_required_present is True
    assert cert.boundary_declared is True


def test_locality_boundary_certificate_fails_without_boundary() -> None:
    cert = locality_boundary_certificate(ROOT, ["docs/status/LOCALITY_BOUNDARY_CERTIFICATE.md"], "")
    assert cert.status == "FAIL"
    assert cert.boundary_declared is False


def test_repository_scope_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/verify_locality_boundary_certificate.py"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    assert '"theorem_id": "FWFK-LBC-1"' in result.stdout
    assert '"status": "PASS"' in result.stdout


def test_nonclaim_boundary_retained() -> None:
    text = (ROOT / "docs/status/LOCALITY_BOUNDARY_CERTIFICATE.md").read_text(encoding="utf-8")
    assert "No repository-level claim of universal FO^k locality completeness." in text
    assert "No repository-level claim that finite locality closure implies external validation." in text
    assert "No repository-level claim of peer-reviewed acceptance unless explicitly documented." in text
    assert "No repository-level claim that finite locality-boundary closure equals theorem-level completion." in text
