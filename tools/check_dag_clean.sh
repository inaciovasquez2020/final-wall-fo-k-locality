#!/usr/bin/env bash
set -euo pipefail
./tools/compile_dag.py
git diff --exit-code -- meta/dag.json meta/dag.sha256
