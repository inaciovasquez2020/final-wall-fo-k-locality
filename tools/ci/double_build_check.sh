#!/usr/bin/env bash
set -euo pipefail

echo "[1/2] clean + build"
rm -rf .lake/build
lake build
R1="$(bash tools/ci/build_root.sh)"

echo "[2/2] clean + build"
rm -rf .lake/build
lake build
R2="$(bash tools/ci/build_root.sh)"

echo "R1=$R1"
echo "R2=$R2"
test "$R1" = "$R2"
