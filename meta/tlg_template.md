# Canonical Local→Global Transfer Template  (T_LG)

## Parameters
- Logic: FO^k
- Degree bound: Δ
- Radius: R
- Patch budget: B
- Local observable class: 𝒪_{k,R}  (FO^k-definable on radius-R neighborhoods)
- Global target: invariant / lower bound (e.g., ED, time, capacity)

## Inputs (Local Witness)
A local witness consists of:
1. Structures A,B on the same vertex set (or coupled distribution) and a set of patches Π = {P_1,...,P_m}, m ≤ B
2. An FO^k sentence φ supported on ⋃Π such that:
   - A ⊨ φ and B ⊭ φ   (or vice versa)
3. Support certificate:
   - Each P_i induces radius-R neighborhoods with degree ≤ Δ
   - Boundary interface types recorded (FO^k-type on ∂P_i)

## Transfer Claim (Global Consequence)
Given the local witness, produce one of:

### (T_LG.1) Capacity / EntropyDepth
∃ constant c=c(k,Δ,R,B)>0 such that:
- ED ≥ c · H_target
or
- T ≥ c · H_target / C_step

### (T_LG.2) Dual witness / parity witness (if applicable)
∃ bounded-support global witness w supported in ⋃Π such that:
- χ_w separates histories / distributions
- bias(χ_w) ≥ c

### (T_LG.3) Invariant obstruction
∃ global invariant I with:
- |I(A) − I(B)| ≥ c
and I is computable / lower-bounded from transcript constraints.

## Output Bundle (Deterministic)
- Local witness object (φ, Π, boundary types)
- Transfer map proof reference (lemma IDs)
- Extracted constant row(s) in meta/constants.yaml
- DAG edges added in meta/deps.yaml

## Required Lemma Hooks (IDs)
- LG.HOOK.Locality: FO^k localization for φ on patches
- LG.HOOK.Compilation: EF^k / logic witness ⇒ canonical local observable
- LG.HOOK.Capacity: transcript capacity bound
- LG.HOOK.Glue: patch union ⇒ global statement
