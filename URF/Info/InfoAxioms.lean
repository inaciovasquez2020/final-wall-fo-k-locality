import Mathlib
import Mathlib.Data.Finset.Basic

axiom InfoStepBound : ℝ
axiom info_step_nonneg : 0 ≤ InfoStepBound

axiom info_increment (t : ℕ) : ℝ
axiom info_increment_le :
  ∀ t, info_increment t ≤ InfoStepBound

namespace URF

variable {α : Type} [DecidableEq α]

structure InfoAxioms (Info : Finset α → ℝ) : Prop :=
(nonneg : ∀ S, 0 ≤ Info S)
(empty : Info ∅ = 0)
(mono : ∀ {S T : Finset α}, S ⊆ T → Info S ≤ Info T)
(subadd : ∀ S T : Finset α, Info (S ∪ T) ≤ Info S + Info T)

end URF
