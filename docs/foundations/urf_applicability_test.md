# URF Applicability Test (URF-AT)

## Status

**Frozen — Canonical Scope Gate**

The URF Applicability Test (URF-AT) is a mandatory front-door test that determines
whether a claim, object, or verification task falls within the regime where the
Unified Rigidity Framework (URF) applies.

URF-AT is not a theorem, proof, or verifier.
It is a *regime membership test*.

No URF verification, certificate, or NO witness is valid unless the associated
claim has an explicit URF-AT classification.

---

## Purpose

URF is a framework for certifying **global claims under finite local information
and bounded capacity**.

URF-AT answers the prior question:

> *Is this claim even of the type where URF reasoning is applicable?*

This prevents:
- overreach,
- misapplication,
- category errors,
- and post-hoc reinterpretation of results.

---

## Input

URF-AT is evaluated on a **claim context**, consisting of:

- the object or system under study,
- the form of refinement, observation, or computation,
- the asserted conclusion (local or global),
- and the information flow model (explicit or implicit).

---

## The Test

URF-AT evaluates the following four conditions.

### (A) Locality Regime

**Question:**  
Is the system accessed or refined only through bounded-radius, bounded-width,
or otherwise local observations?

Examples:
- local neighborhoods in graphs or factor graphs,
- bounded-width logical refinements,
- finite-radius measurements,
- locality-restricted update rules.

**Fail condition:**  
Unrestricted global access, oracle access, or instantaneous nonlocal inspection.

---

### (B) Capacity Regime

**Question:**  
Is the information revealed per step, per locality unit, or per refinement stage
bounded independently of the global system size?

Examples:
- O(1) or polylogarithmic information per step,
- bounded transcript alphabets,
- finite-state or bounded-memory processes.

**Fail condition:**  
Unbounded information extraction in a single step.

---

### (C) Accounting Regime

**Question:**  
Is there a well-defined notion of cumulative information, entropy, transcript
capacity, or refinement cost?

Examples:
- EntropyDepth,
- transcript capacity,
- cumulative distinguishability,
- certified information flow accounting.

**Fail condition:**  
No meaningful way to sum or bound information gained across steps.

---

### (D) Global Claim Regime

**Question:**  
Is the claim asserting a *global determination*, *global uniqueness*, or
*global certainty*?

Examples:
- determining a full satisfying assignment,
- certifying global rigidity or non-existence,
- asserting total classification or resolution.

**Fail condition:**  
Purely exploratory, heuristic, or local descriptive claims.

---

## Outcomes

URF-AT yields exactly one of the following classifications.

### ✅ URF-APPLICABLE

All four regimes (A–D) are satisfied.

URF verification, admissibility checks, certificates, and NO witnesses apply
fully and unconditionally.

---

### ⚠️ URF-CONDITIONAL

Locality and capacity hold, but accounting or claim scope is partial,
approximate, or weakened.

URF results apply **only under explicitly stated conditions**, which must be
labeled and preserved downstream.

---

### ❌ URF-NOT-APPLICABLE

One or more core regimes fail.

URF must not be applied.
No URF certificate or NO witness is meaningful in this regime.

---

## Enforcement Rule

Every URF artifact MUST declare its URF-AT status:

- in documentation,
- in certificates,
- and in verifier output (if applicable).

Artifacts lacking a declared URF-AT classification are **out of scope by default**.

---

## Relationship to URF-ADMISSIBLE

URF-AT precedes URF-ADMISSIBLE.

- **URF-AT** answers: *Does URF apply at all?*
- **URF-ADMISSIBLE** answers: *Is the claim valid under URF rules?*

Passing URF-AT is a prerequisite for admissibility checks.

---

## Non-Scope

URF-AT does not judge:
- truth or falsity,
- usefulness,
- novelty,
- or importance.

It judges **only applicability**.

---

## Design Principle

URF-AT is intentionally conservative.

If applicability is unclear, the correct classification is **URF-CONDITIONAL**
or **URF-NOT-APPLICABLE**, not URF-APPLICABLE.

This protects the integrity of the framework.

