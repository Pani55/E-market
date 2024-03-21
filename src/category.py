class Category:
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

        Category.count_of_categories += 1
        Category.count_of_unique_goods += len(self.__goods)

    def add_product(self, product):
        """
        Функция добавляет продукт в список товаров.
        """

        self.__goods.append(product)

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
