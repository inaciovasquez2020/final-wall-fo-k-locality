import json
import mpmath as mp
from compute_shs_interval import compute_S_HS_interval
from compute_tail_interval import T_HS_interval

mp.mp.dps = 80

def run(P):
    S = compute_S_HS_interval(P)
    T = T_HS_interval(P)
    total = S + T
    cert = {
        "P": int(P),
        "delta": "1/4",
        "precision_bits": mp.mp.dps,
        "S_HS_interval": str(S),
        "T_HS_interval": str(T),
        "sum_interval": str(total),
        "accept": bool(total < 1)
    }
    return cert

if __name__ == "__main__":
    import sys
    P = int(sys.argv[1])
    cert = run(P)
    out = f"zloop/certs/hs_cert_interval_P{P}.json"
    with open(out, "w") as f:
        json.dump(cert, f, indent=2)
    print(cert)
