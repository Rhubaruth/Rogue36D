import random
from dataclasses import dataclass


def roll_dice(n: int = 1):
    return sum(random.randint(1, 6) for _ in range(n))


@dataclass
class Attributes:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int

    def __init__(self,
                 strength: int = 9, dexterity: int = 9, constitution: int = 9,
                 intelligence: int = 9, wisdom: int = 9):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom

    def get_modifier(self, stat) -> int:
        att = {
            'STR': self.strength,
            'DEX': self.dexterity,
            'CON': self.constitution,
            'INT': self.intelligence,
            'WIS': self.wisdom
        }
        stat = stat.upper()
        if stat not in att.keys():
            return -1
        return (att.get(stat) - 10) // 2
