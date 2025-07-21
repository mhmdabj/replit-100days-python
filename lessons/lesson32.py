import random

def random_greeting(seed=None):
    greetings = ["Hello", "Bonjour", "Ni hao","Marhaba", "Hola"]
    if seed is not None:
        random.seed(seed)
    rNumber = random.randint(0,4)
    print(f"{greetings[rNumber]}, Welcome to heaven :) ")

if __name__ == "__main__":
    random_greeting(seed=42) 