import pygame
import random
from circleshape import *
from constants import *

class Asteroids(CircleShape):
    score = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOUR, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.score.hit()
            return
        else:
            rand_angle = random.uniform(20, 50)
            new1 = Asteroids(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new1.velocity = self.velocity.rotate(-rand_angle) *1.2
            new2 = Asteroids(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new2.velocity = self.velocity.rotate(rand_angle) *1.2
