EntropyDepth Simulation Inequality

Definition (EntropyDepth).
Let P_n be a problem instance distribution.
Define EntropyDepth:

ED(P_n) := Σ_t ΔH_t

where ΔH_t is the entropy loss at refinement step t.

Theorem (Simulation Inequality).
For any algorithm A in M_reasonable normalized to a local
refinement system R_A,

T_A(n) >= ED(P_n) / polylog(n)

Proof.
By CE-Bridge, for each step t,

ΔH_t <= O(ΔI_t)

Summing over steps gives:

ED(P_n) <= Σ_t O(ΔI_t) <= T_A(n) * TC(A)

Since TC(A) <= polylog(n) for M_reasonable algorithms,
the inequality follows.

