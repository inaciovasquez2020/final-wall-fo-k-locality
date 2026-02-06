#!/usr/bin/env bash
set -euo pipefail

EXPECTED="$(cat .lake/packages/mathlib/lean-toolchain)"
ACTUAL="$(cat lean-toolchain)"

if [ "$EXPECTED" != "$ACTUAL" ]; then
  echo "Lean toolchain mismatch detected"
  echo "Expected (mathlib): $EXPECTED"
  echo "Actual (project):  $ACTUAL"
  echo ""
  echo "Fix by running:"
  echo "cp .lake/packages/mathlib/lean-toolchain ./lean-toolchain"
  exit 1
fi

echo "Lean toolchain matches mathlib"
