import mpmath as mp
from math import pi

mp.mp.dps = 80

delta = mp.mpf(1)/4
wpp_norm = mp.mpf(15)/4

def T_HS_interval(P):
    return (2/delta) * (wpp_norm**2 / (2*pi)**4) * mp.power(mp.log(P), -2*delta)
