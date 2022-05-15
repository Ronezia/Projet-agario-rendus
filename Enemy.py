import random

from pygame.math import Vector2

import Constants
from MovingEntity import MovingEntity

import core


class Enemy(MovingEntity):
    def __init__(self):
        super().__init__()
        self.lastUpdateDirection = 0
        self.nextTickDirectionUpdate = random.randint(20, 100)
        self.lastDirection = Vector2(random.randint(0, Constants.screenDimensions[0]),
                                     random.randint(0, Constants.screenDimensions[1]))
        self.position = Vector2(random.randint(self.radius * 2, Constants.screenDimensions[0] - self.radius * 2),
                                random.randint(self.radius * 2, Constants.screenDimensions[1] - self.radius * 2))
        # core.memory("c", Creep())

    def eat_enemies(self, enemies):
        for index, enemy in enumerate(enemies):
            if self != enemy and enemy.position.distance_to(self.position) < self.radius and self.radius > enemy.radius:
                core.memory("Ennemi").pop(index)  # Clear creep from board
                self.take_weight_from_enemy(enemy)
                core.memory("Ennemi").append(Enemy())  # Add a new Enemy to the board

    def execute_movement(self):
        if self.lastUpdateDirection > self.nextTickDirectionUpdate:
            self.lastDirection = Vector2(random.randint(0, Constants.screenDimensions[0]),
                                         random.randint(0, Constants.screenDimensions[1]))
            self.lastUpdateDirection = 0
            self.nextTickDirectionUpdate = random.randint(40, 80)
        else:
            self.lastUpdateDirection += 1
        self.movement(self.lastDirection)

    def draw(self):
        core.Draw.circle(self.color, self.position, self.radius)


'''
    #creation du manger des ennemi sur creep
    for p in creep: 
        if p.position.distance_to(self.position) < self.vision
            creepdansvision.append(p)
            if p.position.distance_to(self.position) < distancecreep :
                cible = p
                distancecreep  = p.position.distance_to(self.position)
'''
