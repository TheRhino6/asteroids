import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, SHOT_COLOUR, self.position, self.radius, 0)

    def update(self, dt):
        self.position += self.velocity * dt