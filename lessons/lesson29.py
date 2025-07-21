def print_numbers():
    for i in range(0, 100):
        print(i, end=", ")
    print()

def print_colored_strings():
    print("If you put")
    print("\033[33m", end="") # yellow
    print("nothing as the")
    print("\033[35m", end="") # purple
    print("end character")
    print("\033[32m", end="") # green
    print("then you don't")
    print("\033[0m", end="") # default
    print("get odd gaps")
    print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")

def color(word, color):
    if color == "red":
        return f"\033[31m{word}\033[0m"
    elif color == "green":
        return f"\033[32m{word}\033[0m"
    elif color == "yellow":
        return f"\033[33m{word}\033[0m"
    elif color == "blue":
        return f"\033[34m{word}\033[0m"
    else:
        return word

if __name__ == "__main__":
    print_numbers()
    print_colored_strings()
    print(color("mhmd", "red")) 