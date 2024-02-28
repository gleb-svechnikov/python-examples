import networkx as nx
import matplotlib.pyplot as plt

# Create a tree graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])

# Draw the tree
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=20, font_weight='bold')
plt.show()