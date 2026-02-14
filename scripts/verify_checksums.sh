#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"

cd "$ROOT"

if [ ! -f CHECKSUMS.txt ]; then
  echo "ERROR: CHECKSUMS.txt not found"
  exit 1
fi

grep -vE '^(README.md|CITATION.cff)$' CHECKSUMS.txt | sha256sum -c -

