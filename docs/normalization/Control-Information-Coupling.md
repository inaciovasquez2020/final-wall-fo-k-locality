Title: Control–Information Coupling Principle (Conditional)

Status:
Conditional. Proven for restricted models; open for general RAM.

Statement:
In deterministic RAM computation, the entropy accumulated in control
flow (instruction/address trace) is upper-bounded by the cumulative
number of bits written to memory, up to constant factors.

Formally:
Let Δ_t be the number of bits written to memory at step t. Then
H(p_0, …, p_T | M_0) ≤ Σ_t Δ_t + O(1).

Scope of validity:
- Proven for oblivious RAM, fixed-access RAM, branching programs,
  AC0 update systems, and bounded-update algebras.
- Open for general RAM with unrestricted indirect addressing.

Role:
This principle is equivalent to TRAP. If true, TRAP holds and
locality-based results lift to all polynomial-time computation.
If false, any counterexample must exploit indirect addressing to
accumulate information without corresponding memory writes.

Non-claims:
No unconditional statement about P vs NP is made here.

