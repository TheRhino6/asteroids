import pygame
from constants import *
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField
from Shot import Shot
from score import Score

class Game:
    def __init__(self):
        #initialize the pygame library
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Starting asteroids!")
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True

        # Game variables
        self.level = 1
        
        # Sprite groups
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        # Set containers
        Player.containers = (self.drawable, self.updatable)
        Asteroids.containers = (self.drawable, self.updatable, self.asteroids)
        AsteroidField.containers = (self.updatable,)
        Shot.containers = (self.drawable, self.updatable, self.shots)
        Score.containers = (self.drawable, self.updatable)

        # Create game objects
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.field = AsteroidField(self)
        self.score = Score()
        Asteroids.score = self.score

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        self.screen.fill(BACKGROUND_COLOUR)
        for d in self.drawable:
            d.draw(self.screen)      # draw all the drawable objects
        self.updatable.update(self.dt)   # update all the updatable objects
        self.check_collisions()             # check for collisions
        self.check_level_progression()       # check for level progression
        self.dt = self.clock.tick(60) / 1000 # Set the frame rate to 60 fps
        pygame.display.flip()   # update the display

    def check_collisions(self):
        for asteroid in self.asteroids: # Check for collisions with player
            if self.player.collides_with(asteroid):
                print("Game over!")
                print(self.score, self.level)
                self.running = False
        
        for asteroid in self.asteroids: # Check for collisions with shots
            for shot in self.shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

    def check_level_progression(self):
        current_score = self.score.get_score()
        threshold = self.level * self.level * 10000
        
        # level up if score is greater than threshold
        if current_score >= threshold:
            self.level += 1
            self.score.set_level(self.level)
            print(f"Level up! {self.level}")