#!/usr/bin/env bash
set -euo pipefail

python3 tools/chronos_cert/chronos_cert_verify.py \
tools/chronos_cert/examples/xor_2bit_reveal/CERT.json
