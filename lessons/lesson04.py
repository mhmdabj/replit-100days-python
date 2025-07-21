def lesson4(name, enemy, superpower, live, food):
    print("==== Welcome to YOUR ADVENTURE =====")
    print("Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!")
    print()
    print("Hello ", name, "! Your ability to", superpower, "will make sure you never have to look at", enemy, "again. Go eat", food, "as you walk down the streets of", live, "and use", superpower)
    print("\033[31m Oh no! \033[0m You just ran into", enemy, "!\n")
    print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[32m", "for being a bad, bad person.")

# Example usage for testing
if __name__ == "__main__":
    lesson4("Alice", "Bob", "fly", "Paris", "Pizza") 