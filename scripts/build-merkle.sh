#!/usr/bin/env bash
set -euo pipefail

git ls-files -z | LC_ALL=C sort -z | while IFS= read -r -d '' f; do
  sha="$(shasum -a 256 "$f" | awk '{print $1}')"
  printf "%s  %s\n" "$sha" "$f"
done > transparency/files.sha256

shasum -a 256 transparency/files.sha256 | awk '{print $1}' > transparency/merkle.root
