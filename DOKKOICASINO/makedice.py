import random

def makedice():
    dice = []
    for i in range(3):
        dice.append(random.randint(1, 6))
    return dice
