import networkx as nx

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

def run_scaling_test():
    R = 1
    sizes = [50, 100, 200, 400]

    print(f"Scaling test for R={R}")
    print("n | Path | Star | Random 3-regular")
    print("--------------------------------------")

    for n in sizes:
        path = nx.path_graph(n)
        star = nx.star_graph(n-1)
        rand = nx.random_regular_graph(3, n)

        chi_path = greedy_chromatic_number(power_graph(path, R))
        chi_star = greedy_chromatic_number(power_graph(star, R))
        chi_rand = greedy_chromatic_number(power_graph(rand, R))

        print(f"{n} | {chi_path} | {chi_star} | {chi_rand}")

if __name__ == "__main__":
    run_scaling_test()
