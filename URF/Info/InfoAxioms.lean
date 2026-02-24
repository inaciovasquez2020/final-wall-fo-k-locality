import Mathlib

axiom InfoStepBound : ℝ
axiom entropy_monotone : ∀ {a b : ℕ}, a ≤ b → entropy_of_set a ≤ entropy_of_set b
axiom info_step_nonneg : 0 ≤ InfoStepBound

axiom entropy_step : ∀ n, entropy_of_set (n+1) - entropy_of_set n ≤ InfoStepBound

axiom info_increment
  (t : ℕ) : ℝ

axiom entropy_step : ∀ n, entropy_of_set (n+1) - entropy_of_set n ≤ InfoStepBound

axiom info_increment_le :
  ∀ t, info_increment t ≤ InfoStepBound

import Mathlib

axiom InfoStepBound : ℝ
axiom info_step_nonneg : 0 ≤ InfoStepBound

axiom info_increment
  (t : ℕ) : ℝ

axiom info_increment_le :
  ∀ t, info_increment t ≤ InfoStepBound

import Mathlib.Data.Finset.Basic

namespace URF

variable {α : Type} [DecidableEq α]

structure InfoAxioms (Info : Finset α → ℝ) : Prop :=
(nonneg : ∀ S, 0 ≤ Info S)
(empty : Info ∅ = 0)
(mono : ∀ {S T : Finset α}, S ⊆ T → Info S ≤ Info T)
(subadd : ∀ S T : Finset α, Info (S ∪ T) ≤ Info S + Info T)

end URF
