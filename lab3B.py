import random, math

ROWS, COLS = 6, 7
PLAYER, AI = 1, 2

def create_board():
    return [[0]*COLS for _ in range(ROWS)]

def drop(board, row, col, piece):
    board[row][col] = piece

def valid(board, col):
    return board[0][col] == 0

def get_row(board, col):
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == 0: return r

def win(board, piece):
    for r in range(ROWS):
        for c in range(COLS-3):
            if all(board[r][c+i]==piece for i in range(4)): return True
    for r in range(ROWS-3):
        for c in range(COLS):
            if all(board[r+i][c]==piece for i in range(4)): return True
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(board[r+i][c+i]==piece for i in range(4)): return True
    for r in range(3, ROWS):
        for c in range(COLS-3):
            if all(board[r-i][c+i]==piece for i in range(4)): return True
    return False

def score(board, piece):
    opp = PLAYER if piece == AI else AI
    center = [board[r][COLS//2] for r in range(ROWS)].count(piece) * 3
    return center

def valid_moves(board):
    return [c for c in range(COLS) if valid(board, c)]

def minimax(board, depth, alpha, beta, maximizing):
    valid_cols = valid_moves(board)
    if depth == 0 or win(board, PLAYER) or win(board, AI) or not valid_cols:
        if win(board, AI): return (None, 1000)
        if win(board, PLAYER): return (None, -1000)
        return (None, score(board, AI))
    
    best_col = random.choice(valid_cols)
    if maximizing:
        value = -math.inf
        for col in valid_cols:
            temp = [row[:] for row in board]
            drop(temp, get_row(temp, col), col, AI)
            new_score = minimax(temp, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value, best_col = new_score, col
            alpha = max(alpha, value)
            if alpha >= beta: break
    else:
        value = math.inf
        for col in valid_cols:
            temp = [row[:] for row in board]
            drop(temp, get_row(temp, col), col, PLAYER)
            new_score = minimax(temp, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value, best_col = new_score, col
            beta = min(beta, value)
            if alpha >= beta: break
    return best_col, value

def print_board(board):
    for row in board: print(' '.join(str(x) for x in row))
    print()

def play():
    board = create_board()
    turn = random.choice([PLAYER, AI])
    while True:
        print_board(board)
        if turn == PLAYER:
            col = int(input("Your move (0-6): "))
            if valid(board, col):
                drop(board, get_row(board, col), col, PLAYER)
                if win(board, PLAYER):
                    print_board(board)
                    print("You win!")
                    break
        else:
            col, _ = minimax(board, 4, -math.inf, math.inf, True)
            if valid(board, col):
                drop(board, get_row(board, col), col, AI)
                if win(board, AI):
                    print_board(board)
                    print("AI wins!")
                    break
        if not valid_moves(board):
            print_board(board)
            print("Draw!")
            break
        turn = PLAYER if turn == AI else AI

if __name__ == "__main__":
    play()






# import random, math

# ROWS, COLS = 6, 7
# PLAYER, AI = 1, 2

# def create_board(): return [[0]*COLS for _ in range(ROWS)]
# def drop(board, r, c, piece): board[r][c] = piece
# def valid(board, c): return board[0][c] == 0
# def get_row(board, c): return next(r for r in range(ROWS-1, -1, -1) if board[r][c] == 0)
# def win(board, piece):
#     for r in range(ROWS):
#         for c in range(COLS-3):
#             if all(board[r][c+i] == piece for i in range(4)): return True
#     for r in range(ROWS-3):
#         for c in range(COLS):
#             if all(board[r+i][c] == piece for i in range(4)): return True
#     for r in range(ROWS-3):
#         for c in range(COLS-3):
#             if all(board[r+i][c+i] == piece for i in range(4)): return True
#     for r in range(3, ROWS):
#         for c in range(COLS-3):
#             if all(board[r-i][c+i] == piece for i in range(4)): return True
#     return False

# def score(board, piece):
#     return sum([board[r][COLS//2] == piece for r in range(ROWS)]) * 3

# def minimax(board, depth, alpha, beta, maximizing):
#     valid_cols = [c for c in range(COLS) if valid(board, c)]
#     if depth == 0 or win(board, PLAYER) or win(board, AI) or not valid_cols:
#         if win(board, AI): return (None, 1000)
#         if win(board, PLAYER): return (None, -1000)
#         return (None, score(board, AI))
#     best_col = random.choice(valid_cols)
#     if maximizing:
#         value = -math.inf
#         for col in valid_cols:
#             temp = [row[:] for row in board]
#             drop(temp, get_row(temp, col), col, AI)
#             new_score = minimax(temp, depth-1, alpha, beta, False)[1]
#             if new_score > value: value, best_col = new_score, col
#             alpha = max(alpha, value)
#             if alpha >= beta: break
#     else:
#         value = math.inf
#         for col in valid_cols:
#             temp = [row[:] for row in board]
#             drop(temp, get_row(temp, col), col, PLAYER)
#             new_score = minimax(temp, depth-1, alpha, beta, True)[1]
#             if new_score < value: value, best_col = new_score, col
#             beta = min(beta, value)
#             if alpha >= beta: break
#     return best_col, value

# def print_board(board):
#     for row in board: print(' '.join(map(str, row)))
#     print()

# def play():
#     board = create_board()
#     turn = random.choice([PLAYER, AI])
#     while True:
#         print_board(board)
#         if turn == PLAYER:
#             col = int(input("Your move (0-6): "))
#             if valid(board, col):
#                 drop(board, get_row(board, col), col, PLAYER)
#                 if win(board, PLAYER): print_board(board); print("You win!"); break
#         else:
#             col, _ = minimax(board, 4, -math.inf, math.inf, True)
#             if valid(board, col):
#                 drop(board, get_row(board, col), col, AI)
#                 if win(board, AI): print_board(board); print("AI wins!"); break
#         if not any(valid(board, c) for c in range(COLS)): print_board(board); print("Draw!"); break
#         turn = PLAYER if turn == AI else AI

# if __name__ == "__main__": play()
