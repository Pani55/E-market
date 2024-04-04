import pytest
from src.product import Product, LawnGrass
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
    assert Category.count_of_categories == 1
    assert Category.count_of_unique_goods == 1


def test_get_goods(clothe):
    assert clothe.get_goods == 'pants, 599.99 руб. Остаток: 155 шт.\n'


def test_add_product(clothe, pants):
    grass = LawnGrass('a', 'b', 10, 5,
                      'r', 'R', 12)
    clothe.add_product(pants)
    clothe.add_product(grass)
    assert clothe.count_of_unique_goods == 3


def test___len__(clothe):
    assert len(clothe) == 1


def test_calc_average_price(clothe, pants):
    exp = Product('name', 'descr', 100, 10)
    cat = Category('name', 'descr', [])
    assert clothe.calc_average_price() == 599.99
    clothe.add_product(exp)
    assert clothe.calc_average_price() == 349.995
    assert cat.calc_average_price() == 0

