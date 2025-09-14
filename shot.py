import pygame

from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, rotation, velocity=0):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = velocity

    def draw(self, screen):
        offset = pygame.Vector2(0, SHOT_LENGTH/2).rotate(self.rotation)
        pygame.draw.line(screen, "white", self.position + offset, self.position - offset, 2)

    def update(self, dt):
        self.position += self.velocity * dt
