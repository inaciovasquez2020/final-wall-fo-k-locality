# ATLAS.003 — Dropping FO^k locality breaks T_LG witness compilation

- Target statement: LG.HOOK.Compilation
- Dropped assumption: FO^k locality / EF^k locality compilation hypothesis
- Witness kind: non-local observable (global property)
- Minimal description:
  - Permit an observable that depends on a global property not determined by any bounded-radius neighborhoods (e.g., a property requiring unbounded radius or global aggregation).
  - Then no bounded-patch FO^k formula φ supported on ≤B radius-R patches can compile the witness.
- Verification method:
  - Necessity witness: locality is required for patch-supported compilation.
