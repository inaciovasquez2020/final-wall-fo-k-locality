# final-wall-fo-k-locality

## Status (2026)

This repository records the resolution of the FO^k locality wall.
The results here are conditionally complete, relying on Configuration
Pumping as an explicit axiom. EF Cycle–Linkage and related locality traps
are retired. No claims are made here regarding XYSTEM or the Clause
Contraction Lemma (CCL), which are tracked independently in urf-axioms.

Canonical repository for **FOᵏ locality definitions and structural invariants** used in the *Final Wall* program.

This repository isolates and formalizes the **notion of first‑order k‑locality** as a dependency layer. It contains *definitions only*, plus strictly local structural lemmas where unavoidable. It is not a claim repository and not a proof of rigidity.

---

## Role in the program

FOᵏ locality is the logical substrate underlying overlap rigidity, WLᵏ indistinguishability, and configuration saturation arguments. This repository provides a **single source of truth** for those locality notions.

```
mathlib / finite model theory
        ↓
final-wall-fo-k-locality   (this repo)
        ↓
overlap-rigidity / counterexamples / conditionals / manuscripts
```

Any statement invoking FOᵏ locality must be compatible with the definitions fixed here.

---

## Scope

This repository formalizes:

* FOᵏ syntax (k‑variable first‑order formulas)
* Local satisfaction relative to bounded neighborhoods
* FOᵏ local types and neighborhood equivalence
* Structural locality invariants usable by downstream arguments

The emphasis is on **definitional precision**, not theorem proving.

---

## What this repository is

* A **definitional layer** for FOᵏ locality
* A dependency for rigidity, obstruction, and entropy arguments
* A normalization point ensuring consistent use of locality concepts

## What this repository is not

* A proof of Gaifman locality or Hanf normal forms
* A classification of FOᵏ expressive power
* A repository of rigidity theorems

Those results live outside this layer.

---

## Repository structure

```
.
├── src/
│   ├── FO_k/
│   │   ├── Syntax.lean        # k‑variable syntax
│   │   ├── Semantics.lean     # satisfaction and structures
│   │   ├── Locality.lean      # bounded‑radius locality
│   │   └── Types.lean         # FOᵏ local types
│   └── Main.lean
├── tests/
│   └── sanity.lean            # minimal build checks
├── lake.toml
├── lake-manifest.json
├── STATUS.md
└── README.md
```

File naming may evolve, but **the semantic contract will not**.

---

## Build requirements

* Lean version pinned in `lake.toml`
* mathlib as resolved by `lake-manifest.json`

No external tooling is required.

---

## Build and verification

To build:

```bash
lake build
```

Optional sanity checks:

```bash
lake test
```

A clean build is the sole correctness criterion at this layer.

---

## Stability and versioning

* Definitions in this repository are **API‑stable**
* Any breaking change requires:

  * a version tag
  * an explicit downstream migration note

The default branch is intended to remain usable as a long‑term dependency.

---

## Downstream usage

Typical dependency declaration:

```lean
require foKLocality from git
  "https://github.com/inaciovasquez2020/final-wall-fo-k-locality" @ "<tag>"
```

Downstream projects are expected to:

* state and prove their own theorems
* treat these definitions as fixed

---

## Relationship to adjacent repositories

* Used by `overlap-rigidity-lean` for formal rigidity arguments
* Referenced by `final-wall-conditional-index` for dependency disclosure
* Tested against `overlap-rigidity-counterexamples`

No downstream work may redefine FOᵏ locality independently.

---

## Status

* Layer: **definitional / structural**
* Claims: **none**
* Proofs: **none** (beyond trivial locality lemmas)
* Authority: **canonical for FOᵏ locality**

See `STATUS.md` for coverage notes.

---

## License

MIT (or compatible permissive license).

---

## Integrity note

Locality errors propagate silently. This repository exists to ensure that **every use of FOᵏ locality refers to the same object** everywhere in the program.

If a claim depends on FOᵏ locality, it depends on this layer.
