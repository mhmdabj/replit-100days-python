import random

def pinPicker(number, seed=None):
    if seed is not None:
        random.seed(seed)
    pin = ""
    for i in range(number):
        pin += str(random.randint(0,9))
    return pin

def rollDice(side):
    return random.randint(1, side)

def healthBar(seed=None):
    if seed is not None:
        random.seed(seed)
    roll_6_sided_dice = rollDice(6)
    roll_8_sided_dice = rollDice(8)
    health = roll_6_sided_dice * roll_8_sided_dice
    return health

def character_stats(names, seed=None):
    if seed is not None:
        random.seed(seed)
    for name in names:
        health = str(healthBar())
        print(f"Their health is: {health}")

if __name__ == "__main__":
    print(pinPicker(4, seed=42))
    character_stats(["Alice", "Bob", "Charlie"], seed=42) 