import ast

class LifeOrganizer51:
    def __init__(self):
        self.todoList = []
    def load(self, file_obj):
        file_obj.seek(0)
        self.todoList = ast.literal_eval(file_obj.read())
    def save(self, file_obj):
        file_obj.seek(0)
        file_obj.truncate(0)
        file_obj.write(str(self.todoList))
        file_obj.seek(0)
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
    from io import StringIO
    f = StringIO("[]")
    org = LifeOrganizer51()
    org.load(f)
    org.add("Task1", "Tomorrow", "High")
    org.save(f)
    org.view("all")
    org.edit("Task1", "name", "Task1-Edited")
    org.remove("Task1-Edited")
    org.save(f)
    org.view("all") 