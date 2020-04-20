class MaxHeap(object):
    def __init__(self, nums = None):
        if nums == None:
            self.__data = []
        else:
            self.__data = nums[:]
            self.__heapify()


    def __heapify(self):
        n = len(self.__data)
        if n <= 1:
            return
        for i in range((n - 2) // 2, -1, -1):
            self.__shift_down(i)


    def size(self):
        return len(self.__data)


    def is_empty(self):
        return self.size() == 0


    def p(self):
        print(self.__data)


    def __shift_up(self, i):
        while i > 0 and self.__data[i] > self.__data[(i - 1) // 2]:
            self.__data[i], self.__data[(i - 1) // 2] = self.__data[(i - 1) // 2], self.__data[i]
            i = (i - 1) // 2 


    def push(self, x):
        self.__data.append(x)
        i = len(self.__data) - 1
        self.__shift_up(i)
        
    
    def __shift_down(self, i):
        n = len(self.__data)
        val = self.__data[i]
        while i * 2 + 1 < n:
            j = i * 2 + 1   # j is left child of i
            if j + 1 < n and self.__data[j + 1] > self.__data[j]:
                # if right child exists and greater than left child
                j = j + 1
            if val > self.__data[j]:
                break
            self.__data[i] = self.__data[j]
            i = j
        self.__data[i] = val
        

    def pop(self):
        if self.is_empty():
            raise(ValueError("Trying to pop from an empty heap"))
        top = self.__data[0]
        val = self.__data.pop()
        if not self.is_empty():
            self.__data[0] = val
            self.__shift_down(0)
        return top
