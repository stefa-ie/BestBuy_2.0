import products
from abc import abstractmethod

class Promotion:
    """ Abstract base class for promotions. """
    @abstractmethod
    def apply_promotion(self, price, quantity) -> float:
        pass


class PercentDiscount(Promotion):
    """ Gives percentage discount to price. """
    def __init__(self, discount):
        self.discount = discount / 100

    def apply_promotion(self, price, quantity) -> float:
        return price * quantity * (1 - self.discount)


class SecondHalfPrice(Promotion):
    """ Gives 50% discount on every second item. """
    def apply_promotion(self, price, quantity) -> float:
        half_price_items = quantity // 2
        full_price_items =  quantity - half_price_items
        return price * full_price_items + price / 2 *half_price_items


class SecondOneFree(Promotion):
    """ Gives one item for free, when two were bought. """
    def apply_promotion(self, price, quantity) -> float:
        quantity_to_pay = (quantity + 1) // 2
        return price * quantity_to_pay

class ThirdOneFree(Promotion):
    """ Gives one item for free, when three were bought. """
    def apply_promotion(self, price, quantity) -> float:
        quantity_to_pay = (quantity + 2) // 3
        return price * quantity_to_pay