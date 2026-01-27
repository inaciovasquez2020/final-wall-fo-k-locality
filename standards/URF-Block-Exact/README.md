# URF-Block-Exact Standard

This directory contains the **URF-Block-Exact** standard — a JSON schema and normative description of the block-exact criterion used across the Unified Rigidity Framework (URF).

The block-exact criterion formalizes the notion of exactness under perturbation in spectral problems:  
an operator block that projects to zero corresponds to quadratic sensitivity, whereas nonzero leads to linear perturbative effects.

## Standard Contents

- `schema.json` — canonical JSON Schema v1.0 for URF-Block-Exact certificates  
- `examples/` — example certificates conforming to the schema  
- `checks/` — verification scripts for example certificates

## Canonical Criterion

Formally, the block-exact standard asserts:

\[
\Pi V \Pi = 0 \iff |\,\gamma_k(\varepsilon)-\gamma_k(0)\,| = O(\varepsilon^2),
\]
\[
\Pi V \Pi \neq 0 \Rightarrow |\,\gamma_k(\varepsilon)-\gamma_k(0)\,| = \Theta(|\varepsilon|),
\]

where:
- \(\Pi\) is a projection onto a subspace of interest,
- \(V\) is a bounded perturbation,
- \(\gamma_k(\varepsilon)\) is an eigenvalue branch of an admissible spectral problem.

This rule is mechanically checkable using the JSON schema and verification tooling.

## Usage

To validate a certificate against this standard:

1. Install `jsonschema`:
   ```sh
   pip install jsonschema
