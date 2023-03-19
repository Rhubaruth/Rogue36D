import random


def roll_dice(n: int = 1):
    return sum(random.randint(1, 6) for _ in range(n))


class Player:
    def __init__(self, name, health, damage, attack_power=0, defense_power=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self, target):
        hit_roll = roll_dice(3) + self.attack_power
        print(f"{self.name} Attacks {target.name}. {hit_roll=} against {target.defense_power=}")
        if hit_roll >= target.defense_power:
            damage_roll = roll_dice()
            total_damage = self.damage + damage_roll
            target.take_damage(total_damage)
        else:
            print(self.name + " misses " + target.name + "!")

    def take_damage(self, amount):
        damage_taken = max(amount, 0)
        self.health -= damage_taken
        print(self.name + " takes " + str(damage_taken) + " damage!")
        print(self.name + " has " + str(self.health) + " health remaining.")

    def is_alive(self):
        return self.health > 0
