import sympy as sp
import mpmath as mp
from math import log
from compute_hatw_interval import hatw_interval

mp.mp.dps = 80
delta = mp.mpf(1)/4

def a(p):
    return mp.power(mp.log(p), 1-delta)

def alpha(p):
    return mp.log(p)

def primes_upto(P):
    return list(sp.primerange(2, P+1))

def compute_S_HS_interval(P):
    ps = primes_upto(P)
    S = mp.mpf(0)
    for i,p in enumerate(ps):
        for q in ps[i+1:]:
            b = a(p)*a(q)*hatw_interval(mp.log(p)-mp.log(q))
            term = 2 * abs(b)**2 / (alpha(p)*alpha(q))
            S += term
    return S
