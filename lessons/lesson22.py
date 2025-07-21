def lesson22(target, guesses):
    print("Totally Random One-Million-to-One")
    guessCount = 1
    for guess in guesses:
        if guess == target:
            print("Correct 😁")
            break
        elif guess < target:
            print("Too low fanta")
            guessCount += 1
        elif guess > target:
            print("Too high light")
            guessCount += 1
        else:
            print("Put a number bruv ^^ ")
            return
    print(f"It took you {guessCount} guesses to get the number correct.")

if __name__ == "__main__":
    lesson22(42, [10, 100, 42]) 