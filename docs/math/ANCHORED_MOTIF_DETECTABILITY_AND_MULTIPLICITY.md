# Anchored Motif Detectability and Multiplicity

## Status
OPEN

## Statement template
Fix integers \(\Delta,R,L,\mu \ge 1\).

For each ordered edge \((u,v)\in \vec E(G)\), let
\[
\mathcal C_{R,L}(u,v)
\]
denote the family of simple cycles of length at most \(L\) meeting the ordered-edge \(R\)-ball around \((u,v)\).

Let
\[
\Sig^{\ast}_{R,L}(u,v)
\]
be the anchored ordered-edge motif profile extracted from \(\mathcal C_{R,L}(u,v)\).

Assume:

1. There is a finite anchored motif family.
2. Each anchored motif is \(FO^4\)-definable.
3. For every ordered edge \((u,v)\) and every anchored motif type \(\tau\),
   \[
   \dim_{\mathbf F_2}\Bigl\langle [C]:
   C\in\mathcal C_{R,L}(u,v),\ m_C^{\ast}=\tau
   \Bigr\rangle \le \mu.
   \]

4. If
   \[
   \operatorname{ovrk}_{R,L}(G)>m,
   \]
   then
   \[
   \max_{(u,v)\in\vec E(G)}
   \dim_{\mathbf F_2}\langle \Sig^{\ast}_{R,L}(u,v)\rangle
   >
   \Bigl\lfloor \frac{m}{\mu\,M_{\Delta,R,L}}\Bigr\rfloor .
   \]

## Consequence
There exists \(q_{\Delta,R,L}\) such that
\[
\operatorname{ovrk}_{R,L}(G)>m
\Longrightarrow
\exists (u,v)\neq (u',v'):
(u,v)\not\equiv^{FO^4}_{q_{\Delta,R,L}}(u',v').
\]
