#!/usr/bin/env bash
set -euo pipefail

EXPECTED="$(cat lean-toolchain)"
ACTUAL="$(lean --version | head -n1)"

echo "EXPECTED=$EXPECTED"
echo "ACTUAL=$ACTUAL"
