---
title: Infinity Wall (VCDI Instantiation)
status: non-conditional
scope: urf-core / admissibility / VCDI
---

## Objects

Let \(C_{\max}\in(0,\infty)\) be the per-step transcript capacity bound for a fixed admissible class \(\mathcal{A}\).

Let \((G_n)_{n\ge 1}\) be a family of connected \(d\)-regular graphs with \(d\ge 3\) and \(|V(G_n)|=n\).

Let \(P_n\) denote a URF-admissible refinement process on input instance \(G_n\), with entropy demand \(H(P_n)\) and entropy depth \(\mathrm{ED}(P_n)\).

## VCDI (Canonical)

Assume the Vasquez Capacity–Depth Inequality (VCDI) in canonical form:

\[
\forall P\in\mathcal{A},\qquad \mathrm{ED}(P)\ \ge\ \frac{H(P)}{C_{\max}}.
\]

## Instantiation A: Expander / High Cycle-Rank Families

Assume the family satisfies linear \(\mathbb{F}_2\)-cycle rank:

\[
I(G_n)\ :=\ \dim_{\mathbb{F}_2} Z_1(G_n)\ =\ \Theta(n).
\]

Define the entropy demand to include the cycle-parity uncertainty:

\[
H(P_n)\ \ge\ H\big(\text{uniform cycle-parity state on }Z_1(G_n)\big)\ =\ I(G_n).
\]

Hence:

\[
H(P_n)=\Theta(n).
\]

By VCDI:

\[
\mathrm{ED}(P_n)\ \ge\ \frac{H(P_n)}{C_{\max}}\ =\ \Theta(n).
\]

## Instantiation B: Random Lifts

Let \(G_n\) be a random \(n\)-lift of a fixed connected base graph \(B\) with minimum degree \(\ge 3\).
Then with high probability:

\[
\dim_{\mathbb{F}_2} Z_1(G_n)=\Theta(n),
\qquad
H(P_n)=\Theta(n),
\qquad
\mathrm{ED}(P_n)\ge \Theta(n).
\]

## Sharp Constant (Fixed Class)

If \(\mathcal{A}\) is defined so that each refinement step can reduce entropy by at most \(C_{\max}\):

\[
\forall P\in\mathcal{A},\ \forall t,\qquad \Delta H_t(P)\le C_{\max},
\]

then:

\[
\mathrm{ED}(P)\ \ge\ \frac{H(P)}{C_{\max}}.
\]

The factor \(1/C_{\max}\) is sharp in the sense that equality holds for processes with \(\Delta H_t(P)=C_{\max}\) for all steps \(t\) until termination.

## Separator: Minimal Global Invariant

Define the global invariant

\[
I(G)\ :=\ \dim_{\mathbb{F}_2} Z_1(G).
\]

Computability separation:

\[
I \text{ is computable by global aggregation,}
\qquad
I \text{ is not FO}^k\text{-local computable (fixed }k\text{).}
\]

Thus any regime that terminates by explicitly computing \(I(G_n)\) is non-URF (violates locality).

## Directed-Limit Dichotomy (Infinity Wall)

Let \((P_n)\) be a directed exhaustion with \(H(P_n)\uparrow\infty\). Under URF admissibility with finite capacity \(C_{\max}<\infty\):

\[
\lim_{n\to\infty}\mathrm{ED}(P_n)=\infty.
\]

Define \(P_\infty:=\varinjlim P_n\). Then:

\[
\mathrm{ED}(P_\infty)=\infty,
\]

i.e. the infinite object is rigid (non-terminating) in the admissible refinement regime.

## Classification Rule (Infinity Handling)

An “infinite” method that succeeds must exit URF by at least one of:

- Capacity violation: \(C_{\max}=\infty\) (unbounded transcript per step).
- Locality violation: uses global invariants (e.g., \(I(G)\), spectrum, global homology).

Otherwise (URF-admissible with \(C_{\max}<\infty\)), the infinity wall forces rigidity.


