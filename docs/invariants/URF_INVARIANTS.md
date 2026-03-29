# Unified Rigidity Framework — Core Invariants

## Purpose
Document the principal invariants used across the URF ecosystem and how
they function in rigidity arguments.

## Primary Invariants

### Local Configuration Type (FO^k)
The logical type determined by the radius-R neighborhood of a vertex under
k-variable first-order logic.

Denoted:
type_R^k(v)

Role:
Measures local indistinguishability of configurations.

---

### Cycle–Overlap Rank (COR_R)
A structural quantity measuring the complexity of overlapping cycles in
bounded-radius neighborhoods.

Role:
High cycle-overlap rank forces diversification of local logical types.

---

### EntropyDepth (ED)
A lower bound on the number of refinement steps required to eliminate
configuration ambiguity in a local inference system.

Role:
Captures information-theoretic limits of refinement algorithms.

---

### Capacity Bound
A constraint on the amount of information that can be transmitted during
each refinement step.

Role:
Prevents rapid global reconstruction from purely local information.

---

## Interaction of Invariants

Locality constraint
        ↓
Capacity bound
        ↓
Limited refinement power
        ↓
Structural rigidity
        ↓
Global obstruction

---

## Usage Across Repositories

urf-core  
Defines invariant concepts and formal problem structure.

urf-spine  
Establishes structural relationships between invariants.

chronos-urf-rr  
Empirically explores invariant behavior in graph experiments.

urf-textbook  
Provides exposition and worked examples.

