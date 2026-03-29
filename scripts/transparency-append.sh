#!/usr/bin/env bash
set -euo pipefail
tag="${1:?usage: $0 <tag>}"

./scripts/build-merkle.sh

commit="$(git rev-parse HEAD)"
root="$(cat transparency/merkle.root)"
ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

entry="transparency/log/${tag}.entry"
cat > "$entry" <<EOT
tag: $tag
commit: $commit
utc: $ts
merkle_root_sha256: $root
manifest_path: transparency/files.sha256
EOT

git add transparency/files.sha256 transparency/merkle.root "$entry"
git commit -m "transparency: log $tag (merkle root + manifest)"
