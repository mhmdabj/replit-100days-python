def guessing_game(guesses, target):
    attempts = 0
    for guess in guesses:
        if guess > target:
            print("Too high")
            attempts += 1
        elif guess < target:
            print("Too low")
            attempts += 1
        else:
            print("Just right!")
            print(f"{attempts} attempts this round")
            return attempts
    print("Game ended without correct guess.")
    return attempts

if __name__ == "__main__":
    guessing_game([50, 25, 75, 42], 42) 