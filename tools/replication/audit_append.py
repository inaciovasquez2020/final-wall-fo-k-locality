import json
import os
import subprocess
import sys
import time
import hashlib
from pathlib import Path

def die(msg: str) -> None:
  raise SystemExit(f"AUDIT_FAIL: {msg}")

def sh(cmd):
  r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
  if r.returncode != 0:
    sys.stdout.write(r.stdout)
    die("command failed: " + " ".join(cmd))
  return r.stdout

def sha256_bytes(b: bytes) -> str:
  return hashlib.sha256(b).hexdigest()

def sha256_file(p: Path) -> str:
  h = hashlib.sha256()
  with p.open("rb") as f:
    for chunk in iter(lambda: f.read(1024 * 1024), b""):
      h.update(chunk)
  return h.hexdigest()

def main() -> None:
  repo = "inaciovasquez2020/urf-core"
  root = Path(".").resolve()

  head = sh(["git", "rev-parse", "HEAD"]).strip()
  now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

  cmds = [
    ["python3", "tools/tu/tu_seymour_verify.py", "tools/tu/testdata/network_minimal_CERT.json"],
    ["python3", "tools/tv_cert/generate_tv_finite_cert.py", "8", "/tmp/tv_finite_n8_CERT.json"],
    ["python3", "tools/tv_cert/verify_tv_finite_cert.py", "/tmp/tv_finite_n8_CERT.json"],
    ["python3", "tools/tv_step_cert/generate_tv_step_cert.py", "10", "/tmp/tv_step_n10_CERT.json"],
    ["python3", "tools/tv_step_cert/verify_tv_step_cert.py", "/tmp/tv_step_n10_CERT.json"],
    ["python3", "tools/tv_step_cert/tightness_tv_step_cert.py", "/tmp/tv_step_n10_CERT.json"],
    ["lake", "build"]
  ]

  runs = []
  for c in cmds:
    out = sh(c)
    runs.append({
      "cmd": c,
      "stdout_sha256": sha256_bytes(out.encode("utf-8"))
    })

  key_files = [
    ".github/workflows/verify-lean-and-certs.yml",
    "meta/obstructions/TV_CRI.md",
    "meta/deps/DEPENDENCY_GRAPH.json",
    "docs/urfc/CERT_SOUNDNESS.md"
  ]

  artifacts = {}
  for rel in key_files:
    p = root / rel
    if not p.exists():
      die("missing artifact: " + rel)
    artifacts[rel] = sha256_file(p)

  entry = {
    "repo": repo,
    "ref": head,
    "utc": now,
    "runner": {
      "os": os.uname().sysname,
      "machine": os.uname().machine
    },
    "runs": runs,
    "artifacts_sha256": artifacts
  }

  log_path = root / "meta/replication/TPR_LOG.jsonl"
  log_path.parent.mkdir(parents=True, exist_ok=True)
  with log_path.open("a", encoding="utf-8") as f:
    f.write(json.dumps(entry, sort_keys=True) + "\n")

  print("AUDIT_OK")

if __name__ == "__main__":
  main()
