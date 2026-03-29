import Mathlib.MeasureTheory.Decomposition.SignedHahn
import Mathlib.MeasureTheory.Decomposition.Jordan
import Mathlib.MeasureTheory.Measure.Signed
import Mathlib.MeasureTheory.Integral.Bochner
import Mathlib.MeasureTheory.Function.EssSup

open scoped BigOperators ENNReal
open MeasureTheory

namespace TVDuality

variable {Ω : Type} [MeasurableSpace Ω]

def sdiff (μ ν : Measure Ω) : SignedMeasure Ω :=
  μ.toSignedMeasure - ν.toSignedMeasure

def TV (μ ν : Measure Ω) : ℝ≥0∞ :=
  (sdiff (μ := μ) (ν := ν)).totalVariation univ

noncomputable def TVDual (μ ν : Measure Ω) : ℝ≥0∞ :=
  ⨆ (f : Ω → ℝ) (_hf : Measurable f) (_hb : essSup (fun x => ‖f x‖) ≤ (1:ℝ)),
    ENNReal.ofReal (Real.abs (∫ x, f x ∂(sdiff (μ := μ) (ν := ν))))

lemma integral_bound_by_tv
  (s : SignedMeasure Ω) (f : Ω → ℝ)
  (hf : Measurable f)
  (hB : essSup (fun x => ‖f x‖) ≤ (1:ℝ)) :
  ENNReal.ofReal (Real.abs (∫ x, f x ∂s))
    ≤ s.totalVariation univ := by
  classical
  have h1 :=
    SignedMeasure.integral_le_lintegral_totalVariation
      (s := s) (f := fun x => ‖f x‖)
  have h2 :
      ∫⁻ x, ‖f x‖ ∂(s.totalVariation)
        ≤ (1:ℝ≥0∞) * s.totalVariation univ := by
    have h_ae :
        (fun x => (‖f x‖ : ℝ≥0∞))
          ≤ᵐ[ s.totalVariation ]
        fun _ => (1:ℝ≥0∞) := by
      refine Filter.Eventually.of_forall ?_
      intro x
      have hx :
          (‖f x‖ : ℝ≥0∞)
            ≤ ENNReal.ofReal (1:ℝ) := by
        have hx' := hB
        exact by
          have : ‖f x‖ ≤ 1 := by
            exact le_of_lt (by decide)
          simpa using this
      simpa using hx
    have :=
      lintegral_mono_ae h_ae
    simpa using this
  have :=
    calc
      ENNReal.ofReal (Real.abs (∫ x, f x ∂s))
          ≤ ∫⁻ x, ‖f x‖ ∂(s.totalVariation) := by
            simpa using h1
      _ ≤ (1:ℝ≥0∞) * s.totalVariation univ := h2
      _ = s.totalVariation univ := by
            simp
  simpa using this

theorem TV_ge_dual (μ ν : Measure Ω) :
  TV (μ := μ) (ν := ν) ≥ TVDual (μ := μ) (ν := ν) := by
  classical
  refine iSup_le ?_
  intro f
  refine iSup_le ?_
  intro hf
  refine iSup_le ?_
  intro hB
  have :=
    integral_bound_by_tv
      (s := sdiff (μ := μ) (ν := ν))
      f hf hB
  simpa [TV, TVDual]

theorem TV_le_dual (μ ν : Measure Ω) :
  TV (μ := μ) (ν := ν) ≤ TVDual (μ := μ) (ν := ν) := by
  classical
  let s := sdiff (μ := μ) (ν := ν)
  obtain ⟨P, N, hPmeas, hNmeas, hpos, hneg, hCompl⟩ :=
    SignedMeasure.exists_isCompl_positive_negative s
  let f : Ω → ℝ :=
    fun x => if x ∈ P then 1 else if x ∈ N then -1 else 0
  have hf : Measurable f := by
    refine Measurable.piecewise ?_ ?_ ?_
    exact hPmeas
    refine Measurable.piecewise ?_ ?_ ?_
    exact hNmeas
    exact measurable_const
    exact measurable_const
    exact measurable_const
  have hB : essSup (fun x => ‖f x‖) ≤ (1:ℝ) := by
    classical
    refine le_of_eq ?_
    simp
  have hEval :
      ENNReal.ofReal (Real.abs (∫ x, f x ∂s))
        = s.totalVariation univ := by
    have :=
      SignedMeasure.integral_indicator_positive_negative
        (s := s) (P := P) (N := N)
        hPmeas hNmeas hpos hneg hCompl
    simpa using this
  have :
      s.totalVariation univ
        ≤ TVDual (μ := μ) (ν := ν) := by
    refine le_iSup_of_le f ?_
    refine le_iSup_of_le hf ?_
    refine le_iSup_of_le hB ?_
    simpa [TVDual, s, TV] using hEval
  simpa [TV, s] using this

theorem TV_eq_dual (μ ν : Measure Ω) :
  TV (μ := μ) (ν := ν) = TVDual (μ := μ) (ν := ν) := by
  exact le_antisymm
    (TV_le_dual (μ := μ) (ν := ν))
    (TV_ge_dual (μ := μ) (ν := ν))

end TVDuality
