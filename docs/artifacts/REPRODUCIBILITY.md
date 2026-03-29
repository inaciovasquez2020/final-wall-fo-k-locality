# Unified Rigidity Framework — Reproducibility Artifacts

## Purpose
Provide a clear record of computational, formal, and documentation artifacts
supporting results in the URF ecosystem.

## Artifact Categories

### 1. Formal Verification
Lean modules formalizing definitions and structural lemmas.

Typical locations:
- lean/
- formal/

### 2. Computational Experiments
Scripts and datasets used to explore rigidity phenomena.

Typical locations:
- scripts/
- experiments/
- toolkit/

Outputs include:
- JSON result files
- plots
- experiment summaries

### 3. Documentation
Expository materials explaining framework structure.

Typical locations:
- docs/examples
- docs/referee
- docs/roadmap
- docs/open_problems

### 4. Versioning
Each artifact should reference:

- repository commit hash
- experiment configuration
- script version

## Reproducibility Protocol

To reproduce experiments:

1. clone repository
2. install dependencies
3. run scripts in `scripts/` or `toolkit/`
4. compare outputs with stored result files

## Goal
Ensure results associated with the URF framework are transparent,
verifiable, and reproducible.

