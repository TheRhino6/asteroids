import pygame
from constants import *

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.add(self.containers)

    def update_image(self):
        self.image = self.font.render(f"Score: {self.score}", True, "white")
        self.rect = self.image.get_rect(topleft=(10, 10))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.score += 10
        self.update_image()

    def asteroid_kill_score(self):
        self.score += 1000
        self.update_image()

    def asteroid_split_score(self):
        self.score += 10
        self.update_image()