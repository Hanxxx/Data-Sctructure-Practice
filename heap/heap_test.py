from max_heap import MaxHeap
from index_heap import IndexMaxHeap
import heapq

mh = MaxHeap()
n = [5,6,77,111,31,21,9,1,7,4,45,5]

M = MaxHeap(1000, n)
for i in n:
    mh.push(i)
while not mh.is_empty():
    print(f'{mh.pop()}', end=' ')
print()
while not M.is_empty():
    print(f'{M.pop()}', end=' ')
print()

print('========Index Heap Test========')
imh = IndexMaxHeap()
for i, x in enumerate(n):
    imh.push(i, x)


imh.p()

result = []
while not imh.is_empty():
    result.append(imh.pop())
for l in (range(len(n)), n):
    for i in l:
        print(i, end='\t')
    print()
print("============Result=============")
for i in (0, 1):
    for j in result:
        print(j[i], end='\t')
    print()