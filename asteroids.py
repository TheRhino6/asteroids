import pygame
import random
from circleshape import *
from constants import *
from score import Score

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.life_timer = 0
        self.bounce_count = 0

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOUR, self.position, self.radius, 2)

    def update(self, dt):
        self.life_timer += dt
        if self.position.x + self.radius >= SCREEN_WIDTH and self.life_timer >= 2 and self.bounce_count <= ASTEROID_MAX_BOUNCE:
            self.velocity.x *= -ASTEROID_BOUNCE_RATIO
            self.bounce_count += 1
        elif self.position.x + self.radius <= 0 and self.life_timer >= 2 and self.bounce_count <= ASTEROID_MAX_BOUNCE:
            self.velocity.x *= -ASTEROID_BOUNCE_RATIO
            self.bounce_count += 1
        elif self.position.y + self.radius >= SCREEN_HEIGHT and self.life_timer >= 2 and self.bounce_count <= ASTEROID_MAX_BOUNCE:
            self.velocity.y *= -ASTEROID_BOUNCE_RATIO
            self.bounce_count += 1
        elif self.position.y + self.radius <= 0 and self.life_timer >= 2 and self.bounce_count <= ASTEROID_MAX_BOUNCE:
            self.velocity.y *= -ASTEROID_BOUNCE_RATIO
            self.bounce_count += 1
        
        self.position += self.velocity * dt

    def split(self, score):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            score.asteroid_kill_score()
            return
        
        else:
            score.asteroid_split_score()
            angle = random.uniform(20, 50)
            a = self.velocity.rotate(angle)
            b = self.velocity.rotate(-angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroids(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = a * 1.2
            new_asteroid = Asteroids(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = b * 1.2