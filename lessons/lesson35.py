class ToDoManager:
    def __init__(self):
        self.myList = []
    def add(self, task):
        if task not in self.myList:
            self.myList.append(task)
            print(f"Added: {task}")
        else:
            print(f"{task} is already in your list 🤓")
    def view(self):
        for item in self.myList:
            print(f"{item} \n")
    def edit(self, old, new):
        if old in self.myList:
            for i in range(len(self.myList)):
                if self.myList[i] == old:
                    self.myList[i] = new
        else:
            print("This is a new task I dont recognize..")
    def remove(self, task, confirm=True):
        if task in self.myList:
            if confirm:
                self.myList.remove(task)
                print(f"{task} is removed")
            else:
                print("Ok")
        else:
            print("This is a new task I dont recognize..")
    def clear(self):
        self.myList = []
        print("Your List is clear")

def simulate_manager(actions):
    manager = ToDoManager()
    for action in actions:
        if action[0] == "add":
            manager.add(action[1])
        elif action[0] == "view":
            manager.view()
        elif action[0] == "edit":
            manager.edit(action[1], action[2])
        elif action[0] == "remove":
            manager.remove(action[1], action[2])
        elif action[0] == "clear":
            manager.clear()

if __name__ == "__main__":
    simulate_manager([
        ("add", "Task1"),
        ("add", "Task2"),
        ("view", None),
        ("edit", "Task1", "Task1-Edited"),
        ("remove", "Task2", True),
        ("clear", None)
    ]) 