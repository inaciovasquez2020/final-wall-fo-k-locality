import json
import numpy as np
from jsonschema import validate, ValidationError

# URF-SG Certificate Schema
schema = {
    "type": "object",
    "required": [
        "id",
        "operator",
        "hilbert_space",
        "projector",
        "alpha",
        "gram_matrix",
        "version"
    ],
    "properties": {
        "id": {"type": "string"},
        "operator": {"type": "string"},
        "hilbert_space": {"type": "string"},
        "projector": {"type": "string"},
        "alpha": {"type": "number", "exclusiveMinimum": 0},
        "gram_matrix": {
            "type": "array",
            "items": {
                "type": "array",
                "items": {"type": "number"}
            }
        },
        "version": {"type": "string"}
    }
}

# Example URF-SG Certificate
certificate_data = {
    "id": "URF-SG-BASE-2",
    "operator": "Laplacian on T2",
    "hilbert_space": "L2(T2)",
    "projector": "constants",
    "alpha": 1.0,
    "gram_matrix": [
        [1.0, 0.0],
        [0.0, 1.0]
    ],
    "version": "v1.0"
}

def verify_certificate(cert, sch):
    print(f"--- Initiating Verification for {cert['id']} ---")

    # Step A: Structural validation
    try:
        validate(instance=cert, schema=sch)
        print("✅ Structure: Valid (Matches URF-SG Schema)")
    except ValidationError as e:
        print(f"❌ Structure: Invalid! {e.message}")
        return False

    # Step B: Spectral validation
    matrix = np.array(cert["gram_matrix"])
    eigenvalues = np.linalg.eigvals(matrix)
    min_ev = np.min(eigenvalues)

    print(f"   Claimed Alpha: {cert['alpha']}")
    print(f"   Computed Min Eigenvalue: {min_ev}")

    if min_ev >= cert["alpha"]:
        print("✅ Physics: Valid (Spectral Gap maintained)")
        return True
    else:
        print("❌ Physics: FAILED (Gap smaller than claimed)")
        return False

if __name__ == "__main__":
    verify_certificate(certificate_data, schema)

