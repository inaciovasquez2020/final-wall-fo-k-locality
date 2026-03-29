URF One-Command Lab Machine Bootstrap

Goal
Reproduce full URF dev + verification environment on clean machine.

Command
curl -s https://raw.githubusercontent.com/inaciovasquez2020/urf-templates/main/bootstrap/full_urf_install.sh | bash

Installs
- Lean toolchain pinned version
- Python venv + pinned deps
- URF repos clone
- Hooks install
- Templates install
- Workspace init
- CI local verifier

Post-Install Verification
lake build
run verify_manifest.py
run compile_dag.py
run verify_dag.py

Guarantee
Deterministic environment replication.
