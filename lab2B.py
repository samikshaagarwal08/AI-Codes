import heapq
def uniform_cost_search(graph, start, goal):
    heap = [(0, start)]  # (cost, node)
    visited = set()
    while heap:
        cost, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return cost
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor))
    return float("inf")

graph = {
    'A': {'B': 1,'C': 4},
    'B': {'A': 1,'D': 2,'E': 5},
    'C': {'A': 4,'F': 3},
    'D': {'B': 2},
    'E': {'B': 5,'F': 1},
    'F': {'C': 3,'E': 1}
}

print("Uniform Cost Search Path Cost:", uniform_cost_search(graph, 'A', 'F'))
