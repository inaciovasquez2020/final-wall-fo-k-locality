#!/usr/bin/env python3
"""
URF Hodge Truncation Generator (Deterministic)

Outputs:
  - d1.npy : incidence matrix for d1 : C0 -> C1
  - d2.npy : incidence matrix for d2 : C1 -> C2
  - L.npy  : Δ1 = d1 d1^T + d2^T d2   (1-form combinatorial Hodge Laplacian)
  - P.npy  : orthogonal projector onto ker(L) (first-pass defect space)
  - meta.json : deterministic build metadata

Construction:
  - Uses an N×N periodic square grid (torus) with a fixed vertex ordering.
  - Oriented edges: horizontal (east) and vertical (north).
  - 2-cells: unit squares with CCW boundary orientation.
  - All choices are deterministic from N.

Usage:
  python3 gen_hodge_truncation.py --N 8 --outdir ./hodge_N8
"""
from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np


def mod(a: int, n: int) -> int:
    return a % n


@dataclass(frozen=True)
class GridIndex:
    N: int

    def vid(self, x: int, y: int) -> int:
        """Vertex id for (x,y) in [0..N-1]^2."""
        return mod(y, self.N) * self.N + mod(x, self.N)

    def h_eid(self, x: int, y: int) -> int:
        """Horizontal edge id for edge (x,y) -> (x+1,y)."""
        return mod(y, self.N) * self.N + mod(x, self.N)

    def v_eid(self, x: int, y: int) -> int:
        """Vertical edge id for edge (x,y) -> (x,y+1)."""
        return self.N * self.N + (mod(y, self.N) * self.N + mod(x, self.N))

    def fid(self, x: int, y: int) -> int:
        """Face id for unit square with lower-left corner (x,y)."""
        return mod(y, self.N) * self.N + mod(x, self.N)


def build_d1(N: int) -> np.ndarray:
    """
    Build d1 : C0 -> C1 incidence matrix of size (E × V).
    Each row corresponds to an oriented edge e = (u -> v):
      d1[e,u] = -1, d1[e,v] = +1.
    """
    g = GridIndex(N)
    V = N * N
    E = 2 * N * N
    d1 = np.zeros((E, V), dtype=float)

    # Horizontal edges
    for y in range(N):
        for x in range(N):
            e = g.h_eid(x, y)
            u = g.vid(x, y)
            v = g.vid(x + 1, y)
            d1[e, u] = -1.0
            d1[e, v] = +1.0

    # Vertical edges
    for y in range(N):
        for x in range(N):
            e = g.v_eid(x, y)
            u = g.vid(x, y)
            v = g.vid(x, y + 1)
            d1[e, u] = -1.0
            d1[e, v] = +1.0

    return d1


def build_d2(N: int) -> np.ndarray:
    """
    Build d2 : C1 -> C2 boundary matrix of size (F × E),
    using CCW boundary of each face:
      (x,y)->(x+1,y) (east, +)
      (x+1,y)->(x+1,y+1) (north on right column, +)
      (x+1,y+1)->(x,y+1) (west = negative of horizontal at (x,y+1))
      (x,y+1)->(x,y) (south = negative of vertical at (x,y))
    """
    g = GridIndex(N)
    E = 2 * N * N
    F = N * N
    d2 = np.zeros((F, E), dtype=float)

    for y in range(N):
        for x in range(N):
            f = g.fid(x, y)

            # east edge: (x,y)->(x+1,y)
            e_east = g.h_eid(x, y)
            d2[f, e_east] += 1.0

            # north edge on right: (x+1,y)->(x+1,y+1)
            e_north_right = g.v_eid(x + 1, y)
            d2[f, e_north_right] += 1.0

            # west edge: (x+1,y+1)->(x,y+1) = -((x,y+1)->(x+1,y+1))
            e_west = g.h_eid(x, y + 1)
            d2[f, e_west] += -1.0

            # south edge: (x,y+1)->(x,y) = -((x,y)->(x,y+1))
            e_south = g.v_eid(x, y)
            d2[f, e_south] += -1.0

    return d2


def projector_onto_nullspace(A: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    """
    Orthogonal projector onto ker(A) for symmetric A via eigen-decomposition.
    """
    w, V = np.linalg.eigh(A)
    idx = np.where(w <= tol)[0]
    if idx.size == 0:
        return np.zeros_like(A)
    U = V[:, idx]  # orthonormal eigenvectors
    return U @ U.T


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, required=True, help="grid size (torus): N×N")
    ap.add_argument("--outdir", type=str, default="hodge_out", help="output directory")
    ap.add_argument("--tol", type=float, default=1e-10, help="nullspace eigenvalue tolerance")
    args = ap.parse_args()

    N = int(args.N)
    if N <= 1:
        raise SystemExit("N must be >= 2")
    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)

    d1 = build_d1(N)
    d2 = build_d2(N)

    # Δ1 = d1 d1^T + d2^T d2
    L = d1 @ d1.T + d2.T @ d2
    # first-pass defect: ker(L)
    P = projector_onto_nullspace(L, tol=float(args.tol))

    np.save(os.path.join(outdir, "d1.npy"), d1)
    np.save(os.path.join(outdir, "d2.npy"), d2)
    np.save(os.path.join(outdir, "L.npy"), L)
    np.save(os.path.join(outdir, "P.npy"), P)

    meta = {
        "construction": "NxN periodic square grid (torus) combinatorial cochains",
        "N": N,
        "V": int(N * N),
        "E": int(2 * N * N),
        "F": int(N * N),
        "L_definition": "Delta1 = d1 d1^T + d2^T d2",
        "P_definition": "orthogonal projector onto ker(L) via eigendecomposition",
        "null_tol": float(args.tol),
        "ordering": {
            "vertices": "vid(x,y)=y*N+x (mod N)",
            "edges": "first all horizontal (east), then vertical (north)",
            "faces": "fid(x,y)=y*N+x (mod N)"
        }
    }
    with open(os.path.join(outdir, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, sort_keys=True)

    # quick sanity checks
    sym_err = float(np.max(np.abs(L - L.T)))
    idemp_err = float(np.max(np.abs(P @ P - P)))
    print("Wrote:", outdir)
    print("Sanity:")
    print("  max|L-L^T|      =", sym_err)
    print("  max|P^2-P|      =", idemp_err)
    print("  rank(P) (approx)=", int(np.round(np.trace(P))))


if __name__ == "__main__":
    main()

