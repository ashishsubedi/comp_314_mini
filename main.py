import matplotlib.pyplot as plt
import networkx as nx
import GraphLoader
import Algorithm

nV = 7
nE = 20
p = 0.2

G = GraphLoader.loadRandomGraphP(nV,p,weighted=True)
# G = GraphLoader.loadRandomGraphM(nV,nE,weighted=False)

print("Shortest average path is ",Algorithm.avg_shortest_path(G))


pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)


labels = {e: G[e[0]][e[1]]['weight'] for e in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


plt.show()
