class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """
        Функция является геттером

        :return: Возвращает цену
        """

        return self.__price

    @price.setter
    def price(self, new_price: float):
        """
        Функция является сеттером

        :param new_price: Новая цена
        :return: возвращает Новую цену / Оставляет цену нетронутой при несоблюдённом условии
        """

        if new_price <= 0:
            print("Введена некорректная цена")
        else:
            self.__price = new_price

    @price.deleter
    def price(self):
        """
        Функция является деллитером

        :return: Ничего не возвращает
        """

        print('Цена приведена к нулю!')
        self.__price = 0

    @classmethod
    def add_product(cls, name, descr, price, quantity):
        """
        Классовый метод, нужен для создания экземпляра

        :param name: Название товара
        :param descr: Описание товара
        :param price: Цена товара
        :param quantity: Кол-во товара в наличии

        :return: Возвращает экземпляр, готовый к добавлению в список товаров
        """

        object_ = Product(name, descr, price, quantity)

        return object_
