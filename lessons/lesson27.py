import random
import time

def rollDice(side):
    return random.randint(1, side)

def health():
    hp = ((rollDice(6) * rollDice(12)) / 2 ) + 10
    return hp

def strength():
    st = ((rollDice(6) * rollDice(12)) / 2 ) + 12
    return st

def lesson27(characters, seed=None):
    if seed is not None:
        random.seed(seed)
    for name, ch in characters:
        print(name)
        print("HEALTH:", health())
        print("STRENGTH:", strength())
    print("May your name go down in Legend...")

if __name__ == "__main__":
    lesson27([("Alice", "Elf"), ("Bob", "Orc")], seed=42) 