#!/usr/bin/env bash
set -euo pipefail

# canonical: hash of (path, file-bytes) list, with stable sort
find .lake/build -type f -print0 \
| sort -z \
| xargs -0 shasum -a 256 \
| shasum -a 256 \
| awk '{print $1}'
