# URF Core — Foundational Logic Layer

Canonical foundational logic repository for the **Unified Rigidity Framework (URF)**.

This repository defines the **mathematical, logical, and certificate-semantic base** of the URF program. All downstream executable, packaging, and environment layers derive their meaning from this layer.

---

## URF-ADMISSIBLE (v1.0)

**URF-ADMISSIBLE** is the frozen decision interface enforcing **locality, capacity, and accounting**. All URF claims must pass this gate or provide a certified **NO** witness.

* Spec: `docs/foundations/urf_admissible_spec.md`
* Schemas: `admissible/schema/`
* NO Benchmarks: `admissible/no_benchmarks/`

---

## Purpose

To provide the canonical source of:

* URF axioms and invariant definitions
* Formal reduction theorems and obstruction statements
* Primitive certificate semantics (meaning and validity conditions)
* Formal proof-architecture entry points (Lean, LaTeX, logical certificates)

This repository is the **semantic authority** for URF correctness.

---

## Layer Position

**URF Layer Stack**

```
Core → Prefab → Infrastructure → Applications
```

* **Core** defines truth conditions and invariant structure.
* **Prefab** freezes executable realizations of Core outputs.
* **Infrastructure** provides reproducible execution environments.
* **Applications** consume certified logic.

---

## Canonical Scope

Structural laws governing admissible strategies are indexed in
[docs/foundations/structural_laws_index.md](docs/foundations/structural_laws_index.md).

### Mathematical Foundations

* Rigidity principles
* Capacity–locality constraints
* Admissibility and invariant structure
* EntropyDepth and Chronos structural reductions

### Certificate Semantics

* Logical validity rules
* Certificate meaning definitions
* Structural admissibility interpretation
* Primitive schema semantics (not packaging format)

### Proof Architecture

* Lean formalization entry points
* Reduction skeletons
* Conditional closure boundaries (explicitly labeled)

---

## Structural Invariants

* Structural invariants and recurring constraints: [docs/foundations/structural-laws.md](docs/foundations/structural-laws.md)

This reference records **derived structural invariants** that recur across URF components. These are not physical laws, but invariant constraints under explicit locality, capacity, and admissibility assumptions.

---

## Explicit Non-Scope

This repository intentionally does **not** provide:

* CI packaging or pipeline orchestration
* Frozen prefab bundles
* Container or environment reproducibility layers
* End-user execution tooling
* Deployment workflows

These belong to the **Prefab** or **Infrastructure** layers.

---

## Dependencies

* **Semantic dependencies:** None
* **Mathematical dependencies:** Standard mathematical foundations only

### Downstream Consumers

* URF Prefab System
  [https://github.com/inaciovasquez2020/urf-prefab-system](https://github.com/inaciovasquez2020/urf-prefab-system)

* Scientific Infrastructure
  [https://github.com/inaciovasquez2020/scientific-infrastructure](https://github.com/inaciovasquez2020/scientific-infrastructure)

---

## Stability Model

**Status:** Canonical Foundational Layer

**Change Rules:**

* Mathematical meaning changes must originate here
* Downstream layers must not redefine certificate semantics
* Conditional components must remain explicitly labeled
* Versioning follows semantic mathematical compatibility

---

## Formal Interfaces Exported

Core exports:

* Certificate semantic definitions
* Invariant and admissibility logic
* Formal theorem reference identifiers
* Lean formalization modules
* Logical validity boundary definitions

---

## References

* Framework Overview
  [https://inaciovasquez2020.github.io](https://inaciovasquez2020.github.io)

* Project Index
  [https://inaciovasquez2020.github.io/vasquez-index/](https://inaciovasquez2020.github.io/vasquez-index/)

* Scientific Infrastructure Environment
  [https://inaciovasquez2020.github.io/scientific-infrastructure/](https://inaciovasquez2020.github.io/scientific-infrastructure/)

* Research Website
  [https://www.vasquezresearch.com](https://www.vasquezresearch.com)

---

## Relationship to Prefab Layer

**Prefab Layer Responsibilities:**

* Freeze executable schema realizations
* Provide deterministic verifiers
* Provide CI reproducible bundles
* Provide importable prefab logic modules

Core remains the **semantic authority**.

---

## Citation

If you use URF foundational logic or reductions, cite:

```bibtex
@manual{Vasquez_URF_Core_2026,
  author = {Vasquez, Inacio F.},
  title  = {URF Core: Foundational Logic Layer for the Unified Rigidity Framework},
  year   = {2026},
  url    = {https://github.com/inaciovasquez2020/urf-core}
}
```

---

## Quickstart (60 seconds)

```bash
./scripts/urf verify demo
```

URF applies only to **post-hoc certification of asserted results**. It is unnecessary for exploratory or provisional work and does not govern discovery, intuition, or consensus formation. It provides a voluntary, artifact-based mechanism to make consequential claims auditable.

