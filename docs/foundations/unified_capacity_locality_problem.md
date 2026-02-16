# The Unified Capacity–Locality Problem

## Problem Statement

Consider any oracle-free, uniform, polynomial-time computation.

## Question

Is it true that every such computation admits a simulation by a process that:

1. Operates only on bounded-radius local state
2. Injects at most polylogarithmic information per step
3. Has total progress (entropy reduction or structural refinement) bounded by total injected information

## Equivalent Formulation

Is global computational progress universally limited by local information capacity?

## Significance

A **positive** answer implies:
- Local refinement is complete for polynomial-time computation
- EntropyDepth is a universal obstruction
- Superlinear entropy lower bounds imply \( \mathrm{P} \neq \mathrm{NP} \)

A **negative** answer implies:
- Existence of irreducibly global polynomial-time computation
- Failure of locality as a fundamental principle of computation
- Breakdown of information-accounting limits

Either resolution forces a foundational revision of complexity theory.

---

# CutStrings (Canonical URF Primitive)

## Definition

**CutStrings** is a uniform process that partitions an input string into substrings according to a fixed, uniform cut rule.
The process operates sequentially and emits substrings based on a deterministic rule applied at each step.

## URF Admissibility

### URF-ADMISSIBLE case

If cut indices are part of the uniform input encoding or depend only on bounded local counters (e.g. position modulo a constant), then CutStrings satisfies:
- locality radius \( O(1) \),
- per-step injected information \( O(\log n) \),
- valid progress accounting.

### NOT URF-ADMISSIBLE case

If cut selection depends on a global predicate of the input (e.g. parity, global checksum, or any nonlocal property), then CutStrings violates URF locality and capacity constraints.

## Certified Witnesses

- **YES witness:** locality radius \( O(1) \); injected information per step \( O(\log n) \); total progress bounded by cumulative injected information.
- **NO witness:** a single-step cut decision depending on a global predicate requires locality radius \( \Omega(n) \), yielding a certified violation of URF condition (A) and, when formalized, condition (B).

## Purpose

CutStrings is a minimal separating primitive between:
- locally streamable structure, and
- irreducibly global control logic.

It serves as a canonical benchmark object for:
- testing URF locality and capacity constraints,
- generating certified NO instances,
- enforcing information-accounting discipline in the URF framework.

## Relationship to URF-ADMISSIBLE

URF-ADMISSIBLE is the decision interface that determines whether a given process respects bounded locality, bounded information injection, and valid progress accounting.

CutStrings provides:
- a concrete **YES** instance demonstrating admissibility under purely local control, and
- a concrete **NO** instance demonstrating failure under global control.

These instances anchor the abstract statements of the Unified Capacity–Locality Problem in explicit, verifiable artifacts.

## Status

- URF-ADMISSIBLE is defined as a total decision predicate.
- The Unified Capacity–Locality Problem concerns the universal quantifier over all polynomial-time computations.
- CutStrings is a frozen, canonical benchmark primitive for this program.
