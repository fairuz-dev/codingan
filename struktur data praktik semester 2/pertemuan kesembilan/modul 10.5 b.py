class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    # method printAllConnected
    def printAllConnected(self, vertex):
        if vertex in self.graph:
            print("Vertex yang terhubung dengan", vertex, ":")
            for i in self.graph[vertex]:
                print(i)
        else:
            print("Vertex tidak ditemukan")

# =======================================
# PROGRAM UTAMA
# =======================================

my_graph = Graph()

my_graph.add_vertex(52)
my_graph.add_vertex(18)
my_graph.add_vertex(44)
my_graph.add_vertex(21)
my_graph.add_vertex(76)

my_graph.add_edge(18, 44)
my_graph.add_edge(44, 21)
my_graph.add_edge(44, 76)

my_graph.printAllConnected(44)