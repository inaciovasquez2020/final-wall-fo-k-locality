# URF_law3 — Spectral Gap Rigidity Wall (Terminal, Conditional)

## Axiom Schema (SG–Closure)

For every admissible URF system \((H,\Delta_H,\mathrm{Per})\):

**(A) Compact Resolvent**
\[
(\Delta_H + I)^{-1} \in \mathcal{K}(H).
\]

**(B) Geometric Unitary Realization**
\[
\exists\ \text{compact }(M,g),\ \exists\ \text{unitary }U:H\to L^2(M)\ \text{such that}\ 
\Delta_H = U^{-1}(-\Delta_g)U.
\]

**(C) Projection Alignment**
\[
\mathrm{Per} = U^{-1}\Pi_{\mathrm{const}}U,
\]
where \(\Pi_{\mathrm{const}}\) is orthogonal projection onto constants in \(L^2(M)\).

---

## Theorem (URF_law3 — Conditional Closure)

**Conditional.** Assuming (A)–(C),
\[
\inf \mathrm{Spec}\big(\Delta_H\mid \ker(\mathrm{Per})^\perp\big) > 0.
\]

Equivalently, there is no sequence \(f_n \in \ker(\mathrm{Per})^\perp\) with \(\|f_n\|=1\) and
\[
\langle \Delta_H f_n, f_n\rangle \to 0.
\]

---

## Impossibility Corollary

Under (A)–(C), failure of URF_law3 is logically impossible (in ZFC):
\[
(A)\land(B)\land(C)\ \Rightarrow\ \neg(\text{URF\_law3 fails}).
\]

---

## Break Modes (Exhaustive)

URF_law3 can fail only by violation of at least one of:

1. **Essential spectrum at 0 / non-compact resolvent**: \((\Delta_H+I)^{-1}\notin\mathcal K(H)\).
2. **Non-unitary similarity**: \(\Delta_H = T^{-1}\Delta_0 T\) with \(T\) invertible but not unitary (spectrum not preserved).
3. **Projection misalignment**: \(\mathrm{Per}\neq U^{-1}\Pi_{\mathrm{const}}U\).

---

## Certified Instances

- **URF-SG-BASE-1**: \(H=L^2(S^1)\), \(\Delta=-\frac{d^2}{d\theta^2}\), \(\mathrm{Per}=\Pi_{\mathrm{const}}\), gap \(\lambda_1=1\).
- **Torus family**: \(H=L^2(\mathbb T^d)\), \(\Delta=-\Delta\), \(\mathrm{Per}=\Pi_{\mathrm{const}}\), gap \(\lambda_1=1\).
- **Finite graphs**: \(H=\ell^2(V)\), \(\Delta=dI-A\), \(\mathrm{Per}(f)=|V|^{-1}\sum_v f(v)\), gap \(>0\) for connected graphs.

