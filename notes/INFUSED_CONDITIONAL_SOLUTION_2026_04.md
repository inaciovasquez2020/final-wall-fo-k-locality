# Infused Conditional Solution (2026-04)

## Status
Conditional.

## Missing bridge
Assume:
\[
\mathbf{BRIDGE}(k,\Delta):\quad
\exists R_0,L,m\ \forall G\ \Bigl[
\bigl(\Delta(G)\le \Delta \wedge \operatorname{CorrRank}_{R_0}(G)>m\bigr)
\Longrightarrow
\neg\operatorname{FOHom}_{k,R_0}(G)
\Bigr].
\]

## Known ingredients
1. `final-wall-fo-k-locality` reduces the program to Overlap Rigidity.
2. `CorrRank` supplies the intended COR \(\to\) FO\(^k\)-local-diversity bridge schema.
3. `cycle-local-rigidity` supplies bounded exhaustive FO\(^4\) evidence.
4. `cslib-fmt` supplies FO\(^k\)/EF/local-type infrastructure.
5. `chronos-urf-rr` preserves the cross-layer conditional interface.

## Overlap invariant
Define
\[
\operatorname{ovrk}_{R,L}(G):=
\max_{v\in V(G)}
\dim_{\mathbf F_2}
\Bigl\langle
[C]:
C \text{ simple cycle of length }\le L,\ C\cap B_R(v)\neq\varnothing
\Bigr\rangle .
\]

## Comparison assumptions
Assume
\[
\mathbf{C1}:\quad
\operatorname{ovrk}_{R,L}(G)\le A_{R,L,\Delta}\,\operatorname{CorrRank}_R(G)+B_{R,L,\Delta},
\]
\[
\mathbf{C2}:\quad
\operatorname{ovrk}_{R,L}(G)\ge a_{R,L,\Delta}\,\operatorname{CorrRank}_R(G)-b_{R,L,\Delta}.
\]

Assume FO\(^4\)-detectability:
\[
\mathbf{C3}:\quad
\forall R,L,m\ \exists \varphi_{R,L,m}\in FO^4
\quad
\forall G\;
\Bigl[
G\models \varphi_{R,L,m}
\Longleftrightarrow
\operatorname{ovrk}_{R,L}(G)>m
\Bigr].
\]

## Conditional theorem
Then
\[
\mathbf{ORL}'(k,\Delta):\quad
\exists R_0,L,m\ \forall G\;
\Bigl[
\Delta(G)\le \Delta \wedge \operatorname{ovrk}_{R_0,L}(G)>m
\Longrightarrow
\neg\operatorname{FOHom}_{k,R_0}(G)
\Bigr].
\]

## Proof shell
\[
\operatorname{ovrk}_{R_0,L}(G)>m
\overset{\mathbf{C2}}{\Longrightarrow}
\operatorname{CorrRank}_{R_0}(G)>m'
\overset{\mathbf{BRIDGE}(k,\Delta)}{\Longrightarrow}
\neg\operatorname{FOHom}_{k,R_0}(G).
\]

## Consequence
\[
\bigl(\mathbf{BRIDGE}(k,\Delta)\wedge \mathbf{C2}\bigr)
\Longrightarrow
\text{Overlap Rigidity}
\Longrightarrow
\text{Final-Wall program closure}.
\]

## Label
This note is CONDITIONAL and does not claim unconditional proof of Overlap Rigidity.
