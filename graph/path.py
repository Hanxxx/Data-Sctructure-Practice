class Path():
    """
    find path from source node to all other nodes.
    """
    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.prev = [-1] * self.graph.vertex_count
        self.visited = set()
        self._find_path()


    def _find_path(self):
        self.__dfs(self.source)


    def __dfs(self, v):
        self.visited.add(v)
        for w in self.graph.get_neighbors(v):
            if w not in self.visited:
                self.prev[w] = v
                self.__dfs(w)

    
    def has_path(self, v):
        return v in self.visited


    def get_path(self, v):
        path = []
        cur = v
        while cur != -1:
            path.append(cur)
            cur = self.prev[cur]
        path.reverse()
        return path


    def print_path(self, v):
        path = self.get_path(v)
        for i in range(len(path)):
            print (path[i], end="")
            if i != len(path) - 1:
                print (" => ", end="")
        print()