Title: Worked Example of Linear EntropyDepth

Instance:
A bounded-degree 2-SAT instance consisting of a chain of implications:
x1 → x2 → x3 → … → xn

Propagation:
Unit propagation can only infer xi+1 after xi is fixed.
Each refinement step resolves exactly one new variable.

EntropyDepth:
After t steps, only variables {x1,…,xt} are fixed.
Global solution requires n steps.

Conclusion:
EDA = Θ(n) for this frozen instance under any AC0-local solver.

