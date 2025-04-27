import pygame, random, numpy as np

# Constants
WIDTH, HEIGHT, SIZE, FPS = 400, 600, 30, 60
BIRD_WIDTH, BIRD_HEIGHT, PIPE_WIDTH, GAP = 30, 30, 50, 150
MAX_EPISODES = 1000

# Colors
YELLOW, RED, WHITE = (255, 255, 0), (255, 0, 0), (255, 255, 255)

# Bird & Pipe classes
class Bird:
    def __init__(self):
        self.x, self.y, self.vel = 50, HEIGHT // 2, 0

    def move(self): self.vel += 1; self.y += self.vel
    def flap(self): self.vel = -10
    def get_rect(self): return pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

class Pipe:
    def __init__(self): self.x, self.height = WIDTH, random.randint(100, 400)
    def move(self): self.x -= 5
    def get_rects(self): return pygame.Rect(self.x, 0, PIPE_WIDTH, self.height), pygame.Rect(self.x, self.height + GAP, PIPE_WIDTH, HEIGHT - self.height - GAP)

# Q-learning Agent
class QLearningAgent:
    def __init__(self, actions): self.alpha, self.gamma, self.epsilon, self.actions, self.q_table = 0.1, 0.9, 0.1, actions, {}
    def get_state(self, bird, pipes): return (bird.y, bird.vel, pipes[0].x, pipes[0].height)
    def get_action(self, state): return random.choice(self.actions) if np.random.rand() < self.epsilon else max(self.actions, key=lambda a: self.q_table.get((state, a), 0))
    def update_q_value(self, state, action, reward, next_state, done): self.q_table[(state, action)] = self.q_table.get((state, action), 0) + self.alpha * (reward + self.gamma * max([self.q_table.get((next_state, a), 0) for a in self.actions]) - self.q_table.get((state, action), 0))

# Train the agent
def train():
    pygame.init(); clock = pygame.time.Clock()
    agent, bird, pipes, score = QLearningAgent([0, 1]), Bird(), [Pipe()], 0
    for episode in range(MAX_EPISODES):
        bird, pipes, done, game_score = Bird(), [Pipe()], False, 0
        while not done:
            state = agent.get_state(bird, pipes)
            action = agent.get_action(state)
            if action == 1: bird.flap()
            bird.move(); [pipe.move() for pipe in pipes]
            if pipes[-1].x < WIDTH - 200: pipes.append(Pipe())
            if pipes[0].x < -PIPE_WIDTH: pipes.pop(0)
            if any([bird.get_rect().colliderect(rect) for pipe in pipes for rect in pipe.get_rects()]) or bird.y > HEIGHT or bird.y < 0: done = True
            reward = 10 if pipes[0].x < bird.x and pipes[0].x >= bird.x - 5 else -1
            agent.update_q_value(state, action, reward, agent.get_state(bird, pipes), done)
            game_score += 1
            clock.tick(FPS)
        print(f"Episode {episode+1}: Score {game_score}")

if __name__ == "__main__": train()
