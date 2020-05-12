class Component():
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.__component_count = 0
        self.__component_id = [-1] * graph.vertex_count

        for i in range(graph.vertex_count):
            if self.__component_id[i] == -1:
                self.__dfs(i)
                self.__component_count += 1

    @property
    def component_count(self):
        return self.__component_count


    def __dfs(self, v):
        self.__component_id[v] = self.__component_count
        for w in self.graph.get_neighbors(v):
            if self.__component_id[w] == -1:
                self.__dfs(w)

    
    def is_connected(v, w):
        return self.__component_id[v] == self.__component_id[w]