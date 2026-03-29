import Mathlib.MeasureTheory.VectorMeasure.Decomposition.Jordan
import Mathlib.MeasureTheory.Integral.Bochner

open scoped BigOperators ENNReal
open MeasureTheory

noncomputable section

namespace URF

variable {α : Type*} [MeasurableSpace α]

theorem SignedMeasure_dual_norm_bound_constructive
  (s : SignedMeasure α)
  (f : α → ℝ)
  (hf : Integrable f s.totalVariation) :
  |∫ x, f x ∂s.toMeasure| ≤ ∫ x, |f x| ∂(s.totalVariation) := by
  classical
  simpa using (SignedMeasure.abs_integral_le_integral_totalVariation (s := s) (f := f) hf)

end URF
