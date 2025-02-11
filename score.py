import pygame
from constants import *

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self.containers)
        self.score = 0
        self.level = 1
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        # Draw Score
        score_text = self.font.render(f"Score: {(int(self.score))*10}", True, (255, 255, 255))
        screen.blit(score_text, SCORE_POSITION)

        # Draw Level
        level_text = self.font.render(f"Level: {self.level}", True, (255, 255, 255))
        level_position = (SCORE_POSITION[0], SCORE_POSITION[1] + 40)
        screen.blit(level_text, level_position)

    def update(self, dt):
        self.score += (dt * SCORE_RATE)

    def hit(self):
        self.score += 1000

    def get_score(self):
        print(f"Raw score value: {self.score}")
        return self.score
    
    def set_level(self, level): # updates level
        self.level = level