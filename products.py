
class Product:
    """ Represents a product that can be purchased. """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

        if not name or price < 0 or quantity < 0:
            raise ValueError("Name can not be empty, price and quantity can not be negative.")

        if self.quantity == 0:
            self.deactivate()

    def get_quantity(self) -> int:
        """
        Getter function for quantity.
        Returns the quantity (int).
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Setter function for quantity.
        If quantity reaches 0, deactivates the product.
        """
        if quantity < 0:
            raise ValueError("Quantity can not be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Getter function for active.
        Returns True if the product is active, otherwise False.
        """
        return self.active

    def activate(self):
        """ Activates the product. """
        self.active = True

    def deactivate(self):
        """ Deactivates the product. """
        self.active = False

    def get_promotion(self):
        """
        Getter function for promotion.
        Returns promotion for product, if conditions fit.
        """
        return self.promotion

    def set_promotion(self, promotion):
        """
        Setter function for promotion.
        Assign a promotion to a product.
        """
        self.promotion = promotion

    def show(self) -> str:
        """ Returns a string that represents the product. """
        if self.promotion:
            promo = self.promotion.name
        else:
            promo = None

        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Promotion: {promo}"

    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        """
        if quantity < 0:
            raise ValueError("Quantity can not be negative.")
        if quantity > self.quantity:
            raise ValueError("Requested quantity is not available.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self.price, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price


class NonStockedProduct(Product):
    """ Represents a product with unlimited availability, quantity always stays 0. """
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.active = True

    def get_quantity(self) -> int:
        """ Returns 0 due unlimited quantity. """
        return 0

    def set_quantity(self, quantity):
        """ Raises an error when changing quantity. """
        raise NotImplementedError("NonStockedProduct doe not allow quantity changes.")

    def show(self) -> str:
        """ Overrides show method to return a string that represents the product. """
        if self.promotion:
            promo = self.promotion.name
        else:
            promo = None

        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited, Promotion: {promo}"

    def buy(self, quantity) -> float:
        """ Overrides buy method to enforce unlimited quantity of a product when purchased. """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if self.promotion:
            return self.promotion.apply_promotion(self.price, quantity)
        return self.price * quantity


class LimitedProduct(Product):
    """ Represents a product that can only be purchased up to a specified limit per order. """
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.active = True
        self.maximum = maximum

    def show(self) -> str:
        """ Overrides show method to return a string that represents the product. """
        if self.promotion:
            promo = self.promotion.name
        else:
            promo = None

        return f"{self.name}, Price: ${self.price}, Limited to 1 per order!, Promotion: {promo}"

    def buy(self, quantity) -> float:
        """ Overrides buy method to enforce limit of a product when purchased. """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.maximum:
            raise ValueError(f"It is only possible to purchase up to {self.maximum} units in one order.")

        return super().buy(quantity)

