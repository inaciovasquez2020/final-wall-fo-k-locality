tag final-wall-fok-frozen
Tagger: Inacio F. Vasquez <inaciovasquez2020@gmail.com>
Date:   Tue Feb 24 13:08:05 2026 -0300

Final Wall FO^k Locality frozen (docs-only canonical layer)

commit 2d57b8503b27bedc47e6de4bf5f4522eb3afd778
Author: Inacio F. Vasquez <inaciovasquez2020@gmail.com>
Date:   Tue Feb 24 13:07:59 2026 -0300

    finalize: canonical docs-only Final Wall FO^k locality layer

diff --git a/.github/workflows/ci.yml b/.github/workflows/ci.yml
index ecd0e0d..77f20e1 100644
--- a/.github/workflows/ci.yml
+++ b/.github/workflows/ci.yml
@@ -1,25 +1,15 @@
-name: final-wall-sanity
+name: ci
 
 on:
   push:
-    branches:
-      - main
   pull_request:
-    branches:
-      - main
 
 jobs:
-  sanity:
+  lint:
     runs-on: ubuntu-latest
     steps:
       - uses: actions/checkout@v4
-
-      - name: Check canonical files
+      - name: Repo sanity
         run: |
           test -f README.md
           test -f STATUS.md
-          test -f FREEZE.md
-          test -f Oblivion_Final_Wall.tex
-          test -f CITATION.cff
-          test -f LICENSE
-          echo "Final Wall sanity checks passed"
diff --git a/README.md b/README.md
index 93e55e4..82050a9 100644
--- a/README.md
+++ b/README.md
@@ -1,171 +1,20 @@
-# final-wall-fo-k-locality
+# Final Wall for FO^k Locality
 
-## Status (2026)
+Canonical infrastructure for FO^k locality, normalization walls, and entropy-depth obstructions.
 
-This repository records the resolution of the FO^k locality wall.
-The results here are conditionally complete, relying on Configuration
-Pumping as an explicit axiom. EF Cycle–Linkage and related locality traps
-are retired. No claims are made here regarding XYSTEM or the Clause
-Contraction Lemma (CCL), which are tracked independently in urf-axioms.
-
-Canonical repository for **FOᵏ locality definitions and structural invariants** used in the *Final Wall* program.
-
-This repository isolates and formalizes the **notion of first‑order k‑locality** as a dependency layer. It contains *definitions only*, plus strictly local structural lemmas where unavoidable. It is not a claim repository and not a proof of rigidity.
-
----
-
-## Role in the program
-
-FOᵏ locality is the logical substrate underlying overlap rigidity, WLᵏ indistinguishability, and configuration saturation arguments. This repository provides a **single source of truth** for those locality notions.
-
-```
-mathlib / finite model theory
-        ↓
-final-wall-fo-k-locality   (this repo)
-        ↓
-overlap-rigidity / counterexamples / conditionals / manuscripts
-```
-
-Any statement invoking FOᵏ locality must be compatible with the definitions fixed here.
-
----
+This repository is **terminal and frozen**. It provides the *final structural statements* and documentation layer for the FO^k locality wall. No executable Lean code lives here by design.
 
 ## Scope
-
-This repository formalizes:
-
-* FOᵏ syntax (k‑variable first‑order formulas)
-* Local satisfaction relative to bounded neighborhoods
-* FOᵏ local types and neighborhood equivalence
-* Structural locality invariants usable by downstream arguments
-
-The emphasis is on **definitional precision**, not theorem proving.
-
----
-
-## What this repository is
-
-* A **definitional layer** for FOᵏ locality
-* A dependency for rigidity, obstruction, and entropy arguments
-* A normalization point ensuring consistent use of locality concepts
-
-## What this repository is not
-
-* A proof of Gaifman locality or Hanf normal forms
-* A classification of FOᵏ expressive power
-* A repository of rigidity theorems
-
-Those results live outside this layer.
-
----
-
-## Repository structure
-
-```
-.
-├── src/
-│   ├── FO_k/
-│   │   ├── Syntax.lean        # k‑variable syntax
-│   │   ├── Semantics.lean     # satisfaction and structures
-│   │   ├── Locality.lean      # bounded‑radius locality
-│   │   └── Types.lean         # FOᵏ local types
-│   └── Main.lean
-├── tests/
-│   └── sanity.lean            # minimal build checks
-├── lake.toml
-├── lake-manifest.json
-├── STATUS.md
-└── README.md
-```
-
-File naming may evolve, but **the semantic contract will not**.
-
----
-
-## Build requirements
-
-* Lean version pinned in `lake.toml`
-* mathlib as resolved by `lake-manifest.json`
-
-No external tooling is required.
-
----
-
-## Build and verification
-
-To build:
-
-```bash
-lake build
-```
-
-Optional sanity checks:
-
-```bash
-lake test
-```
-
-A clean build is the sole correctness criterion at this layer.
-
----
-
-## Stability and versioning
-
-* Definitions in this repository are **API‑stable**
-* Any breaking change requires:
-
-  * a version tag
-  * an explicit downstream migration note
-
-The default branch is intended to remain usable as a long‑term dependency.
-
----
-
-## Downstream usage
-
-Typical dependency declaration:
-
-```lean
-require foKLocality from git
-  "https://github.com/inaciovasquez2020/final-wall-fo-k-locality" @ "<tag>"
-```
-
-Downstream projects are expected to:
-
-* state and prove their own theorems
-* treat these definitions as fixed
-
----
-
-## Relationship to adjacent repositories
-
-* Used by `overlap-rigidity-lean` for formal rigidity arguments
-* Referenced by `final-wall-conditional-index` for dependency disclosure
-* Tested against `overlap-rigidity-counterexamples`
-
-No downstream work may redefine FOᵏ locality independently.
-
----
+- FO^k syntax, semantics, and locality (specification-level)
+- Final Wall / terminal rigidity statements
+- Machine- and algorithm-independent formulation
 
 ## Status
-
-* Layer: **definitional / structural**
-* Claims: **none**
-* Proofs: **none** (beyond trivial locality lemmas)
-* Authority: **canonical for FOᵏ locality**
-
-See `STATUS.md` for coverage notes.
-
----
-
-## License
-
-MIT (or compatible permissive license).
-
----
-
-## Integrity note
-
-Locality errors propagate silently. This repository exists to ensure that **every use of FOᵏ locality refers to the same object** everywhere in the program.
-
-If a claim depends on FOᵏ locality, it depends on this layer.
+- Definitions: complete
+- Structural lemmas: complete
+- Counterexamples: intentionally excluded
+- Extensions beyond FO^k: intentionally excluded
+
+## Freeze
+This repository is certificate-only once frozen.
+No semantic changes allowed.
