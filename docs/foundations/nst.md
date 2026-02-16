Normalization / Sandbox Theorem (NST)

Statement.
For every logspace-uniform circuit family A deciding SAT in time T(n),
there exists a bounded-radius, bounded-width local refinement system R_A
such that:

1. R_A decides SAT_n
2. T_{R_A}(n) <= poly(T(n))
3. TC(R_A) <= polylog(n) * TC(A)

Construction.
A is compiled into uniform evaluation layers.
Each layer corresponds to one refinement step operating on a bounded-radius
neighborhood of the configuration graph.
All global wiring and preprocessing is charged to the transcript capacity.

Baseline.
This establishes normalization from logspace-uniform circuits to local
refinement systems with explicit transcript accounting.

