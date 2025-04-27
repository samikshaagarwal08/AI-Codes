import pygame, random, sys

pygame.init()

WIDTH, HEIGHT, SIZE = 600, 600, 75
ROWS, COLS = 8, 8
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Board setup
def create_board():
    board = [[None if (r + c) % 2 == 0 else ('b' if r < 3 else 'w') for c in range(COLS)] for r in range(ROWS)]
    return board

# Draw Board
def draw_board(board):
    for r in range(ROWS):
        for c in range(COLS):
            color = (255, 255, 255) if (r + c) % 2 == 0 else (150, 75, 0)
            pygame.draw.rect(screen, color, pygame.Rect(c * SIZE, r * SIZE, SIZE, SIZE))
            if board[r][c]:
                pygame.draw.circle(screen, (0, 0, 0) if board[r][c] == 'b' else (255, 255, 255),
                                   (c * SIZE + SIZE // 2, r * SIZE + SIZE // 2), SIZE // 2)

# Valid Move
def is_valid_move(board, start, end, player):
    dx, dy = abs(start[0] - end[0]), abs(start[1] - end[1])
    if dx == dy == 1 and not board[end[1]][end[0]]:
        return True
    if dx == dy == 2:
        mid = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
        if board[mid[1]][mid[0]] not in [None, player]:
            return True
    return False

# AI Move
def ai_move(board, player):
    valid_moves = []
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == player:
                for dr in [-2, 2]:
                    for dc in [-2, 2]:
                        end = (c + dc, r + dr)
                        if 0 <= end[0] < COLS and 0 <= end[1] < ROWS and is_valid_move(board, (c, r), end, player):
                            valid_moves.append(((c, r), end))
    return random.choice(valid_moves) if valid_moves else None

# Main Game Loop
def main():
    board = create_board()
    player_turn = 'w'
    while True:
        screen.fill((0, 0, 0))
        draw_board(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and player_turn == 'w':
                x, y = event.pos
                col, row = x // SIZE, y // SIZE
                if board[row][col] == 'w':
                    start = (col, row)
                    move = ai_move(board, 'b')
                    if move:
                        (start_col, start_row), (end_col, end_row) = move
                        board[end_row][end_col], board[start_row][start_col] = 'b', None

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()