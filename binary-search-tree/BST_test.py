from BST import BST
from random import randint
N = 30
x = randint(0, N - 1)
d = {}
for i in range(N):
    k = randint(0, N)
    d[k] = randint(0, N)
    if i == x:
        key = k
    print((k, d[k]))

bst = BST()
for i in d:
    bst.insert(i, d[i])

assert(bst.search(key) == d[key])
bst.level_order()
#bst.pre_order()
bst.in_order()
#bst.post_order()

bst.remove_min()

bst.level_order()
bst.in_order()