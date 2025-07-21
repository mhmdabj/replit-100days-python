from io import StringIO

def find_leader(file_obj):
    max_number = 0
    text = ""
    file_obj.seek(0)
    while True:
        contents = file_obj.readline().strip()
        if contents == "":
            break
        parts = contents.split()
        if len(parts) < 2:
            continue
        try:
            score = int(parts[1])
        except Exception:
            continue
        if max_number < score:
            max_number = score
            text = parts[0]
    print(f"Current leader is {text} {max_number}")
    return text, max_number

if __name__ == "__main__":
    f = StringIO("AB 100\nCD 200\n")
    find_leader(f) 