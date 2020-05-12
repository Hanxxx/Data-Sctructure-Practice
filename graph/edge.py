class Edge():
    """
    Weighted Edge
    """
    def __init__(self, v, w, weight):
        self.__v = v
        self.__w = w
        self.__weight = weight


    @property
    def v(self):
        return self.__v
    
    
    @property
    def w(self):
        return self.__w


    @property  
    def weight(self):
        return self.__weight


    def other(self, v):
        """
        return the other vertex of this edge
        """
        if v == self.__v:
            return self.__w
        elif v == self.__w:
            return self.__v
        else:
            raise ValueError("Not in Edge")

    
    def __lt__(self, other):
        return self.weight < other.weight

    
    def __gt__(self, other):
        return self.weight > other.weight


    def __le__(self, other):
        return self.weight <= other.weight
    

    def __ge__(self, other):
        return self.weight >= other.weight
