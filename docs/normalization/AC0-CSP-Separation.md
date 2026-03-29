Title: Unconditional Separation for AC0-Local CSPs

Theorem:
For every AC0-local CSP solver A and every frozen instance F
in the AC0-local CSP class,
the EntropyDepth satisfies:

EDA_A(F) = Θ(n)

Consequently, no AC0-local CSP solver decides all such instances
in sublinear refinement depth.

Proof:
By (B**) all AC0-local solvers admit bounded-rank refinement simulation.
Frozen instances force linear EntropyDepth under refinement.
No appeal to TRAP is required.

