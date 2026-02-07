import Mathlib.Data.Fin.Basic
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.List.Perm
import Mathlib.Data.Nat.Basic

namespace URF.Lifts

open scoped BigOperators

/--
Deterministic permutation lift on a finite type α.

Construction:
• Enumerate α via Fintype.elems
• Rotate the list by (seed mod card)
• Convert the rotated list into a permutation
-/
structure PermutationLift (α : Type) [Fintype α] where
  seed : Nat
  perm : Equiv.Perm α

namespace Deterministic

variable {α : Type} [Fintype α] [DecidableEq α]

/-- Canonical list of elements of α. -/
def elems : List α :=
  Fintype.elems α

lemma elems_nodup : (elems : List α).Nodup :=
  Fintype.elems_nodup α

lemma elems_complete : ∀ x : α, x ∈ elems :=
  Fintype.complete _

/-- Rotate list by k positions (mod length). -/
def rotate (k : Nat) (l : List α) : List α :=
  let n := l.length
  if h : n = 0 then l
  else
    let k' := k % n
    (l.drop k') ++ (l.take k')

lemma rotate_perm (k : Nat) :
  rotate k elems ~ elems := by
  classical
  unfold rotate
  by_cases h : elems.length = 0
  · simp [h]
  · simp [h]
    exact (List.perm_drop_append_take _ _)

/-- Deterministic permutation induced by seed. -/
def permOfSeed (seed : Nat) : Equiv.Perm α :=
by
  classical
  refine
    (Equiv.ofBijective
      (fun x =>
        (rotate seed elems).get
          ⟨(elems.indexOf x),
           by
             have hx : x ∈ elems := elems_complete x
             have hlen : elems.indexOf x < elems.length :=
               List.indexOf_lt_length.2 hx
             simpa [rotate, hlen]⟩)
      ?_)
  classical
  constructor
  · intro a b h
    have : elems.indexOf a = elems.indexOf b := by
      simpa using congrArg Subtype.val h
    exact List.indexOf_injective elems_nodup this
  · intro y
    refine ⟨
      (rotate seed elems).get
        ⟨(rotate seed elems).indexOf y,
         List.indexOf_lt_length.2
           (by
             have : y ∈ rotate seed elems := by
               have := elems_complete y
               exact (rotate_perm seed).mem_iff.mp this
             simpa)⟩,
      ?_⟩
    simp

/-- Package into PermutationLift. -/
def mk (seed : Nat) : PermutationLift α :=
  ⟨seed, permOfSeed seed⟩

end Deterministic

end URF.Lifts

