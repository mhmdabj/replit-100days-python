from io import StringIO

def add_score(file_obj, initials, score):
    file_obj.write(f"{initials} -> {score} \n")
    print("Added to high score table.")

def add_scores_interactive(file_obj, scores):
    for initials, score in scores:
        add_score(file_obj, initials, score)
        
    file_obj.seek(0)
    return file_obj

if __name__ == "__main__":
    f = StringIO()
    add_scores_interactive(f, [("AB", 100), ("CD", 200)])
    print(f.getvalue()) 