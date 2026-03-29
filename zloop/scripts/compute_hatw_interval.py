import mpmath as mp

mp.mp.dps = 80

def w(t):
    if abs(t) <= 1:
        return mp.mpf(15)/16 * (1 - t*t)**2
    return mp.mpf(0)

def hatw_interval(xi, N=4001):
    a = mp.mpf(-1)
    b = mp.mpf(1)
    f = lambda t: w(t) * mp.e**(-2j*mp.pi*xi*t)
    return mp.quad(f, [a, b])
