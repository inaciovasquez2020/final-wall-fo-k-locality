import numpy as np

def covariance(X):
    X = np.asarray(X, dtype=float)
    X = X - X.mean(axis=0, keepdims=True)
    return (X.T @ X) / (X.shape[0] - 1)

def is_rank1(M, tol=1e-10):
    s = np.linalg.svd(M, compute_uv=False)
    return (s[1] / s[0]) < tol
