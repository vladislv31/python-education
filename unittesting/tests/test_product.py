import pytest

from shop import Product


@pytest.fixture
def product():
    """Returns Book with:
    - name: "Book"
    - price: 100
    - quantity: 1
    """
    return Product("Book", 100)

@pytest.fixture
def product_multiple():
    """Returns Book with:
    - name: "Book"
    - price: 100
    - quantity: 5
    """
    return Product("Book", 100, 5)


def test_no_init_quantity(product):
    assert product.quantity == 1

def test_init_quantity(product_multiple):
    assert product_multiple.quantity == 5

def test_subtract_one_quantity(product):
    product.subtract_quantity()
    assert product.quantity == 0

def test_subtract_quantity(product_multiple):
    product_multiple.subtract_quantity(5)
    assert product_multiple.quantity == 0

def test_add_one_quantity(product):
    product.add_quantity()
    assert product.quantity == 2

def test_add_quantity(product_multiple):
    product_multiple.add_quantity(5)
    assert product_multiple.quantity == 10

@pytest.mark.parametrize("add, subtract, expected", [
    (6, 3, 4),
    (10, 10, 1),
    (7, 0, 8),
    (15, 6, 10),
    (2, 2, 1),
])
def test_transactions(product, add, subtract, expected):
    product.add_quantity(add)
    product.subtract_quantity(subtract)
    assert product.quantity == expected

@pytest.mark.parametrize("price", [
    (100),
    (133),
    (0),
    (11),
    (5),
])
def test_change_price(product, price):
    product.change_price(price)
    assert product.price == price