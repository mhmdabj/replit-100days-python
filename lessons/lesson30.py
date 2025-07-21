def format_examples():
    name = "Katie"
    age = "28"
    pronouns = "she/her"
    print("This is {}, using {} pronouns, and is {} years old.".format(name, pronouns, age))
    print("This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age))
    response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"
    print(response)
    for i in range(1, 31):
        print(f"Day {i: >2} of 30")

def exercise(thoughts):
    for i in range(1, 31):
        print(f"Day {i}: ")
        user = thoughts[i-1]
        print(f"You thought day {i} was {user}")
    print("30 Days Down - What did you think?")
    print()
    for i in range(1, 31):
        thought = thoughts[i-1]
        print()
        myText = f"You thought Day {i} was"
        print(f"{myText:^35}")
        print(f"{thought:^35}")
        print()

if __name__ == "__main__":
    format_examples()
    exercise([f"thought {i}" for i in range(1, 31)]) 