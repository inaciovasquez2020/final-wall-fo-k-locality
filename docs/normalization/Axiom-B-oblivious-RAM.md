Title: Proof Sketch for Axiom B in the Oblivious RAM Model

Model:
Deterministic oblivious RAM with fixed word size and polynomial time.

Claim:
Oblivious RAM computations satisfy Axiom B.

Sketch:
1. Oblivious access enforces a fixed memory access pattern independent of data.
2. Each step reads and writes a bounded number of cells.
3. Cell contents range over a finite vocabulary with bounded arity.
4. State evolution is therefore a bounded-fan-in update algebra.
5. Such update systems admit simulation by bounded-rank logic
   via standard finite-model-theoretic unfolding of time into layers.
6. EntropyDepth increases by at most a constant factor under this simulation.

Conclusion:
Axiom B holds for oblivious RAM.

