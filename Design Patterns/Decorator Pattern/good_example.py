from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def get_description(self):
        pass
    @abstractmethod
    def get_cost(self):
        pass

class Coffee(Beverage):
    def get_cost(self):
        return 20
    def get_description(self):
        return "Coffee"


class AddOnDecorator(Beverage):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    def get_cost():
        pass
    def get_description():
        pass

class CoffeeWithMilkDecorator(AddOnDecorator):
    def get_description(self):
        return self._coffee.get_description() + "+ Milk"
    def get_cost(self):
        return self._coffee.get_cost() + 10

coffee = Coffee()
coffee_milk = CoffeeWithMilkDecorator(coffee)

print(coffee.get_cost())
print(coffee.get_description())

print(coffee_milk.get_description())
print(coffee_milk.get_cost())
                

    