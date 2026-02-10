#!/usr/bin/env bash
set -euo pipefail
python3 tools/tu/tu_seymour_verify.py tools/tu/tests/network_minimal_2x1.json
echo ALL_TU_TESTS_PASSED
