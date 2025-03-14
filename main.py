import pygame
from constants import *
import sys
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from level import Level

def main():
    # initialise code
    pygame.init()
    print ("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Asteroids 2.0")

    # Create containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    score = pygame.sprite.Group()
    level = pygame.sprite.Group()

    # Assign to containers
    Player.containers = (updatable, drawable)
    Asteroids.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    Score.containers = (updatable, drawable, score)
    Level.containers = (drawable, level)

    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    score_display = Score()
    level_display = Level()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        level_display.update(dt, score_display.score)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print ("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split(score_display)

        screen.fill(BACKGROUND_COLOUR)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000 # limit frames to 60 FPS

if __name__ == "__main__":
    main()