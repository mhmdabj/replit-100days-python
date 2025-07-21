class AuthSystem85:
    def __init__(self):
        self.users = {}
        self.session = {}
    def signup(self, username, name, password):
        if self.session.get("loggedIn"):
            return "Already logged in"
        if username not in self.users:
            self.users[username] = {"name": name, "password": password}
            return "Signup successful"
        else:
            return "User already exists"
    def login(self, username, password):
        if self.session.get("loggedIn"):
            return "Already logged in"
        if username not in self.users:
            return "User not found"
        if password == self.users[username]["password"]:
            self.session["loggedIn"] = username
            return f"Welcome {self.users[username]['name']}"
        else:
            return "Incorrect password"
    def logout(self):
        self.session.clear()
        return "Logged out"
    def welcome(self):
        if "loggedIn" in self.session:
            return f"Hi there {self.users[self.session['loggedIn']]['name']}"
        else:
            return "Not logged in"

if __name__ == "__main__":
    auth = AuthSystem85()
    print(auth.signup("david", "David", "Baldy1"))
    print(auth.login("david", "Baldy1"))
    print(auth.welcome())
    print(auth.logout())
    print(auth.welcome()) 