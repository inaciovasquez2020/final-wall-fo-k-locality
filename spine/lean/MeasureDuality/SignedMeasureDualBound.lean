import spine.lean.MeasureDuality.SignedMeasureDualBoundConstructive

open scoped BigOperators ENNReal
open MeasureTheory

noncomputable section

namespace URF

variable {α : Type*} [MeasurableSpace α]

theorem SignedMeasure_dual_norm_bound
  (s : SignedMeasure α)
  (f : α → ℝ)
  (hf : Integrable f s.totalVariation) :
  |∫ x, f x ∂s.toMeasure| ≤ ∫ x, |f x| ∂(s.totalVariation) :=
  SignedMeasure_dual_norm_bound_constructive (s := s) (f := f) hf

end URF
