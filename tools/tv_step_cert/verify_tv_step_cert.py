#!/usr/bin/env python3
import json
import sys

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_tv_step_cert.py CERT.json")

    with open(sys.argv[1], "r", encoding="utf-8") as fh:
        cert = json.load(fh)

    if cert["type"] != "TV_STEP_DUAL_CERT":
        raise SystemExit("VERIFY_FAIL wrong type")

    lhs = cert["lhs_abs_integral"]
    rhs = cert["rhs_tv_bound"]

    if lhs <= rhs + 1e-12:
        print("VERIFY_OK")
    else:
        raise SystemExit("VERIFY_FAIL inequality violated")

if __name__ == "__main__":
    main()
