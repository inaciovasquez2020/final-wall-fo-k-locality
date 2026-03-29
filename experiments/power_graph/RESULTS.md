# Power-Graph R-Coloring Scaling Results

Parameters:
- R = 1
- Greedy coloring (largest_first)
- χ computed on G^(2R)

| n   | Path | Star | Random 3-regular |
|-----|------|------|------------------|
| 50  | 3    | 50   | 7                |
| 100 | 3    | 100  | 8                |
| 200 | 3    | 200  | 7                |
| 400 | 3    | 400  | 7                |

Observations:

- Path: χ₁(G) constant.
- Star: χ₁(G) linear in n.
- Random 3-regular: χ₁(G) appears bounded (≈ 7–8).
