from discount_strategy import DiscountStrategy

class FirstOrder(DiscountStrategy):
    def calculate_discount(self):
        print("The discount is 50%")