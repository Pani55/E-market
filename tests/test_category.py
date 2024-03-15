import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def pants():
    return Product("pants", "green", 599.99, 155)


@pytest.fixture
def clothe(pants):
    return Category("clothes", "red", [pants])


def test_class_category(clothe, pants):
    assert clothe.name == 'clothes'
    assert clothe.description == 'red'
    assert clothe.goods[0] == pants
    assert Category.count_of_categories == 1
    assert Category.count_of_unique_goods == 1