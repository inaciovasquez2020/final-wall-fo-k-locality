# URF-SG: Symmetry Analysis — Toroidal Grid with Chords

Base graph:
Vertices: (i,j) ∈ Z_n × Z_n
Edges:
- nearest neighbors (up, down, left, right)
- plus fixed chord edges (definition below)

Chord model:
Assume chords connect:
(i,j) → (i+k, j+k) mod n
for fixed k.

---

## Baseline symmetry (no chords)

Automorphism group:
G0 = (Z_n × Z_n) ⋊ D4

Actions:
- translations
- rotations
- reflections

---

## With chords

Chord edges break:
- most rotations
- some reflections

Remaining symmetries:
- all translations
- possibly one reflection (if k symmetric)

Thus:
G ≈ Z_n × Z_n   (pure translation group)
or
G ≈ (Z_n × Z_n) ⋊ Z_2

Exact G must be checked.

---

## Task

Determine:
Does any nontrivial rotation/reflection preserve chord edges?

If NO:
G = Z_n × Z_n (abelian)

If YES:
G = (Z_n × Z_n) ⋊ Z_2

