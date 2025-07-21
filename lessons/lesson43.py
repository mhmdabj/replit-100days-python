import random

def generate_bingo_card(seed=None):
    if seed is not None:
        random.seed(seed)
    numbers = [random.randint(1, 90) for _ in range(8)]
    numbers.sort()
    bingo = [ [ numbers[0], numbers[1], numbers[2]],
              [ numbers[3], "BINGO", numbers[4] ],
              [ numbers [5], numbers[6], numbers[7]] ]
    for row in bingo:
        print(row)
    return bingo

if __name__ == "__main__":
    generate_bingo_card(seed=42) 