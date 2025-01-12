def dfs(graph, start):
    visited = set()
    res = []
    def dfs_recursive(vertex):
        if vertex not in visited:
            visited.add(vertex)
            res.append(vertex)
            for neighbor in graph[vertex]:
                dfs_recursive(neighbor)
    dfs_recursive(start)
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
result = dfs(graph, start_vertex)
print("Обход в глубину:", result)
# Ожидаемый результат: ['A', 'B', 'D', 'E', 'H', 'C', 'F', 'G', 'I']