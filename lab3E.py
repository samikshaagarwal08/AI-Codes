import chess, chess.engine, random

def evaluate(board):
    if board.is_checkmate():
        return -9999 if board.turn else 9999
    if board.is_stalemate() or board.is_insufficient_material():
        return 0
    values = {chess.PAWN:1, chess.KNIGHT:3, chess.BISHOP:3, chess.ROOK:5, chess.QUEEN:9}
    score = 0
    for piece in values:
        score += len(board.pieces(piece, chess.WHITE)) * values[piece]
        score -= len(board.pieces(piece, chess.BLACK)) * values[piece]
    return score

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate(board), None

    best_move = None
    if maximizing:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth-1, alpha, beta, False)
            board.pop()
            if eval > max_eval:
                max_eval, best_move = eval, move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth-1, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval, best_move = eval, move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def play():
    board = chess.Board()
    while not board.is_game_over():
        print(board, "\n")
        if board.turn:
            move = None
            while move not in board.legal_moves:
                try:
                    user_input = input("Your move: ")
                    move = chess.Move.from_uci(user_input)
                except:
                    print("Invalid move format.")
        else:
            _, move = minimax(board, 3, -float('inf'), float('inf'), False)
            print(f"AI plays: {move}")
        board.push(move)
    print(board)
    print("Game Over:", board.result())

if __name__ == "__main__":
    play()
