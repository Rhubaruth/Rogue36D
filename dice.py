import random


def roll_dice(n: int = 1):
    return sum(random.randint(1, 6) for _ in range(n))