import Mathlib.Data.List.Basic
import Mathlib.Data.List.Nodup
import Mathlib.Data.Nat.Basic

namespace URF

structure OrEdge where
(u v : Nat)
deriving DecidableEq

structure LiftJSON where
(nSheets : Nat)
(seed : Nat)
(edgePerm : List (OrEdge × List Nat))

def isPermList (n : Nat) (p : List Nat) : Prop :=
  p.length = n ∧ p.Nodup ∧ (∀ x ∈ p, x < n)

def verifyLift (L : LiftJSON) : Prop :=
  ∀ (e,p) ∈ L.edgePerm, isPermList L.nSheets p

end URF

