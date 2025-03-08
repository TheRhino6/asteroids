import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print ("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Assign to containers
    Player.containers = (updatable, drawable)

    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill(BACKGROUND_COLOUR)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000 # limit frames to 60 FPS

if __name__ == "__main__":
    main()