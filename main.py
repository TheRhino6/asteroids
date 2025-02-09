# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

# This is the main function that runs the game

def main():
    #initialize the pygame library
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    # This is the main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(BACKGROUND_COLOUR)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()