import ast

class PizzaOrders:
    def __init__(self):
        self.pizza = []
    def load(self, file_obj):
        try:
            file_obj.seek(0)
            self.pizza = ast.literal_eval(file_obj.read())
        except Exception as err:
            print("ERROR: Unable to load")
            print(err)
    def save(self, file_obj):
        file_obj.seek(0)
        file_obj.truncate(0)
        file_obj.write(str(self.pizza))
        file_obj.seek(0)
    def add(self, nbPizza, nbSize, name):
        cost = nbPizza * nbSize
        self.pizza.append([name, nbPizza, nbSize, cost])
        print(f"Thanks {name}, your pizzas will cost {cost}")
    def view(self):
        for items in self.pizza:
            print(items)

if __name__ == "__main__":
    from io import StringIO
    f = StringIO("[]")
    orders = PizzaOrders()
    orders.load(f)
    orders.add(2, 10, "Alice")
    orders.save(f)
    orders.view() 