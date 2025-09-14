import pygame
from sys import exit

from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    Shot.containers = (drawable, shots, updatable)

    field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for thing in updatable:
            thing.update(dt)

        if player.timeout >= 0:
            player.timeout -= dt

        for asteroid in asteroids:
            if player.collided(asteroid):
                if player.timeout < 0:
                    if player.lives == 0:
                        pygame.quit()
                        exit("Game Over!")
                    else:
                        player.reset(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                elif player.timeout >= 0 and player.timeout < 1:
                    player.timeout += dt
            for bullet in shots:
                if bullet.collided(asteroid):
                    asteroid.split(field)
                    bullet.kill()

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
