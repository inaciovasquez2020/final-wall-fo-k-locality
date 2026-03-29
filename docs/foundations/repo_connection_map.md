# URF Repository Connection Map (Canonical)

## Layer 0 — Core Axioms / Normalization
- **urf-core**: axioms, definitions, normalization doctrine, terminal-obstruction schema.

Edges:
- urf-core → Chronos-EntropyDepth
- urf-core → yang-mills-hs-gap-cert
- urf-core → cells-downwards-rh
- urf-core → (NS reduction artifacts, physics foundations artifacts)

## Layer I — Complexity / Refinement (URF instantiation in CS)
- **Chronos-EntropyDepth**: entropy-depth, transcript capacity, FO^k/local refinement obstruction.

Edge:
- urf-core → Chronos-EntropyDepth

## Layer II — Spectral / Operator (URF instantiation in operator coercivity)
- **cells-downwards-rh**: spectral “cells-downwards” experiments + verification/cert layer for RH-style operator rigidity.
- **yang-mills-hs-gap-cert**: executable Hilbert–Schmidt certification + spectral-gap scaffolding + terminal inequality classification.

Edges:
- urf-core → cells-downwards-rh
- urf-core → yang-mills-hs-gap-cert

## Layer III — PDE / Physics Foundations (URF instantiation in dynamics/thermo)
- Navier–Stokes reduction artifacts: conditional final wall (IECP/DVR-class obstruction).
- Operational Rigidity / Consonance / Collapse / Exchange Force artifacts: capacity–entropy invariant Φ = H − C; prediction horizon; operational rigidity.

Edge:
- urf-core → physics/PDE strands

## Layer IV — Verification / Certification Overlay (cross-cutting)
Shared infrastructure pattern across repos:
- CLAIM graph + STATUS table
- deterministic verification scripts
- certificate schema and verification
- CI green + frozen tags

Edges:
- (all repos) → certification overlay

## Unified Template (all strands)
1. Define complexity/entropy/information invariant.
2. Define capacity/locality constraint.
3. Prove non-amplification / bounded step gain under admissible refinement.
4. Reduce to a single terminal obstruction/inequality (Cyclone-type wall).
5. Classify unconditional vs conditional boundary.
