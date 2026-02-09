#!/usr/bin/env bash
set -euo pipefail

python3 tools/chronos_cert/validate_cert.py \
tools/chronos_cert/examples/toy_uniform_bit_reveal/CERT.json \
tools/chronos_cert/cert_schema.json

python3 tools/chronos_cert/validate_cert.py \
tools/chronos_cert/examples/xor_2bit_reveal/CERT.json \
tools/chronos_cert/cert_schema.json

echo schema validation passed
