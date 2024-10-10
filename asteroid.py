import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            astro1 = Asteroid(self.position.x, self.position.y, new_radius)
            astro1.velocity = self.velocity.rotate(-angle) * 1.2

            astro2 = Asteroid(self.position.x, self.position.y, new_radius)
            astro2.velocity = self.velocity.rotate(angle) * 1.2
