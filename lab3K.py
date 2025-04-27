from collections import deque

# Check if state is valid
def is_valid(state):
    m_left, c_left, m_right, c_right = state
    # Missionaries can't be outnumbered by cannibals on either side
    return (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right) and m_left >= 0 and c_left >= 0 and m_right >= 0 and c_right >= 0

# BFS to solve Missionaries and Cannibals problem
def bfs():
    start = (3, 3, 0, 0)  # (Missionaries left, Cannibals left, Missionaries right, Cannibals right)
    goal = (0, 0, 3, 3)    # Goal state: All on the right
    visited = set()
    queue = deque([(start, [])])  # queue of (state, path to state)

    while queue:
        state, path = queue.popleft()
        if state == goal:
            print("Solution found!")
            for step in path:
                print(f"State: {step}")
            return
        
        for m, c in [(2, 0), (1, 0), (0, 2), (0, 1), (1, 1)]:  # Possible moves
            # Move m missionaries and c cannibals
            new_state = (state[0] - m, state[1] - c, state[2] + m, state[3] + c)
            if is_valid(new_state) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    print("No solution found.")

# Run the BFS
bfs()
