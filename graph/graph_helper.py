
def create_graph_from_file(filename, grpah_class):
    with open(filename, 'w') as f:
        first = f.readline().split()
        