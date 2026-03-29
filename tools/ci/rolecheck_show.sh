#!/usr/bin/env bash
set -euo pipefail
python3 tools/rolecheck/rolecheck.py core || true
