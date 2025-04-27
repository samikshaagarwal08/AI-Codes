def is_safe(x, y, board, n):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def knight_tour(n):
    board = [[-1] * n for _ in range(n)]
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    
    def solve(x, y, move_count):
        if move_count == n * n: return True
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_safe(nx, ny, board, n):
                board[nx][ny] = move_count
                if solve(nx, ny, move_count + 1): return True
                board[nx][ny] = -1
        return False

    board[0][0] = 0  # Start from top-left corner
    if solve(0, 0, 1):
        for row in board: print(row)
    else:
        print("No solution")

# Example usage
knight_tour(8)
