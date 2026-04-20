# Ordered-Edge Reduction

## Definitions
\[
W_{R,L}(u,v):=E\!\bigl(G[B_{R+L}(u)\cup B_{R+L}(v)]\bigr).
\]

\[
\mathcal C_{R,L}(u,v):=
\left\{
C\subseteq E(G):
C\text{ is a simple cycle},\ |C|\le L,\ \{u,v\}\in C,\ C\subseteq W_{R,L}(u,v)
\right\}.
\]

\[
\operatorname{ovrk}_{R,L}(G):=
\max_{x\in V(G)}
\dim_{\mathbf F_2}
\Bigl\langle [C]:
C\text{ simple cycle of length }\le L,\ C\cap B_R(x)\neq\varnothing
\Bigr\rangle .
\]

\[
M_{\Delta,R,L}:=
\max_{\Delta(H)\le \Delta,\ z\in V(H)} |E(B_{R+L}(z))|.
\]

## Proven reduction shell
If $\mathbf{AMDM}_{\Delta,R,L,\mu}$ holds, then
\[
\operatorname{ovrk}_{R,L}(G)>m
\Longrightarrow
\exists (u,v)\neq (u',v'):
(u,v)\not\equiv^{FO^4}_{q_{\Delta,R,L}}(u',v').
\]

## Finish condition
Replace OPEN by PROVED only after:
1. explicit finite motif family is fixed;
2. each motif is FO^4-definable;
3. bounded multiplicity $\mu$ is proved;
4. adversarial ordered-edge separation is certified on a growing family.
