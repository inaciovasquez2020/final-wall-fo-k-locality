# External Status Lock

Date: 2026-04-27

Status: **ACTIVE_CONDITIONAL_FRONTIER**

Scope:

FO^k locality/frontier artifact. No unconditional final theorem closure is claimed unless proved in the repository.

Boundary:

- Axioms, admits, `sorry`, placeholder witnesses, string witnesses, dashboards, ledgers, and narrative wrappers are not theorem proofs.
- CI/build success means the checked surface compiles or verifies; it does not upgrade conditional mathematics into theorem-level closure.
- Any result depending on an axiom, admit, `sorry`, synthetic placeholder, or explicitly named missing lemma is conditional.
- This repository must not be described as proving a Clay problem, RH, P vs NP, BSD, Hodge, Navier--Stokes, Yang--Mills, Collatz, Goldbach, twin primes, or ABC unless the proof is present without assuming the target theorem.

Allowed public description:

- executable artifact;
- conditional reduction;
- certified frontier;
- audit/status infrastructure;
- exposition or dashboard;
- finite verification surface.

Forbidden public description:

- unconditional final proof;
- solved Millennium Prize problem;
- theorem-level closure from assumed axioms;
- machine-checked proof when the central theorem depends on `axiom`, `admit`, `sorry`, or a tautological witness.
