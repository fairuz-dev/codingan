class Graph:
    def __init__(self):
        self.graph = {}

    # menambah vertex
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # menambah edge
    def add_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    # menampilkan graph
    def print_graph(self):
        for vertex in self.graph:
            print(vertex, ":", self.graph[vertex])

# ==============================
# PROGRAM UTAMA
# ==============================

my_graph = Graph()

# menambahkan vertex
my_graph.add_vertex(52)
my_graph.add_vertex(18)
my_graph.add_vertex(21)
my_graph.add_vertex(44)
my_graph.add_vertex(76)
my_graph.add_vertex(27)
my_graph.add_vertex(82)

# menambahkan edge sesuai gambar
my_graph.add_edge(52, 18)
my_graph.add_edge(52, 27)

my_graph.add_edge(18, 21)
my_graph.add_edge(18, 44)

my_graph.add_edge(44, 21)
my_graph.add_edge(44, 76)

my_graph.add_edge(21, 76)

my_graph.add_edge(27, 82)

# menampilkan graph
print("Graph: ")
my_graph.print_graph()