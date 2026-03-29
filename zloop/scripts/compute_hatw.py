import numpy as np

def w(t):
    out = np.zeros_like(t)
    m = np.abs(t) <= 1
    out[m] = (15/16) * (1 - t[m]**2)**2
    return out

def hatw(xi, N=20001):
    t = np.linspace(-1, 1, N)
    dt = t[1] - t[0]
    return np.sum(w(t) * np.exp(-2j * np.pi * xi * t)) * dt
