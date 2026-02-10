#!/usr/bin/env bash
set -euo pipefail

mkdir -p ci-artifacts

{
  echo "GITHUB_SHA=${GITHUB_SHA:-}"
  echo "RUN_ID=${GITHUB_RUN_ID:-}"
  echo "RUN_ATTEMPT=${GITHUB_RUN_ATTEMPT:-}"
  echo "OS=$(uname -a)"
  echo "PATH=$PATH"
  echo "LEAN=$(command -v lean || true)"
  echo "LAKE=$(command -v lake || true)"
  echo "LEAN_VERSION=$(lean --version | head -n1 || true)"
  echo "LAKE_VERSION=$(lake --version | head -n1 || true)"
  echo "ELAN_VERSION=$(elan --version 2>/dev/null || true)"
  echo "TOOLCHAIN_FILE=$(cat lean-toolchain 2>/dev/null || true)"
} > ci-artifacts/env.txt

shasum -a 256 ci-artifacts/env.txt | awk '{print $1}' > ci-artifacts/env.sha256
