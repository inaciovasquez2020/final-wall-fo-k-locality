# Unified Capacity–Locality Problem (UCLP)

## Statement

The Unified Capacity–Locality Problem (UCLP) asks whether polynomial-time
computation is universally constrained by *local information capacity*:
namely, whether any algorithm operating via fixed-radius local refinement
must extract a superlinear amount of global information to solve certain
natural decision problems.

Formally, UCLP investigates whether there exist explicit problem families
for which any fixed-radius local transcript necessarily incurs large total
information cost (transcript capacity), ruling out sublinear-capacity
solutions under URF-admissibility.

---

## Status: RESOLVED (Scoped)

**Decision:** **NO**, for an explicit constant-width SAT family.

An explicit width-3 SAT family with bounded-degree, high-girth factor graphs
admits an **unconditional linear lower bound** on transcript capacity:
any fixed-radius local transcript that determines a satisfying assignment
must extract **Ω(n)** total information.

This establishes a negative resolution of UCLP **within the declared scope**
(fixed-radius locality; canonical local transcripts; URF-admissibility).

---

## Supporting Construction and Proof

The construction uses LDPC/Tseitin-style parity constraints encoded as
constant-width CNF, with the following properties:

- Width-3 CNF
- Bounded variable–clause degrees
- High girth (tree-like local neighborhoods)
- Uniform satisfying distribution forming an affine subspace

Key results:

- Each radius-r local observation reveals **O(1)** bits of information.
- The total entropy of the solution space is **Θ(n)**.
- Therefore, any transcript that uniquely determines a solution has
  transcript capacity **Ω(n)**.

**Canonical artifact and proof:**

- Repository:  
  https://github.com/inaciovasquez2020/overlap-rigidity-counterexamples
- Proof document:  
  `docs/uclp_linear_tc_ldpc.tex`

---

## Scope and Non-Claims

- The result is **unconditional** within the stated locality model.
- No **Ω(n log n)** bound is claimed here.
- Stronger bounds would require additional information-diffusion or
  entropy-decay mechanisms not assumed in UCLP.
- The resolution applies to **explicit constant-width SAT families** and
  does not assert universality across all computational models.

---

## Governance Note

This document records the **authoritative URF decision** for UCLP.
Supporting artifacts live in dedicated evidence repositories; this page
serves as the canonical semantic reference.

**Status:** **CLOSED**
