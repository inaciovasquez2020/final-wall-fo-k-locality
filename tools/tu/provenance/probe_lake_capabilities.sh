#!/usr/bin/env bash
set -euo pipefail
OUT="tools/tu/provenance/lake_capabilities.json"

if lake exe cache -h >/dev/null 2>&1; then
  HAS_CACHE_EXE=true
else
  HAS_CACHE_EXE=false
fi

python3 - <<PY
import json
json.dump({"has_cache_exe": ${HAS_CACHE_EXE}}, open("${OUT}","w"), indent=2, sort_keys=True)
print()
PY
