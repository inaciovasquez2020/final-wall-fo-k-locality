Hanf neighborhood enumeration bound for FO^k

Fix maximum degree Δ ≥ 2 and radius r ≥ 0.
Let s(Δ,r) be the maximum size of a radius r ball in a Δ bounded graph:

s(Δ,r) = 1 + Δ * ((Δ-1)^r - 1) / (Δ-2)

Let T(Δ,r,c) be the number of isomorphism types of rooted radius r neighborhoods with vertex colors from an alphabet of size c, in graphs of maximum degree Δ.
A sufficient explicit bound is

T(Δ,r,c) ≤ c^{s(Δ,r)} * (s(Δ,r))^{O(s(Δ,r))}

Define B_k(Δ,r,c,n) for k tuple refinement by

B_k ≤ ( n * T(Δ,r,c) )^k

Hence the per step answer alphabet size satisfies

log B_k ≤ k log n + k log T(Δ,r,c)

In particular, for fixed Δ,r,c the per step capacity constant may be taken as

C(n) = k log n + O_k(1)

as a concrete instantiation of C = log B_k in the MI ceiling lemma.
