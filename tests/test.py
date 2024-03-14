import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def clothe():
    return Category("clothes", "red", ["T-short"])


@pytest.fixture
def pants():
    return Product("pants", "green", 599.99, 155)


def test_class_category(clothe):
    assert clothe.name == 'clothes'
    assert clothe.description == 'red'
    assert clothe.goods == ['T-short']


def test_class_product(pants):
    assert pants.name == 'pants'
    assert pants.description == 'green'
    assert pants.price == 599.99
    assert pants.quantity == 155
