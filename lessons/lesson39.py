def hangman(word, guesses, lives=6):
    letterPicked = []
    idx = 0
    while True:
        if idx >= len(guesses):
            break
        letter = guesses[idx].lower()
        idx += 1
        if letter in letterPicked:
            print("You've tried that before")
            continue
        letterPicked.append(letter)
        if letter in word:
            print("You found a letter")
        else:
            print("Nope, not in there")
            lives -= 1
        allLetters = True
        print()
        for i in word:
            if i in letterPicked:
                print(i, end="")
            else:
                print("_", end="")
                allLetters = False
        print()
        if allLetters:
            print(f"You won with {lives} left!")
            break
        if lives<=0:
            print(f"You ran out of lives! The answer was {word}")
            break
        else:
            print(f"Only {lives} left")

if __name__ == "__main__":
    hangman("apple", ["a", "p", "l", "e"])
    hangman("pear", ["x", "y", "z", "p", "e", "a", "r"]) 