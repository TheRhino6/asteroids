import pygame
from constants import *
import sys
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # initialise code
    pygame.init()
    print ("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign to containers
    Player.containers = (updatable, drawable)
    Asteroids.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for obj in asteroids:
            if player.collision(obj):
                print ("Game over!")
                sys.exit()

        screen.fill(BACKGROUND_COLOUR)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000 # limit frames to 60 FPS

if __name__ == "__main__":
    main()