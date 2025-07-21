def palindrome_iterative(myString):
    for i in range(len(myString)):
        if myString[i] != myString[-i-1]:
            print(f"{myString} is not a palindrome")
            return False
    print(f"{myString} is a palindrome")
    return True

def palindrome_recursive(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome_recursive(word[1:-1])

if __name__ == "__main__":
    palindrome_iterative("racecar")
    print(palindrome_recursive("racecar"))
    palindrome_iterative("hello")
    print(palindrome_recursive("hello")) 