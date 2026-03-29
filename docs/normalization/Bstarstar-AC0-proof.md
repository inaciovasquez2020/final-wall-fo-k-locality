Title: Proof Sketch of (B**) for AC0 Update Algebra

1. AC0 circuits of constant depth correspond to FO-definable queries
   over finite structures with bounded quantifier rank.

2. Bounded fan-in and bounded arity ensure that each update step
   modifies only O(1) relations with O(1) new dependencies.

3. By classical results (Immerman–Vardi style),
   bounded-depth AC0 update sequences can be unfolded into
   bounded-rank logical refinement over time layers.

4. Each refinement step increases descriptive information by O(1),
   hence EntropyDepth is preserved up to a constant factor.

Conclusion:
AC0 bounded-arity update systems embed into bounded-rank logic refinement.
Therefore (B**) holds for this restricted model.

