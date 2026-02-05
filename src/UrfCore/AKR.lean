import UrfCore.Prelude

namespace UrfCore
namespace AKR

structure Kernel (V : Type) where
  carrier : V → Prop

axiom archimedeanBound : ℕ

def dummy : Nat := 0

end AKR
end UrfCore
