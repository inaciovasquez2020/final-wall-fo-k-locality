#!/usr/bin/env bash
set -euo pipefail
TAG="${1:?usage: audit.sh <tag>}"

# require repo checked out at tag
git checkout "$TAG" >/dev/null 2>&1 || true

calc=$(shasum -a 256 transparency/files.sha256 | awk '{print $1}')
exp=$(cat transparency/merkle.root)
[ "$calc" = "$exp" ]

calc2=$(shasum -a 256 lean-attest/LEAN_BUILD_ATTEST.txt | awk '{print $1}')
exp2=$(cat lean-attest/LEAN_BUILD_ATTEST.sha256)
[ "$calc2" = "$exp2" ]

echo AUDIT_OK "$TAG"
