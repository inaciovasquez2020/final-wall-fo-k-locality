#!/usr/bin/env bash
set -euo pipefail

curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh -s -- -y
echo "$HOME/.elan/bin" >> "$GITHUB_PATH" 2>/dev/null || true
source "$HOME/.elan/env"

lean --version
lake --version

command -v lean
command -v lake
