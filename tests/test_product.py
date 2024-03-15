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
