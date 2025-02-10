import pygame
from constants import *

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self.containers)
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        text = self.font.render(f"Score: {(int(self.score))*10}", True, (255, 255, 255))
        screen.blit(text, SCORE_POSITION)

    def update(self, dt):
        self.score += (dt * SCORE_RATE)

    def hit(self):
        self.score += 1000