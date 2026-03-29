# Release Security Spec (URF Core)

## Objects
- Commit C, tree T.
- Tag τ = v* (annotated, GPG-signed).
- Merkle manifest M = transparency/files.sha256, root R = transparency/merkle.root.
- Log entry L_τ = transparency/log/τ.entry binding (τ,C,R,time).
- Lean attestation A = lean-attest/LEAN_BUILD_ATTEST.txt and hash hA.
- Tuple U_τ = tuple/TUPLE_τ.txt and artifacts list H = tuple/ARTIFACTS.sha256 with root hH.
- Container digest D = sigstore/image.digest.
- Sigstore bundle B = sigstore/cosign.bundle.json (keyless OIDC, Rekor-inclusive).
- SBOMs S_spdx, S_cdx and their cosign bundles.
- Optional TSA tokens K = tsa/τ/*.tsr for (R,M,U_τ).

## Required CI checks (policy)
- SLSA Verify Gate: gh attestation verify for {R,M,D,B,SBOMs}.
- Sigstore: cosign sign + verify via bundle for D; store B.
- Repro Check: double rebuild of R must match.
- Lean Repro: double build of .lake/build file hashes must match.
- Tag Signature: git tag -v τ must validate.
- SBOM: generate + cosign sign-blob bundles; attest in provenance.

## Verification algorithm (auditor)
1) Verify τ is signed (git tag -v).
2) Verify Merkle: sha256(M) == R.
3) Verify tuple: sha256(H) equals hH recorded in U_τ.
4) Verify Lean attestation hash: sha256(A) == hA.
5) Verify cosign: cosign verify --bundle B D.
6) Verify attestations: gh attestation verify each subject path.
7) If TSA present: openssl ts -reply validate K; compare imprint to corresponding file.

## Acceptance condition
All verifications pass and required checks are enforced by ruleset on tags v*.
