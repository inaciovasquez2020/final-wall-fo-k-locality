# Offline Verification Bundle

Inputs (from this repo):
- transparency/files.sha256
- transparency/merkle.root
- transparency/log/<TAG>.entry
- tuple/TUPLE_<TAG>.txt
- tuple/ARTIFACTS.sha256
- sigstore/image.digest
- sigstore/cosign.bundle.json
- lean-attest/LEAN_BUILD_ATTEST.txt
- lean-attest/LEAN_BUILD_ATTEST.sha256

Steps:
1) Verify Merkle:
   - sha256(transparency/files.sha256) == transparency/merkle.root
2) Verify tuple:
   - sha256(tuple/ARTIFACTS.sha256) == artifacts_sha256_root in tuple/TUPLE_<TAG>.txt
3) Verify Lean attestation hash:
   - sha256(lean-attest/LEAN_BUILD_ATTEST.txt) == lean-attest/LEAN_BUILD_ATTEST.sha256
4) Verify cosign bundle (no network required for signature check; Rekor inclusion requires network):
   - cosign verify --bundle sigstore/cosign.bundle.json <image@digest from sigstore/image.digest>
5) Cross-check:
   - tag/commit in transparency/log/<TAG>.entry matches commit in tuple/TUPLE_<TAG>.txt and LEAN_BUILD_ATTEST.txt
