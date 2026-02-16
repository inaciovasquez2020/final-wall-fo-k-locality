Local-Refinement Completeness for SAT (LR-Completeness)

Statement.
If SAT has a polynomial-time algorithm in M_reasonable,
then SAT has a polynomial-time local refinement algorithm
with bounded radius and bounded width.

Preprocessing.
Clause-variable incidence, ordering, and wiring are compiled
into the initial configuration.
All preprocessing cost is charged to transcript capacity TC.

Reduction.
Given any polytime SAT solver A in M_reasonable,
apply the Normalization / Sandbox Theorem to obtain a
local refinement system R_A deciding SAT_n.

Conclusion.
Any impossibility result for polynomial-time local refinement
algorithms applies to all polynomial-time algorithms in
M_reasonable.

