import pygame
import random

from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float, velocity: pygame.Vector2 = pygame.Vector2(0)) -> None:
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self, field):
        self.kill()
        field.asteroid_no -= 1
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            field.asteroid_no += 2
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            velocity = self.velocity.rotate(-angle) * 1.2
            Asteroid(self.position.x, self.position.y, new_radius, velocity)

            velocity = self.velocity.rotate(angle) * 1.2
            Asteroid(self.position.x, self.position.y, new_radius, velocity)
