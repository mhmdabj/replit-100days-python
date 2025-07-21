import random

def rollDice(side, roll_again_responses):
    idx = 0
    while idx < len(roll_again_responses):
        dice = random.randint(1, side)
        print("Your rolled", dice)
        rollAgain = roll_again_responses[idx]
        idx += 1
        if rollAgain == "y":
            continue
        else:
            print("Goodbye!")
            break

if __name__ == "__main__":
    rollDice(6, ["y", "n"]) 