import pytest
import products
import promotions


def test_normal_product():
    """ Tests that creating a normal product works. """
    product = products.Product("Boom Box Big", price=145, quantity=500)
    assert product.name == "Boom Box Big"
    assert product.price == 145
    assert product.quantity == 500


def test_empty_name():
    """ Tests that creating a product with empty name, invokes an exception. """
    with pytest.raises(ValueError, match="Name can not be empty, price and quantity can not be negative."):
        products.Product("", price=1450, quantity=100)


def test_negative_price():
    """ Tests that creating a product with negative price invokes an exception. """
    with pytest.raises(ValueError, match="Name can not be empty, price and quantity can not be negative."):
        products.Product("MacBook Air M2", price=-10, quantity=100)


def test_inactive_when_zero_quantity():
    """ Tests that when a product reaches 0 quantity, it becomes inactive. """
    product = products.Product("Boom Box Small", price=80, quantity=0)
    assert product.get_quantity() == 0
    assert product.is_active() is False


def test_purchase_modifies_quantity():
    """ Tests that product purchase modifies the quantity and returns the right output. """
    product = products.Product("Boom Box Mini", price=50, quantity=250)
    product.buy(8)
    assert product.get_quantity() == 242


def test_buy_larger_quantity():
    """ Tests that buying a larger quantity than exists invokes exception. """
    with pytest.raises(ValueError, match="Requested quantity is not available."):
        product = products.Product("Boom Box Mini", price=50, quantity=250)
        product.buy(300)

