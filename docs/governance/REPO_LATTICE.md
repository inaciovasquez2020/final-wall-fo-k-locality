Repository role lattice

Roles
CORE foundational semantics and proofs
PREFAB frozen executable packaging of CORE semantics
INFRA execution environment and reproducibility envelope
APP application repositories consuming certified logic

Order
CORE → PREFAB → INFRA → APP

Invariants
PREFAB may import CORE
PREFAB must not redefine CORE semantics
INFRA may depend on PREFAB and CORE
INFRA must not redefine certificate meaning
APP may depend on any upstream role but must not redefine semantics

Boundary contract
CORE exports semantic meaning and validity rules
PREFAB exports schemas and verifiers implementing CORE meaning
