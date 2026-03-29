namespace URF

universe u

structure Configuration (α : Type u) where
  data : α
  rank : Nat

structure Witness (α : Type u) where
  support : Finset α

class HasURFValue (α : Type u) where
  value : Configuration α → Nat

instance {α : Type u} : HasURFValue α where
  value C := C.rank

def witnessContribution {α : Type u} (w : Witness α) : Nat :=
  w.support.card

theorem witnessContribution_positive
  {α : Type u} (w : Witness α)
  (h : 0 < w.support.card) :
  0 < witnessContribution w :=
by
  simpa [witnessContribution] using h

theorem rank_decrease_of_positive_contribution
  {α : Type u} (C : Configuration α) (w : Witness α)
  (hC : 0 < C.rank)
  (hw : 0 < witnessContribution w) :
  C.rank - witnessContribution w < C.rank :=
by
  exact Nat.sub_lt hC hw

theorem strict_monotone
  {α : Type u} [HasURFValue α]
  (C : Configuration α) (w : Witness α)
  (hC : 0 < C.rank)
  (hw : 0 < witnessContribution w) :
  HasURFValue.value { C with rank := C.rank - witnessContribution w } < HasURFValue.value C :=
by
  simpa [HasURFValue.value] using rank_decrease_of_positive_contribution C w hC hw

end URF
