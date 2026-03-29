# Unified Rigidity Framework — System Architecture

## Purpose
Provide a structural overview of the URF ecosystem and how the repositories
fit together conceptually and technically.

## Repository Architecture

urf-core
Defines the foundational axioms, invariants, and problem structure.

urf-spine
Contains canonical lemmas, invariant relationships, and structural results.

chronos-urf-rr
Implements computational experiments and reference measurements for
EntropyDepth and rigidity behavior.

urf-textbook
Provides pedagogical exposition, worked examples, and narrative structure
for the framework.

## Conceptual Layers

Layer 1 — Definitions
Basic objects: locality, capacity, refinement systems.

Layer 2 — Invariants
Rigidity invariants and structural measurements.

Layer 3 — Structural Lemmas
Results linking invariants to structural consequences.

Layer 4 — Main Theorems
Global obstructions derived from local constraints.

Layer 5 — Applications
Connections to complexity, graph theory, and dynamical systems.

## Data and Artifact Flow

Experiments (chronos-urf-rr)
        ↓
Structural analysis (urf-spine)
        ↓
Formal definitions (urf-core)
        ↓
Exposition and synthesis (urf-textbook)

## Goal
Provide a coherent architecture for exploring limits of inference under
locality and finite information capacity.

