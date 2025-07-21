class EmailSpammer:
    def __init__(self):
        self.listOfEmail = []
    def add(self, email):
        self.listOfEmail.append(email)
    def remove(self, email):
        if email in self.listOfEmail:
            self.listOfEmail.remove(email)
    def show(self):
        print("listofEmail")
        for index in range(len(self.listOfEmail)):
            print(f"{index}: {self.listOfEmail[index]}")
    def spam(self, max_count):
        print("Spam Email 1by1:")
        for i in range(0, min(max_count, len(self.listOfEmail))):
            print(f"""
    Dear {self.listOfEmail[i]}
    It has come to our attention that you're missing out on the amazing Replit 100 days of code.
    We insist you do it right away.
    If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat.
    We might just do that anyway.

    Love and hugs,
    Ian Spammington III
    """)

def simulate_spammer(actions):
    spammer = EmailSpammer()
    for action in actions:
        if action[0] == "add":
            spammer.add(action[1])
        elif action[0] == "remove":
            spammer.remove(action[1])
        elif action[0] == "show":
            spammer.show()
        elif action[0] == "spam":
            spammer.spam(action[1])

if __name__ == "__main__":
    simulate_spammer([
        ("add", "a@example.com"),
        ("add", "b@example.com"),
        ("show", None),
        ("spam", 2),
        ("remove", "a@example.com"),
        ("show", None)
    ]) 