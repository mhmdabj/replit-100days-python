class ToDoList:
    def __init__(self):
        self.myList = []
    def add(self, item):
        self.myList.append(item)
    def remove(self, item):
        if item in self.myList:
            self.myList.remove(item)
            print(f"{item} is removed")
        else:
            print(f"{item} was not in the list")
    def view(self):
        for item in self.myList:
            print(f"{item} \n")

def simulate_todo(actions):
    todo = ToDoList()
    for action in actions:
        if action[0] == "add":
            todo.add(action[1])
        elif action[0] == "remove":
            todo.remove(action[1])
        elif action[0] == "view":
            todo.view()

if __name__ == "__main__":
    simulate_todo([
        ("add", "Task1"),
        ("add", "Task2"),
        ("view", None),
        ("remove", "Task1"),
        ("view", None)
    ]) 