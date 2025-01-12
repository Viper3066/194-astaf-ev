def bfs(graph, start):
    visited = set()
    queue = [start]
    res = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            res.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    return res


# Тестовый граф в виде словаря смежности
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C', 'I'],
    'H': ['E'],
    'I': ['G']
}

# Тестовый пример
start_vertex = 'A'
result = bfs(graph, start_vertex)
print("Обход в ширину:", result)
# Ожидаемый результат: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']