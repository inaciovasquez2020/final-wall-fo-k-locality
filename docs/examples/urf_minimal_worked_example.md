# URF Minimal Worked Example

## Purpose
Provide a concrete example demonstrating the rigidity / capacity mechanism
in a small explicit instance.

## Example: Bounded-Degree Graph

Let G be a 4-regular graph with n vertices.

Define the local neighborhood ball B_r(v) for radius r.

### Step 1 — Local Type Enumeration
Compute the FO^k local type of each vertex:

type(v) = FO^k(B_r(v))

### Step 2 — Type Collision Analysis
If

|{ type(v) }| < |V|

then multiple vertices share identical local configurations.

### Step 3 — Rigidity Trigger
Large cycle-overlap rank forces divergence of local types:

COR_R(G) ≥ T(k,Δ) ⇒ FO^k type diversity.

### Step 4 — Consequence
Entropy reduction per refinement step remains bounded,
yielding EntropyDepth lower bounds.

## Interpretation
This illustrates the rigidity principle:

local indistinguishability cannot persist under high cycle complexity.

