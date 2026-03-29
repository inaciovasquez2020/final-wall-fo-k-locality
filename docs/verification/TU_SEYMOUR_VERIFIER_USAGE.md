TU Seymour Deterministic Verifier Usage

Purpose

This tool verifies Seymour style Totally Unimodular decomposition certificates deterministically. The verifier checks structural reconstruction and base witnesses without probabilistic steps.

Location

tools/tu/tu_seymour_verify.py

Certificate Schema Overview

Top level object

matrix
  m integer number of rows
  n integer number of columns
  entries flattened row major list with values in -1, 0, 1

root
  decomposition tree node

Node Kinds

network
transpose
R10
sum1
sum2
sum3

Network Node Requirements

A
  rows list of global matrix row indices
  cols list of global matrix column indices

network_witness
  V number of vertices
  E number of edges
  tail list length E
  head list length E
  row_to_vertex list length number of rows in A
  col_to_edge list length number of columns in A

Network Condition

Each column must contain exactly one +1 and one -1 corresponding to head and tail vertices under row_to_vertex mapping.

R10 Node Requirements

R10_witness
  perm_rows permutation of row indices
  perm_cols permutation of column indices
  sign_rows entries in -1 or 1
  sign_cols entries in -1 or 1

The normalized matrix must match the deterministic R10 canonical pattern:

10 by 10 matrix
Each row has exactly 3 nonzero entries
Each column has exactly 3 nonzero entries

Sum Nodes

sum1

Parent must equal block diagonal concatenation of children after deterministic index ordering.

sum2 and sum3

Require boundary object

sum_boundary
  glue_rows overlap rows
  glue_cols overlap columns

Parent must equal union reconstruction and must agree on overlap entries.

Running Verification

Example deterministic smoke test

python3 tools/tu/tu_seymour_verify.py tools/tu/testdata/network_minimal_CERT.json

Expected Output

VERIFY_OK

Failure Mode

Verifier terminates with

VERIFY_FAIL message

Determinism Guarantee

All checks are structural and exact. No randomness or floating point tolerance is used.

Repository Integration Contract

The verifier is safe for CI execution.
The verifier produces identical output across platforms given identical input JSON.
