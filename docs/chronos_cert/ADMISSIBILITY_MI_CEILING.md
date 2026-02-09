Admissibility to Mutual-Information Ceiling and Composition Lemma

Lemma 1 (Finite-alphabet partition query ceiling)

Let X be a random variable and let F be any sigma-field.
Let Q be an answer random variable taking values in a finite set of size at most B_k.

Then

I(X ; Q | F) ≤ log B_k.

Proof

I(X ; Q | F) ≤ H(Q | F) ≤ H(Q) ≤ log |supp(Q)| ≤ log B_k.

Corollary (Per-step ceiling)

If each refinement step outputs an admissible partition-query answer Q_t with |supp(Q_t)| ≤ B_k, then

I(X ; Q_t | F_{t-1}) ≤ log B_k

for all t, hence the per-step capacity constant may be taken as C = log B_k.

Lemma 2 (Entropy-drop composition)

Let F ⊆ F' ⊆ F'' be sigma-fields and define H(F) = H(X | F).

Assume

H(F) − H(F') ≤ C1
H(F') − H(F'') ≤ C2.

Then

H(F) − H(F'') ≤ C1 + C2.

Proof

H(F) − H(F'') = (H(F) − H(F')) + (H(F') − H(F'')) ≤ C1 + C2.
