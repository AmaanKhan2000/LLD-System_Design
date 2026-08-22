from discount_strategy import DiscountStrategy

class DiscountService:
    def __init__(self):
        self._disc_type = None

    def set_strategy(self, discount: DiscountStrategy):
        self._disc_type = discount
        self.process()

    def process(self):
        self._disc_type.calculate_discount()        