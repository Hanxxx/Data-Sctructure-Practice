class UnionFindPathCompres():
    def __init__(self, n):
        self.__parent = [i for i in range(n)]
        self.__rank = [1 for _ in range(n)]

    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)
        if self.__rank[pid] > self.__rank[qid]:
            self.__parent[qid] = pid
        elif self.__rank[pid] < self.__rank[qid]:
            self.__parent[pid] = qid
        else:
            self.__parent[pid] = qid
            self.__rank[qid] += 1

    def find(self, p):
        cur = p
        while cur != self.__parent[cur]:
            self.__parent[cur] = self.__parent[self.__parent[cur]]
            cur = self.__parent[cur]
        return cur

    def isConnected(self, p, q):
        return self.__find(p) == self.__find(q)