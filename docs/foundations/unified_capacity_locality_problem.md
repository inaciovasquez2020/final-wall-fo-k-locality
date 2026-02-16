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
