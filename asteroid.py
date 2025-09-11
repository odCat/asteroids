import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=0):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, field):
        self.kill()
        field.asteroid_no -= 1
        if self.radius > ASTEROID_MIN_RADIUS:
            field.asteroid_no += 2
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            velocity = self.velocity.rotate(-angle) * 1.2
            astro1 = Asteroid(self.position.x, self.position.y, new_radius, velocity)

            velocity = self.velocity.rotate(angle) * 1.2
            astro2 = Asteroid(self.position.x, self.position.y, new_radius, velocity)
