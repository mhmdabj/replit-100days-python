def lesson26(menu_choices):
    print("Welcome")
    print("to")
    print("Replit")
    for user in menu_choices:
        print("Press 1 to Play")
        print()
        print("Press 2 to Exit")
        if user == 1:
            print("Playing sound...")
            print("Paused.")
        elif user == 2:
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    lesson26([1, 2]) 