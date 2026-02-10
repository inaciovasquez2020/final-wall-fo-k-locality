#!/usr/bin/env bash
set -euo pipefail

test -f ci-artifacts/env.sha256

mkdir -p transparency/log
TS="$(date -u +%Y%m%dT%H%M%SZ)"
ENTRY="transparency/log/CI_ENV_${TS}.entry"

SHA="$(cat ci-artifacts/env.sha256)"
echo "${SHA}  ci-artifacts/env.txt" > "${ENTRY}"

python3 tools/update_manifest.sh
