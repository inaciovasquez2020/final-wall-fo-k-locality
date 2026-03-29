Title: Transcript Reduction Axiom for Polytime (TRAP)

Status: Frozen axiom (explicitly assumed, not proved)

Statement:
For every deterministic polynomial-time algorithm A deciding SAT,
there exist constants (k,R,C) and a URF-normalized transcript
τ0 → τ1 → … → τT satisfying locality (L1), finite capacity (L2),
and refinement semantics (L3), such that A is simulated with
Θ-equivalent EntropyDepth by an FO^k / WL^k refinement system.

Role:
This axiom is the only non-derived assumption used to extend
locality-frontier results to all polynomial-time computation.

Scope:
All theorems depending on this axiom are explicitly marked
“Conditional on TRAP”.

