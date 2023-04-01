from dataclasses import dataclass
from character_base import roll_dice, Attributes

BASE_HEALTH = 10
BASE_DAMAGE = 2
BASE_ARMOR = 12
BASE_MANA = 0

@dataclass
class Player:
    attributes: Attributes

    def __init__(self, name, attributes: Attributes):
        self.name = name

        self.attributes = attributes

        self.max_health = BASE_HEALTH + self.attributes.get_modifier('con')
        self.health = self.max_health
        self.damage = BASE_DAMAGE
        self.attack_power = self.attributes.get_modifier('str')
        self.defense_power = BASE_ARMOR + self.attributes.get_modifier('dex')

        self.mana = BASE_MANA + self.attributes.get_modifier('int')

    def attack(self, target):
        hit_roll = roll_dice(3) + self.attack_power
        print(f"{self.name} Attacks {target.name}. {hit_roll=} against {target.defense_power=}")
        if hit_roll < target.defense_power:
            print(f"{self.name} missed {target.name}!")
            return
        damage_roll = max(roll_dice(), roll_dice())
        total_damage = self.damage + damage_roll
        target.take_damage(total_damage)

    def take_damage(self, amount):
        damage_taken = max(amount, 0)
        self.health -= damage_taken
        print(self.name + " takes " + str(damage_taken) + " damage!")
        print(f"{self.name} has {self.health}/{self.max_health} HP.")

    def is_alive(self):
        return self.health > 0
