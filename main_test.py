import matplotlib.pyplot as plt
import networkx as nx
import GraphLoader
import Algorithm
import time
nV = 5
# nE = 20
p = 0.2

# time_random_graph = {}
# time_dijkstra = {}

# for i in range(2,500,20):
#     nV = i
    # start = time.time_ns()
G = GraphLoader.loadRandomGraphP(nV,p,weighted=True)
    # end = time.time_ns()
    
    # time_random_graph[i] = end-start
# G = GraphLoader.loadRandomGraphM(nV,nE,weighted=False)
    # start = time.time()

print(G.nodes)
print(G.edges)
print(Algorithm.dijkstra(G,'1',str(nV)))
    # end = time.time()
    # time_dijkstra[i] = end-start
# print("Shortest average path is ",Algorithm.avg_shortest_path(G))
# print("Shortest average path is ",nx.average_shortest_path_length(G))

# print(time_random_graph)
# x = time_random_graph.keys()
# y = time_random_graph.values()
# plt.plot(x,y)
# x = time_dijkstra.keys()

# y = time_dijkstra.values()

# plt.plot(x,y)

# plt.show()

pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)


labels = {e: G[e[0]][e[1]]['weight'] for e in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


plt.show()
