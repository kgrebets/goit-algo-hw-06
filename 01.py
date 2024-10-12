import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

devices = ["Router", "TV", "Switch", "NAS", "Laptop", "PS4", "Desktop PC"]

edges = [
    ("Router", "TV"),
    ("Router", "Switch"),
    ("Switch", "NAS"),
    ("Switch", "Laptop"),
    ("Switch", "PS4"),
    ("Switch", "Desktop PC")
]

G.add_nodes_from(devices)
G.add_edges_from(edges)

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_of_nodes = dict(G.degree())
print("Stat:")
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print(f"Degree of nodes: {degree_of_nodes}")

pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2500, font_size=10, font_weight='bold', edge_color='gray')
plt.title("Local Network Graph")
plt.show()




