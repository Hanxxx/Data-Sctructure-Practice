from max_heap import MaxHeap
import heapq

mh = MaxHeap()
n = [4,5,6,77,1,3,4,7,5,7,4,45,5]
M = MaxHeap(n)
for i in n:
    mh.push(i)

while not M.is_empty():
    print(f'{M.pop()} ', end='')