#!/usr/bin/env bash
set -euo pipefail

mkdir -p sigstore

docker image inspect "${IMAGE_REF}" --format '{{index .RepoDigests 0}}' \
  | tee sigstore/image.digest

mkdir -p sigstore
docker inspect --format='{{index .RepoDigests 0}}' urf-core:v1.0.1-core-frozen \
  | tee sigstore/image.digest

test -s sigstore/image.digest
