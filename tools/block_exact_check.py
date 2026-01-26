#!/usr/bin/env python3
import json, sys
import numpy as np

def load_matrix(path: str) -> np.ndarray:
    with open(path, "r", encoding="utf-8") as f:
        obj = json.load(f)
    if isinstance(obj, dict) and "matrix" in obj:
        obj = obj["matrix"]
    A = np.array(obj, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError(f"{path}: expected square 2D matrix, got shape {A.shape}")
    return A

def projector_onto_eigenspace(A: np.ndarray, eig_index: int, tol: float = 1e-9) -> np.ndarray:
    # Symmetric eigendecomposition
    w, Q = np.linalg.eigh(A)
    if eig_index < 0 or eig_index >= len(w):
        raise ValueError(f"eig_index out of range: {eig_index} (n={len(w)})")

    lam = w[eig_index]
    # Collect all eigenvectors in the same (numerically) equal-eigenvalue block
    mask = np.abs(w - lam) <= tol
    B = Q[:, mask]
    # Orthonormal columns; projector = B B^T
    return B @ B.T

def main():
    if len(sys.argv) < 4:
        print("Usage: block_exact_check.py A.json V.json k [tol]", file=sys.stderr)
        print("  A.json: square matrix (or {\"matrix\": [...]})", file=sys.stderr)
        print("  V.json: square matrix (or {\"matrix\": [...]})", file=sys.stderr)
        print("  k: eigenvalue index (0-based) for the gap (k,k+1)", file=sys.stderr)
        print("  tol: optional eigenvalue clustering tolerance (default 1e-9)", file=sys.stderr)
        sys.exit(2)

    A_path, V_path = sys.argv[1], sys.argv[2]
    k = int(sys.argv[3])
    tol = float(sys.argv[4]) if len(sys.argv) >= 5 else 1e-9

    A = load_matrix(A_path)
    V = load_matrix(V_path)
    if A.shape != V.shape:
        raise ValueError(f"Shape mismatch: A{A.shape} vs V{V.shape}")

    # Π = Π_k + Π_{k+1}
    Pi_k   = projector_onto_eigenspace(A, k, tol=tol)
    Pi_k1  = projector_onto_eigenspace(A, k+1, tol=tol)
    Pi = Pi_k + Pi_k1

    # Symmetrize Pi numerically (safety)
    Pi = 0.5 * (Pi + Pi.T)

    M = Pi @ V @ Pi
    op_norm = np.linalg.norm(M, ord=2)   # spectral norm
    fro_norm = np.linalg.norm(M, ord="fro")

    print(json.dumps({
        "k": k,
        "tol": tol,
        "op_norm_PiVPi": float(op_norm),
        "fro_norm_PiVPi": float(fro_norm),
        "block_exact_rigid": bool(op_norm <= 1e-10)
    }, indent=2))

if __name__ == "__main__":
    main()

