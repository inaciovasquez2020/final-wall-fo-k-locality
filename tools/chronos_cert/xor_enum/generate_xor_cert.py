#!/usr/bin/env python3
import itertools, json, math, os

def H(p):
    s=0.0
    for x in p:
        if x>0: s-=x*math.log2(x)
    return s

def main():
    out_dir="tools/chronos_cert/examples/xor_enum_3vars"
    os.makedirs(out_dir,exist_ok=True)
    out_path=f"{out_dir}/CERT.json"

    sols=[(0,1,0),(1,0,1)]
    M=len(sols)

    P0=[1/M]*M
    P1=P0[:]
    P2=[1.0,0.0]

    H0=H(P0)
    H1=H(P1)
    H2=H(P2)

    C=max(H0-H1,H1-H2)

    cert={
      "instance":{"name":"xor_enum_3vars","n_states":M,"H0_lower":H0},
      "bound":{"C":C,"epsilon":H2},
      "trace":{"posteriors":[{"p":P0},{"p":P1},{"p":P2}]}
    }

    with open(out_path,"w") as f:
        json.dump(cert,f,indent=2)

    print("wrote",out_path)
    print("H:",H0,H1,H2)
    print("C:",C)

if __name__=="__main__":
    main()
