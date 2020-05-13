from heap.index_heap import IndexMinHeap
class Dijkstra():
    """
    Calculate shortest path from source node to other nodes in the graph.
    Assume all the edge in graph have positive weight.
    """
    def __init__(self, grpah, source):
        self.graph = grpah
        self.source = source
        self.__Dijkstra()

    
    def __Dijkstra(self):
        self.heap = IndexMinHeap(self.graph.vertex_count)
        self.visited = set()
        self.distance = [-1] * self.graph.vertex_count
        self.prev = [-1] * self.graph.vertex_count
        self.heap.push(self.source, 0)
        while not self.heap.is_empty() and len(self.visited) < self.graph.vertex_count:
            idx, dist = self.heap.pop()     # Pop the node with shortest path to source currently among all the unvisited nodes
            self.distance[idx] = dist       # We can prove this path is the shortest. 
            self.visited.add(idx)           # That makes this node "visited" (found shortest path)
            for edge in self.graph.get_neighbors(idx):  # update the distance value of rest of the nodes (relaxation)
                w = edge.other(idx)
                if w in self.visited:
                    continue
                if self.heap.contains(w):
                    if dist + edge.weight < self.heap.get_value(w):
                        self.prev[w] = idx
                        self.heap.modify(w, dist + edge.weight)
                else:
                    self.prev[w] = idx
                    self.heap.push(w, dist + edge.weight)
            