# URF-SG: Toroidal Grid with Chords

Target structure:
2D torus Z_n × Z_n with added chord edges.

Base operator:
Graph Laplacian on the toroidal-chord graph.

Goal:
Determine whether Π V Π = 0 holds for all URF-admissible V.

---

## Symmetry group G

Baseline torus:
G0 = Z_n × Z_n ⋊ D4

With chords:
Global symmetry reduced to subgroup G ⊂ G0.

Exact G:
(TBD — must be computed explicitly)

---

## Eigenstructure

Laplacian spectrum:
λ(k,l) = 4 - 2 cos(2πk/n) - 2 cos(2πl/n)  (without chords)

Chords modify:
(TBD)

Multiplicity structure:
(TBD)

---

## Representation problem

Decompose:
E_k ⊕ E_{k+1} as a representation of G.

Question:
Does the trivial representation occur in:

Hom_G(E_k ⊕ E_{k+1}, E_k ⊕ E_{k+1}) ?

YES → ΠVΠ ≠ 0 possible → wall collapses  
NO  → ΠVΠ = 0 forced → rigidity survives  

---

## Status

Symmetry group: OPEN  
Representation decomposition: OPEN  
ΠVΠ verdict: OPEN

