from collections import deque

# Function to compute the greatest common divisor
def gcd(a, b):
    while b: a, b = b, a % b
    return a

# Check if solution is possible
def is_possible(x, y, z):
    return z <= max(x, y) and (z % gcd(x, y)) == 0

# BFS to find the solution
def water_jug(x, y, z):
    if not is_possible(x, y, z):
        print(f"No solution possible for {x}, {y}, {z}.")
        return
    
    visited = set()
    queue = deque([(0, 0)])  # Start state: (jug1, jug2)

    while queue:
        jug1, jug2 = queue.popleft()
        if jug1 == z or jug2 == z:  # If we reached the goal
            print(f"Solution found: Jug1={jug1}, Jug2={jug2}")
            return
        
        # Possible moves
        moves = [
            (x, jug2),  # Fill jug1
            (jug1, y),  # Fill jug2
            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2
            (jug1 - min(jug1, y - jug2), jug2 + min(jug1, y - jug2)),  # Pour jug1 -> jug2
            (jug1 + min(jug2, x - jug1), jug2 - min(jug2, x - jug1))   # Pour jug2 -> jug1
        ]
        
        for move in moves:
            if move not in visited:
                visited.add(move)
                queue.append(move)

    print("No solution found.")

# Example usage
x = 4  # Jug1 capacity
y = 3  # Jug2 capacity
z = 2  # Goal amount
water_jug(x, y, z)
