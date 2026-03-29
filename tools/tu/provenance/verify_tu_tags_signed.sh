#!/usr/bin/env bash
set -euo pipefail

TAGS=(
  urf-tu-tvduality-main-v1
  urf-tu-tests-green-v1
  urf-tu-ci-nightly-v1
  urf-tu-stack-release-v1
  urf-tu-stack-signed-v1
  urf-tu-stack-freeze-v1
  urf-tu-stack-attested-v1
  urf-tu-stack-provenance-v1
)

ALLOWLIST="tools/tu/provenance/ALLOWED_TAG_KEYS.txt"
test -f "$ALLOWLIST" || { echo "ERROR: missing $ALLOWLIST"; exit 1; }

git fetch --tags --force

fail=0
for t in "${TAGS[@]}"; do
  echo "== verify tag: $t =="
  if command -v gitsign >/dev/null 2>&1; then
    gitsign verify-tag "$t" || { echo "ERROR: gitsign verify-tag failed: $t"; fail=1; continue; }
    continue
  fi

  out="$(git tag -v "$t" 2>&1 || true)"
  echo "$out"
  echo "$out" | grep -q "Good signature" || { echo "ERROR: bad or missing signature: $t"; fail=1; continue; }

  fp="$(echo "$out" | sed -n 's/^Primary key fingerprint: //p' | tr -d ' ')"
  test -n "$fp" || { echo "ERROR: cannot parse fingerprint: $t"; fail=1; continue; }
  grep -q "^${fp}$" "$ALLOWLIST" || { echo "ERROR: fingerprint not allowlisted: $fp"; fail=1; continue; }
done

test "$fail" -eq 0
echo "OK: all TU tags verified and allowlisted"
