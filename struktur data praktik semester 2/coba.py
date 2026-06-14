graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["E"]
}

queue = [["A"]]
while queue:
    path = (queue.pop(0))
    node = path[-1]
    if node not in graph:
        continue
    for adjacent in graph[node]:
        new_path = list(path)
        new_path.append(adjacent)
        queue.append(new_path)
        if adjacent == "F":
            print("Path found:", new_path)
            break
    break
