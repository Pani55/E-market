import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def pants():
    return Product("pants", "green", 599.99, 155)


@pytest.fixture
def clothe(pants):
    return Category("clothes", "red", [pants.name])


def test_class_category(clothe):
    assert clothe.name == 'clothes'
    assert clothe.description == 'red'
    assert clothe.goods == ['pants']
    assert Category.count_of_categories == 1
    assert Category.count_of_unique_goods == 1


def test_class_product(pants):
    assert pants.name == 'pants'
    assert pants.description == 'green'
    assert pants.price == 599.99
    assert pants.quantity == 155
