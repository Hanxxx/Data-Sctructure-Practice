from graph_common import GraphCommon
from edge import Edge

class SparseGraphWeighted(GraphCommon):
    def __init__(self, n, directed):
        self.n = n
        self.m = 0
        self.directed = directed
        self.__graph = [[] for _ in range(n)]

    
    def has_edge(self, v, w):
        for edge in self.__graph[v]:
            if edge.other(v) == w:
                return True
        return False

    
    def add_edge(self, v, w, weight):
        self.__graph[v].append(Edge(v, w, weight))
        if (v != w and not self.directed):
            self.__graph[w].append(Edge(w, v, weight))
        self.m += 1

    
    def get_neighbors(self, v):
        for edge in self.__graph[v]:
            yield edge
            
    
    def print_graph(self):
        print('print adjcent list')
        for i in range(self.n):
            print(f'vertex: {i}:', end="\t")
            for edge in self.__graph[i]:
                print(f'({i} -> {edge.other(i)}, {edge.weight})', end="\t")
            print()
