class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

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


    def show(self) -> str:
        """ Returns a string that represents the product. """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"


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

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price
