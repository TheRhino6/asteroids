import pygame
from constants import *
from circleshape import *

class Shield(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.timer = 0
        self.add(self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius *1.5, 2)

    def update(self, dt, player_position):
        self.position = player_position
        self.timer += dt
        if self.timer >= 0.5:
            self.kill()