class AuthSystem84:
    def __init__(self):
        self.users = {}
    def signup(self, username, name, password):
        if username not in self.users:
            self.users[username] = {"name": name, "password": password}
            return "Signup successful"
        else:
            return "User already exists"
    def login(self, username, password):
        if username not in self.users:
            return "User not found"
        if password == self.users[username]["password"]:
            return f"Hello {self.users[username]['name']}"
        else:
            return "Incorrect password"

if __name__ == "__main__":
    auth = AuthSystem84()
    print(auth.signup("david", "David", "Baldy1"))
    print(auth.signup("david", "David", "Baldy1"))
    print(auth.login("david", "Baldy1"))
    print(auth.login("david", "wrong"))
    print(auth.login("bob", "Baldy1")) 