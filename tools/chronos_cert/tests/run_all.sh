#!/usr/bin/env bash
set -euo pipefail

echo running toy uniform certificate
python3 tools/chronos_cert/chronos_cert_verify.py \
tools/chronos_cert/examples/toy_uniform_bit_reveal/CERT.json

echo running xor certificate
python3 tools/chronos_cert/chronos_cert_verify.py \
tools/chronos_cert/examples/xor_2bit_reveal/CERT.json

echo all certificates passed
