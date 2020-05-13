from dense_graph_weighted import DenseGrpahWeighted
from sparse_graph_weighted import SparseGraphWeighted
from minspan_tree_prim import MinspanTreePrim
from minspan_tree_krusk import MinspanTreeKrusk

# with open('weighted_graph1.txt', 'r') as f1:
#     N = f1.readline().split()[0]
#     g1 = SparseGraphWeighted(int(N), False)
#     g2 = DenseGrpahWeighted(int(N), False)
#     edges = f1.readlines()
#     for edge in edges:
#         edge = edge.split()
#         g1.add_edge(int(edge[0]), int(edge[1]), float(edge[2]))
#         g2.add_edge(int(edge[0]), int(edge[1]), float(edge[2]))

# g1.print_graph()
# g2.print_graph()


def create_sparse_graph_from_file(filename, directed = False):
    try:
        with open(filename, 'r') as f:
            N = f.readline().split()[0]
            g = SparseGraphWeighted(int(N), directed)
            edges = f.readlines()
            for edge in edges:
                edge = edge.split()
                g.add_edge(int(edge[0]), int(edge[1]), float(edge[2]))
    except:
        raise ValueError("Check file name")
    else:
        return g


if __name__ == "__main__":
    g1 = create_sparse_graph_from_file("weighted_graph1.txt")
    g2 = create_sparse_graph_from_file("weighted_graph2.txt")
    
    mst_lazy_prim = MinspanTreePrim(g2, mode=0)
    mst_lazy_prim.print_result()

    mst_prim = MinspanTreePrim(g2, mode=1)
    mst_prim.print_result()

    mst_krusk = MinspanTreeKrusk(g2)
    mst_krusk.print_result()