Model Class M_reasonable

Definition.
M_reasonable is the closure of the following baseline models:

1. Logspace-uniform circuit families NC^k for k >= 1
2. Polynomial-time RAM machines with word size O(log n)
3. Polynomial-time Turing machines

All models are oracle-free. Any advice or preprocessing is charged to the transcript.

Transcript Invariant.
Every computation induces a transcript Π = (Π_0, Π_1, ... , Π_T) with

TC := max_t H(Π_{t+1} | Π_t) <= polylog(n)

Closure Properties.
M_reasonable is closed under:
- uniform compilation
- parallel or interleaved pairing
- oracle-free uniform simulation between models

These closures preserve TC up to polylogarithmic factors.

