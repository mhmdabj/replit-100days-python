

def his_star_wars_name(all_input):
    first = all_input[0].strip()
    last = all_input[1].strip()
    maiden = all_input[2].strip()
    city = all_input[3].strip()
    name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"
    return name

if __name__ == "__main__":
    print(his_star_wars_name(["David", "Morgan", "Jones", "Cardiff"])) 