from Enemy import Enemy
import core
from MovingEntity import MovingEntity


class Avatar(MovingEntity):
    def __init__(self):
        super().__init__()
        # core.memory("c", Creep())

    def eat_enemies(self, enemies):
        for index, enemy in enumerate(enemies):
            if enemy.position.distance_to(self.position) < self.radius and self.radius > enemy.radius:
                print('eat ennemy')
                core.memory("Ennemi").pop(index)  # Clear creep from board
                self.take_weight_from_enemy(enemy)
                core.memory("Ennemi").append(Enemy())  # Add a new Enemy to the board

    def check_ennemi_collision(self, enemies):
        for index, enemy in enumerate(enemies):
            # noinspection PyChainedComparisons
            if enemy.position.distance_to(self.position) < self.radius and self.radius < enemy.radius:
                return True