
class UnionFindQuickFind():
    """
    Union Find: array implementation
    """
    def __init__(self, n):
        self.__ids = [i for i in range(n)]


    def find(self, p):
        return self.__ids[p]


    def isConnected(self, p, q):
        return self.find(p) == self.find(q)


    def union(self, p, q):
        pid = self.__ids[p]
        qid = self.__ids[q]
        if pid == qid:
            return
        for i in range(len(self.__ids)):
            if self.__ids[i] == qid:
                self.__ids[i] = pid
