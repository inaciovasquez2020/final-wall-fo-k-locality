Mutual information ceiling implies entropy drop ceiling under transcript determinism

Let τ_t be the transcript after step t and let Q_t be the step t output.
Assume transcript determinism:

τ_t = (τ_{t-1}, Q_t)

Let H_t = H(X | τ_t).

Then for every t:

H_{t-1} - H_t = I(X ; Q_t | τ_{t-1})

Proof

H_{t-1} - H_t
= H(X | τ_{t-1}) - H(X | τ_{t-1}, Q_t)
= I(X ; Q_t | τ_{t-1})

Therefore if an admissibility condition yields

I(X ; Q_t | τ_{t-1}) ≤ C

for all t, then the entropy drop ceiling holds:

H_{t-1} - H_t ≤ C

and summation yields

H_0 - H_T ≤ C T

If additionally H_T ≤ ε then

T ≥ (H_0 - ε) / C
