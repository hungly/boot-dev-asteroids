import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        child_1_velocity = self.velocity.rotate(angle)
        child_2_velocity = self.velocity.rotate(-angle)
        child_1_radius = self.radius - ASTEROID_MIN_RADIUS
        child_2_radius = self.radius - ASTEROID_MIN_RADIUS
        child_1 = Asteroid(self.position.x, self.position.y, child_1_radius)
        child_1.velocity = child_1_velocity * 1.2
        child_2 = Asteroid(self.position.x, self.position.y, child_2_radius)
        child_2.velocity = child_2_velocity * 1.2

    def update(self, dt):
        self.position +=  self.velocity * dt