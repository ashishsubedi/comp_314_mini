import networkx as nx
import re
import os
import random

                
def loadRandomGraphP(nV: int, p: float, weighted=False, weightRange=(1,10)) -> nx.Graph:
    '''
        Generate Random Graph of nV vertices
        nv : int
            number of vertices
        p: float
            probability threshold for connection (0-1). Higher value will generate strongly connected graph
        weighted: Boolean, default: False
            If true, weighted graph will be generated
        weightRange: (int,int) default: (1,10)
            If weighted graph, weight will be randomly generated from the range (last element exclusive)
    '''
    assert p>=0, "p out of range"
    assert p <= 1, "p out of range"
    G = nx.Graph()
    G.add_nodes_from([str(i+1) for i in range(nV)])
   
    for u in G.nodes():
        for v in G.nodes():
            if u != v:# No self loop allowed
                if random.random() <= p:
                    if(weighted):
                        assert len(weightRange) == 2, f"Weight Range doesn't have 2 values {weightRange}"
                        w = random.randint(weightRange[0],weightRange[1])
                        G.add_edge(str(u),str(v),weight=float(w))
                    else:
                        G.add_edge(str(u),str(v),weight=float(1))
    
    return G

def loadRandomGraphM(nV: int, nE: float, weighted=False, weightRange=(1,10)) -> nx.Graph:
    '''
        Generate Random Graph of nV vertices with nE edges
        nv : int
            number of vertices
        nE: int
            number of edges
        weighted: Boolean, default: False
            If true, weighted graph will be generated
        weightRange: (int,int) default: (1,10)
            If weighted graph, weight will be randomly generated from the range (last element exclusive)
    '''
    assert nE <= nV*(nV-1)/2, "Exceeds maximum number of edges for undirected simple graph"
    G = nx.Graph()
    G.add_nodes_from([str(i+1) for i in range(nV)])
    p = 1/nV
    countEdge = 0

    while countEdge < nE:
        u = random.sample(G.nodes,1)[0]
        v = random.sample(G.nodes,1)[0]
        if u != v and (u,v) not in G.edges(): # No self loop allowed
            if random.random() <= p :
                if(weighted):
                    assert len(weightRange) == 2, f"Weight Range doesn't have 2 values {weightRange}"
                    w = random.randint(weightRange[0],weightRange[1])
                    G.add_edge(str(u),str(v),weight=float(w))
                else:
                    G.add_edge(str(u),str(v),weight=float(1))
                countEdge += 1
                if countEdge >= nE:
                    return G
        


if __name__ == "__main__":

    G = loadRandomGraphP(10,0.8,True,(10,10))
  