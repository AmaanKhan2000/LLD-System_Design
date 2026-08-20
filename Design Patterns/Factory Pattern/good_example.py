from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza")

class Burger(Food):
    def prepare(self):
        print("Preparing Burger")

class Pasta(Food):
    def prepare(self):
        print("Preparing Pasta")

class FoodFactory:
    @staticmethod
    def create_food(food_type: str) -> Food:
        if food_type == "pizza":
            return Pizza()
        elif food_type == "burger":
            return Burger()
        elif food_type == "pasta":
            return Pasta()
        else:
            return None


class RestaurantService:
    def create_order(self, food_type:str):
        f = FoodFactory.create_food(food_type)
        if f is None:
            return None
        f.prepare()
        return f

 
        

        

