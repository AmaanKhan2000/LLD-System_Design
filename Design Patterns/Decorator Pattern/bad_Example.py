from abc import ABC, abstractmethod

class Beverage(ABC):
    def get_description():
        pass
    def get_cost():
        pass

class Coffee(Beverage):
    def get_cost(self):
        return 20
    def get_description(self):
        return "Coffee"


class CoffeeWithMilk(Coffee):
    def get_cost(self):
        return 30
    def get_description(self):
        return "Coffee with milk"

coffee1 = Coffee()
print(coffee1.get_description())
print(coffee1.get_cost())

coffee1 = CoffeeWithMilk()
print(coffee1.get_description())
print(coffee1.get_cost())   

    