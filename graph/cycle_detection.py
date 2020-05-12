class CycleDetection():
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        

    def __dfs(self, v, stack):
        self.visited.add(v)
        stack.add(v)
        for w in self.graph.get_neighbors(v):
            if w not in self.visited:
                return self.__dfs(w, stack)      
            if w in stack:
                return True


    def has_cycle(self):
        for i in range(self.graph.vertex_count):
            if self.__dfs(i, set()):
                return True
        return False