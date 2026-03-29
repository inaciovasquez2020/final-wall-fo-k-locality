#!/usr/bin/env bash
set -euo pipefail

H=$(jq -r '.lean_deps_hash // empty' PROVENANCE.json)
R=$(jq -r '.build_merkle_root // empty' PROVENANCE.json)

if [ -z "$H" ] || [ -z "$R" ]; then
  echo "ERROR: PROVENANCE.json missing lean_deps_hash or build_merkle_root" >&2
  exit 1
fi

cat > URFCore/ProvenanceConstants.lean <<LEOF
namespace URFCore

def expectedLeanDepsHash : String := "$H"
def expectedBuildMerkleRoot : String := "$R"

def expectedAttestationTuple : String × String :=
  (expectedLeanDepsHash, expectedBuildMerkleRoot)

end URFCore
LEOF
