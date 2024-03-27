class Product:


    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.__price}, {self.quantity}"

    def __init__(self, name: str, description: str, price: float, quantity: int, color=None):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

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
    def add_product(cls, *args):
        """
        Классовый метод, нужен для создания экземпляра

        :return: Возвращает экземпляр, готовый к добавлению в список товаров
        """

        object_ = Product(args[0], args[1], args[2], args[3])

        return object_


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, color, performance: int, model: str, memory_capacity: int):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity


class Lawn_grass(Product):

    def __init__(self, name, description, price, quantity, color, manufacturer_country: str, germination_period: float):
        super().__init__(name, description, price, quantity, color)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
