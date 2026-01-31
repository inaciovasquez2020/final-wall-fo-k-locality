# Unified Rigidity Framework (URF) — Core  
**Deterministic Verification of Local→Global Structural Stability**

[![Status: Core Closed](https://img.shields.io/badge/Status-Core%20Closed-blue?style=flat-square)](#current-status)  
[![ORCID: 0009-0008-8459-3400](https://img.shields.io/badge/ORCID-0009--0008--8459--3400-lightgrey?style=flat-square)](https://orcid.org/0009-0008-8459-3400)

---

## Scope

This repository is a **Tier A module** in the **Scientific Infrastructure (URF)**.  
It contains the **core execution and verification layer** of the Unified Rigidity Framework.

It hosts:
- machine-verifiable operator instances,
- spectral gap witnesses,
- JSON certification artifacts,
- deterministic verification standards.

No speculative or experimental theory is developed here.  
All content is frozen, versioned, and externally auditable.

---

## Significance Statement: The URF Closure

The **Unified Rigidity Framework (URF)** resolves a central obstruction in Finite Model Theory:  
the inability of bounded-variable local logic ($FO^k$) to enforce global structural stability in the presence of expander phenomena.

### Why This Matters

**Computational Determinism**  
By establishing the **Logic–Width Dependency** ($k \ge f(tw)$), URF identifies the exact threshold where local homogeneity forces global rigidity.

**Machine-Verifiable Proof Objects**  
URF replaces narrative proofs with **formal operator certificates**, enabling deterministic verification of structural claims.

**Engineering Relevance**  
Any information-bearing system satisfying URF admissibility conditions becomes:
- certifiably stable,
- locally testable,
- globally rigid by construction.

---

## Core Mathematical Pillars

### 1. The Expander Obstruction

Local logical equivalence fails to bound global invariants on spectral expanders.  
Rigidity emerges only when operator systems are isolated from expander regimes via bounded structural width.

### 2. Law 3 — Spectral Rigidity Wall

A system is **URF-rigid** iff:

\[
\inf \mathrm{Spec}(\Delta_H \mid \ker(\mathrm{Per})^\perp) > 0
\]

This spectral gap is the **operational proof-of-rigidity**.

---

## Verified Artifacts (Law 3 Witnesses)

All instances below are audited against the **URF-SG Standard** and stored as machine-verifiable JSON.

| Artifact ID | Operator System | Metric | Status |
|------------|------------------|--------|--------|
| **EXT-1** | Heisenberg Nilmanifold | Gap ≥ \(4\pi\) | Verified |
| **EXT-2** | Ornstein–Uhlenbeck | Gap = 1.0 | Verified |

### Instance Files

- `instances/EXT-1-Heisenberg.json`  
- `instances/EXT-2-Ornstein-Uhlenbeck.json`

These files are first-class scientific objects:
- globally addressable,
- versioned,
- cryptographically auditable.

---

## Reproducibility

All verification is deterministic.

To inspect a witness:

```bash
cat instances/EXT-1-Heisenberg.json
