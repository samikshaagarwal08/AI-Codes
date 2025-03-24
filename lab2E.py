from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node].keys():  # Loop inside the while loop
            if neighbour not in visited:
                visited.add(neighbour)  # Fix here
                queue.append(neighbour)

# Graph with weighted edges
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1},
}

print("BFS Traversal:")
bfs(graph, 'A')
