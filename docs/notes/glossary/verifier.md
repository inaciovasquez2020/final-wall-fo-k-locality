# Verifier / Certificate Glossary

**AIV Certificate**  
A certificate asserting admissibility-invariant validity under a stated schema.

**Canonical Public Key**  
The designated verification key treated as authoritative for signature checks.

**Certificate Re-signing**  
Replacing a signature to match the canonical key and required signature format.

**Enforcement Rule**  
A CI or verifier rule that rejects artifacts failing schema/signature/semantic checks.

**Minisign Format**  
A signature format used to attest artifacts; verification requires the correct public key and expected metadata constraints.

**Verifier Pipeline**  
The ordered sequence of checks: schema validation → signature verification → semantic checks → invariant checks.

**Verifier Smoke Check**  
A minimal CI check ensuring the verifier runs and validates a known-good example.

**Validity Conditions**  
The necessary and sufficient conditions for a certificate to be accepted as meaningfully correct.

