#!/usr/bin/env bash
set -euo pipefail

cosign verify-blob \
  --signature SLSA_PREDICATE.sig \
  --key cosign.pub \
  SLSA_PREDICATE.json

echo "OK: SLSA signature verified"
