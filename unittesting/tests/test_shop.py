import pytest

from shop import Shop, Product


@pytest.fixture
def shop():
    """Returns Shop with no products"""
    return Shop()

@pytest.fixture
def shop_product():
    """Returns Shop with one product"""
    return Shop(Product("Book", 100, 5))

@pytest.fixture
def shop_list():
    """Returns Shop with three products"""
    products = []
    products.append(Product("Book", 100, 5))
    products.append(Product("Pen", 10, 25))
    products.append(Product("Notebook", 35, 4))
    return Shop(products)


def test_start_money(shop):
    assert shop.money == .0

def test_init_empty(shop):
    assert len(shop.products) == 0

def test_init_one_product(shop_product):
    assert len(shop_product.products) == 1

def test_init_list_product(shop_list):
    assert len(shop_list.products) == 3

def test_add_product(shop):
    product = Product("Pen", 10)
    shop.add_product(product)
    assert product in shop.products

def test_sell_one_product(shop_product):
    assert shop_product.sell_product("Book") == 100

def test_sell_few_product(shop_product):
    assert shop_product.sell_product("Book", 5) == 500

def test_sell_product_no_exists(shop_product):
    assert shop_product.sell_product("Pen") is None

def test_sell_product_error(shop_product):
    with pytest.raises(ValueError):
        shop_product.sell_product("Book", 6)

def test_products_length_after_sell(shop_product):
    shop_product.sell_product("Book", 5)
    assert len(shop_product.products) == 0

def test_money_after_sell(shop_product):
    shop_product.sell_product("Book", 5)
    assert shop_product.money == 500

@pytest.mark.parametrize("to_add, to_sell, money, product_length", [
    (
        [
            Product("Book", 100, 5),
            Product("Pen", 10, 25),
            Product("Notebook", 35, 4),
        ],
        [
            ("Book", 3),
            ("Pen", 25),
            ("Notebook", 2),
        ],
        620,
        2,
    ),
    (
        [
            Product("Book", 100, 5),
            Product("Pen", 10, 25),
        ],
        [
            ("Book", 5),
            ("Pen", 25),
        ],
        750,
        0,
    ),
    (
        [
            Product("Pen", 10, 50),
        ],
        [
            ("Pen", 25),
        ],
        250,
        1,
    ),
])
def test_transactions(shop, to_add, to_sell, money, product_length):
    for product in to_add:
        shop.add_product(product)
    for product in to_sell:
        shop.sell_product(product[0], product[1])
    errors = []
    if shop.money != money:
        errors.append("error in summarizing money")
    if len(shop.products) != product_length:
        errors.append("error in counting products length")
    assert not errors, "errors occured:\n{}".format("\n".join(errors))

@pytest.mark.parametrize("product_name, result", [
    ("Book", 0),
    ("Pen", 1),
    ("Notebook", 2),
    ("Not exists", None),
])
def test_get_product_index(shop_list, product_name, result):
    assert shop_list._get_product_index(product_name) == result
