# SECURITY_BASELINE_v1 (URF Core)

Scope: release/tag integrity + reproducibility + verifiability.

Controls (required checks on tags v*):
- Release Gate
- SLSA Verify Gate (GitHub attestations)
- Sigstore (cosign) — sign container + Rekor bundle
- Repro Check (Merkle root)
- Lean Repro (binary hash equality)
- Tag Signature Check (GPG)
- SBOM (SPDX + CycloneDX) + cosign sign

Artifacts bound per tag:
- transparency/files.sha256, transparency/merkle.root, transparency/log/<TAG>.entry
- tuple/TUPLE_<TAG>.txt, tuple/ARTIFACTS.sha256
- lean-attest/LEAN_BUILD_ATTEST.{txt,sha256}
- sigstore/image.digest, sigstore/cosign.bundle.json
- sbom/sbom.{spdx,cdx}.json + cosign bundles
- tsa/<TAG>/*.tsr (RFC3161 timestamps) when minted

Verification entrypoints:
- scripts/build-merkle.sh
- scripts/transparency-append.sh
- tuple/MAKE_TUPLE.sh
- scripts/lean-attest.sh
- scripts/make-offline-bundle.sh
- scripts/tsa-stamp.sh

Threat model (high level):
- Prevent silent mutation of release contents.
- Provide independent reproducible rebuild checks.
- Provide cryptographic binding: tag(GPG) + cosign(OIDC) + attestations + TSA tokens.
