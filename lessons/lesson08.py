def lesson8(name, day):
    if(name == "Abuj" or name =="abuj"):
        print("Hello Abuja")
        if(day=="Monday" or day=="monday"):
            print("It is Monday, the weekend is over.")
        elif(day=="Friday" or day=="friday"):
            print("It is Friday, the weekend is close.")
    elif(name == "hadi" or name =="Hadi"):
        print("Hello Hadi")
        if(day=="Monday" or day=="monday"):
            print("emhiha w back to work")
        elif(day=="Friday" or day=="friday"):
            print("friday time for gamming ^^")
    else:
        print("Invalid name or day")
        print("Please try again")

# Example usage for testing
if __name__ == "__main__":
    lesson8("Abuj", "Monday")
    lesson8("hadi", "Friday")
    lesson8("Alice", "Sunday") 