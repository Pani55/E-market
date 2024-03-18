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
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Введена некорректная цена")
        else:
            self.__price = new_price

    @classmethod
    def add_product(cls, name, descr, price, quantity):
        object_ = Product(name, descr, price, quantity)

        return object_
