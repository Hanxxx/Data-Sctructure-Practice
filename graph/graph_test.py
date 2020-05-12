from random import randint
from sparse_graph import SparseGraph
from dense_graph import DenseGraph
from component import Component
from path import Path
from shortest_path_unweighted import ShortestPathUnweighted as ShortestPathUnweighted
from cycle_detection import CycleDetection

N = 10
M = 10
print ("===================================")
g1 = SparseGraph(N, False)
for _ in range(M):
    g1.add_edge(randint(0, N - 1), randint(0, N - 1))

for i in range(N):
    print(f'Neighbor of i:', end=" ")
    for w in g1.get_neighbors(i):
        print(w, end=" ")
    print()

print ("===================================")
g2 = DenseGraph(N, False)
for _ in range(M):
    g2.add_edge(randint(0, N - 1), randint(0, N - 1))

for i in range(N):
    print(f'Neighbor of i:', end=" ")
    for w in g2.get_neighbors(i):
        print(w, end=" ")
    print()

with open('graph1.txt', 'r') as f1, open('graph2.txt', 'r') as f2:
    N = f1.readline().split()[0]
    g3 = SparseGraph(int(N), False)
    edges = f1.readlines()
    for edge in edges:
        edge = edge.split()
        g3.add_edge(int(edge[0]), int(edge[1]))

    N = f2.readline().split()[0]
    g4 = SparseGraph(int(N), True)
    edges = f2.readlines()
    for edge in edges:
        edge = edge.split()
        g4.add_edge(int(edge[0]), int(edge[1]))
    
# g3.print_grpah()
# c = Component(g3)
# print(c.component_count)

g4.print_grpah()

p = Path(g4, 0)
print ('Path:')
if p.has_path(4):
    p.print_path(4)
else:
    print('no path')

# cd = CycleDetection(g4)
# print(cd.has_cycle())

print('Shorted Path Unweighted:')
spu = ShortestPathUnweighted(g4, 0)
if spu.has_path(4):
    spu.print_path(4)
else:
    print('no path')

print(spu.get_distance(4))