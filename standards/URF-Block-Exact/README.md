# URF Block-Exact Spectral Gap Rigidity (v1.0)

## Scope
This standard replaces informal “stability/robustness under small perturbations” claims by a checkable operator criterion for a fixed spectral gap.

## Data
- Self-adjoint operator A on Hilbert space H with compact resolvent.
- Consecutive isolated eigenvalues λ_k < λ_{k+1}.
- Eigenspaces E_k, E_{k+1} with spectral projections Π_k, Π_{k+1}.
- Combined projection Π := Π_k + Π_{k+1} onto E_k ⊕ E_{k+1}.
- Symmetric A-bounded perturbation V.
- Perturbed operator H(ε) := A + ε V.
- Gap γ_k(ε) := λ_{k+1}(ε) − λ_k(ε).

## Block-Exact Audit Criterion
### Rigid (second-order gap stability)
Π V Π = 0  ⇒  |γ_k(ε) − γ_k(0)| = O(ε^2).

### Generic non-rigid (linear gap variation)
Π V Π ≠ 0  ⇒  for a residual set of such perturbations, |γ_k(ε) − γ_k(0)| = Θ(|ε|).

## Required Replacement Rule (Global)
Any statement of the form “the gap/rigidity/stability is preserved under small perturbations” MUST be rewritten by specifying (A, V, E_k, E_{k+1}) and verifying Π V Π = 0 (rigid) or recording Π V Π ≠ 0 (generic non-rigid).

## Claim Types (Drop-in)
- Claim type 1 (rigid): Assume Π V Π = 0. Then the gap is second-order rigid.
- Claim type 2 (generic non-rigid): If Π V Π ≠ 0, then for a residual set of V, the gap varies linearly.

## Status
Version: v1.0

