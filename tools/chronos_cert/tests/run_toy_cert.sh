#!/usr/bin/env bash
set -euo pipefail

python3 tools/chronos_cert/chronos_cert_verify.py \
tools/chronos_cert/examples/toy_uniform_bit_reveal/CERT.json
