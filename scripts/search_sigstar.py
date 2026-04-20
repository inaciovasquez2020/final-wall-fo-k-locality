from __future__ import annotations

from pathlib import Path
import csv
import random
from collections import deque
import networkx as nx

OUT = Path("artifacts/sigstar_search.csv")

L = 8
R_EDGE = 2
R_VERTEX = 2
LIFT_SIZES = range(2, 6)
SEED_RANGE = range(4)


def normalize_edge(a, b):
    return (a, b) if repr(a) <= repr(b) else (b, a)


def undirected_cycle_edges(cycle):
    edges = []
    for i in range(len(cycle)):
        a = cycle[i]
        b = cycle[(i + 1) % len(cycle)]
        edges.append(normalize_edge(a, b))
    return frozenset(edges)


def all_simple_cycles_upto_length(G: nx.Graph, max_len: int):
    DG = nx.DiGraph()
    DG.add_nodes_from(G.nodes())
    for u, v in G.edges():
        DG.add_edge(u, v)
        DG.add_edge(v, u)
    seen = set()
    out = []
    for cyc in nx.simple_cycles(DG):
        if len(cyc) < 3 or len(cyc) > max_len:
            continue
        edge_set = undirected_cycle_edges(cyc)
        key = tuple(sorted(edge_set, key=repr))
        if len(edge_set) != len(cyc):
            continue
        if key in seen:
            continue
        seen.add(key)
        out.append(edge_set)
    return out


def ball_nodes(G: nx.Graph, sources, radius: int):
    dist = {}
    q = deque()
    for s in sources:
        dist[s] = 0
        q.append(s)
    while q:
        x = q.popleft()
        if dist[x] == radius:
            continue
        for y in G.neighbors(x):
            if y not in dist:
                dist[y] = dist[x] + 1
                q.append(y)
    return set(dist)


def ball_edges(G: nx.Graph, sources, radius: int):
    nodes = ball_nodes(G, sources, radius)
    return {
        normalize_edge(u, v)
        for u, v in G.edges(nodes)
        if u in nodes and v in nodes
    }


def gf2_rank(edge_subsets, edge_order):
    rows = []
    pos = {e: i for i, e in enumerate(edge_order)}
    for subset in edge_subsets:
        mask = 0
        for e in subset:
            if e in pos:
                mask ^= 1 << pos[e]
        if mask:
            rows.append(mask)
    rank = 0
    while rows:
        pivot = max(rows)
        rows.remove(pivot)
        rank += 1
        lead = pivot.bit_length() - 1
        new_rows = []
        for row in rows:
            if (row >> lead) & 1:
                row ^= pivot
            if row:
                new_rows.append(row)
        rows = new_rows
    return rank


def sigstar_motif_signature(G: nx.Graph, u, v, max_len: int, r_edge: int):
    eball = ball_edges(G, [u, v], r_edge)
    cycles = all_simple_cycles_upto_length(G, max_len)
    counts = []
    for ell in range(3, max_len + 1):
        c = 0
        for cyc in cycles:
            if len(cyc) == ell and cyc & eball:
                c += 1
        counts.append(c)
    return tuple(counts)


def sigstar_dim(sig):
    return sum(1 for x in sig if x != 0)


def anchored_rank(G: nx.Graph, u, v, max_len: int, r_edge: int):
    eball = sorted(ball_edges(G, [u, v], r_edge), key=repr)
    cycles = [
        cyc for cyc in all_simple_cycles_upto_length(G, max_len)
        if cyc & set(eball)
    ]
    return gf2_rank(cycles, eball)


def vertex_overlap_rank(G: nx.Graph, x, max_len: int, r_vertex: int):
    vball = sorted(ball_edges(G, [x], r_vertex), key=repr)
    cycles = [
        cyc for cyc in all_simple_cycles_upto_length(G, max_len)
        if any(x in e for e in cyc)
    ]
    return gf2_rank(cycles, vball)


def random_n_lift(base: nx.Graph, n: int, seed: int) -> nx.Graph:
    rng = random.Random(seed)
    H = nx.Graph()
    for u in base.nodes():
        for i in range(n):
            H.add_node((u, i))
    for u, v in base.edges():
        perm = list(range(n))
        rng.shuffle(perm)
        for i in range(n):
            H.add_edge((u, i), (v, perm[i]))
    return H


def family_instances():
    yield ("cube", "cube", nx.cubical_graph())
    yield ("petersen", "petersen", nx.petersen_graph())
    yield ("heawood", "heawood", nx.heawood_graph())
    yield ("dodecahedral", "dodecahedral", nx.dodecahedral_graph())
    base = nx.complete_graph(4)
    for n in LIFT_SIZES:
        for seed in SEED_RANGE:
            yield (f"K4-lift-{n}", f"seed-{seed}", random_n_lift(base, n, seed))


def profile_count_and_max_dim(G: nx.Graph):
    sigs = []
    max_rank = 0
    for u, v in G.edges():
        sig = sigstar_motif_signature(G, u, v, L, R_EDGE)
        sigs.append(sig)
        max_rank = max(max_rank, anchored_rank(G, u, v, L, R_EDGE))
    return len(set(sigs)), max(sigstar_dim(s) for s in sigs), max_rank


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for family, instance, G in family_instances():
        profile_classes, max_sigstar_dim, max_anchored_rank = profile_count_and_max_dim(G)
        max_vertex_rank = max(vertex_overlap_rank(G, x, L, R_VERTEX) for x in G.nodes())
        rows.append(
            {
                "family": family,
                "instance": instance,
                "n_vertices": G.number_of_nodes(),
                "n_edges": G.number_of_edges(),
                "ordered_edge_profile_classes": profile_classes,
                "max_sigstar_dim": max_sigstar_dim,
                "max_anchored_rank": max_anchored_rank,
                "max_vertex_overlap_rank": max_vertex_rank,
            }
        )

    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "family",
                "instance",
                "n_vertices",
                "n_edges",
                "ordered_edge_profile_classes",
                "max_sigstar_dim",
                "max_anchored_rank",
                "max_vertex_overlap_rank",
            ],
        )
        w.writeheader()
        w.writerows(rows)

    best = {}
    for row in rows:
        fam = row["family"]
        key = (
            row["ordered_edge_profile_classes"],
            row["max_sigstar_dim"],
            row["max_anchored_rank"],
        )
        if fam not in best or key > (
            best[fam]["ordered_edge_profile_classes"],
            best[fam]["max_sigstar_dim"],
            best[fam]["max_anchored_rank"],
        ):
            best[fam] = row

    for fam in sorted(best):
        row = best[fam]
        print(
            fam,
            row["instance"],
            row["ordered_edge_profile_classes"],
            row["max_sigstar_dim"],
            row["max_anchored_rank"],
            row["max_vertex_overlap_rank"],
        )


if __name__ == "__main__":
    main()
