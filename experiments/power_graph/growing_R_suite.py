import networkx as nx
import math
import numpy as np

def power_graph(G, R):
    H = nx.Graph()
    H.add_nodes_from(G.nodes())
    for u in G.nodes():
        lengths = nx.single_source_shortest_path_length(G, u, cutoff=2*R)
        for v, d in lengths.items():
            if 0 < d <= 2*R:
                H.add_edge(u, v)
    return H

def greedy_chromatic_number(G):
    coloring = nx.coloring.greedy_color(G, strategy="largest_first")
    return max(coloring.values()) + 1

sizes = [100, 200, 400]
for n in sizes:
    G = nx.random_regular_graph(3, n)
    diam = nx.diameter(G)
    R = math.ceil(diam / 2)
    H = power_graph(G, R)
    chi = greedy_chromatic_number(H)
    print(f"n={n}, diameter={diam}, R={R}, chi={chi}")
