class UnionFindPathCompress():
    def __init__(self, n):
        self.__parent = [i for i in range(n)]


    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)
        self.__parent[pid] = qid


    def find(self, p):
        cur = p
        while cur != self.__parent[cur]:
            cur = self.__parent[cur]
        root = cur
        cur = p
        while cur != root:
            tmp = self.__parent[cur]
            self.__parent[cur] = root
            cur = tmp
        return root


    def isConnected(self, p, q):
        return self.find(p) == self.find(q)