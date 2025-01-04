# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
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

    Player.containers = (updatable, drawable)

    # player initialization
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in updatable:
            obj.draw(screen)

        pygame.display.flip()

        # limit framerate to 60 fps
        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()