
The Unified Capacity–Locality Problem
Problem Statement
Consider any oracle-free, uniform, polynomial-time computation.
Question
Is it true that every such computation admits a simulation by a process that:
Operates only on bounded-radius local state
Injects at most polylogarithmic information per step
Has total progress (entropy reduction or structural refinement) bounded by total injected information
Equivalently: is global computational progress universally limited by local information capacity?
Significance
A positive answer implies:
Local refinement is complete for polynomial-time computation
EntropyDepth is a universal obstruction
Superlinear entropy lower bounds imply P ≠ NP
A negative answer implies:
Existence of irreducibly global polynomial-time computation
Failure of locality as a fundamental principle of computation
Breakdown of information-accounting limits
Either resolution forces a foundational revision of complexity theory.
CutStrings (Canonical URF Primitive)
Definition
CutStrings is a uniform process that partitions an input string into substrings using a fixed, uniform cut rule.
URF Status
If cut indices are part of the uniform input encoding (or depend only on position counters), then CutStrings is URF-ADMISSIBLE.
If cut selection depends on a global predicate of the input (e.g. parity), CutStrings is NOT URF-ADMISSIBLE with a certified locality violation.
Witnesses
YES: locality radius O(1), per-step injected information O(log n), valid accounting
NO: single-step global cut selection requires radius Ω(n)
Purpose
CutStrings serves as a minimal separating example between locally streamable structure and irreducibly global control logic. It is used as a benchmark primitive for enforcing URF locality and capacity discipline.

# Unified Capacity–Locality Problem (UCLP)

## Problem Statement
Consider any oracle-free, uniform, polynomial-time computation.

**Question.**  
Does every such computation admit a simulation that:
1. **Operates on bounded-radius local state** (\(r = O(1)\));
2. **Injects at most polylogarithmic information per step** (\(O(\log n)\));
3. **Has total progress** (entropy reduction or structural refinement) **bounded by total injected information**?

## Equivalent Formulation
Is **global computational progress** universally limited by **local information capacity**?

---

## Consequences

### YES
- Local refinement is complete for polynomial-time computation.
- EntropyDepth is a universal obstruction.
- Superlinear entropy lower bounds imply \(P \neq NP\).

### NO
- There exist irreducibly global polynomial-time computations.
- Locality fails as a fundamental principle of computation.
- Information-accounting limits break down.

Either outcome forces a foundational revision of complexity theory.

---

## Canonical URF Primitive: CutStrings

### Definition
**CutStrings** is a uniform process that partitions an input string into substrings according to a fixed, deterministic cut rule.  
The process operates sequentially and emits substrings step by step.

---

## URF Admissibility

### URF-ADMISSIBLE (YES)
If cut indices are part of the uniform input encoding or depend only on bounded local counters (e.g., position modulo a constant), then:
- Locality radius: \(r = O(1)\);
- Per-step injected information: \(O(\log n)\);
- Progress accounting is valid.

### NOT URF-ADMISSIBLE (NO)
If cut selection depends on a global predicate of the input (e.g., parity, global checksum, or any nonlocal property), then:
- Required locality radius: \(r = \Omega(n)\);
- This yields a certified violation of URF locality (Condition A) and, when formalized, capacity/progress accounting (Condition B).

---

## Certified Witnesses

### YES Witness
A local update rule satisfying:
- \(r = O(1)\);
- Per-step injected information \(O(\log n)\);
- Total progress bounded by cumulative injected information.

### NO Witness
A single cut decision depending on a global predicate, forcing:
\[
r = \Omega(n),
\]
which certifies non-admissibility.

---

## Purpose
CutStrings is a minimal separating primitive between:
- **Locally streamable structure**, and
- **Irreducibly global control logic**.

It serves as a canonical benchmark for:
- Testing URF locality and capacity constraints;
- Generating certified NO instances;
- Enforcing information-accounting discipline within the URF framework.

---

## Decision Interface: URF-ADMISSIBLE
**URF-ADMISSIBLE** is a total decision predicate determining whether a process respects:
- Bounded locality;
- Bounded information injection;
- Valid progress accounting.

---

## Status
- URF-ADMISSIBLE is defined as a total predicate.
- The Unified Capacity–Locality Problem quantifies universally over all polynomial-time computations.
- **CutStrings** is frozen as a canonical benchmark primitive anchoring the framework in explicit, verifiable artifacts.

