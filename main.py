# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Init pygame
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up clock
    clock = pygame.time.Clock()
    dt = 0

    # Set up groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Create objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while(True):
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.get_surface().fill((0,0,0))

        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
            if (asteroid.isCollided(player)):
                print("Game over!")
                return
        for object in drawable:
            object.draw(pygame.display.get_surface())

        pygame.display.flip()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()