import pygame

from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS


def draw_lives(screen: pygame.Surface, number: int) -> None:
    height = width = ASTEROID_MAX_RADIUS
    for _ in range(number):
        position = pygame.Vector2(height, width)
        pygame.draw.circle(screen, "white", position, ASTEROID_MIN_RADIUS, 0)
        height += ASTEROID_MAX_RADIUS