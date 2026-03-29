#!/usr/bin/env bash
set -euo pipefail

# Compare urf-core (this repo) vs flagship-lean (sibling path under ~/github-audit)
BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SIBLING_DIR="$(cd "$BASE_DIR/../flagship-lean" && pwd)"

FILES=(
  meta/dag.schema.json
  meta/lemmas.schema.yaml
  meta/deps.schema.yaml
  meta/constants.schema.yaml
  meta/regime.schema.yaml
  meta/tlg_instances.schema.yaml
  tools/compile_dag.py
  tools/verify_dag.py
  tools/verify_manifest.py
)

for f in "${FILES[@]}"; do
  a="$BASE_DIR/$f"
  b="$SIBLING_DIR/$f"
  if [[ ! -f "$a" ]]; then echo "FAIL missing in urf-core: $f" >&2; exit 2; fi
  if [[ ! -f "$b" ]]; then echo "FAIL missing in flagship-lean: $f" >&2; exit 2; fi
  if ! diff -q "$a" "$b" >/dev/null; then
    echo "FAIL schema/tool mismatch: $f" >&2
    exit 1
  fi
done

echo "OK cross-repo schema/tool match (urf-core == flagship-lean)"
