from discount_service import DiscountService
from diwali import Diwali
from bonanza import Bonanza
from first_order import FirstOrder


ds = DiscountService()
ds.set_strategy(Diwali())
ds.set_strategy()