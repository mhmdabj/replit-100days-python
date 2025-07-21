import random
from io import StringIO

def add_idea(file_obj, idea):
    file_obj.write(f"{idea}\n")
    print("Nice! Your idea has been stored.")

def get_random_idea(file_obj, seed=None):
    file_obj.seek(0)
    contents = file_obj.read().split()
    if not contents:
        print("No Ideas available")
        return None
    if seed is not None:
        random.seed(seed)
    randomIdea = random.choice(contents)
    print(randomIdea)
    return randomIdea

if __name__ == "__main__":
    f = StringIO()
    add_idea(f, "Build a rocket")
    add_idea(f, "Learn Python")
    get_random_idea(f, seed=42) 