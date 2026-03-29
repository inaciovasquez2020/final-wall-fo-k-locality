import Mathlib
import URF.Boundary.VertexBoundary
import URF.PSH.BoundedOverlap
import URF.Info.InfoAxioms

axiom entropy_of_set : ℕ → ℝ

lemma transport_entropy_bound
  {V : Type} [DecidableEq V]
  (adj : V → Finset V)
  (k Δ : ℕ) :
  ∃ C, ∀ S : Finset V,
    entropy_of_set (vertexBoundary adj S).card
      ≤ entropy_of_set S.card + C := by
  obtain ⟨C, hC⟩ := PSH_bounded_overlap adj k Δ
  refine ⟨C, ?_⟩
  intro S
  have hbd : (vertexBoundary adj S).card ≤ C * S.card := hC S
  have hmono :
      entropy_of_set (vertexBoundary adj S).card
        ≤ entropy_of_set (C * S.card) :=
    entropy_monotone hbd
  have hlin :
      entropy_of_set (C * S.card)
        ≤ entropy_of_set S.card + (C * InfoStepBound) := by
    admit
  linarith
