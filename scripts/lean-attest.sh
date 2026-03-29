#!/usr/bin/env bash
set -euo pipefail

commit="$(git rev-parse HEAD)"
tree="$(git rev-parse HEAD^{tree})"

leanv="unknown"
if command -v lake >/dev/null 2>&1; then
  leanv="$(lake env lean --version 2>/dev/null | head -n 1 || true)"
fi

lm_hash="absent"
if [ -f lake-manifest.json ]; then
  lm_hash="$(shasum -a 256 lake-manifest.json | awk '{print $1}')"
fi

mkdir -p lean-attest
cat > lean-attest/LEAN_BUILD_ATTEST.txt <<EOT
commit: $commit
tree: $tree
lake_manifest_sha256: $lm_hash
lean_version: $leanv
EOT

shasum -a 256 lean-attest/LEAN_BUILD_ATTEST.txt | awk '{print $1}' > lean-attest/LEAN_BUILD_ATTEST.sha256
