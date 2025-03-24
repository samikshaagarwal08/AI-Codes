def ao_star(graph, start, goal, heuristic):
    open_list = {start}
    closed_list = set()
    parents = {}
    g = {node: float('inf') for node in graph}
    g[start] = 0

    while open_list:
        current = min(open_list, key=lambda node: g[node] + heuristic[node])

        if current == goal:
            path = []
            while current in parents:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()
            return path  # Return the found path
        
        open_list.remove(current)
        closed_list.add(current)

        for neighbour, cost in graph[current].items():
            if neighbour in closed_list:
                continue

            tentative_g = g[current] + cost

            if neighbour not in open_list:
                open_list.add(neighbour)
            elif tentative_g >= g[neighbour]:
                continue

            parents[neighbour] = current
            g[neighbour] = tentative_g

    return None 

# Sample graph with heuristic values
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1},
}
heuristic = {'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 3, 'F': 0}
print("\nAO* Search (A -> F):", ao_star(graph, 'A', 'F', heuristic))
