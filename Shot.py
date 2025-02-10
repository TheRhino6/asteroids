import pygame

from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x, y, radius)
        self.velocity = velocity
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, SHOT_COLOUR, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt