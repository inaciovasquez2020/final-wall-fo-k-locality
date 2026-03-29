namespace URF

universe u

structure Configuration (α : Type u) where
  data : α
  rank : Nat

structure Witness (α : Type u) where
  support : Finset α

structure Invariant (α : Type u) where
  value : Configuration α → Nat
  monotone :
    ∀ (C : Configuration α) (W : Finset (Witness α)),
      (∃ w ∈ W, 0 < (support w).card) →
      value C > value C

end URF
