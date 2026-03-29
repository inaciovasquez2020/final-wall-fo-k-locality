#!/usr/bin/env bash
set -euo pipefail

tag="${1:?usage: $0 <tag>}"
tsa_url="${TSA_URL:-http://timestamp.digicert.com}"

mkdir -p tsa/"$tag"

stamp_one () {
  in="$1"
  base="$(basename "$in")"
  out="tsa/${tag}/${base}.tsr"
  echo "Stamping $in -> $out"
  openssl ts -query -data "$in" -sha256 -cert > /tmp/tsq.bin
  curl -fsS -H "Content-Type: application/timestamp-query" --data-binary @/tmp/tsq.bin "$tsa_url" > "$out"
  # basic parse check
  openssl ts -reply -in "$out" -text >/dev/null
}

stamp_one "transparency/merkle.root"
stamp_one "transparency/files.sha256"
stamp_one "tuple/TUPLE_${tag}.txt"
