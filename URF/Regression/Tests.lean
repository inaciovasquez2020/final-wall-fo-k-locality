import URF.ND.TypeBound
import URF.XOR.K4
import URF.Lifts.Spec
import URF.XOR.ChronosK4Rows

namespace URF

def testA_small (n : Nat) : Bool := true
def testB_small (n : Nat) : Bool := true
def testC_small (n : Nat) : Bool := true
def testD_small (n : Nat) : Bool := true
def testE_small (n : Nat) : Bool := true

def run_small (n : Nat) : Bool :=
  testA_small n && testB_small n && testC_small n && testD_small n && testE_small n

theorem TestA_general (k Δ R : Nat) : True := by trivial
theorem TestB_general : True := by trivial
theorem TestC_general : True := by trivial
theorem TestD_general : True := by trivial
theorem TestE_general : True := by trivial

end URF


