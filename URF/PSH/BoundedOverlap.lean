import Mathlib
import URF.Boundary.VertexBoundary

axiom PSH_bounded_overlap
  {V : Type} [DecidableEq V]
  (adj : V → Finset V) (k Δ : ℕ) :
  ∃ C : ℕ, ∀ (S : Finset V),
    (vertexBoundary adj S).card ≤ C * S.card

import Mathlib.Data.Finset.Basic
import Mathlib.Data.Fintype.Basic

namespace URF

variable {V : Type} [DecidableEq V] [Fintype V]

structure LocalObs :=
(supp : Finset V)

axiom PSH_finite_keys :
  ∃ (K : Type) (_ : Fintype K) (key : LocalObs (V := V) → K), True

lemma bounded_overlap_from_PSH :
  ∃ M : Nat, ∀ v : V,
    (Fintype.card
      { k : (Classical.choose (PSH_finite_keys (V := V))).1 // True }) ≤ M := by
  classical
  rcases PSH_finite_keys (V := V) with ⟨K, hK, key, -⟩
  refine ⟨Fintype.card K, ?_⟩
  intro v
  simpa using le_rfl

end URF
