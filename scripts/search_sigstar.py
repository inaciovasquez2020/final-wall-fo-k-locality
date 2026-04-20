from pathlib import Path
import csv

OUT = Path("artifacts/sigstar_search.csv")

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["family", "instance", "ordered_edge_profile_classes", "max_sigstar_dim"])
        # populate from external search implementation
    print(OUT)

if __name__ == "__main__":
    main()
