import URFCore.Provenance

structure ProvenanceFull where
  leanDepsHash : String
  buildMerkleRoot : String
  imageDigest : String

structure AttestationFull where
  lean_deps_hash : String
  build_merkle_root : String
  image_digest : String

def fullToAtt (p : ProvenanceFull) : AttestationFull :=
  ⟨p.leanDepsHash, p.buildMerkleRoot, p.imageDigest⟩

def attToFull (a : AttestationFull) : ProvenanceFull :=
  ⟨a.lean_deps_hash, a.build_merkle_root, a.image_digest⟩

theorem full_left_inv : ∀ p, attToFull (fullToAtt p) = p := by
  intro p; cases p; rfl

theorem full_right_inv : ∀ a, fullToAtt (attToFull a) = a := by
  intro a; cases a; rfl

def fullEquiv : ProvenanceFull ≃ AttestationFull :=
{ toFun := fullToAtt
, invFun := attToFull
, left_inv := full_left_inv
, right_inv := full_right_inv
}
