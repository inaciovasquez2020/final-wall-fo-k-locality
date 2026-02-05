import UrfCore.Prelude

namespace UrfCore
namespace CLR

open Classical

structure Graph (V : Type) where
  adj : V → V → Prop
  degree_bound : ℕ

variable {V : Type} [Fintype V] [DecidableEq V]

noncomputable def pathLength (_G : Graph V) (_v _w : V) : ℕ :=
  0

noncomputable def radiusBall (G : Graph V) (R : ℕ) (v : V) : Finset V :=
  Finset.univ.filter (fun w => pathLength G v w ≤ R)

lemma radiusBall_mono_R
  (G : Graph V) {R₁ R₂ : ℕ} (h : R₁ ≤ R₂) (v : V) :
  radiusBall G R₁ v ⊆ radiusBall G R₂ v :=
by
  intro w hw
  have hw' : pathLength G v w ≤ R₁ := by
    simpa [radiusBall] using hw
  have : pathLength G v w ≤ R₂ := le_trans hw' h
  simpa [radiusBall] using this

end CLR
end UrfCore

