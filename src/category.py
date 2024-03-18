from product import Product


class Category:
    name: str
    description: str
    __goods: list

    count_of_categories = 0
    count_of_unique_goods = 0

    def __repr__(self):
        return f"Категория: {self.name}, Описание: {self.description}, Товары: {self.__goods}"

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.count_of_categories += 1
        Category.count_of_unique_goods += len(self.__goods)

    def add_goods(self, product):
        if product not in self.__goods:
            self.__goods.append(product)
        return self.__goods

    @property
    def get_goods(self):
        result = ''
        for product in self.__goods:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'

        return result

# prod_3 = Product.add_product('name3', 'descr3', 123, 10)
# test_prod_2 = Product('name2', 'descr2', 50, 55)
# test_prod = Product('name1', 'descr1', 10, 5)
# test_cat = Category('test', 'test_descr', [test_prod])
# print(test_cat.get_goods)
# print(test_cat)
# test_cat.add_goods(prod_3)
# print(test_cat.get_goods)
