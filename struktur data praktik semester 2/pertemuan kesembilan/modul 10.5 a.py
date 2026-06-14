class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # method isInGraph
    def isInGraph(self, vertex):
        if vertex in self.graph:
            return True
        else:
            return False

# =======================================
# PROGRAM UTAMA
# =======================================

my_graph = Graph()

my_graph.add_vertex(52)
my_graph.add_vertex(18)
my_graph.add_vertex(21)

print(my_graph.isInGraph(18))
print(my_graph.isInGraph(100))