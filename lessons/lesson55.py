import os

# Directory and file operations
def list_dir(path="."):
    print(os.listdir(path))
    return os.listdir(path)

def make_dir(name):
    os.mkdir(name)
    print(f"Created directory: {name}")

def rename_file(src, dst):
    os.rename(src, dst)
    print(f"Renamed {src} to {dst}")

# To-do list manager (simplified for testability)
class ToDoList55:
    def __init__(self):
        self.todoList = []
    def add(self, task, due, priority):
        row = [task, due, priority.capitalize()]
        self.todoList.append(row)
        print("Thanks, this task has been added.")
    def view(self, option, prio=None):
        if option == "all":
            for row in self.todoList:
                print(row)
        elif option == "priority":
            for row in self.todoList:
                if row[2] == prio:
                    print(row)
    def edit(self, editTask, editInfo, changedTo):
        for row in self.todoList:
            for items in row:
                if editTask in items:
                    if editInfo == "name":
                        row[0] = changedTo
                    elif editInfo == "due":
                        row[1] = changedTo
                    elif editInfo == "priority":
                        row[2] = changedTo
                    print("")
                    return
        print("no such task :)")
    def remove(self, removeTask):
        for row in self.todoList:
            if removeTask in row:
                print("removed successfully")
                self.todoList.remove(row)
                return
    def prettyPrint(self):
        print()
        for row in self.todoList:
            print(row)
        print()

if __name__ == "__main__":
    # Directory and file operations (commented out for safety)
    # list_dir()
    # make_dir("HelloTest")
    # rename_file("test.txt", "test_renamed.txt")
    todo = ToDoList55()
    todo.add("Task1", "Tomorrow", "High")
    todo.view("all")
    todo.edit("Task1", "name", "Task1-Edited")
    todo.remove("Task1-Edited")
    todo.prettyPrint() 