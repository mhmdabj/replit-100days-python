def lesson16(guesses):
    print(" Fill in the blank lyrics!\n(Type in the blank lyrics and see if you are as cool as me.)")
    print()
    attempt = 0
    for fill in guesses:
        print("Never going to ______ you up.")
        attempt += 1
        if fill != "give":
            print("Nope, try again.")
        else:
            break
    print("Well done! It only took you", attempt, "attempts.")

if __name__ == "__main__":
    lesson16(["take", "give"]) 