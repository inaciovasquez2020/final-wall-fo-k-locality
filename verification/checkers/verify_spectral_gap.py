#!/usr/bin/env python3
import json, sys, hashlib
import numpy as np

def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def is_symmetric(A, tol=1e-10):
    return np.max(np.abs(A - A.T)) <= tol

def is_projector(P, tol=1e-10):
    return is_symmetric(P, tol) and np.max(np.abs(P @ P - P)) <= tol

def main():
    if len(sys.argv) < 2:
        print("Usage: verify_spectral_gap.py <cert.json>")
        sys.exit(2)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        cert = json.load(f)

    for k in ["schema_version","kind","id","created_utc","n","epsilon","L","P"]:
        if k not in cert:
            raise SystemExit(f"FAIL: missing field {k}")

    if cert["kind"] != "URF_SPECTRAL_GAP_CERT":
        raise SystemExit("FAIL: wrong kind")

    n = int(cert["n"])
    eps = float(cert["epsilon"])
    if eps <= 0:
        raise SystemExit("FAIL: epsilon must be > 0")

    L = np.array(cert["L"], dtype=float)
    P = np.array(cert["P"], dtype=float)

    if L.shape != (n,n) or P.shape != (n,n):
        raise SystemExit("FAIL: matrix shapes do not match n")

    if not is_symmetric(L):
        raise SystemExit("FAIL: L is not symmetric")

    if not is_projector(P):
        raise SystemExit("FAIL: P is not an orthogonal projector")

    I = np.eye(n)
    Q = I - P
    A = Q @ L @ Q

    U, s, _ = np.linalg.svd(Q)
    idx = np.where(s > 1e-8)[0]
    if len(idx) == 0:
        raise SystemExit("FAIL: im(Q) is {0}; no complement space")

    B = U[:, idx]
    Ared = B.T @ A @ B
    w = np.linalg.eigvalsh(Ared)
    lam_min = float(np.min(w))

    if lam_min + 1e-10 < eps:
        raise SystemExit(f"FAIL: spectral gap check failed: lam_min={lam_min} < eps={eps}")

    print("OK")
    print(f"lambda_min(QLQ|im(Q)) = {lam_min}")
    print(f"epsilon               = {eps}")
    print(f"sha256(cert)          = {sha256_file(path)}")

if __name__ == "__main__":
    main()

