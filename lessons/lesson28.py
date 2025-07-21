import random
import time

def rollDice(side):
    return random.randint(1, side)

def health():
    hp = ((rollDice(6) * rollDice(12)) / 2) + 10
    return hp

def strength():
    st = ((rollDice(6) * rollDice(12)) / 2) + 12
    return st

def lesson28(name1, ch1, name2, ch2, seed=None):
    if seed is not None:
        random.seed(seed)
    print(name1)
    health1 = health()
    strength1 = strength()
    print("HEALTH:", health1)
    print("STRENGTH:", strength1)
    print()
    print(name2)
    health2 = health()
    strength2 = strength()
    print("HEALTH:", health2)
    print("STRENGTH:", strength2)
    round_num = 1
    while True:
        print("⚔️ BATTLE TIME ⚔️")
        strengthDiff = abs(strength1 - strength2)
        roll1 = rollDice(6)
        roll2 = rollDice(6)
        if roll1 > roll2:
            health2 -= strengthDiff
            if round_num == 1:
                print(name1, "wins the first blow")
            else:
                print(name1, "wins round", round_num)
            print(name2, "takes a hit, with", strengthDiff, "damage")
        elif roll2 > roll1:
            health1 -= strengthDiff
            if round_num == 1:
                print(name2, "wins the first blow")
            else:
                print(name2, "wins round", round_num)
            print(name1, "takes a hit, with", strengthDiff, "damage")
        print(name1)
        print("HEALTH:", health1)
        print(name2)
        print("HEALTH:", health2)
        if (health1 <= 0):
            print("Oh no", name1, "has died!")
            print(name2, "destroyed", name1, " in ", round_num, " rounds!")
            break
        elif (health2 <= 0):
            print("Oh no", name2, "has died!")
            print(name1, "destroyed", name2, " in ", round_num, " rounds!")
            break
        else:
            print("And they're both standing for the next round!")
            round_num += 1

if __name__ == "__main__":
    lesson28("Alice", "Elf", "Bob", "Orc", seed=42) 