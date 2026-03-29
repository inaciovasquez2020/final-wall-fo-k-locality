# Structural Laws Index (URF)

This document indexes the frozen structural laws governing the Unified Rigidity Framework (URF)
and its core subframeworks. These laws define **what classes of strategies, refinements, or
descriptions are structurally possible** under explicit admissibility conditions.

This index is descriptive, not promotional. Each law is frozen in its canonical repository.

---

## URF Core Laws

### 1. URF Admissibility Law (URF-ADMISSIBLE)

**Statement (informal):**  
Any claim certified under URF must respect locality, bounded per-step information gain,
and explicit accounting of extracted information.

**Role:**  
Defines the admissible class of refinement, inference, and certification strategies.

**Canonical specification:**  
`docs/foundations/urf_admissible_spec.md` (this repository)

---

### 2. URF Applicability Test (URF-AT)

**Statement (informal):**  
URF applies only to claims that assert necessity, impossibility, optimality, or inevitability.
Exploratory, heuristic, or provisional work lies outside URF scope.

**Role:**  
Prevents category errors and misuse of rigidity arguments.

**Canonical specification:**  
`docs/foundations/urf_applicability_test.md` (this repository)

---

## Chronos Laws

### 3. Chronos Strategy-Class No-Go Law

**Statement (formal):**  
For satisfiable families with \( H(X_n)=\Omega(n) \), any admissible fixed-radius local refinement
strategy that recovers a witness with vanishing ambiguity must incur
\[
\mathrm{TC}(T) \ge \Omega(n).
\]

**Role:**  
Rules out sublinear total information extraction within the admissible strategy class.
Optimization within the class cannot evade the bound.

**Canonical statement:**  
Chronos-EntropyDepth  
`docs/foundations/chronos_no_go_theorem.md`

---

## Status

- All listed laws are **frozen**.
- Extensions may strengthen bounds but must not weaken stated constraints.
- Conditional laws are explicitly labeled in their canonical locations.

---

## Scope Note

This index records **structural boundaries**, not empirical predictions
and not performance claims.

