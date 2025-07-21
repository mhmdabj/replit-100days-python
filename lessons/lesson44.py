import random

def prettyPrint(card):
    print()
    for row in card:
        print(row)
    print()

def bingo_marking(seed=None, numbers_to_mark=None):
    if seed is not None:
        random.seed(seed)
    numbers = [random.randint(1, 90) for _ in range(8)]
    numbers.sort()
    card = [[numbers[0], numbers[1], numbers[2]], [numbers[3], "Bingo", numbers[4]], [numbers[5], numbers[6], numbers[7]]]
    won = 0
    if numbers_to_mark is None:
        numbers_to_mark = []
    for next_nb in numbers_to_mark:
        prettyPrint(card)
        if(won == 8):
            print("You have won")
            break
        i = 0
        for row in card:
            if next_nb in row:
                for item in row:
                    i += 1
                    if next_nb == item:
                        row[i - 1] = "X"
                        won += 1
    prettyPrint(card)
    if won == 8:
        print("You have won")
    return card

if __name__ == "__main__":
    bingo_marking(seed=42, numbers_to_mark=[1,2,3,4,5,6,7,8]) 