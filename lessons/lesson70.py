def check_login(username, password, env):
    if username == env['adminUsername'] and password == env['adminPassword']:
        print("Welcome Admin")
        return "admin"
    elif username == env['username'] and password == env['password']:
        print("Welcome Normy")
        return "normy"
    else:
        print("Try again")
        return None

if __name__ == "__main__":
    env = {
        'adminUsername': 'admin',
        'adminPassword': 'adminpass',
        'username': 'user',
        'password': 'userpass'
    }
    check_login('admin', 'adminpass', env)
    check_login('user', 'userpass', env)
    check_login('foo', 'bar', env) 