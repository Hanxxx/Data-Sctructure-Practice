from dense_graph_weighted import DenseGrpahWeighted
from sparse_graph_weighted import SparseGraphWeighted

with open('weighted_graph1.txt', 'r') as f1:
    N = f1.readline().split()[0]
    g1 = SparseGraphWeighted(int(N), False)
    g2 = DenseGrpahWeighted(int(N), False)
    edges = f1.readlines()
    for edge in edges:
        edge = edge.split()
        g1.add_edge(int(edge[0]), int(edge[1]), float(edge[2]))
        g2.add_edge(int(edge[0]), int(edge[1]), float(edge[2]))

g1.print_graph()
g2.print_graph()