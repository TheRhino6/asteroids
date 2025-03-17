import pygame
import sys
from circleshape import *
from constants import *
from shot import Shot
from shield import Shield

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.jump_timer = 0
        self.speed = PLAYER_SPEED
        self.is_hit = False
        self.flash_timer = 0
        self.flash_duration = 1.5 # seconds
        self.visible = True
        self.shield_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        if self.visible:
            pygame.draw.polygon(screen, PLAYER_COLOUR, self.triangle(), 0)
            #screen.blit(self.image, self.rect)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if self.jump_timer > PLAYER_JUMP_COOLDOWN - 0.1:
            self.position += forward * PLAYER_SPEED * PLAYER_JUMP_RATIO * dt #jump speed

        self.position += forward * PLAYER_SPEED * dt #normal speed

        # screen wrap
        if self.position.x >= SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x <= 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.y >= SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y <= 0:
            self.position.y = SCREEN_HEIGHT

    def update(self, dt):
        self.timer -= dt
        self.jump_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
        if keys[pygame.K_LSHIFT]:
            if self.jump_timer <= 0:
                self.jump()
        if keys[pygame.K_q]:
            self.shield()
        if keys[pygame.K_ESCAPE]:
            print ("forced quit with key press")
            sys.exit()

        if self.is_hit:
            self.flash_timer += dt
            if int(self.flash_timer * 10) % 2 == 0:
                self.visible = True
            else:
                self.visible = False

            if self.flash_timer >= self.flash_duration:
                self.is_hit = False
                self.flash_timer = 0
                self.visible = True

    def shoot(self):
        self.timer = PLAYER_SHOOT_COOLDOWN
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def jump(self):
        self.jump_timer = PLAYER_JUMP_COOLDOWN

    def hit(self):
        self.is_hit = True
        self.flash_timer = 0

    def shield(self):
        self.shield_timer = 0.5
        shield = Shield(self.position.x, self.position.y)