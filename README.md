# Unified Rigidity Framework (URF Core)
**Version:** 2026.01-alpha  
**Status:** Core Mathematically Closed | Spectral Gap Externally Verified

[![Research Dashboard](https://img.shields.io/badge/Status-Mathematically_Closed-b31b1b)](https://inaciovasquez2020.github.io/vasquez-index/dashboard.html)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0008--8459--3400-A6CE39)](https://orcid.org/0009-0008-8459-3400)

## Overview
Executable verification artifacts for the **Unified Rigidity Framework (URF)**. This repository hosts the formal standards, schemas, and verification tools for spectral-gap rigidity and finite-capacity invariants. 

The URF establishes the conditions under which local homogeneity within a system forces global deterministic rigidity, effectively resolving the Local→Global problem outside of the **Expander Obstruction**.

---

## External Certification (Verified Witnesses)

The **URF_law3** (Spectral Gap Rigidity) is externally verified on non-artificial, real-operator systems. These witnesses confirm intrinsic spectral rigidity:

### EXT-1 (Geometric)
**Heisenberg nilmanifold horizontal sub-Laplacian** The spectral gap is bounded by the period kernel:
$$\lambda_1(\Delta_H \mid \ker(\mathrm{Per})^\perp) \ge 4\pi > 0$$

### EXT-2 (Statistical Physics)
**Ornstein–Uhlenbeck operator on $L^2(\mathbb{R},\gamma)$** Standardized witness of system stability:
$$\lambda_1(\Delta_H \mid \ker(\mathrm{Per})^\perp) = 1 > 0$$

---

## Technical Regimes & Closure

The mathematical core of the URF is now **closed**. Stability is guaranteed across the following regimes:

* **Bounded Treewidth:** Resolved via Logic-Width Dependency $k \ge f(tw)$.
* **Subexponential Growth:** Verified via deterministic audit.
* **Expander Exclusion:** Isolated as the unique obstruction set $\mathcal{O} = \{\text{Expanders}\}$.

## Repository Structure
* `/standards`: Formal JSON schemas (e.g., `URF-SG`, `URF-Block-Exact`).
* `/instances`: Registry of certified graph instances and witness data.
* `/audit`: Automated verification logs and build-state hashes.
* `/docs`: Manuscripts regarding the **Expander Exclusion Axiom**.

## External Links
* **Academic Index:** [inaciovasquez2020.github.io/vasquez-index/](https://inaciovasquez2020.github.io/vasquez-index/)
* **Artifact Dashboard:** [Live Verification Dashboard](https://inaciovasquez2020.github.io/vasquez-index/dashboard.html)

---
© 2026 Inacio F. Vasquez — Independent Research Program. 
*Remaining uncertainty is non-mathematical (institutional uptake).*
