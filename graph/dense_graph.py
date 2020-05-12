from graph_common import GraphCommon

class DenseGraph(GraphCommon):
    """
    Dense graph with no parallel edges
    Implementation: Adjacency Matrix
    """
    def __init__(self, n, directed):
        # initialize graph with node number n
        self.n = n
        self.m = 0
        self.directed = directed
        self.__graph = [[0] * n for _ in range(n)]

    
    def has_edge(self, v, w):
        return self.__graph[v][w] == 1


    def add_edge(self, v, w):
        if self.has_edge(v, w):
            return
        self.__graph[v][w] = 1
        if (not self.directed):
            self.__graph[w][v] = 1
        self.m += 1


    def print_graph(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.__graph[i][j], end="\t")
            print()


    def get_neighbors(self, v):
        """
        Generator for neighbor iteration
        """
        for i in range(self.n):
            if self.__graph[v][i] == 1:
                yield i