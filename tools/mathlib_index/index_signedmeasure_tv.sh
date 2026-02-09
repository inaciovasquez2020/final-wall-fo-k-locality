#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.lake/packages/mathlib/Mathlib}"
OUT="${2:-docs/mathlib/SIGNEDMEASURE_TV_LEMMAS.txt}"

if [ ! -d "$ROOT" ]; then
  echo "ERROR: mathlib root not found: $ROOT" 1>&2
  exit 2
fi

TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

{
  echo "Mathlib SignedMeasure totalVariation lemma index"
  echo "Generated at: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "Mathlib root: $ROOT"
  echo

  echo "Targets"
  echo "1 Hahn decomposition: exists_isCompl_positive_negative"
  echo "2 totalVariation definition and properties"
  echo "3 integral bounds involving totalVariation"
  echo "4 indicator formulations for Jordan/Hahn sets"
  echo

  echo "Matches: exists_isCompl_positive_negative"
  rg -n "exists_isCompl_positive_negative" "$ROOT" || true
  echo

  echo "Matches: totalVariation definition"
  rg -n "def totalVariation \\(s : SignedMeasure" "$ROOT" || true
  echo

  echo "Matches: totalVariation theorems"
  rg -n "theorem .*totalVariation" "$ROOT" || true
  echo

  echo "Matches: integral and totalVariation in same lemma"
  rg -n "theorem .*integral.*totalVariation|theorem .*totalVariation.*integral" "$ROOT" || true
  echo

  echo "Matches: abs and integral for SignedMeasure"
  rg -n "SignedMeasure.*abs.*integral|abs.*integral.*SignedMeasure" "$ROOT" || true
  echo

  echo "Matches: Jordan decomposition API"
  rg -n "toJordanDecomposition|jordanDecomposition|toMeasureOfZeroLE" "$ROOT" || true
  echo
} > "$TMP"

mkdir -p "$(dirname "$OUT")"
mv "$TMP" "$OUT"
echo "WROTE $OUT"
