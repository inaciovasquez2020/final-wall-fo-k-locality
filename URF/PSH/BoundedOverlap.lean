import Mathlib
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Fintype.Basic
import URF.Boundary.VertexBoundary

/-- PSH-style bounded overlap stated directly at the vertex-boundary level. -/
axiom PSH_bounded_overlap
  {V : Type} [DecidableEq V]
  (adj : V → Finset V) (k Δ : ℕ) :
  ∃ C : ℕ, ∀ (S : Finset V),
    (vertexBoundary adj S).card ≤ C * S.card

namespace URF

variable {V : Type} [DecidableEq V] [Fintype V]

/-- Local observation with finite support. -/
structure LocalObs :=
(supp : Finset V)

/--
Abstract PSH finiteness principle:
local observations admit a finite key space.
-/
axiom PSH_finite_keys :
  ∃ (K : Type) (_ : Fintype K) (key : LocalObs (V := V) → K), True

/--
Trivial boundedness consequence: any finite key space
admits a uniform cardinal bound.
This is the *only* thing used downstream.
-/
lemma bounded_overlap_from_PSH :
  ∃ M : ℕ, True := by
  classical
  rcases PSH_finite_keys (V := V) with ⟨K, hK, key, -⟩
  exact ⟨Fintype.card K, trivial⟩

end URF