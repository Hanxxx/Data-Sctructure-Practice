class IndexMaxHeap(object):
    """
    IndexMaxHeap binary tree implement using array as storage
    data: self.__data
    index: self.__index
    reversed_index: self.__r_index
    =========================================================
    index of node i in array:   i
    parent of i:                i // 2
    left child:                 i * 2
    right child:                i * 2 + 1
    """
    def __init__(self, capacity = 100):
            self.__capacity = capacity
            self.__size = 0
            self.__data = [-1] * (capacity + 1)
            self.__index = [-1] * (capacity + 1)
            self.__r_index = [-1] * (capacity + 1)

    @property
    def capacity(self):
        return self.__capacity


    @property
    def size(self):
        return self.__size


    def is_empty(self):
        return self.__size == 0


    def p(self):
        """
        print function for test only
        """
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for l in (range(self.__size + 5), self.__index[:self.__size + 5], self.__data[:self.__size + 5], self.__r_index[:self.__size + 5]):
            for i in l:
                print(i, end='\t')
            print()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    def __shift_up(self, i):
        """
        from node i, comparing it with its parent until reaching the proper position.
        """
        idx = self.__index[i]
        val = self.__data[idx]
        while i > 1 and val > self.__data[self.__index[i // 2]]:
            self.__index[i] = self.__index[i // 2]
            self.__r_index[self.__index[i]] = i
            i = i // 2 
        self.__index[i] = idx
        self.__r_index[idx] = i


    def push(self, idx, x):
        """
        insert the new elment in the back of array, and shift it up
        assume the index to push is unique.
        """
        assert(self.__size < self.__capacity)
        assert(0 <= idx < self.capacity)
        self.__size += 1
        idx += 1
        self.__data[idx] = x
        self.__index[self.__size] = idx
        self.__r_index[idx] = self.__size
        self.__shift_up(self.__size)
        
    
    def __shift_down(self, i):
        """
        start from i, comparing it with its largest child
        until   1) i is leaf node (has no child)
                2) i is greater than its children
        put the value on the proper position
        """
        n = self.__size
        idx = self.__index[i]
        val = self.__data[idx]
        while i * 2 <= n:
            j = i * 2
            if j + 1 <= n and self.__data[self.__index[j + 1]] > self.__data[self.__index[j]]:
                # if right child exists and larger
                j = j + 1
            if val > self.__data[self.__index[j]]:
                break
            self.__index[i] = self.__index[j]
            self.__index[self.__index[i]] = i
            i = j
        self.__index[i] = idx
        self.__r_index[idx] = i
        

    def pop(self):
        """
        swap the last node to the top, and shift it down
        pop (decrease size) and return the former top of the heap (from the last)
        """
        assert(not self.is_empty())
        top_idx = self.__index[1]
        top = self.__data[top_idx]
        self.__index[1] = self.__index[self.__size]
        self.__r_index[self.__index[1]] = 1
        self.__size -= 1
        self.__shift_down(1)
        return top_idx - 1, top


    def top(self):
        return self.__data[self.__index[1]]

    
    def modify(self, idx, x):
        assert(0 <= idx < self.capacity)
        idx += 1
        self.__data[idx] = x
        self.__shift_up(self.__r_index[idx])
        self.__shift_down(self.__r_index[idx])



class IndexMinHeap(object):
    """
    IndexMinHeap binary tree implement using array as storage
    data: self.__data
    index: self.__index
    reversed_index: self.__r_index
    =========================================================
    index of node i in array:   i
    parent of i:                i // 2
    left child:                 i * 2
    right child:                i * 2 + 1
    """
    def __init__(self, capacity = 100):
            self.__capacity = capacity
            self.__size = 0
            self.__data = [-1] * (capacity + 1)
            self.__index = [-1] * (capacity + 1)
            self.__r_index = [-1] * (capacity + 1)

    @property
    def capacity(self):
        return self.__capacity


    @property
    def size(self):
        return self.__size


    def is_empty(self):
        return self.__size == 0


    def p(self):
        """
        print function for test only
        """
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for l in (range(self.__size + 5), self.__index[:self.__size + 5], self.__data[:self.__size + 5], self.__r_index[:self.__size + 5]):
            for i in l:
                print(i, end='\t')
            print()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    def __shift_up(self, i):
        """
        from node i, comparing it with its parent until reaching the proper position.
        """
        idx = self.__index[i]
        val = self.__data[idx]
        while i > 1 and val < self.__data[self.__index[i // 2]]:
            self.__index[i] = self.__index[i // 2]
            self.__r_index[self.__index[i]] = i
            i = i // 2 
        self.__index[i] = idx
        self.__r_index[idx] = i


    def push(self, idx, x):
        """
        insert the new elment in the back of array, and shift it up
        assume the index to push is unique.
        """
        assert(self.__size < self.__capacity)
        assert(0 <= idx < self.capacity)
        self.__size += 1
        idx += 1
        self.__data[idx] = x
        self.__index[self.__size] = idx
        self.__r_index[idx] = self.__size
        self.__shift_up(self.__size)
        
    
    def __shift_down(self, i):
        """
        start from i, comparing it with its largest child
        until   1) i is leaf node (has no child)
                2) i is greater than its children
        put the value on the proper position
        """
        n = self.__size
        idx = self.__index[i]
        val = self.__data[idx]
        while i * 2 <= n:
            j = i * 2
            if j + 1 <= n and self.__data[self.__index[j + 1]] < self.__data[self.__index[j]]:
                # if right child exists and smaller
                j = j + 1
            if val < self.__data[self.__index[j]]:
                break
            self.__index[i] = self.__index[j]
            self.__r_index[self.__index[i]] = i
            i = j
        self.__index[i] = idx
        self.__r_index[idx] = i
        

    def pop(self):
        """
        swap the last node to the top, and shift it down
        pop (decrease size) and return the former top of the heap
        """
        assert(not self.is_empty())
        top_idx = self.__index[1]
        top = self.__data[top_idx]
        self.__r_index[top] = -1
        self.__index[1] = self.__index[self.__size]
        self.__r_index[self.__index[1]] = 1
        self.__size -= 1
        self.__shift_down(1)
        return top_idx - 1, top


    def top(self):
        return self.__data[self.__index[1]]

    
    def modify(self, idx, x):
        assert(self.contains(idx))
        idx += 1
        self.__data[idx] = x
        self.__shift_up(self.__r_index[idx])
        self.__shift_down(self.__r_index[idx])


    def get_value(self, idx):
        assert(self.contains(idx))
        return self.__data[idx + 1]

    
    def contains(self, idx):
        assert(0 <= idx < self.capacity)
        return self.__r_index[idx + 1] != -1