import heapq
from heap.index_heap import IndexMinHeap

class MinspanTreePrim():
    """
    Calculate the Minimum Span Tree of a grpah using Prim algorithm
    mode 0: lazy prim O(ElogE)
    mode 1: better prim O(logV)
    Assume graph is connected and undirected.
    """

    def __init__(self, graph, mode = 0):
        self.graph = graph
        self.mst = []
        if mode == 0:
            self.__lazy_prim()
        elif mode == 1:
            self.__better_prim()
        else:
            raise ValueError(f'Mode {mode} is not supported.')


    def __lazy_prim_visit_helper(self, i):
        self.visited[i] = True
        for edge in self.graph.get_neighbors(i):
            if self.visited[edge.other(i)] == False:
                heapq.heappush(self.heap, edge)


    def __lazy_prim(self):
        self.visited = [False] * self.graph.vertex_count
        self.heap = []
        self.__lazy_prim_visit_helper(0)
        while self.heap:
            edge = heapq.heappop(self.heap)
            if self.visited[edge.v] == self.visited[edge.w]:
                continue
            else:
                self.mst.append(edge)
            if self.visited[edge.v] == False:
                self.__lazy_prim_visit_helper(edge.v)
            else:
                self.__lazy_prim_visit_helper(edge.w)


    def __better_prim_visit_helper(self, idx):
        self.visited[idx] = True
        for edge in self.graph.get_neighbors(idx):
            w = edge.other(idx)
            if self.visited[w] == False:
                if not self.heap.contains(w):
                    self.heap.push(w, edge)
                elif edge < self.heap.get_value(idx):
                    self.heap.modify(w, edge)


    def __better_prim(self):
        self.heap = IndexMinHeap(self.graph.vertex_count)
        self.visited = [False] * self.graph.vertex_count
        self.__better_prim_visit_helper(0)
        while not self.heap.is_empty():
            idx, edge = self.heap.pop()
            self.mst.append(edge)
            self.__better_prim_visit_helper(idx)
            