Chronos Core Inequality (Finite Certificate Form)

Objects

State random variable X on finite space Ω  
Refinement transcript sequence τ_0, τ_1, …, τ_T  
Posterior distributions P_t = Law(X | τ_t)

Invariant

For admissible refinement class R with transcript capacity bound C:

I(X ; τ_{t+1} | τ_t) ≤ C

Entropy Form

Let H_t = H(X | τ_t)

Then

H_t − H_{t+1} = I(X ; τ_{t+1} | τ_t) ≤ C

Summation

H_0 − H_T ≤ C T

Depth Lower Bound

If H_T ≤ ε then

T ≥ (H_0 − ε) / C

Finite Certificate Interpretation

Given:

H0_lower  
C  
ε  
Posterior sequence P_0 … P_T  

Verifier checks:

1. H(P_t) − H(P_{t+1}) ≤ C for all t  
2. H(P_T) ≤ ε  

If satisfied:

Certified lower bound

T ≥ (H0_lower − ε) / C

Toy Instance

Uniform 3-bit reveal sequence achieves equality.
