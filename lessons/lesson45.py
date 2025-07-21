class LifeOrganizer:
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

def simulate_life_organizer(actions):
    organizer = LifeOrganizer()
    for action in actions:
        if action[0] == "add":
            organizer.add(action[1], action[2], action[3])
        elif action[0] == "view":
            if len(action) == 2:
                organizer.view(action[1])
            else:
                organizer.view(action[1], action[2])
        elif action[0] == "edit":
            organizer.edit(action[1], action[2], action[3])
        elif action[0] == "remove":
            organizer.remove(action[1])
        elif action[0] == "print":
            organizer.prettyPrint()

if __name__ == "__main__":
    simulate_life_organizer([
        ("add", "Task1", "Tomorrow", "High"),
        ("add", "Task2", "Next Week", "Low"),
        ("view", "all"),
        ("edit", "Task1", "name", "Task1-Edited"),
        ("remove", "Task2"),
        ("print",),
    ]) 