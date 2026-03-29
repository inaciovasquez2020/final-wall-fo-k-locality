#!/usr/bin/env bash
set -e
./tools/compile_dag.py
shasum -a 256 $(cat meta/MANIFEST.sha256 2>/dev/null | awk '{print $2}') > meta/MANIFEST.sha256
./tools/verify_manifest.py
