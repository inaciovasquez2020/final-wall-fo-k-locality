import json
import numpy as np
from pathlib import Path
from datetime import datetime, timezone

def make_cert(n: int, gap: float) -> dict:
    # Diagonal matrix: eigenvalues [0, gap, gap, ..., gap]
    P = np.zeros((n, n), dtype=float)
    for i in range(1, n):
        P[i, i] = gap

    created_utc = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    return {
        "standard": "URF-SG",
        "version": "v1.0",
        "cert_id": f"URF-SG-NUM-{n}-{str(gap).replace('.','p')}",
        "admissible_class": "finite_numeric",
        "statement": {
            "type": "spectral_gap",
            "quantity": "lambda_1(P | ker(P)^⊥)",
            "lower_bound": gap
        },
        "instance": {
            "geometry": {"name": "FiniteDimToy", "model": f"R^{n}"},
            "hilbert_space": {"H": f"R^{n}"},
            "operator": {
                "name": "P",
                "definition": "Diagonal numeric toy operator",
                "domain": f"R^{n}"
            },
            "projection": {
                "name": "Per",
                "subspace": "span{e0}",
                "kernel_orthogonal": f"span{{e1,...,e{n-1}}}"
            }
        },
        "P": P.tolist(),
        "n": n,
        "created_utc": created_utc,
        "notes": "Generated diagonal toy certificate: eigenvalues [0,gap,...,gap].",
        "checks": {
            "method": "numeric",
            "notes": "Verifier computes smallest nonzero eigenvalue and checks >= lower_bound."
        }
    }

def main():
    out = Path("verification/certs")
    out.mkdir(parents=True, exist_ok=True)

    for n in [4, 8, 16]:
        for gap in [0.5, 1.0, 2.0]:
            cert = make_cert(n, gap)
            path = out / f"{cert['cert_id']}.json"
            with open(path, "w", encoding="utf-8") as f:
                json.dump(cert, f, indent=2)
            print("wrote", path)

if __name__ == "__main__":
    main()

