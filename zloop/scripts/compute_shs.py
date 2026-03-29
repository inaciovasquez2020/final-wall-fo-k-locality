import sympy as sp
import numpy as np
from math import log
from compute_hatw import hatw

delta = 0.25

def a(p):
    return log(p)**(1-delta)

def alpha(p):
    return log(p)

def primes_upto(P):
    return list(sp.primerange(2, P+1))

def compute_S_HS(P):
    ps = primes_upto(P)
    S = 0.0
    for i,p in enumerate(ps):
        for q in ps[i+1:]:
            b = a(p)*a(q)*hatw(log(p)-log(q))
            S += 2 * abs(b)**2 / (alpha(p)*alpha(q))
    return S.real
