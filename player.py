from dice import roll_dice


BASE_HEALTH = 10
BASE_DAMAGE = 2
BASE_ARMOR = 12


class Player:
    def __init__(self, name,
                 strength: int = 9, dexterity: int = 9, constitution: int = 9,
                 intelligence: int = 9, wisdom: int = 9):
        self.name = name

        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom

        self.max_health = BASE_HEALTH + (self.constitution - 10) // 2
        self.health = self.max_health
        self.damage = BASE_DAMAGE
        self.attack_power = max((self.strength - 10) // 2, (self.dexterity - 10) // 2)
        self.defense_power = BASE_ARMOR + (self.dexterity - 10) // 2

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
