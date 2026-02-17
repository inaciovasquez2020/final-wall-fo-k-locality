# Unified Capacity–Locality Problem (UCLP)

## Status
**Canonical formulation (normalized)**  
All definitions are explicit. No implicit models, resources, or oracles.

---

## 1. Informal statement

The Unified Capacity–Locality Problem asks whether a computational task can be
performed by a **local refinement process** whose **per-step information gain**
is uniformly bounded, while still achieving a required **global separation**
or decision.

The problem isolates the minimal obstruction shared by locality-based
algorithms across models (RAM, circuits, TMs) once compiled into a common
refinement transcript.

---

## 2. Computational model (Reasonable)

### Definition 2.1 (Reasonable models)
A model of computation is **Reasonable** if it satisfies all of the following:

1. Polynomial-time bounded (uniform).
2. Compilable into a finite transcript of refinement steps.
3. Each step produces a bounded-description local update.
4. No hidden global oracle or unbounded preprocessing outside the transcript.

Examples:
- Logspace-uniform circuits
- Polynomial-time RAM
- Polynomial-time Turing machines

Non-examples:
- Models with unbounded advice
- Global algebraic solvers not representable as refinement steps

---

## 3. Transcript formalism

### Definition 3.1 (Refinement transcript)
A **refinement transcript** is a sequence
\[
T = (S_0, S_1, \dots, S_m)
\]
where each transition \(S_{t-1} \to S_t\) is a local, bounded-radius update
computed by a Reasonable model.

### Definition 3.2 (Transcript capacity)
Let \(X\) be the hidden target (e.g. satisfying assignment).
The **transcript capacity** is
\[
\mathrm{TC}(T) := \sum_{t=1}^m I(X ; S_t \mid S_{t-1}).
\]

This quantity measures the total information extracted by the process.

---

## 4. Locality constraint

### Definition 4.1 (Locality bound)
A transcript is **\(r\)-local** if each refinement step depends only on an
\(r\)-radius neighborhood of the current state representation.

The locality bound \(r\) is fixed independently of input size.

---

## 5. Admissibility

### Definition 5.1 (URF-admissible)
A task is **URF-admissible** if there exists a Reasonable algorithm whose
compiled transcript satisfies:

1. Fixed locality radius \(r = O(1)\).
2. Per-step information gain bounded by
   \[
   I(X ; S_t \mid S_{t-1}) \le C
   \]
   for a constant \(C\).
3. Total runtime polynomial in input size.

---

## 6. The decision problem

### UCLP (Decision Form)

**Instance:**  
A computational task \(\mathcal{P}\) (e.g. SAT on a specified distribution).

**Question:**  
Does there exist a URF-admissible transcript solving \(\mathcal{P}\)?

---

## 7. Obstruction principle

### Principle 7.1 (Capacity–Locality obstruction)
If any solution of \(\mathcal{P}\) requires
\[
\mathrm{TC}(T) \ge \Omega(f(n))
\]
for superconstant \(f(n)\), then no URF-admissible algorithm exists for
\(\mathcal{P}\).

This obstruction is invariant under compilation between Reasonable models.

---

## 8. Consequences

- Local refinement algorithms are fundamentally capacity-limited.
- Increasing power requires violating locality, bounded information gain,
  or Reasonable compilation.
- Hardness results reduce to lower-bounding transcript capacity.

---

## 9. Relation to other frameworks

- **FO\(^k\) / WL\(^k\):** locality-restricted refinement instances.
- **EntropyDepth / Chronos:** quantitative lower bounds on \(\mathrm{TC}(T)\).
- **Oblivion Atom:** structural source of unavoidable capacity growth.

---

## 10. Canonical form

This document defines the **single formal decision problem** underlying
capacity-locality limits. All variants must reduce to UCLP to be comparable.

No additional assumptions are permitted unless stated explicitly.
