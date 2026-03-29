#!/usr/bin/env bash
set -euo pipefail
tag="${1:?usage: $0 <tag>}"
out="verify/offline/urf-core_${tag}_offline_bundle"
rm -rf "$out"
mkdir -p "$out"

cp -v transparency/files.sha256 transparency/merkle.root "$out"/
cp -v "transparency/log/${tag}.entry" "$out"/
cp -v "tuple/TUPLE_${tag}.txt" tuple/ARTIFACTS.sha256 "$out"/
cp -v sigstore/image.digest sigstore/cosign.bundle.json "$out"/
cp -v lean-attest/LEAN_BUILD_ATTEST.txt lean-attest/LEAN_BUILD_ATTEST.sha256 "$out"/
cp -v verify/offline/VERIFY_OFFLINE.md "$out"/

tar -czf "${out}.tar.gz" -C verify/offline "urf-core_${tag}_offline_bundle"
echo "Wrote ${out}.tar.gz"
