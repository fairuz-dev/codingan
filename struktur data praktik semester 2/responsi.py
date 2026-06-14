graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["E", "C"]
}

def bfs(graph, start, stop):
    jalur = set()
    queue = [[start]]
    while queue:
        jalur = queue.pop(0)
        node = jalur[-1]
        if node not in graph:
            continue
        for adjacent in graph[node]:
            new_jalur = list(jalur)
            new_jalur.append(adjacent)
            print('jalur:', new_jalur)
            queue.append(new_jalur)
            if adjacent == stop:
                return new_jalur

def dfs(graph, start, stop,):
    jalur = set()
    stack = [[start]]
    while stack:
        jalur = stack.pop()
        node = jalur[-1]
        if node not in graph:
            continue
        for adjacent in graph[node]:
            new_jalur = list(jalur)
            new_jalur.append(adjacent)
            stack.append(new_jalur)
            print('jalur:', new_jalur)
            if adjacent == stop:
                return new_jalur
print(bfs(graph, "A", "F"))
print(dfs(graph, "A", "F"))