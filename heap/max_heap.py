class MaxHeap(object):
    """
    MaxHeap binary tree implement using array as storage
    Elements start from self.__data[1] for simple computation
    index of node i in array:   i
    parent of i:                i // 2
    left child:                 i * 2
    right child:                i * 2 + 1
    """
    def __init__(self, capacity = 100, nums = []):
            assert(len(nums) <= capacity)
            self.__capacity = capacity
            self.__size = len(nums)
            self.__data = [-1] + nums + [0] * (capacity - len(nums))
            self.__heapify()


    def __heapify(self):
        """
        Initialization of self.__data
        shift down from the last non-leaf node
        """
        n = self.__size
        if n <= 1:
            return
        for i in range(n // 2, 0, -1):
            self.__shift_down(i)


    @property
    def capacity(self):
        return self.__capacity


    @property
    def size(self):
        return self.__size


    def is_empty(self):
        return self.__size == 0


    def p(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for l in (range(self.__size + 5), self.__data[:self.__size + 5]):
            for i in l:
                print(i, end='\t')
            print()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    def __shift_up(self, i):
        """
        from node i, comparing it with its parent until reaching the proper position.
        """
        val = self.__data[i]
        while i > 1 and val > self.__data[i // 2]:
            self.__data[i] = self.__data[i // 2]
            i = i // 2 
        self.__data[i] = val


    def push(self, x):
        """
        insert the new elment in the back of array, and shift it up
        """
        assert(self.__size < self.__capacity)
        self.__size += 1
        self.__data[self.__size] = x
        self.__shift_up(self.__size)
        
    
    def __shift_down(self, i):
        """
        start from i, comparing it with its largest child
        until   1) i is leaf node (has no child)
                2) i is greater than its children
        put the value on the proper position
        """
        n = self.__size
        val = self.__data[i]
        while i * 2 <= n:
            j = i * 2
            if j + 1 <= n and self.__data[j + 1] > self.__data[j]:
                # if right child exists and larger
                j = j + 1
            if val > self.__data[j]:
                break
            self.__data[i] = self.__data[j]
            i = j
        self.__data[i] = val
        

    def pop(self):
        """
        swap the last node to the top, and shift it down
        pop (decrease size) and return the former top of the heap (from the last)
        """
        assert(not self.is_empty())
        top = self.__data[1]
        val = self.__data[self.__size]
        self.__data[1] = val
        self.__size -= 1
        self.__shift_down(1)

        return top


    def top(self):
        return self.__data[1]