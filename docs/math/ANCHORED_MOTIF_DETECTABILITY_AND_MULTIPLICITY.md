# Anchored Motif Detectability and Multiplicity

## Status
OPEN

## Target lemma
For fixed $(\Delta,R,L)$ there exist a finite motif set $\mathcal M^{\ast}_{\Delta,R,L}$,
FO^4 formulas $\Mot_\tau(x,y)$ for each $\tau\in\mathcal M^{\ast}_{\Delta,R,L}$,
and a constant $\mu=\mu(\Delta,R,L)$ such that:

1. For every bounded-degree graph $G$ with $\Delta(G)\le \Delta$ and every ordered edge $(u,v)$,
   \[
   \Sig^{\ast}_{R,L}(u,v):=\{\tau:\ G\models \Mot_\tau(u,v)\}
   \]
   is well-defined.

2. For every motif class $\tau$ and every ordered edge $(u,v)$,
   \[
   \dim_{\mathbf F_2}\Bigl\langle [C]:
   C\in\mathcal C_{R,L}(u,v),\ m_C^{\ast}=\tau
   \Bigr\rangle \le \mu.
   \]

3. If
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
There exists $q_{\Delta,R,L}$ such that
\[
\operatorname{ovrk}_{R,L}(G)>m
\Longrightarrow
\exists (u,v)\neq (u',v'):
(u,v)\not\equiv^{FO^4}_{q_{\Delta,R,L}}(u',v').
\]
