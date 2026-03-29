# Atlas Statistical Coverage Bound

## Conditional Lemma ATLAS.STAT.NoSmallCE  (Conditional)
Assume a probability model μ_N on the finite set 𝒰_N of candidate structures of size ≤ N
(e.g., uniform on 𝒰_N, or a declared sampling distribution with full support).

Let 𝒞 ⊆ 𝒰_N be the set of counterexamples to a target statement S under stated assumptions.

If the atlas verification certifies that no element of 𝒰_N is a counterexample (i.e., 𝒞 = ∅),
then:
μ_N(𝒞) = 0.

If instead the atlas samples t independent draws X_1,...,X_t ~ μ_N and finds no counterexample,
then for any p := μ_N(𝒞),
P[no counterexample in t draws] = (1-p)^t ≤ e^{-pt},
hence
p ≤ (1/t)·log(1/δ)  whenever  P[no counterexample] ≥ 1-δ.

## Minimal missing assumption
A declared μ_N and independence (or an explicit martingale alternative).
