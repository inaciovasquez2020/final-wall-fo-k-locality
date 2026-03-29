# Structural Laws (Derived Invariants)
Chronos Strategy-Class Boundary (No-Go): admissible fixed-radius local refinement requires Ω(n) total transcript capacity when H(X)=Ω(n). See Chronos-EntropyDepth/docs/foundations/chronos_no_go_theorem.md.

This document records a small set of **structural invariants** that recur across
the Unified Rigidity Framework (URF) repositories and associated artifacts.

These statements are **not physical laws** and do not assert new empirical
regularities. Instead, they are **derived constraints**: limitations that apply
to any system satisfying the stated assumptions on locality, information
capacity, and admissibility.

They are included to:
- orient new users,
- prevent misinterpretation of scope,
- and provide a stable conceptual index for cross-domain reuse.

---

## Assumptions (Shared)

Unless otherwise stated, the laws below apply under some or all of the following
conditions:

- **Locality:** Information is accessed through bounded-radius or bounded-width
  observations.
- **Finite Capacity:** Each step of a process reveals at most a bounded amount
  of information.
- **Admissibility:** Processes respect explicit normalization, certification,
  and transcript constraints.
- **Determinacy Goal:** The objective is to determine or certify a global state,
  witness, or solution.

Concrete instantiations may strengthen or weaken these assumptions.

---

## Law 1: Capacity–Information Constraint

**Statement.**  
If a process reveals at most a bounded amount of information per step, then
resolving a global state with entropy \( H \) requires total information capacity
at least proportional to \( H \).

**Interpretation.**  
There is no admissible shortcut that extracts global information faster than
capacity allows.

**Instantiations.**
- Transcript Capacity (TC) lower bounds
- EntropyDepth (ED) lower bounds
- Constant mutual-information-per-step refinements

---

## Law 2: Locality–Global Separation

**Statement.**  
Local consistency under bounded locality does not imply global determinacy.

**Interpretation.**  
Inspecting all bounded-radius neighborhoods is insufficient to reconstruct or
certify the global structure.

**Instantiations.**
- UCLP(P) obstructions for constant-width SAT families
- FOᵏ locality limits
- Weisfeiler–Leman refinement obstructions
- Tree-local rank bounds in factor graphs

---

## Law 3: Non-Amplification of Information

**Statement.**  
No admissible refinement can reduce global uncertainty faster than permitted by
its information capacity.

**Interpretation.**  
Entropy cannot be collapsed by bookkeeping, reparameterization, or local
conditioning alone.

**Instantiations.**
- Failure of entropy martingales
- ED lower bounds under bounded locality
- Non-amplification lemmas in refinement processes

---

## Law 4: Verification–Generation Asymmetry

**Statement.**  
Under locality and capacity constraints, verification is strictly weaker than
generation.

**Interpretation.**  
The ability to check local conditions does not imply the ability to produce,
certify, or reconstruct a global object.

**Instantiations.**
- Necessity of global verifiers
- Admissibility certificates (AIV)
- Stress-test and adversarial validation infrastructure

---

## Law 5: Rigidity Under Local Constraint

**Statement.**  
Sufficiently strong local constraints coupled across a system induce global
rigidity.

**Interpretation.**  
Beyond a threshold, systems lose smooth degrees of freedom and admit only
discrete or rigid global configurations.

**Instantiations.**
- Cycle-local rigidity in graphs
- Spectral and WL-based obstructions
- Radiative rigidity in physical models
- Constraint locking in cosmological constructions

---

## Law 6: Admissibility Constraint (Meta-Law)

**Statement.**  
Only processes that explicitly account for locality, capacity, and normalization
are admissible explanations or algorithms.

**Interpretation.**  
Uncertified information flow is not an acceptable explanatory mechanism within
URF.

**Instantiations.**
- URF-ADMISSIBLE predicate
- AIV certificate schemas
- Prefab system normalization
- CI-enforced verifier pipelines

---

## Status

Each law above is supported by at least one **concrete, executable, or
machine-checkable instantiation** within the URF repository family.

This list is intended to be **stable**. New results should be recorded as
instantiations of existing laws unless a genuinely new invariant is identified.

---

## Scope Note

These laws constrain **what cannot be done** under the stated assumptions.
They do not assert optimality, completeness, or empirical truth beyond those
constraints.

