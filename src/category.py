from src.product import Product
from src.classmixin import ClassMixin


class Category(ClassMixin):
    count_of_categories = 0
    count_of_unique_goods = 0

    def __len__(self):
        return len(self.__goods)

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.__goods.__len__()} шт."

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.__goods}"

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods

        if type(self) is Category:
            super().print_repr()

        Category.count_of_categories += 1
        Category.count_of_unique_goods += len(self.__goods)

    def add_product(self, product):
        """
        Функция добавляет продукт в список товаров.
        """
        if product.quantity <= 0:
            raise ValueError('Нельзя добавить товар с нулевым количеством!')
        elif isinstance(product, Product):
            self.__goods.append(product)
            Category.count_of_unique_goods += 1
        else:
            raise TypeError("Нельзя добавлять экзэмпляр не класса Product или его подклассов")

    @property
    def get_goods(self):
        """
        Функция является геттером

        :return: Возвращает список продуктов в читаемом формате
        """

        result = ''
        for product in self.__goods:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'

        return result

    def calc_average_price(self):
        summ = 0
        try:
            for i in self.__goods:
                summ += i.price
            return summ / len(self)
        except ZeroDivisionError:
            print('В категории нет товаров!')
            return 0
