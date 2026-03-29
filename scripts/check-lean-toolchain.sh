#!/usr/bin/env bash
set -euo pipefail

if [ ! -f "lean-toolchain" ]; then
  echo "FAIL missing lean-toolchain file"
  exit 1
fi

echo "Lean toolchain:"
cat lean-toolchain

echo "PASS lean toolchain check"
