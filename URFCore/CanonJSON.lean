namespace URFCore

/-
Computable canonicalization interface (string-level), with correctness asserted
only for strings produced by the external canonicalizer.
A full parser can replace this later.
-/

def CanonJSON := String

def encodeCanon (s : String) : CanonJSON := s
def decodeCanon (c : CanonJSON) : Option String := some c

theorem decode_encode (s : String) : decodeCanon (encodeCanon s) = some s := by rfl

end URFCore
