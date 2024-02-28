import networkx as nx

# Create an undirected graph
G = nx.Graph()
G.add_edge("A", "B", weight=4)
G.add_edge("B", "D", weight=2)
G.add_edge("A", "C", weight=3)
G.add_edge("C", "D", weight=4)

# Find the shortest path between two nodes
shortest_path = nx.shortest_path(G, "A", "D", weight="weight")
print(shortest_path)