def flask_login(username, email, password, logins):
    details = logins.get(username)
    if not details:
        return "Username, email or password incorrect"
    if email == details["email"] and password == details["password"]:
        return "You are logged in"
    else:
        return "Username, email or password incorrect"

if __name__ == "__main__":
    logins = {
        "david": {"email": "a@a.com", "password": "Baldy1"},
        "katie": {"email": "b@b.com", "password": "k8t"},
        "yul": {"email": "c@c.com", "password": "etc"}
    }
    print(flask_login("david", "a@a.com", "Baldy1", logins))
    print(flask_login("david", "a@a.com", "wrong", logins))
    print(flask_login("foo", "bar", "baz", logins)) 