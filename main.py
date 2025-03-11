import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    # initialize pygame
    pygame.init()
    # get new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # fill screen with solid black
    # pygame.Surface.fill(screen, (0,0,0))
    #
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()


    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)


        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()


        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        # limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
