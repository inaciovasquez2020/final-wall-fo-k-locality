URF Lemma Transparency Log

Purpose
Append-only, publicly auditable log of lemma registrations and lifecycle events
for canonical lemma hashes H_L across the URF federation.

Entry Format
{
  "index": uint64,
  "timestamp": RFC3339,
  "event": "register" | "deprecate" | "supersede",
  "H_L": hex,
  "namespace_key": K_global,
  "repo_id": repoID,
  "release_root": hex,          // Merkle release root anchoring this event
  "metadata_hash": hex,
  "signature": sig_repo         // repo signing key over entry (without signature)
}

Log Structure
- Total order by index.
- Hash chain:
  entry_hash_i = SHA256( canonical_json(entry_i_without_signature) )
  chain_hash_i = SHA256( chain_hash_{i-1} || entry_hash_i ), with chain_hash_0 = 0^256.

Inclusion Proof
- Provide (entry_hash_i, sibling hashes) for Merkle segment OR
- Provide (chain_hash_{i-1}, entry_i) to recompute chain_hash_i.

Consistency Proof
- For two heads h_m and h_n (m < n), provide suffix entries m+1..n to recompute h_n.

Federation Operation
- Each repo publishes a signed fragment:
  meta/transparency_fragment.jsonl
- Global log is merge-by-index with signature verification and chain checks.

Security Goals
- Append-only (detect truncation or rewrite).
- Non-equivocation (detect conflicting entries at same index via signatures + hash chain).
- External anchoring optional (e.g., public timestamp / blockchain anchor of chain_hash head).
