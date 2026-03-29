import Mathlib
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Fintype.Basic

open Finset
open scoped BigOperators

variable {V : Type} [DecidableEq V]

/-- Adjacency given as a finitary neighborhood map. -/
variable (adj : V → Finset V)

/-- Vertex boundary defined via adjacency lists. -/
def vertexBoundary (S : Finset V) : Finset V :=
  S.bind (fun v => (adj v).filter (fun u => u ∉ S))

lemma vertexBoundary_subset_neighbors (S : Finset V) :
  vertexBoundary adj S ⊆ S.bind adj := by
  intro x hx
  simpa [vertexBoundary] using hx

namespace URF

/-- Adjacency given as a binary relation. -/
variable (E : V → V → Prop)
variable [DecidablePred (fun p : V × V => E p.1 p.2)]

/-- Vertex boundary defined relationally. -/
def vertex_boundary (S : Finset V) : Finset V :=
  S.filter (fun v => ∃ u : V, E v u ∧ u ∉ S)

lemma mem_vertex_boundary {S : Finset V} {v : V} :
  v ∈ vertex_boundary (E := E) S
    ↔ v ∈ S ∧ ∃ u : V, E v u ∧ u ∉ S := by
  simp [vertex_boundary]

end URF
