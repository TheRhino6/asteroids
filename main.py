import pygame
from constants import *

def main():
    pygame.init()
    print ("Starting Asteroids!")
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOUR)
        pygame.display.flip()

if __name__ == "__main__":
    main()