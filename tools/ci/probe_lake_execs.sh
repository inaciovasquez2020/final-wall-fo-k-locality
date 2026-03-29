#!/usr/bin/env bash
set -euo pipefail

mkdir -p build

# capture executables help
lake exe --help > build/lake-exe-help.txt 2>/dev/null || true

# witness HasExec(cache)
if grep -Eq '(^|[[:space:]])cache([[:space:]]|$)' build/lake-exe-help.txt; then
  HAS_CACHE=true
else
  HAS_CACHE=false
fi

# encode capabilities
jq -n --argjson has_cache "$HAS_CACHE" '{HasExec_cache:$has_cache}' > build/ci-capabilities.json

# hash for audit
sha256sum build/lake-exe-help.txt | awk '{print $1}' > build/lake-exe-help.sha256

echo "HasExec(cache)=${HAS_CACHE}"
