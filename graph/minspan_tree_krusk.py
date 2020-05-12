import heapq
from union_find.union_find_path_compress import UnionFindPathCompres as UF

class MinspanTreeKrusk():
    """
    Calculate the Minimum Span Tree of a grpah using Krusk algorithm
    O(ElogE)
    """
    def __init__(self, graph):
        self.graph = graph
        self.mst = []
        self.__krusk()


    def __krusk(self):
        self.uf = UF(self.graph.vertex_count)
        self.heap = []
        for i in range(self.graph.vertex_count):
            for edge in self.graph.get_neighbors(i):
                if edge.v < edge.w:
                    # Undirected graph
                    heapq.heappush(self.heap, edge)

        while self.heap and len(self.mst) < self.graph.vertex_count - 1:
            # Edges in MST = V - 1
            edge = heapq.heappop(self.heap)
            if not self.uf.isConnected(edge.v, edge.w):
                self.mst.append(edge)
                self.uf.union(edge.v, edge.w)
