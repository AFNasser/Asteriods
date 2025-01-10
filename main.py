import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    dt = 0  # delta Time
    timer = pygame.time.Clock() # time tracking object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    # player initialization
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # astroid field initialization
    astroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            return

        screen.fill("black")    

        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        for ast_obj in asteroids:
            if player.check_collision(ast_obj):
                print("Game over!")
                sys.exit()
            for shot_obj in shots:
                if shot_obj.check_collision(ast_obj):
                    ast_obj.split()
                    shot_obj.kill()

        # limit framerate to 60 fps
        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()