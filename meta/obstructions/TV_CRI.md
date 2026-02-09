TV Constructive Replacement Completion Index

Obstruction object
TV-CRI := (A, T, P, V)

A
A is the set of interface axioms currently used by downstream theorems.
Distinguished TV axiom
aTV := URF.SignedMeasure_dual_norm_bound

T
T is the target theorem set that must become axiom-free for constructive TV closure.
Minimal target set
t1 SignedMeasure_dual_norm_bound_simple
t2 SignedMeasure_dual_norm_bound
t3 TVDuality.TV_eq_dual specialized to sdiff μ ν

P
P is the required primitive proof ingredient set to derive t2 without axioms.
p1 Jordan decomposition API access for SignedMeasure
p2 integral expansion via posPart and negPart
p3 absolute integral bound for nonnegative measures
p4 SimpleFunc integrability transfer lemmas
p5 L1 density or dominated convergence bridge SimpleFunc to L1

V
V is the verification witness set.
v1 Lean proof term for t2 without axioms
v2 regression certificate suite for finite and step models

Index definition
Let proved(p) ∈ {0,1}.
TV-CRI := (1/|P|) * Σ proved(p)

Operational thresholds
TV-CRI = 0.0 only interface axiom exists
TV-CRI ≥ 0.6 SimpleFunc proof completed, L1 bridge pending
TV-CRI = 1.0 interface axiom eliminated and downstream TVDuality depends only on proved lemmas

Current status marker
aTV is still present as isolated interface axiom
Therefore TV-CRI < 1.0
