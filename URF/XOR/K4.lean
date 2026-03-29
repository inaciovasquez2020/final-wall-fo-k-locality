import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Vector.Basic

namespace URF
abbrev F2 := ZMod 2

variable {V : Type} [DecidableEq V]

structure K4Patch :=
(a b c d : V) (hab : a ≠ b) (hac : a ≠ c) (had : a ≠ d)
(hbc : b ≠ c) (hbd : b ≠ d) (hcd : c ≠ d)

structure K4Row :=
(coeff : Vector F2 4)  -- order: [a,b,c,d]
(rhs   : F2)

-- Minimal missing object:
constant ChronosK4Rows : List K4Row

def evalRow (P : K4Patch (V:=V)) (x : V → F2) (row : K4Row) : Prop :=
  let a := x P.a; let b := x P.b; let c := x P.c; let d := x P.d
  let v : Vector F2 4 := ⟨[a,b,c,d], by decide⟩
  (Finset.univ.sum (fun i : Fin 4 => row.coeff.get i * v.get i) = row.rhs)

def satisfiesPatch (P : K4Patch (V:=V)) (x : V → F2) : Prop :=
  ∀ row ∈ ChronosK4Rows, evalRow (V:=V) P x row

end URF

