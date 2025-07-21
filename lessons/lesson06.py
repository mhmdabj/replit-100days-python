def lesson6(login, password):
    if(login == "admin" and password == "admin"):
        print("Welcome to your page")
    elif(login == "user" and password == "user"):
        print("Welcome user")
    elif(login == "guest" and password == "guest"):
        print("Welcome guest")
    else:
        print("Wrong username or password")

# Example usage for testing
if __name__ == "__main__":
    lesson6("admin", "admin")
    lesson6("user", "user")
    lesson6("guest", "guest")
    lesson6("foo", "bar") 