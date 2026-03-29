import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Fin.Basic

namespace URF.XOR

open scoped BigOperators

/--
Concrete K₄ XOR row system over ℤ₂.

Vertices: Fin 4
Each row is a parity equation over edges incident to a vertex.
-/
abbrev V := Fin 4
abbrev F2 := ZMod 2

/-- An edge indicator (i,j) with i < j encoded symmetrically. -/
def edge (i j : V) : F2 :=
  if h : i = j then 0 else 1

/-- Row corresponding to vertex v: sum of incident edges mod 2. -/
def row (v : V) : F2 :=
  ∑ u : V, edge v u

/-- The full K₄ XOR row system: exactly four rows. -/
def ChronosK4Rows : Fin 4 → F2
| v => row v

/-- Sanity check: each row is well-defined in ℤ₂. -/
theorem ChronosK4Rows_well_defined (v : V) :
  ChronosK4Rows v = ∑ u : V, edge v u := rfl

/--
Closure property used by Regression Test E:
the sum of all rows vanishes in ℤ₂.
-/
theorem sum_rows_zero :
  (∑ v : V, ChronosK4Rows v) = 0 := by
  -- each unordered edge counted exactly twice
  simp [ChronosK4Rows, row, edge, Fin.sum_univ_eq]()

