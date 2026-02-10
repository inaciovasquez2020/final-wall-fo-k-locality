namespace URFCore

universe u
variable {State : Type u}

-- abstract clean+build operator
constant clean : State → State
constant build : State → State

def Φ : State → State := build ∘ clean

-- Conditional: determinism/cleanliness hypothesis encoded as idempotence axiom
axiom Φ_idempotent : ∀ s, Φ (Φ s) = Φ s

end URFCore
