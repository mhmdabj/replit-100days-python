class ClueGame:
    def __init__(self):
        self.clue = {}
    def add(self, name, location, weapon):
        self.clue[name] = {"location": location, "weapon": weapon}
    def prettyPrint(self):
        print()
        for key, value in self.clue.items():
            print(key, end=": ")
            for subKey, subValue in value.items():
                print(subKey, subValue, end=" | ")
            print()

class Mokedex:
    def __init__(self):
        self.mokedex = {}
    def add(self, name, type_, move, hp, mp):
        self.mokedex[name] = {"Type": type_, "Special Move": move, "HP": hp, "MP": mp}
    def prettyPrint(self):
        for key, value in self.mokedex.items():
            print(key, end=": ")
            for subKey, subValue in value.items():
                print(subKey, subValue, end=" | ")
            print()

if __name__ == "__main__":
    game = ClueGame()
    game.add("Alice", "Library", "Candlestick")
    game.prettyPrint()
    m = Mokedex()
    m.add("Pikachu", "Electric", "Thunderbolt", "35", "55")
    m.prettyPrint() 