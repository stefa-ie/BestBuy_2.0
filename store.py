
class Store:
    def __init__(self, products: list):
        self.products = products


    def add_product(self, product):
        """ Adds a product to the store. """
        self.products.append(product)


    def remove_product(self, product):
        """ Removes a product from store. """
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        """ Returns how many items are in the store in total. """
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total


    def get_all_products(self) -> list:
        """ Returns all products in the store that are active. """
        return self.products


    def order(self, shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if quantity < 0:
                raise ValueError("Quantity can not be negative.")
            total_price += product.buy(quantity)
        return total_price

