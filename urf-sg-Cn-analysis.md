# URF-SG: Cycle Graph C_n

Base operator:
A = graph Laplacian on C_n.

Symmetry group:
G = D_n (dihedral group).

Irreducible representations:
All eigenmodes are 1D or 2D real irreps of D_n.

Spectrum:
λ_k = 2 - 2 cos(2πk/n).

Each eigenspace E_k has:
- dimension 2 for k ≠ 0, n/2
- dimension 1 for k = 0, n/2

Key fact:
For any consecutive nontrivial gap (E_k, E_{k+1}),
the representation E_k ⊕ E_{k+1} decomposes as a sum
of two non-isomorphic irreps of D_n.

Therefore:
Hom_G(E_k ⊕ E_{k+1}, E_k ⊕ E_{k+1}) = C · I

Hence:
Π V Π = 0 for all admissible V.

Conclusion:
Cycle graphs are rigid under URF-SG admissible perturbations.

