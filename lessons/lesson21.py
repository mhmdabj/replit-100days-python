def lesson21(number, answers):
    print("Math game!")
    counter = 0
    for i in range(1, 11):
        answer = answers[i-1]
        if (answer != i * number):
            print(f"Nope. The answer was {i * number}")
        elif answer == i * number:
            print("Great work!")
            counter += 1
    print("---")
    print()
    print(f"You scored {counter} out of 10.")

if __name__ == "__main__":
    lesson21(2, [2,4,6,8,10,12,14,16,18,20])
    lesson21(3, [3,6,9,12,15,18,21,24,27,0]) 