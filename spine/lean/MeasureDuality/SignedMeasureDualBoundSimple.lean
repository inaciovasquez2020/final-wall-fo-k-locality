import Mathlib.MeasureTheory.VectorMeasure.Decomposition.Jordan
import Mathlib.MeasureTheory.Integral.SimpleFunc
import Mathlib.MeasureTheory.Integral.Bochner.Basic

open MeasureTheory

noncomputable section

namespace URF

variable {α : Type*} [MeasurableSpace α]

/--
Simple function version of the TV dual bound.

Target inequality for a real-valued measurable simple function `f`:

|∫ f d s| ≤ ∫ |f| d (s.totalVariation)

This file is intended to become the local proof that replaces the interface axiom.
For now it provides a lemma statement in the correct shape, with the proof delegated
to the repository interface lemma.
-/
theorem SignedMeasure_dual_norm_bound_simple
  (s : SignedMeasure α)
  (f : MeasureTheory.SimpleFunc α ℝ)
  (hf : Integrable f s.totalVariation) :
  |∫ x, f x ∂s.toMeasure| ≤ ∫ x, |f x| ∂(s.totalVariation) := by
  simpa using URF.SignedMeasure_dual_norm_bound (s := s) (f := f) hf

end URF
