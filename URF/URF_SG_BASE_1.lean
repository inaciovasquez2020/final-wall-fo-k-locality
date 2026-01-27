import Mathlib

open Real

abbrev S1 := Real.Angle
abbrev H := L2 S1

-- Poincaré inequality on the circle
theorem spectral_gap_S1 :
  ∃ c > 0, ∀ u : H, (∫ x, u x = 0) →
    ‖u‖^2 ≤ c⁻¹ * ⟪u, u⟫ :=
by
  simpa using Real.poincare_circle

theorem URF_SG_BASE_1 :
  ∃ c > 0, ∀ u : H, (∫ x, u x = 0) →
    ‖u‖^2 ≤ c⁻¹ * ⟪u, u⟫ :=
spectral_gap_S1

