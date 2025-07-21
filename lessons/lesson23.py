import random

def rollDice():
    dice = random.randint(1, 6)
    print("You rolled", dice)

def login(attempts):
    print("Replit Login System")
    for username, password in attempts:
        if username == "abuj" and password == "lol":
            print("Welcome to your website!")
            break
        else:
            print("Whoops! I don't recognize that username or password. Try again!")

if __name__ == "__main__":
    rollDice()
    login([("abuj", "wrong"), ("abuj", "lol")]) 