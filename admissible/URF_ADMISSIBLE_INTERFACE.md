# URF-ADMISSIBLE — Formal Interface (Frozen)

Status: **FROZEN v1.0**

URF-ADMISSIBLE is the canonical decision interface for locality–capacity–accounting compliance.

Any process P must either:
- provide a valid URF-ADMISSIBLE certificate, or
- provide a certified NO witness (¬A/¬B/¬C/¬D).

No URF theorem may assume locality, capacity, or accounting without passing through this interface.

## Versioning
- v1.0: CutStrings primitive, entropy ΔH accounting, TM/RAM normalization, certified NO benchmarks.

Changes require:
- new semantic capability, and
- explicit version increment.

