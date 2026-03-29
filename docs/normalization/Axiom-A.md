Title: Axiom A — Bounded Update Normalization

Status: Candidate axiom (unproven)

Statement:
For every deterministic polynomial-time algorithm A deciding SAT,
there exists a simulation whose state evolution can be expressed
as a sequence of local updates with uniformly bounded fan-in,
but without assuming FO^k definability.

Meaning:
Axiom A asserts bounded update algebra only.
It does not assume logical locality or refinement semantics.

Failure mode:
Violation requires a single update step that creates
Ω(n) new independent dependencies.

