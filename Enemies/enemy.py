from character_base import roll_dice, Attributes
from player import Player

class Enemy(Player):
    attributes: Attributes

    def __init__(self, name, attributes: Attributes, xp: int = 10):
        self.xp_reward = xp
        super().__init__(name, attributes)
        pass

    def attack(self, target):
        pass
