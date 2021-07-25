class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0 for i in range(size)] for j in range((size))]
        self.size = size
    
    def add_edge(self, u, v):
        if u == v:
            print("Self loops are not allowed")
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
    
    def remove_edge(self, u, v):
        if self.adj_matrix[u][v] == 0:
            print("No edge exists between %d and %d" % (u, v))
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0
    
    def __len__(self):
        return self.size
    
    def print_matrix(self):
        for row in self.adj_matrix:
            for val in row:
                print("{:4}".format(val), end="")
            print()


if __name__ == '__main__':
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.print_matrix()
    graph.remove_edge(2, 3)
    print("\nAfter removing edge ({}, {})".format(2, 3))
    graph.print_matrix()
