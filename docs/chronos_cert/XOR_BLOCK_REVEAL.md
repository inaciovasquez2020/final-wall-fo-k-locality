Affine XOR block reveal

Let S ⊆ F2^n be an affine solution space of dimension d.
Let X be uniform on S, so H(X) = d bits.

A block step reveals r_t independent linear constraints not implied by prior constraints.
Equivalently, the affine space dimension drops by at most r_t.

Let H_t = H(X | τ_t). Then

H_{t-1} - H_t ≤ r_t

If the transcript alphabet size per step is at most B, then r_t ≤ log B is sufficient for correctness of the certificate ceiling, and in particular if r_t ≤ R for all t then C = R works.

Special case
One independent parity per step gives H_t = d - t until 0, with per step drop exactly 1.
