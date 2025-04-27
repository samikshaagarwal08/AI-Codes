import pygame, sys
pygame.init()

WIDTH, HEIGHT, SIZE = 600, 600, 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
YELLOW, RED = (255, 255, 0), (255, 0, 0)

# Pac-Man class
class PacMan:
    def __init__(self, x, y):
        self.x, self.y, self.speed = x, y, 5

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), SIZE//2)

# Ghost class
class Ghost:
    def __init__(self, x, y):
        self.x, self.y, self.speed = x, y, 3

    def move_toward(self, target_x, target_y):
        dx, dy = target_x - self.x, target_y - self.y
        dist = max(1, (dx**2 + dy**2)**0.5)
        self.x += self.speed * dx / dist
        self.y += self.speed * dy / dist

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), SIZE//2)

# Maze layout
maze = [
    [1,1,1,1,1,1,1,1,1], [1,0,0,0,0,0,0,0,1], [1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,1], [1,0,1,0,1,1,1,0,1], [1,0,1,0,0,0,1,0,1],
    [1,0,0,0,1,0,0,0,1], [1,1,1,1,1,1,1,1,1]
]

# Draw maze
def draw_maze():
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 255), (x * SIZE, y * SIZE, SIZE, SIZE))

# Main loop
def main():
    pacman, ghost = PacMan(SIZE, SIZE), Ghost(SIZE*6, SIZE*6)
    while True:
        screen.fill((0, 0, 0))
        draw_maze()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()

        keys = pygame.key.get_pressed()
        pacman.move(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], keys[pygame.K_DOWN] - keys[pygame.K_UP])

        ghost.move_toward(pacman.x, pacman.y)
        pacman.draw()
        ghost.draw()

        if (pacman.x - ghost.x) ** 2 + (pacman.y - ghost.y) ** 2 < (SIZE//2 + SIZE//2) ** 2:
            print("Game Over! Ghost caught Pac-Man!")
            pygame.quit(); sys.exit()

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
