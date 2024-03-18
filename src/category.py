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
        """
        Функция добавляет продукт в список товаров.

        :return: Возвращает обновлённый список товаров
        """

        if product not in self.__goods:
            self.__goods.append(product)
        return self.__goods

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
