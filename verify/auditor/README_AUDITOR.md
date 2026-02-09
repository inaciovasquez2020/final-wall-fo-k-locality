# Third-Party Auditor Package (URF Core)

Goal: independently verify a release tag without trusting CI logs.

What to check:
1) Merkle: sha256(transparency/files.sha256) == transparency/merkle.root
2) Tuple: sha256(tuple/ARTIFACTS.sha256) matches artifacts_sha256_root in tuple/TUPLE_<TAG>.txt
3) Lean attestation: sha256(LEAN_BUILD_ATTEST.txt) == LEAN_BUILD_ATTEST.sha256
4) Sigstore:
   - cosign verify --bundle sigstore/cosign.bundle.json <image@digest in sigstore/image.digest>
5) GitHub attestations (online): gh attestation verify <artifact> --repo <owner/repo>
6) TSA tokens (if present): openssl ts -reply -in tsa/<TAG>/<file>.tsr -text

Bundle:
- use scripts/make-offline-bundle.sh <TAG> to produce verify/offline/urf-core_<TAG>_offline_bundle.tar.gz
