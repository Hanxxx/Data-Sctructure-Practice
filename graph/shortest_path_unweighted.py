from path import Path
class ShortestPathUnweighted(Path):
    def __init__(self, graph, source):
        self.distance = [-1] * graph.vertex_count
        super().__init__(graph, source)


    def _find_path(self):
        self.__find_shortest_path()


    def __find_shortest_path(self):
        q = []
        q.append(self.source)
        self.visited.add(self.source)
        self.distance[self.source] = 0
        while q:
            cur = q.pop(0)
            for w in self.graph.get_neighbors(cur):
                if w not in self.visited:
                    self.visited.add(w)
                    self.prev[w] = cur
                    self.distance[w] = self.distance[cur] + 1
                    q.append(w)
            
        
    def get_distance(self, v):
        return self.distance[v]