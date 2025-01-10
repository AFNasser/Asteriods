import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        
        split_angle = random.uniform(20, 50)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        
        split_asteroid_1 = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid_1.velocity = self.velocity.rotate(split_angle) * 1.2

        split_asteroid_2 = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid_2.velocity = self.velocity.rotate(-split_angle) * 1.2
        
        


