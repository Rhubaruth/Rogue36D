from player import Player
from character_base import roll_dice, Attributes


class Warrior(Player):
    def __init__(self, name="Blessed Knight"):
        attributes = Attributes(
            strength=roll_dice(2) + 6,
            dexterity=roll_dice(3),
            constitution=roll_dice(2) + 6,
            intelligence=roll_dice(2) + 3,
            wisdom=roll_dice(2) + 3
            )
        super().__init__(name, attributes)


class Rogue(Player):
    def __init__(self, name="Sneaky Shadow"):
        attributes = Attributes(
            strength=roll_dice(2) + 3,
            dexterity=roll_dice(2) + 6,
            constitution=roll_dice(2) + 3,
            intelligence=roll_dice(6),
            wisdom=roll_dice(6)
            )
        super().__init__(name, attributes)

class Wizard(Player):

    def __init__(self, name="Smart Grandma"):
        attributes = Attributes(
            strength=roll_dice(2)+1,
            dexterity=roll_dice(3),
            constitution=roll_dice(2)+1,
            intelligence=roll_dice(2)+6,
            wisdom=roll_dice(2)+6
            )
        super().__init__(name, attributes)
