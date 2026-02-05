import UrfCore.Prelude

namespace UrfCore
namespace CLR

structure Graph (V : Type) :=
  (adj : V → V → Prop)
  (degree_bound : ℕ)

variable {V : Type} [Fintype V]

def radiusBall (G : Graph V) (R : ℕ) (v : V) : Finset V :=
  Finset.univ.filter (fun _ => True)

end CLR
end UrfCore
