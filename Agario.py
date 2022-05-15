import sys

import pygame

import Constants
import core
from Creep import Creep
from Avatar import Avatar

from Enemy import Enemy


def setup():
    print("Setup START----------")

    core.fps = 60
    core.WINDOW_SIZE = Constants.screenDimensions
    core.memory("c", Creep())
    core.memory("a", Avatar())
    core.memory("listCreep", [])
    core.memory("nbrCreep", Constants.numberOfCreeps)
    core.memory("e", Enemy())
    core.memory("Ennemi", [])
    core.memory("nbrEnnemi", Constants.numberOfEnemies)

    for i in range(0, core.memory("nbrEnnemi")):
        core.memory("Ennemi").append(Enemy())

    for i in range(0, core.memory("nbrCreep")):
        core.memory("listCreep").append(Creep())
    print("Setup END----------")


def run():
    core.cleanScreen()

    core.memory("a").draw()

    for moncreep in core.memory("listCreep"):
        moncreep.draw(core.screen)

    for enemy in core.memory("Ennemi"):
        enemy.draw()

    for enemy in core.memory("Ennemi"):
        enemy.execute_movement()

    for enemy in core.memory("Ennemi"):
        enemy.eat_creeps(core.memory("listCreep"))

    for enemy in core.memory("Ennemi"):
        enemy.eat_enemies(core.memory("Ennemi"))

    for enemy in core.memory("Ennemi"):
        enemy.edges_collisions()

    core.memory("a").movement(core.getMouseLeftClick())
    core.memory("a").edges_collisions()

    core.memory("a").eat_creeps(core.memory("listCreep"))
    core.memory("a").eat_enemies(core.memory("Ennemi"))

    # Check if the game is lost
    if core.memory("a").check_ennemi_collision(core.memory("Ennemi")):
        pygame.display.quit()
        sys.exit()

core.main(setup, run)
