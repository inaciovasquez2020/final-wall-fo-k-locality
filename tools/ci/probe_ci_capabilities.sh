#!/usr/bin/env bash
set -euo pipefail

HAS_CACHE=false
if lake exe --help 2>/dev/null | grep -qE '(^|[[:space:]])cache([[:space:]]|$)'; then
  HAS_CACHE=true
fi

cat > ci-capabilities.json <<JSON
{"has_cache_exec":$HAS_CACHE}
JSON

cat ci-capabilities.json
