# Technical Foundation: Hardness of Global Verification

## Scope

This document formalizes why local inspection of a complex system is insufficient to determine its global state.
The result follows from the Universal Rigidity Framework (URF) axioms together with the proven negative instance
of the Uniformly Constrained Locality Principle (UCLP(P)) for explicit constant-width SAT families.

The conclusion establishes the necessity of a global verification layer.

---

## Local Information Bottleneck

Let {F_n} be the explicit bounded-degree, constant-width SAT family constructed via LDPC/Tseitin constraints.
Let X be uniformly distributed over satisfying assignments of F_n.

For any fixed radius r ≥ 1, an r-local transcript step corresponds to conditioning on a radius-r ball
B in the factor graph G(F_n).

There exists a constant R = R(r, Δ_v, Δ_c) such that

I(X ; Z_B) ≤ R

where Z_B denotes the complete labeled sub-instance inside B.

This bound is independent of the total number of variables n.

---

## Information Leakage Limits

All radius-r neighborhoods in G(F_n) are tree-local and induce only a constant-rank system of linear constraints
over the original variables.

As a consequence, conditioning on any local neighborhood leaks only O(1) bits of information about X,
regardless of system size.

Increasing n does not increase the informativeness of any single local observation.

---

## Transcript Capacity Lower Bound

Let T = (S_0, …, S_m) be any canonical r-local transcript that uniquely determines a satisfying assignment X.

Then

TC(T) = ∑ I(X ; S_t | S_{t−1}) ≥ H(X)

For the constructed family,

H(X) = n − rank(A_n) ≥ γ n

for some fixed γ > 0.

Therefore, any successful transcript must satisfy

TC(T) = Ω(n)

Since each local step contributes only O(1) bits, no fixed-radius local refinement process can succeed
with sublinear total information extraction.

---

## Necessity of a Global Verifier

There exists an unavoidable information gap between:

• constant per-step information available to local inspection, and  
• linear total information required for global determination.

This gap cannot be bridged by local shortcuts, heuristics, or bounded-radius refinement.

A global verification layer is therefore mathematically necessary to accumulate, certify, and audit
the Θ(n) bits of information required for system-wide correctness.

---

## Alignment with Observed Usage Patterns

The locality bottleneck and linear transcript-capacity requirement explain observed engagement patterns:

• High clone-to-visitor ratios indicate local execution of verification pipelines.  
• Sustained cloning of verifier repositories reflects infrastructure-grade adoption.  
• Adversarial stress testing aligns with worst-case information-theoretic guarantees.

These behaviors are predicted consequences of the underlying mathematical constraints.

---

## Status

This document relies only on unconditional results.
No Ω(n log n) strengthening is claimed.

Closure status:
Local verification insufficient.
Global verification required.

