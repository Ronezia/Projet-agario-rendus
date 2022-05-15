import random
import pygame
from pygame.math import Vector2

import Constants


class Creep:
    def __init__(self):
        self.radius = Constants.creepRadius
        self.mass = Constants.creepMass
        self.food = Constants.creepFood
        self.position = Vector2(random.randint(self.radius * 2, Constants.screenDimensions[0] - self.radius * 2),
                                random.randint(self.radius * 2, Constants.screenDimensions[1] - self.radius * 2))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def ghost(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)