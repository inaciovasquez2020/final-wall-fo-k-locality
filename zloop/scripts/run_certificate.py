import json
from compute_shs import compute_S_HS
from compute_tail import T_HS

def run(P):
    S = compute_S_HS(P)
    T = T_HS(P)
    cert = {
        "P": P,
        "delta": 0.25,
        "S_HS": float(S),
        "T_HS": float(T),
        "sum": float(S + T),
        "accept": bool(S + T < 1)
    }
    return cert

if __name__ == "__main__":
    import sys
    P = int(sys.argv[1])
    cert = run(P)
    out = f"zloop/certs/hs_cert_P{P}.json"
    with open(out, "w") as f:
        json.dump(cert, f, indent=2)
    print(cert)
