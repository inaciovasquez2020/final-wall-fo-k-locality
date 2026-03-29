URF-Core Quickstart

Requirements:
- git
- bash
- pinned toolchains as specified in the repository

Steps:

1. Clone
   git clone https://github.com/inaciovasquez2020/urf-core.git
   cd urf-core

2. Build (if applicable)
   ./scripts/build.sh

3. Verify
   ./scripts/verify.sh

4. Reproduce checksum
   sha256sum artifacts/*

Expected Result:
Verification passes and hashes match published values.

Notes:
- No CI secrets required
- No network access required after clone
- Deterministic execution

