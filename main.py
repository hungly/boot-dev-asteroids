# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player

def main():
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.get_surface().fill((0,0,0))

        player.update(dt)
        player.draw(pygame.display.get_surface())

        pygame.display.flip()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()