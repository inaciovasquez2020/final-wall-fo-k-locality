import UrfCore.Prelude

namespace UrfCore
namespace CLR

structure Graph (V : Type) where
  adj : V → V → Prop
  degree_bound : ℕ

variable {V : Type} [Fintype V]

def radiusBall (_G : Graph V) (_R : ℕ) (_v : V) : Finset V :=
  Finset.univ

end CLR
end UrfCore

