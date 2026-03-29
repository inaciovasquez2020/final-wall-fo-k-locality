Canonical URF Lemma Hash H_L

Definition
Let:
AST_norm(L)  := canonical normalized Lean AST of lemma L
Schema_norm(L) := canonical normalized YAML schema fragment of L

Canonical serialization:
C(L) := CBOR_canonical( AST_norm(L), Schema_norm(L) )

Lemma hash:
H_L(L) := SHA256( C(L) )

Required Canonical Properties

AST normalization:
- α-normalization (binder canonicalization)
- deterministic implicit argument expansion
- deterministic universe representation
- whitespace / comment removal

Schema normalization:
- UTF-8 only
- canonical scalar encoding
- sorted mapping keys
- canonical float / int forms

CBOR canonical layer (RFC canonical form):
- shortest integer encoding
- definite-length containers
- lexicographic map key ordering by CBOR bytes
- canonical NaN or disallowed NaN

Uniqueness Guarantee
If canonical CBOR bytes are equal, normalized lemma representations are equal.

Security Property
Collision resistance reduces to SHA256 collision resistance + CBOR canonical uniqueness.
