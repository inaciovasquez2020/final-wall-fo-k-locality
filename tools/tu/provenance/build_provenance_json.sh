#!/usr/bin/env bash
set -euo pipefail

OUT="PROVENANCE.json"

COMMIT="$(git rev-parse HEAD)"
TOOLCHAIN="$(cat lean-toolchain 2>/dev/null || echo "")"
MERKLE_ROOT="$(cat manifest/merkle.root 2>/dev/null || echo "")"
IMAGE_DIGEST="$(cat IMAGE_DIGEST.txt 2>/dev/null || echo "")"

python3 - <<PY
import json
out = {
  "commit": "${COMMIT}",
  "tags": [
    "urf-tu-tvduality-main-v1",
    "urf-tu-tests-green-v1",
    "urf-tu-ci-nightly-v1",
    "urf-tu-stack-release-v1",
    "urf-tu-stack-signed-v1",
    "urf-tu-stack-freeze-v1",
    "urf-tu-stack-attested-v1",
    "urf-tu-stack-provenance-v1"
  ],
  "toolchain": "${TOOLCHAIN}",
  "merkle": {"root": "${MERKLE_ROOT}"},
  "image_digest": "${IMAGE_DIGEST}"
}
with open("${OUT}", "w", encoding="utf-8") as f:
  json.dump(out, f, indent=2, sort_keys=True)
  f.write("\\n")
print("wrote ${OUT}")
PY
