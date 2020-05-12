from graph_common import GraphCommon

class SparseGraph(GraphCommon):
    """
    Sparse graph: Adjacency List Implementation
    """
    def __init__(self, n, directed):
        self.n = n
        self.m = 0
        self.directed = directed
        self.__graph = [[] for _ in range(n)]


    def has_edge(self, v, w):
        return w in self.__graph[v]

    
    def add_edge(self, v, w):
        self.__graph[v].append(w)
        if (v != w and not self.directed):
            self.__graph[w].append(v)
        self.m += 1
        
    def get_neighbors(self, v):
        """
        Generator for neighbor iteration
        """
        for w in self.__graph[v]:
            yield w

    
    def print_grpah(self):
        print('print adjcent list')
        for i in range(self.n):
            print(f'vertex: {i}:', end="\t")
            for w in self.__graph[i]:
                print(w, end="\t")
            print()
