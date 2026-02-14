This certificate is frozen and treated as authoritative.

Contents
hs_cert_interval_P200.json

Meaning
Interval arithmetic HS certificate
Condition verified: S_HS(P) + T_HS(P) < 1
Implied invariant: Zloop holds at cutoff P = 200

Reproduction
Run python zloop/scripts/run_certificate_interval.py 200
Compare output JSON byte-for-byte
