URF Cross-Repo Federation Consistency Verifier

Purpose
Deterministically verify that a set of URF repositories can be federated into a single
global lemma DAG and metadata state without conflicts.

Inputs
- Repo list R = {R₁,…,R_k}
- For each repo R_i:
  - meta/lemmas.yaml
  - meta/deps.yaml
  - meta/constants.yaml
  - meta/regime.yaml
  - meta/dag.json
  - meta/MANIFEST.sha256
  - meta/pipeline_version.txt
  - meta/lemma_hash_registry_fragment.json (optional but recommended)

Derived Global Objects
- Global node set V = ⋃ V_i keyed by K_global
- Global edge set E = ⋃ E_i (plus validated cross-repo edges)
- Global registry map H_L → K_global
- Global manifest summary M* (per-repo manifest roots + versions)

Verification Phases

1) Manifest Integrity (per repo)
- Recompute hashes for files listed in MANIFEST.sha256
- Compare to recorded values
FAIL if any mismatch.

2) Schema & Version Compatibility
- Validate YAML/JSON against repo schemas
- Check pipeline_version compatibility matrix
FAIL if incompatible MAJOR or missing migration path.

3) Namespace & Hash Consistency
For each H_L appearing across repos:
- All namespace_key values must match
- All metadata_hash values must match
FAIL on divergence.

4) DAG Acyclicity (Global)
- Construct G = (V,E) over all repos
- Check acyclicity (e.g., Kahn or DFS white/gray/black)
FAIL if cycle found.

5) Rank Monotonicity (Optional but Recommended)
- Compute longest-path rank (weighted or unweighted per spec)
- Verify cross-repo edges satisfy monotonicity condition
WARN or FAIL per policy.

6) Transparency / Attestation (If Enabled)
- Verify signatures on registry / transparency fragments
- Verify Merkle release ancestry consistency
FAIL if signature or chain invalid.

Outputs
- meta/federation_report.json:
  {
    "repos": [...],
    "manifest_ok": bool,
    "schema_ok": bool,
    "namespace_ok": bool,
    "dag_acyclic": bool,
    "rank_ok": bool,
    "attestation_ok": bool,
    "global_node_count": int,
    "global_edge_count": int,
    "timestamp": RFC3339
  }

Determinism
Given identical repo snapshots, verifier must produce identical report bytes.

Security Model
- Detects tampering, namespace spoofing, hash drift, DAG structural violations.
- Collision resistance reduces to H_L + release hash primitives.

Operational Modes
- STRICT: any WARN → FAIL
- PERMISSIVE: WARN allowed, only structural FAIL stops federation
