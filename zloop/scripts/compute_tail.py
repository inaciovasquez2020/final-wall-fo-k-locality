from math import log, pi

delta = 0.25
wpp_norm = 15/4

def T_HS(P):
    return (2/delta) * (wpp_norm**2 / (2*pi)**4) * (log(P)**(-2*delta))
