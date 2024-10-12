import networkx as nx

G = nx.Graph()

G.add_edge('Router', 'TV', weight=2)
G.add_edge('Router', 'Switch', weight=1)
G.add_edge('Switch', 'NAS', weight=3)
G.add_edge('Switch', 'Laptop', weight=2)
G.add_edge('Switch', 'PS4', weight=4)
G.add_edge('Switch', 'Desktop PC', weight=5)

def print_shortest_path(source, target):
    path = nx.shortest_path(G, source=source, target=target, weight='weight')
    weight = nx.shortest_path_length(G, source=source, target=target, weight='weight')
    path_str = ' -> '.join(path)
    print(f"{source:<10} -> {target:<10}, [Weight: {weight}], [Path: {path_str}]")

devices = ['Router', 'TV', 'Switch', 'NAS', 'Laptop', 'PS4', 'Desktop PC']

for i in range(len(devices)):
    print("")
    for j in range(len(devices)):
        if i != j:
            print_shortest_path(devices[i], devices[j])

