class LoginSystem72:
    def __init__(self):
        self.users = {}
        self.salt = 1997
    def add_user(self, username, password):
        newPassword = f"{password}{self.salt}"
        newPassword = hash(newPassword)
        self.users[username] = {"password": newPassword, "salt": self.salt}
        print("Added successfully")
    def login(self, username, password):
        if username not in self.users:
            print("User not found")
            return False
        salt = self.users[username]["salt"]
        newPassword = f"{password}{salt}"
        newPassword = hash(newPassword)
        if newPassword == self.users[username]["password"]:
            print("Login successful")
            return True
        else:
            print("Error")
            return False

if __name__ == "__main__":
    sys = LoginSystem72()
    sys.add_user("david", "Baldy1")
    sys.login("david", "Baldy1")
    sys.login("david", "wrong")
    sys.login("bob", "Baldy1") 