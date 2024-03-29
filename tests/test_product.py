import pytest
from src.product import Product


@pytest.fixture
def pants():
    return Product("pants", "green", 599.99, 155)


def test_class_product(pants):
    assert pants.name == 'pants'
    assert pants.description == 'green'
    assert pants.price == 599.99
    assert pants.quantity == 155


def test_price_getter(pants):
    assert pants.price == 599.99


def test_price_setter(pants):
    pants.price = 155
    assert pants.price == 155
    pants.price = 0
    assert pants.price == 155


def test_price_deleter(pants):
    assert pants.price == 599.99
    del pants.price
    assert pants.price == 0


def test_add_product():
    circle = Product.add_product(name='circle', description='big', price=200, quantity=50)
    assert circle.price == 200


def test___add__(pants):
    circle = Product.add_product(name='circle', description='big', price=200, quantity=50)
    assert pants + circle == 102998.45
