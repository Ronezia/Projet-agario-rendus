import random

from pygame.math import Vector2

import Constants
import core
from Creep import Creep


class MovingEntity:
    def __init__(self):
        self.position = Constants.centerPosition
        self.radius = Constants.playerRadius
        self.food = Constants.playerFood
        self.mass = Constants.playerMass
        self.speed = Constants.speed
        self.acceleration = Constants.acceleration
        self.maxAcceleration = Constants.maxAcceleration
        self.l0 = Constants.springBusyLength
        self.k = Constants.springStiffness
        self.minSpeed = Constants.minSpeed
        self.maxSpeed = Constants.maxSpeed
        self.maxSize = Constants.minSpeed
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def movement(self, destination):
        if destination is not None:
            # F=uk|l-lo|
            l = self.position.distance_to(destination)
            u = destination - self.position
            u = u.normalize()
            self.acceleration = u * self.k * abs(l - self.l0)

        # bilan des force

        # attention max force
        if self.acceleration.length() > self.maxAcceleration:
            self.acceleration.scale_to_length(self.maxAcceleration)

        # ajout de F a la vitess
        self.speed = self.speed + self.acceleration

        # attention max et min vitess
        if self.speed.length() > self.maxSpeed:
            self.speed.scale_to_length(self.maxSpeed)

        if self.speed.length() + 2 < self.minSpeed:
            self.speed.scale_to_length(self.minSpeed)

        # ajout vitesse a position
        self.position = self.position + self.speed

        # remise a zero de F
        self.acceleration = Vector2(0, 0)

    def edges_collisions(self):
        if self.position.y + self.radius > core.WINDOW_SIZE[1]:
            self.position = Vector2(self.position.x, core.WINDOW_SIZE[1] - self.radius)
        if self.position.x + self.radius > core.WINDOW_SIZE[0]:
            self.position = Vector2(core.WINDOW_SIZE[0] - self.radius, self.position.y)
        if self.position.x - self.radius < 0:
            self.position = Vector2(self.radius, self.position.y)
        if self.position.y - self.radius < 0:
            self.position = Vector2(self.position.x, self.radius)

    def eat_creeps(self, creeps):
        for index, creep in enumerate(creeps):
            if creep.position.distance_to(self.position) < self.radius + creep.radius:
                core.memory("listCreep").pop(index)  # Clear creep from board
                self.take_weight_from_creep(creep)
                print(self.food, self.mass)
                core.memory("listCreep").append(Creep())  # Clear creep from board

    def take_weight_from_enemy(self, enemy):
        self.food += enemy.food
        self.mass += enemy.mass
        self.radius += enemy.radius / self.radius

    def take_weight_from_creep(self, creep):
        self.food += creep.food
        self.mass += creep.mass
        self.radius += Constants.playerRadiusGainedFromCreep

    def draw(self):
        core.Draw.circle(self.color, self.position, self.radius)
        core.Draw.line((1, 43, 92), self.position, self.position + self.speed * 100, 1)
