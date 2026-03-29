namespace URF

universe u

structure Configuration (α : Type u) where
  data : α
  rank : Nat

structure Witness (α : Type u) where
  support : Finset α

def value {α : Type u} (C : Configuration α) : Nat := C.rank

theorem strict_monotone
  {α : Type u} (C : Configuration α) (W : Finset (Witness α))
  (h : ∃ w ∈ W, 0 < w.support.card) :
  value C > value { C with rank := C.rank - 1 } :=
by
  simp [value]
  exact Nat.sub_lt (Nat.succ_le_of_lt (Nat.pos_of_ne_zero (by decide))) (by decide)

end URF
