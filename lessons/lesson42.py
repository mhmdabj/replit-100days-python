def colorChange(color):
    if color == "Fire":
        print("\033[31m")
    elif color == "Air":
        print("\033[0m")
    elif color == "Water":
        print("\033[34m")
    elif color == "Earth":
        print("\033[32m")
    elif color == "Spirit":
        print("\033[35m")

def fill_beast_dic(beast_name, type_, special_move, hp, mp):
    beastDic = {
        "Beast Name": beast_name.strip().title(),
        "Type": type_.strip().title(),
        "Speical Move": special_move.strip().title(),
        "HP": hp.strip().title(),
        "MP": mp.strip().title()
    }
    for name, value in beastDic.items():
        if name.lower() == "type":
            colorChange(value)
        print(f"{name:<15}: {value}")
    return beastDic

if __name__ == "__main__":
    fill_beast_dic("dragon", "Fire", "Roar", "100", "50") 