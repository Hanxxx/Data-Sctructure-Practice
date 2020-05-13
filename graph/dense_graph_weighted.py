from graph_common import GraphCommon
from edge import Edge

class DenseGrpahWeighted(GraphCommon):
    """
    Dense graph with no parallel edges
    New come edge will override the previous edge
    Implementation: Adjacency Matrix
    """
    def __init__(self, n, directed):
        self.n = n
        self.m = 0
        self.directed = directed
        self.__graph = [[None] * n for _ in range(n)]

    
    def has_edge(self, v, w):
        return not self.__graph[v][w] == None


    def add_edge(self, v, w, weight):
        if not self.has_edge(v, w):
            self.m += 1
        self.__graph[v][w] = Edge(v, w, weight)
        if (not self.directed):
            self.__graph[w][v] = Edge(w, v, weight)


    def print_graph(self):
        print('Print Adjacency Matrix')
        for i in range(self.n):
            for j in range(self.n):
                weight = 'None' if self.__graph[i][j] == None \
                    else f'{self.__graph[i][j].weight:.2f}'
                print(weight, end="\t")
            print()


    def get_neighbors(self, v):
        for i in range(self.n):
            if self.__graph[v][i] != None:
                yield self.__graph[v][i]