def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start,end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    'A': {'B':1, 'C':4},
    'B': {'A':1, 'D':2, 'E':5},
    'C': {'A':4, 'F':3},
    'D': {'B':2},
    'E': {'B':5, 'F':1},
    'F': {'C':3, 'E':1},
}

print("DFS Traversal:")
dfs(graph, 'A')
