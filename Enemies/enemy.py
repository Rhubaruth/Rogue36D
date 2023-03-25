from character_base import roll_dice, Attributes


class Enemy:
    attributes: Attributes

    def __init__(self, attributes: Attributes):

        self.attributes = attributes
        pass

    def attack(self):
        pass

    def take_dmg(self):
        pass
