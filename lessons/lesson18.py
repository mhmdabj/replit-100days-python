def lesson18(chosen, guesses):
    print("Guess the Number game :)")
    guessCounter = 0
    for guess in guesses:
        if(guess / chosen < 1):
            print("Too low")
            guessCounter += 1
        elif (guess / chosen > 1):
            print("Too high")
            guessCounter += 1
        elif guess == chosen:
            print("correct")
            break
        else:
            print("type a number bro :)")
            break
    print("It took you", guessCounter, "to get it correct")

if __name__ == "__main__":
    lesson18(50, [10, 100, 50]) 