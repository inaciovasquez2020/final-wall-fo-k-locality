# Escape Classification and Chronos Integration

## Purpose

This note records the canonical *escape routes* from fixed-radius local
computation identified after the resolution of the Unified Capacity–Locality
Problem (UCLP), and explains how the UCLP lower bound plugs into the
Chronos / EntropyDepth framework.

---

## Escape Classification (Canonical)

Given a fixed-radius local transcript model, any solver that avoids the
UCLP lower bound must exit the regime via one of the following routes.
Each route corresponds to a chargeable resource in URF.

### A. Radius Escape
- **Mechanism:** allow the locality radius r to grow with n.
- **Resource:** locality parameter r(n).
- **Effect:** neighborhoods cease to be tree-like; local bounds no longer apply.

### B. Bandwidth / Memory Escape
- **Mechanism:** keep r fixed but store large global summaries over time.
- **Resource:** transcript capacity TC.
- **Effect:** violates bounded-capacity admissibility.

### C. Global Invariant Oracle Escape
- **Mechanism:** compute a global invariant in one or few steps.
- **Resource:** global-call cost (or charged into TC).
- **Effect:** leaves local refinement; invokes nonlocal operators.

### D. Coordination Escape
- **Mechanism:** nonlocal communication among distributed agents.
- **Resource:** communication bandwidth / synchronization cost.
- **Effect:** effective observation becomes global.

### E. Model / Task Escape
- **Mechanism:** weaken the output requirement (decision-only, approximation).
- **Resource:** residual entropy H(X | S_m).
- **Effect:** changes the solved task; yields graded lower bounds.

### F. Preprocessing Escape
- **Mechanism:** heavy global preprocessing before local steps.
- **Resource:** preprocessing transcript capacity TC_prep.
- **Effect:** must be charged or the model is inconsistent.

These exhaust the admissible ways to bypass fixed-radius locality in URF.

---

## Plug-in to Chronos / EntropyDepth

Let T = (S_t) be a transcript and X the target witness.

### Information Accounting
- Total information required:  H(X).
- Transcript capacity:  TC(T) = Σ I(X; S_t | S_{t-1}).

For the explicit SAT family resolving UCLP:
- H(X) = Θ(n) unconditionally.
- Any transcript that determines X satisfies  TC(T) ≥ H(X) = Θ(n).

### Chronos Ceiling
Chronos supplies a per-step ceiling:
I(X; S_t | S_{t-1}) ≤ C(n)
for the admissible regime (e.g., C(n)=O(1) or polylog(n)).

### Depth Lower Bound
By chaining:
TC(T) ≤ m · C(n)  and  TC(T) ≥ H(X)
implies
m ≥ H(X) / C(n).

Hence:
- If C(n)=O(1), then m = Ω(n).
- If C(n)=polylog(n), then m = Ω(n / polylog(n)).

### On Ω(n log n)
An Ω(n log n) bound requires an additional ingredient (e.g., diffusion or
non-amplification) that raises the required target functional beyond H(X)=Θ(n).
No such strengthening is claimed here.

---

## Governance

- UCLP is **resolved (NO)** for an explicit constant-width SAT family.
- This document classifies all legitimate escape routes and their costs.
- Status: **CANONICAL REFERENCE**.

