import pygame
from constants import *

class Lives(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 3
        self.font = pygame.font.Font(None, 36)
        self.add(self.containers)

    def update_image(self):
        self.image = self.font.render(f"Lives: {self.lives}", True, "white")
        self.rect = self.image.get_rect(topleft=(350, 10))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.update_image()

    def lose_life(self):
        self.lives = self.lives - 1