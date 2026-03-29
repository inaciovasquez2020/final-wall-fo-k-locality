Title: Candidate Counterexample to Axiom A

Construction:
Gaussian elimination over F2 with dynamic pivoting.

Observation:
Single elimination steps may create Θ(n) new linear dependencies
in one update, violating bounded update algebra.

Status:
This falsifies Axiom A unless update granularity is artificially
restricted.

Consequence:
TRAP does not follow from Axiom A alone.

