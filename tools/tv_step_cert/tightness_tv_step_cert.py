import json
import sys
from typing import Any

def die(msg: str) -> None:
  raise SystemExit(f"TIGHTNESS_FAIL: {msg}")

def load(path: str) -> Any:
  with open(path, "r", encoding="utf-8") as f:
    return json.load(f)

def main() -> None:
  if len(sys.argv) != 2:
    die("usage: tightness_tv_step_cert.py CERT.json")
  cert = load(sys.argv[1])

  tv = cert.get("tv_bound")
  lhs = cert.get("lhs_abs_integral")
  if not isinstance(tv, (int, float)) or not isinstance(lhs, (int, float)):
    die("missing tv_bound or lhs_abs_integral numeric fields")

  if tv <= 0:
    die("tv_bound must be positive")

  ratio = lhs / tv
  out = {
    "lhs_abs_integral": lhs,
    "tv_bound": tv,
    "tightness_ratio": ratio
  }
  print(json.dumps(out, sort_keys=True))

  if ratio < -1e-12:
    die("ratio negative")
  if ratio > 1.0000001:
    die("ratio exceeds bound")

if __name__ == "__main__":
  main()
