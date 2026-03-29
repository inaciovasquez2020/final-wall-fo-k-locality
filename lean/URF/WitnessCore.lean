namespace URF

universe u

structure Cycle (α : Type u) :=
  (nodes : Finset α)

structure Witness (α : Type u) :=
  (cycle : Cycle α)

def cycleSize {α} (w : Witness α) : Nat :=
  w.cycle.nodes.card

end URF
