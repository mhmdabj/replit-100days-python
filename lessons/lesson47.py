import random

class TopTrumps:
    def __init__(self):
        self.cards = {}
    def add_card(self, name, intelligence, handsomeness, skills, baldness):
        self.cards[name] = {
            "Intelligence": int(intelligence),
            "Handsomeness": int(handsomeness),
            "L33t c0ding skillz": int(skills),
            "Baldness level": int(baldness)
        }
    def choose_card(self, name):
        return self.cards[name]
    def compare_stats(self, user, comp, stat):
        user_val = self.cards[user][stat]
        comp_val = self.cards[comp][stat]
        print(f"{user}: {user_val}")
        print(f"{comp}: {comp_val}")
        if user_val > comp_val:
            print(f"{user} wins")
        elif user_val < comp_val:
            print(f"{comp} wins")
        else:
            print("Draw")

if __name__ == "__main__":
    game = TopTrumps()
    game.add_card("David", 178, 99, 80, 99)
    game.add_card("Spock", 200, 50, 50, 0)
    user = "David"
    comp = "Spock"
    stat = "Intelligence"
    game.compare_stats(user, comp, stat) 