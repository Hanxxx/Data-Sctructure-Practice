class TreeNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST():
    
    def __init__(self):
        self.__root = None
        self.__count = 0

    
    @property
    def size(self):
        return self.__count


    def is_empty(self):
        return self.__count == 0


    def __insert_recur(self, node, key, value):
        if node == None:
            self.__count += 1
            return TreeNode(key, value)
        if key > node.key:
            node.right = self.__insert_recur(node.right, key, value)
        elif key < node.key:
            node.left = self.__insert_recur(node.left, key, value)
        else:
            node.value = value

        return node
    

    def insert(self, key, value):
        self.__root = self.__insert_recur(self.__root, key, value)


    def __contain__recur(self, node, key):
        if node == None:
            return False
        if key == node.key:
            return True
        elif key > node.key:
            return self.__contain__recur(node.right, key)
        else:
            return self.__contain__recur(node.left, key)


    def contain(self, key):
        return self.__contain__recur(self.root, key)


    def __search_recur(self, node, key):
        if node == None:
            return None
        if key == node.key:
            return node.value
        elif key > node.key:
            return self.__search_recur(node.right, key)
        else:
            return self.__search_recur(node.left, key)


    def search(self, key):
        return self.__search_recur(self.__root, key)


    def __pre_order_recur(self, node):
        if node == None:
            return
        print(node.key, end='\t')
        self.__pre_order_recur(node.left)
        self.__pre_order_recur(node.right)


    def __pre_order_non_recur(self):
        s = []
        if self.__root != None:
            s.append(self.__root)
        while s:
            cur = s.pop()
            print(cur.key, end='\t')
            if cur.right != None:
                s.append(cur.right)
            if cur.left != None:
                s.append(cur.left)


    def pre_order(self):
        print("Pre Order: Recursive Method")
        self.__pre_order_recur(self.__root)
        print()
        # print("Pre Order: Non Recursive Method")
        # self.__pre_order_non_recur()
        # print()

    
    def __in_order_recur(self, node):
        if node == None:
            return
        self.__in_order_recur(node.left)
        print(node.key, end='\t')
        self.__in_order_recur(node.right)


    def __in_order_non_recur(self):
        s = []
        v = {}
        if self.__root != None:
            s.append(self.__root)
        while s:
            cur = s.pop()
            if v.setdefault(cur.key, 1) == 2:
                print(cur.key, end='\t')
            if cur.right != None:
                s.append(cur.right)
            if v[cur.key] < 2:
                s.append(cur)
            if cur.left != None:
                s.append(cur.left)
            v[cur.key] += 1


    def in_order(self):
        print('In Order: recursive Method')
        self.__in_order_recur(self.__root)
        print()
        # print('In Order: non-recursive Method')
        # self.__in_order_non_recur()
        # print()


    def __post_order_recur(self, node):
        if node == None:
            return
        self.__post_order_recur(node.left)
        self.__post_order_recur(node.right)
        print(node.key, end='\t')


    def __post_order_non_recur(self):
        s = []
        v = {}
        if self.__root != None:
            s.append(self.__root)
        while s:
            cur = s.pop()
            if v.setdefault(cur.key, 1) == 3:
                print(cur.key, end='\t') 
            if v[cur.key] < 3:
                s.append(cur)
            if cur.right != None:
                s.append(cur.right)
            if cur.left != None:
                s.append(cur.left)
            v[cur.key] += 1


    def post_order(self):
        print('Post Order: recursive Method')
        self.__post_order_recur(self.__root)
        print()
        # print('Post Order: non-recursive Method')
        # self.__post_order_non_recur()
        # print()


    def level_order(self):
        print("Level Order")
        q = []
        if self.__root != None:
            q.append(self.__root)
        lvl = 1
        while q:
            tmp = []
            print(f'Level {lvl}:  ', end='')
            while q:
                cur = q.pop(0)
                print(cur.key, end='\t')
                if cur.left !=None:
                    tmp.append(cur.left)
                if cur.right != None:
                    tmp.append(cur.right)
            print()
            lvl += 1
            q = tmp
        print()
        

    def __remove_min_non_recur(self):
        if self.__root.left == None:
            self.__root = self.__root.right
        prev = self.__root
        cur = self.__root.left
        while cur.left != None:
            prev = prev.left
            cur = cur.left
        prev.left = cur.right


    def __remove_min_recur(self, node):
        if node.left == None:
            self.__count -= 1
            return node.right
        node.left = self.__remove_min_recur(node.left)
        return node


    def remove_min(self):
        assert(self.__root != None)
        self.__root = self.__remove_min_recur(self.__root)


    def remove_largest(self):
        pass
