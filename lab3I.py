import pygame, random, numpy as np

WIDTH, HEIGHT, FPS, JUMP_VEL, SIZE, MAX_EPISODES = 600, 150, 60, -15, 20, 1000
WHITE, BLACK, GREEN = (255,255,255), (0,0,0), (0,255,0)

class Dino:
    def __init__(self): self.x, self.y, self.vel, self.jumping = 50, HEIGHT-SIZE-10, 0, 0
    def move(self):
        if self.jumping: self.vel += 1; self.y += self.vel
        if self.y >= HEIGHT-SIZE-10: self.y, self.vel, self.jumping = HEIGHT-SIZE-10, 0, 0
    def jump(self): 
        if not self.jumping: self.jumping, self.vel = 1, JUMP_VEL
    def get_rect(self): return pygame.Rect(self.x, self.y, SIZE, SIZE)
    def draw(self, s): pygame.draw.rect(s, GREEN, self.get_rect())

class Cactus:
    def __init__(self): self.x, self.y, self.w = WIDTH, HEIGHT-SIZE-10, 20
    def move(self): self.x -= 5
    def get_rect(self): return pygame.Rect(self.x, self.y, self.w, SIZE)
    def is_offscreen(self): return self.x < -self.w
    def draw(self, s): pygame.draw.rect(s, BLACK, self.get_rect())

class QAgent:
    def __init__(self): self.q, self.a, self.alpha, self.gamma, self.eps = {}, [0,1], .1, .9, .1
    def state(self, d, c): return (int(d.y//5), int(d.vel), int((c.x-d.x)//10))
    def act(self, s):
        if np.random.rand()<self.eps: return random.choice(self.a)
        qv = [self.q.get((s,a),0) for a in self.a]; m = max(qv)
        return random.choice([a for a,q in zip(self.a,qv) if q==m])
    def update(self, s, a, r, ns, done):
        old = self.q.get((s,a),0)
        target = r if done else r+self.gamma*max([self.q.get((ns,na),0) for na in self.a])
        self.q[(s,a)] = old + self.alpha*(target-old)

def train():
    pygame.init(); screen = pygame.display.set_mode((WIDTH,HEIGHT)); clock = pygame.time.Clock()
    agent = QAgent()
    for ep in range(MAX_EPISODES):
        d, c, done, score = Dino(), Cactus(), 0, 0
        while not done:
            for e in pygame.event.get():
                if e.type==pygame.QUIT: pygame.quit(); return
            s = agent.state(d,c)
            if agent.act(s): d.jump()
            d.move(); c.move()
            if c.is_offscreen(): c = Cactus()
            r = 1
            if d.get_rect().colliderect(c.get_rect()): r, done = -100, 1
            ns = agent.state(d,c)
            agent.update(s, agent.act(s), r, ns, done)
            screen.fill(WHITE); d.draw(screen); c.draw(screen)
            pygame.display.update(); clock.tick(FPS); score += 1
        print(f"Episode {ep+1}: Score {score}")

if __name__=="__main__": train()
