URF Core
Canonical Foundational Logic Layer for the Unified Rigidity Framework
Role
Foundational mathematics and logic layer of the URF program.
Defines axioms, reductions, invariant structure, and primitive certificate semantics.
Does not provide packaging, CI orchestration, or executable distribution bundles.
Repository Guarantees
Mathematical soundness of stated axioms and reductions (conditional components explicitly labeled).
Deterministic certificate semantics at the logical layer.
Stable primitive interfaces consumed by downstream prefab and infrastructure layers.
This Repository Provides
Core axiom system (URF Axiom series and invariant definitions).
Formal reduction statements linking rigidity, capacity, locality, and admissibility.
Proof skeletons and formalization entry points (Lean, LaTeX, and certificate logic).
Primitive certificate semantic definitions (structure, meaning, and validity conditions).
Canonical reference definitions used by prefab schemas and verifiers.
Status
Canonical foundational layer.
Active development permitted only for mathematical or logical closure.
Downstream compatibility preserved via semantic version discipline.
Dependency Structure
Upstream Dependencies: None at semantic level.
Downstream Consumers:
URF Prefab System (packaging, schemas, deterministic verifier wiring).
Scientific Infrastructure (execution environment, reproducibility, CI standardization).
Application Repositories (domain implementations and certification consumers).
Explicit Non Scope
Executable prefab bundles.
CI pipeline definitions.
Container or environment reproducibility specifications.
End user deployment workflows.
Experimental or draft packaging structures.
Scope Boundaries
Mathematical invariants and admissibility logic.
Certificate meaning and logical validity rules.
Reduction structure and obstruction statements.
Formal proof architecture and theorem organization.
Interfaces Exported
Certificate semantic specification.
Invariant and admissibility logic definitions.
Formal theorem reference identifiers.
Lean formalization entry modules.
Compatibility Contract
Prefab layer must not alter semantic meaning of certificates defined here.
Infrastructure layer must not redefine logical validity rules.
Downstream layers may only extend by instantiation, never by semantic override.
References
URF Prefab System
https://github.com/inaciovasquez2020/urf-prefab-system
Scientific Infrastructure
https://github.com/inaciovasquez2020/scientific-infrastructure
Research Website
https://www.vasquezresearch.com
Documentation Navigation
Framework overview
https://inaciovasquez2020.github.io
Project index
https://inaciovasquez2020.github.io/vasquez-index
Scientific infrastructure environment
https://inaciovasquez2020.github.io/scientific-infrastructure
Citation
If you use foundational URF logic or reductions, cite:
@manual{Vasquez_URF_Core_2026,
author = {Vasquez, Inacio F.},
title = {urf-core: Foundational Logic for the Universal Reference Frame},
year = {2026},
url = {https://github.com/inaciovasquez2020/urf-core}
}
Layer Relationship Summary
Core defines truth conditions and invariant structure.
Prefab defines frozen executable packaging of Core outputs.
Infrastructure defines environment and reproducibility envelope.
Governance Rule
Any change that alters logical meaning of certificates or invariants must occur in Core first and propagate downstream via versioned release.
