#!/usr/bin/env python3
import json, sys, datetime, hashlib
import numpy as np

def write_sha256(path_json: str, path_sha: str):
    h = hashlib.sha256()
    with open(path_json, "rb") as f:
        h.update(f.read())
    with open(path_sha, "w", encoding="utf-8") as g:
        g.write(h.hexdigest() + "  " + path_json.split("/")[-1] + "\n")

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    eps = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0

    L = np.diag([0.0] + [1.0]* (n-1))
    P = np.zeros((n,n))
    P[0,0] = 1.0

    cid = f"URF-SG-{n}-{int(1000*eps)}"
    now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    cert = {
        "schema_version": "1.0",
        "kind": "URF_SPECTRAL_GAP_CERT",
        "id": cid,
        "created_utc": now,
        "n": n,
        "epsilon": eps,
        "L": L.tolist(),
        "P": P.tolist(),
        "notes": "Toy example: defect space span(e0), unit gap on complement."
    }

    out = f"URF-SG-{cid}.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(cert, f, indent=2, sort_keys=True)

    write_sha256(out, out.replace(".json",".sha256"))
    print(out)

if __name__ == "__main__":
    main()

