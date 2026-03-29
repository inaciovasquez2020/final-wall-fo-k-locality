Certificate soundness contract

Objects
Cert is a JSON document parsed into a structured object C
Verifier is a deterministic function V : C → Bool
Property is a Lean predicate P : C → Prop

Soundness axiom schema
For each certificate family F
Sound_F : ∀ c, V_F c = true → P_F c

Completeness axiom schema (optional)
Complete_F : ∀ c, P_F c → V_F c = true

Tight coupling requirement
V_F is versioned by (repo, git ref, tool path sha256, schema sha256)

Audit tuple
A_F(c) := (repo, ref, verifier_sha256, schema_sha256, cert_sha256)

Acceptance rule
If V_F c = true under the recorded audit tuple then P_F c is considered established in the repository contract layer

Current families
TV finite
TV step
TU seymour

Status flags
Soundness required
Completeness optional
