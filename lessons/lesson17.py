def lesson17(moves):
    print("Welcome to ROCK, PAPER, SCISSORS GAME!")
    p1_score = 0
    p2_score = 0
    for player_1, player_2 in moves:
        if p1_score < 3 and p2_score < 3:
            if player_1 == "R":
                if player_2 == "R":
                    print("tie")
                elif player_2 == "P":
                    print("p2 won")
                    p2_score += 1
                elif player_2 == "S":
                    print("p1 won")
                    p1_score += 1
            elif player_1 == "P":
                if player_2 == "R":
                    print("p1 won")
                    p1_score += 1
                elif player_2 == "P":
                    print("tie")
                elif player_2 == "S":
                    print("p2 won")
                    p2_score += 1
            elif player_1 == "S":
                if player_2 == "R":
                    print("p2 won")
                    p2_score += 1
                elif player_2 == "P":
                    print("p1 won")
                    p1_score += 1
                elif player_2 == "S":
                    print("tie")
            else:
                print("gg")
            if p1_score == 3:
                print("Game over, PLAYER 1 WON")
                break
            elif p2_score == 3:
                print("Game over, PLAYER 1 WON")
                break
    
if __name__ == "__main__":
    lesson17([("R", "S"), ("P", "R"), ("S", "P"), ("R", "P"), ("P", "S")]) 