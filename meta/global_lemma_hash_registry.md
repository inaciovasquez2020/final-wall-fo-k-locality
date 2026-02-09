Global URF Lemma Hash Registry

Purpose
Provide a federation-level directory mapping canonical lemma hashes (H_L) to global metadata.

Registry Entry
H_L → {
  namespace_key: K_global,
  repo_id: repoID,
  module_path: modulePath,
  lemma_name: lemmaName,
  first_seen_release: release_root_hash,
  status: {active | deprecated | superseded},
  superseded_by: optional H_L,
  schema_version,
  metadata_hash
}

Uniqueness Rule
Each H_L must map to exactly one canonical namespace_key at first registration.
Subsequent registrations must match or be rejected.

Federation Sync
Each repo publishes:
meta/lemma_hash_registry_fragment.json

Global registry = union of fragments + conflict resolution by first_seen_release.

Verification
On import:
1. Verify H_L exists in registry.
2. Verify namespace matches.
3. Verify metadata hash matches.

Security
Tamper detection via:
- signed fragment releases
- Merkle release chain anchoring
