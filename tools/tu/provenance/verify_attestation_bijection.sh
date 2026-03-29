#!/usr/bin/env bash
set -euo pipefail
jq '{lean_deps_hash,build_merkle_root}' PROVENANCE.json > /tmp/prov_proj.json
diff -u /tmp/prov_proj.json ATTESTATION_SUBJECT.json
echo "OK: attestation <-> provenance bijection"
