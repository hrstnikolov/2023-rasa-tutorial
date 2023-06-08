import random
from enum import auto, Enum


class Moves(Enum):
    Rock = auto()
    Paper = auto()
    Scissors = auto()


x = random.choice(list(Moves))
print()
