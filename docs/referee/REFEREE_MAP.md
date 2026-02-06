Referee Map — Chronos / EntropyDepth

This document classifies results by epistemic status.

1. Proven (Unconditional)
2. Conditional (Explicit Hypotheses Stated)
3. Framework / Reduction Results
4. Explicit Non-Claims

No claim outside Section 1 is asserted unconditionally.

--------------------------------------------------
1. Proven (Unconditional)
--------------------------------------------------

• Formal definition of EntropyDepth.
• Correctness of the refinement–entropy accounting identity.
• Monotonicity of EntropyDepth under admissible refinement.
• Equivalence of transcript capacity and entropy non-amplification.

--------------------------------------------------
2. Conditional Results (Explicit Hypotheses)
--------------------------------------------------

All results in this section are conditional on the stated hypotheses and are not asserted unconditionally.

Hypothesis H1 (Locality):
Refinement procedures are FO^k-admissible with fixed k.

Hypothesis H2 (Bounded Information Loss):
Each refinement step incurs O(1) conditional mutual information loss.

Hypothesis H3 (Residual Entropy Persistence):
Adaptive refinement preserves Ω(n) residual entropy unless depth is Ω(n).

Under H1–H3:
• EntropyDepth lower bounds of order Ω(n) (or stronger, as stated) hold.
• Any polynomial-time refinement algorithm must violate at least one hypothesis.

--------------------------------------------------
3. Framework / Reduction Results
--------------------------------------------------

• Definition of EntropyDepth as a refinement-complexity invariant.
• Formal separation between refinement-based and global-invariant algorithms.
• Reduction of P ≠ NP lower-bound attempts to entropy non-amplification.
• Normalization of algorithmic strategies into admissible refinement systems.
• Identification of exact obstruction points requiring new mathematics.

--------------------------------------------------
4. Explicit Non-Claims
--------------------------------------------------

• This work does not claim an unconditional proof of P ≠ NP.
• This work does not claim a resolution of any Clay Millennium Problem.
• No lower bound is asserted outside explicitly stated hypotheses.
• No probabilistic or empirical evidence is used as proof.
• No claim depends on unverified physical assumptions.
• No result asserts optimal constants unless stated.

