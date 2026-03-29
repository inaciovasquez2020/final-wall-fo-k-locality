# Hardening v2 Plan (Hermetic + Fully Pinned)

Targets:
1) Hermetic builds (no network) for Lean + verifiers.
2) Fully pinned toolchains:
   - Lean toolchain version pinned
   - mathlib commit pinned
   - OS base image digest pinned
3) Repro environment:
   - Nix flake OR Guix manifest
   - one command: nix build / guix shell + build
4) CI: run hermetic job that fails if network used.

Deliverables:
- flake.nix (or guix.scm)
- Docker hermetic builder image
- CI job: hermetic-build (network disabled)
