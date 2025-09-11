import pygame

from circleshape import CircleShape
from shot import Shot
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_countdown = 0.0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward_unit = pygame.Vector2(0, 1).rotate(self.rotation)
        lateral_unit = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        apex = self.position + forward_unit * self.radius
        left_vertex = self.position - forward_unit * self.radius - lateral_unit
        right_vertex = self.position - forward_unit * self.radius + lateral_unit

        return [apex, left_vertex, right_vertex]

    def update(self, dt):
        self.shot_countdown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_SPACE] and self.shot_countdown <= 0:
            self.shoot()

    def move(self, dt):
        unit = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += unit * PLAYER_SPEED * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        unit = pygame.Vector2(0, 1).rotate(self.rotation)
        apex = self.position + unit * self.radius
        velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

        Shot(apex.x, apex.y, velocity)

        self.shot_countdown = PLAYER_SHOOT_COOLDOWN

