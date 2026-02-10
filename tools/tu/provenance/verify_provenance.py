#!/usr/bin/env python3
import json, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
P = ROOT / "PROVENANCE.json"

REQ_TAGS = [
  "urf-tu-tvduality-main-v1",
  "urf-tu-tests-green-v1",
  "urf-tu-ci-nightly-v1",
  "urf-tu-stack-release-v1",
  "urf-tu-stack-signed-v1",
  "urf-tu-stack-freeze-v1",
  "urf-tu-stack-attested-v1",
  "urf-tu-stack-provenance-v1",
]

def sh(cmd):
  return subprocess.check_output(cmd, cwd=ROOT).decode().strip()

def read_text(path):
  try:
    return (ROOT / path).read_text(encoding="utf-8").strip()
  except FileNotFoundError:
    return ""

def fail(msg):
  print(f"ERROR: {msg}", file=sys.stderr)
  sys.exit(1)

def main():
  if not P.exists():
    fail("missing PROVENANCE.json")
  data = json.loads(P.read_text(encoding="utf-8"))

  for k in ["commit", "tags", "toolchain", "merkle", "image_digest"]:
    if k not in data:
      fail(f"missing key: {k}")

  head = sh(["git", "rev-parse", "HEAD"])
  if data["commit"] != head:
    fail(f"commit mismatch: PROVENANCE={data['commit']} HEAD={head}")

  tags = data["tags"]
  if sorted(tags) != sorted(REQ_TAGS):
    fail(f"tags mismatch: {tags}")

  toolchain = read_text("lean-toolchain")
  if data["toolchain"] != toolchain:
    fail("toolchain mismatch")

  merkle_root = read_text("manifest/merkle.root")
  if data.get("merkle", {}).get("root", "") != merkle_root:
    fail("merkle.root mismatch")

  image_digest = read_text("IMAGE_DIGEST.txt")
  if data.get("image_digest", "") != image_digest:
    fail("IMAGE_DIGEST mismatch")

  print("OK: PROVENANCE.json verified")

if __name__ == "__main__":
  main()
