Capacity–Entropy Bridge (CE-Bridge)

Setup.
Let C_t denote the configuration random variable at step t.
Let Π_t denote the transcript prefix up to step t.

Define entropy loss:
ΔH_t := H(C_t) − H(C_{t+1})

Define information gain:
ΔI_t := I(C_t ; Π_{t+1} | Π_t)

Theorem (CE-Bridge).
There exists a universal monotone function f(x) = O(x) such that
for all verifier-auditable transcript schemas and all t,

ΔH_t <= f(ΔI_t)

In particular, if ΔI_t <= C for all t, then ΔH_t <= O(C).

Formal core.
C_t → Π_t → Π_{t+1} forms a Markov chain.
By data processing and conditional entropy subadditivity,
entropy contraction is dominated by injected mutual information.

