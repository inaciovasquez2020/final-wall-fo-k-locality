#!/usr/bin/env bash
set -euo pipefail

sudo apt-get update
sudo apt-get install -y --no-install-recommends \
  git curl ca-certificates xz-utils unzip jq build-essential

# Lean via elan (pinned stable; you can replace later with exact toolchain)
if ! command -v elan >/dev/null 2>&1; then
  curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y
fi
export PATH="$HOME/.elan/bin:$PATH"

# Ensure lake exists
lean --version
lake --version || true

echo "postCreate OK"
