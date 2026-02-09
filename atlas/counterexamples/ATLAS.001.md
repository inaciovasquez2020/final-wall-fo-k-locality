# ATLAS.001 — Dropping Admissibility breaks VCDI jurisdiction

- Target statement: URF.THM.VCDI
- Dropped assumption: URF.AX.Admissibility
- Witness kind: global preprocessing / global algebraic move
- Minimal description:
  - Allow an algorithm to perform a non-refinement global transformation (e.g., solve/encode via global algebraic preprocessing)
  - This exits the step-bounded refinement regime and invalidates the transcript-capacity accounting that yields VCDI.
- Verification method:
  - Regime separation: witness is classified as global_algebraic, hence outside VCDI jurisdiction.
- References:
  - URF.NOTE.RegimeSeparation
