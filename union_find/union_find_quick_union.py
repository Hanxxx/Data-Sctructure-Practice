class UnionFindQuickUnion():
    def __init__(self, n):
        self.__parent = [i for i in range(n)]

    def union(self, p, q):
        self.__parent[p] = self.__parent[q]

    def find(self, p):
        cur = p
        while cur != self.__parent[cur]:
            cur = self.__parent[cur]
        return cur

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)