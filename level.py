import pygame
from constants import *

class Level(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.level = 1
        self.font = pygame.font.Font(None, 36)
        self.add(self.containers)

    def update_image(self):
        self.image = self.font.render(f"Level: {self.level}", True, "white")
        self.rect = self.image.get_rect(topleft=(200, 10))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dt, score):
        self.level = int(score / LEVEL_RATIO) + 1
        self.update_image()