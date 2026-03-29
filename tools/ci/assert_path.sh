#!/usr/bin/env bash
set -euo pipefail

echo "PATH=$PATH"
command -v lean
command -v lake
lake --version
lean --version
