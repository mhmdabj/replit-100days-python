def reverse(value):
    if value <= 0:
        print("Done!")
        return
    else:
        for i in range(value):
            print("💯", end="")
        print()
        reverse(value - 2)

def factorial(value):
    if value == 1:
        return 1
    else:
        return value * factorial(value-1)

if __name__ == "__main__":
    reverse(10)
    print(factorial(5)) 