# Unified Rigidity Framework — Reduction Status (Canonical)

This document records the **authoritative reduction state** of URF.
It distinguishes proved results, conditional closures, and remaining open walls.

---

## Closed (Unconditional)

- Information-theoretic capacity accounting
- Transcript mutual information telescoping
- FO^k locality ⇒ finite per-step transcript alphabet
- Normalization of locality-based refinement processes

---

## Closed (Conditional)

### FO^k Locality Wall
**Status:** CONDITIONALLY CLOSED

- Cycle–Orbit Splitting Lemma holds **conditional on Configuration Pumping**
- Configuration Pumping is based on finite FO^k type counting
- No EF Cycle–Linkage Trap, holonomy, or global linkage principle assumed

Artifacts:
- `toolkit/URF-Core/final-wall-fo-k-locality/lemmas/cycle_orbit_splitting.tex`
- `toolkit/URF-Core/final-wall-fo-k-locality/lemmas/configuration_pumping.tex`

---

## Open (Terminal Walls)

### Clause Contraction Lemma (CCL)
**Status:** OPEN — analytic wall

- Uniform contraction coefficient ρ < 1 remains unresolved
- Frozen regime refutations exist
- Liquid regime holds conditionally under spectral independence

Artifact:
- `urf-axioms/last-door/OPEN_PROBLEM_CCL.md`

---

## XYSTEM

**Status:** OPEN / CONDITIONAL

- Reduced to FO^k locality + analytic contraction
- FO^k component conditionally closed
- Remaining obstruction is CCL

No unconditional proof or refutation currently exists.

---

## Canonical Position

URF is **reduction-complete** up to a single analytic open problem (CCL).
All other walls are either closed or conditionally closed with explicit dependencies.

- CCL deferred
- XYSTEM deferred
- No new work until review
