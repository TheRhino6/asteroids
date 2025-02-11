# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from Shot import *
from score import *
from game import *

# This is the main function that runs the game

def main():
    game = Game()
    
    while game.running:
        game.handle_events()
        game.update()
    pygame.quit()

if __name__ == "__main__":
    main()