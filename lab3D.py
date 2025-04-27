import pygame, random, sys
pygame.init()

W, H, S = 400, 400, 20
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

snake = [(100, 100)]
food = (random.randrange(0, W, S), random.randrange(0, H, S))

def move(snake, dir):
    head = (snake[0][0] + dir[0], snake[0][1] + dir[1])
    return [head] + snake[:-1]

def ai(snake, food):
    hx, hy = snake[0]
    fx, fy = food
    if abs(fx - hx) > abs(fy - hy):
        return (S if fx > hx else -S, 0)
    else:
        return (0, S if fy > hy else -S)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()

    dir = ai(snake, food)
    new_head = (snake[0][0] + dir[0], snake[0][1] + dir[1])

    if new_head in snake or not (0 <= new_head[0] < W and 0 <= new_head[1] < H):
        pygame.quit(); sys.exit()

    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randrange(0, W, S), random.randrange(0, H, S))
    else:
        snake.pop()

    screen.fill((0, 0, 0))
    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*s, S, S))
    pygame.draw.rect(screen, (255, 0, 0), (*food, S, S))
    pygame.display.flip()
    clock.tick(10)
