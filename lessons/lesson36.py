def add_names(name_pairs):
    nameList = []
    for first_name, last_name in name_pairs:
        first = first_name.strip().capitalize()
        last = last_name.strip().capitalize()
        name = f"{first} {last}"
        if name not in nameList:
            nameList.append(name)
        else:
            print("ERROR: Duplicate name")
    print()
    for i in nameList:
        print(i)
    print()

if __name__ == "__main__":
    add_names([
        ("alice", "smith"),
        ("bob ", " jones"),
        ("alice", "smith")
    ]) 