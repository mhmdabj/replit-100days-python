def lesson15(inputs):
    # inputs: list of (animal, exit) tuples
    for animal, exit_ans in inputs:
        if animal == "Cow":
            print("A cow goes moo.")
        elif animal == "A Lesser Spotted lemur":
            print("Ummm...the Lesser Spotter Lemur goes awooga.")
        elif animal == "cat":
            print("meow")
        if exit_ans == "yes":
            break

if __name__ == "__main__":
    lesson15([("Cow", "no"), ("cat", "yes")]) 