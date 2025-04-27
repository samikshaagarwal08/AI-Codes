def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens_util(board, row, n, solutions):
    # If all queens are placed
    if row == n:
        solutions.append(board[:])  # Add the solution as a copy of the board
        return
    
    # Try placing a queen in all columns of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place the queen
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row] = -1  # Backtrack

def solve_nqueens(n):
    board = [-1] * n  # Board to store the column positions of queens
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    
    # Print the solutions
    print(f"Total solutions for {n}-Queens: {len(solutions)}")
    for solution in solutions:
        for row in solution:
            print(' '.join(['Q' if i == row else '.' for i in range(n)]))
        print()

# Example usage
n = 4  # You can change this value for different sizes
solve_nqueens(n)
