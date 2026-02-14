#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

test -f CHECKSUMS.txt

set +e
grep -vE '^(README.md|CITATION.cff|CHECKSUMS.txt)$' CHECKSUMS.txt \
  | sha256sum --ignore-missing -c - \
  | tee /tmp/checksum.log
rc=${PIPESTATUS[1]}
set -e

grep -q 'FAILED' /tmp/checksum.log && exit 1
exit 0
