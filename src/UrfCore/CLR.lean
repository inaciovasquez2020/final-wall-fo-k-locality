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

end CLR
end UrfCore

