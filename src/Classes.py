class Category:
    name: str
    description: str
    goods: list

    count_of_categories = 0
    count_of_unique_goods = 0

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.goods}"

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
