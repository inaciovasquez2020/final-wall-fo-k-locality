#!/usr/bin/env bash
set -euo pipefail

FORBIDDEN=("ip/" "workspace/" "scratch/" "\.pem$" "\.key$")

FILES="$(git ls-files)"

for f in "${FORBIDDEN[@]}"; do
  if echo "$FILES" | grep -E -q "(^|/)$f"; then
    echo "FAIL forbidden content tracked: $f"
    exit 1
  fi
done

echo "PASS hygiene"
