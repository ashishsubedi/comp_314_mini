import networkx as nx
import math
from collections import OrderedDict
import heapq
    

def dijkstra(G: nx.Graph,s,dest):
    '''
    Find Dijkstra's shortest path algorithm
    G = Graph
    s = source node/vertex
    dest = Path to destinationL; If dest == 'all' then it will return the destination for all other the nodes
    '''
    if (not nx.is_connected(G)):
        print("Graph is not connected.")
  
    d = {}
    for v in G.nodes:
        d[v] = 0 if s == v else math.inf


    Q = OrderedDict(sorted(d.items(),key=lambda t: t[1]))

    while len(Q)>0:
        v,_ = Q.popitem(last=False)
        
        for u in G[v]:
            if(d[v]+G[v][u]['weight'] <= d[u] and d[v] != math.inf):
                d[u] = d[v]+G[v][u]['weight']
                Q[u] = d[u]

                Q = OrderedDict(sorted(Q.items(),key=lambda t: t[1]))


    
    if(dest == 'all'):
    
        costDict = {}
        for u in G.nodes:
            costDict[u] = d[u]
        return {
            'cost': costDict
        }
        
    return {'cost': d[dest] }   

def dijkstraV2(G: nx.Graph,s,dest):
    '''
    Find Dijkstra's shortest path algorithm
    G = Graph
    s = source node/vertex
    dest = Path to destinationL; If dest == 'all' then it will return the destination for all other the nodes
    '''

    if (not nx.is_connected(G)):
        print("Graph is not connected.")

    #heap data is in form (cost, vertex)
    d = {}
    pq = []
    for v in G.nodes:
        d[v] = 0 if s == v else math.inf
        heapq.heappush(pq,(d[v],v))



    while len(pq)>0:
  
        _,v = heapq.heappop(pq)
        for u in G[v]:
            if(d[v]+G[v][u]['weight'] <= d[u] and d[v] != math.inf):
                d[u] = d[v]+G[v][u]['weight']
                heapq.heappush(pq,(d[u],u))

                
    
    if(dest == 'all'):
    
        costDict = {}
        for u in G.nodes:
            costDict[u] = d[u]
        return {
            'cost': costDict
        }
        
    return {'cost': d[dest] }    

def avg_shortest_path(G:nx.Graph):
    '''
        Calculate the average shortest path between all the vertices of the graph
        G: Graph to calculate the average shortest path of
    '''
    #Algorithm
    #1 For all nodes v
        #1.1 Find dijkstra cost from the node v
        #1.2 For all path from u where u>=v
            #1.1.1 Add the path length to sum of all path lengths
        #1.3 Calculate the average for the node and add it to the total average
    #2 Display the total average

    #Check if graph is connected
    if (not nx.is_connected(G)):
        print("Graph is not connected.")
        return math.inf
    n = G.number_of_nodes()
    vertices = set(sorted(G.nodes))
    totalPathLength = 0
    for i in G.nodes:
        pathLength = 0

        result = dijkstra(G,i,'all')

        vertices.remove(i)
        
        for j in vertices:
            
            pathLength += result['cost'][j]

        totalPathLength += (2/(n*(n+1)))*pathLength
        
    return totalPathLength



