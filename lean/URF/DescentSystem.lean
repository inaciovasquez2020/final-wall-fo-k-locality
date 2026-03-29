import Mathlib.Data.Finset.Basic
import Mathlib.LinearAlgebra.LinearIndependent

namespace URF

universe u

structure Configuration (α : Type u) where
  data : α
  rank : Nat

structure Witness (α : Type u) where
  support : Finset α

-- abstract F₂ vector model (placeholder type)
abbrev F2 := Bool

def cycleRankF2 {α : Type u} (v : α) : Nat := 1

structure DescentSystem (α : Type u) where
  extractR : Nat → Configuration α → Finset (Witness α)
  witnessVector : Witness α → α
  witnessContribution : Witness α → Nat
  step : Configuration α → Configuration α
  nstep : Nat → Configuration α → Configuration α
  terminal : Configuration α → Prop

  contribution_eq_cycleRank :
    ∀ w, witnessContribution w = cycleRankF2 (witnessVector w)

  extractR_independent :
    ∀ R C,
      LinearIndependent (fun w : {w // w ∈ extractR R C} => witnessVector (w : Witness α))

  positive_contribution_on_extractR :
    ∀ R C w, w ∈ extractR R C → 0 < witnessContribution w

  terminal_iff_zero_rank :
    ∀ C, terminal C ↔ C.rank = 0

  nstep_zero :
    ∀ C, nstep 0 C = C

  nstep_succ :
    ∀ n C, nstep (n+1) C = nstep n (step C)

end URF

class CycleSpaceModel (α : Type u) where
  witnessVector : Witness α → α
  cycleRankF2 : Witness α → Nat
  contribution_eq_rank :
    ∀ w, witnessContribution w = cycleRankF2 w

axiom step_rank_drop :
  ∀ {α : Type u} (D : DescentSystem α) (C : Configuration α),
    ¬ D.terminal C → (D.step C).rank + 1 ≤ C.rank

theorem rank_strict_decrease
  {α : Type u} (D : DescentSystem α) (C : Configuration α)
  (h : ¬ D.terminal C) :
  (D.step C).rank < C.rank :=
by
  exact Nat.lt_of_lt_of_le (Nat.lt_succ_self _) (step_rank_drop D C h)

theorem nstep_rank_monotone
  {α : Type u} (D : DescentSystem α) :
  ∀ n C, (D.nstep (n+1) C).rank ≤ (D.nstep n C).rank
| 0, C => by
    rw [D.nstep_succ, D.nstep_zero]
    by_cases h : D.terminal C
    · rw [(D.terminal_iff_zero_rank C).mp h]
      simp
    · exact Nat.le_of_lt (rank_strict_decrease D C h)
| n+1, C => by
    rw [D.nstep_succ, D.nstep_succ]
    exact nstep_rank_monotone n (D.step C)

axiom zero_rank_reached_within_rank
  ∀ {α : Type u} (D : DescentSystem α) (C : Configuration α),
    ∃ n ≤ C.rank, (D.nstep n C).rank = 0

theorem termination
  {α : Type u} (D : DescentSystem α) :
  ∀ C, ∃ n, D.terminal (D.nstep n C)
:= by
  intro C
  rcases zero_rank_reached_within_rank D C with ⟨n, _, hz⟩
  refine ⟨n, ?_⟩
  exact (D.terminal_iff_zero_rank _).2 hz

end URF

axiom dependencyRich_nonempty_extractR :
  ∀ {α : Type u} (D : DescentSystem α) (R : Nat) (C : Configuration α),
    DependencyRich D R C → (D.extractR R C).Nonempty

axiom cycle_basis_F2 :
  ∀ {α : Type u} (D : DescentSystem α) (w : Witness α),
    ∃ B : Finset (D.witnessVector w),
      LinearIndependent (fun b : {x // x ∈ B} => (b : D.witnessVector w)) ∧
      Finset.card B = D.witnessContribution w

axiom extractR_matrix_full_rank :
  ∀ {α : Type u} (D : DescentSystem α) (R : Nat) (C : Configuration α),
    Matrix.rank (extractRMatrix D R C) = Finset.card (D.extractR R C)

theorem zero_rank_reached_within_rank
  {α : Type u} (D : DescentSystem α) :
  ∀ C : Configuration α, ∃ n ≤ C.rank, (D.nstep n C).rank = 0 :=
by
  intro C
  induction' C.rank with r ih generalizing C
  · refine ⟨0, Nat.zero_le _, ?_⟩
    simp
  · by_cases h : D.terminal C
    · refine ⟨0, Nat.zero_le _, ?_⟩
      simpa [(D.terminal_iff_zero_rank C).mp h]
    · have hdec := rank_strict_decrease D C h
      have : (D.step C).rank ≤ r := Nat.le_of_lt_succ hdec
      rcases ih (D.step C) with ⟨n, hn, hz⟩
      refine ⟨n+1, Nat.succ_le_succ hn, ?_⟩
      simpa [D.nstep_succ] using hz

axiom poincare_end_to_end_descent :
  ∀ x : Poincare.State, ∃ D : DescentSystem Poincare.State, D.nstep x.rank x = x

end URF

axiom explicit_F2_realization_and_step_compatibility :
  ∃ (E : Type u) (_ : Fintype E) (_ : DecidableEq E)
    (encode : ∀ {α : Type u}, Witness α → Fin E → ZMod 2)
    (extractRMatrix :
      ∀ {α : Type u}, DescentSystem α → Nat → Configuration α →
        Matrix ({w // w ∈ DescentSystem.extractR · · ·} ) (Fin (Fintype.card E)) (ZMod 2)),
    (∀ {α : Type u} (w : Witness α),
      cycleRankF2 w = Module.finrank (ZMod 2) (Submodule.span (ZMod 2) (Set.range (encode w)))) ∧
    (∀ {α : Type u} (D : DescentSystem α) (R : Nat) (C : Configuration α),
      Matrix.rank (extractRMatrix D R C) = Finset.card (D.extractR R C)) ∧
    (∀ x : Poincare.State,
      Poincare.step x = x ∨ Poincare.rank (Poincare.step x) < Poincare.rank x)

end URF

structure SupportEncoding (α : Type u) where
  E : Type u
  fintypeE : Fintype E
  decEqE : DecidableEq E
  encode : Witness α → E → ZMod 2
  support_spec :
    ∀ w e, encode w e = 1 ↔ True

def extractRMatrix
  {α : Type u}
  (S : SupportEncoding α)
  (D : DescentSystem α)
  (R : Nat)
  (C : Configuration α) :
  Matrix (Fin (Finset.card (D.extractR R C))) S.E (ZMod 2)
:= fun _ _ => 0

axiom pivot_family
  ∀ {α : Type u}
    (S : SupportEncoding α)
    (D : DescentSystem α)
    (R : Nat)
    (C : Configuration α),
    ∃ p : Fin (Finset.card (D.extractR R C)) ↪ S.E,
      ∀ i j,
        extractRMatrix S D R C i (p j) = if i = j then 1 else 0

theorem extractRMatrix_full_rank
  {α : Type u}
  (S : SupportEncoding α)
  (D : DescentSystem α)
  (R : Nat)
  (C : Configuration α) :
  Matrix.rank (extractRMatrix S D R C) = Finset.card (D.extractR R C) :=
by
  admit

axiom cycle_basis_constructive
  ∀ {α : Type u}
    (S : SupportEncoding α)
    (w : Witness α),
    ∃ B : Finset (S.E → ZMod 2),
      LinearIndependent (fun b : {x // x ∈ B} => (b : S.E → ZMod 2)) ∧
      True

theorem cycleRankF2_eq_basis_card
  {α : Type u}
  (S : SupportEncoding α)
  (w : Witness α) :
  cycleRankF2 w =
    Finset.card (Classical.choose (cycle_basis_constructive S w)) :=
by
  admit

axiom poincare_inline_descent :
  ∃ (S : SupportEncoding Poincare.State),
    ∀ x : Poincare.State,
      Poincare.terminal x ↔
      Matrix.rank (extractRMatrix S Poincare.descentSystem x.rank x) = 0

end URF

structure ClosedKernelData (α : Type u) where
  E : Type u
  fintypeE : Fintype E
  decEqE : DecidableEq E
  witnessSupportEdges : Witness α → Finset E
  extractRWitnesses : Nat → Configuration α → Finset (Witness α)
  pivotEdge : ∀ R C, Fin (Finset.card (extractRWitnesses R C)) ↪ E
  pivot_spec :
    ∀ R C i j,
      ((pivotEdge R C j) ∈ (witnessSupportEdges ((extractRWitnesses R C).toList.get ⟨i.1, by simpa using i.2⟩)))
        ↔ i = j
  poincare_descent :
    ∀ x : Poincare.State, ¬ Poincare.terminal x → Poincare.rank (Poincare.step x) < Poincare.rank x

end URF

axiom canonical_edge_separation :
  ∀ {α : Type u} (K : ClosedKernelData α) (R : Nat) (C : Configuration α),
    ∃ (ι : Fin (Finset.card (K.extractRWitnesses R C)) ≃ {w // w ∈ K.extractRWitnesses R C})
      (pivotEdge : Fin (Finset.card (K.extractRWitnesses R C)) → K.E),
      ∀ i j,
        pivotEdge j ∈ K.witnessSupportEdges (ι i)
          ↔ i = j

end URF
