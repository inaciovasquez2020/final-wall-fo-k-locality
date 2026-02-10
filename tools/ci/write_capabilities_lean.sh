#!/usr/bin/env bash
set -euo pipefail

HAS="$(jq -r '.has_cache_exec' ci-capabilities.json)"
mkdir -p URFCore/Generated

cat > URFCore/Generated/CICapabilities.lean <<LEAN
namespace URFCore
def hasCacheExec : Bool := $HAS
end URFCore
LEAN
