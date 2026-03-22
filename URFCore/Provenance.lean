structure ProvenanceProj where
  leanDepsHash : String
  buildMerkleRoot : String

structure SLSADigest where
  lean_deps_hash : String
  build_merkle_root : String

def projToDigest (p : ProvenanceProj) : SLSADigest :=
  ⟨p.leanDepsHash, p.buildMerkleRoot⟩

def digestToProj (d : SLSADigest) : ProvenanceProj :=
  ⟨d.lean_deps_hash, d.build_merkle_root⟩

theorem proj_digest_left_inv : ∀ p, digestToProj (projToDigest p) = p := by
  intro p
  cases p
  rfl

def projDigestEquiv : ProvenanceProj ≃ SLSADigest where
 toFun := projToDigest
 invFun := digestToProj
 left_inv := proj_digest_left_inv
 right_inv := proj_digest_right_inv
{ toFun := projToDigest
, invFun := digestToProj
, left_inv := proj_digest_left_inv
, right_inv := proj_digest_right_inv
}

namespace URFCore

-- Conditional: assume a canonical JSON codec for each record.
axiom encodeProvenanceProj : ProvenanceProj → String
axiom decodeProvenanceProj : String → Option ProvenanceProj
axiom encodeSLSADigest : SLSADigest → String
axiom decodeSLSADigest : String → Option SLSADigest

axiom decode_encode_prov : ∀ p, decodeProvenanceProj (encodeProvenanceProj p) = some p
axiom decode_encode_slsa : ∀ d, decodeSLSADigest (encodeSLSADigest d) = some d

theorem slsa_codec_transport (p : ProvenanceProj) :
    decodeSLSADigest (encodeSLSADigest (projToDigest p)) = some (projToDigest p) := by
  simpa using (decode_encode_slsa (projToDigest p))

end URFCore
