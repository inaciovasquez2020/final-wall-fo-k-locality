import numpy as np

N = 50
k = np.arange(-N, N+1)
eigs = k**2
eigs = eigs[eigs > 0]

print("Computed λ1:", eigs.min())

