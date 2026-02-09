# T_LG Composition Law

## Lemma LG.THM.Composition  (proved)
Let (k,Δ,R,B) be fixed. Suppose we have m transfer instances I_1,...,I_m such that:

1. Each I_j satisfies the T_LG template with local witness supported on ≤ B_j patches of radius R,
2. Each I_j produces a global consequence G_j with constant witness c_j>0 in meta/constants.yaml,
3. The instances are executed under the same jurisdiction assumptions (in particular URF.AX.Admissibility when required).

Define the disjoint-union patch budget:
B_total := Σ_{j=1}^m B_j.

Then there exists a composed instance I_* supported on ≤ B_total patches with global consequence:
G_* := ⋂_{j=1}^m G_j
and constant witness:
c_* := min_{1≤j≤m} c_j.

In particular, for ED-type bounds:
(∀j, ED ≥ c_j · H_j) ⇒ ED ≥ (min_j c_j) · (min_j H_j).

## Dependency hooks
Uses: LG.HOOK.Glue; jurisdiction inheritance; constant-min rule.
