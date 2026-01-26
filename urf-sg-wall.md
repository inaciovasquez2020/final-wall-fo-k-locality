# URF Spectral Gap Rigidity Wall

## Status
Core unresolved structural lemma of the Unified Rigidity Framework (URF).

This file contains **no heuristic stability claims**.
All statements are governed by the Block-Exact standard.

---

## 1. Problem Statement (Block-Exact Form)

Let:

- \( H \) be a Hilbert space.
- \( \Delta_H : H \to H \) be a self-adjoint operator with compact resolvent.
- \( \mathrm{Per} \subset H \) be a distinguished finite-dimensional subspace.
- Consider the restricted operator:
  
  \[
  A := \Delta_H \mid \ker(\mathrm{Per})^\perp
  \]

Let:

- \( \lambda_k < \lambda_{k+1} \) be two consecutive isolated eigenvalues of \( A \).
- \( E_k, E_{k+1} \) their eigenspaces.
- \( \Pi := \Pi_{E_k \oplus E_{k+1}} \) the combined spectral projection.

Let \( V \) range over the class of **URF-admissible perturbations**:
- symmetric,
- \( A \)-bounded,
- compatible with the combinatorial / geometric structure defining \( H \).

Define the perturbed operator:
\[
A(\varepsilon) := A + \varepsilon V
\]

and the spectral gap:
\[
\gamma_k(\varepsilon) := \lambda_{k+1}(\varepsilon) - \lambda_k(\varepsilon)
\]

---

## 2. Block-Exact Wall

The Spectral Gap Rigidity Wall is the decision problem:

> **For the operator \( A = \Delta_H \mid \ker(\mathrm{Per})^\perp \) and all URF-admissible perturbations \( V \), determine whether**
>
> \[
> \Pi V \Pi = 0
> \]
> **holds identically.**

This is the entire wall.

No other formulation is valid inside URF.

---

## 3. Consequences (By URF-Block-Exact Standard)

By the Block-Exact standard:

### Rigid case
If:
\[
\Pi V \Pi = 0 \quad \text{for all admissible } V
\]

then:
\[
|\gamma_k(\varepsilon) - \gamma_k(0)| = O(\varepsilon^2)
\]

for all sufficiently small \( \varepsilon \).

---

### Non-rigid case
If:
\[
\exists V \text{ admissible such that } \Pi V \Pi \neq 0
\]

then generically:
\[
|\gamma_k(\varepsilon) - \gamma_k(0)| = \Theta(|\varepsilon|)
\]

and no rigidity theorem holds.

---

## 4. Known Results

The block-exact criterion has been evaluated in the following regimes:

### Proven rigid
- Trees
- Bounded treewidth graphs
- Finite covers of trees
- Any structure where admissible \( V \) preserves a full block symmetry

### Open
- Deterministic high-cycle-overlap graphs
- Cycle expanders
- Hypergraph gadget limits
- Any URF instance with dense local overlap geometry

---

## 5. What This Is *Not*

This wall is:

- not a question about smallness of \( V \),
- not about positivity of \( V \),
- not about smoothness of \( V \),
- not about analytic perturbation theory.

It is **only** about:

\[
\Pi V \Pi \stackrel{?}{=} 0
\]

---

## 6. Operational Form

The wall can be tested mechanically:

Input:
- matrix representation of \( A \)
- matrix representation of \( V \)
- eigenvalue index \( k \)

Compute:
- eigenvectors for \( \lambda_k, \lambda_{k+1} \)
- projection \( \Pi \)
- norm \( \|\Pi V \Pi\| \)

Output:
- 0 → rigid
- >0 → non-rigid

---

## 7. URF Interpretation

All URF rigidity results reduce to this invariant.

There is no higher-level obstruction.
There is no additional spectral phenomenon.
There is no hidden analytic difficulty.

The Spectral Gap Rigidity Wall is exactly:

> **Does the admissible perturbation class force a nontrivial action on the two-dimensional spectral block or not?**

---

## 8. Audit Status

This file is governed by:

- `standards/URF-Block-Exact/README.md`
- `URF-AUDIT.md`

No statement here is allowed to bypass the block-exact criterion.

---

## 9. Research Frontier

All remaining theoretical work in URF concerning spectral rigidity is now:

- representation theory,
- symmetry classification,
- combinatorial structure of admissible \( V \),
- geometry of \( H \) inducing unavoidable block mixing.

This is no longer spectral analysis.
This is structural mathematics.

