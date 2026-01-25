import json, numpy as np, sys

with open(sys.argv[1]) as f:
    cert = json.load(f)

G = np.array(cert["gram_matrix"])
alpha = cert["alpha"]

eig = np.linalg.eigvalsh(G)
lam = eig[0]

print("lambda_min =", lam)
print("alpha =", alpha)

if lam >= alpha and alpha > 0:
    print("PASS: URF-SG certificate valid")
else:
    print("FAIL: spectral gap violated")

