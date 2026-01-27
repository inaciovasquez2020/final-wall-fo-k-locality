import json
import math

def make_t2_L(L):
    return {
        "standard": "URF-SG",
        "version": "v1.0",
        "cert_id": f"URF-SG-STRESS-T2-L-{L}",
        "statement": {
            "type": "spectral_gap",
            "quantity": "lambda_1(Delta_H | ker(Per)^⊥)",
            "lower_bound_exact": f"(2*pi/{L})^2"
        },
        "instance": {
            "geometry": {
                "name": "T^2_L",
                "model": "(R/LZ)×(R/Z)",
                "periods": [L, 1]
            },
            "hilbert_space": { "H": "L2(T^2_L)" },
            "operator": {
                "name": "Delta_H",
                "definition": "-(d^2/dx^2 + d^2/dy^2)",
                "domain": "H^2(T^2_L)"
            },
            "projection": {
                "name": "Per",
                "subspace": "span{1}",
                "kernel_orthogonal": "mean_zero"
            }
        },
        "checks": {
            "method": "closed_form",
            "exact_value": f"(2*pi/{L})^2",
            "notes": "Stress-test: gap collapses as L→∞"
        }
    }

for L in [1, 2, 4, 8, 16, 32]:
    cert = make_t2_L(L)
    path = f"verification/certs/{cert['cert_id']}.json"
    with open(path, "w") as f:
        json.dump(cert, f, indent=2)
    print("wrote", path)

