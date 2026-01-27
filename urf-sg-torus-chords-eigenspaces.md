# URF-SG: Eigenspace Decomposition — Toroidal Grid with Chords

Assume symmetry group:
G = Z_n × Z_n   (pure translations)
or
G = (Z_n × Z_n) ⋊ Z_2   (translations + one reflection)

---

## Case 1: G = Z_n × Z_n (abelian)

All irreducible representations are 1-dimensional:
χ_{a,b}(x,y) = exp(2πi(ax + by)/n)

Laplacian eigenfunctions:
f_{a,b}(x,y) = exp(2πi(ax + by)/n)

Eigenvalues:
λ_{a,b} = 4 - 2cos(2πa/n) - 2cos(2πb/n)
(modified slightly by chords)

Multiplicity:
Each (a,b) is distinct as a representation.

However:
λ_{a,b} = λ_{-a,-b}
⇒ spectral multiplicity ≥ 2 generically.

Thus:
E_k carries two copies of distinct characters.

Then:
E_k ⊕ E_{k+1} contains at least 4 independent 1D irreps.

Therefore:
dim End_G(E_k ⊕ E_{k+1}) ≥ 4

So:
Π V Π ≠ 0 is forced.

Rigidity collapses.

---

## Case 2: G = (Z_n × Z_n) ⋊ Z_2

Representations split into:
- symmetric modes
- antisymmetric modes

Multiplicity still ≥ 2 for generic eigenvalues.

Thus:
Trivial representation appears in End_G(E_k ⊕ E_{k+1})

Again:
Π V Π ≠ 0 generically.

---

## Conclusion

For toroidal grids with chords:

Pure translation symmetry forces
huge representation multiplicity.

Hence:
There exist admissible V with Π V Π ≠ 0.

The URF-SG rigidity wall fails
for torus-with-chords.

