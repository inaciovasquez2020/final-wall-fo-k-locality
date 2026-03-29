import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Nat.Pow

namespace URF

def BR' (Δ R : Nat) : Nat := 1 + Δ * (Δ - 1) ^ R

def Ntype_ub (k Δ R : Nat) : Nat :=
  let m := BR' Δ R
  m * (2 ^ (Nat.choose m 2)) * (m ^ k)

abbrev MEF (k Δ R : Nat) : Nat := Ntype_ub k Δ R

end URF

