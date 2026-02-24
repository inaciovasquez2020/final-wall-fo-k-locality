import Mathlib

open Finset

variable {V : Type} [DecidableEq V]
variable (adj : V → Finset V)

def vertexBoundary (S : Finset V) : Finset V :=
  S.bind (fun v => (adj v).filter (fun u => u ∉ S))

lemma vertexBoundary_subset_neighbors (S : Finset V) :
  vertexBoundary adj S ⊆ S.bind adj := by
  intro x hx
  simpa [vertexBoundary] using hx


import Mathlib.Data.Finset.Basic
import Mathlib.Data.Fintype.Basic

open scoped BigOperators

namespace URF

variable {V : Type} [DecidableEq V]
variable (E : V → V → Prop)
variable [DecidablePred (fun p : V × V => E p.1 p.2)]

def vertex_boundary (S : Finset V) : Finset V :=
S.filter (fun v => ∃ u : V, E v u ∧ u ∉ S)

lemma mem_vertex_boundary {S : Finset V} {v : V} :
  v ∈ vertex_boundary (E := E) S
    ↔ v ∈ S ∧ ∃ u : V, E v u ∧ u ∉ S := by
  simp [vertex_boundary]

end URF