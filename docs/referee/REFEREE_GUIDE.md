# URF Referee Guide

## Purpose
Provide referees with a concise map of the Unified Rigidity Framework (URF),
its core invariants, and the dependency structure of the results.

## Core Idea
URF studies limits of refinement and inference processes under locality
and finite information capacity.

The guiding principle is:

Locality + bounded information transfer ⇒ structural rigidity.

## Canonical Dependency Chain

Definitions  
↓  
Rigidity / Capacity Invariant  
↓  
Structural Lemma  
↓  
Main Theorem  
↓  
Applications

## Key Objects

- Local configuration types (FO^k neighborhoods)
- Cycle overlap rank / structural complexity
- EntropyDepth lower bounds
- Capacity limits on refinement processes

## What Each Repository Provides

urf-core  
Foundational definitions and axioms of the framework.

urf-spine  
Canonical invariants and structural lemmas.

chronos-urf-rr  
Reference implementation and experiments for EntropyDepth and rigidity.

urf-textbook  
Expository presentation of the framework and examples.

## Reading Order

1. Worked example (docs/examples)
2. Core invariant definitions
3. Structural lemma
4. Main theorem
5. Applications

## Intended Contribution

The framework proposes a structural mechanism explaining why certain
refinement or inference processes cannot achieve global reconstruction
under locality constraints.

## Reproducibility

Artifacts included:

- Lean formalization modules
- computational experiments
- documentation and dependency maps

