def lesson14(player_1, player_2):
    print("Welcome to ROCK, PAPER, SCISSORS GAME!")
    if player_1 == "R":
        if player_2 == "R":
            print("tie")
        elif player_2 == "P":
            print("p2 won")
        elif player_2 == "S":
            print("p1 won")
    elif player_1 == "P":
        if player_2 == "R":
            print("p1 won")
        elif player_2 == "P":
            print("tie")
        elif player_2 == "S":
            print("p2 won")
    elif player_1 == "S":
        if player_2 == "R":
            print("p2 won")
        elif player_2 == "P":
            print("p1 won")
        elif player_2 == "S":
            print("tie")
    else:
        print("gg")

if __name__ == "__main__":
    lesson14("R", "S")
    lesson14("P", "R")
    lesson14("S", "S")
    lesson14("X", "R") 